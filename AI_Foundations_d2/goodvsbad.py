from ollama import chat
bad= "Tell me about types of omlet."
good="List about the types of omlet and ways to do it.."
responseB=chat(
    model="llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : bad
        }
    ]
)
responseG=chat(
    model="llama3.2",
    messages=[
        {
            "role" : "user",
            "content" : good
        }
    ]
)
print("Bad prompt:",responseB["message"]["content"])
print("Good prompt:",responseG["message"]["content"])