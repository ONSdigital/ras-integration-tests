/* Clean Party DB */

TRUNCATE securemessage.events CASCADE;
TRUNCATE securemessage.secure_message CASCADE;
TRUNCATE securemessage.status CASCADE;

ALTER SEQUENCE securemessage.events_id_seq RESTART WITH 1;
ALTER SEQUENCE securemessage.secure_message_id_seq RESTART WITH 1;
ALTER SEQUENCE securemessage.status_id_seq RESTART WITH 1;
