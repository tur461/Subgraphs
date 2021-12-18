#!/usr/bin/python

# Exports contract ABI in JSON

import argparse
import requests
import json

Usage = '\nUsage: python fetch_abi.py <contract address> -o <output abi json file path & name>\n'

BASE_URL = {
    'BSC': 'api.bscscan.com',
    'ETH': 'api.etherscan.io'
}
API_KEY = {
    'BSC': 'XBE328BQKTZVZMXCI73TKJAHHQQ9UPVWZS',
    'ETH': 'Y6PMZSW9N93SV5ZHMTMXXX4FJRAVMEZ7KC'
}
ABI_ENDPOINT = 'https://{}/api?module=contract&action=getabi&address={}&apikey={}'

print(Usage)

parser = argparse.ArgumentParser()
parser.add_argument('addr', type=str, help='Contract address')
parser.add_argument('-o', '--output', type=str,
                    help="Path to the output JSON file", required=True)


def __main__():

    args = parser.parse_args()
    response = requests.get(ABI_ENDPOINT.format(
        BASE_URL['BSC'], args.addr, API_KEY['BSC']))
    response_json = response.json()
    # print(response_json)
    abi_json = json.loads(response_json['result'])
    result = json.dumps(abi_json, indent=4, sort_keys=True)

    open(args.output, 'w').write(result)
    print('Done...Please check!')


if __name__ == '__main__':
    __main__()
