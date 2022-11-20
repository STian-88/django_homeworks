import pytest
from rest_framework.test import APIClient
from model_bakery import baker
import random
from students.models import Student, Course
from students.filters import CourseFilter


@pytest.fixture
def path():
    return 'http://127.0.0.1:8000/api/v1/courses/'

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def random_num():
    return random.randrange(1, 10)

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory, random_num, path):
    courses = course_factory(_quantity=10)
    random_course_id = random.choice(Course.objects.values_list('id'))[0]
    response = client.get(path, {'id': random_course_id})
    assert response.status_code == 200
    data = response.json()[0]
    course_name = [item.name for item in courses if item.id == random_course_id][0]
    assert data['name'] == course_name

@pytest.mark.django_db
def test_get_courses(client, course_factory, random_num, path):
    count = Course.objects.count()
    random_id = random_num
    courses = course_factory(_quantity=random_id)
    data = client.get(path).json()
    assert len(data) == count + random_id

@pytest.mark.django_db
def test_course_filter_name(client, course_factory, random_num, path):
    courses = course_factory(_quantity=10)
    random_course_name = courses[random_num].name
    path = path + '?name=' + random_course_name
    response = client.get(path)
    assert response.status_code == 200
    assert response.json()[0]['name'] == random_course_name

@pytest.mark.django_db
def test_course_filter_id(client, course_factory, random_num, path):
    courses = course_factory(_quantity=10)
    random_course_id = random.choice(Course.objects.values_list('id'))[0]
    path = path + '?id=' + str(random_course_id)
    response = client.get(path)
    assert response.status_code == 200
    assert response.json()[0]['id'] == random_course_id

@pytest.mark.django_db
def test_create_course(client, path):
    count = Course.objects.count()
    data = {'id': '1', 'name': 'Course1'}
    response = client.post(path, data=data)
    assert response.status_code == 201
    assert Course.objects.count() == count + 1

@pytest.mark.django_db
def test_update_course(client, course_factory, path):
    courses = course_factory(_quantity=10)
    random_course_id = random.choice(Course.objects.values_list('id'))[0]
    Course.objects.filter(id=random_course_id).update(name='Update_course_name')
    assert Course.objects.get(id=random_course_id).name == 'Update_course_name'

@pytest.mark.django_db
def test_delete_course(client, course_factory, path):
    courses = course_factory(_quantity=10)
    count = Course.objects.count()
    random_course_id = random.choice(Course.objects.values_list('id'))[0]
    Course.objects.get(id=random_course_id).delete()
    assert Course.objects.count() == count-1


