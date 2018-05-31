import os
import grp
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users_exist(host):

    global users
#    path = """/home/users/carlos/ansible-playbooks/
#           roles/users/molecule/default/tests/users_list"""
#    users = eval(host.file('tests/user_list').content_string)
    users = ['aj', 'carlos', 'tom', 'rob', 'tejinder']
    for user in users:
        u = host.user(user)
        assert u.uid >= 0


def test_users_home_dir(host):

    print(users)
    for user in users:
        f = host.file('/home/users/'+user)
        assert f.exists
        assert f.user == user
        assert f.group == user


def test_users_ssh(host):

    for user in users:
        f = host.file('/home/users/'+user+'/.ssh/')
        assert f.exists
        assert f.user == user
        assert f.group == user


def test_users_belong_admin_group(host):

    for user in users:
        groups = host.user(user).groups
        assert len(list(set(groups).intersection(['sysadmins']))) == 1


def test_sudoer_cotains_admin_group(host):

    f = host.file('/etc/sudoers.d/sysadmins')
    assert f.exists
    assert ('%sysadmins ALL=(ALL)       NOPASSWD: ALL') in f.content_string


def test_no_other_users(host):

    for p in grp.getgrnam('sysadmins').gr_mem:
        assert len(list(set(users).intersection([p]))) == 1
