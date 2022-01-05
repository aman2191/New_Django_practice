from django.shortcuts import render

# Create your views here.
def TemplateView(request):
    return render(request,'testapp/home.html')