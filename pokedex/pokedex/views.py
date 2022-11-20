from django.shortcuts import render
import requests

# Liste de pokémon dans la limite de 151
urlPokedex = 'https://pokeapi.co/api/v2/pokemon?limit=151&offset=0'


def equipe(request):
  """ Renvoie la page equipe """

  equipe = ['equipe_test']

  # réponse de la création d'équipe
  rep = request.GET.get("create_equipe")

  if rep:
    equipe.append(rep)

  return render(request, "equipe.html")

def index(request):
  """ Renvoie la page pokedex/index """

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
      elif req.status_code == 200:
        message = f"{rep.capitalize()} est présent dans notre pokedex"
      context['message'] = message
    except Exception:
      message = "Une erreur est survenue, veuillez recommencer votre recherche"
      context['message'] = message


  return render(request, "index.html", context)