from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
# request is supposed to be of type 'HttpRequest'
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at question {question_id}")

def results(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse(f"You're voting on question {question_id}")

