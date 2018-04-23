insert into survey.classifierType( classifiertypepk,classifiertypeselectorfk,classifiertype)
values(4,17,'COLLECTION_EXERCISE');

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('878c3462-766a-4cf6-8fb3-867d5124cc0f',3,'Bricks and Blocks Enrolment','Bricks and Blocks Enrolment','SYSTEM',now())
ON CONFLICT (actionplanpk) DO NOTHING;

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('46a4cdc2-8995-4969-a02d-37f6be767ef4',4,'Bricks and Blocks','Bricks and Blocks','SYSTEM',now())
ON CONFLICT (actionplanpk) DO NOTHING;

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(3,'B','878c3462-766a-4cf6-8fb3-867d5124cc0f','cb8accda-6118-4d3b-85a3-149e28960c54')
ON CONFLICT (casetypedefaultpk) DO NOTHING;

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(4,'BI','46a4cdc2-8995-4969-a02d-37f6be767ef4','cb8accda-6118-4d3b-85a3-149e28960c54')
ON CONFLICT (casetypedefaultpk) DO NOTHING;

update collectionexercise.collectionexercise
 set scheduledstartdatetime = '2017-09-11 23:00:00+00',
    scheduledexecutiondatetime ='2017-09-10 23:00:00+00',
    scheduledreturndatetime = '2018-02-28 00:00:00+00',
    scheduledenddatetime = '2018-06-29 23:00:00+00',
    periodstartdatetime = '2017-09-14 23:00:00+00',
    periodenddatetime = '2017-09-15 22:59:59+00'
    where id=(select id from collectionexercise.collectionexercise where survey_uuid = 'cb8accda-6118-4d3b-85a3-149e28960c54' and exerciseref='201801');