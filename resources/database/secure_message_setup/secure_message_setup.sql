INSERT INTO securemessage.actors
(id, msg_id, from_actor, to_actor, sent_from_internal)
VALUES(1, '005fa2f2-83fe-4127-8c71-2cd6f6baf1bd', 'BRES', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712', true);


INSERT INTO securemessage.secure_message
(id, msg_id, subject, body, thread_id, collection_case, ru_id, collection_exercise, survey)
VALUES(1, '005fa2f2-83fe-4127-8c71-2cd6f6baf1bd', 'test subject', 'test body', '005fa2f2-83fe-4127-8c71-2cd6f6baf1bd', 'CC_PLACEHOLDER', 'c614e64e-d981-4eba-b016-d9822f09a4fb', '', 'BRES 2017');

INSERT INTO securemessage.status (id, label, msg_id, actor) VALUES
(1, 'SENT', '005fa2f2-83fe-4127-8c71-2cd6f6baf1bd', 'BRES'),
(2, 'INBOX', '005fa2f2-83fe-4127-8c71-2cd6f6baf1bd', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712'),
(3, 'UNREAD', '005fa2f2-83fe-4127-8c71-2cd6f6baf1bd', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712');
