from django.shortcuts import render
from django.http import Http404
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, "dictionary/index.html")

def word_details(request):
    if request.method == "POST":
        dict = PyDictionary()
        word = request.POST.get("word")
        meaning = dict.meaning(word)
        key = 'Noun' if 'Noun' in meaning.keys() else 'Verb' 
        synonyms = dict.synonym(word)
        antonyms = dict.antonym(word)

        return render(request, "dictionary/word.html", {
            "word" : word.capitalize(),
            "meaning" : meaning[key][0],
            "synonyms" : synonyms,
            "antonyms" : antonyms
        })
    else:
        return Http404("Sorry this page is not found")
