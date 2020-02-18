# collex-loader

The collex-loader package is a group of Python scripts for loading data as supplied by the business into the collection exercise service using JSON POST requests. It currently supports the loading of:
- [Collection exercises](data/CE_Details_for_loading_into_RM.csv) via the [load.py](load.py) script
- [Collection exercises events](data/2018_surveys_schedule.csv) via the [load_events.py](load_events.py) script

## example usage

### loading collection exercises
```
python load.py config/collex-config.json
```
### loading collection exercise events
```
python load_events.py config/event-config.json
```

## configuration

The load scripts require JSON configuration files to be supplied as the first command line parameter.  JSON was chosen for the configuration in place of YML as it requires no additional libraries to parse. 

### load.py configuration file

There is [an example of the configuration file](config/collex-config.json), repeated here for clarity.

```
{
    "inputFiles": ["data/CE_Details_for_loading_into_RM.csv"],
    "dryRun": false,
    "api":{
        "post-url": "http://localhost:8145/collectionexercises",
        "user": "admin",
        "password": "secret"
    },
    "columnMappings": {
        "Survey_Id": "surveyRef",
        "Collection_Period": "exerciseRef",
        "Collection_Period_Label": "userDescription"
    }
}
```

### load_events.py configuration file

There is [an example of the configuration file](config/event-config.json), repeated here for clarity.

```
{
    "inputFiles": ["data/023_2018_Schedule.csv", "data/073__2018_Schedule.csv", "data/134_2018_Schedule.csv", "data/139_2018_schedule.csv"],
    "dryRun": false,
    "api":{
        "post-url": "http://localhost:8145/collectionexercises/{id}/events",
        "get-url": "http://localhost:8145/collectionexercises/{exercise_ref}/survey/{survey_ref}",
        "user": "admin",
        "password": "secret"
    },
    "columnMappings": {
        "Survey Code": "surveyRef",
        "Survey Period": "exerciseRef"
    }
}
```
### field description

| Config item    | Description |
| -----------    | ----------- |
| inputFiles      | A list of the CSV files containing the collection exercise data to load |
| dryRun         | A boolean to indicate whether this is a dry run or not - see section on Dry Runs below | 
| api/post-url   | The URL to which  the loader script should post JSON in order to create collection exercises or events |
| api/get-url   | The URL load_events.py should use to look up a collection exercise by survey ref and exercise ref |
| api/user       | The the name of the basic auth user protecting the collection exercise service endpoint |
| api/password   | The the password of the basic auth user protecting the collection exercise service endpoint |
| columnMappings | A dictionary of column name mappings to apply to the rows in the CSV - key is CSV column name, value is the column as it should appear in the JSON output |

## dry runs

It is possible to get the loader to run in a test mode to examine the output it would produce. In order to do this, the dryRun flag in app-config.json should be set to true.  When this is set to true, instead of POSTing the JSON to the collection exercise service endpoint, the loader will dump it out to a file in the current directory with the following filename:

<survey_ref>-<exercise_ref>.json

For example, 134-201807.json
