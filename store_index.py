from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
import time
from dotenv import load_dotenv
import os

load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

extracted_data = load_pdf("Data/")
text_chunks = text_split(extracted_data)
length = len(text_chunks)
embedding_model = download_hugging_face_embeddings()
pc = Pinecone(api_key=PINECONE_API_KEY)
index_name = "medi-bot"
existing_indexes = [index_info["name"]for index_info in pc.list_indexes()]
if index_name not in existing_indexes:
    pc.create_index(
        name = index_name,
        dimension=384,
        metric="cosine",
        spec = ServerlessSpec(cloud="aws", region="us-east-1"),
    )
    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(1)

index = pc.Index(index_name)
vector_store = PineconeVectorStore(index=index, embedding=embedding_model)
ids = [str(i) for i in range(length)]
vector_store.add_documents(documents=text_chunks, ids=ids)


