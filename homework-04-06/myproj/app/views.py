from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
from rest_framework import generics
from .models import Subject, Student, Transcript
from .serializers import SubjectSerializer, StudentSerializer, TranscriptSerializer
import json


@require_http_methods(["GET"])
def all_subjects(request):
    try:
        subjects = list(Subject.objects.all().values())
        return JsonResponse(subjects, safe=False)
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subjects not found'}, status=404)


@require_http_methods(["GET"])
def all_students(request):
    try:
        students = list(Student.objects.all().values())
        return JsonResponse(students, safe=False)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Students not found'}, status=404)


@require_http_methods(["GET"])
def all_transcripts(request):
    try:
        transcripts = list(Transcript.objects.all().values())
        return JsonResponse(transcripts, safe=False)
    except Transcript.DoesNotExist:
        return JsonResponse({'error': 'Transcripts not found'}, status=404)


@require_http_methods(["GET"])
def subject(request, subject_id):
    try:
        subject = Subject.objects.get(id=subject_id)
        data = {
            'id': subject.id,
            'name': subject.name,
            'description': subject.description
        }
        return JsonResponse(data, safe=False)
    except Subject.DoesNotExist:
        return JsonResponse({'error': 'Subject not found'}, status=404)


@require_http_methods(["GET"])
def student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
        data = {
            'id': student.id,
            'first_name': student.first_name,
            'last_name': student.last_name,
            'gender': student.gender,
            'age': student.age,
            'subjects': list(student.subjects.values())
        }
        return JsonResponse(data, safe=False)
    except Student.DoesNotExist:
        return JsonResponse({'error': 'Student not found'}, status=404)


@require_http_methods(["GET"])
def transcript(request, transcript_id):
    try:
        transcript = Transcript.objects.get(id=transcript_id)
        data = {
            'id': transcript.id,
            'student': transcript.student.id,
            'subject': transcript.subject.id,
            'mark': transcript.mark
        }
        return JsonResponse(data, safe=False)
    except Transcript.DoesNotExist:
        return JsonResponse({'error': 'Transcript not found'}, status=404)


@require_http_methods(["GET"])
def search_students(request):
    query = request.GET.get('q', '')
    try:
        students = Student.objects.filter(last_name__icontains=query).values()
        results = {
            'students': list(students)
        }
        return JsonResponse(results, safe=False)
    except (Subject.DoesNotExist, Student.DoesNotExist, Transcript.DoesNotExist):
        return JsonResponse({'error': 'No results found'}, status=404)


@require_http_methods(["POST"])
def create_subject(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')

        subject = Subject.objects.create(name=name, description=description)

        response_data = {
            'id': subject.id,
            'name': subject.name,
            'description': subject.description
        }

        return JsonResponse(response_data, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


class SubjectList(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TranscriptList(generics.ListCreateAPIView):
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer


class TranscriptDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transcript.objects.all()
    serializer_class = TranscriptSerializer
