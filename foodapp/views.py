from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    return render(request,"index.html")



def userReg(request):
    msg=''
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        goal=request.POST['goal']
        password=request.POST['password']
        try:
            user=CustomUser.objects.create_user(username=email,password=password,is_active=0,usertype="User")
            user.save()
            cust=User.objects.create(name=name,phone=phone,email=email,address=address,goal=goal,user=user)
            cust.save()
            msg="Registration Successfull.."
            return render(request,"userReg.html",{"msg":msg})
        except:
            msg="Username Already Exists.."
            return render(request,"userReg.html",{"msg":msg})
    else: 
        return render(request,"userReg.html",{"msg":msg})

def deliveryReg(request):
    msg=''
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        password=request.POST['password']
        try:
            user=CustomUser.objects.create_user(username=email,password=password,is_active=0,usertype="Delivery")
            user.save()
            cust=Delivery.objects.create(name=name,phone=phone,email=email,address=address,user=user)
            cust.save()
            msg="Registration Successfull.."
            return render(request,"deliveryReg.html",{"msg":msg})
        except:
            msg="Username Already Exists.."
            return render(request,"deliveryReg.html",{"msg":msg})
    else: 
        return render(request,"deliveryReg.html",{"msg":msg})

def supplierReg(request):
    msg=''
    if request.POST:
        company_name=request.POST['company_name']
        owner_name=request.POST['owner_name']
        type=request.POST['type']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        password=request.POST['password']
        try:
            user=CustomUser.objects.create_user(username=email,password=password,is_active=0,usertype="Supplier")
            user.save()
            cust=Supplier.objects.create(comapny_name=company_name,owner_name=owner_name,type=type,phone=phone,email=email,address=address,user=user)
            cust.save()
            msg="Registration Successfull.."
            return render(request,"supplierReg.html",{"msg":msg})
        except:
            msg="Username Already Exists.."
            return render(request,"supplierReg.html",{"msg":msg})
    else: 
        return render(request,"supplierReg.html",{"msg":msg})


def login(request):
    msg=''
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser:
                return redirect("/adminHome")
            elif user.usertype == 'User':
                data=User.objects.get(email=username)
                request.session['id']=data.id
                return redirect("/userHome")
            elif user.usertype == 'Delivery':
                data=Delivery.objects.get(email=username)
                request.session['id']=data.id
                return redirect("/DeliveryHome")
            elif user.usertype == 'Supplier':
                data=Supplier.objects.get(email=username)
                request.session['id']=data.id
                return redirect("/supplierHome")
        else:
            msg="Invalid Username or Password!"
            return render(request,"login.html",{"msg":msg})
    else:
        return render(request,"login.html",{"msg":msg})
    
def adminHome(request):
    return render(request,"adminHome.html")
    
def adminUser(request):
    data=User.objects.filter().order_by("-id")
    return render(request,"adminUser.html",{"data":data})
    
def adminApproveUser(request):
    id=request.GET['id']
    status=request.GET['status']
    data=CustomUser.objects.get(id=id)
    data.is_active=status
    data.save()
    return redirect("/adminUser")
    

    
def adminDelivery(request):
    data=Delivery.objects.filter().order_by("-id")
    return render(request,"adminDelivery.html",{"data":data})


def adminApproveDelivery(request):
    id=request.GET['id']
    status=request.GET['status']
    data=CustomUser.objects.get(id=id)
    data.is_active=status
    data.save()
    return redirect("/adminDelivery")

    
def adminSupplier(request):
    data=Supplier.objects.filter().order_by("-id")
    return render(request,"adminSupplier.html",{"data":data})

def adminApproveSupplier(request):
    id=request.GET['id']
    status=request.GET['status']
    data=CustomUser.objects.get(id=id)
    data.is_active=status
    data.save()
    return redirect("/adminSupplier")

def adminAdd(request):
    data=Food.objects.filter().order_by("-id")
    
    if request.POST:
        pid=request.POST['id']
        price=request.POST['price']
        food=Food.objects.get(id=pid)
        food.price=price
        food.save()

    return render(request,"adminAdd.html",{"food":data})


def adminApproveFood(request):
    id=request.GET['id']
    status=request.GET['status']
    food=Food.objects.get(id=id)
    food.status=status
    food.save()
    return redirect("/adminAdd")

