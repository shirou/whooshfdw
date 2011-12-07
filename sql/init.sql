CREATE EXTENSION multicorn;  -- 拡張をいれる
CREATE SERVER whoosh_srv FOREIGN DATA WRAPPER multicorn options (
	wrapper 'whooshfdw.whooshfdw.WhooshFDW'
);
CREATE FOREIGN TABLE whooshtable(
	id numeric,
	title character varying
) server whoosh_srv options (
	indexdir '/tmp/indexdir'
);
