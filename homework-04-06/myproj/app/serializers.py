from rest_framework import serializers
from .models import Subject, Student, Transcript


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    subjects = SubjectSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'


class TranscriptSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Transcript
        fields = '__all__'
