import os 
from langchain_community.document_loaders import PyPDFLoader 


path = "data/sample.pdf" 

if not os.path.exists(path):
    print("file does not exist")  
else : 
    print("file exists")  
    loader = PyPDFLoader(path) 
    documents = loader.load() 
    print(f"Loaded {len(documents)} documents from {path}")
    index = 0

    print("****************************************"  )
    for doc in documents: 
        # print(f"Document {index} : document content : {doc}") 
        print(doc.metadata) 
        print(doc.page_content)
        index = index +1
    print("****************************************"  )
    if len(documents) > 0:
      for docu in documents: 
        # print(f"Document : document content : {docu}") 
        first = documents[0]  

        print(f"First document content : {first.page_content}" ) 
        print(f"First document metadata : {first.metadata}" )  


