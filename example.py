# First import the csv-Import script
import os
import intelligentCsvLoader as csvL

# Switch to the folder containing the example csv files
os.chdir('./examples/rawdat')

# To load the data in the examples folder, invoke the data_loader() method with a
# search string matching the csv files. In this case we search for 'Ex*' 
csvp, series = csvL.data_loader('ExLife*')
