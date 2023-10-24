
from django.contrib import admin
from django.urls import path, include

from myApp import views

urlpatterns = [
    path("login/" , views.login),
    path("changePassword/" , views.changePassword),
    path("viewAndVerifyMentors/" , views.viewAndVerifyMentors),
    path("viewComplaints/" , views.viewComplaints),
    path("sendReply/" , views.sendReply),
    path("ApprovedMentors/" , views.ApprovedMentors),
    path("RejectedMentors/" , views.RejectedMentors),
    path("viewMentorReview/" , views.viewMentorReview),
    path("viewAppRating/" , views.viewAppRating),
    path("viewUsers/" , views.viewUsers),
]
