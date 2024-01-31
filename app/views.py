from django.shortcuts import render, redirect
from django.views import View
from app.models import Customer, Product, Cart, OrderPlaced
from app.forms import CustomerRegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self, request):
        topwears=Product.objects.filter(category='TW')
        buttomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        laptops=Product.objects.filter(category='L')              
        return render(request, "app/home.html", {'topwears':topwears, 'buttomwears':buttomwears, 'mobiles':mobiles, 'laptops':laptops})
    
class ProductDetailView(View):
    def get(self, request, pk):
        product=Product.objects.get(pk=pk) 
        return render(request, 'app/productdetail.html', {'product':product})     
    
def product_detail(request):
 return render(request, 'app/productdetail.html')

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request, data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
        
    elif data=='Readmi' or data== 'Samsung':
         mobiles=Product.objects.filter(category='M').filter(brand=data)
        
    return render(request, 'app/mobile.html', {'mobiles':mobiles})

def login(request):
 return render(request, 'app/login.html')




# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()  # Instantiate the form
        return render(request, 'app/customerregistration.html', {'form': form})
    
    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully submitted the query")
            return redirect('customerregistration')  # Redirect to a success page or any desired URL
        else:
            messages.error(request, "Error in the form submission. Please correct the errors.")
        return render(request, 'app/customerregistration.html', {'form': form})
    

def checkout(request):
 return render(request, 'app/checkout.html')
