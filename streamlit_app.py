#!/usr/bin/env python3

# APMA NEWSLETTER GENERATOR - GUI
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

"""
#####################################################
##                                                 ##
##            -- STREAMLIT MAIN APP --             ##
##                                                 ##
#####################################################
"""

# REQUIREMENTS
# pip install streamlit

# import packages
import streamlit as st

from functions import generate_html
from functions import get_issue_date
from defaults import APMA_CONTENT_DEFAULT
from defaults import APMA_JOURNAL_CLUB_DEFAULT
from defaults import APMA_OMICS_HUB_DEFAULT
from defaults import EUPA_NEWS_DEFAULT
from defaults import NATIONAL_EVENTS_DEFAULT
from defaults import INTERNATIONAL_EVENTS_DEFAULT

# the newsletter generator site
def validated() -> None:

    # set default states
    if "apma_content" not in st.session_state:
        st.session_state["apma_content"] = ""
    if "apma_journal_club" not in st.session_state:
        st.session_state["apma_journal_club"] = ""
    if "apma_omics_hub" not in st.session_state:
        st.session_state["apma_omics_hub"] = ""
    if "eupa_news" not in st.session_state:
        st.session_state["eupa_news"] = ""
    if "national_events" not in st.session_state:
        st.session_state["national_events"] = ""
    if "international_events" not in st.session_state:
        st.session_state["international_events"] = ""

    title = st.title("APMA Newsletter Generator")

    cols = st.columns(2)

    with cols[0]:
        general_description = \
        """
        The following webapp will walk you through the process of creating
        the current APMA newsletter based on the newsletter template. This
        webapp is based on the newsletter from Q4, December 2023. The template
        simplifies some of the newsletter style elements but tries to conserve
        as much of the original as possible.

        **The created newsletter can of course be manually edited after download.**

        _All input fields support html tags for further styling._
        """
        description = st.markdown(general_description)

        general_info = \
        """
        Please be aware that all inputs are only saved as long as the page is open.
        Closing or reloading the page will delete all inputs, even if they were saved!
        """
        info = st.info(general_info.strip())

        header = st.subheader("Data Input", divider = "rainbow")

        # apma content input
        i1t = \
        """
        **APMA_CONTENT**

        The following field controls what goes into the `template:{APMA_CONTENT}`
        box. So any APMA related news, reviews, announcements and other info that
        might fit here should be described below. The general structure should be
        a list, so please start every item with `<li>` and end it with `</li>`,
        an example is provided. You can also load the example to work with the
        default of a previous newsletter.

        As usual the box support html tags, so highlighting elements can be achieved
        with `<b>` and `</b>`. Links should be denoted with `<a href="URL">` and
        closed with `</a>`. Line breaks can be inserted with `<br>`.
        """

        i1m = st.markdown(i1t)

        i1 = st.text_area(label = "Please enter any general APMA information here:",
                          value = st.session_state["apma_content"] if st.session_state["apma_content"] != "" else None,
                          placeholder = APMA_CONTENT_DEFAULT.strip(),
                          height = 500,
                          help = "The html content that replaces APMA_CONTENT.")

        i1cols = st.columns(2)

        with i1cols[0]:

            i1s = st.button(label = "Save!",
                            key = "i1s",
                            use_container_width = True,
                            help = "Save the current textbox state!")

            if i1s and i1 != None:
                st.session_state["apma_content"] = i1
                st.rerun()

        with i1cols[1]:

            i1d = st.button(label = "Load Example!",
                            key = "i1d",
                            use_container_width = True,
                            help = "Load the default html for this textbox! Only works for empty boxes!")

            if i1d:
                if st.session_state["apma_content"] == "":
                    st.session_state["apma_content"] = APMA_CONTENT_DEFAULT.strip()
                    st.rerun()
                else:
                    st.error("Textbox not empty, can't load default content! If you want to load the default, delete everything from the textbox, save and try again!")

        # apma journal club input
        i2t = \
        """
        **APMA_JOURNAL_CLUB**

        The following field controls what goes into the `template:{APMA_JOURNAL_CLUB}`
        box. So any APMA Journal Club related news, announcements or other info that
        might fit here should be described below. The general structure should be
        just raw text, there is no support for list items. You can also load the
        example to work with the default of a previous newsletter.

        As usual the box support html tags, so highlighting elements can be achieved
        with `<b>` and `</b>`. Links should be denoted with `<a href="URL">` and
        closed with `</a>`. Line breaks can be inserted with `<br>`.
        """

        i2m = st.markdown(i2t)

        i2 = st.text_area(label = "Please enter any APMA Journal Club information here:",
                          value = st.session_state["apma_journal_club"] if st.session_state["apma_journal_club"] != "" else None,
                          placeholder = APMA_JOURNAL_CLUB_DEFAULT.strip(),
                          height = 100,
                          help = "The html content that replaces APMA_JOURNAL_CLUB.")

        i2cols = st.columns(2)

        with i2cols[0]:

            i2s = st.button(label = "Save!",
                            key = "i2s",
                            use_container_width = True,
                            help = "Save the current textbox state!")

            if i2s and i2 != None:
                st.session_state["apma_journal_club"] = i2
                st.rerun()

        with i2cols[1]:

            i2d = st.button(label = "Load Example!",
                            key = "i2d",
                            use_container_width = True,
                            help = "Load the default html for this textbox! Only works for empty boxes!")

            if i2d:
                if st.session_state["apma_journal_club"] == "":
                    st.session_state["apma_journal_club"] = APMA_JOURNAL_CLUB_DEFAULT.strip()
                    st.rerun()
                else:
                    st.error("Textbox not empty, can't load default content! If you want to load the default, delete everything from the textbox, save and try again!")

        # apma omics tech hub input
        i3t = \
        """
        **APMA_OMICS_HUB**

        The following field controls what goes into the `template:{APMA_OMICS_HUB}`
        box. So any APMA Omics Tech Hub related news, announcements or other info that
        might fit here should be described below. The general structure should be
        just raw text, there is no support for list items. You can also load the
        example to work with the default of a previous newsletter.

        As usual the box support html tags, so highlighting elements can be achieved
        with `<b>` and `</b>`. Links should be denoted with `<a href="URL">` and
        closed with `</a>`. Line breaks can be inserted with `<br>`.
        """

        i3m = st.markdown(i3t)

        i3 = st.text_area(label = "Please enter any APMA Omics Tech Hub information here:",
                          value = st.session_state["apma_omics_hub"] if st.session_state["apma_omics_hub"] != "" else None,
                          placeholder = APMA_OMICS_HUB_DEFAULT.strip(),
                          height = 150,
                          help = "The html content that replaces APMA_OMICS_HUB.")

        i3cols = st.columns(2)

        with i3cols[0]:

            i3s = st.button(label = "Save!",
                            key = "i3s",
                            use_container_width = True,
                            help = "Save the current textbox state!")

            if i3s and i3 != None:
                st.session_state["apma_omics_hub"] = i2
                st.rerun()

        with i3cols[1]:

            i3d = st.button(label = "Load Example!",
                            key = "i3d",
                            use_container_width = True,
                            help = "Load the default html for this textbox! Only works for empty boxes!")

            if i3d:
                if st.session_state["apma_omics_hub"] == "":
                    st.session_state["apma_omics_hub"] = APMA_OMICS_HUB_DEFAULT.strip()
                    st.rerun()
                else:
                    st.error("Textbox not empty, can't load default content! If you want to load the default, delete everything from the textbox, save and try again!")

        # eupa and eubic news input
        i4t = \
        """
        **EUPA_NEWS**

        The following field controls what goes into the `template:{EUPA_NEWS}`
        box. So any EUPA and EuBIC related news, announcements or other info that
        might fit here should be described below. The general structure should be
        a list, so please start every item with `<li>` and end it with `</li>`,
        an example is provided. You can also load the example to work with the
        default of a previous newsletter.

        As usual the box support html tags, so highlighting elements can be achieved
        with `<b>` and `</b>`. Links should be denoted with `<a href="URL">` and
        closed with `</a>`. Line breaks can be inserted with `<br>`.
        """

        i4m = st.markdown(i4t)

        i4 = st.text_area(label = "Please enter any EUPA & EuBIC news here:",
                          value = st.session_state["eupa_news"] if st.session_state["eupa_news"] != "" else None,
                          placeholder = EUPA_NEWS_DEFAULT.strip(),
                          height = 500,
                          help = "The html content that replaces EUPA_NEWS.")

        i4cols = st.columns(2)

        with i4cols[0]:

            i4s = st.button(label = "Save!",
                            key = "i4s",
                            use_container_width = True,
                            help = "Save the current textbox state!")

            if i4s and i4 != None:
                st.session_state["eupa_news"] = i4
                st.rerun()

        with i4cols[1]:

            i4d = st.button(label = "Load Example!",
                            key = "i4d",
                            use_container_width = True,
                            help = "Load the default html for this textbox! Only works for empty boxes!")

            if i4d:
                if st.session_state["eupa_news"] == "":
                    st.session_state["eupa_news"] = EUPA_NEWS_DEFAULT.strip()
                    st.rerun()
                else:
                    st.error("Textbox not empty, can't load default content! If you want to load the default, delete everything from the textbox, save and try again!")

        # national events input
        i5t = \
        """
        **NATIONAL_EVENTS**

        The following field controls what goes into the `template:{NATIONAL_EVENTS}`
        box. So any national related news, announcements or other info that
        might fit here should be described below. The general structure should be
        a list, so please start every item with `<li>` and end it with `</li>`,
        an example is provided. You can also load the example to work with the
        default of a previous newsletter.

        As usual the box support html tags, so highlighting elements can be achieved
        with `<b>` and `</b>`. Links should be denoted with `<a href="URL">` and
        closed with `</a>`. Line breaks can be inserted with `<br>`.
        """

        i5m = st.markdown(i5t)

        i5 = st.text_area(label = "Please enter any national events and news here:",
                          value = st.session_state["national_events"] if st.session_state["national_events"] != "" else None,
                          placeholder = NATIONAL_EVENTS_DEFAULT.strip(),
                          height = 500,
                          help = "The html content that replaces NATIONAL_EVENTS.")

        i5cols = st.columns(2)

        with i5cols[0]:

            i5s = st.button(label = "Save!",
                            key = "i5s",
                            use_container_width = True,
                            help = "Save the current textbox state!")

            if i5s and i5 != None:
                st.session_state["national_events"] = i5
                st.rerun()

        with i5cols[1]:

            i5d = st.button(label = "Load Example!",
                            key = "i5d",
                            use_container_width = True,
                            help = "Load the default html for this textbox! Only works for empty boxes!")

            if i5d:
                if st.session_state["national_events"] == "":
                    st.session_state["national_events"] = NATIONAL_EVENTS_DEFAULT.strip()
                    st.rerun()
                else:
                    st.error("Textbox not empty, can't load default content! If you want to load the default, delete everything from the textbox, save and try again!")

        # international events input
        i6t = \
        """
        **INTERNATIONAL_EVENTS**

        The following field controls what goes into the `template:{INTERNATIONAL_EVENTS}`
        box. So any international related news, announcements or other info that
        might fit here should be described below. The general structure should be
        a list, so please start every item with `<li>` and end it with `</li>`,
        an example is provided. You can also load the example to work with the
        default of a previous newsletter.

        As usual the box support html tags, so highlighting elements can be achieved
        with `<b>` and `</b>`. Links should be denoted with `<a href="URL">` and
        closed with `</a>`. Line breaks can be inserted with `<br>`.
        """

        i6m = st.markdown(i6t)

        i6 = st.text_area(label = "Please enter any international events and news here:",
                          value = st.session_state["international_events"] if st.session_state["international_events"] != "" else None,
                          placeholder = INTERNATIONAL_EVENTS_DEFAULT.strip(),
                          height = 500,
                          help = "The html content that replaces INTERNATIONAL_EVENTS.")

        i6cols = st.columns(2)

        with i6cols[0]:

            i6s = st.button(label = "Save!",
                            key = "i6s",
                            use_container_width = True,
                            help = "Save the current textbox state!")

            if i6s and i6 != None:
                st.session_state["international_events"] = i6
                st.rerun()

        with i6cols[1]:

            i6d = st.button(label = "Load Example!",
                            key = "i6d",
                            use_container_width = True,
                            help = "Load the default html for this textbox! Only works for empty boxes!")

            if i6d:
                if st.session_state["international_events"] == "":
                    st.session_state["international_events"] = INTERNATIONAL_EVENTS_DEFAULT.strip()
                    st.rerun()
                else:
                    st.error("Textbox not empty, can't load default content! If you want to load the default, delete everything from the textbox, save and try again!")

        html = st.download_button(label = "Generate & Download the Newsletter!",
                                  data = generate_html(i1, i2, i3, i4, i5, i6),
                                  file_name = "apma_newsletter_" + get_issue_date().replace(" ", "-").replace(",", "") + ".html",
                                  mime = "text/html",
                                  help = "Generate and download the APMA Newsleter based on the current data.",
                                  type = "primary",
                                  use_container_width = True)

    # display structure of the newsletter on right column
    with cols[1]:
        st.image("img/template.png",
                 caption = "Template structure of the APMA Newsletter. Does not contain all style elements and does NOT resemble the look of the final newsletter!")

