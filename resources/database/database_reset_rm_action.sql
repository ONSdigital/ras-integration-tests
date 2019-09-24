/* Clean Action DB */

TRUNCATE action.action CASCADE;
TRUNCATE action.actionplanjob CASCADE;
TRUNCATE action.case CASCADE;
TRUNCATE action.messagelog CASCADE;
TRUNCATE action.actionplan CASCADE;
TRUNCATE action.actionrule CASCADE;

ALTER SEQUENCE action.actionpkseq RESTART WITH 1;
ALTER SEQUENCE action.actionplanjobseq RESTART WITH 1;
ALTER SEQUENCE action.casepkseq RESTART WITH 1;
ALTER SEQUENCE action.messageseq RESTART WITH 1;
