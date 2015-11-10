# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = '2'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  # Every Vagrant virtual environment requires a box to build off of.
  config.vm.box = 'charles-mead-WC/debian-wheezy_django-build'

  # Open ports:
  #
  # 1080  - MailCatcher
  # 3000  - Rails
  # 3005  - BrowserSync
  # 5432  - Postgres
  # 6379  - Redis
  # 35729 - Livereload
  # 5316  - Jasmine
  [1080, 3000, 3005, 5432, 6379, 5316].each do |p|
    config.vm.network :forwarded_port, guest: p, host: p
  end

  # NFS
  config.vm.network 'private_network', ip: '192.168.50.4'
  config.vm.synced_folder '.', '/vagrant', type: 'nfs'

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  config.vm.provider 'virtualbox' do |vb|
    vb.customize ['modifyvm', :id, '--memory', '2048']
  end

  # Provision application
  config.vm.provision 'shell',
    privileged: false,
    path: 'bin/vagrant'
end
