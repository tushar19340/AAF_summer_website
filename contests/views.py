from django.shortcuts import render
from contests import models

# Create your views here.

def contests(request):

    Contests = models.Contest.objects.all()
    Categories = models.Category.objects.all()

    requested_filters = request.GET.getlist('filter_list')

    print(requested_filters)
    filtered_contests = []
    
    if(len(requested_filters) > 0):
        for contest in Contests:
            curr_categories = contest.category.all()

            for category in curr_categories:
                if category.name in requested_filters:
                    filtered_contests.append(contest)
                    break          
        print("Hello from filter if")  
        Contests = filtered_contests

    context = {
        'contests': Contests,
        'filters': Categories,
        'active_filters': requested_filters
    }

    return render(request, 'contests/contests.html', context)

def contests_individual(request, contest_id):

    contest = models.Contest.objects.get(pk=contest_id)

    print(contest)

    context = {
        'contest': contest
    }

    return render(request, 'contests/individual_contest.html', context)
