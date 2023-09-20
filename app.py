
# LangChain imports
from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit

# Streamlit
import streamlit as st

# Built-in
import os
import json

# Dependency to query BQ-GCP
import pyarrow

# Paths
from packages.paths import DS_LLM_PATHS

PATHS = DS_LLM_PATHS()

with open(PATHS.OPEN_AI) as creds:
    openai_keys = json.load(creds)

OPENAI_API_KEY = openai_keys['OPENAI_API_KEY']

with open(PATHS.EXTRACT_KEYS) as creds:
    bq_keys = json.load(creds)

project_id = bq_keys['project_id_gcp']
dataset_bq = bq_keys['dataset_bq']
table_bq = bq_keys['table_bq']

sqlalchemy_url = f'bigquery://{project_id}/{dataset_bq}?credentials_path={PATHS.GCP_KEYS}'

st.title("🤖 DataGPT 🤖")
st.title("Chat with your BigQuery database!")
st.subheader("This is DataGPT, your data analytics assistant.", divider='gray')
st.subheader("Powered by :blue[DataSpeaks.ai] :bar_chart:")
api_key = st.text_input("OpenAI key", type='password')


if api_key:
    db = SQLDatabase.from_uri(sqlalchemy_url)
    llm = ChatOpenAI(model='gpt-4', temperature=0, openai_api_key=api_key)
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    agent_executor = create_sql_agent(
        llm=llm,
        toolkit=toolkit,
        verbose=True,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    )
else:
    st.write("Please input OpenAI key")

if prompt := st.chat_input():
    st.chat_message("user").write(prompt)
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent_executor.run(prompt, callbacks=[st_callback])
        
        st.write(response)
