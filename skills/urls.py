from django.conf.urls import patterns, include, url

from skills.views import CreateSkillTreeView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skills.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^skill-tree/create/', CreateSkillTreeView.as_view(), name='create_skill_tree'),
)
