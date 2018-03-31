#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import sqlparse
import jsbeautifier
import xmlformatter


def detect_string_type(str):
    str = str.strip().lower()
    if str.startswith('{'):
        return 'json'
    if str.startswith('['):
        return 'json'
    if str.startswith('<'):
        return 'xml'
    return 'sql'


selected_text = os.getenv("POPCLIP_TEXT")
str_type = detect_string_type(selected_text)
res = None

if str_type == 'json':
    res = jsbeautifier.beautify(selected_text)
if str_type == 'xml':
    formatter = xmlformatter.Formatter(indent="1", indent_char="\t", encoding_output="UTF-8", preserve=["literal"])
    res = formatter.format_string(selected_text)
if str_type == 'sql':
    res = sqlparse.format(selected_text, keyword_case='upper', reindent_aligned=True, use_space_around_operators=True,
                          strip_whitespace=True, strip_comments=True)
if res is None:
    res = selected_text

print res
