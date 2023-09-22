
# LangChain imports
from langchain.sql_database import SQLDatabase
from langchain.llms import OpenAI
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamlitCallbackHandler
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from dotenv import load_dotenv

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
load_dotenv()

PROJECT_ID = os.environ.get("PROJECT_ID_GCP")
DATASET_ID = os.environ.get("DATASET_BQ")
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")


sqlalchemy_url = f'bigquery://{PROJECT_ID}/{DATASET_ID}?credentials_path={PATHS.GCP_KEYS}'

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
