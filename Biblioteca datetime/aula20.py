#!/usr/bin/env python

from datetime import datetime

now = datetime.now()

print '%s/%s/%s' % (now.month, now.day, now.year)