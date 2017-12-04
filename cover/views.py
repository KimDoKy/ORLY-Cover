from django.http import HttpResponse
from django.shortcuts import render, redirect
from PIL import Image
from .forms import CoverForm

def index(request):
    if request.method == 'POST':
        form = CoverForm(request.POST)
        if form.is_valid():
            form.cleaned_data  # 이미지를 생성할 데이터
            return redirect('cover:index')
    else:
        form = CoverForm()
    return render(request, 'cover/index.html', {
        'form': form,
    })

# 위 데이터를 받아서 이미지를 그림
def image_generator(request):
    im = Image.new('RGB', (256, 256), 'yellow')
    response = HttpResponse(content_type='image/jpeg')
    im.save(response, format='JPEG')
    return response