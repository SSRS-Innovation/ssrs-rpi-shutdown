# SSRS Raspberry Pi Companion Computer Shutdown Script

Shuts down the Raspberry Pi Companion Computer when the power supply module
on the carrier board sets GPIO21 high.

## Installation

```
$ sudo install ssrs-rpi-shutdown.py /usr/local/bin
$ sudo install ssrs-rpi-shutdown.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl enable ssrs-rpi-shutdown.service
$ sudo systemctl start ssrs-rpi-shutdown.service
```
