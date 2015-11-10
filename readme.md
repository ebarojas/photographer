http://blog.smalleycreative.com/tutorials/setup-a-django-vm-with-vagrant-virtualbox-and-chef/

# Initial setup of Vagrant Base

# If it's a new project ->
Copy vagrantfile and /binfolder
Install Pip and Django
Install latest version of node.js
install bower + bootstrap

If not, download source from GitHub

vagrant up

...Insert password

This step only ever needs to be done once. Once the precise64 box is installed on a system the remaining steps refer to that same box regardless of the project.

On an Apple running OS X, download and install [Xcode from the Apple App Store](https://itunes.apple.com/us/app/xcode/id497799835?ls=1&mt=12). This is necessary to get some compilers and install Git on the host machine.

Download VirtualBox from http://www.virtualbox.org/wiki/Downloads, install the package.

Download Vagrant 2 or higher from http://downloads.vagrantup.com/, install the package.

Launch a Terminal window, check that it installed:

    (host) $ which vagrant

Add a Vagrant box (we'll be using Ubuntu Precise Pangolin (12.04 LTS) 64-bit):

    (host) $ vagrant box add precise64 http://files.vagrantup.com/precise64.box

# Using Vagrant with This Project

Make a directory for the project and change to it, replacing `<path_to>` with the path to the project and `<project_name>` with the name of the project.

    (host) $ mkdir <path_to>/<project_name> && cd $_

For example, to create a project called 'website' in your home directory:

    (host) $ mkdir ~/website && cd $_

When you're all done, this directory will match up with `/vagrant/` in the virtual environment. VirtualBox keeps the two directories in sync so changes to one will be made in the other.

Clone the repo, replacing `<path_to_repo>` with the clone URL of the repo.

    (host) $ git clone <path_to_repo>

Startup Vagrant and provision the Virtual Machine.

    (host) $ vagrant up

SSH in to the Virtual Machine.

    (host) $ vagrant ssh

Install the project-specific packages.

    (vm) sudo pip install -r requirements/development.txt

Sync the database and migrate any migrations.

    (vm) $ dj syncdb
    (vm) $ dj migrate

Force compile the stylesheets (first time only).

    (vm) $ compass compile myproject/static_media/stylesheets --force

## Smoke Test

    (vm) $ frs

Open a Web browser and navigate to [http://localhost:8000](http://localhost:8000). You should see the `home.html` template rendered.

## Full Documentation

This project is a derivative of [django-newproj-template](https://github.com/jbergantine/django-newproj-template) and uses the [Gesso](https://github.com/jbergantine/compass-gesso) frontend framework.