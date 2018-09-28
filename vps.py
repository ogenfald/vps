#!/usr/bin/python3

#TODO Enable a way to omit '-p' flag

import os
import argparse

class parseArguments():
    parser = argparse.ArgumentParser(description='A simple Xbps wrapper') 
    parser.add_argument('operation', help='Usage: update, remove, install, search')
    parser.add_argument('-p', '--package', help='Usage: Name of the package used with install, remove, search')
    args = parser.parse_args()

def update():
    print('Running sudo xbps-install -Su')
    os.system('sudo xbps-install -Su')

def remove():
    print('Running sudo xbps-remove')
    os.system('sudo xbps-remove ' + p.args.package)

def install():
    print('Running sudo xbps-install')
    os.system('sudo xbps-install ' + p.args.package)

def search():
    print('Running xbps-query -Rs')
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
	