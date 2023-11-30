from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

###################### admin functions#################################
from myApp.models import *


def login(request):
    return render(request , "Login.html")

def login_post(request):
    user=request.POST['username']
    password = request.POST['password']
    obj = Login.objects.filter(username=user,password=password)

    if obj.exists():
        obj = Login.objects.get(username=user , password=password)
        request.session['lid']=obj.id
        if obj.type == 'admin':
            return  HttpResponse('''<script>alert("success");window.location='/myApp/adminHome/'</script>''')
        else:
            return HttpResponse('''<script>alert(" user failed");window.location='/myApp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("login failed");window.location='/myApp/login/'</script>''')








def adminHome(request):
    return render(request , "admin/home.html")






def changePassword(request):
    return render(request , "admin/Change Password.html")

def changePassword_post(request):
    old_password = request.POST['oldPassword']
    new_password = request.POST['newPassword']
    confirmNewPassword = request.POST['confirmPassword']
    obj = Login.objects.filter(id=request.session['lid'],password = old_password)
    if obj.exists():
        obj = Login.objects.get(id=request.session['lid'], password=old_password)

        obj.password=new_password
        obj.save()
        return HttpResponse(
            '''<script>alert("password changed successfully");window.location = '/myApp/login/'</script>''')

    else:
        return HttpResponse(
            '''<script>alert("failed");window.location = '/myApp/changePassword /'</script>''')


def viewAndVerifyMentors(request):
    res = Mentor.objects.filter(status = 'pending')
    return render(request , "admin/View and verify mentors.html" , {'data' :res})

def viewAndVerifyMentors_post(request):
    search = request.POST['search']
    res = Mentor.objects.filter(status = 'pending' ,name__icontains = search )
    return render(request , "admin/View and verify mentors.html" , {'data':res})



def ApproveMentor_post(request , id):
    res = Mentor.objects.filter(LOGIN_id = id).update(status  = 'approved')
    obj = Login.objects.filter(id = id).update(type = 'mentor')

    return HttpResponse('''<script>alert("approved successfully");window.location = '/myApp/viewAndVerifyMentors/'</script>''')


def RejectMentor_post(request , id):
    res = Mentor.objects.filter(LOGIN_id = id).update(status = 'rejected')
    obj = Login.objects.filter(id = id).update(type  = 'blocked')
    return HttpResponse('''<script>alert("rejected successfully");window.location = '/myApp/viewAndVerifyMentors/'</script>''')




def ApprovedMentors(request):
    res = Mentor.objects.filter(status='approved')
    return render(request , "admin/View Approved mentors.html" , {'data':res})


def ApprovedMentors_post(request):
    search = request.POST['Search']
    res = Mentor.objects.filter(status='approved', name__icontains=search)
    return render(request, "admin/View Approved mentors.html", {'data': res})







def RejectedMentors(request):
    res = Mentor.objects.filter(status='rejected')
    return render(request , "admin/View Rejected mentors.html" , {'data' :res})


def RejectedMentors_post(request):
    search = request.POST['search']
    res = Mentor.objects.filter(status='rejected', name__icontains=search)
    return render(request, "admin/View Rejected mentors.html" , {'data':res})




def viewComplaints(request):
    res = Complaint.objects.all()
    return render(request , "admin/View Complaint.html" , {'data':res})

def viewComplaints_post(request):
    fromDate = request.POST['fromDate']
    toDate = request.POST['toDate']
    res = Complaint.objects.filter(date__range=[fromDate,toDate])
    return render(request, "admin/View Complaint.html" , {'data' : res})



def sendReply(request,id):
    return render(request , "admin/Send Reply.html",{'id':id})



def sendReply_post(request,id):
    sendReply = request.POST['sendReply']
    Complaint.objects.filter(id = id).update(reply = sendReply , status = 'send')
    return HttpResponse('''<script>alert("reply given");window.location = '/myApp/viewComplaints/'</script>''')




def viewMentorReview(request):
    res = Mentor_review.objects.all()

    return render(request , "admin/View reviews about mentor.html" , {'data':res})

def viewMentorReview_post(request):
    fromDate = request.POST['fromDate']
    toDate = request.POST['toDate']
    res = Mentor_review.objects.filter(date__range=[fromDate, toDate])
    return render(request, "admin/View reviews about mentor.html" , {'data':res})




def viewAppRating(request):
    res  = App_reviews.objects.all()

    return render(request , "admin/View application reviews and ratings.html" , {'data':res})

def viewAppRating_post(request):
    fromDate = request.POST['fromDate']
    toDate = request.POST['toDate']
    res = App_reviews.objects.filter(date__range=[fromDate, toDate])
    return render(request, "admin/View application reviews and ratings.html" , {'data':res})




def viewUsers(request):
    res = User.objects.all()
    return render(request , "admin/View Users.html" , {'data' : res})

def viewUsers_post(request):
    username = request.POST['usrch']
    search = User.objects.filter(name__icontains = username)
    return render(request, "admin/View Users.html" , {'data':search})




#####################Mentor functions############################













