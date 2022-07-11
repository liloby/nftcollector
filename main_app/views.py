from django.shortcuts import render
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Nft:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, cost, description, id):
    self.name = name
    self.cost = cost
    self.description = description
    self.id = id
 

nfts = [
  Nft('CryptoPunks', '$1500', 'Monkey', 23),
  Nft('Meebits', '$10000', 'Moon', 1023),
  Nft('The Saudis', '$300', 'Cat', 101)
]


# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

# Add new view
def nfts_index(request):
  return render(request, 'nfts/index.html', { 'nfts': nfts })
