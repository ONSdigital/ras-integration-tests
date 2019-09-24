/* Clean Case DB */

TRUNCATE casesvc.case CASCADE;
TRUNCATE casesvc.caseevent CASCADE;
TRUNCATE casesvc.casegroup CASCADE;
TRUNCATE casesvc.response CASCADE;
TRUNCATE casesvc.caseiacaudit CASCADE;

ALTER SEQUENCE casesvc.caseeventseq RESTART WITH 1;
ALTER SEQUENCE casesvc.casegroupseq RESTART WITH 1;
ALTER SEQUENCE casesvc.caseseq RESTART WITH 1;
ALTER SEQUENCE casesvc.caserefseq RESTART WITH 1000000000000001;
ALTER SEQUENCE casesvc.responseseq RESTART WITH 1;
ALTER SEQUENCE casesvc.caseiacauditseq RESTART WITH 1;
