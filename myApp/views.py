from django.core.files.storage.filesystem import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.


from myApp.models import *
########## for Admin & Mentor

def login(request):
    return render(request , "indexlogin.html    ")

def login_post(request):
    user=request.POST['username']
    password = request.POST['password']
    obj = Login.objects.filter(username=user,password=password)

    if obj.exists():
        obj = Login.objects.get(username=user , password=password)
        request.session['lid']=obj.id
        if obj.type == 'admin':
            return  HttpResponse('''<script>alert("success");window.location='/myApp/adminHome/'</script>''')
        elif obj.type == 'mentor':
            return HttpResponse('''<script>alert("success");window.location='/myApp/MentorHomePage/'</script>''')
        else:
            return HttpResponse('''<script>alert(" user failed");window.location='/myApp/login/'</script>''')
    else:
        return HttpResponse('''<script>alert("login failed");window.location='/myApp/login/'</script>''')






############################################ admin functions  ########################################################

def adminHome(request):
    return render(request , "admin/adminIndex.html")


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
    res = Mentor.objects.filter(LOGIN = id).update(status  = 'approved')
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




###########################################    Mentor functions   #########################################################

def SignUp(request):
    return render(request , "Mentor/Sign Up.html")



def SignUp_Post(request):
    name = request.POST['textfield']
    dob = request.POST['textfield2']
    gender = request.POST['radio']
    city = request.POST['city']
    post = request.POST['post']
    district = request.POST['district']
    pin = request.POST['pin']
    state = request.POST['state']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    course = request.POST['textfield8']
    photo = request.FILES['Upload']
    password = request.POST['textfield9']
    confirmPassword = request.POST['textfield10']


    objLogin = Login()
    objLogin.username = email
    objLogin.password = password
    objLogin.type = 'pending'
    objLogin.save()


    if password == confirmPassword:
        objSignup = Mentor()
        objSignup.name = name
        objSignup.dob = dob
        objSignup.gender = gender
        objSignup.city = city
        objSignup.post = post
        objSignup.district = district
        objSignup.pincode = pin
        objSignup.state = state
        objSignup.phone = phone
        objSignup.email = email
        objSignup.course = course

        from datetime import datetime

        date  =  datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'

        fs  =  FileSystemStorage()
        fs.save(date , photo)
        path = fs.url(date)
        objSignup.photo = path



        objSignup.LOGIN = objLogin
        objSignup.status = 'pending'

        objSignup.save()

    return HttpResponse('''<script>alert("signUP success");window.location = '/myApp/login/'</script>''')





def ViewProfile(request):
    obj = Mentor.objects.get(LOGIN_id = request.session['lid'])
    return render(request , "Mentor/View Profile.html" , {'data' : obj})




def EditProfile(request):

    obj = Mentor.objects.get(LOGIN_id = request.session['lid'])

    return render(request , "Mentor/Edit profile.html" ,  {'data' : obj})



def EditProfile_Post(request):
    name = request.POST['textfield']
    dob = request.POST['textfield2']
    gender = request.POST['radio']
    city = request.POST['city']
    post = request.POST['post']
    district = request.POST['district']
    pin = request.POST['pin']
    state = request.POST['state']
    phone = request.POST['textfield6']
    email = request.POST['textfield7']
    course = request.POST['textfield8']
    id = request.POST['id']

    objSignup = Mentor.objects.get(id = id)

    if 'Upload' in request.FILES:
        photo = request.FILES['Upload']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        objSignup.photo = path

        objSignup.save()

    objSignup.name = name
    objSignup.dob = dob
    objSignup.gender = gender
    objSignup.city = city
    objSignup.post = post
    objSignup.district = district
    objSignup.pincode = pin
    objSignup.state = state
    objSignup.phone = phone
    objSignup.email = email
    objSignup.course = course

    objSignup.save()
    return HttpResponse('''<script>alert("successfully edited");window.location = '/myApp/ViewProfile/'</script>''')



