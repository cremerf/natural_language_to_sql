# Natural Language to SQL
## Description

In this this repository you will find an application designed to serve as a Data Analytics Assistant. You can chat with it in natural language and the assistant will translate it to SQL queries emerging by [Chain of Thought](https://en.wikipedia.org/wiki/Prompt_engineering#Chain-of-thought), go to the db, execute the query and finally, answering your question in natural language. 

It enables users to interact with and analyze BigQuery and MySQL databases seamlessly. The application is built using LangChain(SQL Agents), Streamlit, SQL Alchemy and Google Cloud-BigQuery.

It intends to meet the demands of those who need more **general insights** from the data. 

- Some of those questions might be:

What are the top-performing products in the last quarter?
Which marketing channels have the highest customer acquisition cost?
How do sales promotions impact revenue?


Other concerns that could involve several joins and complex reasoning like **churn, retention, life-time value, seasonality by region**, etc might create hallucinations outcomming poor results in term of precision.  

## Features 
- **Data Analytics Assistant** : A user-friendly interface to ask in natural langauge about data. 
- **Database Support** : Compatible with BigQuery and MySQL databases. 
- **Interactive UI** : Built with Streamlit for an interactive user experience.
## Technologies Used 
- [LangChain](https://github.com/langchain-ai/langchain): Open source framework for building context-aware reasoning applications, enabling almost unlimited power by large language models.
- [Streamlit](https://streamlit.io/) : Free and open-source front-end framework to rapidly build and share beautiful machine learning and data science web apps. 
- [SQL Alchemy](https://github.com/sqlalchemy/sqlalchemy) : SQLAlchemy is a tool in Python that helps software developers work with databases more easily. It allows you to use Python code to run SQL queries and manage relationships between data, giving you the best of both worlds—Python's simplicity and SQL's capabilities.



## How to Use
#### Step 1: Clone the Repository

```bash

git clone https://github.com/cremerf/ds_llm_sql.git .
```
#### Step 2: Create .env file with enviroment variables

```toml
DB_USER=""
DB_PASSWORD=""
DB_HOST= ""
DB_NAME= ""
PROJECT_ID_GCP= ""
DATASET_BQ= ""
OPENAI_API_KEY=""
```
Store this file in the root directory of the app

#### Step 2.1: Create credentials folder and save GCP keys

###### Step 2.1.1: Open Google Cloud Console 
- Navigate to [Google Cloud Console](https://console.cloud.google.com/) .
###### Step 2.1.2: Select Project
- Choose the project for which you want to create the service account.
###### Step 2.1.3: Go to IAM & Admin
- In the left sidebar, click on "IAM & Admin" and then select "Service accounts."
###### Step 2.1.4: Create Service Account
- Click on "Create Service Account."
- Fill in the required details like name, description, and click "Create."
###### Step 2.1.5: Assign Roles
- Assign necessary roles to the service account and click "Continue."
###### Step 2.1.6: Add Users (Optional)
- Add users who can access this service account, if needed. 
- Click "Done."
###### Step 2.1.7: Generate Key
- In the Service accounts list, find the newly created service account.
- Click on the three-dot menu (actions) and select "Manage keys."
- Click on "Add Key" and choose "JSON."
###### Step 2.1.8: Download Key
Download the JSON key and store it in the credentials/ folder

#### Step 3: Create running env and install requirements

###### Step 3.1: Install Miniconda/Conda 
- Download Miniconda installer

```bash

wget https://repo.anaconda.com/archive/Anaconda3-2021.05-Linux-x86_64.sh
```

Install it in your home user


###### Step 3.2: Create Environment 
- Create a new environment with Python 3.11:

```bash

conda create --name ds_llm_analytics python=3.11
```

###### Step 3.3: Create Environment 

```bash

pip install -r requirements.txt
```

By default, the installed dependencies will only run with BigQuery databases. If you wish to interact with MySQL DB, create a conda env using this yml file: ds_llm_sql_92023.yml  


```bash

conda env create --file docs/ds_llm_sql_92023.yml
```

#### Step 4: Run the Streamlit Application

```bash

streamlit run app.py
```

This will launch the Streamlit app in your default web browser. Follow the on-screen instructions to interact with BigQuery or MySQL databases.---

Feel free to fork this repository to better suit the actual content and functionality of your use case.


