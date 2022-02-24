from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from myapp.models import Flower
from django.http import HttpResponseRedirect
from .forms import MyForm
from django.contrib.auth.decorators import permission_required  # Authentication add in views label

"""
  Authentication is about verifying a user. Authorization is about restricting or
allowing access to resources.


"""
def index(request):
    q = request.GET.get('q', None)
    items = ''
    if q is None or q == "":
        flowers = Flower.objects.all()
    elif q is not None:
        flowers = Flower.objects.filter(title__contains=q)

    return render(request, 'myapp/index.html', {
        'flowers': flowers
    })


@permission_required('myapp.add_flower')
def create(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MyForm()
    return render(request, 'myapp/edit.html', {'form': form})


# Delete method
@permission_required('myapp.change_delete')
def delete(request, pk=None):
    flower = get_object_or_404(Flower, pk=pk)
    flower.delete()
    return render(request, 'myapp/index.html')


def detail(request, slug=None):  # < here
    flower = get_object_or_404(Flower, slug=slug)
    return render(request, 'myapp/detail.html', {'flower': flower})


def tags(request, slug=None):  # < here
    flowers = Flower.objects.filter(tags__slug=slug)
    return render(request, 'myapp/index.html', {'flowers': flowers})
