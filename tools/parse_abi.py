#!/usr/bin/python

# Exports contract ABI in JSON

import argparse
import json

Usage = '\nUsage: python parse_abi.py <abi file path> -o <retrieve string: events|read-functions|write-functions|properties>\n'

print(Usage)

parser = argparse.ArgumentParser()
parser.add_argument('abi', type=str, help='ABI File Name')
parser.add_argument('-r', '--retrieve', type=str,
                    help="retrieve what: events, functions, properties", required=True)
parser.add_argument(
    '-f', '--format', help="format for sub-graph manifest", action="store_true")


def printEvents(dat, args):
    event_name = ''
    event_params = []
    for item in dat:
        if item['type'] == 'event':
            event_name = item['name']
            for ip in item['inputs']:
                if ip['indexed']:
                    event_params.append('{} {}'.format('indexed', ip['type']))
                else:
                    event_params.append(ip['type'])
            if args.format:
                print('- event: {}({})'.format(
                    event_name, ','.join(event_params)))
                print('  handler: handle{}'.format(event_name))
            else:
                print('{}({})'.format(event_name, ','.join(event_params)))
            event_params.clear()


def printReadFunctions(dat):
    pass


def printWriteFunctions(dat):
    pass


def printProps(dat):
    pass


def __main__():

    args = parser.parse_args()
    with open(args.abi, 'r') as abiFile:
        abi_data = json.load(abiFile)
        if args.retrieve == 'events':
            printEvents(abi_data, args)
        elif args.retrieve == 'read-functions':
            printReadFunctions(abi_data, args)
        elif args.retrieve == 'write-functions':
            printWriteFunctions(abi_data, args)
        elif args.retrieve == 'properties':
            printProps(abi_data, args)
        else:
            print('please specify what to retrieve, correctly!')


if __name__ == '__main__':
    __main__()
