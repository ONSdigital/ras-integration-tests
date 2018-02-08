update collectionexercise.collectionexercise
 set scheduledstartdatetime = '2018-12-11 23:00:00+00',
    scheduledexecutiondatetime ='2017-09-10 23:00:00+00',
    scheduledreturndatetime = '2018-02-28 00:00:00+00',
    scheduledenddatetime = '2018-06-29 23:00:00+00',
    periodstartdatetime = '2017-09-14 23:00:00+00',
    periodenddatetime = '2017-09-15 22:59:59+00'
    where id=(select id from collectionexercise.collectionexercise where survey_uuid = 'cb8accda-6118-4d3b-85a3-149e28960c54' and exerciseref='201812');