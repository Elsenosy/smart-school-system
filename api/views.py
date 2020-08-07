from django.shortcuts import render
from django.http import HttpResponse 
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import MaterialSerializer, ExamSerializer, ExamQuestionSerializer, ExamQuestionAnswerSerializer
from .models import Exam, Material, ExamQuestion, ExamQuestionAnswer
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from  django.http import Http404

# Create your views here.

def index(request):
    timenow = timezone.now().date()
    return HttpResponse(timenow)

@api_view(['get'])
def examsLookup(request):
    exams = Exam.objects.values('id','title')
    return Response({'data': exams})

@api_view(['get'])
def getExamQuestions(request, id):
    questions = ExamQuestion.objects.filter(exam=id)
    questionsSerialized = ExamQuestionSerializer(questions, many=True)

    if questionsSerialized.data != []:
        return Response({"data": questionsSerialized.data}, status=status.HTTP_200_OK)
    else:
        return Response({"data": None}, status=status.HTTP_204_NO_CONTENT)

"""
    ## Question answers part
"""
@api_view(['post'])
def addAnswerForQuestion(request, id):
    # Check if object exists
    try:
        question = ExamQuestion.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404
    
    answer = ExamQuestionAnswer(
                        examquestion = question,
                        content = request.data.get('content'),
                        is_right_answer = request.data.get('is_right')
                        )
                        
    serlizedObject = ExamQuestionAnswerSerializer(answer)

    return Response({"data":serlizedObject.data}, status=status.HTTP_200_OK)

@api_view(['get'])
def getSubjectMaterials(request, id):
    materials = Material.objects.filter(subject=id)
    materialSerialized = MaterialSerializer(materials, many=True)

    if materials != []:
        return Response({"data": materialSerialized.data}, status=status.HTTP_200_OK)
    else:
        return Response({"data": None}, status=status.HTTP_204_NO_CONTENT)