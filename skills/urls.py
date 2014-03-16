from django.conf.urls import patterns, include, url

from skills.views import CreateSkillTreeView, DetailSkillTreeView, UpdateSkillTreeView, DeleteSkillTreeView, ListSkillTreeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skills.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^skill-tree/create/', CreateSkillTreeView.as_view(), name='create_skill_tree'),
    url(r'^skill-tree/(?P<pk>\d+)/view/', DetailSkillTreeView.as_view(), name='detail_skill_tree'),
    url(r'^skill-tree/(?P<pk>\d+)/edit/', UpdateSkillTreeView.as_view(), name='update_skill_tree'),
    url(r'^skill-tree/(?P<pk>\d+)/delete/', DeleteSkillTreeView.as_view(), name='delete_skill_tree'),
    url(r'^skill-tree/list/', ListSkillTreeView.as_view(), name='list_skill_trees'),
)
