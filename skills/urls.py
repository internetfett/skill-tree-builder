from django.conf.urls import patterns, include, url

from tastypie.api import Api

from skills.api import UserResource, SkillTreeResource, SkillTreeBranchResource, SkillResource, SkillLevelResource
from skills.views import CreateSkillTreeView, DetailSkillTreeView, UpdateSkillTreeView, DeleteSkillTreeView, ListSkillTreeView
from skills.views import CreateSkillTreeBranchView, UpdateSkillTreeBranchView, DeleteSkillTreeBranchView
from skills.views import CreateSkillView, UpdateSkillView, DeleteSkillView
from skills.views import CreateSkillLevelView, UpdateSkillLevelView, DeleteSkillLevelView

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(SkillTreeResource())
v1_api.register(SkillTreeBranchResource())
v1_api.register(SkillResource())
v1_api.register(SkillLevelResource())

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^skill-tree/create/', CreateSkillTreeView.as_view(), name='create_skill_tree'),
    url(r'^skill-tree/(?P<pk>\d+)/view/', DetailSkillTreeView.as_view(), name='detail_skill_tree'),
    url(r'^skill-tree/(?P<pk>\d+)/edit/', UpdateSkillTreeView.as_view(), name='update_skill_tree'),
    url(r'^skill-tree/(?P<pk>\d+)/delete/', DeleteSkillTreeView.as_view(), name='delete_skill_tree'),
    url(r'^$', ListSkillTreeView.as_view(), name='list_skill_trees'),
    url(r'^skill-tree-branch/create/(?P<id>\d+)/', CreateSkillTreeBranchView.as_view(), name='create_skill_tree_branch'),
    url(r'^skill-tree-branch/(?P<pk>\d+)/edit/', UpdateSkillTreeBranchView.as_view(), name='update_skill_tree_branch'),
    url(r'^skill-tree-branch/(?P<pk>\d+)/delete/', DeleteSkillTreeBranchView.as_view(), name='delete_skill_tree_branch'),
    url(r'^skill/create/(?P<id>\d+)/', CreateSkillView.as_view(), name='create_skill'),
    url(r'^skill/(?P<pk>\d+)/edit/', UpdateSkillView.as_view(), name='update_skill'),
    url(r'^skill/(?P<pk>\d+)/delete/', DeleteSkillView.as_view(), name='delete_skill'),
    url(r'^skill-level/create/(?P<id>\d+)/', CreateSkillLevelView.as_view(), name='create_skill_level'),
    url(r'^skill-level/(?P<pk>\d+)/edit/', UpdateSkillLevelView.as_view(), name='update_skill_level'),
    url(r'^skill-level/(?P<pk>\d+)/delete/', DeleteSkillLevelView.as_view(), name='delete_skill_level'),
)
