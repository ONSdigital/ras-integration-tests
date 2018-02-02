/* Clean Party DB */

TRUNCATE partysvc.business CASCADE;
TRUNCATE partysvc.business_attributes CASCADE;
TRUNCATE partysvc.business_respondent CASCADE;
TRUNCATE partysvc.enrolment CASCADE;
TRUNCATE partysvc.pending_enrolment CASCADE;
TRUNCATE partysvc.respondent CASCADE;

ALTER SEQUENCE partysvc.business_attributes_id_seq RESTART WITH 1;
ALTER SEQUENCE partysvc.pending_enrolment_id_seq RESTART WITH 1;
ALTER SEQUENCE partysvc.respondent_id_seq RESTART WITH 1;
