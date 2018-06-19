# auto-openvpn


[![PyPI](https://img.shields.io/pypi/v/auto-openvpn.svg)](https://pypi.org/project/auto-openvpn/)
[![Build Status](https://travis-ci.com/aashutoshrathi/auto-openvpn.svg?token=x5wHaKpXyy9apivkjrhr&branch=master)](https://travis-ci.com/aashutoshrathi/auto-openvpn)

A command line interface for creating an OpenVPN account which will last for 5 days.

OpenVPN supports unlimited **online gaming** and works for Port **53**, 8080 and 25000.


## Prerequisites

#### Selenium

First, install python package using,

```sh
$ pip install selenium
```

and then Download Chrome Drivers from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads)

Now, extract the zip and save folder to Home Drive. Also add `C:\chromedriver_win32` to `PATH` variable.

#### pyperclip
```sh
$ pip install pyperclip
```

### UDP VPN config

Download UDP VPN config from tcpvpn.com, and choose port 53.


## Installation

```sh
$ pip install auto-openvpn
```

### Updating

```sh
$ aovpn -U
```

## Demo

![Demo](https://media.giphy.com/media/7SWHqisJev13A5su06/giphy.gif)


## Using

```sh
$ aovpn 4CSGo
  Creating OpenVPN account for 4CSGo.
  This may take upto 20 seconds....
  
  Username: udpvpn.com-4CSGo (Copied to your clipboard)
  Password: test
  Valid till 25/06/2018
```

## How does it work?

It uses Headless Chrome driver to load `https://www.tcpvpn.com/home` and then select Asia -> India -> UDP VPN, and then submits the form for creating an account for 5 days with random **username** and **password** as `test` and *copies* the username to your clipboard.

## Limitations

You should not make more than 3 accounts in a day and more than one in a minute.

This may lead to blocking your IP forever.


<p align="center"> Made from scratch by <a href="https://github.com/aashutoshrathi">Aashutosh Rathi</a> </p>