import random
from django.core.management.base import BaseCommand
from thewema.models import Student, Exam, Score, Subject


class Command(BaseCommand):
    help = "Generate scores for all students for the last exam"

    def generate(self):
        '''
        Generate scores for the 5 standard subjects:
        Maths, English, Kiswahili, Science, Social Studies
        '''

        scores = []

        for subject_id in [1, 2, 3, 4, 5]:
            subject = Subject.objects.get(pk=subject_id)
            for student in Student.objects.iterator():
                kwargs = {
                     'student': student,
                     'exam': Exam.objects.last(),
                     'subject': subject,
                     'marks': random.randint(30, 100)
                }
                scores.append(Score(**kwargs))
        Score.objects.bulk_create(scores)

    def handle(self, *args, **options):
        self.generate()
