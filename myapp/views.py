from django.shortcuts import render,HttpResponse,redirect # type: ignore
from .models import*

# Create your views here.
# def home(request):
#     return HttpResponse("Hello, Django!")


def home(request):
    return HttpResponse("Hello, Django!")

def crud(request):
    uid=Employee.objects.all()
    contaxt={
        "uid":uid
    }
    return render(request, "crud.html", contaxt)

def create(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']
        Employee.objects.create(name=name,email=email,address=address,phone=phone)
        return redirect('crud')
    else:
        return render(request,"crud.html")

def update(request,id):
    uid=Employee.objects.get(id=id)
    print(uid)

    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        phone=request.POST['phone']

        uid.name=name
        uid.email=email
        uid.address=address
        uid.phone=phone
        uid.save()
        return redirect('crud')
    else:
        return render(request, "crud.html")
    
def delete(request,id):
    uid=Employee.objects.get(id=id)
    uid.delete()
    return redirect('crud')

def index(request):
    cat_list = category.objects.prefetch_related('subcategories').all()
    did = request.GET.get('did')
    sid = request.GET.get('sid')
    context = {
        "cat_id": cat_list,
        "did": did,
        "sid": sid,
    }
    return render(request, 'index.html', context)

def shop(request):
    cat_id=category.objects.all()
    sub=request.GET.get('sub')
    contaxt={   
        "cat_id":cat_id,
        "sub":sub
    }
    return render(request, 'shop.html',contaxt)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def contact(request):
    return render(request, 'contact.html')

def detail(request):
    return render(request, 'detail.html')

def register(request):
    if request.POST:
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
    
        if password == confirm_password:
            registeruser.objects.create(name=name,email=email,password=password,confirm_password=confirm_password)
            return render(request,'login.html')
            
    
        else:
            contaxt={
                "msg":"password do not match"
            }
        return render(request, 'register.html',contaxt)

    else:
        return render(request, 'register.html')
    
def login(request):
    if 'email' in request.session:
        return render(request,"index.html")
    try:
        if request.POST:
            email=request.POST['email']
            password=request.POST['password']

            uid=registeruser.objects.get(email=email)
            print(uid)
            if uid.email == email:

                request.session['email']=uid.email
                if uid.password == password:
                    return redirect("index")
                else:
                    contaxt={
                        "msg":"Invalid password"
               }
                    return render(request,"login.html",contaxt)
            else:
                return render(request,"login.html")

    except registeruser.DoesNotExist:
        contaxt={
            "msg":"Invalid Email"
        }
        return render(request,"register.html",contaxt)
    else:
        return render(request, 'login.html')
    
# def logout(request):
#     if 'email' in request.session:
#         del request.session['email']
#         return render(request,"login.html")
#     else:
#         return render(request,"login.html")
    
def category1(request):
    cat_id=category.objects.all()
    contaxt={
        "cat_id":cat_id
    }
    return render(request,"index.html",contaxt)

def category2(request):
    sub=subcategory.objects.all()
    contaxt={   
        "sub":sub
    }   
    return render(request,"index.html",contaxt)

# def category_list(request):
#     categories = category.objects.prefetch_related('subcategories').all()
#     context = {
#         'categories': categories
#     }
#     return render(request, 'index.html', context)