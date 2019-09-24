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

/* Remove test surveys (deemed to be any survey with survey ref > 999) */

DELETE FROM survey.classifiertype WHERE classifiertypeselectorfk IN (SELECT classifiertypeselectorpk from survey.classifiertypeselector cts JOIN survey.survey s ON cts.surveyfk = s.surveypk WHERE CASE WHEN surveyref ~ '[^0-9]' THEN 0 ELSE surveyref::integer END > 999);
DELETE FROM survey.classifiertypeselector WHERE surveyfk IN (SELECT surveypk FROM survey.survey WHERE CASE WHEN surveyref ~ '[^0-9]' THEN 0 ELSE surveyref::integer END > 999);
DELETE FROM survey.survey WHERE CASE WHEN surveyref ~ '[^0-9]' THEN 0 ELSE surveyref::integer END > 999;
UPDATE survey.survey SET shortname = 'NBS', longname = 'National Balance Sheet' WHERE id = '7a2c9d6c-9aaf-4cf0-a68c-1d50b3f1b296' and surveyref = '199';

/* Clean And Reset Collection Exercise DB */

TRUNCATE collectionexercise.sampleunit CASCADE;
TRUNCATE collectionexercise.sampleunitgroup CASCADE;
TRUNCATE collectionexercise.samplelink CASCADE;
TRUNCATE collectionexercise.collectionexercise CASCADE;
TRUNCATE collectionexercise.casetypedefault CASCADE;
TRUNCATE collectionexercise.casetypeoverride CASCADE;


ALTER SEQUENCE collectionexercise.casetypedefaultseq RESTART WITH 1;
ALTER SEQUENCE collectionexercise.casetypeoverrideseq RESTART WITH 1;
ALTER SEQUENCE collectionexercise.sampleunitgrouppkseq RESTART WITH 1;
ALTER SEQUENCE collectionexercise.sampleunitpkseq RESTART WITH 1;
ALTER SEQUENCE collectionexercise.samplelinkpkseq RESTART WITH 1;