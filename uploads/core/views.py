from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
import os.path
import time


def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            myfile = request.FILES['document']
            query = request.POST['request']
            # print(query)
            # print(myfile.name)
            
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            # print(fs.url())
            command = "sh run_remote.sh media/" +str(filename)+ " \"" +str(query)+ "\" media/" + "inference_"+str(filename)
            print(command)
            os.system(command)
            output_file_url = fs.url("inference_"+str(filename))
            # print(output_file_url)
            return render(request, 'core/model_form_upload.html', {
                'uploaded_file_url': uploaded_file_url,
                'output_file_url':output_file_url
            })
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })


# def model_form_upload(request):
#     if request.method == 'POST':
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocumentForm()
#     return render(request, 'core/model_form_upload.html', {
#         'form': form
#     })
