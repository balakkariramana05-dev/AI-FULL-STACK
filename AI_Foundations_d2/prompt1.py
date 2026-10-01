from ollama import chat
response=chat(
    model="llama3.2",
    messages=[
        {
            "role" : "system",
            "content" : "Act as a skin expert and answer in 3 lines ",
            "role" : "user",
            "content" : "why do pimples occur on face?"
        }
    ]
)
print(response.message.content)