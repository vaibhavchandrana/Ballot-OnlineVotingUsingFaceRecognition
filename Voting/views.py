import profile
from tkinter import EXCEPTION
from unicodedata import name
from django.shortcuts import render, HttpResponse, redirect
import random
import cv2
import numpy as np
import face_recognition
import os
from django.contrib.auth.hashers import make_password,check_password
from .models import User,Candidate
from django.conf import settings


from Voting.models import User
# Create your views here.

def login(request):
    try:
        if request.method == 'POST':
            email=request.POST.get('email')
            password=request.POST.get('pass')
            user=User.get_user_by_email(email) # return object matching email
            if user:
                flag=check_password(password,user.password)
                if flag:
                    request.session['user'] = email
                    request.session['flag'] = 0
                    return redirect('index')
                else:
                    error="Invalid email or password !!! "
                    return render(request,'loader.html',{'error1':error})

            else:
                error="Invalid email or password !!! "
                return render(request,'loader.html',{'error1':error})
                    
    except Exception as e:
        print("Error While login", e)   
    return render(request, 'loader.html')

# view for registration page page 
def register(request):
    voter_id=random.randint(100000, 999999)
    
    try:
        if request.method =="POST":
            name=request.POST.get('name')
            email=request.POST.get('email')
            phone=request.POST.get('phone')
            age=request.POST.get('age')
            password=request.POST.get('pass')
            cpassword=request.POST.get('c_pass')
            vid=voter_id
            image=request.FILES.get('image')
            print(image)
            user=User(name=name,email=email,
                        phone=phone,password=password,
                        age=age,voter_id=vid,profile=image,flag=0)
            user.password=make_password(user.password)
           
            isExist=User.isExists(email)
        
            if isExist:
                return redirect('login')

            user.register()
            return redirect('login')
                    
    except Exception as e:
        print("eroor", e)
    return render(request, 'registration.html')

# view for home page 
def index(request):
    if request.session['user']:
        return render(request, 'index.html')
    else:
        return redirect('/')

# view for voting  page 
def voting(request):
    if request.method=="GET":
        candidates=Candidate.get_all_candidates()
        return render(request, 'voting.html',{'cand':candidates})
    else:
        try:
            if request.session['user']:
                face=face_recognition_fun()
                if face==True:
                    print(request.session['user'])
                    if request.method == "POST":
                        cd1 = request.POST.get('candidate_id')
                        user1=request.session['user']
                        voter=User.get_user_by_email(user1)
                        u_id=voter.id
                        if voter.flag==0:
                            candi=Candidate.get_candidate_by_cnd_id(cd1)
                            vote=candi[0].votes +1
                            candi.update(votes=vote)

                            myuser=User.get_user_by_id(u_id)
                            flag1=myuser[0].flag +1
                            myuser.update(flag=flag1)
                                   
                    candidates=Candidate.get_all_candidates()
                    return render(request, 'voting.html',{'cand':candidates})
                else:
                    return redirect('/')
            else:
                return redirect('/')
        except Exception as e:
            print("error",e)
        
# view for logout page 
def logout(request):
    del request.session['user']
    return redirect('/')
        

def face_recognition_fun():
    path = settings.MEDIA_ROOT
    images = []
    classNames = []
    myList = os.listdir(path) 
    print(myList)  
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode =face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
            return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    while True:
        name=""
        success,img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            if len(myList):
                matchIndex = np.argmin(faceDis)
                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
        cv2.imshow('Webcam', img)
        cv2.waitKey(1) 
        if(len(name)):
            flag=True
            break
        else:
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                flag=False
                break
    return flag

# view for face recognition page 
def authorization(request):
    flag=face_recognition_fun()
    if flag==False:         
        return redirect('signup')
    else:  
        return render(request, 'authorization.html')
# view for result  page 
def result(request):
    fv = Candidate.get_all_candidates()
    context = {
        'fav' : fv
    }
    print(fv)
    return render(request, 'result.html',context)

# view for profile page 
def profile(request):
    
    if request.session['user']:
        user1=request.session['user']
        
        fv=User.get_user_by_email(user1)
        
        
        context = {
        'fav' : fv
        }
    return render(request,"main.html",context)

    #project finished