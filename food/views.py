from django.shortcuts import render ,get_object_or_404 ,redirect# type: ignore
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


def update_food(request, id):
    food_item = get_object_or_404(food, id=id)

    if request.method == "POST":
        # Update fields with data from the POST request
        food_item.food_name = request.POST.get('name')
        food_item.food_type = request.POST.get('food')
        food_item.food_price = request.POST.get('food_price')
        food_item.description = request.POST.get('description')
        food_item.save()  # Save the updated food item

        return redirect('foodMenu')  # Redirect to the food menu page

    return render(request, 'food/update_food.html', {'food': food_item})  # Render update form


# Delete
def delete_food(request, id):
    food_item = get_object_or_404(food, id=id)  # Get the specific food item
    if request.method == "POST":
        food_item.delete()  # Delete the item
        return redirect('foodMenu')  # Redirect to the food menu page

    return render(request, 'food/delete_confirm.html', {'food': food_item}) 