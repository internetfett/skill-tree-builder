from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from django.shortcuts import render

from skills.skills.forms import CreateSkillTreeForm, CreateSkillTreeBranchForm, CreateSkillForm, CreateSkillLevelForm
from skills.skills.models import SkillTree, SkillTreeBranch, Skill, SkillLevel


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
            'skill_tree_branch_form': CreateSkillTreeBranchForm(initial={'skill_tree': self.object}, prefix="branch"),
            'skill_form': CreateSkillForm(prefix="skill"),
            'skill_level_form': CreateSkillLevelForm(prefix="skill_level")
        })
        return context


class UpdateSkillTreeView(LoginRequiredMixin, SkillTreeMixin, UpdateView):
    template_name = "skill_tree_update.html"


class DeleteSkillTreeView(LoginRequiredMixin, SkillTreeMixin, DeleteView):
    template_name = "skill_tree_delete.html"
    success_url = reverse_lazy('create_skill_tree')


class ListSkillTreeView(LoginRequiredMixin, SkillTreeMixin, ListView):
    template_name = "skill_tree_list.html"


class SkillTreeBranchMixin(object):
    template_name = "skill_tree_branch_create.html"
    form_class = CreateSkillTreeBranchForm
    model = SkillTreeBranch


class CreateSkillTreeBranchView(LoginRequiredMixin, SkillTreeBranchMixin, CreateView):
    def get_initial(self):
        skill_tree = get_object_or_404(SkillTree, id=self.kwargs.get('id'))
        return {
            'skill_tree': skill_tree,
        }


class UpdateSkillTreeBranchView(LoginRequiredMixin, SkillTreeBranchMixin, UpdateView):
    template_name = "skill_tree_branch_update.html"


class DeleteSkillTreeBranchView(LoginRequiredMixin, SkillTreeBranchMixin, DeleteView):
    template_name = "skill_tree_branch_delete.html"

    def get_success_url(self):
        return reverse_lazy('create_skill_tree_branch', args=[str(self.object.skill_tree.id)])


class SkillMixin(object):
    template_name = "skill_create.html"
    form_class = CreateSkillForm
    model = Skill


class CreateSkillView(LoginRequiredMixin, SkillMixin, CreateView):
    def get_initial(self):
        skill_tree_branch = get_object_or_404(SkillTreeBranch, id=self.kwargs.get('id'))
        return {
            'skill_tree_branch': skill_tree_branch,
        }


class UpdateSkillView(LoginRequiredMixin, SkillMixin, UpdateView):
    template_name = "skill_update.html"


class DeleteSkillView(LoginRequiredMixin, SkillMixin, DeleteView):
    template_name = "skill_delete.html"

    def get_success_url(self):
        return reverse_lazy('create_skill', args=[str(self.object.skill_tree_branch.id)])


class SkillLevelMixin(object):
    template_name = "skill_level_create.html"
    form_class = CreateSkillLevelForm
    model = SkillLevel


class CreateSkillLevelView(LoginRequiredMixin, SkillLevelMixin, CreateView):
    def get_initial(self):
        skill = get_object_or_404(Skill, id=self.kwargs.get('id'))
        return {
            'skill': skill,
        }


class UpdateSkillLevelView(LoginRequiredMixin, SkillLevelMixin, UpdateView):
    template_name = "skill_level_update.html"


class DeleteSkillLevelView(LoginRequiredMixin, SkillLevelMixin, DeleteView):
    template_name = "skill_level_delete.html"

    def get_success_url(self):
        return reverse_lazy('create_skill_level', args=[str(self.object.skill.id)])
