from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Academy_review, TestSite_review
from .models import Academy, TestSite
from searchApp.models import Academy_town
from django.http import  JsonResponse

from django.http import HttpResponse
from django.template import loader

# 처음 리뷰 게시판 들어갔을 때, academy 정보 먼저 보여줌

def review(request) :
    page = request.GET.get('page', 1)

    academyReview = Academy_review.objects.all()
    reviewPaginator = Paginator(academyReview, 5)
    reviewlistpage = reviewPaginator.get_page(page)

    context = {"academyReview": reviewlistpage}
    return render(request, 'review.html', context)

def review_academy(request):
    page = request.GET.get('page', 1)

    academyReview = Academy_review.objects.all()
    reviewPaginator = Paginator(academyReview, 5)
    reviewlistpage = reviewPaginator.get_page(page)

    context = {"academyReview": reviewlistpage}
    return render(request, 'review_academy.html', context)


def review_testsite(request):
    page = request.GET.get('page', 1)

    testsiteReview = TestSite_review.objects.all()
    reviewPaginator = Paginator(testsiteReview, 5)
    reviewlistpage = reviewPaginator.get_page(page)

    context = {"testsiteReview": reviewlistpage}
    return render(request, 'review_testsite.html', context)


# 학원 리뷰 삭제
def delete_academy(request):
    pk = request.GET['pk']

    delete_object = Academy_review.objects.get(pk=pk)
    delete_object.delete()
    return redirect("review_academy")

# 시험장 리뷰 삭제
def delete_testsite(request):
    pk = request.GET['pk']

    delete_object = TestSite_review.objects.get(pk=pk)
    delete_object.delete()
    return redirect("review_testsite")

def create_academy_review(request):
    if request.method == "POST":
        title = request.POST['title']
        password = request.POST['password']
        content = request.POST['content']
        academy_id = request.POST['academy_id']
        data = Academy(title=title, password=password, content=content, academy_id=academy_id)
        data.save()
        return redirect("review_academy")
    else:
        context = {"flag":1}
        return render(request, 'create_academy_review.html', context)

def create_testsite_review(request):
    if request.method == "POST":
        title = request.POST['title']
        password = request.POST['password']
        content = request.POST['content']
        testsite_id = request.POST['testsite_id']
        data = TestSite(title=title, password=password, content=content, testsite_id=testsite_id)
        data.save()
        return redirect("review_academy")

    else:
        context = {"flag": 1}
        return render(request, 'create_testsite_review.html', context)

def get_academy_town(request):
    value = request.GET['value']
    academy = Academy_town.objects.all()
    townList = []
    for a in academy:
        if a.town_name==value:
            townList.append(a.city_name)

    return JsonResponse({"townList": townList})

def get_academy_name(request):
    value = request.GET['value']
    academy = Academy.objects.all()
    nameList = []
    for a in academy:
        if a.address_town==value:
            nameList.append(a.name)
    return JsonResponse({"nameList": nameList})

def get_testsite_name(request):
    testsite = TestSite.objects.all()
    nameList = []
    for t in testsite:
        nameList.append(t.name)
    return JsonResponse({"nameList": nameList})
