from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Academy_review, TestSite_review
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
