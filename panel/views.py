
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from django.contrib.auth.models import User, Group


# import model
from sejarah.models import Sejarah
from geografis.models import Geografis
from pemerintah.models import Pemerintah, Organisasi
from administrasi.models import Administrasi
from berita.models import Berita
from galery.models import Galery

# import model statistik
from statistik.models import DataPerKampung

from .forms import SejarahForm, GeografisForm, PemerintahForm, OrganisasiForm, AdministrasiForm, BeritaForm, DataForm, GaleryForm, CrateUserForm


# index admin panel
@login_required(login_url='panel:login')
def index(request):

    pemerintah = Pemerintah.objects.all()

    context = {
        'title': 'Admin Panel Distrik Ninati',
        'pemerintah': pemerintah,
    }

    return render(request, 'panel/index.html', context)


# get sejarah
@login_required(login_url='panel:login')
def sejarah(request):

    sejarah = Sejarah.objects.all()

    context ={
        'title' : 'Panel | Sejarah Distrik',
        'sejarah': sejarah,
    }

    return render(request, 'panel/sejarahdistrik.html', context)

# update sejarah
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
def pemerintah(request):

    pemerintah = Pemerintah.objects.all().order_by('-id')

    context = {
        'title' : 'Panel | Pemerintah Distrik',
        'judul' : 'Pemerintah Distrik',
        'pemerintah': pemerintah,

        
    }
    return render(request, 'panel/pemerintah.html', context)


# tambah data pemerintah
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
def hapus_pemerintah(request, pk):
    hapus_pemerintah = Pemerintah.objects.filter(id=pk)
    hapus_pemerintah.delete()
    

    return redirect('panel:pemerintah')


# get struktur organisasi
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
def administrasi(request):

    administrasi = Administrasi.objects.all().order_by('-id')

    context ={
        'title':'Panel | Administrasi',
        'administrasi': administrasi,
        
    }
    return render(request, 'panel/administrasi.html',context)

# add administrasi
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
def hapus_administrasi(request, pk):
    hapus_administrasi = Administrasi.objects.filter(id=pk)
    hapus_administrasi.delete()
    

    return redirect('panel:administrasi')


# get berita
@login_required(login_url='panel:login')
def berita(request):
    berita = Berita.objects.all().order_by('-update')
    context = {
        'title' : 'Panel | List Berita',
        'judul' : 'List berita',
        'berita': berita,
    }
    return render(request, 'panel/berita.html', context)


# add berita
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
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
@login_required(login_url='panel:login')
def hapus_berita(request, pk):
    hapus_berita = Berita.objects.filter(id=pk)
    hapus_berita.delete()
    

    return redirect('panel:berita')



# get data
@login_required(login_url='panel:login')
def data(request):

    datakampung = DataPerKampung.objects.all()


    context = {
        'title':'Panel | Data kampung',
        'judul': 'List kampung dan data',
        'data':datakampung,

    }
    return render(request, 'panel/data.html', context)



# add data
@login_required(login_url='panel:login')
def add_data(request):
    tombol = "Tambah"
    if request.method == 'POST':
        kampung = request.POST['nama_kampung'].lower()
        form = DataForm(request.POST, request.FILES)
        
        if DataPerKampung.objects.filter(nama_kampung=kampung):
            messages.error(request, 'Nama kampung sudah ada !')
            form = DataForm()
            context ={
                'title' : 'Panel | Tambah data kampung',
                'keterangan': 'Tambah data kampung',
                'form': form,
                'tombol': tombol,
            }
            return render(request, 'panel/add_data.html', context)

        elif form.is_valid():
            form.save()
            form = DataForm()
            pesan = 'Data berhasil ditambahkan'
            context ={
                'title' : 'Panel | Tambah data kampung',
                'keterangan': 'Tambah data kampung',
                'form': form,
                'pesan': pesan,
                'tombol': tombol,
            }

            return render(request, 'panel/add_data.html', context)
    else:

        form = DataForm()

        context = {
            'title' : 'Panel | Tambah data kampung',
            'keterangan': 'Tambah data kampung',
            'form': form,
            'tombol': tombol,
        }
    return render(request, 'panel/add_data.html', context)



