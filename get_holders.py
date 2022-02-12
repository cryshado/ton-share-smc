"""
ton-share-smc – TON based smart contract for share allocation

Copyright (C) 2022 Alexander Gapak

This file is part of ton-share-smc.

ton-share-smc is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

ton-share-smc is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ton-share-smc.  If not, see <https://www.gnu.org/licenses/>.
"""

import argparse
from requests import post
from lib.tonutil import address_to_b64


def parse_args():
    parser = argparse.ArgumentParser(
        description='run get method "get_holders" of share-smc with json rpc'
    )

    parser.add_argument("-a", "--address", type=str, dest="smc_address", required=True)
    parser.add_argument("-u", "--url", type=str, dest="json_rpc_url",
                        default="https://testnet.toncenter.com/api/v2/jsonRPC")

    return parser.parse_args()


def main():
    args = parse_args()

    resp = post(url=args.json_rpc_url, json={
        "method": "runGetMethod",
        "params": {"address": args.smc_address,
                   "method": "get_holders", "stack": []},
        "jsonrpc": "2.0"
    })

    if not resp.ok:
        print(f"error JSON RPC status code: {resp.status_code}")
        return

    resp = resp.json()

    for elem in resp["result"]["stack"][0][1]["elements"]:
        wc, int_address, percent = (int(i["number"]["number"])
                                    for i in elem["tuple"]["elements"])

        print(address_to_b64(wc, int_address), f"{percent / 100}%")


if __name__ == "__main__":
    main()
