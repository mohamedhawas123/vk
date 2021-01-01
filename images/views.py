from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import ImageCreateForm
from .models import Image


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
          
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, "image added successfuly")
            return redirect(new_item.get_absolte_url)

    
    else:
        form = ImageCreateForm(data=request.GET)

    
    return render(request, 'images/image/create.html', {'section': 'images', 'form': form})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request,  'images/image/detail.html', {'secatioj': 'images', 'image': image})
    
