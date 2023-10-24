from django.shortcuts import render

# Create your views here.

###################### admin functions#################################
def login(request):
    return render(request , "Login.html")


def changePassword(request):
    return render(request , "admin/Change Password.html")


def viewAndVerifyMentors(request):
    return render(request , "admin/View and verify mentors.html")



def ApprovedMentors(request):
    return render(request , "admin/View Approved mentors.html")


def RejectedMentors(request):
    return render(request , "admin/View Rejected mentors.html")




def viewComplaints(request):
    return render(request , "admin/View Complaint.html")


def sendReply(request):
    return render(request , "admin/Send Reply.html")



def viewMentorReview(request):
    return render(request , "admin/View reviews about mentor.html")




def viewAppRating(request):
    return render(request , "admin/View application reviews and ratings.html")


def viewUsers(request):
    return render(request , "admin/View Users.html")



#####################Mentor functions############################













