#!/usr/bin/env python3

import RPi.GPIO as gpio
from datetime import datetime, timedelta
from time import sleep
import cotidie

from config import *

gpio.setmode(gpio.BCM)
mode = gpio.IN
resistenza = gpio.PUD_UP

for c in canali:
  gpio.setup(canali[c], mode, resistenza)

max_delay_between_boa = 4

while True:

  # aspetto un evento sulla boa_1 (esterna)
  gpio.wait_for_edge(canali["boa_1"], gpio.RISING)
  boa_1_dt = datetime.now()

  # aspetto per N secondi il passagio dalla boa_2
  gpio.wait_for_edge(canali["boa_2"], gpio.RISING, timeout=max_delay_between_boa*1000)
  boa_2_dt = datetime.now()

  delta = boa_2_dt - boa_1_dt
