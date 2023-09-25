import csv

def main():

    f = open("./data/clean_data.csv","r")
    csv_reader = csv.DictReader(f)
    csv_list = list(csv_reader)

    years = []
    for line in csv_list:
        years.append(line['Year'])

    print('Year'.ljust(15) + 'Average Temperature Anomaly(F)')

    for current_decade in range(int(min(years)),int(max(years)),10):
        year_count = 0
        sum_anomly_decade = 0
        for line in csv_list:
            if (int(line['Year'])//10)*10 == current_decade:
                year_count+=1
                avg_anomly_year = (float(line['Jan']) + float(line['Feb']) + float(line['Mar']) + float(line['Apr']) + float(line['May']) + float(line['Jun']) + float(line['Jul']) + float(line['Aug']) + float(line['Sep']) + float(line['Oct']) + float(line['Nov']) + float(line['Dec']))/12
                sum_anomly_decade += avg_anomly_year
        result = round(sum_anomly_decade/year_count, 2)

        print(str(current_decade) + "-" + str(current_decade+year_count-1).ljust(10) +  str(result).rjust(5))
        
    f.close()

if __name__ == "__main__":
    main()