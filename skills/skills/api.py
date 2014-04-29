from django.contrib.auth.models import User

from tastypie import fields
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource, ALL

from skills.skills.models import SkillTree, SkillTreeBranch, Skill, SkillLevel


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        allowed_methods = ['get']


class SkillTreeResource(ModelResource):
    owner = fields.ForeignKey(UserResource, 'owner')

    class Meta:
        queryset = SkillTree.objects.all()
        resource_name = 'skill_tree'
        allowed_methods = ['get']
        authorization = Authorization()


class SkillTreeBranchResource(ModelResource):
    skill_tree = fields.ForeignKey(SkillTreeResource, 'skill_tree')

    class Meta:
        queryset = SkillTreeBranch.objects.all()
        resource_name = 'skill_tree_branch'
        authorization = Authorization()
        always_return_data = True


class SkillResource(ModelResource):
    skill_tree_branch = fields.ForeignKey(SkillTreeBranchResource, 'skill_tree_branch')
    pre_req = fields.ForeignKey('self', 'pre_req', null=True)
    skill_levels = fields.ToManyField('skills.skills.api.SkillLevelResource', 'skill_levels', full=True, null=True)

    class Meta:
        queryset = Skill.objects.all()
        resource_name = 'skill'
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'skill_tree_branch': ALL
        }


class SkillLevelResource(ModelResource):
    skill = fields.ForeignKey(SkillResource, 'skill')

    class Meta:
        queryset = SkillLevel.objects.all()
        resource_name = 'skill_level'
        authorization = Authorization()
        always_return_data = True
        filtering = {
            'skill': ALL
        }
