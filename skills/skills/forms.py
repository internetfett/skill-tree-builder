from django import forms

from skills.skills.models import SkillTree


class CreateSkillTreeForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = SkillTree
