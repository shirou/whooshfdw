#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from whoosh import index
from whoosh.fields import Schema, STORED, NGRAM
from whoosh.qparser import QueryParser
from whoosh.analysis import NgramAnalyzer

INDEX_DIR = "/tmp/indexdir"
schema = Schema(title=NGRAM(stored=True))


def open_index(indexdir):
    if not os.path.exists(indexdir):
        os.mkdir(indexdir)
        index.create_in(indexdir, schema)

    return index.open_dir(indexdir)


def register(filename, indexdir=INDEX_DIR):
    ix = open_index(indexdir)
    writer = ix.writer()

    for line in open(filename):
        writer.add_document(title=line.strip().decode('utf-8'))

    writer.commit(optimize=True)
    ix.close()


if __name__ == '__main__':
    register("/tmp/jawiki-20111111-all-titles-in-ns0")
    #register("/tmp/top1000")
