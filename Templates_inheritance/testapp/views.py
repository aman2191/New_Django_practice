from django.shortcuts import render

# Create your views here.
def TemplateView(request):
    print('farkade')
    print('aman')
    return render(request,'testapp/home.html')
