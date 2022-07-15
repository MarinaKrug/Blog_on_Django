from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from blogs.forms import EntryForm
from blogs.models import BlogPost


def index(request):
    all_entry_blogs = BlogPost.objects.order_by('-date_added')
    context = {'all_entry_blogs': all_entry_blogs}
    return render(request, 'blogs/index.html', context=context)



@login_required
def new_entry(request):
    """Добавляет новую запись """

    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user
            new_entry.save()

            return redirect('blogs:home')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = BlogPost.objects.get(id=entry_id)
    title = entry.title
    if entry.owner != request.user:
        raise Http404
    if request.method != 'POST':
    # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
 # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    context = {'entry': entry, 'title': title, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)


def register(request):
    """Регистрирует нового пользователя."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blogs:home')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/register.html', context)