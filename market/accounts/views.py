from django.shortcuts import render
from accounts.forms import vendorform,customerform


# Create your views here.
#-------------INDEX---PAGE---------------------------------
def index(request):
    return render(request,'index.html')

#-------------VENDOR--REGISTRATION---PAGE---------------------------------
def venreg(request):
    vform=vendorform # getting all the details of the vendorform and storing it in a variable

    if request.method=="POST": 
        vform=vendorform(request.POST)

        if vform.is_valid():
            vform.save()
 
    return render(request,'vendreg.html',{'vform':vform})  

#-------------CUSTOMER-----REGISTRATION--PAGE---------------------------------
def cusreg(request):
    cform=customerform # getting all the details of the customerform and storing it in a variable

    if request.method=="POST":
        cform=customerform(request.POST)

        if cform.is_valid():
            cform.save()

    return render(request,'custreg.html',{'cform':cform})
