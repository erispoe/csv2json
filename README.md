csv2json
========

**A python script to transform csv files to json files**

Python version: 2.*

To read help, pass the argument help:

python csv2json.py help

========

The arguments for using this script are:

python csv2json.py csv_data_model_file csv_data_input_file json_output_file separator

All arguments are required, apart from the separator.

Data model (i.e. column names) and data itself, both in cdv format, are separated into two different files so that you can treat several files of data sharing the same data model (for instance, data files from multiple years).

The separator should be provided in the form of a string, like "," or ';'. It's the character used to separate columns in the csv input file. If a specific separator is not passed to the script, it will assume that it's a regular comma(',').