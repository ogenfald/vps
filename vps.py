#!/usr/bin/python3

import os
import argparse

#TODO Add proper error messages

class parseArguments():
    parser = argparse.ArgumentParser(description='A simple Xbps wrapper') 
    parser.add_argument('operation', help='Usage: update, remove, install, search')
    parser.add_argument('package', nargs='?', help='Usage: Name of the package used with install, remove, search')
    args = parser.parse_args()

def update():
    print('Running sudo xbps-install -Su')
    os.system('sudo xbps-install -Su')

def remove():
    print('Running sudo xbps-remove ' + p.args.package)
    os.system('sudo xbps-remove ' + p.args.package)

def install():
    print('Running sudo xbps-install ' + p.args.package)
    os.system('sudo xbps-install ' + p.args.package)

def search():
    print('Running xbps-query -Rs ' + p.args.package)
    os.system('xbps-query -Rs ' + p.args.package)

def main():
    if p.args.operation == 'update':
        update()
    elif p.args.operation == 'remove':
        remove()
    elif p.args.operation == 'install':
        install()
    elif p.args.operation == 'search':
        search()
    else:
        p.parser.print_help()

p=parseArguments()

if __name__ =='__main__':
	main()
	
