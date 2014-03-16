from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from django.shortcuts import render

from skills.skills.forms import CreateSkillTreeForm
from skills.skills.models import SkillTree


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class SkillTreeMixin(object):
    template_name = "skill_tree_create.html"
    form_class = CreateSkillTreeForm
    model = SkillTree


class CreateSkillTreeView(SkillTreeMixin, CreateView, LoginRequiredMixin):
    pass
