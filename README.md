# Ansible

Command lines

Check connetivity with the private servers through the Bastion:

    ansible private-servers -i hosts -m ping -u ec2-user

Execute aws creation playbooks:

    ansible-playbook -i hosts create_aws_private_instance.yml
