from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import pymongo
import datetime
import uuid
import jsonschema
import copy
from . import permissions
from .schemas import swagger_schema
from .file_parser import file_parser


candidate_keys = ('id', 'name', 'email', 'phone', 'status', 'roomId', 'record')


@api_view(['POST', 'GET'])
def get_set_candidate(request, **kwargs):
    '''
    'id': '3001',
    'name': 'Mike',
    'email': 'example@example.com',
    'phone': '1300000000',
    'status': 'weimianshi',
    'roomId': '1001',
    'record':{
        'video': 'string',
        'board': 'string',
        'chat' : 'string',
        'code' : 'string',
        'report':'string'
    }
    '''

    # Check user permission
    if permissions.check(request, ('hr', 'interviewer')) != permissions.PASS:
        return Response(
            {
                'status': '30',
                'error': 'Access denied.'
            },
            status.HTTP_403_FORBIDDEN
        )

    client = pymongo.MongoClient()
    db = client[settings.DB_NAME]

    if request.method == 'POST':
        candidate_data = request.data

        # Check key error
        try:
            jsonschema.validate(candidate_data, swagger_schema['definitions']['Candidate'])
        except:
            return Response(
                {
                    'status': '30',
                    'error': 'Key error'
                },
                status.HTTP_400_BAD_REQUEST
            )

        # Add record

        temp_username = "User_" + str(uuid.uuid4())[:8]
        while db.users.find({'username': temp_username}).count() > 0:
            temp_username = "User_" + str(uuid.uuid4())[:8]
        temp_password = uuid.uuid4()
        user_part = {
            'username': temp_username,
            'type': 'candidate',
            'email': candidate_data['email'],
            'password': temp_password,
            'organization': 'Candidate Group',
        }
        if 'phone' in candidate_data:
            user_part['contact'] = candidate_data['phone']
        db.users.insert_one(user_part)

        candidate_part = candidate_data.copy()
        candidate_part['unique_username'] = temp_username
        db.candidate.insert_one(candidate_part)
        return Response(
            {
                'status': '200'
            },
            status.HTTP_200_OK
        )
    elif request.method == 'GET':
        offset = request.GET.get('offset')
        limit = request.GET.get('limit')
        if offset is None or offset == '':
            offset = 0
        else:
            offset = int(offset)

        if limit is None or limit == '':
            limit = 1
        else:
            limit = int(limit)

        sorted_candidate = db.candidate.find({}).sort('id', pymongo.ASCENDING)
        if offset + limit - 1 > int(sorted_candidate.count()):
            return Response(
                {
                    'error': 'Index out of boundary'
                },
                status.HTTP_400_BAD_REQUEST
            )
        return_list = map(lambda x: {k: v for k, v in dict(sorted_candidate).items() if k in candidate_keys},
                          list(sorted_candidate)[offset: offset + limit])
        return Response(
            {
                'data': return_list
                # sorted_candidate[offset, offset + limit]
            },
            status.HTTP_200_OK
        )
    else:
        return Response(
            {
                'error': 'Unknown method'
            },
            status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'DELETE', 'PUT'])
def workon_candidate(request, candidate_id, **kwargs):
    # Check user permission
    if permissions.check(request, ('hr', 'interviewer')) != permissions.PASS:
        return Response(
            {
                'error': 'Access denied.'
            },
            status.HTTP_403_FORBIDDEN
        )

    client = pymongo.MongoClient()
    db = client[settings.DB_NAME]

    # Check existance
    data = db.candidate.find({'id': candidate_id})
    if data.count() == 0:
        return Response(
            {
                'error': 'Candidate not found.'
            },
            status.HTTP_404_NOT_FOUND
        )
    elif data.count() > 1:  # Should never occur
        return Response(
            {
                'error': 'Candidate id duplicated'
            },
            status.HTTP_400_BAD_REQUEST
        )

    if request.method == 'GET':
        # Get data
        for item in data:
            temp_data = {k: v for k, v in dict(item).items() if k in candidate_keys}
            return Response(
                {
                    'data':  temp_data
                },
                status.HTTP_200_OK
            )
    elif request.method == 'PUT':
        # Put data
        input_data = request.data
        if input_data['id'] is not candidate_id:
            for item in data:
                dulp_list = db.candidate.find({'id': input_data['id']})
                if dulp_list.count() > 0:
                    return Response(
                        {
                            'error': 'Trying to generate candidates with same id'
                         },
                        status.HTTP_400_BAD_REQUEST
                    )
        temp_data = {k: v for k, v in input_data.items() if k in candidate_keys}
        db.candidate.update(
            {'id': candidate_id},
            {
                '$set': temp_data
            }
        )
        return Response(
            input_data,
            status.HTTP_200_OK
        )

    elif request.method == 'DELETE':
        # Delete data
        db.candidate.delete_one({'id': candidate_id})
        return Response(
            status.HTTP_200_OK
        )

    else:
        return Response(
            {
                'status': '30',
                'error': 'Unknown request method'
            },
            status.HTTP_400_BAD_REQUEST
        )


