from dataclasses import fields
from django import forms
from django.forms import ModelForm

# import model
from sejarah.models import Sejarah
from geografis.models import Geografis
from pemerintah.models import Pemerintah, Organisasi
from administrasi.models import Administrasi


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