def adminReport(request):
    selected_month = request.GET.get('month', '')
    bok = Bookings.objects.filter().exclude(status='CART').order_by("-id")
    
    if selected_month:
        try:
            year, month = map(int, selected_month.split('-'))
            bok = bok.filter(book_date__year=year, book_date__month=month)
        except ValueError:
            return render(request, "adminReport.html", {"bok": bok, "error": "Invalid month format", "selected_month": selected_month})
    
    total_price = sum(b.total for b in bok)
    return render(request, "adminReport.html", {"bok": bok, "selected_month": selected_month, "growth_total_price": total_price})




def userHome(request):
    return render(request,"userHome.html")

def userFood(request):
    food=Food.objects.filter(status="Approved").order_by("-id")
    # if request.POST:
    #     goal=request.POST['goal']
    #     # if goal == "All":
    #     #     food=Food.objects.filter()
    #     #     return render(request,"userFood.html",{"foods":food})
    #     if goal:
    #         food=Food.objects.filter(goal=goal)
    #         return render(request,"userFood.html",{"foods":food})
    #     else:
    #         messages.info(request,"Please select your goal")
    #         return render(request,"userFood.html",{"food":food})
    if request.POST:
        goal = request.POST.get('goal', '')
        if goal:
            food = Food.objects.filter(goal=goal)
            return render(request, "userFood.html", {"foods": food})
        else:
            food = Food.objects.filter(status="Approved").order_by("-id")
            return render(request, "userFood.html", {"foods": food})

    else:
        return render(request,"userFood.html",{"food":food})
    
def userCart(request):
    uid=request.session['id']
    user=User.objects.get(id=uid)
    if request.POST:
        pid=request.POST['pid']
        count=int(request.POST['count'])
        food=Food.objects.get(id=pid)
        bok = Bookings.objects.filter(cust_id=uid, food_id=pid, status="CART").first()
        if bok:  
            bok.count += count  
            bok.total = int(food.price) * bok.count 
            bok.save()  

           

            messages.info(request, "Product quantity updated in cart.")
            return redirect("/userFood")

        else:  
            total=int((food.price) * count)
            bok = Bookings.objects.create(cust=user,food=food,count=count,total=total)
            bok.save()

            

            messages.info(request, "Product Added to Cart.")
            return redirect("/userFood")
    else:
        return redirect("/userFood")
   
def userCartView(request):
    uid=request.session['id']
    data=Bookings.objects.filter(cust_id=uid,status="CART").order_by("-id")
    rate=0
    for i in data:
        rate=rate + int(i.total)
    return render(request,"userCart.html",{"data":data,"rate":rate})
    
def userRemove(request):
    id=request.GET['id']
    bok=Bookings.objects.get(id=id)
    bok.delete()
    return redirect("/userCartView")
    
def userPay(request):
    uid=request.session['id']
    user=User.objects.get(id=uid)
    bok=Bookings.objects.filter(cust_id=uid)
    rate=0
    for i in bok:
        if i.status == "CART":
            rate += int(i.total)
    if request.POST:
        messages.info(request,"Payment Succesfull..")

        for i in bok:
            if i.status == "CART":
                i.status = "Booked"
                i.book_date = datetime.now()
                i.save()
        return redirect("/userBookings")

    return render(request,"userPay.html",{"rate":rate})
    
def userBookings(request):
    uid=request.session['id']
    data=Bookings.objects.filter(cust_id=uid).order_by("-id")
    return render(request,"userBookings.html",{"data":data})
    
def userFeedback(request):
    uid=request.session['id']
    id=request.GET['id']
    bok=Bookings.objects.get(id=id)
    if request.POST:
        rating=request.POST['rating']
        feedback=request.POST['feedback']
        feed=Feedback.objects.create(book=bok,review=feedback,rating=rating)
        feed.save()
        bok.status="Feedback Completed"
        bok.save()
        messages.info(request,"Feedback added succesfully..")
        return redirect("/userBookings")

    return render(request,"userFeedback.html")

