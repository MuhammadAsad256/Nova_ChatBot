from django.shortcuts import render
from django.http import JsonResponse
import cohere

# Initialize the Cohere client with your API key
co = cohere.Client('PW4VcTg8XiWXZ3BsX39QJKlXOlHhkbpe1efHNL6i')

# Initialize conversation history
conversation_history = ""

def index(request):
    global conversation_history
    conversation_history = ""  
    return render(request, 'chat/chat.html')

def chat(request):
    global conversation_history
    if request.method == "POST":
        msg = request.POST.get("msg", "").lower() 

        if any(word in msg for word in ["invent", "create", "made", "invented you", "created you", "made you"]):
            ai_response = "I was created by Muhammad Asad."

        elif any(word in msg for word in ["what is your name", "your name", "who are you", "tell me your name"]):
            ai_response = "My name is Nova AI, a language model designed to assist with various queries and discussions. How can I assist you today?"

        else:
            conversation_history += f"User: {msg}\n"

            response = co.generate(
                model='command-r-08-2024',
                prompt=f"{conversation_history}AI: ",
                max_tokens=100,
                stop_sequences=["User:"],
            )
            
            ai_response = response.generations[0].text.strip()
            
            conversation_history += f"AI: {ai_response}\n"

        return JsonResponse(ai_response, safe=False)