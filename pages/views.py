from django.shortcuts import render
def mainpage(request):
    return render(request, 'pages/mainpage.html')
def serv(request):
    return render(request, 'pages/company_serv.html')

def info(request):
    return render(request, 'pages/company_info.html')