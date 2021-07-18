from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from home.models import Submission, Question
import os


# Create your views here.


def index(request):
    arr = Question.objects.all()
    context = {
        "questions": arr
    }
    return render(request, 'index.html', context)


def problem(request, id):
    question = Question.objects.get(question_id=id)
    context = {
        "ques": question,
        "ques_id": id
    }
    return render(request, 'problem.html', context)


def checker(question_id, code, input, output):
    verdict = ""
    os.chdir('docker')
    file = open('test.cpp', 'w')
    file.write(code)
    file.close()
    file_input = open('input.txt', 'w')
    file_input.write(input)
    file_input.close()
    file_output = open('output.txt', 'w')
    file_output.write(output)
    file_output.close()
    os.system('docker build -t test .')
    os.system('docker run --name checker test ')
    os.system('docker cp checker:/usr/src/cpp_test/output1.txt .')
    os.system('docker rm -f checker')
    flg = os.system('FC /W output.txt output1.txt')
    if flg == 1:
        verdict = "wrong answer"
    else:
        verdict = "accepted"
    os.system('del /f test.cpp')
    os.system('del /f input.txt')
    os.system('del /f output.txt')
    os.system('del /f output1.txt')
    os.chdir('..')
    return verdict


def submitsol(request, id):
    if request.method == "POST":
        question_id = id
        code = request.POST.get('solution')
    verdict = checker(question_id, code, Question.objects.get(
        question_id=id).input, Question.objects.get(question_id=id).output)
    submit = Submission(question_id=question_id, name=Question.objects.get(
        question_id=id).name, code=code, verdict=verdict)
    submit.save()
    return redirect('/leaderboard')


def LeaderBoard(request):
    arr = Submission.objects.all()
    latest = []
    for i in reversed(arr):
        latest.append(i)
        if(len(latest) == 10):
            break
    context = {
        "results": latest
    }
    return render(request, 'leaderboard.html', context)
