/* Clean Party DB */

TRUNCATE securemessage.actors CASCADE;
TRUNCATE securemessage.events CASCADE;
TRUNCATE securemessage.internal_sent_audit CASCADE;
TRUNCATE securemessage.secure_message CASCADE;
TRUNCATE securemessage.status CASCADE;

ALTER SEQUENCE securemessage.actors_id_seq RESTART WITH 1;
ALTER SEQUENCE securemessage.events_id_seq RESTART WITH 1;
ALTER SEQUENCE securemessage.internal_sent_audit_id_seq RESTART WITH 1;
ALTER SEQUENCE securemessage.secure_message_id_seq RESTART WITH 1;
ALTER SEQUENCE securemessage.status_id_seq RESTART WITH 1;
