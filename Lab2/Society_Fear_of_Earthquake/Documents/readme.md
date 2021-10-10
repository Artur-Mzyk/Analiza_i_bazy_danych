# Folder structure:
## Original_Data
* earthquake_data.csv - original data
### Metadata
* metadata_guide.md - metadata guide
## Analysis_Data
* earthquake_data.csv - original data
* earthquake_data_cleaned.csv - valid data with modified column names
* earthquake_data_big_one.csv - data containing the age, the gender and the answer to the question "Do you think the "Big One" will occur in your lifetime?"
## Documents
* data_appendix.pdf - data appendix documentation
* readme.md - readme file
### Data_Appendix_Output
* data_appendix_report.txt - file generated with data_appendix.ipynb containing variable information
* earthquake_data_cleaned_freq.png - variable's frequency bar chart for earthquake_data_cleaned.csv
* earthquake_data_big_one_freq.png - variable's frequency bar chart for earthquake_data_big_one.csv
## Command_Files
* data_processing.ipynb - data processing main file written in Python, fully commented
* data_appendix.ipynb - data appendix file written in Python, fully commented

# Replicating the study:
1. Data analysis may be performed on any software which allows to install Python. To run the command files there need to be installed 2 packages:
* pandas
* matplotlib.
2. Onto the replicator's computer there should be copied:
* Original_Data/earthquake_data.csv
* Command_Files/data_processing.ipynb
* Command_Files/data_appendix.ipynb files.

There also need to be created 2 empty folders:
* Analysis_Data
* Documents/Data_Appendix_Output
4. Then one only needs to run the Jupyter notebook code.
5. Command_Files folder should be set as the working directory while running the Jupyter notebook code.
6. data_processing.ipynb file has to be run before data_appendix.ipynb file.
7. data_processing.ipynb file uses earthquake_data.csv file. It produces earthquake_data_cleaned.csv and earthquake_data_big_one.csv files.
8. data_appendix.ipynb file uses earthquake_data_cleaned.csv and earthquake_data_big_one.csv files.
