from django.db import models

class FarmVisit(models.Model):
    # Farmer Details
    farmer_name = models.CharField(max_length=100)
    farm_id = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    gps_coordinates = models.CharField(max_length=100, blank=True)
    farm_size = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Farm Type Choices
    FARM_TYPE_CHOICES = [
        ('Crop', 'Crop'),
        ('Livestock', 'Livestock'),
        ('Mixed', 'Mixed'),
    ]
    farm_type = models.CharField(max_length=20, choices=FARM_TYPE_CHOICES)
    
    # Visit Details
    visit_date = models.DateField()
    VISIT_TYPE_CHOICES = [
        ('Routine', 'Routine'),
        ('Emergency', 'Emergency'),
        ('Follow-up', 'Follow-up'),
    ]
    visit_type = models.CharField(max_length=20, choices=VISIT_TYPE_CHOICES)
    officer_name = models.CharField(max_length=100)
    time_spent = models.DecimalField(max_digits=4, decimal_places=1)
    
    # Observations - Crops
    main_crops = models.CharField(max_length=200, blank=True)
    CROP_STAGE_CHOICES = [
        ('Planting', 'Planting'),
        ('Vegetative', 'Vegetative'),
        ('Flowering', 'Flowering'),
        ('Fruiting', 'Fruiting'),
        ('Harvesting', 'Harvesting'),
    ]
    crop_stage = models.CharField(max_length=20, choices=CROP_STAGE_CHOICES, blank=True)
    
    # Crop Issues (stored as comma-separated values)
    crop_issues = models.CharField(max_length=200, blank=True)
    
    # Observations - Livestock
    livestock_type = models.CharField(max_length=100, blank=True)
    animal_count = models.IntegerField(null=True, blank=True)
    
    # Livestock Issues (stored as comma-separated values)
    livestock_issues = models.CharField(max_length=200, blank=True)
    
    # Recommendations
    advice = models.TextField(blank=True)
    # Change this field to handle multiple images
    photos = models.ImageField(upload_to='farm_photos/', blank=True, null=True)
    
    # Add this new field for multiple images
    additional_photos = models.ManyToManyField('FarmPhoto', blank=True, related_name='visits')
    
    # Follow-Up
    follow_up_needed = models.BooleanField(default=False)
    follow_up_date = models.DateField(null=True, blank=True)
    training_needed = models.BooleanField(default=False)
    referral_needed = models.BooleanField(default=False)
    follow_up_notes = models.TextField(blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Visit to {self.farmer_name}'s farm on {self.visit_date}"

class FarmPhoto(models.Model):
    image = models.ImageField(upload_to='farm_photos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Photo {self.id} - {self.uploaded_at.strftime('%Y-%m-%d')}"
