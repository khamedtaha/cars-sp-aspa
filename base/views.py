from django.shortcuts import render , redirect

from .models import *



def main(request) : 
   return render(request , "index.html")

def upload_file(request) : 
   if request.method == 'POST':
      name = request.POST.get('name')
      video =  request.FILES.get('video')
      print("===============")
      print(name)
      print(video)
      print("===============")
      Video.objects.create(
         name = name ,
         video = video
      )
      return redirect("/all-video")
   return render(request , "upload_file.html")

def all_video(request) :
   video = Video.objects.all()
   print("===============")
   for v in video : 
      print(v.video.url)
   print("===============")
   return render(request , "all_video.html" , {"video" : video })