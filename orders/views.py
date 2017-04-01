from django.shortcuts import render, redirect
from .form import Order_ItemForm,OrdersForm
from .models import Orders_Item,Orders
from django.http import HttpResponse
from course.models import course_details
from login.models import User
# Create your views here.


def new_order(request):
    if request.user.is_authenticated():
        form = Order_ItemForm( request.POST )
        user = request.user
        course_id = request.POST.get('id')
        if course_id is not None:
            if request.POST:
                course = course_details.objects.filter( id = course_id )
                member = User.objects.filter( id = user.id )
                member_id = member.values()[0]['id']
                if course is not None:
                    order_form = Order_ItemForm(initial={"course_Id": course_id})
                    context = {
                        "form": order_form,
                        "course_Id": course_id,
                        "member_id": member_id,
                        "data":course
                    }
                    return render(request,'member_order.html',context)
            else:
                return HttpResponse("Error")
        elif request.POST:
            if form.is_valid():
                form.save()
            return redirect('/payment/')
        else:
            form = Order_ItemForm()
            return render(request,'member_order.html',{'form':form})

def Payment_Gateway(request):
    if request.user.is_authenticated():
        form = OrdersForm( request.POST )
        user = request.user
        order = Orders_Item.objects.filter( member_id = user.id )
        order_id = order.values()[0]['order_item_id']
        order_form = OrdersForm(initial={"order_id": order_id})
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('/login/')
        else:
            context = {
                "form": order_form,
                "order_id": order_id,
                "order": order,
            }
            return render(request, 'payment_gateway.html', context)
        return render(request, 'payment_gateway.html',{'display':"Error"})
