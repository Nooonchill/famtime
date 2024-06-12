from django.shortcuts import render, redirect, get_object_or_404
from app.internal.forms.log_in import LogInForm
from app.internal.forms.register import RegisterForm
from app.internal.forms.family import CreateFamilyForm
from app.internal.forms.task import CreateTaskForm, UpdateTaskForm
from app.internal.forms.invitation import AddFamilyForm
from app.internal.models.task import Task
from app.internal.services.user_service import *
from app.internal.services.auth_service import *
from app.internal.services.family_service import *
from app.internal.services.task_service import *
from app.internal.services.notification_service import *
from django.http import HttpResponse, JsonResponse
from django.contrib import messages


def auth(request):
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        log_in_form = LogInForm(request.POST)
        user = None
        if register_form.is_valid():
            user = try_register_user(register_form)
        elif log_in_form.is_valid():
            user = try_log_in_user(log_in_form)
        if user is not None:
            response = redirect('/')
            response = add_cookie(response, 'id', user.id)
            return response
    else:
        register_form = RegisterForm()
        log_in_form = LogInForm()
    context = {'register_form': register_form, 'log_in_form': log_in_form}
    return render(request, 'auth.html', context)


def index(request):
    notifications = get_user_notifications(request.custom_user)
    families = get_family_list(request.custom_user)
    if request.method == 'POST':
        add_family_form = AddFamilyForm(request.POST)
        create_family_form = CreateFamilyForm(request.POST)
        if 'create_family' in request.POST:
            if create_family_form.is_valid():
                create_family(
                    request.custom_user,
                    create_family_form.cleaned_data['name'],
                    create_family_form.cleaned_data['color']
                )
                return redirect('/')
        elif 'add_family' in request.POST:
            if add_family_form.is_valid():
                family = add_family(request.custom_user, add_family_form.cleaned_data['code'])
                if family is None:
                    messages.error(request, 'Введен неверный код приглашения или семья уже активна') 
                    return redirect('/')
                return redirect('/')
    else:
        create_family_form = CreateFamilyForm()
        add_family_form = AddFamilyForm()
    context={
        'notifications': notifications,
        'first_name': request.custom_user.first_name,
        'families': families,
        'create_family_form': create_family_form,
        'add_family_form': add_family_form,
    }
    return render(request, 'index.html', context)


def get_invitation(request):
    if request.COOKIES.get('family') is None:
        return {}
    family_id = request.COOKIES.get('family')
    invite_code = get_or_create_invite(family_id).code
    return JsonResponse({'invite_code': invite_code})


def schedule(request):
    if request.method == 'POST':
        update_task_form = UpdateTaskForm(request.POST)
        if 'create_task' in request.POST:
            create_task_form = CreateTaskForm(request.POST)
            if create_task_form.is_valid():
                create_task(
                    app_user=request.custom_user,
                    family_id=request.COOKIES['family'],
                    name=create_task_form.cleaned_data['name'],
                    description=create_task_form.cleaned_data['description'],
                    start_time=create_task_form.cleaned_data['start_time'],
                    end_time=create_task_form.cleaned_data['end_time'],
                    tag=create_task_form.cleaned_data['tag'],
                    status=create_task_form.cleaned_data['status'],
                    private=create_task_form.cleaned_data['private']
                )
                return redirect('/schedule/')
        elif 'update_task' in request.POST:
            if update_task_form.is_valid():
                update_task(
                    app_user=request.custom_user,
                    task_id=request.POST.get('task_id'),
                    family_id=request.COOKIES['family'],
                    name=update_task_form.cleaned_data['name'],
                    description=update_task_form.cleaned_data['description'],
                    start_time=update_task_form.cleaned_data['start_time'],
                    end_time=update_task_form.cleaned_data['end_time'],
                    tag=update_task_form.cleaned_data['tag'],
                    status=update_task_form.cleaned_data['status'],
                    private=update_task_form.cleaned_data['private']
                )
                return redirect('/schedule/')
    else:
        tasks = get_day_task_list(request.custom_user)
        update_task_form = UpdateTaskForm()
        create_task_form = CreateTaskForm()
    context={'create_task_form': create_task_form, 'update_task_form': update_task_form, 'tasks': tasks}
    return render(request, 'schedule.html', context)


def get_tasks_for_date(request, date):
    selected_date = datetime.strptime(date, '%Y-%m-%d')
    tasks = get_day_task_list(request.custom_user, selected_date.date())
    tasks_data = [{
        'id': task.id,
        'name': task.task.name,
        'start_time': task.task.start_time.strftime('%Y-%m-%d %H:%M'),
        'end_time': task.task.end_time.strftime('%Y-%m-%d %H:%M'),
        'usernames': task.app_user.username,
        'tag': task.task.get_tag_display(),
        'private': task.task.get_private_display(),
        'status': task.task.get_status_display(),
        'description': task.task.description,
    } for task in tasks]
    return JsonResponse(tasks_data, safe=False)


def get_day_tags(request, date):
    date = datetime.strptime(date, '%Y-%m-%d')
    tasks = get_day_task_list(request.custom_user, date.date())
    tags = {
        'tag': list(set(task.task.get_tag_display() for task in tasks)),
    }
    return JsonResponse(tags, safe=False) 