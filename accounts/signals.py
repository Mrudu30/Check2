from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Exam, Student, Subjects

@receiver(pre_save, sender=Exam)
def select_subjects(sender, instance, **kwargs):
    if instance.course.name == 'IELTS AT':
        instance.subject.clear()
        instance.subject.add(Subjects.objects.get(listening='listening'))
        instance.subject.add(Subjects.objects.get(reading='Reading'))
        instance.subject.add(Subjects.objects.get(writing='Writing'))
        instance.subject.add(Subjects.objects.get(speaking='Speaking'))
