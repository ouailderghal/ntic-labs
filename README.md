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
