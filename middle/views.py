from django.shortcuts import render, redirect
from .models import Users,Apply,Video
import requests
from django.views.decorators.csrf import csrf_exempt
from .form import VideoForm
import os
from . import videoporcessing

from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request,'middle/main.html')



def login(request):

    nickname=request.session.get('nickname')

    context={
        'nickname':nickname
    }
    ##
    #
    #
    if request.method == 'POST':
        new_user = Users.objects.create(
            u_name=str(nickname),
            u_school=request.POST['school'],
            u_major=request.POST['major'],
            u_interest=request.POST['interest']
        )
        print("새로운 유저 "+nickname)
        return render(request, 'middle/apply.html')

    return  render(request, 'middle/login.html',context)



def apply(request):

    nickname = request.session.get('nickname')

    #자기소개서 관련 항목들이 들어오면 Apply에 저장함!
    if request.method == 'POST':
        new_apply=Apply.objects.create(
            a_company=request.POST['company'],
            a_interset=request.POST['interest'],
            a_qone=request.POST['q_one'],
            a_qtwo=request.POST['q_two'],
        )
        return redirect('/testing/')
    #'a_nowusers','a_company', 'a_interest','a_qone_q', 'a_qone', 'a_qtwo_q','a_qtwo', 'a_qthree_q','a_qthree', 'a_qfour_q' ,'a_four', 'a_qfive_q','a_five'
    return render(request,'middle/apply.html')

def tologin(request):


    if request.method == 'GET':

        login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'

        client_id = '1c9a05af3aaca8efed4d2cda193f0401'
        redirect_uri = 'http://127.0.0.1:8000/oauth'

        login_request_uri += 'client_id=' + client_id
        login_request_uri += '&redirect_uri=' + redirect_uri
        login_request_uri += '&response_type=code'

        request.session['client_id'] = client_id
        request.session['redirect_uri'] = redirect_uri

        return redirect(login_request_uri)


def oauth(request):

    code=request.GET['code']
    print('code= '+str(code))

    client_id = request.session.get('client_id')
    redirect_uri = request.session.get('redirect_uri')
    access_token_request_uri = "https://kauth.kakao.com/oauth/token?grant_type=authorization_code&"

    ##access token 을 얻는다.
    access_token_request_uri += "client_id=" + client_id
    access_token_request_uri += "&redirect_uri=" + redirect_uri
    access_token_request_uri += "&code=" + code

    print(access_token_request_uri)

    #얻은 access token을 이용해서 값을 받아온다.
    access_token_request_uri_data = requests.get(access_token_request_uri)
    json_data = access_token_request_uri_data.json()
    access_token = json_data['access_token']

    #닉네임 등을 받아오는 것
    user_profile_info_uri = "https://kapi.kakao.com/v1/api/talk/profile?access_token="
    user_profile_info_uri += str(access_token)

    user_profile_info_uri_data = requests.get(user_profile_info_uri)
    user_json_data = user_profile_info_uri_data.json()
    nickName = user_json_data['nickName']
    profileImageURL = user_json_data['profileImageURL']
    thumbnailURL = user_json_data['thumbnailURL']


    print("nickName = " + str(nickName))
    print("profileImageURL = " + str(profileImageURL))
    print("thumbnailURL = " + str(thumbnailURL))


    #로그인에 보내기위해서 올려둠
    request.session['nickname'] = nickName


    #중복된 로그인 방지용 -> 이미 있는 아이디라면 바로 학교 입력으로 넘어간다.

    user_objects=Users.objects.all()

    search_users= user_objects.filter(u_name=nickName)

    if search_users :
        return redirect('/apply/')


    return redirect('/login/')



@csrf_exempt
def testing(request):

    form = VideoForm(request.POST or None, request.FILES or None)


    Uname = Users.objects.latest('u_name').u_name
    Uname=str(Uname).replace(' ','_')

    if form.is_valid():
        form.save()


    if request.method == 'POST':
        print("Post가 왔다")


        # form = VideoForm(request.POST)
        # print(form)
        # print(request.POST.get('name', ''))
        # print(request.FILES.get('videofile',''))

        filename = request.POST.get('name', '')
        file = request.FILES.get('videofile', '')
        if file:
            print("비디오파일이이쯤")
            # new_vid = Video.objects.create(
            #     name=request.POST.get('name', ''),
            #     videofile=file,
            # )

            if not os.path.exists('media/videos/'):
                os.mkdir('media/videos/')

            with open('media/videos/'+ str(Uname) + "_" + filename + '.webm', 'wb+') as destination:
                for chunk in file.chunks():

                    destination.write(chunk)
                    #webm으로 바꾸기
                    videoporcessing.convert_to_mp4('media/videos/'+ str(Uname) + "_" + filename + '.webm',Uname)
                    return HttpResponse('Created!')

        else:
            return HttpResponse("Blob getting Error")

    return  render(request,'middle/testing0.html')
