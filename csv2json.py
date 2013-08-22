import sys
import json
import csv

def main():

    if sys.argv[1] == 'help':
        printHelp()
    else:
        convert2json()


def convert2json():
    
    separator = ","    
    try:
        separator = str(sys.argv[4])
    except:
        pass
    
    try:
        datamodelfile = csv.reader(open(sys.argv[1], "rU"), delimiter=separator, dialect="excel")
        datafile = open(sys.argv[2], "rU")
        outfile = open(sys.argv[3], 'a')
    except:
        print "The parameters for this script are: csv_data_model_file csv_input_data_file output_file separator"

    datamodel = []
    for row in datamodelfile:
        datamodel = row
        
    data = csv.reader(datafile, delimiter=separator)
    
    
    for row in data:
        if len(row) == len(datamodel):
            dic = {}
            for i in range(len(datamodel)):
                dic[datamodel[i]] = row[i]
            json.dump(dic, outfile, sort_keys=True)
            outfile.write('\n')
        else:
            print "Datamodel does not correspond with the data"
    
def printHelp():
    
    helptext = open('README.md').read()
    print helptext
    
if __name__ == '__main__':
    main()