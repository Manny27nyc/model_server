#
# Copyright (c) 2021 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import urllib.request
import re
from html.parser import HTMLParser
import logging as log

class HTMLDataExtractor(HTMLParser):
    def __init__(self, tags):
        super(HTMLDataExtractor, self).__init__()
        self.started_tags = {k:[] for k in tags}
        self.ended_tags = {k:[] for k in tags}

    def handle_starttag(self, tag, attrs):
        if tag in self.started_tags:
            self.started_tags[tag].append([])

    def handle_endtag(self, tag):
        if tag in self.ended_tags:
            txt = ''.join(self.started_tags[tag].pop())
            self.ended_tags[tag].append(txt)

    def handle_data(self, data):
        for tag, l in self.started_tags.items():
            for d in l:
                d.append(data)

# read html urls and list of all paragraphs data
def get_paragraphs(url_list):
    paragraphs_all = []
    for url in url_list:
        log.info("Get paragraphs from {}".format(url))
        with urllib.request.urlopen(url) as response:
            parser = HTMLDataExtractor(['title', 'p'])
            charset='utf-8'
            if 'Content-type' in response.headers:
                m = re.match('.*charset=(\S+).*', response.headers['Content-type'])
                if m:
                    charset = m.group(1)
            data = response.read()
            parser.feed(data.decode(charset))
            title = ' '.join(parser.ended_tags['title'])
            paragraphs = parser.ended_tags['p']
            log.info("Page '{}' has {} chars in {} paragraphs".format(title, sum(len(p) for p in paragraphs), len(paragraphs)))
            paragraphs_all.extend(paragraphs)

    return paragraphs_all
