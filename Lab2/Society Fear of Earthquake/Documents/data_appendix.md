All files from Analysis Data folder are described here.

## earthquake_data.csv
Original data file described in Original Data/Metadata/metadata_guide.md.

##  earthquake_data_modified_column_names.csv
This file contains all information extracted from original data. The columns' names have been changed so they are no longer questions.\
Columns have been sorted so that the people personal data is stored on the left side. Records have been sorted due to the age.\
It does not include any new information in comparison to 'earthquake_data.csv' file.

The unit of observation is a survey response.

Columns information:
1. Age - categorical variable, number interval, missing values: 12/1013, 60 means 60 or more, original variable name: Age,
2. Gender - categorical variable, missing values: 12/1013, Male or Female, original variable name: What is your gender?,
3. Household income - categorical variable, interval number of dollars, missing values: 12/1013, possibility of not answering, original variable name: How much total combined money did all members of your HOUSEHOLD earn last year?,
4. US Region - categorical variable, missing values: 35/1013, original variable name: US Region,
5. Earthquakes fear - categorical variable, missing values: 0/1013, original variable name: In general, how worried are you about earthquakes?, possible answers:
* Not at all worried,
* Not so worried,
* Somewhat worried,
* Very worried,
* Extremely worried,
6. The "Big One" fear - categorical variable, missing values: 0/1013, original variable name: How worried are you about the Big One, a massive, catastrophic earthquake?, possible answers:\
* Not at all worried,
* Not so worried,
* Somewhat worried,
* Very worried,
* Extremely worried,
7. The "Big One" experiencing possible - categorical variable, missing values: 0/1013, original variable name: Do you think the "Big One" will occur in your lifetime?, Yes or No,
8. Earthquake experienced - categorical variable, missing values: 7/1013, original variable name: Have you ever experienced an earthquake?, possible answers:\
* No,
* Yes, one or more minor ones,
* Yes, one or more major ones
9. Earthquake precautions taken - categorical variable, missing values: 7/1013, original variable name: Have you or anyone in your household taken any precautions for an earthquake (packed an earthquake survival kit, prepared an evacuation plan, etc.)?, Yes or No,
10. San Andreas Fault line familiarity - categorical variable, missing values: 12/1013, original variable name: How familiar are you with the San Andreas Fault line?, possible answers:\
* Not at all familiar,
* Not so familiar,
* Somewhat familiar,
* Very familiar,
* Extremely familiar,
11. Yellowstone Supervolcano familiarity - categorical variable, missing values: 12/1013, original variable name: How familiar are you with the Yellowstone Supervolcano?, possible answers:\
* Not at all familiar,
* Not so familiar,
* Somewhat familiar,
* Very familiar,
* Extremely familiar.

## earthquake_data_big_one.csv
This file contains a table consisting of the age, the gender and the answer to the question "Do you think the "Big One" will occur in your lifetime?".\
It does not include any new information in comparison to 'earthquake_data.csv' file.

Columns information:
1. Age - categorical variable, number interval, missing values: 12/1013, 60 means 60 or more, original variable name: Age,
2. Gender - categorical variable, missing values: 12/1013, Male or Female, original variable name: What is your gender?,
3. The "Big One" experiencing possible - categorical variable, missing values: 0/1013, original variable name: Do you think the "Big One" will occur in your lifetime?, Yes or No.

Frequency tables and bar charts are available in Command Files/data_appendix.ipynb file.
