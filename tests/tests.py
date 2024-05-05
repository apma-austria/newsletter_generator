#!/usr/bin/env python3

# APMA NEWSLETTER GENERATOR - TESTS
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

def test():

    from functions import generate_html

    html = generate_html()

    assert len(html) > 0
    assert "template:{ISSUE_DATE}" not in html
    assert "template:{APMA_CONTENT}" not in html
    assert "template:{APMA_JOURNAL_CLUB}" not in html
    assert "template:{APMA_OMICS_HUB}" not in html
    assert "template:{EUPA_NEWS}" not in html
    assert "template:{NATIONAL_EVENTS}" not in html
    assert "template:{INTERNATIONAL_EVENTS}" not in html
    assert "template:{CURRENT_YEAR}" not in html
