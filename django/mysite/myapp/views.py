from django.shortcuts import render, HttpResponse, redirect,get_object_or_404
from myapp.models import *
from myapp.forms import *

# Create your views here.
def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    for i in authors:
        print(i)
    return render(request, 'author/list.html', {'authors': authors})

def create_author(request):
     if request.method == 'POST':
         form = AuthorForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('author_list')
     else:
               form=AuthorForm()
     return render(request, 'author/add.html', {'form': form})

def delete_author(request, id):
    if request.method == 'POST':
        author = Author.objects.get(id=id)
        author.delete()
        return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'author/delete.html', {'form': form})

def update_author(request, id):
    author = get_object_or_404(Author, id=id)
    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
        return render(request, 'author/edit.html', {'form': form, 'author': author}) 



