/* Populate action rules for ready for live */

INSERT INTO action.actionplan (actionplanpk, id, name, description, createdby )
VALUES ( 1000002, '2908e8c5-dbb8-4ce6-9383-ab16a8224b75', 'MBS Enrol', 'Monthly Business Enrolment', 'SYSTEM')
ON CONFLICT (actionplanpk) DO NOTHING;

INSERT INTO action.actionplan (actionplanpk, id, name, description, createdby )
VALUES ( 1000003, '90dd5b4f-381f-4766-a19b-a8346a7cdba1', 'MBS', 'Monthly Business', 'SYSTEM')
ON CONFLICT (actionplanpk) DO NOTHING;

INSERT INTO collectionexercise.casetypedefault ( casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid )
VALUES ( 1000002, 'B', '2908e8c5-dbb8-4ce6-9383-ab16a8224b75', '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c' )
ON CONFLICT (casetypedefaultpk) DO NOTHING;
INSERT INTO collectionexercise.casetypedefault ( casetypedefaultpk, sampleunittypefk, actionplanid, survey_uuid )
VALUES ( 1000003, 'BI', '90dd5b4f-381f-4766-a19b-a8346a7cdba1', '75b19ea0-69a4-4c58-8d7f-4458c8f43f5c' )
ON CONFLICT (casetypedefaultpk) DO NOTHING;

INSERT INTO action.actionrule (id, actionrulepk, actionplanfk, actiontypefk, name, description, daysoffset, priority)
VALUES ('205f3512-eb6e-419d-81fb-d563f8b27bb3', 1000003, 1000002, 1, 'MBSENR', 'Enrolment', 0, 3)
ON CONFLICT (actionrulepk) DO NOTHING;

INSERT INTO action.actionrule (id, actionrulepk, actionplanfk, actiontypefk, name, description, daysoffset, priority)
VALUES ('bc71fc5f-eac3-4d96-a04b-89c593a0e8b1', 1000004, 1000002, 2, 'MbSREM1', 'Enrolment Reminder', 45, 3)
ON CONFLICT (actionrulepk) DO NOTHING;

INSERT INTO action.actionrule (id, actionrulepk, actionplanfk, actiontypefk, name, description, daysoffset, priority)
VALUES ('a1232e28-7268-481b-b0d0-b4cd8c49e5b1', 1000005, 1000003, 3, 'MbSREM2', 'Survey Reminder', 45, 3)
ON CONFLICT (actionrulepk) DO NOTHING;