# if not logged in this will be displayed
# simple login form that is not secure, but should keep away accidental guests
def not_validated() -> None:

    title = st.title("APMA Newsletter Generator - Login")

    header = st.subheader("", divider = "rainbow")

    cols = st.columns(2)

    with cols[0]:
        description = st.markdown("Please login to use the webapp.")
        un = st.text_input(label = "Username",
                           help = "Your username to login into the webapp.")
        pw = st.text_input(label = "Password",
                           type = "password",
                           help = "Your password for your username.")
        vl = st.button(label = "Login",
                       type = "primary",
                       use_container_width = True,
                       help = "Login into the APMA Newsletter Generator webapp.")

        if vl:
            # lul plz no hax
            if un == "apma" and pw == "ampa":
                st.session_state["validated"] = True
                st.rerun()
            else:
                st.error("Sorry, the provided username and password did not match!")

# main page content
def main_page() -> None:

    if "validated" in st.session_state:
        if st.session_state["validated"]:
            validated()
        else:
            not_validated()
    else:
        st.session_state["validated"] = False
        not_validated()

# side bar and main page loader
def main() -> None:

    about_str = \
    """
    The APMA Newsletter Generator is a simple webapp to generate
    html-based newsletters to send via email. The webapp uses a base
    html-template provided by APMA and semi-automatically fills in
    necessary information. Additional information can be given via
    the various input fields.
    """

    st.set_page_config(page_title = "APMA Newsletter Generator",
                       page_icon = ":test_tube:",
                       layout = "wide",
                       initial_sidebar_state = "expanded",
                       menu_items = {"Get Help": "https://github.com/apma-austria/newsletter_generator/discussions",
                                     "Report a bug": "https://github.com/apma-austria/newsletter_generator/issues",
                                     "About": about_str}
                       )

    title = st.sidebar.title("APMA Newsletter Generator")

    logo = st.sidebar.image("https://avatars.githubusercontent.com/u/157498035",
                            caption = "Logo of the Austrian Proteomics and Metabolomics Association (c) APMA")

    doc = st.sidebar.markdown(about_str)

    apma_str = \
    """
    [**APMA**](https://www.apma.at/) is short for Austrian Proteomics and Metabolomics Association.
    APMA's mission is to represent researchers in the fields of proteomics, lipidomics, metabolomics
    and bioinformatics in Austria and to foster a community that emphasizes scientific dialogue,
    exchange of ideas and supporting researchers at any point of their career.
    """
    apma = st.sidebar.markdown(apma_str)

    apma_web_str = "**APMA:** [Web](https://www.apma.at/), [Mail](mailto:office@apma.at)"
    apma_web = st.sidebar.markdown(apma_web_str)

    contact_str = "**Contact:** [Micha Birklbauer](mailto:micha.birklbauer@gmail.com)"
    contact = st.sidebar.markdown(contact_str)

    project_str = "**Project Page:** [GitHub](https://github.com/apma-austria/newsletter_generator)"
    project = st.sidebar.markdown(project_str)

    main_page()

if __name__ == "__main__":

    main()