@api_view(['PUT'])
def change_status_candidate(request, candidate_id, **kwargs):

    new_status = request.GET.get('status')
    # Check key error

    client = pymongo.MongoClient()
    db = client[settings.DB_NAME]

    # Check user permission
    if permissions.check(request, ('hr', 'interviewer')) != permissions.PASS:
        return Response(
            {
                'status': '30',
                'error': 'Access denied.'
            },
            status.HTTP_403_FORBIDDEN
        )

    candidate = db.candidate.find({'id': candidate_id})
    if candidate.count() == 0:
        return Response(
            {
                'status': '30',
                'error': 'Candidate not found.'
            },
            status.HTTP_404_NOT_FOUND
        )
    elif candidate.count() > 1:
        return Response(
            {
                'status': '30',
                'error': 'Candidate id duplicated'
            },
            status.HTTP_400_BAD_REQUEST
        )
    else:
        for item in candidate:
            db.candidate.update(
                {'id': candidate_id},
                {
                    '$set':
                    {
                        'status': new_status
                    }
                }
            )
            response_dict = {k: v for k, v in dict(item).items() if k in candidate_keys}

            return Response(
                response_dict,
                status.HTTP_200_OK
            )

@api_view(['GET', 'POST'])
def batch_candidate(request, **kwargs):
    if permissions.check(request, ('hr', 'interviewer')) != permissions.PASS:
        return Response(
            {
                'status': '30',
                'error': 'Access denied.'
            },
            status.HTTP_403_FORBIDDEN
        )

    client = pymongo.MongoClient()
    db = client[settings.DB_NAME]

    if request.method == 'POST':
        if request.FILES == None:
            return Response(
                {
                    'error': "No available file"
                },
                status.HTTP_400_BAD_REQUEST
            )
        file_name = request.FILES['file'].name
        if '.' not in file_name:
            return Response(
                {
                    'error': "Unknown file format"
                },
                status.HTTP_400_BAD_REQUEST
            )
        ext_name = file_name.split('.')[-1]
        # print (request.FILES)
        # print (dir(request.FILES))
        file_content = request.FILES['file']

        candidate_list = file_parser(ext_name, file_content)
        #print ("Candidate_list:")
        #print (candidate_list)
        if candidate_list is None:
            return Response(
                {
                    'error': "Illegal file format"
                },
                status.HTTP_400_BAD_REQUEST
            )
        for item in candidate_list:
            candidate_to_be_added = item.copy()
            tmp_id = uuid.uuid4()
            while db.candidate.find({'id': tmp_id}).count() > 0:
                tmp_id = uuid.uuid4()
            candidate_to_be_added['id'] = tmp_id
            db.candidate.insert_one(candidate_to_be_added)

        return Response(
            status.HTTP_200_OK
        )

    elif request.method == 'GET':
        return Response(
            {
                'csv': '../file_example/example2.csv',
                'xlsx': '../file_example/example1.xlsx'
            },
            status.HTTP_200_OK
        )

    else:
        return Response(
            {
                'error': 'No such request type'
            },
            status.HTTP_400_BAD_REQUEST
        )
