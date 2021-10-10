import csv
from os import listdir
from os.path import join

path_source_data = "02-src-data"

output_file = "processed_data/output.csv"
output = [['user_id', 'first_name', 'last_name', 'birthts', 'img_path']]

files = listdir(path_source_data)

for file in files:
    used_id = file[:-4]
    path = join(path_source_data, file)
    if file[-3:] == "csv":
        with open(path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            skip_filed_name = False


            for line in csv_reader:
                if not skip_filed_name:
                    skip_filed_name = True
                    continue

                output.append([used_id, line[0], line[1], line[2], join(path_source_data, used_id + '.png')])

with open(output_file, mode='w') as writer_file:
    writer_csv = csv.writer(writer_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer_csv.writerows(output)

