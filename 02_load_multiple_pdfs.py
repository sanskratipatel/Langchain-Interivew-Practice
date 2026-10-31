import os 
from langchain_community.document_loaders import PyPDFLoader 

folder_path = "data" 
files_data = [] 


if not os.path.exists(folder_path): 
    print("Folder does not exist") 
else : 
    print("Folder Exists") 
    files = os.listdir(folder_path) 

    for file in files : 
        if file.endswith(".pdf") : 
            pdf_path = os.path.join(folder_path, file)  
            print(f"Loading PDF file: {pdf_path}") 

            loader = PyPDFLoader(pdf_path)
            files_data.extend(loader.load()) 

    index = 0 

    for doc in files_data : 
        print(doc.metadata.get("source")) 
        print(doc.metadata.get("page")) 
        print(doc.page_content) 
        index += 1