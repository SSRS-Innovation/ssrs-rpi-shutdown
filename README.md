# SSRS Raspberry Pi Companion Computer Shutdown Script

Shuts down the Raspberry Pi Companion Computer when the power supply module
on the carrier board sets GPIO21 high.

NOTE: This script isn't really needed. It can be replaced by adding the following to
`/boot/firmware/config.txt`:
```
# Initiate shutdown when GPIO21 is pulled high for at least 500 ms
dtoverlay=gpio-shutdown,gpio_pin=21,active_low=0,gpio_pull=down,debounce=500
```

## Installation

```
$ sudo install ssrs-rpi-shutdown.py /usr/local/bin
$ sudo install ssrs-rpi-shutdown.service /etc/systemd/system/
$ sudo systemctl daemon-reload
$ sudo systemctl enable ssrs-rpi-shutdown.service
$ sudo systemctl start ssrs-rpi-shutdown.service
```
