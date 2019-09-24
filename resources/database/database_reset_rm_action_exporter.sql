/* Clean Action Exporter DB */

TRUNCATE actionexporter.actionrequest CASCADE;
TRUNCATE actionexporter.address CASCADE;
TRUNCATE actionexporter.contact CASCADE;
TRUNCATE actionexporter.filerowcount CASCADE;

ALTER SEQUENCE actionexporter.actionrequestpkseq RESTART WITH 1;
ALTER SEQUENCE actionexporter.contactpkseq RESTART WITH 1;
