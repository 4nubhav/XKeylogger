# XKeylogger

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/4nubhav/XKeylogger/graphs/commit-activity)

Keylogger for Linux with GTK+ 3 based desktop environments such as GNOME, XFCE, LXDE etc.

## Features

* Keystrokes logging
* Clipboard logging
* Screenshot after every paste (Ctrl+V)

## Installation

1. Clone the repo
```bash
git clone https://github.com/4nubhav/XKeylogger
```
2. Go to the directory
```bash
cd XKeylogger
```
3. Install the dependencies

* [pyxhook](https://github.com/JeffHoogland/pyxhook) (Already included, no need to install)
* [python-xlib](https://github.com/python-xlib/python-xlib) [![PyPI version](https://badge.fury.io/py/python-xlib.svg)](https://badge.fury.io/py/python-xlib)
* [PyGObject](https://github.com/GNOME/pygobject) [![PyPI version](https://badge.fury.io/py/PyGObject.svg)](https://badge.fury.io/py/PyGObject)

```bash
pip install -r requirements.txt
```
## Usage

```bash
python keylogger.py
```
You can change the path to the log file & screenshots directory in ```keylogger.py```

## Bugs & Issues
[![Report Issues !](https://img.shields.io/badge/Report-Issues-red.svg)](https://github.com/4nubhav/XKeylogger/issues/new)

## Roadmap

* Sending the logs via email, etc.  
* Supporting Qt based desktop environments such as KDE, LXQt

## Contributing

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
