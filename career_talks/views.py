from django.shortcuts import render, HttpResponse
from career_talks import models


# fetch all the career talks
def career_talks(request):

    Career_Talks = models.Career_Talk.objects.all()
    Categories = models.Category.objects.all() # All the categories we have (to show the filter option on frontend)

    requested_filters = request.GET.getlist('filter_list')

    print(requested_filters)
    
    filtered_talks = [] # Filtered talks list
    
    if(len(requested_filters) > 0):
        for talk in Career_Talks:
            curr_categories = talk.category.all()

            for category in curr_categories:
                if category.name in requested_filters:
                    filtered_talks.append(talk)
                    break          
        print("Hello from filter if")  
        Career_Talks = filtered_talks

    context = {
        'career_talks': Career_Talks,
        'filters': Categories,
        'active_filters': requested_filters
    }

    return render(request, 'career_talks/career_talks.html', context)

# Fetch a particular career talk
def career_talk_individual(request, talk_id):
    career_talk = models.Career_Talk.objects.get(pk = talk_id)

    context = {
        'career_talk' : career_talk
    }

    return render(request, 'career_talks/career_talk_individual.html', context)
