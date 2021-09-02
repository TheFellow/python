#!/usr/bin/env python3

import sys
import argparse
import invoiced
import pandas

from math import ceil
from obfuscation import CustomerObfuscater
from invoice_mapping import InvoicedCustomerToBillingCustomer

def main(arguments):

    parser = argparse.ArgumentParser(
        epilog="""Example:\n python main.py <API_KEY> """,
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument("api_key", help="A valid API key is required for all requests.")
    args = parser.parse_args(arguments)
    client = invoiced.Client(args.api_key)

    data_list = pull_paginated_rows(client)
    process(data_list)

def process(data_list):
    obfuscated = CustomerObfuscater.Process(data_list)
    mapped = [InvoicedCustomerToBillingCustomer(customer) for customer in obfuscated]
    print(mapped)
    # TODO: Pull this from args?
    pandas.DataFrame(mapped).to_csv(r"c:\temp\out.csv", index=False)

def pull_paginated_rows(client):
    max_per_page = 100
    
    data_list, metadata = client.Customer.list(per_page=max_per_page)
    total_pages = ceil(metadata.total_count / max_per_page)

    print(f"Get page 1 of {total_pages}")
    for num_page in range(2, total_pages + 1):
        data_list += client.Customer.list(page=num_page)[0]
        print(f"Get page {num_page} of {total_pages}")

    return data_list

    
if __name__ == "__main__":
    main(sys.argv[1:])
