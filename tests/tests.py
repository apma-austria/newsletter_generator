#!/usr/bin/env python3

# APMA NEWSLETTER GENERATOR - TESTS
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

def test():

    from functions import generate_html

    html = generate_html()
    assert len(html) > 0
