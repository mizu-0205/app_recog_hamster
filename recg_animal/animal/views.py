from django.shortcuts import redirect, render
from .forms import ImageForm
from .models import Image
from .recognition.recognize import main

def showall(request):
    images = Image.objects.all().order_by("-pk")
    context = {"images": images}
    return render(request, "animal/showall.html", context)

def upload(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img = Image.objects.get(pk=Image.objects.count())
            output = main(img.picture)
            img.first_name = output[0][0]
            img.first_value = output[0][1]
            img.second_name = output[1][0]
            img.second_value = output[1][1]
            img.save()
            return redirect("animal:result")
    else:
        form = ImageForm()
    context = {"form": form}
    return render(request, "animal/upload.html", context)

def result(request):
    images = Image.objects.all().order_by("-pk")
    context = {"images": images[1:], "now_image": images[0]}
    return render(request, "animal/result.html", context)
