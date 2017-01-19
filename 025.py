#! /usr/bin/env python3

from datetime import datetime

or = datetime.now()
print("Today is {0:%Y}-{0:%m}-{0:%d} and it is {0:%H}:{0:%M}:{0:%S}".format(or))