def userReport(request):
    uid=request.session['id']
    selected_month = request.GET.get('month', '')
    bok = Bookings.objects.filter(cust_id=uid).exclude(status='CART').order_by("-id")
    
    if selected_month:
        try:
            year, month = map(int, selected_month.split('-'))
            bok = bok.filter(book_date__year=year, book_date__month=month)
        except ValueError:
            return render(request, "userReport.html", {"bok": bok, "error": "Invalid month format", "selected_month": selected_month})
    
    total_price = sum(b.total for b in bok)
    return render(request, "userReport.html", {"bok": bok, "selected_month": selected_month, "growth_total_price": total_price})
    
def userGuidence(request):
    data=Guidence.objects.filter().order_by("-id")
    return render(request,"userGuidence.html",{"data":data})



    
def supplierHome(request):
    return render(request,"supplierHome.html")
    
def supplierAdd(request):
    uid=request.session['id']
    user=Supplier.objects.get(id=uid)
    foods=Food.objects.filter(user_id=uid).order_by("-id")
    if request.POST:
        goal=request.POST['goal']
        name=request.POST['name']
        desc=request.POST['desc']
        incredients=request.POST['incredients']
        nutrients=request.POST['Nutrients']
        time=request.POST['time']
        amount=request.POST['amount']
        price=request.POST['price']
        image=request.FILES['image']

        food=Food.objects.create(goal=goal,name=name,desc=desc,incredients=incredients,
                                 nutrients=nutrients,time=time,amount=amount,price=price,
                                 image=image,user=user)
        food.save()
        messages.info(request,"Item Added Successfully..")
        return redirect("/supplierAdd")
    else:
        return render(request,"supplierAdd.html",{"food":foods})
    
def supplierOreder(request):
    uid=request.session['id']
    data=Bookings.objects.filter(food__user_id=uid).order_by("-id")
    boy=Delivery.objects.filter(status="Available")
    if request.POST:
        bid=request.POST['bid']
        boy=request.POST['boy']
        bok=Bookings.objects.get(id=bid)
        boy_=Delivery.objects.get(id=boy)
        bok.boy=boy_
        bok.status="Assigned"
        bok.save()



    return render(request,"supplierOreder.html",{"data":data,"boy":boy})
    
def supplierGuidence(request):
    uid=request.session['id']
    user=Supplier.objects.get(id=uid)
    data=Guidence.objects.filter(shop_id=uid).order_by("-id")
    if request.POST:
        goal=request.POST['goal']
        file=request.FILES['file']
        guide=Guidence.objects.create(shop=user,goal=goal,file=file)
        guide.save()
        messages.info(request,"Guidence added successfully..")
        return redirect("/supplierGuidence")


    return render(request,"supplierGuidence.html",{"data":data})
    
def guidenceOpen(request):
    data=request.GET['file']
    return render(request,"guidenceOpen.html",{"file":data})
    
def DeliveryHome(request):
    uid=request.session['id']
    data=Delivery.objects.get(id=uid)
    return render(request,"DeliveryHome.html",{"data":data})
    
def deliveryStatus(request):
    uid=request.session['id']
    data=Delivery.objects.get(id=uid)
    status=request.GET['status']
    data.status=status
    data.save()
    return redirect("/DeliveryHome")
    
def DeliveryOrder(request):
    uid=request.session['id']
    data=Bookings.objects.filter(boy_id=uid,status="Assigned").order_by("-id")
    return render(request,"DeliveryOrder.html",{'data':data})

    
def dBookingAccept(request):
    uid=request.session['id']
    boy=Delivery.objects.get(id=uid)
    id=request.GET['id']
    status=request.GET['status']
    bok=Bookings.objects.get(id=id)
    bok.status=status
    bok.save()
    if boy.status == "Available":
        messages.info(request,"mark your status as UNAVAILABLE " )
        return redirect("/DeliveryHome")
    else :
        messages.info(request,"mark your status as AVAILABLE " )
        return redirect("/DeliveryHome")

    
def deliveryDelivered(request):
    uid=request.session['id']
    data=Bookings.objects.filter(boy_id=uid).exclude(status="Assigned").order_by("-id")
    return render(request,"deliveryDelivered.html",{'data':data})
    
def dBookingComplete(request):
    id=request.GET['id']
    status=request.GET['status']
    bok=Bookings.objects.get(id=id)
    bok.status=status
    bok.save()
    messages.info(request,"mark your status as AVAILABLE" )
    return redirect("/DeliveryHome")
