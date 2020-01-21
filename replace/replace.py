#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

f = open('./replace.json' , 'r')
json_dict = json.load(f)

for a in range(12):
  print(a)

for x in json_dict:
  dist_page = x['body_value']
  result_search = print('a11y-dialog.min.js' in dist_page or 'photoswipe-ui-default\.min.js' in dist_page)
  
  if result_search:
    print(json_dict[x])