def ViewMenteeRequest(request):
    var = Request_mentor.objects.filter(status = "pending")
    return render(request , "Mentor/View Mentor request.html" , {'data':var})


def ViewMenteeRequest_post(request):
    fromdate=request.POST['fromDate']
    todate=request.POST['toDate']
    var = Request_mentor.objects.filter(status = "pending",date__range=[fromdate,todate])
    return render(request , "Mentor/View Mentor request.html" , {'data':var})




def  ApproveUser(request, id):
    var = Request_mentor.objects.filter(pk =id).update(status = "approved")
    return HttpResponse('''<script>alert("approved");window.location = '/myApp/ViewMenteeRequest/'</script>''')



def  RejectUser(request, id):
    var = Request_mentor.objects.filter(pk =id).update(status = "rejected")
    return HttpResponse('''<script>alert("rejected");window.location = '/myApp/ViewMenteeRequest/'</script>''')



def AcceptedMentee(request):
    var = Request_mentor.objects.filter(MENTOR__LOGIN_id = request.session['lid'] , status = "approved")
    return render(request , "Mentor/AcceptedMentee.html" , {'data':var})



def AcceptedMentee_post(request):
    fromdate = request.POST['fromDate']
    todate = request.POST['toDate']
    var = Request_mentor.objects.filter(MENTOR__LOGIN_id = request.session['lid'] , status = "approved",date__range=[fromdate,todate])
    return render(request , "Mentor/AcceptedMentee.html" , {'data':var})


def RejectedMentee(request):
    var = Request_mentor.objects.filter(MENTOR__LOGIN_id = request.session['lid'] ,status ="rejected")
    return render(request , "Mentor/RejectedMentee.html" , {'data':var})


def RejectedMentee_post(request):
    fromdate = request.POST['fromDate']
    todate = request.POST['toDate']
    var = Request_mentor.objects.filter(MENTOR__LOGIN_id = request.session['lid'] ,status ="rejected",date__range=[fromdate,todate])
    return render(request , "Mentor/RejectedMentee.html" , {'data':var})






def  SendTips(request):

    return render(request , "Mentor/Send tips to accepted user.html")



def SendTips_post(request):
    tips=request.POST['textfield']
    obj = Tips()
    obj.content = tips
    from datetime import datetime
    obj.date= datetime.now().strftime('%Y-%m-%d')
    obj.MENTOR= Mentor.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("Added");window.location = '/myApp/MentorHomePage/'</script>''')





def  editTips(request,id):
    var=Tips.objects.get(id=id)

    return render(request , "Mentor/editTips.html",{'data':var})



def editTips_post(request):
    tips=request.POST['textfield']
    tid=request.POST['tid']
    obj = Tips.objects.get(id=tid)
    obj.content = tips
    from datetime import datetime
    obj.date= datetime.now().strftime('%Y-%m-%d')
    obj.MENTOR= Mentor.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("updated");window.location = '/myApp/viewSendTips/'</script>''')



def viewSendTips(request):
    obj = Tips.objects.filter(MENTOR__LOGIN_id=request.session["lid"])
    return render(request , "Mentor/view send tips .html",{"data":obj})

def viewSendTips_post(request):
    fromdate = request.POST['fromDate']
    todate = request.POST['toDate']
    obj = Tips.objects.filter(MENTOR__LOGIN_id=request.session["lid"],date__range=[fromdate,todate])
    return render(request , "Mentor/view send tips .html",{"data":obj})


