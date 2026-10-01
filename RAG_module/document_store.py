from sentence_transformers import SentenceTransformer
import chromadb 

with open("fest_info.txt","r",encoding="utf-8") as f:
    text = f.read()
print(f"Your file has {len(text)} characters.")
print() 
print("Sample text:",text[:300])
def chunck_text(text, chunck_size = 300, overlap = 50):
    chuncks = []
    start = 0
    while start < len(text):
        chuncks.append(text[start:start + chunck_size])
        start += chunck_size - overlap
    return chuncks  

chuncks = chunck_text(text)

model = SentenceTransformer('all-MiniLM-L6-V2')
embeddings = model.encode(chuncks)
client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="fest_docs")
collection.upsert(
    ids = [f"chuncks_{i}"for i in range(len(chuncks))],
    documents=chuncks,
    embeddings=embeddings

)
print(f"Total{collection.count()} number of documents stored successfully")

print(f"Total{len(chuncks)}created -> Shape of embeddings: {embeddings.shape}")
print(f"Total{len(chuncks)} created.")
for i in range(len(chuncks)):
    print(f"emb_{i+1}:{embeddings[i][:5]}")
    print()
    print("-------------------------------------------------")
question = "what is the cost of registration?"    
q_embedding = model.encode([question]).tolist()
results=collection.query(query_embeddings=q_embedding,n_results=1)
retrieved = results["documents"][0]
print(retrieved)