from django.shortcuts import render , HttpResponse 
from django.http import JsonResponse
import os
import openai

openai.api_key = "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"



# Create your views here.
def chat(request):
    return render(request, "index.html")

# def chatApi(request):
#     response = openai.ChatCompletion.create(
#         model="text-davinci-003",
#         prompt="",
#         temperature=0.7,
#         max_tokens=256,
#         top_p=1,
#         frequency_penalty=0,
#         presence_penalty=0
#         )
#     messages = {"this" : "that"}
#     return JsonResponse(response["message"])

import openai
from django.http import JsonResponse


# def chatApi(request):
#     if request.method == "POST":
#         print(request.post["prompt"])
#         prompt = "Love code"  # Provide your text generation prompt
#         response = openai.Completion.create(# Make the OpenAI API request for text completion
#             engine="text-davinci-003",
#             prompt=prompt,
#             temperature=0.7,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#         )
#         return JsonResponse(response)
#     return HttpResponse("Bad Request")

import openai
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Import this decorator if you need to disable CSRF protection for this view

@csrf_exempt  # You may need to use csrf_exempt depending on your use case
def chatApi(request):
    if request.method == "POST":
        try:
            # Access the 'prompt' parameter from the POST data
            prompt = request.POST["prompt"]
            
            # Make the OpenAI API request for text completion
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            
            # Return the response as JSON
            return JsonResponse(response)
        except KeyError:
            # Handle the case where 'prompt' is not provided in the POST data
            return HttpResponse("Bad Request: 'prompt' parameter missing", status=400)
    else:
        # Handle other HTTP methods (e.g., GET) or return a 405 Method Not Allowed response
        return HttpResponse("Method Not Allowed", status=405)




def about(request):
    return render(request,'about.html')

def home(request):
    return render(request,'home.html')