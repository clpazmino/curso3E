from django.shortcuts import render

# Create your views here.
def inicio(request):
   return render(request,'inicio.html')

def historia(request):
   return render(request,'historia.html')



def visitanos(request):
   return render(request,'visitanos.html')

