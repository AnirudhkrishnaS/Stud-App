
from django.contrib import admin
from django.urls import path, include

from myApp import views

urlpatterns = [
    path("login/" , views.login),
    path("login_post/" , views.login_post),
    path("changePassword/" , views.changePassword),
    path("changePassword_post/" , views.changePassword_post),
    path("viewAndVerifyMentors/" , views.viewAndVerifyMentors),
    path("viewAndVerifyMentors_post/" , views.viewAndVerifyMentors_post),
    path("viewComplaints/" , views.viewComplaints),
    path("viewComplaints_post/" , views.viewComplaints_post),
    path("sendReply/<id>" , views.sendReply),
    path("sendReply_post/<id>" , views.sendReply_post),
    path("ApprovedMentors_post/" , views.ApprovedMentors_post),
    path("RejectedMentors/" , views.RejectedMentors),
    path("RejectedMentors_post/" , views.RejectedMentors_post),
    path("ApprovedMentors/" , views.ApprovedMentors),
    path("viewMentorReview/" , views.viewMentorReview),
    path("viewMentorReview_post/" , views.viewMentorReview_post),
    path("adminHome/" , views.adminHome),

    path("viewAppRating/", views.viewAppRating),
    path("viewAppRating_post/", views.viewAppRating_post),

    path("viewUsers/" , views.viewUsers),
    path("viewUsers_post/" , views.viewUsers_post),
    path("RejectMentor_post/<id>", views.RejectMentor_post),

]
