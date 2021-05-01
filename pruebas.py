#!/usr/bin/env python3

import requests

def check(url):
   x = requests.get('https://www.uclm.com/%27)

   if x.status_code == 200:
     print('yay!')
     return 'yay!'
   else:
     print('uh-oh!')
     return 'error'
