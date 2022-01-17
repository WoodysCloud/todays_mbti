from django.shortcuts import render

# Create your views here.
from mainPage.models import Interior_obj

import random

def main(request):
    print('mainPage 호출됨')
    context = {'mbti': ['ENFJ','ENFP','ENTJ','ENTP','ESFJ',
                 'ESFP','ESTJ','ESTP','INFJ','INFP',
                 'INTJ','INTP','ISFJ','ISFP','ISTJ','ISTP'],
               }
    return render(request, 'mainPage/main.html',context)

def test(request):
    print('test 페이지')

    # 회원 mbti에 해당하는 best mood에서 랜덤 10개
    mood = list(Interior_obj.objects.filter(individuality=1))
    print("mood data 가져온 것: ", mood)
    moodpick = random.sample(mood, 10)

    # 회원 mbti에 해당하는 top10 소품 10개
    objpick = Interior_obj.objects.order_by('-enfj')[:10]

    # 잘 넘어오는지 확인
    print("무드 Random10 >> ", moodpick)
    print("소품 Top10 >> ", objpick)

    # 딕셔너리 형태로 넘겨주기
    context = {
        'mood' : moodpick,
        'obj' : objpick
    }

    return render(request, 'mainPage/test.html', context)

def board(request):
    print('게시판')
    return render(request, 'mainPage/board.html')

