from ollama import chat
system_msg= "You are a friend .Give me answer how our friend speaks in one line"
history = [{"role" : "system","content" : system_msg}]
question_counter = 0

print("Excited for the conversations!")
while True:
    question=input("You:")
    if question == " ":
        print("Eva(❁´◡`❁): Ask something!!")
        continue
    if question.lower().strip() == "/history":
        print("---- Your Conversation so far ----")
        if len(history) < 2:
            print("Nothing so far!!")
        for msg in history[1:]:
            if msg["role"]== "user":
                speaker= "You"
            else:
                speaker = "Eva(❁´◡`❁)"
            print(f"{speaker} : {msg['content']}")
            print("-----------------")
            print()
            continue
    if question.lower().strip() == "/help":
        print("-----Available commands -----")
        print("/history - displays conversation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quit the chatbot")
        print("----------------------------------------------")
        print()
        continue

    if question.lower().strip() == "/clear":
        history = [{"role":"system","content" : system_msg}]
        print("Your history is cleared.Start a fresh conversation.")
        print()
        continue
    if question.lower().strip() .startswith("/personality"):
        personality = input("Enter personality:")
        system_msg = personality
        history = [{"role" :"system","content":system_msg}]
        print("Personality changed successfully!!")
        continue
    if question.lower().strip() == "exit":
        print("Eva(❁´◡`❁):  BYE 👋 FOR THE DAY")
        print(f"You asked{question_counter}questions today.Good job!")
        break
    history.append({"role" : "user" , "content" : question})
    question_counter += 1
    try:
        response = chat(
            model="llama3.2",
            messages=history
        )
        reply = response["message"]["content"]
        history.append({"role" : "assistant" , "content" : reply})
        print(f"Eva(❁´◡`❁) :{reply}")
        print()
    except Exception as e:
        print("Unknown issue. Is ollama running?")