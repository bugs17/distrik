
from multiprocessing import context
from django.shortcuts import render, redirect

# import model
from sejarah.models import Sejarah
from geografis.models import Geografis
from pemerintah.models import Pemerintah, Organisasi
from administrasi.models import Administrasi
from berita.models import Berita

from .forms import SejarahForm, GeografisForm, PemerintahForm, OrganisasiForm, AdministrasiForm, BeritaForm

# index admin panel
def index(request):

    pemerintah = Pemerintah.objects.all()

    context = {
        'title': 'Admin Panel Distrik Ninati',
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
        'link_kembali': link_kembali,
        
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

    pemerintah = Pemerintah.objects.all().order_by('-id')

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
    camat = Pemerintah.objects.get(struktur_organisasi='camat')
    organisasi = Organisasi.objects.all()

    context = {
        'title' : 'Panel | Struktur Organisasi',
        'judul' : 'Struktur Organisasi Pemerintahan Distrik',
        'organisasi': organisasi,
        'camat': camat,
        
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

# get administrasi
def administrasi(request):

    administrasi = Administrasi.objects.all().order_by('-id')

    context ={
        'title':'Panel | Administrasi',
        'administrasi': administrasi,
        
    }
    return render(request, 'panel/administrasi.html',context)

# add administrasi
def add_administrasi(request):
    tombol = "Tambah"
    link_kembali = '/panel/administrasi/'
    if request.method == 'POST':
        form = AdministrasiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = AdministrasiForm()
            pesan = 'Data berhasil ditambahkan'
            context ={
                'title' : 'Panel | Tambah data administrasi',
                'keterangan': 'Tambah Data',
                'form': form,
                'pesan': pesan,
                'tombol': tombol,
                'link_kembali': link_kembali,
            }

            return render(request, 'panel/add_administrasi.html', context)
    else:

        form = AdministrasiForm()

        context = {
            'title' : 'Panel | Tambah data administrasi',
            'keterangan': 'Tambah Data',
            'form': form,
            'tombol': tombol,
            'link_kembali': link_kembali,
        }
    return render(request, 'panel/add_administrasi.html', context)


# edit administrasi administrasi
def update_administrasi(request, pk):
    administrasi_update = Administrasi.objects.get(id=pk)
    form = AdministrasiForm( request.POST or None, request.FILES or None, instance=administrasi_update)
    link_kembali = '/panel/administrasi/'
    tombol = "Update"
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Data Administrasi',
        'keterangan': 'Update administrasi',
        'form': form,
        'tombol': tombol,
        
    }

    return render(request, 'panel/add_administrasi.html', context)

# hapus administrasi
def hapus_administrasi(request, pk):
    hapus_administrasi = Administrasi.objects.filter(id=pk)
    hapus_administrasi.delete()
    

    return redirect('panel:administrasi')


# get berita
def berita(request):
    berita = Berita.objects.all().order_by('-update')
    context = {
        'title' : 'Panel | List Berita',
        'judul' : 'List berita',
        'berita': berita,
    }
    return render(request, 'panel/berita.html', context)


# add berita
def add_berita(request):
    tombol = "Tambah"
    if request.method == 'POST':
        form = BeritaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = BeritaForm()
            pesan = 'Berita berhasil ditambahkan'
            context ={
                'title' : 'Panel | Tambah berita',
                'keterangan': 'Tambah Berita',
                'form': form,
                'pesan': pesan,
                'tombol': tombol,
            }

            return render(request, 'panel/add_berita.html', context)
    else:

        form = BeritaForm()

        context = {
            'title' : 'Panel | Tambah Berita',
            'keterangan': 'Tambah Berita',
            'form': form,
            'tombol': tombol,
        }
    return render(request, 'panel/add_berita.html', context)


# update berita
def update_berita(request, pk):
    berita_update = Berita.objects.get(id=pk)
    form = BeritaForm( request.POST or None, request.FILES or None, instance=berita_update)
    link_kembali = '/panel/berita/'
    
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update berita',
        'keterangan': 'Update data berita',
        'form': form,
        
    }

    return render(request, 'panel/update_berita.html', context)


# hapus berita
def hapus_berita(request, pk):
    hapus_berita = Berita.objects.filter(id=pk)
    hapus_berita.delete()
    

    return redirect('panel:berita')