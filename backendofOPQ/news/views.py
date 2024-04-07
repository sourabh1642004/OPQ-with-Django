from django.shortcuts import render
# quiz/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Choice

@login_required
def quiz_start(request):
    quiz = Quiz.objects.first()  # Assuming there is only one quiz for simplicity
    questions = Question.objects.filter(quiz=quiz)
    context = {'quiz': quiz, 'questions': questions}
    return render(request, 'quiz_start.html', context)

@login_required
def quiz_submission(request):
    if request.method == 'POST':
        quiz = Quiz.objects.first()  # Assuming there is only one quiz for simplicity
        questions = Question.objects.filter(quiz=quiz)
        score = 0
        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                selected_choice = Choice.objects.get(pk=selected_choice_id)
                if selected_choice.is_correct:
                    score += 1
        context = {'quiz': quiz, 'score': score}
        return render(request, 'quiz_submission.html', context)
    else:
        return redirect('quiz_start')

# Create your views here.
