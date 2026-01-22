from django.db import models

class AssessmentResult(models.Model):
    # user demographics
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    scenario_used = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    scores = models.JSONField(default=dict) 
    overall_score = models.FloatField(default=0.0)
    rating = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.row_id} - {self.profession} ({self.created_at.strftime('%Y-%m-%d')})"
