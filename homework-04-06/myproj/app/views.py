from django.http import JsonResponse, HttpResponseBadRequest
from .models import Subject, Student, Transcript

from django.views.decorators.http import require_http_methods


@require_http_methods(["GET", "POST"])
def subjects(request):
    data = list(Subject.objects.values())
    return JsonResponse(data, safe=False)


@require_http_methods(["GET", "POST"])
def students(request):
    data = list(Student.objects.values())
    return JsonResponse(data, safe=False)


@require_http_methods(["GET", "POST"])
def transcripts(request):
    data = list(Transcript.objects.values())
    return JsonResponse(data, safe=False)
