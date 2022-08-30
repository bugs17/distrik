

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



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

# from dari app panel
from .forms import (
    SejarahForm, 
    GeografisForm, 
    PemerintahForm, 
    OrganisasiForm, 
    AdministrasiForm, 
    BeritaForm, 
    DataForm, 
    GaleryForm, 
    CrateUserForm, 
    ChangeUserForm,
    ChangePassForm,
    UserProfileForm,
) 


# index admin panel
@login_required(login_url='panel:login')
def index(request):
    groupcheck = Group.objects.get(name= 'admin')

    pemerintah = Pemerintah.objects.all()

    context = {
        'title': 'Admin Panel Distrik Ninati',
        'pemerintah': pemerintah,
        'groupcheck': groupcheck,
    }

    return render(request, 'panel/index.html', context)


# get sejarah
@login_required(login_url='panel:login')
def sejarah(request):
    groupcheck = Group.objects.get(name= 'admin')
    sejarah = Sejarah.objects.all()

    context ={
        'title' : 'Panel | Sejarah Distrik',
        'sejarah': sejarah,
        'groupcheck': groupcheck,
    }

    return render(request, 'panel/sejarahdistrik.html', context)

# update sejarah
@login_required(login_url='panel:login')
def update_sejarah(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
    }

    return render(request, 'panel/update.html', context)


# get geografis
@login_required(login_url='panel:login')
def geografis(request):
    groupcheck = Group.objects.get(name= 'admin')
    geografis = Geografis.objects.all()
    peta = f'<iframe class="col-sm-8" height="558" id="gmap_canvas" src="https://maps.google.com/maps?q=ninati&t=&z=11&ie=UTF8&iwloc=&output=embed" frameborder="0" scrolling="no" marginheight="0" marginwidth="0"></iframe>'

    context = {
        'title' : 'Panel | Geografis Distrik',
        'geografis': geografis,
        'peta' : peta,
        'groupcheck': groupcheck,
        
    }
    return render(request, 'panel/geografis.html', context)


# update geografis
@login_required(login_url='panel:login')
def update_geografis(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'link_kembali': link_kembali,
        'groupcheck': groupcheck,
        
    }

    return render(request, 'panel/update.html', context)


# get geografis
@login_required(login_url='panel:login')
def pemerintah(request):
    groupcheck = Group.objects.get(name= 'admin')
    pemerintah = Pemerintah.objects.all().order_by('-id')

    context = {
        'title' : 'Panel | Pemerintah Distrik',
        'judul' : 'Pemerintah Distrik',
        'pemerintah': pemerintah,
        'groupcheck': groupcheck,

        
    }
    return render(request, 'panel/pemerintah.html', context)


# tambah data pemerintah
@login_required(login_url='panel:login')
def add_pemerintah(request):
    groupcheck = Group.objects.get(name= 'admin')
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
                'groupcheck': groupcheck,
            }

            return render(request, 'panel/add_pemerintah.html', context)
    else:

        form = PemerintahForm()

        context = {
            'title' : 'Panel | Tambah data',
            'keterangan': 'Tambah Data',
            'form': form,
            'tombol': tombol,
            'groupcheck': groupcheck,
        }
    return render(request, 'panel/add_pemerintah.html', context)


# update data pemerintah
@login_required(login_url='panel:login')
def update_pemerintah(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
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
    groupcheck = Group.objects.get(name= 'admin')
    camat = Pemerintah.objects.get(struktur_organisasi='camat')
    organisasi = Organisasi.objects.all()

    context = {
        'title' : 'Panel | Struktur Organisasi',
        'judul' : 'Struktur Organisasi Pemerintahan Distrik',
        'organisasi': organisasi,
        'camat': camat,
        'groupcheck': groupcheck,
        
    }

    return render(request, 'panel/organisasi.html', context)


# update organisasi
@login_required(login_url='panel:login')
def update_organisasi(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
    }

    return render(request, 'panel/update_organisasi.html', context)

# get administrasi
@login_required(login_url='panel:login')
def administrasi(request):
    groupcheck = Group.objects.get(name= 'admin')
    administrasi = Administrasi.objects.all().order_by('-id')

    context ={
        'title':'Panel | Administrasi',
        'administrasi': administrasi,
        'groupcheck': groupcheck,
        
    }
    return render(request, 'panel/administrasi.html',context)

# add administrasi
@login_required(login_url='panel:login')
def add_administrasi(request):
    groupcheck = Group.objects.get(name= 'admin')
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
                'groupcheck': groupcheck,
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
            'groupcheck': groupcheck,
        }
    return render(request, 'panel/add_administrasi.html', context)


# edit administrasi administrasi
@login_required(login_url='panel:login')
def update_administrasi(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
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
    groupcheck = Group.objects.get(name= 'admin')
    berita = Berita.objects.all().order_by('-update')
    context = {
        'title' : 'Panel | List Berita',
        'judul' : 'List berita',
        'berita': berita,
        'groupcheck': groupcheck,
    }
    return render(request, 'panel/berita.html', context)


# add berita
@login_required(login_url='panel:login')
def add_berita(request):
    groupcheck = Group.objects.get(name= 'admin')
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
                'groupcheck': groupcheck,
            }

            return render(request, 'panel/add_berita.html', context)
    else:

        form = BeritaForm()

        context = {
            'title' : 'Panel | Tambah Berita',
            'keterangan': 'Tambah Berita',
            'form': form,
            'tombol': tombol,
            'groupcheck': groupcheck,
        }
    return render(request, 'panel/add_berita.html', context)



