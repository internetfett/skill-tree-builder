from django import forms

from skills.skills.models import SkillTree, SkillTreeBranch, Skill, SkillLevel


class CreateSkillTreeForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = SkillTree
        exclude = ["owner"]


class CreateSkillTreeBranchForm(forms.ModelForm):
    name = forms.CharField(required=True)
    skill_tree = forms.ModelChoiceField(queryset=SkillTree.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = SkillTreeBranch


class CreateSkillForm(forms.ModelForm):
    name = forms.CharField(required=True)
    point_req = forms.IntegerField(required=False, initial=0)
    other_req = forms.CharField(required=False)
    pre_req = forms.ModelChoiceField(queryset=Skill.objects.all(), required=False)
    skill_tree_branch = forms.ModelChoiceField(queryset=SkillTreeBranch.objects.all(), widget=forms.HiddenInput())

    class Meta:
        model = Skill


class CreateSkillLevelForm(forms.ModelForm):
    level = forms.IntegerField(required=False)
    cost = forms.IntegerField(required=False, initial=1)
    text = forms.CharField(required=True)
    skill = forms.ModelChoiceField(queryset=Skill.objects.all(), required=True, widget=forms.HiddenInput())

    class Meta:
        model = SkillLevel
