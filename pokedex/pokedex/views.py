from django.shortcuts import render
import requests

# Liste de pokémon dans la limite de 151
urlPokedex = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'


def equipe(request):
  """ Renvoie la page equipe """
  return render(request, "equipe.html")

def index(request):
  """ Renvoie la page pokedex/index"""
  req = requests.get(urlPokedex)
  wb = req.json()
  context = {"pokemon_list": wb['results']}

  # réponse de l'envoie du formulaire de recherche
  rep = request.GET.get("pokemon")
  
  if rep:
    # requete à l'api avec la valeur du formulaire comme nom de pokemon
    try:
      req = requests.get(f"https://pokeapi.co/api/v2/pokemon/{rep.lower()}")
      if req.status_code == 404:
        message = "Nous n'avons pas trouvé votre pokémon, désolé"
        context['message'] = message
    except Exception:
      message = "Une erreur est survenue, veuillez recommencer votre recherche"
      context['message'] = message
  else:
      message = "Veuillez remplir le champ pour effectuer une recherche"
      context['message'] = message


  return render(request, "index.html", context)