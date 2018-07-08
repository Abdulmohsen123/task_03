from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    bukhari = {
        'name': 'bukhari',
        'food_type': 'rice',
    }
    bo_zaid = {
        'name': 'bo_zaid',
        'food_type': 'kuwaiti rice',
    }
    kfc = {
        'name': 'kfc',
        'food_type': 'fried chicken',
    }

    list_of_objects = [
           bukhari,
           bo_zaid,
           kfc,
    ]
    context = {
            'my_list': list_of_objects,
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    bukhari = {
        'name': 'bukhari',
        'food_type': 'rice',
    }

    # my_objects = [
    #        bukhari,
    # ]

    context = {
        'my_object': bukhari,
    }
    return render(request, 'detail.html', context)
