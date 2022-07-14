from django.shortcuts import render, redirect

# Create your views here.
from blogs.forms import EntryForm
from blogs.models import BlogPost


def index(request):
    all_entry_blogs = BlogPost.objects.order_by('-date_added')
    context = {'all_entry_blogs': all_entry_blogs}
    return render(request, 'blogs/index.html', context=context)


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
            # new_entry.title = title
            new_entry.save()
            return redirect('blogs:home')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'blogs/new_entry.html', context)


def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = BlogPost.objects.get(id=entry_id)
    title = entry.title
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