def deleteTips(request,id):
    var=Tips.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location = '/myApp/viewSendTips/'</script>''')








def  ManageSessions(request,id):

    return render(request , "Mentor/ManageSession.html",{'id':id})

def  ManageSessions_post(request):
    fromTime=request.POST['textfield']
    toTime=request.POST['textfield2']
    title=request.POST['textfield4']
    user=request.POST['id']
    document=request.FILES['fileField']
    from datetime import datetime

    date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.pdf'

    fs = FileSystemStorage()
    fs.save(date, document)
    path = fs.url(date)
    obj=Session()
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.from_time=fromTime
    obj.to_time=toTime
    obj.title=title
    obj.document=path
    obj.USER_id=user
    obj.MENTOR= Mentor.objects.get(LOGIN=request.session['lid'])
    obj.save()
    return HttpResponse('''<script>alert("Added");window.location = '/myApp/MentorHomePage/'</script>''')

def ViewSession(request,id):
    var=Session.objects.filter(USER_id=id)
    return render(request, "Mentor/View Session.html",{'data':var})


def ViewSession_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    var=Session.objects.filter(date__range=[fromdate,todate])
    return render(request, "Mentor/View Session.html",{'data':var})

def deleteSession(request,id):
    var=Session.objects.get(id=id).delete()
    return HttpResponse('''<script>alert("deleted");window.location = '/myApp/AcceptedMentee/'</script>''')


def  EditSessions(request,id):
    res = Session.objects.get(id=id)

    return render(request , "Mentor/EditSession.html",{'data':res})

def  EditSessions_post(request):
    fromTime=request.POST['textfield']
    toTime=request.POST['textfield2']
    title=request.POST['textfield4']

    # user=request.POST['id']
    id=request.POST['id']
    obj=Session.objects.get(id=id)

    if 'fileField' in request.FILES:
        document=request.FILES['fileField']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.pdf'
        fs = FileSystemStorage()
        fs.save(date, document)
        path = fs.url(date)
        obj.document = path
        obj.save()

    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.from_time=fromTime
    obj.to_time=toTime
    obj.title=title
    obj.save()
    return HttpResponse('''<script>alert("Updated");window.location = '/myApp/AcceptedMentee/'</script>''')



def  SendComplaint(request):

    return render(request , "Mentor/Send complaint.html")


def  SendComplaint_post(request):
    complaint=request.POST['textfield']
    obj=Complaint()
    obj.complaint=complaint
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.reply="pending"
    obj.status="pending"
    obj.type="mentor"
    lobj=Mentor.objects.get(LOGIN=request.session['lid'])
    obj.LOGIN_id=lobj.LOGIN.id
    obj.save()
    return HttpResponse('''<script>alert("Sending");window.location = '/myApp/MentorHomePage/'</script>''')


def  ViewReply(request):
    var=Complaint.objects.filter(LOGIN=request.session['lid'])
    return render(request , "Mentor/View Reply.html",{'data':var})

def  ViewReply_post(request):
    fromdate = request.POST['textfield']
    todate = request.POST['textfield2']
    var=Complaint.objects.filter(LOGIN=request.session['lid'],date__range=[fromdate,todate])
    return render(request , "Mentor/View Reply.html",{'data':var})


def  ChangePasswordMentor(request):

    return render(request , "Mentor/Change Password Mentor.html")



def changePasswordMentor_Post(request):
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
            '''<script>alert("failed");window.location = '/myApp/ChangePasswordMentor/'</script>''')



def MentorHomePage(request):

    return render(request , "Mentor/MentorHomePage.html")




#################################################### user ############################################################





def and_login(request):
    user = request.POST['name']
    password = request.POST['password']
    obj = Login.objects.filter(username=user, password=password)

    if obj.exists():
        objj = Login.objects.get(username=user, password=password)

        if objj.type == 'user':
                return JsonResponse({'status':'ok',"type":objj.type,"lid":str(objj.id)})

        else:
            return JsonResponse({'status':'not ok'})

    else:
        return JsonResponse({'status': 'not ok'})



def and_signUp(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    photo = request.POST['photo']
    state = request.POST['state']
    district = request.POST['district']
    city = request.POST['city']
    print(city,"hiii")

    post = request.POST['post']
    print(post,"kkkkk")
    pincode = request.POST['pincode']
    phone = request.POST['phone']
    Currently_course = request.POST['currentlyCourse']
    email = request.POST['email']
    password = request.POST['password']
    confirmPassword = request.POST['confirm_password']

    import datetime
    import base64
    date = datetime.datetime.now().strftime("%Y%m%d%G%M%S")
    a = base64.b64decode(photo)
    fh = open("C:\\Users\\anini\PycharmProjects\\StudApp\media\\user\\" + date + ".jpg" , "wb")
    path = "/media/user/"+date+".jpg"
    fh.write(a)
    fh.close()




    obj = Login()
    obj.username = email
    obj.password = password
    obj.type = 'user'
    obj.save()

    uobj = User()
    uobj.name = name
    uobj.dob = dob
    uobj.gender  = gender
    uobj.photo = path
    uobj.state = state
    uobj.district = district
    uobj.city = city
    uobj.post = post
    uobj.pincode = pincode
    uobj.phone = phone
    uobj.Currently_course = Currently_course
    uobj.email = email
    uobj.LOGIN = obj
    uobj.save()

    return JsonResponse({'status':'ok'})




def and_viewProfile(request):
    lid=request.POST['lid']
    print(lid,"jjjj")
    var = User.objects.get(LOGIN_id = lid)

    return JsonResponse({
        'status':'ok',
        "name":var.name,
        "dob":var.dob,
        "gender":var.gender,
        "photo":var.photo,
        "state":var.state,
        "district":var.district,
        "city":var.city,
        "post":var.post,
        "pincode":var.pincode,
        "phone":var.phone,
        "Currently_course":var.Currently_course,
        "email":var.email

    })



def and_editProfile(request):
    name = request.POST['name']
    dob = request.POST['dob']
    gender = request.POST['gender']
    photo = request.POST['photo']
    state = request.POST['state']
    district = request.POST['district']
    city = request.POST['city']
    post = request.POST['post']
    pincode = request.POST['pin']
    phone = request.POST['phone']
    Currently_course = request.POST['Currently_course']
    email = request.POST['email']
    lid=request.POST['lid']

    if len(photo)>0:
        import datetime
        import base64
        date = datetime.datetime.now().strftime("%Y%m%d%G%M%S")
        a = base64.b64decode(photo)
        fh = open("C:\\Users\\anini\PycharmProjects\\StudApp\media\\user\\" + date + ".jpg", "wb")
        path = "/media/user/" + date + ".jpg"
        fh.write(a)
        fh.close()

        uobj = User.objects.get(LOGIN__id=lid)
        uobj.name = name
        uobj.dob = dob
        uobj.gender = gender
        uobj.photo = path
        uobj.state = state
        uobj.district = district
        uobj.city = city
        uobj.post = post
        uobj.pincode = pincode
        uobj.phone = phone
        uobj.Currently_course = Currently_course
        uobj.email = email
        uobj.save()
    uobj = User.objects.get(LOGIN__id=lid)
    uobj.name = name
    uobj.dob = dob
    uobj.gender = gender
    uobj.state = state
    uobj.district = district
    uobj.city = city
    uobj.post = post
    uobj.pincode = pincode
    uobj.phone = phone
    uobj.Currently_course = Currently_course
    uobj.email = email
    uobj.save()
    return JsonResponse({'status':'ok'})


def and_sendComplaint(request):
    complaint = request.POST['complaint']
    lid=request.POST['lid']

    obj = Complaint()
    obj.complaint = complaint
    obj.status = 'pending'
    obj.reply = 'pending'
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    lobj=User.objects.get(LOGIN_id=lid)
    obj.LOGIN_id=lobj.LOGIN.id
    obj.type = 'user'
    obj.save()
    return JsonResponse({'status':'ok'})

def and_viewReply(request):
    lid = request.POST['lid']
    var = Complaint.objects.filter(LOGIN_id = lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'date':i.date , 'complaint':i.complaint , 'reply':i.reply})
    return JsonResponse({'status':'ok','data':l})



def and_changePassword(request):
    old_password = request.POST['oldPassword']
    new_password = request.POST['newPassword']
    confirmNewPassword = request.POST['confirmPassword']
    lid=request.POST['lid']
    obj = Login.objects.filter(id=lid, password=old_password)
    if obj.exists():
        obj = Login.objects.get(id=lid, password=old_password)

        obj.password = new_password
        obj.save()
        return JsonResponse({'status':'ok'})
    else:
        return JsonResponse({'status':'not ok'})



def and_sendAppReview(request):
    lid = request.POST['lid']
    review = request.POST['review']
    rating = request.POST['rating']
    obj = App_reviews()
    obj.review = review
    obj.rating = rating
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.USER = User.objects.get(LOGIN_id = lid)
    obj.save()

    return JsonResponse({'status':'ok'})


def add_viewReview(request):
    res = App_reviews.objects.all()
    l = []
    for i in res:
        l.append({'id': i.id, 'date': i.date, 'review': i.review, 'rating': i.rating , 'user':i.USER.name})
    return JsonResponse({'status': 'ok', 'data': l})


def and_sendMentorReview(request):
    lid = request.POST['lid']
    review = request.POST['review']
    rating = request.POST['rating']
    mid = request.POST['mid']
    obj = Mentor_review()
    obj.review = review
    obj.rating = rating
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.USER = User.objects.get(LOGIN_id=lid)
    obj.MENTOR_id = mid
    obj.save()

    return JsonResponse({'status':'ok'})



def and_viewMentors(request):
    obj = Mentor.objects.filter(status = 'approved')
    l = []
    for i in obj:
        l.append({'id':i.id ,
                  'name':i.name ,
                  'photo':i.photo,
                  'course':i.course,


                  }
                 )
    return JsonResponse({'status':'ok','data':l})


def and_viewMentorDetail(request):
    mid=request.POST['mid']
    var = Mentor.objects.get(id=mid)
    return JsonResponse({
        'status': 'ok',
        "id": var.id,
        "name": var.name,
        "photo": var.photo,
        "phone": var.phone,
        "city":var.city,
        "Currently_course": var.course,
        'qualification': var.qualification,
        "email": var.email


    })



def and_sendRequest(request):
    lid=request.POST['lid']
    mid = request.POST['mid']
    obj=Request_mentor()
    from datetime import datetime
    obj.date = datetime.now().strftime('%Y-%m-%d')
    obj.status='pending'
    obj.USER = User.objects.get(LOGIN_id=lid)
    obj.MENTOR_id = mid
    obj.save()
    return JsonResponse({'status':'ok'})



def and_viewSession(request):
    mid = request.POST['mid']
    lid = request.POST['lid']
    print(mid)
    print(lid)
    obj=Session.objects.filter(MENTOR_id=mid,USER__LOGIN_id = lid)
    l=[]
    for i in obj:
        l.append({'id':i.id,
                  'date':i.date,
                  'from_time':i.from_time,
                  'to_time':i.to_time,
                  'title':i.title,
                  'document':i.document})
    return JsonResponse({'status':'ok' , 'data':l})


def and_viewRequestStatus(request):
    lid = request.POST['lid']
    obj = Request_mentor.objects.filter(USER__LOGIN_id = lid,)
    l = []
    for i in obj:
        l.append({'id': i.id,
                  'date': i.date,
                  'status': i.status,
                  'mentorName': i.MENTOR.name,
                  'mid': i.MENTOR.id,
                  })
    return JsonResponse({'status':'ok' , 'data':l})

def and_viewMyMentors(request):
    lid = request.POST['lid']
    obj = Request_mentor.objects.filter(USER__LOGIN_id = lid,status="approved")
    l = []
    for i in obj:
        l.append({'id': i.MENTOR.id,
                  'name': i.MENTOR.name,
                  'photo':i.MENTOR.photo,
                  'course':i.MENTOR.course,
                  })
    return JsonResponse({'status':'ok' , 'data':l})


























































