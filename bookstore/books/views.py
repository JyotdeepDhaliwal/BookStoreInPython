from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def homepage(request):
    books = Book.objects.all()
    return render(request, 'homepage.html', {'books': books})

def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'book_detail.html', {'book': book})


@login_required
def add_book(request):
    form = BookForm()

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'add_book.html', context)


@login_required
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.user != book.posted_by:
        return redirect('homepage')

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', id=book.id)
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form, 'book': book})


@login_required
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.user != book.posted_by:
        return redirect('homepage')

    if request.method == 'POST':
        book.delete()
        return redirect('homepage')

    return render(request, 'delete_book.html', {'book': book})



def register_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('homepage')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('homepage')

    else:
        form = AuthenticationForm()

    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')