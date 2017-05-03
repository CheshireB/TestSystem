from selenium import webdriver
from django.test import TestCase
from .models import Subject, tasks

class MainPageTests(TestCase):
    def setUp(self):
        Subject.objects.create(nameoftask="balblabla", subjecteng="math", typeoftask="1", subject="Математика")
        Subject.objects.create(nameoftask="1", subjecteng="russian", typeoftask="1", subject="Русский язык")
        Subject.objects.create(nameoftask="2", subjecteng="russian", typeoftask="2", subject="Русский язык")
        Subject.objects.create(nameoftask="3", subjecteng="russian", typeoftask="3", subject="Русский язык")
        Subject.objects.create(nameoftask="4", subjecteng="russian", typeoftask="4", subject="Русский язык")
        tasks.objects.create(
            type_task = 1,
            task = "bla",
            answer = "11",
            subject_id = "math",
            test_id = 1,
        )

    def test_get_main(self):
        response = self.client.get('http://127.0.0.1:8000/')
        self.assertEqual(response.status_code, 200)

    def test_get_subject(self):
        subjects = Subject.objects.all()
        subjectList = []

        for i in subjects:
            if i.subjecteng not in subjectList:
                subjectList.append(i.subjecteng)

        for i in subjectList:
            response = self.client.get('http://127.0.0.1:8000/{0}'.format(i))
            self.assertEqual(response.status_code, 200)

    def test_check_static_var(self):
        browser = webdriver.Firefox()
        browser.get("http://127.0.0.1:8000/math")
        elm = browser.find_elements_by_id("myid")

        self.assertEqual(len(elm), 6)

        browser.close()

    def test_check_generatic_table_name(self):
        browser = webdriver.Firefox()
        browser.get("http://127.0.0.1:8000/math")
        elm = browser.find_elements_by_id("genericmy")
        self.assertNotEqual(elm, [])

        browser.close()

    def test_generatic_button_plus(self):
        browser = webdriver.Firefox()
        browser.get("http://127.0.0.1:8000/math")
        elm = browser.find_elements_by_id("plusbutton")[0]
        old_value = browser.find_elements_by_id("number")[0].get_attribute('value')
        elm.click()
        browser.implicitly_wait(5)
        new_value = browser.find_elements_by_id("number")[0].get_attribute('value')
        self.assertNotEqual(old_value,new_value)
        browser.close()

    def test_generatic_button_minus(self):
        browser = webdriver.Firefox()
        browser.get("http://127.0.0.1:8000/math")
        elm = browser.find_elements_by_id("minusbutton")[0]
        old_value = browser.find_elements_by_id("number")[0].get_attribute('value')
        elm.click()
        browser.implicitly_wait(5)
        new_value = browser.find_elements_by_id("number")[0].get_attribute('value')
        self.assertNotEqual(old_value,new_value)
        browser.close()

    def test_get_static_test(self):
        response = self.client.get('http://127.0.0.1:8000/math/1')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('http://127.0.0.1:8000/russian/1')
        self.assertEqual(response.status_code, 200)










