---
layout: post
title: How I Learned to Stop Worrying About Development Environments and Love Vagrant
date: 2014-08-19 11:07:30
tags: process
---

Configuring Development Environments Gives Me Migraines
---------------------------------------------

For me, setting up a working development environment is one of the most difficult parts about learning a new technology stack. I remember my frustration when I began my co-op and my machine’s configuration would be just slightly different from the other developers’. For weeks, I would install and uninstall Visual Studio support packs, tweak my version control setup, and reconfigure the other software that my group’s software interfaced with. I just wanted to code, but I had to pour so much effort into creating the right environment.

Setting up a dev environment also dogged me the first time I tried to learn Ruby on Rails. I was installing Ruby, Bundler, and a whole bunch of gems when I started seeing strange errors. I couldn’t figure out how to fix them. Nor could I figure out how to completely retrace my path and start again. That was the as far as that attempt to learn Ruby on Rails ever got.

A Clever Solution
------------------

When I started working with the [Pitt Computer Science Club][CSC], the other officers proposed using [Vagrant][vagrant] as a way to easily set up and share development environments across a team. My prayers to the programmer gods had been answered. There is a solution to the environment setup problem. And it’s really cool.

Vagrant was created by a web dev named Mitchell Hashimoto. He got fed up with setting up and tearing down development environments for all of the web frameworks he worked in for different projects. The basic gist of his solution is this: write a _Vagrantfile_ that specifies a virtual machine (VM) and the software to be installed on it.  Call `vagrant up` in the directory with the Vagrantfile and Vagrant will use a _provider_ (like Virtualbox or VMWare) to spin up the VM from the _box_ (VM base image) you specified. Then, a _provisioner_ will install the tools you want on the VM and perform any other configuration. A provisioner can be as simple as a shell script, but Vagrant also supports configuration management tools like [Chef][chef] and [Ansible][ansible] that can do some fancier things. 

Once the box is running and provisioned, you can start working. Vagrant syncs the folder on the host OS that contains the Vagrantfile with the /vagrant directory on the guest OS. You can compose on your host machine with your favorite text editor and then compile on the guest OS. The real magic comes in when you understand Vagrant’s name. You can mess around in your VM sandbox all you want and when you’re done working, type `vagrant destroy`. Your sandbox is obliterated and you can start again the next day in a known state with a simple `vagrant up`.

An Unpaid Testimonial
----------------------

I’ve only been playing with Vagrant for the last two weeks (mostly to build this blog). I still have a lot to learn. In particular, I would like to learn a configuration management tool instead of provisioning with shell scripts. Still, Vagrant is easy to pick up and it solves a hairy problem. I plan on making a Vagrantfile for each one of my classes this semester. At last, I am walking out of the inner rings of dev environment hell with Vagrant my Virgil.

I plan on posting a slightly more technical overview soon. I'd like to share some of the specific roadblocks I encountered when I was getting everything set up. In the mean time, Vagrant's [Getting Started][tutorial] page is very helpful if you want to dive in.

[CSC]:	http://pitt-csc.github.io/
[tutorial]:	http://docs.vagrantup.com/v2/getting-started/index.html
[vagrant]:	http://www.vagrantup.com/
[chef]:	http://www.getchef.com/chef/
[ansible]:	http://www.ansible.com/home