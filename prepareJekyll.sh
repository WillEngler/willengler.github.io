#!/usr/bin/env bash
#The above line specifies what shell this
# script needs to run on.

#This script takes about 30 minutes to execute on 
# a VM w/ 512 MB of RAM
echo 'Hello, Vagrant!'

#Go to the folder shared by the host and guest OS's.
cd /vagrant

#This line is needed to work around a bug in the
# Nokogiri gem.
sudo ln -s /usr/bin/gcc /usr/bin/gcc-4.2

#This lets Ubuntu's package manager know 
# what software packages are available to install.
apt-get update

#First things first, get git so that 
# we can grab source code.
apt-get install -y git

#The following lines are used to install Ruby 2.1.2
#I adapted them from a rails setup tutorial at
# https://gorails.com/setup/ubuntu/14.04
#Rather than use the version of Ruby preinstalled
# in Trusty Tahr, I used RVM to work around 
# some errors I didn't understand.

#BEGIN: content from gorails to install ruby with RVM
sudo apt-get install libgdbm-dev libncurses5-dev automake libtool bison libffi-dev
curl -L https://get.rvm.io | bash -s stable

#I changed the argument in the next two lines from
# "~/.rvm/scripts/rvm" to "/etc/profile.d/rvm.sh"
# because an RVM error message told me to.
source /etc/profile.d/rvm.sh
echo "source /etc/profile.d/rvm.sh" >> ~/.bashrc
rvm install 2.1.2
rvm use 2.1.2 --default
#Print out the version of Ruby we're using
#to make sure we got it right.
ruby -v

#This line just disables time-consuming
# documentation downloads for gems
echo "gem: --no-ri --no-rdoc" > ~/.gemrc
#END: content from gorails

#We'll need a Javascript runtime. Node will work.
apt-get install -y nodejs

#Use bundler to manage gems
apt-get install -y bundler

#Install the gems in our Gemfile (namely, the
# Github-pages gem that makes sure our working
# environment will be identical to the one Github
# uses)
bundle install

#Fire up the website!
# When provisioning is complete, you should be able
# to direct your browser to http://127.0.0.1::4567
# and see the website.
bundle exec jekyll serve