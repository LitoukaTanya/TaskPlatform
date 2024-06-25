from django.shortcuts import render, redirect, get_object_or_404
from .models import Task, Comment
from .form import TaskForm, CommentForm       #SignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login


def base_view(request):
    return render(request, 'base.html')

def task_list(request):
    tasks = Task.objects.order_by('-created_at')
    context = {
        'tasks': tasks,
        'title': 'Task List',
    }
    return render(request, 'tasks/all_tasks.html', context)


@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
        context = {
            'form': form,
            'title': 'Create Task',
        }
        return render(request, 'tasks/new_tasks.html', context)


@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    comments = task.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.task = task
            new_comment.user = request.user
            new_comment.save()
            return redirect('task_detail', pk=task.pk)
    else:
        comment_form = CommentForm()
    context = {
        'task': task,
        'comments': comments,
        'comment_form': comment_form,
        'title': 'Task Detail',
    }
    return render(request, 'tasks/task_detail.html', context)


@login_required
def status_update(request, pk, status):
    task = get_object_or_404(Task, pk=pk)
    task.status = status
    task.save()
    return redirect('task_detail', pk=pk)
