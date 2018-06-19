# auto-openvpn


[![PyPI](https://img.shields.io/pypi/v/aovpn.svg)](https://pypi.org/project/aovpn/)
[![Build Status](https://travis-ci.com/aashutoshrathi/auto-openvpn.svg?token=x5wHaKpXyy9apivkjrhr&branch=master)](https://travis-ci.com/aashutoshrathi/auto-openvpn)

A command line interface for creating an OpenVPN account which will last for 5 days.


## Installation

```sh
 pip install aovpn
```

## Using

```sh
$ aovpn 4CSGo
  Creating OpenVPN account for 4CSGo.
  This may take upto 20 seconds....
  
  Username: udpvpn.com-4CSGo (Copied to your clipboard)
  Password: test
  Valid till 25/06/2018

```


## Limitations

You should not make more than 3 accounts in a day and more than one in a minute.
This may lead to blocking your IP forever.


<p align="center"> Made from scratch by <a href="https://github.com/aashutoshrathi">Aashutosh Rathi</a> </p>