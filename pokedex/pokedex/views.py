from multiprocessing import context
from django.shortcuts import render

# liste de pokémon dans la limite de 151
urlPokedex = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0' 


def index(request):
  return render(request, "index.html")

def pokemon(request):
  req = request.get(urlPokedex)
  wb = req.json()
  context = {"pokemon_list": wb}
  return render(request, "pokemon.html", context)