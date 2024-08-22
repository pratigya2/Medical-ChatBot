from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
import pinecone
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os


app = Flask(__name__)
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
embedding_model = download_hugging_face_embeddings()
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medi-bot"

index = pc.Index(index_name)
vector_store = PineconeVectorStore(index=index, embedding=embedding_model)

prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": prompt}

llm = CTransformers(model = "model/llama-2-7b-chat.ggmlv3.q4_0.bin",
model_type = "llama",
config={'max_new_tokens': 512,
'temperature': 0.8})

qa = RetrievalQA.from_chain_type(llm= llm,
chain_type="stuff",
retriever = vector_store.as_retriever(search_kwargs={'k':2}),
return_source_documents= True,
chain_type_kwargs=chain_type_kwargs)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods = ["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print(type(msg))
    result = qa({"query": msg})
    print("Response :", result["result"])
    return str(result["result"])

if __name__ == '__main__':
    app.run(debug=True)




