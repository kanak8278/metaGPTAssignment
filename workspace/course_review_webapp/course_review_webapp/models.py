## models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    average_rating = models.FloatField(default=0)

    def get_average_rating(self):
        reviews = self.reviews.all()
        if reviews:
            total_rating = sum(review.rating for review in reviews)
            return total_rating / len(reviews)
        else:
            return 0

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField()
    comments = models.TextField()

    def create_review(self):
        self.save()

class Search(models.Model):
    query = models.CharField(max_length=100)

    def search_courses(self):
        return Course.objects.filter(title__icontains=self.query)

class Filter(models.Model):
    rating = models.IntegerField()

    def filter_courses(self):
        return Course.objects.filter(average_rating__gte=self.rating)

class Sort(models.Model):
    sort_by = models.CharField(max_length=100)

    def sort_courses(self):
        if self.sort_by == 'rating':
            return Course.objects.order_by('-average_rating')
        elif self.sort_by == 'reviews':
            return Course.objects.order_by('-reviews__count')
        else:
            return Course.objects.all()
