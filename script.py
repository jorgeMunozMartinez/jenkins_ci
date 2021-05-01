#!/usr/bin/env python3

import requests

def check(url):
   x = requests.get(url)

   if x.status_code == 200:
     print('uclm')
     return 'uclm'
   else:
     print('no uclm')
     return 'no uclm'
