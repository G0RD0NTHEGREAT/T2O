from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from uploads.core.models import Document
from uploads.core.forms import DocumentForm
from django.core.files import File

import os.path
import time
import base64
import subprocess
import json


def home(request):
    documents = Document.objects.all()
    for doc in documents:
        doc.inference = "/media/" + "inference_"+doc.document.url.split("/")[-1]
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
            if os.path.exists("media"):

                print("exists")

                pass
            form.save()
            myfile = request.FILES['document']
            query = request.POST['request']
            sequenece = False if len(request.POST) == 2 else True
            print(sequenece)
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
 
            filename_base64 = subprocess.check_output("echo "+str(filename)+" | base64 ", shell=True);
            filename_base64 = str(filename_base64[0:8])
            print("name_base64 is ", filename_base64 )
            
            # print(fs.url())
            if sequenece:

                '''
                 *******************************************
                 change the command in the following line
                 *******************************************   
                '''

                command = "sh run_remote_multi.sh media/" +str(filename)+ " \"" +str(query)+"\" media/"
                os.system(command)
                prefix = 1
                while fs.exists(str(prefix)+"_inference_" + str(filename_base64) + ".jpg"):
                    prefix+=1
                print("prefix: ",prefix)

                
                with open("media/"+str(filename_base64)+'.json', 'r') as f:
                    distros_dict = json.load(f)

                operations = distros_dict[0]['operations']

                output_file_url_list = []
                for index in range(1,prefix):
                    name = operations[index-1][0]
                    if name == "color" or name == "tone":
                        arg = ""
                    else:
                        arg =   "{:.7f}".format(operations[index-1][1][0]) 
                    url = fs.url(str(index)+"_inference_"+str(filename_base64)+".jpg")
                    op = str(name)+ " " + arg
                    print(op,url)
                    output_file_url_list.append((op,url))
                    # output_file_url_list.append(fs.url(str(index)+"_inference_"+str(filename_base64)+".jpg"))
                print("Here are the results:")
                print(output_file_url_list)
                

                
                return render(request, 'core/model_form_upload.html', {
                    'query':query,
                    'show_sequenece':sequenece,
                    'uploaded_file_url': uploaded_file_url,
                    'output_file_url_list':output_file_url_list
                })

            # print(fs.exists("1_inference_2_in.jpg"))
            command = "sh run_remote_single.sh media/" +str(filename)+ " \"" +str(query)+ "\" media/" + "inference_"+str(filename)
            print(command)
            os.system(command)
            
            output_file_url = fs.url("inference_"+str(filename))
            # print(output_file_url)
            return render(request, 'core/model_form_upload.html', {
                'query':query,
                'show_sequenece':sequenece,
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
