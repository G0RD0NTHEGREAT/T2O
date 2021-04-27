# Our model T2Onet is accepted to CVPR 2021 !!! 
check out our paper at https://www.cs.rochester.edu/~cxu22/p/cvpr2021_langimgplan_paper.pdf  
CVPR publication will be availble in June 2021 on CVF.

# T2ONet 
T2ONet is used in our language-guided image editing paper.
This repo provides a web user interface for using the T2ONet.

## What does it do
The web app is currently not delopyed, so if you want to test, please contact me at gordonxyh@mgmail.com
Upload an image you want to edit, and a editing request such as "brighten the image and sharpen".
The image will be edited automatically by our T2ONet.

## How does it work
All computation runs on GPU-machine located in University of Rochester's Vision lab.
T2ONet is a Machine Learning model trained with samples to perform image editing.
For specific implementation of the T2ONet, please refer to our paper.

## Running Locally

Change the ssh crudentials in run_remote_single.sh and run_remote_multi.sh

```bash
git clone https://github.com/G0RD0NTHEGREAT/T2O.git
```

```bash
pip install -r requirements.txt
```
```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```
