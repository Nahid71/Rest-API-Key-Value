import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Connect to Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                   port=settings.REDIS_PORT, db=0)


@api_view(['GET', 'POST'])
def values(request, *args, **kwargs):
    if request.method == 'GET':
        values = {}
        count = 0
        for key in redis_instance.keys("*"):
            values[key.decode("utf-8")] = redis_instance.get(key)
            count += 1
        response = {
            'count': count,
            'msg': f"Found {count} items.",
            'values': values
        }
        return Response(response, status=200)
    elif request.method == 'POST':
        items = json.loads(request.body)
        # print(list(items.values()))
        i = 0
        while i < len(items):
            key = list(items.keys())[i]
            value = list(items.values())[i]
            redis_instance.set(key, value)
            i += 1
        response = {
            'msg': f"successfully set to"
        }
        return Response(response, 201)
