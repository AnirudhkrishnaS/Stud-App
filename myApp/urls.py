
from django.contrib import admin
from django.urls import path, include

from myApp import views

urlpatterns = [
    path("login/", views.login),
    path("login_post/" , views.login_post),
    path("changePassword/" , views.changePassword),
    path("changePassword_post/" , views.changePassword_post),
    path("viewAndVerifyMentors/" , views.viewAndVerifyMentors),
    path("viewAndVerifyMentors_post/" , views.viewAndVerifyMentors_post),
    path("viewComplaints/" , views.viewComplaints),
    path("viewComplaints_post/" , views.viewComplaints_post),
    path("sendReply/<id>" , views.sendReply),
    path("sendReply_post/<id>" , views.sendReply_post),
    path("ApproveMentor_post/<id>" , views.ApproveMentor_post),
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



#####################################################  Mentor  ##################################################################
    path("SignUp/", views.SignUp),
    path("SignUp_Post/", views.SignUp_Post),
    path("ViewProfile/", views.ViewProfile),
    path("EditProfile/", views.EditProfile),
    path("ViewMenteeRequest/", views.ViewMenteeRequest),
    path("ApproveUser/<id>", views.ApproveUser),
    path("RejectUser/<id>", views.RejectUser),
    path("AcceptedMentee/", views.AcceptedMentee),
    path("RejectedMentee/", views.RejectedMentee),
    path("SendTips/", views.SendTips),
    path("SendTips_post/", views.SendTips_post),
    path("viewSendTips/", views.viewSendTips),
    path("ManageSessions/<id>", views.ManageSessions),
    path("SendComplaint/", views.SendComplaint),
    path("ViewReply/", views.ViewReply),
    path("ChangePasswordMentor/", views.ChangePasswordMentor),
    path("MentorHomePage/", views.MentorHomePage),
    path("EditProfile_Post/", views.EditProfile_Post),
    path("changePasswordMentor_Post/", views.changePasswordMentor_Post),
    path("editTips_post/", views.editTips_post),
    path("deleteTips/<id>", views.deleteTips),
    path("editTips/<id>", views.editTips),
    path("ManageSessions_post/", views.ManageSessions_post),
    path("ViewSession/<id>", views.ViewSession),
    path("deleteSession/<id>", views.deleteSession),
    path("EditSessions/<id>", views.EditSessions),
    path("EditSessions_post/", views.EditSessions_post),
    path("SendComplaint_post/", views.SendComplaint_post),
    path("ViewMenteeRequest_post/", views.ViewMenteeRequest_post),
    path("AcceptedMentee_post/", views.AcceptedMentee_post),
    path("RejectedMentee_post/", views.RejectedMentee_post),
    path("ViewReply_post/", views.ViewReply_post),
    path("viewSendTips_post/", views.viewSendTips_post),
    path("ViewSession_post/", views.ViewSession_post),

    path('chat/<id>',views.chat),
    path('chat_view/',views.chat_view),
    path('chat_send/<msg>',views.chat_send),



    ###########################################user##################################################

    path('and_login/',views.and_login),
    path('and_signUp/',views.and_signUp),
    path('and_viewProfile/',views.and_viewProfile),
    path('and_editProfile/',views.and_editProfile),
    path('and_sendComplaint/',views.and_sendComplaint),
    path('and_viewReply/',views.and_viewReply),
    path('and_changePassword/',views.and_changePassword),
    path('and_sendAppReview/',views.and_sendAppReview),
    path('add_viewReview/',views.add_viewReview),
    path('and_sendMentorReview/',views.and_sendMentorReview),
    path('and_viewMentors/',views.and_viewMentors),
    path('and_viewMyMentors/',views.and_viewMyMentors),
    path('and_viewMentorDetail/',views.and_viewMentorDetail),
    path('and_sendRequest/',views.and_sendRequest),
    path('and_viewSession/',views.and_viewSession),
    path('and_viewRequestStatus/',views.and_viewRequestStatus),
    path('user_view_chat/', views.user_view_chat),
    path('user_send_chat/', views.user_send_chat),









]
