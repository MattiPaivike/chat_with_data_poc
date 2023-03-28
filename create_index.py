from llama_index import SimpleDirectoryReader, GPTSimpleVectorIndex

def construct_index(directory_path):

    documents = SimpleDirectoryReader(directory_path).load_data()
    
    index = GPTSimpleVectorIndex(documents)
    index.save_to_disk('index.json')

    return index

construct_index("server_documentation")