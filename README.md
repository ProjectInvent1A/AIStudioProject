Project Summary
---

The goal of our project was to to pair students in the 6th-12th grade with nonprofit organizations based on their location and interest to help them find potential local organizations to partner with in developing inventions for social good. We created an application that suggests five nearby organizations based on a user's input sentence that describes what they're interested in. 

**Link to our Final Product:**

(Please note this takes a little while to load because it needs access to our large dataset (almost one million rows!)

[**Final Presentation Slides:**](https://docs.google.com/presentation/d/1lH2ij4ymx_ZaTJVi78ol9RbpHtFo0rSmF8Q-owhMWJw/edit?usp=sharing)
Our final presentation slides give an overview of our project process and technologies used.

**Original Datasets**
- [IRS Publication 78 Data 2024](https://www.irs.gov/charities-non-profits/tax-exempt-organization-search-bulk-data-downloads#pub78): List of organizations eligible to receive tax-deductible charitable contributions.
- [Urban Data Catalog CBDO Population Dataset.csv 2022](https://datacatalog.urban.org/dataset/community-based-development-organization-sector-and-financial-datasets): Community-Based Development Organizations Sector


Overview of Files in this Repository
---

**Development Process folder**: These are the Google Colab notebooks we used in developing our final product.
- **CharityNavigatorAPIScript.ipynb**
  - Developing script to call the Charity Navigator API — this code is then included in other notebooks where needed
- **AI Studio Project Data Cleaning.ipynb**
  - Combining our two initial datasets (CBDO and IRS pub78) and doing some initial data cleaning. Pulled info about each organization’s purpose from the NTEE codes and Charity Navigator API. We ended up having to run the Charity Navigator API on the data in chunks, since our dataset is so big, so only the first chunk is seen here.
- **DataPreparationAndModeling.ipynb**
  - Data preparation for modeling: combined data chunks from API, dropped unnecessary columns, removed duplicates, and managed missing values.
- **BTT_modeling.ipynb**
  - Figuring out the modeling process using BERT Sentence Transformers
- **GeoCode Example.ipynb**
  - Learning how to use the GeoPy library
- **Location_work.ipynb**
  - Creating a dataset of cities and their latitude and longitude coordinates for later use
- **KMeansCluster_location.ipynb** (too big to upload to GitHub, link [here](https://colab.research.google.com/drive/12bjS2ENHvrfypCdVd7gqKxblHqI6b7nh?authuser=2#scrollTo=i1O4bM_1374H))
  - Experimenting with a different way of matching locations using K means clustering. Didn't end up using this method based on efficiency
- **DashInterfaceWork.ipynb**
  - Creating a UI for our application using Dash
- **ModelFullDataSet.ipynb**
  - Saving the sentence embedding vector of each organization’s text description in the organizations dataframe, then ran the model on this complete dataset.


**org_matching folder:** These are our final files for deployment. Our python file can be run locally and is also deployed on Google Cloud Run.
- **dashinterfacework.py**
  - Final application code. A Dash interface that suggests organizations based on location and interest inputs
- **requirements.txt**
  - Package requirements for dashinterfacework.py
- **Dockerfile**
  - File to create Docker image in order to upload to Google Cloud Run

