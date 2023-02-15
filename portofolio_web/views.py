from django.shortcuts import render

def HalamanUtama(request):
    return render(request, "halaman_utama.html")
