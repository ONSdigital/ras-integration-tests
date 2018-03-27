insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('878c3462-766a-4cf6-8fb3-867d5124cc0a',7,'ASHE enrolment','Annual Survey of Hours and Earnings Enrolment','SYSTEM',now());

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('46a4cdc2-8995-4969-a02d-37f6be767efa',8,'ASHE','Annual Survey of Hours and Earnings','SYSTEM',now());

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(7,'B','878c3462-766a-4cf6-8fb3-867d5124cc0a','6aa8896f-ced5-4694-800c-6cd661b0c8b2');

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(8,'BI','46a4cdc2-8995-4969-a02d-37f6be767ef4','6aa8896f-ced5-4694-800c-6cd661b0c8b2');