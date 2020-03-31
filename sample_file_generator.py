import csv, sys, getopt

with open("performance-test-sample.csv", "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=':')
        try:
            opts, args = getopt.getopt(sys.argv, "n:")
        except getopt.GetoptError:
            print('Usage: make performance RESPONDENTS=<number of respondents>')
            sys.exit(1)
        for opt, arg in opts:
            if opt == '-n':
                sampleunits = int(arg)
        formtype='0001'
        i = 1
        while i <= sampleunits:
            sampleunitref='499'+format(str(i), "0>8s")
            runame3=str(i)
            tradas3=str(i)
            region_code='WW'
            row=(   sampleunitref,
                    'H',
                    '75110',
                    '75110',
                    '84110',
                    '84110',
                    '3603',
                    '97281',
                    '9905249178',
                    '5',
                    'E',
                    region_code,
                    '07/08/2003',
                    'OFFICE FOR',
                    'NATIONAL STATISTICS',
                    runame3,
                    'OFFICE FOR',
                    'NATIONAL STATISTICS',
                    tradas3,
                    '',
                    '',
                    '',
                    'C',
                    '',
                    '1',
                    formtype,
                    'S')
            writer.writerow(row)
            i += 1