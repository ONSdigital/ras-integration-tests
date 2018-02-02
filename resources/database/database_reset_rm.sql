/* Clean Sample DB */

TRUNCATE sample.samplesummary CASCADE;
TRUNCATE sample.sampleunit CASCADE;
TRUNCATE sample.collectionexercisejob CASCADE;

ALTER SEQUENCE sample.samplesummaryseq RESTART WITH 1;
ALTER SEQUENCE sample.sampleunitseq RESTART WITH 1;
ALTER SEQUENCE sample.collectionexercisejobseq RESTART WITH 1;


/* Clean Notify Gateway DB */

TRUNCATE notifygatewaysvc.message CASCADE;

ALTER SEQUENCE notifygatewaysvc.messageseq RESTART WITH 1;


/* Clean And Reset Collection Exercise DB */

TRUNCATE collectionexercise.sampleunit CASCADE;
TRUNCATE collectionexercise.sampleunitgroup CASCADE;

ALTER SEQUENCE collectionexercise.sampleunitgrouppkseq RESTART WITH 1;
ALTER SEQUENCE collectionexercise.sampleunitpkseq RESTART WITH 1;

UPDATE collectionexercise.collectionexercise SET statefk = 'INIT';
DELETE FROM collectionexercise.samplelink;


/* Clean Case DB */

TRUNCATE casesvc.case CASCADE;
TRUNCATE casesvc.caseevent CASCADE;
TRUNCATE casesvc.casegroup CASCADE;
TRUNCATE casesvc.response CASCADE;

ALTER SEQUENCE casesvc.caseeventseq RESTART WITH 1;
ALTER SEQUENCE casesvc.casegroupseq RESTART WITH 1;
ALTER SEQUENCE casesvc.caseseq RESTART WITH 1;
ALTER SEQUENCE casesvc.caserefseq RESTART WITH 1000000000000001;
ALTER SEQUENCE casesvc.responseseq RESTART WITH 1;


/* Clean Action DB */

TRUNCATE action.action CASCADE;
TRUNCATE action.actionplanjob CASCADE;
TRUNCATE action.case CASCADE;
TRUNCATE action.messagelog CASCADE;
TRUNCATE action.actionrule CASCADE;

ALTER SEQUENCE action.actionpkseq RESTART WITH 1;
ALTER SEQUENCE action.actionplanjobseq RESTART WITH 1;
ALTER SEQUENCE action.casepkseq RESTART WITH 1;
ALTER SEQUENCE action.messageseq RESTART WITH 1;


/* Clean Action Exporter DB */

TRUNCATE actionexporter.actionrequest CASCADE;
TRUNCATE actionexporter.address CASCADE;
TRUNCATE actionexporter.contact CASCADE;
TRUNCATE actionexporter.filerowcount CASCADE;
TRUNCATE actionexporter.report CASCADE;

ALTER SEQUENCE actionexporter.actionrequestpkseq RESTART WITH 1;
ALTER SEQUENCE actionexporter.contactpkseq RESTART WITH 1;
ALTER SEQUENCE actionexporter.reportpkseq RESTART WITH 1;


/* Notification Action Seed */

SET SCHEMA 'action';

INSERT INTO action.actionrule (actionrulepk, actionplanfk, actiontypefk, name, description, daysoffset, priority)
VALUES (1, 1, 1, 'BSNOT+0', 'Enrolment Invitation Letter(+0 days)', 0, 3);
