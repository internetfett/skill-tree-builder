from django.conf.urls import patterns, include, url

from tastypie.api import Api

from skills.api import UserResource, SkillTreeResource, SkillTreeBranchResource, SkillResource
from skills.views import CreateSkillTreeView, DetailSkillTreeView, UpdateSkillTreeView, DeleteSkillTreeView, ListSkillTreeView

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(SkillTreeResource())
v1_api.register(SkillTreeBranchResource())
v1_api.register(SkillResource())

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
    url(r'^skill-tree/list/', ListSkillTreeView.as_view(), name='list_skill_trees'),
)
