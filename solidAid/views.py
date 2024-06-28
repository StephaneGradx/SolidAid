from django.shortcuts import render

from solidAid.models import Actions

# Create your views here.
 
def index(request):
    action_ids = [1, 2, 3] 
    actions = Actions.objects.filter(id__in=action_ids)
    return render(request, 'index.html', context={"actions": actions})

def details_actions(request):
    action = Actions.objects.all()
    return render(request, "details_actions.html", context={"actions": action})

