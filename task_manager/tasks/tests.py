from django.test import TestCase
from .models import Family, Task
from datetime import date, timedelta

class FamilyAndTaskTest(TestCase):

    def create_family(self):
        self.family = Family.objects.create(name="Family_Test")
        self.assertEqual(self.family.name, "Family_Test")

    def create_task(self):
        task = Task.objects.create(
            title="Task_Test",
            description="Description_Test",
            state="to do",
            expiration_date=date.today() + timedelta(days=7),
            family=self.family
        )

        self.assertEqual(task.title, "Task_Test")
        self.assertEqual(task.family, self.family)
        self.assertEqual(task.state, "to do")