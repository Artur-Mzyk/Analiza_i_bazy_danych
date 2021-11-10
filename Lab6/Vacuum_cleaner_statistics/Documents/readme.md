# Folder structure
## Original_Data
* 9_PODLASKIE.csv - original data
### Metadata
* metadata_guide.md - metadata guide
## Analysis_Data
* vacuum_cleaner_statistics_podlaskie.csv - tidy data
### Data_Appendix_Output
* data_appendix_report.txt - file generated with data_appendix.ipynb containing codebook for variables in the vacuum_cleaner_statistics_podlaskie.csv file
* data_appendix_statistics.pdf - file generated with dapa_appendix.ipynb containing basic summary statistics, frequency tables and bar charts for variables in the vacuum_cleaner_statistics_podlaskie.csv file
## Documents
* data_appendix.pdf - data appendix documentation
* readme.md - readme file
* final_paper.pdf - the final paper
## Command_Files
* data_processing.ipynb - data processing main file written in Python, fully commented
* data_appendix.ipynb - data appendix file written in Python, fully commented

# Replicating the study:
1. Data analysis may be performed on any software which allows to install Python. To run the command files there need to be installed 3 packages:
* pandas
* matplotlib
* numpy.
2. Onto the replicator's computer there should be copied the files listed below:
* Original_Data/9_PODLASKIE.csv
* Command_Files/data_processing.ipynb
* Command_Files/data_appendix.ipynb.

There also need to be created 3 empty folders:
* Analysis_Data
* Analysis_Data/Data_Appendix_Output
* Documents.
4. Then one only needs to run the Jupyter notebook code.
* Command_Files folder should be set as the working directory while running the Jupyter notebook code.
* The data_processing.ipynb file has to be run before data_appendix.ipynb file.
* The data_processing.ipynb file uses the 9_PODLASKIE.csv file. It produces the vacuum_cleaner_statistics_podlaskie.csv and final_paper.pdf files.
* The data_appendix.ipynb file uses the vacuum_cleaner_statistics_podlaskie.csv file. It produces the data_appendix_report.txt and data_appendix_statistics.pdf files.
5. Data appendix documentation has been created linking the data_appendix_report.txt and data_appendix_statistics.pdf files.
