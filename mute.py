#!/usr/bin/env python

import syslog
import RPi.GPIO as GPIO
import time
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('pin', metavar='PIN', type=int,
                    choices=range(2, 27),
                    help='GPIO pin number for connected mute switch')
parser.add_argument('-mute', '--mute', type=str, required=True,
                    choices=['on','off'], help='Toggle mute on/off')

args = parser.parse_args()

PIN=args.pin
MUTE=args.mute.lower()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN,GPIO.OUT)

STATE = GPIO.input(PIN)

if(MUTE == 'on' and STATE == 0):
  GPIO.output(PIN,GPIO.HIGH)
  syslog.syslog('Mute is activated via GPIO Pin #%d' % PIN)

if(MUTE == 'off' and STATE == 1):
  GPIO.output(PIN,GPIO.LOW)
  syslog.syslog('Mute is deactivated via GPIO Pin #%d' % PIN)

