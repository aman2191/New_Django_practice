from django.shortcuts import render

# Create your views here.
def TemplateView(request):
    print('aman')
    return render(request,'testapp/home.html')
