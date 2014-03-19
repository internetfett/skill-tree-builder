from django.contrib import admin

from skills.skills.models import SkillTree, SkillTreeBranch, Skill, SkillLevel

admin.site.register(SkillTree)
admin.site.register(SkillTreeBranch)
admin.site.register(Skill)
admin.site.register(SkillLevel)
