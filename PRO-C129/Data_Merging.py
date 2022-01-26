import csv

df1 = []
df2 = []

with open('Sample_1.csv', 'r', encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        df1.append(row[1:])

with open("Sample2_Sorted.csv", "r", encoding='utf-8') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        df2.append(row)

headers_1 = df1[0]
planet_df1 = df1[1:]

headers_2 = df2[0]
planet_df2 = df2[1:]

headers = headers_2 + headers_1
planet_data = []
for index, data_row in enumerate(planet_df2):
    planet_data.append(planet_df2[index] + planet_df1[index])

with open("Final.csv", "w", encoding='utf-8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
