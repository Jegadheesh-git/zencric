from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PlayerSerializers
from .models import Player

@api_view(['GET'])
def getAllPlayers(request):
    player = Player.objects.all()
    serializer = PlayerSerializers(player,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getPlayerById(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return Response({"message": "Player not found"}, status=404)

    serializer = PlayerSerializers(player)
    return Response(serializer.data)

@api_view(['POST'])
def addPlayer(request):
    serializer = PlayerSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updatePlayer(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return Response({"message": "Player not found"}, status=404)

    serializer = PlayerSerializers(player, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deletePlayer(request, player_id):
    try:
        player = Player.objects.get(id=player_id)
    except Player.DoesNotExist:
        return Response({"message": "Player not found"}, status=404)

    player.delete()
    return Response({"message": "Player deleted successfully"})