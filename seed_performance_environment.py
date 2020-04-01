from common.collection_exercise_utilities import execute_collection_exercise, poll_database_for_iac
from common.respondent_utilities import register_respondent
import csv, sys

survey_id = '02b9c366-7397-42f7-942a-76dc5876d86d'
period = '1806'

def main():
    respondents = int(sys.argv[2])
    print('Executing collection exercise')
    execute_collection_exercise(survey_id, period, ci_type='eQ', performance_test=True)
    print('Waiting for collection exercises to finish executing')
    poll_database_for_iac(survey_id=survey_id, period=period, count=respondents)
    print('Collection exercises have finished executing, registering respondents')
    i = 1
    with open("performance-test-accounts.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        while i <= respondents:
            sampleunitref = '499' + format(str(i), "0>8s")
            print('Attempting to register user '+ sampleunitref + "@test.com")
            register_respondent(survey_id=survey_id, period=period,
                                username=sampleunitref + "@test.com", ru_ref=sampleunitref)
            writer.writerow([sampleunitref + "@test.com"])
            i += 1

if __name__ == '__main__':
    main()
