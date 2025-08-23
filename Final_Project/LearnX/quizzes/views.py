
from django.shortcuts import render, get_object_or_404, redirect
from .models import Quiz, Question, Choice

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, "quizzes/quiz_list.html", {"quizzes": quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    return render(request, "quizzes/quiz_detail.html", {
        "quiz": quiz,
        "questions": questions,
    })

def quiz_submit(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()
    score = 0

    if request.method == "POST":
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = get_object_or_404(Choice, id=int(selected))
                if choice.is_correct:
                    score += 1

        return render(request, "quizzes/quiz_result.html", {
            "quiz": quiz,
            "score": score,
            "total": questions.count(),
        })

    return redirect("quizzes:quiz_detail", quiz_id=quiz.id)

