#!/usr/bin/env python

import fileinput
import re

acronym = ""
for line in fileinput.input():
    words = re.split('\s+', line)
    for word in words:
        if (len(word) > 0 and word[0] == word[0].upper()):
            acronym += word[0]
    print(acronym)

