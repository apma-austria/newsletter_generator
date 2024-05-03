#!/usr/bin/env python3

# APMA NEWSLETTER GENERATOR - DEFAULTS
# 2024 (c) Micha Johannes Birklbauer
# https://github.com/michabirklbauer/
# micha.birklbauer@gmail.com

# version tracking
__version = "1.0.0"
__date = "2024-05-02"

###### PARAMETERS #######

APMA_CONTENT_DEFAULT = \
"""
<li>
  <b>APMRS 2023: It was great seeing you in Innsbruck! Next year Vienna!</b><br>
  APMRS 2023 took place from 27th to 29th of September in the beautiful city of
  Innsbruck. We would like to thank all the sponsors, organizers and participants
  for making this event such a success as it was! <b>APMRS 2024</b> will be held from
  <b>24th to 26th of September 2024</b> jointly as a <b>Central and Eastern European
  Proteomics Conference (CEEPC)</b> at the Medical University Vienna. Stay tuned about it on
  <a href="https://www.apma.at/apmrs-22/">apma.at</a>.
</li>
<li>
  <b>APMA Junior Board Christmas Stammtisch in Vienna!</b><br>
  We would like to invite you
  to our <b>Christmas gathering</b> organized by the <b>APMA Junior Board</b>
  which will take place on the <b>15th of December</b>, starting from <b>16:30 at Altes AKH</b>
  (meeting point at main entrance). Check out AMPA social media channels for exact timeline.
  This and other junior Board events are open for support by industry and collaborators!
  Reach out to office@apma.at for more info.<br>
  Day: Friday 15th December 2023<br>
  Time: 16:30<br>
  Location: Weihnachtsdorf at Campus UniWien (Altes AKH), Alserstrasse 1090 Vienna
</li>
"""

APMA_JOURNAL_CLUB_DEFAULT = \
"""
The last interuniversity APMA Journal club of this year will take
place on the 20th of December at 16:30 and will restart again on the 10th of January next year.
"""

APMA_OMICS_HUB_DEFAULT = \
"""
Next to the Journal club, another, more theme specific
discussion platform was recently introduced: Omics Tech Hub! After the success of our
first tech hub on GC-MS, next one (taking place on 17th of January at 3 pm)
will tackle Stable isotopes in LC-MS based metabolomics studies.
"""

EUPA_NEWS_DEFAULT = \
"""
<li>
  <b>EuPA/HUPO 2024 Conference</b> in
  Dresden, Germany October 20<sup>th</sup> – 24<sup>th</sup>, 2024, in the
  tradition of the German Proteomic Forum – the place to be for proteomics
  next year:
  <a href="https://www.hupo.org/event-5307330">
    https://www.hupo.org/
  </a>
</li>
<li>
  <b>EuPA Mental Health Workshop:</b>
  Breathe, rest and work will take place online on 24th of January at
  2 pm CET. If interested, register and join following this
  <a href="https://us06web.zoom.us/meeting/register/tZ0pcu6srjsoGta1fhbyRrDOf_7R-W-QHGZg#/registration">
    link.
  </a>
</li>
<li>
  The <b>EuPA 2025 Conference</b> will be hosted in Saint-Malo, France, on June 16<sup>th</sup>
  – 20<sup>th</sup>, 2025. Check it out:
  <a href="https://eupa.org/events/">
    https://eupa.org/events/
  </a>
</li>
<li>
  <b>EuBIC-MS Winter School 2024: </b> <br>
  The 2024 Winter School will be held on January 15<sup>th</sup>
  – 19<sup>th</sup>, 2024, in Winterberg, Germany. Save the date!
  <a href="https://eubic-ms.org/events/2024-winter-school/">
    https://eubic-ms.org/events/2024-winter-school/
  </a>
</li>
"""

NATIONAL_EVENTS_DEFAULT = \
"""
<li>
  <b>34th Mass Spec Forum 2024:</b> The 34th Mass Spec forum will take
  place from 21<sup>st</sup> to 23<sup>rd</sup> of February at the University of Vienna.This already a traditional
  event will cover mass spectrometry application across whole sphere of analytical chemistry. For more information
  For more information regarding the program and the speakers, check out their
  <a href="https://anchem.univie.ac.at/vortraege-lehr-veranstaltungen/massspec-forum-2024/">
    website.
  </a>
</li>
<li>
  Join and support <b>females in mass spectrometry</b>:
  <a href="https://femalesinms.com/">
    https://femalesinms.com/
  </a>
</li>
<li>
  <b>5th ESCP Symposium Vienna 2024:</b> An excellent networking opportunity in the field of single
  cell proteomics at IMP, Vienna, on August 27<sup>th</sup> to 28<sup>th</sup>,
  2024. Save the date!
</li>
"""

INTERNATIONAL_EVENTS_DEFAULT = \
"""
<li>
  <b>European School of Metabolomics</b>, will be held from
  April 22<sup>rd</sup>– 24<sup>th</sup>, 2024 in Grenada, Spain. Check it out!
  <a href="https://www.eusm2024.com/home">
    https://www.eusm2024.com
  </a>
</li>
<li>
  <b>Gordon Conference Toward Functional Lipidomics
    - Structure Elucidation, Quantification,
    Data Integration and Clinical Translation:</b>
  The event will take place from May 5<sup>th</sup>
  – 10<sup>th</sup>, 2024, in in Lucca, Tuscany, Italy.
  Have a look!
  <a href="https://www.grc.org/lipidomics-conference/2024/">
    GRC Lipidomics
  </a>
</li>
<li>
  <b>72nd ASMS Conference on Mass Spectrometry and Allied Topics:</b>
  ASMS 2024 will be held at the Anaheim Convention Center, Aneheim, CA from 2<sup>nd</sup> – 6<sup>th</sup> of June 2024!
  <a href="https://www.asms.org/conferences/annual-conference/annual-conference-homepage">
    ASMS
  </a>
</li>
<li>
  <b>25th International Mass Spectrometry Conference 2024:</b>
  IMSC2024 will take place from August 17<sup>th</sup> – 20<sup>th</sup>, 2024, in Melbourne, Australia. Have a look!
  <a href="https://imsc2024melbourne.com/">
    https://imsc2024melbourne.com/
  </a>
</li>
"""
