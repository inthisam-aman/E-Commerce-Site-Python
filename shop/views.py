import json
from django.shortcuts import redirect, render, reverse
from shop.form import cutomuserform
from . models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
# Create your views here.
def home(request):
    Product=product.objects.filter(trending=1)
    return render(request,"shop/index.html",{"Product":Product})


def checkout_page(request):
         if request.user.is_authenticated:
            checkout=Cart.objects.filter(user=request.user)
            return render(request,"shop/checkout.html",{"checkout":checkout})
         else:
            return redirect("/")

def remove_fav(request,fid):
    item=Favourite.objects.get(id=fid)
    item.delete()
    return redirect("/favviewpage")

def favviewpage(request):
    if request.user.is_authenticated:
            fav=Favourite.objects.filter(user=request.user)
            return render(request,"shop/fav.html",{"fav":fav})
    else:
        return redirect("/")

def fav_page(request):
     if request.headers.get('x-requested-With')=='XMLHttpRequest':
      if request.user.is_authenticated:
         data=json.load(request)
         product_id=(data['Pid'])
         product_status=product.objects.get(id=product_id)
         if product_status:
            if Favourite.objects.filter(user=request.user.id,product_id=product_id):
                return JsonResponse({'status':'Product Already In Favourite'}, status=200)
            else:               
                Favourite.objects.create(user=request.user,product_id=product_id)
                return JsonResponse({'status':'Product Added To Favourite'}, status=200)       
      else:
          return JsonResponse({'status':'Login Add To Favourite'}, status=200)
     else:
        return JsonResponse({'status':'Invalid Access'}, status=200)


def remove_cart(request,cid):
    cartitem=Cart.objects.get(id=cid)
    cartitem.delete()
    return redirect("/cart")

def cart_page(request):
        if request.user.is_authenticated:
            cart=Cart.objects.filter(user=request.user)
            return render(request,"shop/cart.html",{"cart":cart})
        else:
            return redirect("/")

def add_to_cart(request):
    if request.headers.get('x-requested-With')=='XMLHttpRequest':
     if request.user.is_authenticated:
         data=json.load(request)
         product_qty=(data['Product_qty'])
         product_id=(data['Pid'])
         #print(request.user.id)
         product_status=product.objects.get(id=product_id)
         if product_status:
             if Cart.objects.filter(user=request.user.id,product_id=product_id):
                  return JsonResponse({'status':'Product Already In Cart'}, status=200)
             else:
                 if product_status.quantity>=product_qty:
                     Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                     return JsonResponse({'status':'Product Added To Cart'}, status=200)
                 else:
                     return JsonResponse({'status':'Product Stock Not Available'}, status=200)        
     else:
          return JsonResponse({'status':'Login Add To Cart'}, status=200)
    else:
        return JsonResponse({'status':'Invalid Access'}, status=200)

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfully')
    return redirect("/")

def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,'Loged in Successfully')
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name Or Password")
                return redirect("/login")
        return render(request,"shop/login.html")

def Register(request):
    form=cutomuserform()
    if request.method=='POST':
        form=cutomuserform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registration success you can login now....')
            return redirect('/login')
    return render(request,"shop/register.html",{'form':form})

def collection(request):
    Category=category.objects.filter(status=0)
    return render(request,"shop/collection.html",{"category":Category})

def collectionview(request,name):
    if(category.objects.filter(name=name,status=0)):
        Product=product.objects.filter(category__name=name)
        return render(request,"shop/products/index.html",{"Product":Product,"category_name":name})
    else:
       messages.warning(request,"No Catogery Found")
       return redirect('collection')

def productdetails(request,cname,pname):
       if(category.objects.filter(name=cname,status=0)):
         if(product.objects.filter(name=pname,status=0)):
             Product=product.objects.filter(name=pname,status=0).first()
             return render(request,"shop/products/productdetails.html",{"Product":Product})
         else:
            messages.error(request, "No  catogory found")
            return redirect('collection')
       else:
           messages.error(request, "No  catogory found")
           return redirect('collection')