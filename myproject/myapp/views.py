from django.shortcuts import render,redirect
from django.http import HttpResponse
from myapp.models import Book

# Create your views here.
def index(request):
    return render(request,"index.html")


def Book_list(request):
    if request.method == 'POST':
        # รับข้อมูล
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        table = request.POST['table']
        message = request.POST['message']
        print(name, email, phone, date, time, table, message)
        #บันทึกข้อมูล
        book = Book.objects.create(
            name=name,
            email=email,
            phone=phone,
            date=date,
            time=time,
            table=table,
            message=message
        )
        book.save()
        #เปลี่ยนเส้นทาง
        return redirect("/")

    else :
        return render(request,"index.html")



