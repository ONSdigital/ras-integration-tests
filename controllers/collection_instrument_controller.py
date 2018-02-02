from acceptance_tests.features.steps.common import signed_in_rops
from acceptance_tests.features.pages import collection_exercise_details


def load_collection_instrument_bricks_201801():
    signed_in_rops()
    collection_exercise_details.go_to('Bricks', '201801')
    collection_exercise_details.load_collection_instrument(
        test_file='resources/collection_instrument_files/064_0001_201803.xlsx')
