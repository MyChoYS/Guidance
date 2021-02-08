from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Academy, TestSite

# 학원 검색
def services1(request) :
    return render(request, 'services1.html', None)

# 내 주변 학원 검색 (맵)
def services2(request) :
    return render(request, 'services2.html', None)

# 내 주변 시험장 검색 (맵)
def services3(request) :
    mylocation = Academy.objects.all()
    context = {
        'Academy':mylocation,
    }
    return render(request, 'services3.html', context)

    ## thisUserMoments = mymoment.objects.filter(user=randomuserid, score__gte=4).order_by('-momentcreatedate', '-score')[0:4]
# 지도 테스트 나중에 지우기
def tt(request):
    return render(request, 'tt.html', None)