# update berita
@login_required(login_url='panel:login')
def update_berita(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
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
    groupcheck = Group.objects.get(name= 'admin')
    datakampung = DataPerKampung.objects.all()


    context = {
        'title':'Panel | Data kampung',
        'judul': 'List kampung dan data',
        'data':datakampung,
        'groupcheck': groupcheck,

    }
    return render(request, 'panel/data.html', context)



# add data
@login_required(login_url='panel:login')
def add_data(request):
    groupcheck = Group.objects.get(name= 'admin')
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
                'groupcheck': groupcheck,
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
                'groupcheck': groupcheck,
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
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
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
    groupcheck = Group.objects.get(name= 'admin')
    galery = Galery.objects.all().order_by('-id')
    context = {
        'title':'Panel | Galery',
        'judul': 'List Galery',
        'galery':galery,
        'groupcheck': groupcheck,
    }

    return render(request, 'panel/galery.html', context)



# add data galery
@login_required(login_url='panel:login')
def add_galery(request):
    groupcheck = Group.objects.get(name= 'admin')
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
                'groupcheck': groupcheck,
            }

            return render(request, 'panel/add_galery.html', context)
    else:

        form = GaleryForm()

        context = {
            'title' : 'Panel | Tambah Galery',
            'keterangan': 'Tambah Galery',
            'form': form,
            'tombol': tombol,
            'groupcheck': groupcheck,
        }
    return render(request, 'panel/add_galery.html', context)



# update galery
@login_required(login_url='panel:login')
def update_galery(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
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
        'groupcheck': groupcheck,
        
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
    groupcheck = Group.objects.get(name= 'admin')
    grup = Group.objects.all()
    if request.method == 'POST':
        form = CrateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name=request.POST.get('pilihgroup'))
            if request.POST.get('pilihgroup') == 'admin':
                user.is_staff = True
                form.save()
                user.groups.add(group)
                return redirect('panel:user')
            else:
                user.groups.add(group)
                return redirect('panel:user')
        else:
            form = CrateUserForm()
            context = {
                'gagal':'GAGAL!! Password harus 8 karakter dan mengandung angka, periksa kembali data yang dimasukan',
                'form':form,
                'grup':grup,
                'groupcheck':groupcheck,
                'title': 'Panel | Buat user baru'
            }
            return render(request,'panel/register.html',context)


    else:

        form = CrateUserForm()
        context = {
            'form': form,
            'grup': grup,
            'groupcheck':groupcheck,
            'title': 'Panel | Buat user baru'
        }
        return render(request, 'panel/register.html', context)



# edit user informasi by admin
@login_required(login_url='panel:login')
def update_user(request, pk):
    grup = Group.objects.all()
    groupcheck = Group.objects.get(name= 'admin') 
    user_update = User.objects.get(id=pk)
    form = ChangeUserForm( request.POST or None, instance=user_update)
    link_kembali = '/panel/user/'
    
    
    if form.is_valid():
        datausername = form.cleaned_data['username']
        form.save()
        group = Group.objects.get(name=request.POST.get('pilihgroup'))
        user = User.objects.get(username=datausername)
        if user.groups.filter(name='admin'):
            user.groups.clear()
            user.groups.add(group)
            form.save()


            
        elif user.groups.filter(name='user'):
            user.groups.clear()
            user.groups.add(group)
            form.save() 
     
        else :
            user.groups.add(group)
            form.save()


        return redirect(link_kembali)
    
    context = {
        'title':'Panel | Update data user',
        'keterangan': 'Update data user',
        'groupcheck': groupcheck,
        'form': form,
        'grup': grup,
        
    }

    return render(request, 'panel/update_user.html' , context)




# user page (hanya di tampilakn ketika yg request berada didalam group admin)
@login_required(login_url='panel:login')
def user_page(request):
    groupcheck = Group.objects.get(name= 'admin')
    user = User.objects.all().order_by('-id')

    context = {
        'user': user,
        'groupcheck': groupcheck,
        'title': 'Panel | user'
   
    }
    return render(request, 'panel/user_page.html', context)



# hapus akun
def delete_user(request, pk):
    hapus_user = User.objects.filter(id=pk)
    hapus_user.delete()

    return redirect('panel:user')



# rubah password tanpa old password
@login_required(login_url='panel:login')
def changepassword(request, pk):
    groupcheck = Group.objects.get(name= 'admin')
    user_update = User.objects.get(id=pk)
    link_kembali = '/panel/user/'


    if request.method == 'POST':
        form = ChangePassForm(user=user_update, data=request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(link_kembali)
    else:
        form = ChangePassForm(user=user_update)
        context = {
            'form':form,
            'title': 'Panel | Ubah Password',
            'groupcheck':groupcheck
        }
        return render(request, 'panel/ubah_password.html', context)






# personal
# user akun seting
@login_required(login_url='panel:login')
def akun_seting(request):
    groupcheck = Group.objects.get(name= 'admin')
    form = ChangeUserForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('/panel/')
        

    context = {
        'title': 'Panel | Akun seting',
        'form': form,
        'groupcheck':groupcheck,
    }
    
    return render(request, 'panel/akun_seting.html', context)






# personal
# user profile seting
@login_required(login_url='panel:login')
def user_profile(request):
    groupcheck = Group.objects.get(name= 'admin')
    form = UserProfileForm(request.POST or None, request.FILES or None, instance=request.user.userprofile)
    if form.is_valid():
        form.save()
        return redirect('/panel/')

    context = {
        'title': 'Panel | Profil seting',
        'form': form,
        'groupcheck':groupcheck,
    }
    return render(request, 'panel/personal_seting.html', context)