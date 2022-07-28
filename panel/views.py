
from multiprocessing import context
from django.shortcuts import render, redirect

# import model
from sejarah.models import Sejarah
from geografis.models import Geografis
from pemerintah.models import Pemerintah, Organisasi

from .forms import SejarahForm, GeografisForm, PemerintahForm, OrganisasiForm

# index admin panel
def index(request):

    pemerintah = Pemerintah.objects.all()

    context = {
        'title': 'Admin Panel',
        'pemerintah': pemerintah,
    }

    return render(request, 'panel/index.html', context)


# get sejarah
def sejarah(request):

    sejarah = Sejarah.objects.all()

    context ={
        'title' : 'Panel | Sejarah Distrik',
        'sejarah': sejarah,
    }

    return render(request, 'panel/sejarahdistrik.html', context)

# update sejarah
def update_sejarah(request, pk):
    sejarah_update = Sejarah.objects.get(id=pk)
    form = SejarahForm( request.POST or None, instance=sejarah_update)
    link_kembali = '/panel/sejarahdistrik/'
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Sejarah Distrik',
        'keterangan': 'Update Sejarah Distrik',
        'form': form,
        'link_kembali': link_kembali
        
    }

    return render(request, 'panel/update.html', context)


# get geografis
def geografis(request):

    geografis = Geografis.objects.all()
    peta = f'<iframe class="col-sm-8" height="558" id="gmap_canvas" src="https://maps.google.com/maps?q=ninati&t=&z=11&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>'

    context = {
        'title' : 'Panel | Geografis Distrik',
        'geografis': geografis,
        'peta' : peta
        
    }
    return render(request, 'panel/geografis.html', context)


# update geografis
def update_geografis(request, pk):
    geografis_update = Geografis.objects.get(id=pk)
    form = GeografisForm( request.POST or None, instance=geografis_update)
    link_kembali = '/panel/geografisdistrik/'
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Geografis Distrik',
        'keterangan': 'Update Geografis Distrik',
        'form': form,
        'link_kembali': link_kembali
        
    }

    return render(request, 'panel/update.html', context)


# get geografis
def pemerintah(request):

    pemerintah = Pemerintah.objects.all()

    context = {
        'title' : 'Panel | Pemerintah Distrik',
        'judul' : 'Pemerintah Distrik',
        'pemerintah': pemerintah,

        
    }
    return render(request, 'panel/pemerintah.html', context)

# tambah data pemerintah
def add_pemerintah(request):
    tombol = "Tambah"
    if request.method == 'POST':
        form = PemerintahForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = PemerintahForm()
            pesan = 'Data berhasil ditambahkan'
            context ={
                'title' : 'Panel | Tambah data',
                'keterangan': 'Tambah Data',
                'form': form,
                'pesan': pesan,
                'tombol': tombol,
            }

            return render(request, 'panel/add_pemerintah.html', context)
    else:

        form = PemerintahForm()

        context = {
            'title' : 'Panel | Tambah data',
            'keterangan': 'Tambah Data',
            'form': form,
            'tombol': tombol,
        }
    return render(request, 'panel/add_pemerintah.html', context)


# update data pemerintah
def update_pemerintah(request, pk):
    pemerintah_update = Pemerintah.objects.get(id=pk)
    form = PemerintahForm( request.POST or None, request.FILES or None, instance=pemerintah_update)
    link_kembali = '/panel/pemerintahdistrik/'
    tombol = "Update"
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Data Pemerintah',
        'keterangan': 'Update Pemerintah Distrik',
        'form': form,
        'link_kembali': link_kembali,
        'tombol': tombol,
        
    }

    return render(request, 'panel/add_pemerintah.html', context)


# hapus data pemerintah
def hapus_pemerintah(request, pk):
    hapus_pemerintah = Pemerintah.objects.filter(id=pk)
    hapus_pemerintah.delete()
    

    return redirect('panel:pemerintah')


# get struktur organisasi
def organisasi(request):

    organisasi = Organisasi.objects.all()

    context = {
        'title' : 'Panel | Struktur Organisasi',
        'judul' : 'Struktur Organisasi Pemerintahan Distrik',
        'organisasi': organisasi
        
    }

    return render(request, 'panel/organisasi.html', context)

# update organisasi

def update_organisasi(request, pk):
    organisasi_update = Organisasi.objects.get(id=pk)
    form = OrganisasiForm( request.POST or None, request.FILES or None, instance=organisasi_update)
    link_kembali = '/panel/organisasi/'
    
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Data Pemerintah',
        'keterangan': 'Update Struktur Organisasi',
        'form': form,
        
    }

    return render(request, 'panel/update_organisasi.html', context)