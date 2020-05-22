from django.shortcuts import render
import requests
import json
from .forms import SearchForm

# Create your views here.


def get_word(word):

    s_url = "https://wordsapiv1.p.rapidapi.com/words/{}/synonyms".format(word)
    a_url = "https://wordsapiv1.p.rapidapi.com/words/{}/antonyms".format(word)
    e_url = "https://wordsapiv1.p.rapidapi.com/words/{}/examples".format(word)
    headers = {
        'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
        'x-rapidapi-key': "503340062bmshdf589e0c55dd9afp1ceecejsn2b96afda0fb3"
    }

    try:
        s_response = requests.request("GET", s_url, headers=headers)
        s_data = s_response.text.encode('cp850', 'replace').decode('utf-8')
        j_data_s = json.loads(s_data)
    except:
        pass
    try:
        a_response = requests.request("GET", a_url, headers=headers)
        a_data = a_response.text.encode('cp850', 'replace').decode('utf-8')
        j_data_a = json.loads(a_data)
    except:
        pass
    try:
        e_response = requests.request("GET", e_url, headers=headers)
        e_data = e_response.text.encode('cp850', 'replace').decode('utf-8')
        j_data_e = json.loads(e_data)
    except:
        pass
    #print(response.text.encode('cp850', 'replace'))

    if 'message' not in j_data_s:
        synonyms = j_data_s["synonyms"]
    else:
        synonyms = []
    if 'message' not in j_data_a:
        antonyms = j_data_a["antonyms"]
    else:
        antonyms = []
    if 'message' not in j_data_e:
        examples = j_data_e["examples"]
    else:
        examples = []
    return synonyms, antonyms, examples


def index(request):

    if request.method == "POST":
        form = SearchForm(request.POST or None)
        if form.is_valid:
            word = request.POST.get('word')
            synonyms, antonyms, example = get_word(word)

            return render(request, 'main/index.html', {
                'form': form,
                'synonyms': synonyms,
                'antonyms': antonyms,
                'example': example
            })
    else:
        form = SearchForm()
    return render(request, 'main/index.html', {
        'form': form,

    })
