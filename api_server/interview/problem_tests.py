from __future__ import unicode_literals
from rest_framework import status
from rest_framework.test import APISimpleTestCase
from django.conf import settings
import pymongo
import random
import string
import datetime


class ProblemTestCase(APISimpleTestCase):

    interviewer_data_template = {
        'username': 'Sharon',
        'password': 'Naive',
        'type': 'hr',
        'email': '',
        'organization': '',
        'contact': '',
        'token': 'houbuhouwa',
        'last_login': datetime.datetime.now()
    }

    room_template = {
        'id': 301,
        'logo': '',
        'candidates': [
            301
        ],
        'problems': [1, 2, 3],
        'interviewer': 'Sharon'
    }

    empty_room_template = {
        'id': 302,
        'logo': '',
        'candidates': [302],
        'problems': [],
        'interviewer': 'Sharon'
    }

    problems_template = [
        {
          "id": 1,
          "roomId": 301,
          "type": "choice",
          "content": {
              "title": "problem1",
              "description": "His lifespan",
              "option": [
                    {
                        "content": "\\infty",
                        "correct": True
                    },
                    {
                        "content": "\\infty",
                        "correct": True
                    }
                  ],
            }
        },
        {
          "id": 2,
          "roomId": 302,
          "type": "choice",
          "content": {
              "title": "problem2",
              "description": "His height",
              "option": [
                        {
                            "content": "\\infty",
                            "correct": True
                        },
                        {
                            "content": "\\infty",
                            "correct": True
                        }
                  ],
              "sampleInput": "1 2",
              "sampleOutput": "-1"
            }
        },
        {
          "id": 3,
          "roomId": 303,
          "type": "choice",
          "content": {
              "title": "problem3",
              "description": "Her speed",
              "option": [
                        {
                            "content": "\\infty",
                            "correct": False
                        },
                        {
                            "content": "c",
                            "correct": True
                        }
                  ],
              "sampleInput": "1 2",
              "sampleOutput": "-1"
            }
        }
    ]

    new_problem_template = {
      "id": 2333,
      "roomId": 302,
      "type": "choice",
      "content": {
          "title": "WHO IS HE?",
          "description": "THE MAN MUST NOT BE NAMED",
          "option": [
                    {
                        "content": "The elder",
                        "correct": True
                    },
                    {
                        "content": "The professor",
                        "correct": True
                    },
                    {
                        "content": "The former chairman",
                        "correct": True
                    },
                    {
                        "content": "Trump",
                        "correct": False
                    }
              ],
          "sampleInput": "1 2",
          "sampleOutput": "-1"
        }
    }

    db_client = None

    @classmethod
    def setUpClass(cls):
        super(ProblemTestCase, cls).setUpClass()
        db_client = pymongo.MongoClient(port=settings.DB_PORT)
        test_db_name = 'test'
        existing_db_names = set(db_client.database_names())
        while True:
            if test_db_name not in existing_db_names:
                break
            # test_db_name = nr.bytes(10)
            test_db_name = ''.join(
                random.choice(string.ascii_letters + string.digits)
                for _ in range(10))
        settings.DB_NAME = test_db_name

    @classmethod
    def tearDownClass(cls):
        super(ProblemTestCase, cls).tearDownClass()
        db_client = pymongo.MongoClient(port=settings.DB_PORT)
        db_client.drop_database(settings.DB_NAME)

    def init_db(self):
        if self.db_client is None:
            self.db_client = pymongo.MongoClient(port=settings.DB_PORT)
            self.db = self.db_client[settings.DB_NAME]

    def get_room_problems(self, room_id, token):
        url = '/api/' + settings.REST_FRAMEWORK['DEFAULT_VERSION'] + \
            '/problem/room/' + str(room_id) + '?token=' + token
        response = self.client.get(url)
        return response

    def post_room_problems(self, room_id, data, token):
        url = '/api/' + settings.REST_FRAMEWORK['DEFAULT_VERSION'] + \
            '/problem/room/' + str(room_id) + '?token=' + token
        if '_id' in data:
            del data['_id']
        response = self.client.post(url, data)
        return response

    def get_problem(self, problem_id, token):
        url = '/api/' + settings.REST_FRAMEWORK['DEFAULT_VERSION'] + \
            '/problem/' + str(problem_id) + '?token=' + token
        response = self.client.get(url)
        return response

    def put_problem(self, problem_id, data, token):
        url = '/api/' + settings.REST_FRAMEWORK['DEFAULT_VERSION'] + \
            '/problem/' + str(problem_id) + '?token=' + token
        response = self.client.put(url, data)
        return response

    def delete_problem(self, problem_id, token):
        url = '/api/' + settings.REST_FRAMEWORK['DEFAULT_VERSION'] + \
            '/problem/' + str(problem_id) + '?token=' + token
        response = self.client.delete(url)
        return response

    def clear_database(self):
        self.db.users.delete_many({})
        self.db.rooms.delete_many({})
        self.db.problems.delete_many({})

    def test_get_room_problems_success(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        response = self.get_room_problems(301, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clear_database()

    def test_post_room_problems_success(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        self.db.users.insert_one(tmp1)
        tmp2 = self.empty_room_template.copy()
        self.db.rooms.insert_one(tmp2)
        response = self.post_room_problems(
            302, self.new_problem_template, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clear_database()

    def test_get_problems_success(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        response = self.get_problem(1, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clear_database()

    def test_put_problems_success(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        updated_problem = self.problems_template[0]
        del updated_problem['_id']
        updated_problem['content']['title'] = "Is Mr.Dong good?"
        response = self.put_problem(1, updated_problem, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clear_database()

    def test_delete_problems_success(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        response = self.delete_problem(1, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.clear_database()

    def test_get_room_problems_failures(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        # Permission check
        response = self.get_room_problems(301, 'zhongyangyezicitama')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # RoomId
        response = self.get_room_problems(305, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.clear_database()

    def test_post_room_problems_failures(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        weak_problem = self.new_problem_template.copy()
        # Permission check
        response = self.post_room_problems(
            301, weak_problem, 'zhongyangyezicitama')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Format check
        del weak_problem['type']
        response = self.post_room_problems(301, weak_problem, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # RoomId
        weak_problem = self.new_problem_template.copy()
        response = self.post_room_problems(305, weak_problem, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.clear_database()

    def test_get_problems_failures(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        # Permission check
        response = self.get_problem(1, 'zhongyangyezicitama')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Problem id
        response = self.get_problem(2333, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.clear_database()

    def test_put_problems_failures(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        # Permission check
        weak_problem = self.new_problem_template.copy()
        weak_problem['id'] = 2
        response = self.put_problem(2, weak_problem, 'zhongyangyezicitama')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Problem id
        response = self.put_problem(2333, weak_problem, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        # Restriction
        response = self.put_problem(3, weak_problem, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # Key error
        del weak_problem['type']
        response = self.put_problem(2, weak_problem, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.clear_database()

    def test_delete_problems_failures(self):
        self.init_db()
        tmp1 = self.interviewer_data_template.copy()
        tmp2 = self.room_template.copy()
        self.db.users.insert_one(tmp1)
        self.db.rooms.insert_one(tmp2)
        for item in self.problems_template:
            self.db.problems.insert_one(item)
        # Permission check
        response = self.delete_problem(1, 'zhongyangyezicitama')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # Problem id
        response = self.delete_problem(2333, 'houbuhouwa')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.clear_database()
