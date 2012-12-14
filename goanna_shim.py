#!/usr/bin/python2.7

import re, sys, os, subprocess, time

## GOanna Project CGI ----> Command Line Client
## by Eric Dawson
## 11/2012

## 1. Write a client that can fake the command line inputs, send a file to the servers at GOanna, process it using the desired parameters, and then go fetch the results
#3 (probably in a sleep 10/ping/sleep 10 interval until a result is returned).
## Make sure to use named parameters rather than positional (e.g. sys.argv[1], [2], etc; instead use "--myVar 1", etc)

## Integrate said CLI tool into the iPlant discovery environment (this should be super easy). We'd like this done by Jan 1.

def pingGOanna(url):
	while True:
		ret = subprocess.call("ping -c 1 %s" % url, shell = True)
		if ret ==0 : print "%s is alive" % url
		print "Taking a 3 second nap"
		time.sleep(3)

def main():
	url = 'www.google.com'
	pingGOanna(url)
	


main()
