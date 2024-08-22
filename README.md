# Medical-ChatBot
#Medical ChatBot using LLAMA2
# ![Medical-ChatBot](static\output.png) Medi-Bot

Medi-Bot is an AI-powered medical assistant designed to provide instant healthcare information and assistance. Utilizing advanced language models and machine learning algorithms, Medi-Bot engages users in real-time conversations, offering medical advice, symptom analysis, and healthcare recommendations.

## Key Features
- **Interactive Chat Interface**: Engages users in natural conversations to understand their symptoms and provide relevant advice.
- **AI-Powered Responses**: Powered by Meta Llama2, offering accurate and contextually appropriate responses.
- **Seamless Integration**: Built using Flask, allowing easy integration into various platforms.
- **Efficient Data Management**: Uses Pinecone for fast and efficient data retrieval and storage.
- **Extensible and Modular**: Developed with LangChain for scalable and modular code.


##Steps to run the project

#Clone the Repository
```bash
git clone https://github.com/pratigya2/Medical-ChatBot/tree/main
```
#Step 1: Create virtual environment after opening the repository
```bash
mkvirtualenv chatbot
```

```bash
workon chatbot
```
```bash
setpojectdir "path/to/your/project folder"
```
#Step 2: Install the requirements
```bash
pip install -r requirements.txt
```

#Create .env file in the root directory and add pinecone credentials
```bash
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
PINECONE_API_ENV = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

#Download the model and keep in the model directory
```bash
llama-2-7b-chat.ggmlv3.q4_0.bin
```
```bash
## Dowload model from the following link
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML
```
#Run the following command to make knowledge base in Pinecone
```bash
python store_index.py
```

#Finally run following command and open up local host
```bash
python app.py
```

## Tech Stack Used

- **Python**: Programming language used for backend logic and integration.
- **LangChain**: Framework for developing applications powered by language models.
- **Flask**: Lightweight web framework used to build the web application.
- **Meta Llama2**: Language model utilized for natural language processing and generating responses.
- **Pinecone**: Vector database used for storing and retrieving embeddings efficiently.



