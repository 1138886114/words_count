from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)


    word_dict = {}
    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    Sortword_dict = sorted(word_dict.items(),key=lambda x:x[1],reverse=True)

    return render(request, 'count.html',{'key_total_count':total_count,
                                         'key_text': user_text,
                                         'key_sort_dict': Sortword_dict,})