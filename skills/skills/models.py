from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.db import models


class SkillTree(models.Model):
    name = models.CharField(max_length=128, blank=False)
    owner = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('detail_skill_tree', args=[str(self.id)])


class SkillTreeBranch(models.Model):
    name = models.CharField(max_length=128, blank=False)
    skill_tree = models.ForeignKey(SkillTree)

    def __unicode__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=128, blank=False)
    point_req = models.IntegerField(blank=True, default=1)
    other_req = models.CharField(max_length=128, blank=True, null=True)
    pre_req = models.ForeignKey("self", blank=True, null=True)
    skill_tree_branch = models.ForeignKey(SkillTreeBranch)

    def __unicode__(self):
        return self.name


class SkillLevel(models.Model):
    level = models.IntegerField(blank=True, default=1)
    cost = models.IntegerField(blank=True, default=1)
    text = models.CharField(max_length=255, blank=False)
    skill = models.ForeignKey(Skill)

    def __unicode__(self):
        return "{0} {1}".format(self.skill.name, self.level)

def create_skill_level(sender, instance, created, **kwargs):
    if created:
        skill_level = SkillLevel()
        skill_level.skill = instance
        skill_level.save()

models.signals.post_save.connect(create_skill_level, sender=Skill)
