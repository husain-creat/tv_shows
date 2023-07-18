from django.shortcuts import render,redirect,HttpResponse 
from .models import tv
from django.contrib import messages


def index(request):
    all_shows = tv.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request,'index.html', context)

def new_show(request):
    if request.method =='POST':
        tv.objects.create(
            title = request.POST['title'],
            network = request.POST['network'],
            description = request.POST['description'],
            releace_date = request.POST['releace_date'],
        )
    return render(request,'new_show.html')
def desc(request,id):
    show_desc = tv.objects.get(id = id) 
    context = {
        'show_desc': show_desc
    } 
    return render (request,'description.html',context)

def update(request,id):
    from django.http import HttpResponse

def update(request, id):
    if request.method == 'POST':
        errors = tv.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/' + str(id) + '/edit')
        else:
            show_update = tv.objects.get(id=id) 
            show_update.title = request.POST['title'] 
            show_update.network = request.POST['network'] 
            show_update.description = request.POST['description'] 
            show_update.releace_date = request.POST['releace_date'] 
            show_update.save()
    
    context = {
        'show_update': tv.objects.get(id=id)
    }
    
    return render(request, 'edit.html', context)

            
            
                
            

        

            

    
    


    









    


    

    


    
    

