from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework import status

# @api_view(['GET'])
# def start_game(request):
#     player = models.PlayerStatus()
#     player.current_location = models.Location.objects.get(id=1)
#     player.health = 100
#     player.save()

#     serialized = serializers.PlayerCreatorSerializer(player, many=False)
#     return Response(serialized.data)


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

    location_data = serializers.LocationSerializer(starting_location).data

    choices_data = []
    for choice in starting_location.choices.all():
        choices_data.append({
            "id": choice.id,
            "text": choice.text,
        })

    response_data = {
        "player_id": player_status.player_id,
        "current_location": location_data,
        "health": player_status.health,
        "items": player_status.items,
    }

    return Response(response_data, status=status.HTTP_201_CREATED)