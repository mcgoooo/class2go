"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from c2g.models import Institution, Course
from django.contrib.auth.models import Group 

class C2GUnitTests(TestCase):
    
    fixtures=['db_snapshot.json']
    
    def test_multisave(self):
        """
        Tests saving a course more than once
        """
        numGroupsB4=len(Group.objects.all())
        i=Institution(title='TestInstitute')
        i.save()
        course1=Course(institution=i,title='gack',handle='test-course')
        course1.save()
        course1.title='hack'
        course1.save()
        numGroupsAfter=len(Group.objects.all())
        self.assertEqual(numGroupsB4+4, numGroupsAfter)


    def test_course_create(self):
        """
        Tests that course creation creates groups
        """
        numGroupsB4=len(Group.objects.all())
        i=Institution(title='TestInstitute')
        i.save()
        course1=Course(institution=i,title='gack',handle='test-course')
        course1.save()
        numGroupsAfter=len(Group.objects.all())
        self.assertEqual(numGroupsB4+4, numGroupsAfter)
        

    def test_fixture_install(self):
        """
        Tests that fixtures were installed correctly
        """
        c = Course.objects.get(code='CS1234') 
        self.assertEqual(len(Course.objects.all()),1) 
        self.assertEqual(c.title, u'Natural Language Processing')

                               
    def test_index_page(self):
        """
        Tests that we can access the index page
        """
        resp=self.client.get('/')
        self.assertEqual(resp.status_code,301)
        self.assertIn("nlp/Fall2012", resp['Location'])