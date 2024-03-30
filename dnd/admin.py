from django.contrib import admin

from .models import Race, Affiliation, NonPlayerCharacter, Enemy, Stat, Skill, Character_Sheet, Weapon, Skill_Class

admin.site.register(Race)
admin.site.register(Stat)
admin.site.register(Weapon)
admin.site.register(Skill)
admin.site.register(Skill_Class)
admin.site.register(Enemy)
admin.site.register(Affiliation)
admin.site.register(Character_Sheet)
admin.site.register(NonPlayerCharacter)


