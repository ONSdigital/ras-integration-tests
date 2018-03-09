/* Populate secure message with 3 messages with the same thread id  and survey so that they can be aggregated in the same a conversation */

INSERT INTO securemessage.secure_message( msg_id, subject, body, thread_id, collection_case,
                                                 ru_id, collection_exercise, survey, from_internal) VALUES
  ('fb0e79bd-e132-4f4f-a7fd-5e8c6b41b9af', 'This is a subject', 'This is the message body',
   'fb0e79bd-e132-4f4f-a7fd-5e8c6b41b9af','', 'fdf8ba40-7ed7-4463-bb0f-69a5dc683b79', '',
   'cb8accda-6118-4d3b-85a3-149e28960c54', True);

INSERT INTO securemessage.secure_message( msg_id, subject, body, thread_id, collection_case,
                                                 ru_id, collection_exercise, survey, from_internal) VALUES
  ('gb0e79bd-e132-5f5f-a7fd-5e8c6b41b9af', 'This is a subject', 'This is the message body',
   'fb0e79bd-e132-4f4f-a7fd-5e8c6b41b9af','', 'fdf8ba40-7ed7-4463-bb0f-69a5dc683b79', '',
   'cb8accda-6118-4d3b-85a3-149e28960c54', FALSE);


INSERT INTO securemessage.secure_message( msg_id, subject, body, thread_id, collection_case,
                                                 ru_id, collection_exercise, survey, from_internal) VALUES
  ('hb0e79bd-e132-6f6f-a7fd-5e8c6b41b9af', 'This is a subject', 'This is the message body',
   'fb0e79bd-e132-4f4f-a7fd-5e8c6b41b9af','', 'fdf8ba40-7ed7-4463-bb0f-69a5dc683b79', '',
   'cb8accda-6118-4d3b-85a3-149e28960c54', True );


/* Populate status table with the correlated rows. Two for internal and one for external*/


INSERT INTO securemessage.status(label, msg_id,actor) VALUES ('SENT' , 'fb0e79bd-e132-4f4f-a7fd-5e8c6b41b9af', '0d7b3e2e-4c0c-4479-a002-09f8328f7292' );
INSERT INTO securemessage.status(label, msg_id,actor) VALUES ('INBOX' , 'gb0e79bd-e132-5f5f-a7fd-5e8c6b41b9af', '633330a6-aa84-4d1e-8e5d-2bafa9e3dac5' );
INSERT INTO securemessage.status(label, msg_id,actor) VALUES ('SENT' , 'hb0e79bd-e132-6f6f-a7fd-5e8c6b41b9af', '0d7b3e2e-4c0c-4479-a002-09f8328f7292' );


/* Populate event table  */

INSERT INTO securemessage.events(event, msg_id, date_time) VALUES('READ', 'fb0e79bd-e132-4f4f-a7fd-5e8c6b41b9af', '2017-02-03 00:00:00');
INSERT INTO securemessage.events(event, msg_id, date_time) VALUES('SENT', 'gb0e79bd-e132-5f5f-a7fd-5e8c6b41b9af', '2017-02-04 00:00:00');
INSERT INTO securemessage.events(event, msg_id, date_time) VALUES('READ', 'hb0e79bd-e132-6f6f-a7fd-5e8c6b41b9af', '2017-02-05 00:00:00');
