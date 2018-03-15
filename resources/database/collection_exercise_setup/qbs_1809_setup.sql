insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('67ef4dc2-8995-4969-a02d-37f6be746a4c',5,'QBS Enrolment','QBS Enrolment','SYSTEM',now());

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('67ef4dc2-8995-4969-a02d-37f6be746777',6,'QBS','QBS','SYSTEM',now());

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(5,'B','67ef4dc2-8995-4969-a02d-37f6be746a4c','02b9c366-7397-42f7-942a-76dc5876d86d');

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(6,'BI','67ef4dc2-8995-4969-a02d-37f6be746777','02b9c366-7397-42f7-942a-76dc5876d86d');


update collectionexercise.collectionexercise
 set scheduledstartdatetime = '2017-09-11 23:00:00+00',
    scheduledexecutiondatetime ='2017-09-10 23:00:00+00',
    scheduledreturndatetime = '2018-02-28 00:00:00+00',
    scheduledenddatetime = '2018-06-29 23:00:00+00',
    periodstartdatetime = '2017-09-14 23:00:00+00',
    periodenddatetime = '2017-09-15 22:59:59+00'
    where id=(select id from collectionexercise.collectionexercise where survey_uuid = '02b9c366-7397-42f7-942a-76dc5876d86d' and exerciseref='1809');

update collectionexercise.event
    set timestamp='2017-09-11 23:00:00+00'
    where eventpk=(select e.eventpk
    from collectionexercise.event e
    inner join collectionexercise.collectionexercise ce
    on ce.exercisepk=e.collexfk
    where ce.survey_uuid='02b9c366-7397-42f7-942a-76dc5876d86d' and ce.exerciseref='1809' and e.tag='go_live')
