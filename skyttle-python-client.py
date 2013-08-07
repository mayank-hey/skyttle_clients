# -*- coding: UTF-8 -*-

"""
Insert your MASHAPE_AUTH value below (it is available from "Keystore" on your
Mashape account)

Usage:

    python skyttle-python-client.py <language>

where `language` is one of: "en", "fr", "de", or "ru"
"""

import sys
import time
import json
import urllib
import urllib2


URL = "https://sentinelprojects-skyttle20.p.mashape.com/"
MASHAPE_AUTH = <your mashape key>


TEXTS = {
    'ru': """Мы были в этом ресторане и раньше и качество обслуживания было
    хорошим, но вчера мы были сильно разочарованы.""",

    'de': """Wir waren in diesem Restaurant auch früher gewesen,
    und das Essen war ok, aber dieses Mal waren wir sehr enttäuscht.""",

    'en': """We have visited this restaurant a few times in the past, and the
    meals have been ok, but this time we were deeply disappointed.""",

    'fr': """Nous avons visité ce restaurant plusieurs fois avant, et la
    nourriture n'était pas mal, mais cette fois nous avons été très déçus.""",
}


def main(lang='en'):

    keywords = 1
    sentiment = 1
    annotate = 1
    domain = 'hospitality'
    text = TEXTS[lang]

    start = time.time()

    opener = urllib2.build_opener(urllib2.HTTPHandler)
    params = {'text': text, 'lang': lang, 'keywords': keywords,
              'sentiment': sentiment, 'annotate': annotate, 'domain': domain}
    headers = {'X-Mashape-Authorization': MASHAPE_AUTH}

    request = urllib2.Request(URL, urllib.urlencode(params), headers=headers)
    response = opener.open(request)
    opener.close()
    duration = time.time() - start
    data = json.loads(response.read())

    print 'RESPONSE HEADERS:'
    print response.headers
    print
    print 'DATA:'
    print data
    print
    print '='*79
    print 'RESPONSE:'
    print '='*79
    for doc in data['docs']:
        print 'Doc id: %s' % doc['doc_id']
        if keywords:
            print 'TERMS:'
            for term in doc.get('terms', []):
                line = '%s\t%s\t%d' % (term['id'], term['term'], term['count'])
                print line.encode('utf8')
            print '-'*79
        if sentiment:
            print 'SENTIMENT:'
            for sw in doc.get('sentiment', []):
                line = "%s\t%s" % (sw['text'], sw['polarity'])
                print line.encode('utf8')
            print '-'*79
            print 'DOCUMENT SENTIMENT:'
            for k, v in doc.get('sentiment_scores', {}).items():
                print k, v
            print '-'*79
        if annotate:
            print 'ANNOTATED TEXT:'
            print doc.get('doc_text', '')
            print '-'*79

    print 'Took %f secs' % duration

main(lang=sys.argv[1])
