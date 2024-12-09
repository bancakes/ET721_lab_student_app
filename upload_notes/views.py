from django.shortcuts import render, redirect
from .models import NoteImage
from .forms import NoteImageForm

def upload_image(request):
    if request.method == 'POST':
        form = NoteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_images')
    else:
        form = NoteImageForm()
    return render(request, 'upload_notes/upload_image.html', {'form': form})

def view_images(request):
    images = NoteImage.objects.all()
    return render(request, 'upload_notes/view_images.html', {'images': images})
