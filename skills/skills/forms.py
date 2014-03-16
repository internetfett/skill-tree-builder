from django import forms

from skills.skills.models import SkillTree, SkillTreeBranch


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
