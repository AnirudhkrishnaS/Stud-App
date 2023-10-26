from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

###################### admin functions#################################
def login(request):
    return render(request , "Login.html")

def login_post(request):
    user=request.POST['username']
    password = request.POST['password']
    confirmNewPassword = request.POST['confirmPassword']
    return HttpResponse('''<script>alert("Login successfully");window.location='/myApp/login/'</script>''')


def adminHome(request):
    return render(request , "admin/home.html")






def changePassword(request):
    return render(request , "admin/Change Password.html")

def changePassword_post(request):
    old_password = request.POST['oldPassword']
    new_password = request.POST['newPassword']
    return HttpResponse('''<script>alert("password changed successfully");window.location = '/myApp/changePassword /'</script>''')


def viewAndVerifyMentors(request):
    return render(request , "admin/View and verify mentors.html")

def viewAndVerifyMentors_post(request):
    search = request.POST['search']
    return render(request , "admin/View and verify mentors.html")


def ApprovedMentors(request):
    return render(request , "admin/View Approved mentors.html")


def ApprovedMentors_post(request):
    search = request.POST['Search']
    return render(request , "admin/View Approved mentors.html")






def RejectedMentors(request):
    return render(request , "admin/View Rejected mentors.html")

def RejectedMentors_post(request):
    search = request.POST['search']
    return render(request, "admin/View Rejected mentors.html")




def viewComplaints(request):
    return render(request , "admin/View Complaint.html")

def viewComplaints_post(request):
    fromDate = request.POST['fromDate']
    toDate = request.POST['toDate']
    return render(request, "admin/View Complaint.html")



def sendReply(request):
    return render(request , "admin/Send Reply.html")

def sendReply_post(request):
    sendReply = request.POST['sendReply']
    return HttpResponse('''<script>alert("reply given");window.location = '/myApp/sendReply/'</script>''')




def viewMentorReview(request):
    return render(request , "admin/View reviews about mentor.html")

def viewMentorReview_post(request):
    fromDate = request.POST['fromDate']
    toDate = request.POST['toDate']
    return render(request, "admin/View reviews about mentor.html")




def viewAppRating(request):
    return render(request , "admin/View application reviews and ratings.html")

def viewAppRating_post(request):
    fromDate = request.POST['fromDate']
    toDate = request.POST['toDate']
    return render(request, "admin/View application reviews and ratings.html")




def viewUsers(request):
    return render(request , "admin/View Users.html")

def viewUsers_post(request):
    username = request.POST['username']
    return render(request, "admin/View Users.html")




#####################Mentor functions############################













