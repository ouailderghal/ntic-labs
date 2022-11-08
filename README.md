# Laboratory machines configuration

This repository contains Ansible playbook files and documentation for setting up laboratory machines of the faculty
of new technologies, University of Constantine 2.

Please follow carefully this tutorial, make sure that you have a stable internet connection on both your host and the
machine(s) you want to set up.

## Generate automatic installation ISO

The distribution of choice is `Debian 11`, the installation process is fully automated. In order to prepare installation
ISO file, you need to use the custom image builder of the [FAI Project](https://fai-project.org/) tool. The goal of
using such tool is to automate the process of installation, and provide pre-downloaded common packages (such as OpenJDK)
out of the box after installation.

List of packages to feed to [FAI Image Builder](https://fai-project.org/FAIme/) is available under `fai/` directory.
You will find 2 package lists for the TTY (no GUI) version and the XFCE version. After the build is finished, you will
be notified via email with the download link of the custom ISO image.

The last step is to burn the ISO file on thumb drives; if you are using a GNU/Linux machine, you can use the commands
below :

```shell
lsblk # list connected devices
sudo dd if=fai.iso of=/dev/sdX status=progress bs=1M
```

If you are on a Windows machine, you can use [Rufus](https://rufus.ie/en/) to burn the ISO.

## Install Ansible

In order to install `Ansible` on your machine you have to execute the command bellow, this guide assumes that you are
running Debian or a Debian-based GNU/Linux distribution such as Ubuntu. It is also recommended to install a
terminal-based text editor such as `vim`.

```shell
sudo apt install -y ansible sshpass vim
```

After the installation is completed, you can check Ansible version by typing the command below. If you are
running `Debian 11`, you
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

```
Password: guest
Confirm: guest
$6$tKzqnzGe8soA9MBJ$LxRiSKU/UP.sC/Ozd/gzMUiWU/E0uV5tKnpvMQWswhxJ9iGyOOItOuZeOCr7IdEfTviHEt1gf7cdrJmzQ78tY/
```

## Generate SSH key

Administrators may need to access lab machines using `SSH`, it is better to use authentication with keys over
passwords. If you don't already have a key pair (public and private key), you can generate one by running the command
below. Replace the e-mail address with the admin address.

```shell
ssh-keygen -t ed25519 -C "admin@univ-constantine2.dz" -f ./ssh/id_ed25519
```

Password authentication over SSH is disabled, make sure to backup your private key on a thumb drive or print it on paper
(avoid saving your key on cloud storage).

If you want to generate more than one key pair for administrators, you can execute the previous command multiple times.
After that, you have to list all administrators public keys into `authorized_keys` located under `ssh/` directory.

```shell
cat ./ssh/id_ed25519.pub >> ./ssh/authorized_keys
```
