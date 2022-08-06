#!/bin/env python3
#
# Ansible passowrd generator helper script
#
# Author : Ouail Derghal <ouail.derghal@univ-constantine2.dz>
# GitLab : https://gitlab.com/ouailderghal1
#
# Generate encrypted password for users created from Ansible playbooks.
# Make sure that you have python3 and Bcrypt library installed on your system.
# Check out the README before running this script.
#


import crypt
import getpass

password = getpass.getpass();

print(crypt.crypt(password) if (password == getpass.getpass("Confirm: ")) else exit())

