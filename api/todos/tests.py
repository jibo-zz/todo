from django.test import TestCase

from .models import Todo


class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Todo.objects.create(title='Cook a meal', body='1 banana 2 rice')

    def test_title_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'

        self.assertEquals(expected_object_name, 'Cook a meal')

    def test_body_content(self):
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'

        self.assertEquals(expected_object_name, '1 banana 2 rice')
