from controllers import collection_instrument_controller

if __name__ == '__main__':
    print("Adding initial data required for executing collection exercises")
    # Upload eQ collection instrument for QBS
    collection_instrument_controller.upload_eq_collection_instrument(survey_id='02b9c366-7397-42f7-942a-76dc5876d86d',
                                                                     form_type='0001', eq_id='2')
    print("Required collection exercises can be executed")
