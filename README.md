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

## Example

```bash
$ whoenum -d alibaba.com | jq
```

```json
{
  "domain_name": [
    "ALIBABA.COM",
    "alibaba.com"
  ],
  "registrar": "Alibaba Cloud Computing (Beijing) Co., Ltd.",
  "whois_server": "grs-whois.hichina.com",
  "referral_url": null,
  "updated_date": "2018-11-19 04:52:41",
  "creation_date": "1999-04-15 04:00:00",
  "expiration_date": "2023-05-23 19:54:58",
  "name_servers": [
    "NS1.ALIBABADNS.COM",
    "NS2.ALIBABADNS.COM"
  ],
  "status": [
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",
    "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",
    "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited"
  ],
  "emails": "DomainAbuse@service.aliyun.com",
  "dnssec": "unsigned",
  "name": null,
  "org": null,
  "address": null,
  "city": null,
  "state": "zhe jiang",
  "zipcode": null,
  "country": "CN"
}
```

## Thanks

This tool is based on [python-whois](https://github.com/richardpenman/whois)
