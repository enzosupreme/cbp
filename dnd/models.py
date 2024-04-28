from django.contrib.auth.models import User
from django.db import models


class Stat(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Stats'

    def __str__(self):
        return self.name

class Race(models.Model):
    name = models.CharField(max_length=255)
    bonus = models.ForeignKey(Stat, related_name='race',blank=True, null=True,on_delete=models.CASCADE)
    darkvision = models.BooleanField(default=False)
    #race = models.ForeignKey(Race, related_name='npc', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Races'

    def __str__(self):
        return self.name

class Affiliation(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Affiliations'
    def __str__(self):
        return self.name

class NonPlayerCharacter(models.Model):
    race = models.ForeignKey(Race, related_name='npc', on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, related_name='npc', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    invisible = models.BooleanField(default=False)

    pictures = models.URLField(max_length=200, blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'NPCs'
    def __str__(self):
        return self.name

class Enemy(models.Model):
    race = models.ForeignKey(Race, related_name='enemy', on_delete=models.CASCADE)
    affiliation = models.ForeignKey(Affiliation, related_name='enemy', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    height = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hp = models.IntegerField(null=True)
    str = models.IntegerField(null=True)
    dex = models.IntegerField(null=True)
    con = models.IntegerField(null=True)
    int = models.IntegerField(null=True)
    wis = models.IntegerField(null=True)
    cha = models.IntegerField(null=True)
    ac = models.IntegerField(null=True)
    speed = models.CharField(max_length=255, blank=True, null=True)
    abilities = models.TextField(blank=True, null=True)
    actions = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    invisible = models.BooleanField(default=False)



    pictures = models.URLField(max_length=200, blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Enemies'
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'skills'
    def __str__(self):
        return self.name

class Skill_Class(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'classes'
    def __str__(self):
        return self.name

class Weapon(models.Model):
    name = models.CharField(max_length=255)
    damage = models.CharField(max_length=255)


    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'weapons'
    def __str__(self):
        return self.name

class Spell(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=4088)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'spells'
    def __str__(self):
        return self.name

class DM_Menu(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'dm Options'

    def __str__(self):
        return self.name
class Monster(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField(max_length=200, blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'monsters'
    def __str__(self):
        return self.name
class Map(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image5 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image6 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image7 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image8 = models.ImageField(upload_to='project_images', blank=True, null=True)


    link = models.URLField(max_length=200, blank=True, null=True)
    monsters1 = models.ForeignKey(Monster, related_name='monster', on_delete=models.CASCADE, blank=True, null=True)
    monsters2 = models.ForeignKey(Monster, related_name='monster2', on_delete=models.CASCADE, null=True, blank=True)
    monsters3 = models.ForeignKey(Monster, related_name='monster3', on_delete=models.CASCADE, null=True, blank= True)
    monsters4 = models.ForeignKey(Monster, related_name='monster4', on_delete=models.CASCADE, null=True, blank=True)
    monsters5 = models.ForeignKey(Monster, related_name='monster5', on_delete=models.CASCADE, null=True, blank=True)
    monsters6 = models.ForeignKey(Monster, related_name='monster6', on_delete=models.CASCADE, null=True, blank=True)

    description = models.TextField(blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'maps'

    def __str__(self):
        return self.name

class Character_Sheet(models.Model):
    race = models.ForeignKey(Race, related_name='character', on_delete=models.CASCADE)
    skill_class = models.ForeignKey(Skill_Class, related_name='character', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    character_name = models.CharField(max_length=255, blank=True, null=True)
    lvl = models.IntegerField(null=True)
    inspiration = models.IntegerField(null=True, blank=True)
    proficiency = models.IntegerField(null=True, blank=True)
    personality_traits = models.TextField(blank=True, null=True)
    ideals = models.TextField(blank=True, null=True)
    bonds = models.TextField(blank=True, null=True)
    flaws = models.TextField(blank=True, null=True)
    hp = models.IntegerField(null=True,)
    str = models.IntegerField(null=True,)
    dex = models.IntegerField(null=True,)
    con = models.IntegerField(null=True,)
    int = models.IntegerField(null=True,)
    wis = models.IntegerField(null=True,)
    cha = models.IntegerField(null=True,)
    ac = models.IntegerField(null=True,)
    speed = models.CharField(max_length=255, blank=True, null=True)
    equipment = models.TextField(blank=True, null=True)
    weapon = models.ForeignKey(Weapon, related_name='weapon', on_delete=models.CASCADE, blank=True, null=True)
    weapon_bonus = models.IntegerField(null=True, blank=True)
    weapon_2 = models.ForeignKey(Weapon, related_name='weapon2', on_delete=models.CASCADE, blank=True, null=True)
    weapon2_bonus = models.IntegerField(null=True, blank=True)
    weapon_3 = models.ForeignKey(Weapon, related_name='weapon3', on_delete=models.CASCADE, blank=True, null=True)
    weapon3_bonus = models.IntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='project_images', blank=True, null=True)
    image2 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image3 = models.ImageField(upload_to='project_images', blank=True, null=True)
    image4 = models.ImageField(upload_to='project_images', blank=True, null=True)
    invisible = models.BooleanField(default=False)
    proficient_skill = models.ForeignKey(Skill, related_name='skill', on_delete=models.CASCADE, blank=True, null=True)
    skill_2 = models.ForeignKey(Skill, related_name='skill2', on_delete=models.CASCADE, blank=True, null=True)
    skill_3 = models.ForeignKey(Skill, related_name='skill3', on_delete=models.CASCADE, blank=True, null=True)
    skill_4 = models.ForeignKey(Skill, related_name='skill4', on_delete=models.CASCADE, blank=True, null=True)
    skill_5 = models.ForeignKey(Skill, related_name='skill5', on_delete=models.CASCADE, blank=True, null=True)
    skill_6 = models.ForeignKey(Skill, related_name='skill6', on_delete=models.CASCADE, blank=True, null=True)
    skill_7 = models.ForeignKey(Skill, related_name='skill7', on_delete=models.CASCADE, blank=True, null=True)
    skill_8 = models.ForeignKey(Skill, related_name='skill8', on_delete=models.CASCADE, blank=True, null=True)

    spell = models.ForeignKey(Spell, related_name='spell', on_delete=models.CASCADE, blank=True, null=True)
    spell2 = models.ForeignKey(Spell, related_name='spell2', on_delete=models.CASCADE, blank=True, null=True)
    spell3 = models.ForeignKey(Spell, related_name='spell3', on_delete=models.CASCADE, blank=True, null=True)
    spell4 = models.ForeignKey(Spell, related_name='spell4', on_delete=models.CASCADE, blank=True, null=True)
    spell5 = models.ForeignKey(Spell, related_name='spell5', on_delete=models.CASCADE, blank=True, null=True)
    spell6 = models.ForeignKey(Spell, related_name='spell6', on_delete=models.CASCADE, blank=True, null=True)
    spell7 = models.ForeignKey(Spell, related_name='spell7', on_delete=models.CASCADE, blank=True, null=True)
    spell8 = models.ForeignKey(Spell, related_name='spell8', on_delete=models.CASCADE, blank=True, null=True)
    spell9 = models.ForeignKey(Spell, related_name='spell9', on_delete=models.CASCADE, blank=True, null=True)
    spell10 = models.ForeignKey(Spell, related_name='spell10', on_delete=models.CASCADE, blank=True, null=True)
    spell11 = models.ForeignKey(Spell, related_name='spell11', on_delete=models.CASCADE, blank=True, null=True)
    spell12 = models.ForeignKey(Spell, related_name='spell12', on_delete=models.CASCADE, blank=True, null=True)
    spell13 = models.ForeignKey(Spell, related_name='spell13', on_delete=models.CASCADE, blank=True, null=True)
    spell14 = models.ForeignKey(Spell, related_name='spell14', on_delete=models.CASCADE, blank=True, null=True)
    spell15 = models.ForeignKey(Spell, related_name='spell15', on_delete=models.CASCADE, blank=True, null=True)
    spell16 = models.ForeignKey(Spell, related_name='spell16', on_delete=models.CASCADE, blank=True, null=True)
    spell17 = models.ForeignKey(Spell, related_name='spell17', on_delete=models.CASCADE, blank=True, null=True)


    spell_link = models.URLField(max_length=200, blank=True, null=True)
    spell_link2 = models.URLField(max_length=200, blank=True, null=True)
    spell_link3 = models.URLField(max_length=200, blank=True, null=True)
    spell_link4 = models.URLField(max_length=200, blank=True, null=True)
    spell_link5 = models.URLField(max_length=200, blank=True, null=True)
    spell_link6 = models.URLField(max_length=200, blank=True, null=True)
    spell_link7 = models.URLField(max_length=200, blank=True, null=True)
    spell_link8 = models.URLField(max_length=200, blank=True, null=True)
    spell_link9 = models.URLField(max_length=200, blank=True, null=True)
    spell_link10 = models.URLField(max_length=200, blank=True, null=True)
    spell_link11 = models.URLField(max_length=200, blank=True, null=True)
    spell_link12 = models.URLField(max_length=200, blank=True, null=True)
    spell_link13 = models.URLField(max_length=200, blank=True, null=True)
    spell_link14 = models.URLField(max_length=200, blank=True, null=True)
    spell_link15 = models.URLField(max_length=200, blank=True, null=True)
    spell_link16 = models.URLField(max_length=200, blank=True, null=True)
    spell_link17 = models.URLField(max_length=200, blank=True, null=True)


    pictures = models.URLField(max_length=200, blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Character_Sheets'
    def __str__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.name

class Treasure(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=4088)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'treasures'
    def __str__(self):
        return self.name
