import sys
import argparse
from itertools import repeat
from whoisenum.whois import whois 
from whoisenum.whois.parser import PywhoisError
from concurrent.futures import ThreadPoolExecutor


def args():
    parser = argparse.ArgumentParser() 
    parser.add_argument("-t", "--threads", type=int, default=5, help="Number of threads")
    parser.add_argument("-r", "--retries", type=int, default=5, help="Number of retries after failure attempt")

    group_list = parser.add_mutually_exclusive_group()
    group_list.add_argument("-d","--domain", type=str, help="Use domains as a string sperated by ','")
    group_list.add_argument("-l","--list", type=str, help="Use list of domains")

    return parser

def read_data(domain, retries:int):
    retry_num = 0
    while retry_num < retries:
        try:
            data = whois(domain)
            if data["domain_name"] != None:    
                sys.stdout.write(str(data) + "\n")
                break

        except PywhoisError:
            sys.stderr.write(f"Not found {domain} - retry {str(retry_num)}\n")

        except Exception as e:
            sys.stderr.write(f"Error {domain} : {str(e)}\n")

        finally:
            retry_num += 1

def main():
    parser = args()
    opts = parser.parse_args()

    if opts.domain or opts.list:
        if opts.list:
            with open(opts.list, "r") as e:
                data = e.read().splitlines()
        
        if opts.domain:
            data = opts.domain.split(",")
    else:
        input_type = sys.stdin
        if input_type.isatty():
            parser.print_help()
            exit()
        else:
            data = input_type.read().splitlines()

    handler = ThreadPoolExecutor(opts.threads)
    handler.map(read_data, data, repeat(opts.retries))
    handler.shutdown(True)

if  __name__ == "__main__":
   main()