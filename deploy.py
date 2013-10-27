#!/usr/bin/env python

import os

print('Push to GitHub')
os.system('git push origin master')
print('Push to Heroku')
os.system('git push heroku master')
