#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from whoosh import index
from whoosh.fields import Schema, STORED, NGRAM
from whoosh.qparser import QueryParser
from whoosh.analysis import NgramAnalyzer

from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres


class WhooshFDW(ForeignDataWrapper):

    def __init__(self, options, columns):
        super(WhooshFDW, self).__init__(options, columns)
        self.columns = columns
        self.indexdir = options["indexdir"]
        self.schema = Schema(title=NGRAM(stored=True))

    def open_index(self, indexdir, schema):
        '''indexを開きます。なければ作ります。'''
        if not os.path.exists(indexdir):
            os.mkdir(indexdir)
            index.create_in(indexdir, schema)
        return index.open_dir(indexdir)

    def execute(self, quals, columns):
        '''multicornによって呼び出されます'''
        ix = self.open_index(self.indexdir, self.schema)

        parser = QueryParser("title", schema=ix.schema)

        for query in quals:
            q = parser.parse(query.value.replace("%", ""))  # %はいらない
            with ix.searcher() as searcher:
                count = 1
                for r in searcher.search(q):
                    res = {'id': count,
                           'title': r["title"].encode('utf-8')}
                    yield res
                    count += 1
        ix.close()
