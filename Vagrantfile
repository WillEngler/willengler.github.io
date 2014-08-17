VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provision :shell, path: "prepareJekyll.sh"
  config.vm.network :forwarded_port, host: 4567, guest: 4000
end