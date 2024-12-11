from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status

def player_response_builder(id, location, health, items):
    choices_data = []
    for choice in location.choices.all():
        choices_data.append({
            "id": choice.id,
            "text": choice.text,
        })
    return {
        "player_id": id,
        "current_location": serializers.LocationSerializer(location).data,
        "health": health,
        "items": items,
    }

@api_view(['GET'])
def start_game(request):
    try:
        starting_location = models.Location.objects.get(name="Kastély bejárata")
    except models.Location.DoesNotExist:
        return Response({"error": "Kezdő helyszín nem található."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    player_status = models.PlayerStatus.objects.create(
        current_location=starting_location,
        health=100,
        items=[]
    )

    return Response(player_response_builder(player_status.player_id, starting_location, player_status.health, player_status.items), status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_state(request, player_id):
    try:
        player_status = models.PlayerStatus.objects.get(player_id = player_id)
        return Response(player_response_builder(player_status.player_id, player_status.current_location, player_status.health, player_status.items), status=status.HTTP_200_OK)
    except:
         return Response({"error": "Játékos nem található"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def choose(request):
    player_id = request.data.get('player_id')
    choice_id = request.data.get('choice_id')

    if not player_id or not choice_id:
        return Response({"error": "player_id és choice_id megadása szükséges."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        player_status = models.PlayerStatus.objects.get(player_id=player_id)
    except models.PlayerStatus.DoesNotExist:
        return Response({"error": "Játékos nem található."}, status=status.HTTP_404_NOT_FOUND)
    try:
        choice = player_status.current_location.choices.get(id=choice_id)
    except models.Choice.DoesNotExist:
        return Response({"error": "Érvénytelen választás."}, status=status.HTTP_400_BAD_REQUEST)

    new_location = choice.next_location

    player_status.current_location = new_location
    player_status.save()


    return Response(player_response_builder(player_status.player_id, new_location, player_status.health, player_status.items), status=status.HTTP_200_OK)