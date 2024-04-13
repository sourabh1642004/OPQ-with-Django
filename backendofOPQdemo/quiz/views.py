# quiz/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Choice

@login_required
def quiz_start(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_start.html', {'quizzes': quizzes})

@login_required
def quiz_view(request, quiz_id, question_number=1):
    quiz = Quiz.objects.get(id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)
    current_question = questions[question_number - 1]
    
    if request.method == 'POST':
        selected_choice_id = request.POST.get('choice')
        if selected_choice_id:
            selected_choice = Choice.objects.get(pk=selected_choice_id)
            if selected_choice.is_correct:
                request.session['score'] = request.session.get('score', 0) + 1
                
        next_question_number = question_number + 1
        if next_question_number > len(questions):
            return redirect('quiz_submission', quiz_id=quiz_id)
        else:
            return redirect('quiz_view', quiz_id=quiz_id, question_number=next_question_number)
    
    context = {
        'quiz': quiz,
        'question': current_question,
        'question_number': question_number,
        'total_questions': len(questions)
    }
    return render(request, 'quiz_view.html', context)

@login_required
def quiz_submission(request, quiz_id):
    score = request.session.get('score', 0)
    request.session['score'] = 0  # Reset score after submission
    return render(request, 'quiz_submission.html', {'score': score})