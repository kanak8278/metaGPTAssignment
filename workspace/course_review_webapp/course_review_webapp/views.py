from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from course_review_webapp.models import Course, Review

@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

@login_required
def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        user = User.objects.create_user(username=username, password=password, email=email)
        login(request, user)
        return redirect('homepage')
    else:
        return render(request, 'signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def homepage_view(request):
    courses = Course.objects.all()
    return render(request, 'index.html', {'courses': courses})

@login_required
def course_details_view(request, course_id):
    course = Course.objects.get(id=course_id)
    reviews = Review.objects.filter(course=course)
    return render(request, 'course_details.html', {'course': course, 'reviews': reviews})

@login_required
def create_review_view(request, course_id):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comments = request.POST.get('comments')
        course = Course.objects.get(id=course_id)
        review = Review(user=request.user, course=course, rating=rating, comments=comments)
        review.save()
        return redirect('course_details', course_id=course_id)
    else:
        return redirect('course_details', course_id=course_id)

@login_required
def filter_courses_view(request):
    if request.method == 'POST':
        rating = request.POST.get('rating')
        courses = Course.objects.filter(average_rating__gte=rating)
        return render(request, 'index.html', {'courses': courses})
    else:
        return redirect('homepage')

@login_required
def sort_courses_view(request):
    if request.method == 'POST':
        sort_by = request.POST.get('sort_by')
        if sort_by == 'rating':
            courses = Course.objects.order_by('-average_rating')
        elif sort_by == 'reviews':
            courses = Course.objects.order_by('-reviews__count')
        else:
            courses = Course.objects.all()
        return render(request, 'index.html', {'courses': courses})
    else:
        return redirect('homepage')
