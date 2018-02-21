INSERT INTO securemessage.secure_message
(msg_id, subject, body, thread_id, collection_case, ru_id, collection_exercise, survey) VALUES
('611d8e8e-3722-47c7-80ff-3130da39bdeb', 'test', 'test body', '611d8e8e-3722-47c7-80ff-3130da39bdeb', 'CC_PLACEHOLDER', 'c614e64e-d981-4eba-b016-d9822f09a4fb', '', 'BRES 2017'),
('5f24d0ae-a9a9-41f8-877f-b83051e6b1bf', 'test2', 'test body2', '611d8e8e-3722-47c7-80ff-3130da39bdeb', 'CC_PLACEHOLDER', 'c614e64e-d981-4eba-b016-d9822f09a4fb', '', 'BRES 2017');

INSERT INTO securemessage.actors
(msg_id, from_actor, to_actor, sent_from_internal) VALUES
('611d8e8e-3722-47c7-80ff-3130da39bdeb', 'BRES', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712', true),
('5f24d0ae-a9a9-41f8-877f-b83051e6b1bf', 'BRES', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712', true);

INSERT INTO securemessage.events
(event, msg_id, date_time) VALUES
('Sent', '611d8e8e-3722-47c7-80ff-3130da39bdeb', '2018-02-20 16:22:40.022'),
('Sent', '5f24d0ae-a9a9-41f8-877f-b83051e6b1bf', '2018-02-20 17:45:05.022');

INSERT INTO securemessage.status
(label, msg_id, actor) VALUES
('SENT', '611d8e8e-3722-47c7-80ff-3130da39bdeb', 'BRES'),
('INBOX', '611d8e8e-3722-47c7-80ff-3130da39bdeb', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712'),
('UNREAD', '611d8e8e-3722-47c7-80ff-3130da39bdeb', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712'),
('SENT', '5f24d0ae-a9a9-41f8-877f-b83051e6b1bf', 'BRES'),
('INBOX', '5f24d0ae-a9a9-41f8-877f-b83051e6b1bf', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712'),
('UNREAD', '5f24d0ae-a9a9-41f8-877f-b83051e6b1bf', 'f62dfda8-73b0-4e0e-97cf-1b06327a6712');
