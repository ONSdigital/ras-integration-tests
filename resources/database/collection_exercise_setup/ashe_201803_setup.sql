insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('878c3462-766a-4cf6-8fb3-867d5124cc0a',7,'ASHE enrolment','Annual Survey of Hours and Earnings Enrolment','SYSTEM',now());

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('46a4cdc2-8995-4969-a02d-37f6be767efa',8,'ASHE','Annual Survey of Hours and Earnings','SYSTEM',now());

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(7,'B','878c3462-766a-4cf6-8fb3-867d5124cc0a','6aa8896f-ced5-4694-800c-6cd661b0c8b2');

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(8,'BI','46a4cdc2-8995-4969-a02d-37f6be767ef4','6aa8896f-ced5-4694-800c-6cd661b0c8b2');

update collectionexercise.collectionexercise
 set scheduledstartdatetime = '2017-09-11 23:00:00+00',
    scheduledexecutiondatetime ='2017-09-10 23:00:00+00',
    scheduledreturndatetime = '2018-02-28 00:00:00+00',
    scheduledenddatetime = '2018-06-29 23:00:00+00',
    periodstartdatetime = '2017-09-14 23:00:00+00',
    periodenddatetime = '2017-09-15 22:59:59+00'
    where id=(select id from collectionexercise.collectionexercise where survey_uuid = '6aa8896f-ced5-4694-800c-6cd661b0c8b2' and exerciseref='201803');
