
from django.shortcuts import render
from .forms import ReserveFrom

# Create your views here.
from .models import property , catagory

def property_list(request):
    property_list = property.objects.all() 
    template = 'property/list.html' 
    context = {
        'property_list' : property_list
    }
    
    return render(request , template , context)

def property_detail(request , id):
    property_detail = property.objects.get( id = id )
    template = 'property/detail.html'
    

    if request.method == 'POST':
        reserve_form = ReserveFrom(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()

    else:
        reserve_form = ReserveFrom()


    context = {
        'property_detail' : property_detail ,
        'reserve_form' : reserve_form 
    }
    
    return render(request , template , context)