import csv

datafile = list(csv.reader(open("neural_map.csv")))

def write_to_csv(data):
   with open("neural_map.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(data)