from django.shortcuts import render, HttpResponse
from career_talks import models

def career_talks(request):

    Career_Talks = models.Career_Talk.objects.all()
    Categories = models.Category.objects.all()

    requested_filters = request.GET.getlist('filter_list')

    print(requested_filters)
    filtered_talks = []
    
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

def career_talk_individual(request, talk_id):

    return render(request, 'career_talks/career_talk_individual.html')
