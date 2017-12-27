#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import subprocess
import logging
import requests


def parseDates(diz, k):
  diz[k] = datetime.fromtimestamp(diz[k])
  return diz


def run(cmd, testo=""):
  logging.debug('Processo {0} {1}'.format(testo, cmd))
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  p.communicate()
  if p.returncode != 0:
    logging.error('Stderr {}'.format(p.stderr))
    logging.error('Stdout {}'.format(p.stdout))
    logging.error('Cmd {0} {1}'.format(testo, cmd))
    return 1
  return 0

