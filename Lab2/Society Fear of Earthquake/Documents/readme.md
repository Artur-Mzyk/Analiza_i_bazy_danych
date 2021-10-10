# Folder structure:
## Original Data
* earthquake_data.csv - original data\
### Metadata
* metadata_guide.md - metadata guide
## Analysis Data
* earthquake_data.csv - original data
* earthquake_data_modified_column_names.csv - original data with modified column names
* earthquake_data_big_one.csv - data containing the age, the gender and the answer to the question "Do you think the "Big One" will occur in your lifetime?"
## Documents
* data_appendix.md - data appendix documentation
* readme.md - readme file
## Command Files
* data_processing.ipynb - data processing main file written in Python, fully commented
* data_appendix.ipynb - data appendix file written in Python, fully commented

# Replicating the study:
1. Data analysis may be performed on any software which allows to install Python. To run the command files there need to be installed 3 packages:
* pandas,
* numpy,
* matplotlib.
2. Onto the replicator's computer should be copied Analysis Data/earthquake_data.csv, Command Files/data_processing.ipynb and Command Files/data_appendix.ipynb files. Then it only needs to run the Jupyter notebook code.
3. Command Files folder should be set as the working directory while running the Jupyter notebook code.
4. data_processing.ipynb file has to be run before data_appendix.ipynb file
5. data_processing.ipynb file uses earthquake_data.csv file. It produces earthquake_data_modified_column_names.csv and earthquake_data_big_one.csv files.
6. data_appendix.ipynb file uses earthquake_data_modified_column_names.csv and earthquake_data_big_one.csv files.
