from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from grid_core.managers import GridManager


@login_required
def account_deshbord(request):
    allfriends = GridManager.get_friends_user(request.user)
    allgroups = GridManager.get_group_user(request.user)

    return render(
        request, "grid_my/dashbord-my.html",
        {'friends': allfriends, 'groups': allgroups}
        )
