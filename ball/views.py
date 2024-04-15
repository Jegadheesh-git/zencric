from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BallSerializers
from .models import Ball

@api_view(['GET'])
def getAllBalls(request):
    player = Ball.objects.all()
    serializer = BallSerializers(player,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBallById(request, ball_id):
    try:
        ball = Ball.objects.get(id=ball_id)
    except Ball.DoesNotExist:
        return Response({"message": "Player not found"}, status=404)

    serializer = BallSerializers(ball)
    return Response(serializer.data)

@api_view(['POST'])
def addBall(request):
    serializer = BallSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateBall(request, ball_id):
    try:
        ball = Ball.objects.get(id=ball_id)
    except Ball.DoesNotExist:
        return Response({"message": "Player not found"}, status=404)

    serializer = BallSerializers(ball, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteBall(request, ball_id):
    try:
        ball = Ball.objects.get(id=ball_id)
    except Ball.DoesNotExist:
        return Response({"message": "Player not found"}, status=404)

    ball.delete()
    return Response({"message": "Player deleted successfully"})