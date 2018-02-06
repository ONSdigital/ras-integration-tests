insert into survey.classifierType( classifiertypepk,classifiertypeselectorfk,classifiertype)
values(5,15,'COLLECTION_EXERCISE');

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('878c3462-766a-4cf6-8fb3-867d5124cc0f',3,'Bricks and Blocks Enrolment','Bricks and Blocks Enrolment','SYSTEM',now());

insert into action.actionplan(id, actionplanpk, name, description, createdby, lastrundatetime)
values('46a4cdc2-8995-4969-a02d-37f6be767ef4',4,'Bricks and Blocks','Bricks and Blocks','SYSTEM',now());

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(5,'B','878c3462-766a-4cf6-8fb3-867d5124cc0f','9b6872eb-28ee-4c09-b705-c3ab1bb0f9ec');

insert into collectionexercise.casetypedefault(casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid)
values(6,'BI','46a4cdc2-8995-4969-a02d-37f6be767ef4','9b6872eb-28ee-4c09-b705-c3ab1bb0f9ec');