from django.shortcuts import render,redirect, get_object_or_404
from .models import Item


#CRUD

#create

def create_item(request):
    if request.method == 'POST':
        first_name= request.POST.get('first_name')
        second_name= request.POST.get('second_name')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        description= request.POST.get('description')
        image=request.POST.get('image')
        Item.objects.create(first_name=first_name, second_name=second_name, phone=phone, image=image,email=email,description=description)
        return redirect ('item_list')

    return render(request, 'item_form.html')



     #read
def read_item(request):
    items =  Item.objects.all()
    return render(request, 'item_list.html', {'items':items})

    #update
def update_item(request, pk):
    item= get_object_or_404(Item, pk=pk)
    if request.method =='POST':
        first_name= request.POST.get('first_name')
        second_name= request.POST.get('second_name')
        phone= request.POST.get('phone')
        email= request.POST.get('email')
        description= request.POST.get('description')
        image=request.FILES.get('image')


        item.first_name=first_name
        item.second_name=second_name
        item.phone=phone
        item.email=email
        item.description=description
        # if image: 
        #     item.image = image

        item.save()
        
        
    
        return redirect ('item_list')
    return render(request, 'item_form.html', {'item':item})

      #delete
def delete_item(request, pk):
    item=get_object_or_404(Item, pk=pk)
    if request.method=='POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_confirm_delete.html', {'item':item})