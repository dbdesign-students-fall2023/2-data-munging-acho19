def main(): 
    f = open('./data/data.txt', 'r',encoding='utf-8')
    d = open('./data/clean_data.csv', 'w',encoding='utf-8')
    lines = f.readlines()
    header = lines[7] # header for comparison purposes
    top_header = header.split()
    top_header = top_header[:-7]
    top_header = ','.join(top_header) + '\n'
    d.write(top_header) 
    for line in lines[8:-13]: # take out the first 8 lines and the last 8 lines 
        if line.strip():
            if header != line: #check to see if it is not the header
                line = line.split()
                line = line[:-7]
                result = []
                for i in range(len(line)):
                    if int(line[i]) < 1700: 
                        Celsius = (int(line[i])/100)
                        Faren = Celsius * 1.8 
                        result.append('{:.1f}'.format(Faren))
                    else: 
                        result.append(line[i])
                result = ','.join(result) + '\n'
                d.write(result)
    f.close()
    d.close()

if __name__ == "__main__":
    main()   