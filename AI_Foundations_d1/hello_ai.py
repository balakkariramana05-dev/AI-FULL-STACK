from ollama import chat
response = chat(
    model="llama3.2",
    messages=[{
        "role":"user",
        "content":"Explain SQL briefly" }])
print(response.message.content)
