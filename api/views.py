from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import ExamSerializer
from .models import Exam
# Create your views here.

def index(request):
    timenow = timezone.now().date()
    return HttpResponse(timenow)

@api_view(['get'])
def testTaha(request):
    exams = Exam.objects.values('id','title')
    return Response({'data': exams})