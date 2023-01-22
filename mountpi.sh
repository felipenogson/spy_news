#!/bin/env bash
sudo sshfs -o follow_symlinks,allow_other,default_permissions pi@pi.nogson.com:./Dev/pi_spy_news ./pi
