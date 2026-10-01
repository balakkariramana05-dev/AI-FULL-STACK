import chromadb
import streamlit as st
from ollama import chat
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Technova Conclerge", page_icon=".",layout="wide")
@st.cache_resource
def load_resources():
    model=SentenceTransformer('all-MiniM-L6-V2')
    client = chromadb.PersistentClient(path="chroma_db")
    collection = client.get_or_create_collection("fest_docs")
    return model,collection

def retrieve(question,k=3):
    q_emb = model.encode(question).tolist()
    res = collection.query(query_embeddings= q_emb,n_results = k)
    return list(zip(res["ids"][0],res["documents"][0],res["distances"][0]))

model,collection = load_resources()
st.title("Nova,the Technova Conceirge")
st.caption("I only know the fest documents.Ask me anything about Technoval")

st.session_state.setdefault("last_query","-")
st.session_state.setdefault("results",[])

left,right = st.columns(2)
with left:
    st.subheader("Ask Nova")
    question = st.text_input("Type something...",placeholder="when is the hackathon going to be?")
    search = st.button("Search")
with right:
    st.subheader("Evidence")    
    st.info("Retreived chunks will be displayed here.")

with st.sidebar:
    st.header("Knowledge meter")
    st.metric("Total chunks in memory",collection.count())
    st.caption("Last searched query")
    st.write(st.session_state.last_query)