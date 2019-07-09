# fetch-gh-key

Copyright (c) 2019 by Nils Magnus (nils.magnus@t-systems.com)

Licensed under the GPLv2.

This script fetches SSH public keys from GitHub's public API.

How to install
--------------

Requires the `requests` library. To install it run `pip install requests`.
A virtual env is recommended. Written for Python 3.

How to use
----------

```bash
python fetch-gh-keys.py userid ...
```

The script fetches all verified SSH keys for all listed users. Use the pure username without any URL around it.

Example
-------

```bash
python fetch-gh-keys.py Nils-Magnus Nils
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDRjzCczBVLyUD1WkJr92lodTjP7slf99wWnJ09Po63404OdylEmGls8m7gtEply/KYoeTzLe3
282W0Gwl0iWmNUkLOVK1eZlIrMlzlsE2cirpVH+6JbpBQXVtQ3InmG13wNzYrGYMQIuHrJgbWsO1ON4Q5wvIsZbzhDNpu5Ban/TwySFBFasaN5Q
[... truncated ...]
YUJOi4KMkQdQj31epvzZmYru9qfpLSs7XVhIRBUHShexy/j3H50cvZWj1lQZRAIYnpLjb3s9QgvvGIatSqQob8gbCksU3hFWmFsyF/VoDn4HAzP
JgnNzP8B8VCy9P9Ra6l0RniRgWvGsPv2mXB0xBScPpwMnS9X0U+lA7DdW8D1sUkAAmV0W5iRTG0Sk5aTvTLYp2GjZW4GKlsuB/mQWEwSU3zZUXd
eXlkInNR0BIs+xIEu3H2m6gv2GI6qFxfCBGEpEE34g2n5B18BJE1VmIw== key from Github user Nils-Magnus (ID 16118465)

ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCadaGS7ThMhyXOaLJnGTsR4hZicmp8L7szWQKHEOtbM72Xx29ysLWmhVIum/2kxYt2GFYcLkz
Vh2ApCZ8o5cd/nRtEb3MCO1wzeaVQ1aguFhK3K+/M5zmGSMq38obDSXqWZeKM0g9DGX+vhKbHX9v3aGfew61UKZ0VEbRxEdPOE6gOdhP9uEfuHa
[... truncated ...]
iMCmF0qLlT0/HnirWMgvWSVF6miBt3xROqjQXprqYQGmMZZ key from Github user Nils (ID 7719095)
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCzqVktpDpdHDjVuJJBv1zyDi+iefmxLQC+OdjEQu595y3S2Ku4euEGThMixst7m8JOq2+fJVC
[... truncated ...]
WzIfb08+AMgKmD3vrjM1ahMBFDlE84CZFV/UK12EIpJ49+f key from Github user Nils (ID 30270359)
```
