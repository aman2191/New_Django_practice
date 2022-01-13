from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.
def TemplateView(request):
    print('farkade')
    print('aman')
    return render(request,'testapp/home.html')

def indexview(request):
    request.session.set_test_cookie()
    print(request.COOKIES)
    return HttpResponse("index page")
def Check_view(request):
    if request.session.test_cookie_worked():
        print("session work")
        request.session.delete_test_cookie()
        return HttpResponse("Chicking page")
    
def CountView(request):
    if 'count' in request.COOKIES:
        count_val=int(request.COOKIES['count'])+1
        # return count_val
    else:
        count_val=1
    response=render(request,'testapp/home.html',{'count_val':count_val})
    response.set_cookie('count',count_val)
    return response
    
        
        
