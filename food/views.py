from django.shortcuts import render # type: ignore
from django.http import HttpResponse
from .models import food


#read
def foodMenu(request):
    c = food.objects.all()
    return render(request,"food\idex.html",{'food':c})


#create
def food_menu(request):
    if request.method == "POST":
        # Get the data from the POST request
        name = request.POST.get('name')  
        food_type = request.POST.get('food')
        food_price = request.POST.get('food_price')
        description = request.POST.get('description')

        # Create a new food item and save it to the database
        new_food = food(
            food_name=name,
            food_type=food_type,
            food_price=food_price,
            description=description
        )
        new_food.save()  # Save the new entry to the database

        return HttpResponse("Food item added successfully!")  # Send a success response

    return render(request, 'food/food_menu.html')  # Replace with the name of your HTML template
