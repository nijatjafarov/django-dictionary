import imp
from unicodedata import name
import django
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CreateWordForm
from django.contrib import messages
from .models import Word, Translation, Definition
from PyMultiDictionary import MultiDictionary
from googletrans import Translator
from django.http import HttpResponse
import json
from django.core import serializers
import random

# Yenidən bax
@login_required
def home(request):
    words = Word.objects.filter(author = request.user).order_by('-id')
    if request.method == "POST":
        selectedWords = request.POST.getlist('words')
        if selectedWords != []:
            selectedInts = [ int(x) for x in selectedWords ]
            random_id= random.choice(selectedInts)
            selectedWord = Word.objects.get(id=random_id)
            return render(request, 'app/index.html', {'words': words, 'selectedInts': selectedInts,
            'selectedWord':selectedWord})
    return render(request, 'app/index.html', {'words': words})

@login_required
def source(request):
    words = Word.objects.filter(author = request.user).order_by('-id')
    return render(request, 'app/source.html', {'words': words})

@login_required
def create_word(request):
    if request.method == "POST":
        form = CreateWordForm(request.POST)
        if form.is_valid():
            _name = str(form.cleaned_data['name']).lower()
            if Word.objects.filter(name=_name, author=request.user).exists() == False:
                if form.cleaned_data['author_translation'] != None:
                    _author_translation = str(form.cleaned_data['author_translation']).lower()
                else:
                    _author_translation = ''
                _word = Word(
                    name = _name, 
                    author_translation = _author_translation,
                    author = request.user
                    )
                _word.save()

                dictionary = MultiDictionary()
                meaning = dictionary.meaning('en', _name)
                if meaning[1] != '':
                    for i in range(1, len(meaning)):
                        _definition = Definition(name=meaning[i], word = _word)
                        _definition.save()

                    translator = Translator()
                    trans = translator.translate(str(_word.name), dest='az')

                    all_translations = trans.extra_data['all-translations']
                    if all_translations != None:
                        for i in range(len(all_translations)):
                            _translation = Translation(name=", ".join(all_translations[i][1]), 
                            part_of_speech=all_translations[i][0], word = _word)
                            _translation.save()

                        messages.success(request, 'Yeni söz uğurla əlavə edildi!')
                        return redirect('client-source')
                    messages.error(request, "Bu sözün tərcüməsi yoxdur")
                    _word.delete()
                    form = CreateWordForm()
                    return render(request, 'app/edit.html', {'form': form})
                messages.error(request, "Bu sözün mənası yoxdur")
                _word.delete()
                form = CreateWordForm()
                return render(request, 'app/edit.html', {'form': form})
            else:
                messages.error(request, "Bu söz daha əvvəl daxil edilib.")
                form = CreateWordForm()
                return render(request, 'app/edit.html', {'form': form})
        messages.error(request, "Uğursuz cəhd. Daxil etdiyiniz məlumatları yenidən yoxlayın.")
        form = CreateWordForm()
        return render(request, 'app/edit.html', {'form': form})
    else:
        form = CreateWordForm()
        return render(request, 'app/edit.html', {'form': form})

@login_required
def delete_word(request, pk):
    word = Word.objects.get(id=pk)
    if word.author == request.user:  
        if request.method == "POST":
                word.delete()
                messages.success(request, 'Söz uğurla silindi!')
                return redirect('client-source')
        else:
            return render(request, 'app/delete.html', {'word': word})
    else:    
        messages.error(request, 'Silməyə çalışdığınız söz sizə məxsus deyil!')
        return redirect('client-source')

@login_required
def update_word(request, pk):
    word = Word.objects.get(id=pk)
    if word.author == request.user:    
        if request.method == "POST":
        
            form = CreateWordForm(request.POST)
            if form.cleaned_data['author_translation'] != None:
                _author_translation = str(form.cleaned_data['author_translation']).lower()
            else:
                _author_translation = ''
            word.author_translation = _author_translation
            word.save()
            messages.success(request, 'Sizin tərcüməniz uğurla yeniləndi!')
            return redirect('client-source')
        else:
            return render(request, 'app/update.html', {'word': word})
    else:    
        messages.error(request, 'Düzəltməyə çalışdığınız söz sizə məxsus deyil!')
        return redirect('client-source')
