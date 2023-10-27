from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=10)
    type = models.CharField(max_length=10)

class Mentor(models.Model):
    LOGIN = models.ForeignKey(Login , on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)
    dob = models.DateField()
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

class User(models.Model):
    LOGIN = models.ForeignKey(Login , on_delete = models.CASCADE)
    name = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    photo = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    Currently_course = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Complaint(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.DateField()
    complaint = models.CharField(max_length=200)
    reply = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    type =  models.CharField(max_length=50)


class App_reviews(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)
    date = models.DateField()

class Mentor_review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    MENTOR =  models.ForeignKey(Mentor, on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    rating = models.CharField(max_length=50)
    date = models.DateField()

class Tips(models.Model):
    date = models.DateField()
    content = models.CharField(max_length=200)
    MENTOR = models.ForeignKey(Mentor, on_delete=models.CASCADE)


class Chat(models.Model):
    FROM_ID= models.ForeignKey(Login, on_delete=models.CASCADE,related_name='fromid')
    TO_ID = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='toid')
    message = models.CharField(max_length=200)
    date = models.DateField()



class Session(models.Model):
    date = models.DateField()
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    from_date = models.DateField()
    to_date = models.DateField()
    title = models.CharField(max_length=100)
    document = models.CharField(max_length=100)
    MENTOR = models.ForeignKey(Mentor, on_delete=models.CASCADE)

class Request(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    MENTOR = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateField()
    SESSION = models.ForeignKey(Session, on_delete=models.CASCADE)


class Questions(models.Model):
    SESSION = models.ForeignKey(Session, on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)

class Content(models.Model):
    date = models.DateField()
    MENTOR = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    USER = models.ForeignKey(User, on_delete=models.CASCADE)






















