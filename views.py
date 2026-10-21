from django.shortcuts import render, redirect, get_object_or_404
from models import Task

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subject = request.POST.get("subject")
        due_date = request.POST.get("due_date")
        if title and subject and due_date:
            Task.objects.create(
                title=title,
                subject=subject,
                due_date=due_date
            )
            return redirect("index")

    tasks = Task.objects.all().order_by("due_date")
    total = tasks.count()
    completed = tasks.filter(completed=True).count()
    pending = total - completed
    progress = int((completed / total) * 100) if total > 0 else 0

    return render(request, "index.html", {
        "tasks": tasks,
        "total": total,
        "completed": completed,
        "pending": pending,
        "progress": progress,
    })

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect("index")

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect("index")