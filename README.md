# Laboratory machines configuration

This repository contains Ansible playbook files and documentation for setting up laboratory machines of the faculty 
of new technologies, University of Constantine 2.

Please follow carefully this tutorial, make sure that you have a stable internet connection on both your host and the 
machine(s) you want to set up.

## Install Ansible

In order to install `Ansible` on your machine you have to execute the command bellow, this guide assumes that you are
running Debian or a Debian-based GNU/Linux distribution such as Ubuntu. It is also recommended to install a
terminal-based text editor such as `vim`.

```shell
sudo apt install -y ansible vim
```

After the installation is completed, you can check Ansible version by typing the command below. If you are running `Debian 11`, you
should have version `2.10.8` available on your system.

## Generate encrypted password

When you create a new user, you are able to specify the password in an encrypted format. In order to generate the 
encrypted password from plain text, you need to have `Python` version 3 and `Bcrypt` library installed on your system.

```shell
sudo apt install -y python3 python3-bcrypt
```

After that, you have to run the helper script to generate the encrypted password :

```shell
$ python3 ./scripts/generate_pwd.py
```

You will be prompted to type the password and next to confirm it, if the two strings match you will get the
encrypted password.

```shell
Password: guest
Confirm: guest

$6$tKzqnzGe8soA9MBJ$LxRiSKU/UP.sC/Ozd/gzMUiWU/E0uV5tKnpvMQWswhxJ9iGyOOItOuZeOCr7IdEfTviHEt1gf7cdrJmzQ78tY/
```
