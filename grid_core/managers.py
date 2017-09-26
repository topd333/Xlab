from grid_core.models import (
    Friends, OsGroupsGroups, OsGroupsMembership)
from grid_user.models import User


class GridManager(object):

    """docstring for GridManager"""
    @classmethod
    def get_friends_user(cls, user):
        Friends_list = Friends.objects.filter(principalid=user.principal_id)
        friendids = map(lambda X: X.friend, Friends_list)
        Allfriends = User.objects.filter(principal_id__in=friendids)
        return Allfriends

    @classmethod
    def get_group_user(cls, user):
        membership = OsGroupsMembership.objects.filter(
            principalid=user.principal_id)
        groupids = map(lambda X: X.groupid, membership)
        groups = OsGroupsGroups.objects.filter(groupid__in=groupids)
        return groups
