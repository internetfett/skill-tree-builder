from django.contrib.auth.models import User

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource

from skills.skills.models import SkillTree, SkillTreeBranch


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'


class SkillTreeResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')

    class Meta:
        queryset = SkillTree.objects.all()
        resource_name = 'skill_tree'
        authorization = Authorization()


class SkillTreeBranchResource(ModelResource):
    skill_tree = fields.ForeignKey(SkillTreeResource, 'skill_tree')

    class Meta:
        queryset = SkillTreeBranch.objects.all()
        resource_name = 'skill_tree_branch'
        authorization = Authorization()