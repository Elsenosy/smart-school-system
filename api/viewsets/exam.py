from rest_framework import viewsets, status
from api.serializers import ExamSerializer, ExamQuestionSerializer
from api.models import Exam
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

# Exam viewSet
class ExamViewSet(viewsets.ModelViewSet):
    queryset         = Exam.objects.all()
    serializer_class = ExamSerializer

    def retrieve(self, request, pk=None):
        exam = get_object_or_404(self.queryset, pk=pk)
        data = {
            "id": exam.id,
            "title": exam.title,
            "duration": exam.duration,
            "mark": exam.mark,
            "notes": exam.notes
        }

        response = {
            "status": True,
            "payload": data
        }

        return Response(response)
    
    @action(detail=True, methods=['post'])
    def addQuestions(self, request, pk=None):
        exam = self.get_object()

        questions = list()
        for question in request.data:
            question.update({"exam": exam.id})

            newQ = ExamQuestionSerializer(data=question)
            
            if newQ.is_valid():
                newQ.save()

                questions.append({
                    "data": True,
                    "question": newQ.data
                })
            else:
                return Response(newQ.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(questions)
        
    @action(detail=True, methods=['get'])
    def examsLookup(self):
        return Response(self.queryset)