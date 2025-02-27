from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class YourModel(models.Model):
    # Define your model fields here
    name = models.CharField(max_length=100)
    # other fields...

    def __str__(self):
        return self.name

class FieldData(models.Model):
    studyYear = models.IntegerField(blank=True, null=True)
    programDbId = models.CharField(max_length=255, blank=True, null=True)
    programName = models.CharField(max_length=255, blank=True, null=True)
    programDescription = models.TextField(blank=True, null=True)
    studyDbId = models.CharField(max_length=255, blank=True, null=True)
    studyName = models.CharField(max_length=255, blank=True, null=True)
    studyDescription = models.TextField(blank=True, null=True)
    studyDesign = models.CharField(max_length=255, blank=True, null=True)
    plotWidth = models.FloatField(blank=True, null=True)
    plotLength = models.FloatField(blank=True, null=True)
    fieldSize = models.FloatField(blank=True, null=True)
    plantingDate = models.DateField(blank=True, null=True)
    harvestDate = models.DateField(blank=True, null=True)
    locationDbId = models.CharField(max_length=255, blank=True, null=True)
    locationName = models.CharField(max_length=255, blank=True, null=True)
    germplasmDbId = models.CharField(max_length=255, blank=True, null=True)
    germplasmName = models.CharField(max_length=255, blank=True, null=True)
    germplasmSynonyms = models.CharField(max_length=255, blank=True, null=True)
    observationLevel = models.CharField(max_length=255, blank=True, null=True)
    observationUnitDbId = models.CharField(max_length=255, blank=True, null=True)
    observationUnitName = models.CharField(max_length=255, blank=True, null=True)
    replicate = models.IntegerField(blank=True, null=True)
    blockNumber = models.IntegerField(blank=True, null=True)
    plotNumber = models.IntegerField(blank=True, null=True)
    entryType = models.CharField(max_length=255, blank=True, null=True)
    boiled_storage_root_color = models.CharField(max_length=255, blank=True, null=True)
    cassava_anthractnose_disease_incidence_6_month = models.FloatField(blank=True, null=True)
    cassava_anthractnose_disease_incidence_9_month = models.FloatField(blank=True, null=True)
    cassava_anthractnose_disease_severity_6_month = models.FloatField(blank=True, null=True)
    cassava_anthractnose_disease_severity_9_month = models.FloatField(blank=True, null=True)
    cassava_bacterial_blight_incidence_3_month = models.FloatField(blank=True, null=True)
    cassava_bacterial_blight_incidence_6_month = models.FloatField(blank=True, null=True)
    cassava_bacterial_blight_severity_3_month = models.FloatField(blank=True, null=True)
    cassava_bacterial_blight_severity_6_month = models.FloatField(blank=True, null=True)
    cassava_green_mite_severity_first_evaluation = models.FloatField(blank=True, null=True)
    cassava_green_mite_severity_second_evaluation = models.FloatField(blank=True, null=True)
    cassava_mosaic_disease_incidence_1_month = models.FloatField(blank=True, null=True)
    cassava_mosaic_disease_incidence_3_month = models.FloatField(blank=True, null=True)
    cassava_mosaic_disease_incidence_6_month = models.FloatField(blank=True, null=True)
    cassava_mosaic_disease_severity_1_month = models.FloatField(blank=True, null=True)
    cassava_mosaic_disease_severity_3_month = models.FloatField(blank=True, null=True)
    cassava_mosaic_disease_severity_6_month = models.FloatField(blank=True, null=True)
    dry_matter_content_specific_gravity_method = models.FloatField(blank=True, null=True)
    dry_matter_content_percentage = models.FloatField(blank=True, null=True)
    ease_of_peeling_root_cortex_visual_rating = models.IntegerField(blank=True, null=True)
    first_apical_branch_height_cm = models.FloatField(blank=True, null=True)
    fresh_shoot_weight_kg_per_plot = models.FloatField(blank=True, null=True)
    fresh_storage_root_weight_per_plot = models.FloatField(blank=True, null=True)
    harvest_index_variable = models.FloatField(blank=True, null=True)
    initial_vigor_assessment = models.IntegerField(blank=True, null=True)
    number_of_planted_stakes_per_plot = models.IntegerField(blank=True, null=True)
    plant_architecture_visual_rating = models.IntegerField(blank=True, null=True)
    plant_stands_harvested_counting = models.IntegerField(blank=True, null=True)
    poundability_assessment = models.IntegerField(blank=True, null=True)
    proportion_lodged_plants_percentage = models.FloatField(blank=True, null=True)
    root_neck_length_visual_rating = models.IntegerField(blank=True, null=True)
    root_number_counting = models.IntegerField(blank=True, null=True)
    rotted_storage_root_counting = models.IntegerField(blank=True, null=True)
    specific_gravity = models.FloatField(blank=True, null=True)
    sprout_count_nine_month = models.IntegerField(blank=True, null=True)
    sprout_count_one_month = models.IntegerField(blank=True, null=True)
    sprout_count_six_month = models.IntegerField(blank=True, null=True)
    sprout_count_three_month = models.IntegerField(blank=True, null=True)
    sprouting_proportion = models.FloatField(blank=True, null=True)
    storage_root_cortex_color_visual_rating = models.IntegerField(blank=True, null=True)
    storage_root_periderm_color_visual_rating = models.IntegerField(blank=True, null=True)
    storage_root_pulp_color_visual_rating = models.IntegerField(blank=True, null=True)
    storage_root_shape_visual_rating = models.IntegerField(blank=True, null=True)
    storage_root_size_visual_rating = models.IntegerField(blank=True, null=True)
    taste_of_boiled_root_rating = models.IntegerField(blank=True, null=True)
    top_yield = models.FloatField(blank=True, null=True)
    total_carotenoid_chart_1_8 = models.FloatField(blank=True, null=True)
    total_carotenoid_iCheck_method = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.programName} - {self.studyName}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=30, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()