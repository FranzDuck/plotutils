# plotutils

Python library to automate the import of measurement csv-files and speed up the procedure of importing different flavors of csv (or dat or any other plain text data file).
Mainly used to ease the process of plotting experimental data in science.


## Usage of the CSV Import
To use the import functionality run in your project: 
```python 
import intelligentCsvImport as csvI
```
Then, run:
```python
csvp, series = csvI.data_loader('expr')
```
where `expr` is a regex search pattern for a series of csv-files, i.e. if you named your files measurement1.csv, measurement2.csv, etc. the search string would be `measurement*`.

---
