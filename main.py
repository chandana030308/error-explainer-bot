import ollama
name = input("enter your name: ")
branch = input('enter your branch: ')
print(f"Hi {name} from {branch} ")
SYSTEM ='''
you explain programming error messages to a 2nd year engineering student . reply in 3 parts.
1) what it means in plain english
2) the likely cause
3) how to fix 
keep it under 120 words.
'''
while True:
    data = input("enter your error message or exit to stop: ")
    if not data:
        print("enter an error:")
    elif data.lower() == "exit":
        break
    elif data.lower() == "help":
        print("enter the error message you want to understand or type 'exit'")
    else:
        try: 
            response = ollama.chat(model="gemma3:1b",messages=[
            {
                "role": "system",
                "content": SYSTEM
            },
            {
                "role": "user",
                "content": "python error - NameError : name 'x' is not defined"
            }
            ])
            print(response.message.content)
        except Exception as e:
            print(f"could not reach the model: {e}")
