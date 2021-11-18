# WhoEnum

Mass querying whois records using whois tool

## Install

```bash
git clone http://github.com/melbadry9/WhoEnum.git;
cd WhoEnum; 
pip3 install .;
```

## Help

```bash
$ whoenum -h 

usage: whoenum [-h] [-t THREADS] [-r RETRIES] [-d DOMAIN | -l LIST]

optional arguments:
  -h, --help            show this help message and exit
  -t THREADS, --threads THREADS
                        Number of threads
  -r RETRIES, --retries RETRIES
                        Number of retries after failure attempt
  -d DOMAIN, --domain DOMAIN
                        Use domains as a string sperated by ','
  -l LIST, --list LIST  Use list of domains
```

## Thanks

This tool is based on [python-whois](https://github.com/richardpenman/whois)