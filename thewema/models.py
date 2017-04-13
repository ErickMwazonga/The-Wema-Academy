from __future__ import unicode_literals
from django.db import models


class StudentClass(models.Model):
    STANDARD = (
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five', 'Five'),
        ('Six', 'Six'),
        ('Seven', 'Seven'),
        ('Eight', 'Eight'),
    )

    YEAR = (
        ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'),
        ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'),
        ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'),
        ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'),
        ('2016', '2016'), ('2017', '2017'),
    )

    standard = models.CharField(max_length=10, choices=STANDARD)
    year = models.CharField(max_length=10, choices=YEAR)
    # year = models.DateField(help_text='Use this format : YYYY-MM-DD')
    teacher = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s' % (self.standard, self.year)

    class Meta:
        ordering = ['-year']
        unique_together = ('standard', 'year')


class Subject(models.Model):
    NAME = (
        ('Maths', 'Maths'),
        ('English', 'English'),
        ('Kiswahili', 'Kiswahili'),
        ('Science', 'Science'),
        ('Social Studies', 'Social Studies'),
    )
    name = models.CharField(max_length=20, choices=NAME)
    code = models.CharField(max_length=200)

    def __str__(self):
        return '%s' % self.name


class Student(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    admin_no = models.CharField(max_length=200, unique=True)
    surname = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=6, choices=GENDER)
    dob = models.DateField()
    sclass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    @property
    def full_name(self):
        return '{} {} {}'.format(self.first_name, self.middle_name, self.surname)

    def __str__(self):
        return '%s-%s %s' % (self.admin_no, self.first_name, self.surname)


class Exam(models.Model):
    TERM = (
        ('TERM 1', 'TERM 1'),
        ('TERM 2', 'TERM 2'),
        ('TERM 3', 'TERM 3'),
    )
    EXAM_TYPE = (
        ('Opening-Term', 'Opening-Term'),
        ('Mid-Term', 'Mid-Term'),
        ('End-Term', 'End-Term'),
    )

    term = models.CharField(max_length=200, choices=TERM)
    etype = models.CharField(max_length=200, choices=EXAM_TYPE)

    def __str__(self):
        return '%s %s' % (self.term, self.etype)

    class Meta:
        unique_together = ('term', 'etype')


class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject)
    exam = models.ForeignKey(Exam)
    marks = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.student, self.exam)

    class Meta:
        unique_together = ('student', 'exam', 'subject')


class Feedback(models.Model):
    FEEDBACK_CHOICES = {
        ('Feedback', 'Feedback'),
        ('Correction', 'Correction'),
        ('Support', 'Support'),
    }
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    subject = models.CharField(max_length=200, choices=FEEDBACK_CHOICES)
    message = models.TextField()

    def __str__(self):
        return '{}-{}'.format(self.name, self.message)
