from django.shortcuts import render

def index(request):
    con = MySQLdb.connect()
    return render(request, 'index.html')
