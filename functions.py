#!/usr/bin/env python3

# APMA NEWSLETTER GENERATOR
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# version tracking
__version = "1.0.0"
__date = "2024-05-02"

# import packages
from datetime import datetime

from defaults import APMA_CONTENT_DEFAULT
from defaults import APMA_JOURNAL_CLUB_DEFAULT
from defaults import APMA_OMICS_HUB_DEFAULT
from defaults import EUPA_NEWS_DEFAULT
from defaults import NATIONAL_EVENTS_DEFAULT
from defaults import INTERNATIONAL_EVENTS_DEFAULT

####### FUNCTIONS #######

def get_issue_date() -> str:
    """Returns the issue date in the style 'Q{Quartal}, Month Year'.

    Returns
    -------
    issue_date : str
        The issue date based on the current date.

    Examples
    --------
    >>> from functions import get_issue_date
    >>> get_issue_date()
    Q2, May 2024
    """

    months = {1: "January",
              2: "February",
              3: "March",
              4: "April",
              5: "May",
              6: "June",
              7: "July",
              8: "August",
              9: "September",
              10: "October",
              11: "November",
              12: "December"}

    today = datetime.today().strftime("%Y-%m-%d")

    q = int(int(today.split("-")[1]) / 4) + 1
    month = months[int(today.split("-")[1])]
    year = int(today.split("-")[0])

    return f"Q{q}, {month} {year}"

def get_current_year() -> str:
    """Returns the current year.

    Returns
    -------
    current_year : str
        The current year based on the current date.

    Examples
    --------
    >>> from functions import get_current_year
    >>> get_current_year()
    2024
    """

    return datetime.today().strftime("%Y-%m-%d").split("-")[0]

def generate_html(apma_content: str = APMA_CONTENT_DEFAULT,
                  apma_journal_club: str = APMA_JOURNAL_CLUB_DEFAULT,
                  apma_omics_hub: str = APMA_OMICS_HUB_DEFAULT,
                  eupa_news: str = EUPA_NEWS_DEFAULT,
                  national_events: str = NATIONAL_EVENTS_DEFAULT,
                  international_events: str = INTERNATIONAL_EVENTS_DEFAULT,
                  save_html: bool = False) -> str:
    """Generates the html for the current newsletter based on the given input.

    Parameters
    ----------
    apma_content : str
        APMA relevant announcements about organisatorial stuff.
    apma_journal_club : str
        APMA Journal Club announcement text.
    apma_omics_hub : str
        APMA Omics Tech Hub announcement text.
    eupa_news : str
        EUPA and EuBIC related announcements.
    national_events : str
        Announcements about national events.
    international_events : str
        Announcements about international events.
    save_html : bool, default = False
        Whether or not to save the generated html to file.

    Returns
    -------
    html : str
        The html for the current newsletter based on the given input.

    Examples
    --------
    >>> from functions import generate_html
    >>> html = generate_html()
    """

    if apma_content is None or apma_content.strip() == "":
        apma_content = "template:{APMA_CONTENT}"
    if apma_journal_club is None or apma_journal_club.strip() == "":
        apma_journal_club = "template:{APMA_JOURNAL_CLUB}"
    if apma_omics_hub is None or apma_omics_hub.strip() == "":
        apma_omics_hub = "template:{APMA_OMICS_HUB}"
    if eupa_news is None or eupa_news.strip() == "":
        eupa_news = "template:{EUPA_NEWS}"
    if national_events is None or national_events.strip() == "":
        national_events = "template:{NATIONAL_EVENTS}"
    if international_events is None or international_events.strip() == "":
        international_events = "template:{INTERNATIONAL_EVENTS}"

    with open("template.html", "r", encoding = "utf-8") as f:
        html = f.read()
        f.close()

    issue_date = get_issue_date()
    current_year = get_current_year()

    html = html.replace("template:{ISSUE_DATE}", issue_date)
    html = html.replace("template:{APMA_CONTENT}", apma_content)
    html = html.replace("template:{APMA_JOURNAL_CLUB}", apma_journal_club)
    html = html.replace("template:{APMA_OMICS_HUB}", apma_omics_hub)
    html = html.replace("template:{EUPA_NEWS}", eupa_news)
    html = html.replace("template:{NATIONAL_EVENTS}", national_events)
    html = html.replace("template:{INTERNATIONAL_EVENTS}", international_events)
    html = html.replace("template:{CURRENT_YEAR}", current_year)

    if save_html:
        filename = "apma_newsletter_" + issue_date.replace(" ", "-").replace(",", "") + ".html"
        with open(filename, "w", encoding = "utf-8") as f:
            f.write(html)
            f.close()

    return html
