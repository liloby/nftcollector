from django.shortcuts import render
from .models import Nft


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

# Add new view
def nfts_index(request):
  nfts = Nft.objects.all()
  return render(request, 'nfts/index.html', { 'nfts': nfts })

def nfts_detail(request, nft_id):
  nft = Nft.objects.get(id=nft_id)
  return render(request, 'nfts/detail.html', { 'nft': nft })