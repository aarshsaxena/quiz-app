from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from question.models import Question, QuizSession
import random

def start_quiz(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', 'Guest')
        session = QuizSession.objects.create(nickname=nickname)
        return redirect('questions', session_id=session.id)
    return render(request, 'start_quiz.html')

def questions(request, session_id):
    session = QuizSession.objects.get(id=session_id)
    questions = Question.objects.order_by('?')[:10]  # Get a random set of 10 questions
    if request.method == 'POST':
        answers = request.POST.dict()
        session.total_questions = 10
        correct = 0
        for question in questions:
            submitted_answer = answers.get(f'question_{question.id}')
            if submitted_answer == question.correct_option:
                correct += 1
        session.correct_answers = correct
        session.incorrect_answers = 10 - correct
        session.save()
        return redirect('results', session_id=session.id)

    return render(request, 'questions.html', {'session': session, 'questions': questions})

def quiz_results(request, session_id):
    session = QuizSession.objects.get(id=session_id)
    return render(request, 'quiz_results.html', {'session': session})
