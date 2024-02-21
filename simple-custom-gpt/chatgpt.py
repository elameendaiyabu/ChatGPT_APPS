import os
import sys
import constants

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.API_KEY

# loader = TextLoader('text.txt', encoding='utf-8')  #To Specify the encoding when using pdf - uncomment for pdfs
loader = TextLoader('text.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

while True:
    query = input("Enter your query (or 'exit' to end): ")
    if query.lower() == 'exit':
        break
    result = index.query(query, llm=ChatOpenAI())
    print(result)


"""
#this is the same code as above but no looping and you would have to rerun script everytime
import os
import sys
import constants

from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.chat_models import ChatOpenAI

os.environ["OPENAI_API_KEY"] = constants.API_KEY

query = sys.argv[1]


loader = TextLoader('text.txt')
index = VectorstoreIndexCreator().from_loaders([loader])

print(index.query(query, llm=ChatOpenAI()))
"""