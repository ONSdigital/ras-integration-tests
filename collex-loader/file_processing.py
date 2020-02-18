import csv

def map_columns(column_mappings, row):
    new_row = dict()
    for key, value in row.items():
        try:
            if key and value:
                new_row[column_mappings[key] if column_mappings[key] else key] = value
        except KeyError:
           new_row[key] = value 
    return new_row

def process_file(filename, row_handler, column_mappings):
    with open(filename) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            new_row = map_columns(column_mappings, row)

            if new_row:
                row_handler(data=new_row)

def process_files(file_list, row_handler, column_mappings):
    for filename in file_list:
        process_file(filename, row_handler, column_mappings)


