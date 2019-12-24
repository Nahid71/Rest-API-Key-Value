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


@api_view(['GET', 'POST'])
def values(request, *args, **kwargs):
    if request.method == 'GET':
        values = {}
        if request.GET:
            m_keys = request.GET['keys'].split()
            for key_ in m_keys:
                values[key_] = redis_instance.get(key_)
            response = {
                'msg': f"Found  items.",
                'values': values
            }
        else:

            for key in redis_instance.keys("*"):
                values[key.decode("utf-8")] = redis_instance.get(key)
            response = {
                'msg': f"Found  items.",
                'values': values
            }
        return Response(response, status=200)
    elif request.method == 'POST':
        items = json.loads(request.body)
        print(items)
        i = 0
        while i < len(items):
            key = list(items.keys())[i]
            value = list(items.values())[i]
            redis_instance.setex(key, timedelta(minutes=5), value)
            i += 1
        response = {
            'msg': f"successfully set to"
        }
        return Response(response, 201)
