from django.shortcuts import render
import requests
from subprocess import run,PIPE
import sys

def index(request):
  return render(request,'index.html')

def external(request):
    out=run([sys.executable,'musicbeats//music_player_webcam.py'],shell=False,stdout=PIPE)
    #print(out)
    return render(request,'index.html',{'out': out.stdout})

def musicbeats(request):
  return render(request,'index.html')