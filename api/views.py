import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from datetime import timedelta

# Connect to Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET', 'POST', 'PUT'])
def values(request, *args, **kwargs):
    if request.method == 'GET':
        values = {}
        if request.GET:
            m_keys = request.GET['keys'].split(',')
            for key_ in m_keys:
                values[key_] = redis_instance.get(key_)
                redis_instance.pexpire(key_, timedelta(minutes=1))
            if values:
                msg = "Found items"
            else:
                msg = "No values found"
            response = {
                'msg': msg,
                'values': values
            }
        else:

            for key in redis_instance.keys("*"):
                values[key.decode("utf-8")] = redis_instance.get(key)

            if values:
                msg = "Found items"
            else:
                msg = "No values found"
            response = {
                'msg': msg,
                'values': values
            }
        return Response(response, status=200)

    elif request.method == 'POST':
        items = json.loads(request.body)
        i = 0
        while i < len(items):
            key = list(items.keys())[i]
            value = list(items.values())[i]
            redis_instance.setex(key, timedelta(minutes=1), value)
            i += 1
        response = {
            'msg': "Successfully store the vaules"
        }
        return Response(response, 201)

    elif request.method == 'PUT':
        request_data = json.loads(request.body)
        i = 0
        for key_ in request_data:
            new_value = request_data[key_]
            old_value = redis_instance.get(key_)
            if old_value:
                redis_instance.setex(key_, timedelta(minutes=1), new_value)
                i += 1
        if i > 0:
            msg = f"Successfully updated {i} values"
            response = {
                'msg': msg
            }
            return Response(response, status=200)

        else:
            response = {
                'msg': 'Keys are not exists!'
            }
            return Response(response, status=404)
