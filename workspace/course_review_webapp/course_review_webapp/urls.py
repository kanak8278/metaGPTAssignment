## urls.py
from django.urls import path
from course_review_webapp.views import (
    login_view,
    signup_view,
    logout_view,
    homepage_view,
    course_details_view,
    create_review_view,
    filter_courses_view,
    sort_courses_view,
)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('', homepage_view, name='homepage'),
    path('course/<int:course_id>/', course_details_view, name='course_details'),
    path('course/<int:course_id>/review/', create_review_view, name='create_review'),
    path('filter/', filter_courses_view, name='filter_courses'),
    path('sort/', sort_courses_view, name='sort_courses'),
]
