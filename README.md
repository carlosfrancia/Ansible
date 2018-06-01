# Ansible POC

Repository for Ansible proof of concepts.

## Roles

- aws: Role to manage AWS EC2 instances and Security Groups
- aws-private-instance: Role to create EC2 instances in a private subnet behind a NAT instance (Bastion)
- docker: ROle to install Docker software
- elasticsearch-docker: Role to deploy elasticsearch on a Docker container
- elk-docker: Role to deploy ELK stack on Docker containers
- filebeat: Role to install filebeat softare
- kibana-docker: Role to deploy Kiaban on a Docker container
- users: Role to create SSH users with sudo rights.
- users-extra-help: Users role plus task to restart a service after completion of a previous task. Molecule files (uncompleted)


## Command lines

Check connetivity with the private servers through the Bastion:

    ansible private-servers -i hosts -m ping -u ec2-user

Execute aws creation playbooks:

    ansible-playbook -i hosts create_aws_private_instance.yml
