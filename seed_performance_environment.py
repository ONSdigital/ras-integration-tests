from common.collection_exercise_utilities import execute_collection_exercise, poll_database_for_iac

def main():
    print('Executing collection exercise')
    execute_collection_exercise('02b9c366-7397-42f7-942a-76dc5876d86d', '1806', ci_type='eQ', performance_test=True)
    print('Waiting for collection exercises to finish executing')
    poll_database_for_iac(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d', period='1806')
    print('Collection exercises have finished executing')

if __name__ == '__main__':
    main()
