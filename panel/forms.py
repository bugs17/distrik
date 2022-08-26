
from django import forms
from django.forms import ModelForm

from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User

# import model
from .models import UserProfile
from sejarah.models import Sejarah
from geografis.models import Geografis
from pemerintah.models import Pemerintah, Organisasi
from administrasi.models import Administrasi
from berita.models import Berita
from statistik.models import DataPerKampung
from galery.models import Galery



class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'phone', 'foto')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'maxlength':'12', }),
            
        }

# form untuk change informasi user by admin
class ChangeUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', )

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'id': 'username','name':'username' }),
            'email': forms.TextInput(attrs={'class': 'form-control', 'id': 'email','type':'email' }),
            
        }

# form change password tanpa old password
class ChangePassForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ('new_password1', 'new_password2',)


# form untuk register user
class CrateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'groups')




# create form untuk update sejarah distrik
class SejarahForm(ModelForm):
    class Meta:
        model = Sejarah
        fields = ('judul', 'body' )

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Judul'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Isikan Sejarah Distrik disini..', 'aria-label': 'Isikan Sejarah Distrik disini..', 'aria-describedby': 'basic-icon-default-message2'}),
        }


# create form untuk update sejarah distrik
class GeografisForm(ModelForm):
    class Meta:
        model = Geografis
        fields = ('judul', 'body' )

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Judul'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Isikan Geografis Distrik disini..', 'aria-label': 'Isikan Geografis Distrik disini..', 'aria-describedby': 'basic-icon-default-message2'}),
        }


# form add data pemerintah
class PemerintahForm(ModelForm):
    class Meta:
        model = Pemerintah
        fields = ('nama', 'golongan', 'jabatan', 'nip','struktur_organisasi',  'pendidikan','foto')

        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Masukan Nama..'}),
            'golongan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Golongan', 'aria-label': 'Isikan Geografis Distrik disini..', 'aria-describedby': 'basic-icon-default-message2'}),
            'jabatan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Jabatan', 'aria-label': 'Isikan Geografis Distrik disini..', 'aria-describedby': 'basic-icon-default-message2'}),
            'struktur_organisasi': forms.Select(attrs={'class': 'form-select', 'id': 'defaultSelect'}),
            'nip': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Nip','aria-describedby': 'basic-icon-default-message2'}),
            'pendidikan': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masukan Jenjang pendidikan','aria-describedby': 'basic-icon-default-message2'}),
            
            # 'foto': forms.Imagefield(attrs={'class': 'form-control', 'type': 'file'}),
        }

# form add data Organisasi
class OrganisasiForm(ModelForm):
    class Meta:
        model = Organisasi
        fields = ('judul', 'gambar')

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Masukan judul..'})
        }


# form add data administrasi
class AdministrasiForm(ModelForm):
    class Meta:
        model = Administrasi
        fields = ('nama_layanan', 'persyaratan')

        widgets = {
            'nama_layanan': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Masukan nama layanan..'}),
            'persyaratan': forms.Textarea(attrs={'class': 'form-control', 'aria-label': 'Isikan pesyaratan-persyaratan administrasi..', 'aria-describedby': 'basic-icon-default-message2'}),
        }

# form add berita
class BeritaForm(ModelForm):
    class Meta:
        model = Berita
        fields = ('judul', 'body', 'category', 'gambar')

        labels = {
            'body' : 'Isi berita',
            'category' : 'Kategori',
        }

        widgets = {
            'judul': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Isikan judul berita..'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'aria-label': 'Isi berita', 'aria-describedby': 'basic-icon-default-message2'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Isikan kategori berita..'}),
        }



# form add data kampung
class DataForm(ModelForm):
    class Meta:
        model = DataPerKampung
        fields = ('nama_kampung','jumlah_jiwa', 'kk', 'puskesmas', 'sekolah',)

        labels = {
            'nama_kampung' : 'Nama Kampung',
            'jumlah_jiwa': 'Jumlah Penduduk',
            'kk': 'Jumlah kepala Keluarga',
            'puskesmas':'Jumlah Puskesamas',
            'sekolah':'Jumlah Sekolah'
        }

        widgets = {
            'jumlah_jiwa': forms.NumberInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Jumlah Penduduk'}),
            'nama_kampung': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Masukan nama kampung'}),
            'kk': forms.NumberInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Jumlah KK'}),
            'puskesmas': forms.NumberInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Jumlah puskesmas'}),
            'sekolah': forms.NumberInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Jumlah sekolah'}),
            }


    
# form tambah galery
class GaleryForm(ModelForm):
    class Meta:
        model = Galery
        fields = ('deskripsi', 'file',)

        labels = {
            'deskripsi' : 'Deskripsi',
            'file': 'Foto'
        }

        widgets = {
            'deskripsi': forms.TextInput(attrs={'class': 'form-control', 'id': 'basic-default-name', 'placeholder': 'Masukan Deskripsi gambar..'}),

        }
        