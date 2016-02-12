#!/usr/bin/env python
#----------------------------------------------------------
# ecore cli
#
# To install your ecore development environement type:
#
# wget -O- https://raw.githubusercontent.com/ecore/ecore/8.0/ecore.py | python
#
# The setup_* subcommands used to boostrap ecore are defined here inline and may
# only depends on the python 2.7 stdlib
#
# The rest of subcommands are defined in ecore/cli or in <module>/cli by
# subclassing the Command object
#
#----------------------------------------------------------
import os
import re
import sys
import subprocess

GIT_HOOKS_PRE_PUSH = """
#!/usr/bin/env python2
import re
import sys
if re.search('github.com[:/]ecore/ecore.git$', sys.argv[2]):
    print "Pushing to /ecore/ecore.git is forbidden, please push to ecore-dev, use --no-verify to override"
    sys.exit(1)
"""

def printf(f,*l):
    print "ecore:" + f % l

def run(*l):
    if isinstance(l[0], list):
        l = l[0]
    printf("running %s", " ".join(l))
    subprocess.check_call(l)

def git_locate():
    # Locate git dir
    # TODO add support for os.environ.get('GIT_DIR')

    # check for an ecore child
    if os.path.isfile('ecore/.git/config'):
        os.chdir('ecore')

    path = os.getcwd()
    while path != os.path.abspath(os.sep):
        gitconfig_path = os.path.join(path, '.git/config')
        if os.path.isfile(gitconfig_path):
            release_py = os.path.join(path, 'ecore/release.py')
            if os.path.isfile(release_py):
                break
        path = os.path.dirname(path)
    if path == os.path.abspath(os.sep):
        path = None
    return path

def cmd_setup_git():
    git_dir = git_locate()
    if git_dir:
        printf('git repo found at %s',git_dir)
    else:
        run("git", "init", "ecore")
        os.chdir('ecore')
        git_dir = os.getcwd()
    if git_dir:
        # push sane config for git < 2.0, and hooks
        #run('git','config','push.default','simple')
        # alias
        run('git','config','alias.st','status')
        # merge bzr style
        run('git','config','merge.commit','no')
        # pull let me choose between merge or rebase only works in git > 2.0, use an alias for 1
        run('git','config','pull.ff','only')
        run('git','config','alias.pl','pull --ff-only')
        pre_push_path = os.path.join(git_dir, '.git/hooks/pre-push')
        open(pre_push_path,'w').write(GIT_HOOKS_PRE_PUSH.strip())
        os.chmod(pre_push_path, 0755)
        # setup ecore remote
        run('git','config','remote.ecore.url','https://github.com/ecore/ecore.git')
        run('git','config','remote.ecore.pushurl','git@github.com:ecore/ecore.git')
        run('git','config','--add','remote.ecore.fetch','dummy')
        run('git','config','--unset-all','remote.ecore.fetch')
        run('git','config','--add','remote.ecore.fetch','+refs/heads/*:refs/remotes/ecore/*')
        # setup ecore-dev remote
        run('git','config','remote.ecore-dev.url','https://github.com/ecore-dev/ecore.git')
        run('git','config','remote.ecore-dev.pushurl','git@github.com:ecore-dev/ecore.git')
        run('git','remote','update')
        # setup 8.0 branch
        run('git','config','branch.8.0.remote','ecore')
        run('git','config','branch.8.0.merge','refs/heads/8.0')
        run('git','checkout','8.0')
    else:
        printf('no git repo found')

def cmd_setup_git_dev():
    git_dir = git_locate()
    if git_dir:
        # setup ecore-dev remote
        run('git','config','--add','remote.ecore-dev.fetch','dummy')
        run('git','config','--unset-all','remote.ecore-dev.fetch')
        run('git','config','--add','remote.ecore-dev.fetch','+refs/heads/*:refs/remotes/ecore-dev/*')
        run('git','config','--add','remote.ecore-dev.fetch','+refs/pull/*:refs/remotes/ecore-dev/pull/*')
        run('git','remote','update')

def cmd_setup_git_review():
    git_dir = git_locate()
    if git_dir:
        # setup ecore-dev remote
        run('git','config','--add','remote.ecore.fetch','dummy')
        run('git','config','--unset-all','remote.ecore.fetch')
        run('git','config','--add','remote.ecore.fetch','+refs/heads/*:refs/remotes/ecore/*')
        run('git','config','--add','remote.ecore.fetch','+refs/tags/*:refs/remotes/ecore/tags/*')
        run('git','config','--add','remote.ecore.fetch','+refs/pull/*:refs/remotes/ecore/pull/*')

def setup_deps_debian(git_dir):
    debian_control_path = os.path.join(git_dir, 'debian/control')
    debian_control = open(debian_control_path).read()
    debs = re.findall('python-[0-9a-z]+',debian_control)
    debs += ["postgresql"]
    proc = subprocess.Popen(['sudo','apt-get','install'] + debs, stdin=open('/dev/tty'))
    proc.communicate()

def cmd_setup_deps():
    git_dir = git_locate()
    if git_dir:
        if os.path.isfile('/etc/debian_version'):
            setup_deps_debian(git_dir)

def setup_pg_debian(git_dir):
    cmd = ['sudo','su','-','postgres','-c','createuser -s %s' % os.environ['USER']]
    subprocess.call(cmd)

def cmd_setup_pg():
    git_dir = git_locate()
    if git_dir:
        if os.path.isfile('/etc/debian_version'):
            setup_pg_debian(git_dir)

def cmd_setup():
    cmd_setup_git()
    cmd_setup_deps()
    cmd_setup_pg()

def main():
    # registry of commands
    g = globals()
    cmds = dict([(i[4:],g[i]) for i in g if i.startswith('cmd_')])
    # if curl URL | python2 then use command setup
    if len(sys.argv) == 1 and __file__ == '<stdin>':
        cmd_setup()
    elif len(sys.argv) == 2 and sys.argv[1] in cmds:
        cmds[sys.argv[1]]()
    else:
        import ecore
        ecore.cli.main()

if __name__ == "__main__":
    main()
