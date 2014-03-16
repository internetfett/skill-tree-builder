from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from django.shortcuts import render

from skills.skills.forms import CreateSkillTreeForm, CreateSkillTreeBranchForm
from skills.skills.models import SkillTree


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)


class SkillTreeMixin(object):
    template_name = "skill_tree_create.html"
    form_class = CreateSkillTreeForm
    model = SkillTree


class CreateSkillTreeView(LoginRequiredMixin, SkillTreeMixin, CreateView):
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class DetailSkillTreeView(LoginRequiredMixin, SkillTreeMixin, DetailView):
    template_name = "skill_tree_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DetailSkillTreeView, self).get_context_data(**kwargs)
        context.update({
            'skill_tree_branch_form': CreateSkillTreeBranchForm(initial={'skill_tree': self.object}),
        })
        return context
    


class UpdateSkillTreeView(LoginRequiredMixin, SkillTreeMixin, UpdateView):
    template_name = "skill_tree_update.html"


class DeleteSkillTreeView(LoginRequiredMixin, SkillTreeMixin, DeleteView):
    template_name = "skill_tree_delete.html"
    success_url = reverse_lazy('create_skill_tree')


class ListSkillTreeView(LoginRequiredMixin, SkillTreeMixin, ListView):
    template_name = "skill_tree_list.html"