# update data
@login_required(login_url='panel:login')
def update_data(request, pk):
    tombol = "Simpan"
    data_update = DataPerKampung.objects.get(id=pk)
    form = DataForm( request.POST or None, request.FILES or None, instance=data_update)
    link_kembali = '/panel/data/'
    
    if form.is_valid():
        
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Data Kampung',
        'keterangan': 'Update data kampung',
        'form': form,
        'tombol': tombol,
        
    }

    return render(request, 'panel/update_data.html', context)



# hapus data
@login_required(login_url='panel:login')
def hapus_data(request, pk):
    hapus_data = DataPerKampung.objects.filter(id=pk)
    hapus_data.delete()

    return redirect('panel:data')


# get galery
@login_required(login_url='panel:login')
def galery(request):
    galery = Galery.objects.all().order_by('-id')
    context = {
        'title':'Panel | Galery',
        'judul': 'List Galery',
        'galery':galery,
    }

    return render(request, 'panel/galery.html', context)



# add data galery
@login_required(login_url='panel:login')
def add_galery(request):
    tombol = "Tambah"
    if request.method == 'POST':
        form = GaleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = GaleryForm()
            pesan = 'Foto berhasil ditambahkan'
            context ={
                'title' : 'Panel | Tambah Galery',
                'keterangan': 'Tambah Galery',
                'form': form,
                'pesan': pesan,
                'tombol': tombol,
            }

            return render(request, 'panel/add_galery.html', context)
    else:

        form = GaleryForm()

        context = {
            'title' : 'Panel | Tambah Galery',
            'keterangan': 'Tambah Galery',
            'form': form,
            'tombol': tombol,
        }
    return render(request, 'panel/add_galery.html', context)



# update galery
@login_required(login_url='panel:login')
def update_galery(request, pk):
    tombol = "Simpan"
    galery_update = Galery.objects.get(id=pk)
    form = GaleryForm( request.POST or None, request.FILES or None, instance=galery_update)
    link_kembali = '/panel/galery/'
    
    if form.is_valid():
        form.save()
        return redirect(link_kembali)
    
    context ={
        'title':'Panel | Update Galery',
        'keterangan': 'Update data Galery',
        'form': form,
        'tombol': tombol,
        
    }

    return render(request, 'panel/update_galery.html', context)



# hapus galery
@login_required(login_url='panel:login')
def hapus_galery(request, pk):
    hapus_galery = Galery.objects.filter(id=pk)
    hapus_galery.delete()

    return redirect('panel:galery')


# login
def login_panel(request):
    if request.user.is_authenticated:
        return redirect('panel:index')
    
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('panel:index')
            else:
                messages.error(request,('Login gagal. username/password salah'))
                return redirect('panel:login')
        
        else:
            return render(request, 'panel/login.html')

# logout
def logout_panel(request):
    logout(request)
    messages.success(request,('Anda telah Logout dari dashboard admin'))
    return redirect('panel:login')







# register
@login_required(login_url='panel:login')
def register(request):
    grup = Group.objects.all()
    if request.method == 'POST':
        form = CrateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST.get('test')
)
            user.groups.add(group)
            return redirect('panel:user')
        else:
            form = CrateUserForm()
            context = {
                'gagal':'GAGAL!! Password harus 8 karakter dan mengandung angka',
                'form':form,
                'grup':grup,
            }
            return render(request,'panel/register.html',context)


    else:

        form = CrateUserForm()
        context = {
            'form': form,
            'grup': grup,
        }
        return render(request, 'panel/register.html', context)


def user_page(request):
    user = User.objects.all().order_by('-id')

    
    context = {
        'user': user,

        
    }
    return render(request, 'panel/user_page.html', context)


