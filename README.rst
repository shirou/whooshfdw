Whooshfdw
====================

Whooshfdw is a sample of PostgreSQL FDW(Foreign Data Wrappers). This
can search text file using Whoosh, pure python full text search engine.


Requirement
-----------

- PostgreSQL 9.1 or above
- multicorn (http://multicorn.org/)
- Whoosh (http://packages.python.org/Whoosh/)

How to use
----------

Install
++++++++++++++++


::

  % sudo pip install pgxnclient
  % sudo pip install whoosh
  % sudo pip install -e "hg+http://bitbucket.org/r_rudi/whooshfdw#egg=whooshfdw"

  % sudo pgxn install multicorn --testing


You must install whoosh and whooshfdw to system wide because
PostgreSQL server need to run these software. This means please do not
use virtualenv.


create whoosh index
+++++++++++++++++++

You should create a whoosh index before search. Whooshfdw have a
simple create index module.

Before running this python script, please download wikipedia dump
(http://dumps.wikimedia.org/jawiki/20111203/) and uncompress into the /tmp.

::

  from whooshfdw import register

  register.register(file='/tmp/jawiki-20111203-all-titles-in-ns0',
                    indexdir='/tmp/indexdir')


Table Setup
+++++++++++

::

  CREATE EXTENSION multicorn;  -- Install multicorn to your DB
  CREATE SERVER whoosh_srv FOREIGN DATA WRAPPER multicorn options (
          wrapper 'whooshfdw.whooshfdw.WhooshFDW' -- create Server
  );
  CREATE FOREIGN TABLE whooshtable( -- create FOREIGN TABLE
          id numeric,
          title character varying
  ) server whoosh_srv options (
          indexdir '/tmp/indexdir'  -- set the Index directory
  );


Query
+++++

::

  % psql -c "SELECT * from whooshtable where title LIKE '%what%';"



LICENSE
-------

new BSD.

