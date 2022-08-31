from django.shortcuts import render
from django.http import HttpResponse
from .models import Score,Memo,Media,Genre
from .forms import EditScoreForm,EditMemoForm,EditMediaForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import Q


def index(request):
    data = Score.objects.all()
    url = request._current_scheme_host
    keyword = request.GET.get('keyword')
    if keyword:
        data = data.filter(Q(title__icontains=keyword))
        if len(data) == 0:
            mes = '見つかりませんでした。'
        messages.success(request, '「{}」の検索結果'.format(keyword))
    params = {
            'data': data,
            'url': url,
        }
    return render(request, 'web/index.html', params)

def edit(request):
    url = request._current_scheme_host
    if (request.method == 'POST'):
        if 'Score' in request.POST:
            obj = Score()
            edit = EditScoreForm(request.POST, instance=obj)
            edit.save()
            return redirect(to=url)
        elif 'Memo' in request.POST:
            obj = Memo()
            edit = EditMemoForm(request.POST, instance=obj)
            edit.save()
            return redirect(to=url)
        elif 'Media' in request.POST:
            obj = Media()
            edit = EditMediaForm(request.POST, instance=obj)
            edit.save()
            return redirect(to=url)
        elif 'TrueScore' in request.POST:
            hidden_data = request.POST['hidden_data']
            obj = Score.objects.get(id=hidden_data)
            edit = EditScoreForm(request.POST, instance=obj)
            edit.save()
            return redirect(to=url)
        elif 'TrueMemo' in request.POST:
            hidden_data = request.POST['hidden_data']
            obj = Memo.objects.get(id=hidden_data)
            edit = EditMemoForm(request.POST, instance=obj)
            edit.save()
            return redirect(to=url)
        elif 'TrueMedia' in request.POST:
            hidden_data = request.POST['hidden_data']
            obj = Media.objects.get(id=hidden_data)
            edit = EditMediaForm(request.POST, instance=obj)
            edit.save()
            return redirect(to=url)
    
    edit = request.GET['edit']
    if edit == "True":
        edittype = request.GET['edittype']
        if edittype == "Score":
            formtype = "TrueScore"
            scoreid = request.GET['id']
            score = Score.objects.get(id=scoreid)
            scoretitle = score.title
            initial_dict = dict(title=scoretitle)
            params = {
            'form': EditScoreForm(initial=initial_dict),
            'formtype': formtype,
            'id': scoreid,
            }
        elif edittype == "Memo":
            formtype = "TrueMemo"
            memoid = request.GET['id']
            memo = Memo.objects.get(id=memoid)
            memodocument = memo.document
            initial_dict = dict(document=memodocument)
            params = {
            'form': EditMemoForm(initial=initial_dict),
            'formtype': formtype,
            'id': memoid,
            }
        elif edittype == "Media":
            formtype = "TrueMedia"
            mediaid = request.GET['id']
            media = Media.objects.get(id=mediaid)
            mediapath = media.mediapath
            mediacomment = media.comment
            initial_dict = dict(mediapath=mediapath, comment=mediacomment)
            params = {
            'form': EditMediaForm(initial=initial_dict),
            'formtype': formtype,
            'id': mediaid,
            }
            
    elif edit == "Memo":
        formtype = "Memo"
        scoreid = request.GET['id']
        score = Score.objects.get(id=scoreid)
        scoretitle = score.title
        initial_dict = dict(title=scoretitle)
        params = {
        'form': EditMemoForm(initial=initial_dict),
        'formtype': formtype,
        }
    elif edit == "Media":
        formtype = "Media"
        scoreid = request.GET['id']
        score = Score.objects.get(id=scoreid)
        scoretitle = score.title
        initial_dict = dict(title=scoretitle)
        params = {
        'form': EditMediaForm(initial=initial_dict),
        'formtype': formtype,
        }
    else:
        formtype = "Score"
        params = {
        'form': EditScoreForm,
        'formtype': formtype,
        }
    return render(request, 'web/edit.html', params)

def db(request, num):
    score = Score.objects.get(id=num)
    memo = score.memo_set.all()
    media = score.media_set.all()
    url = request._current_scheme_host
    params = {
        'score': score, 
        'memo': memo,
        'media': media,
        'id': num,
        'url': url,
        }
    return render(request, 'web/db.html', params)


def dbdel(request):
    url = request._current_scheme_host
    if (request.method == 'POST'):
        dbid = request.POST['id']
        if "del_yes" in request.POST:
            Score.objects.filter(id=dbid).delete()
            return redirect(to=url)
        elif "del_no" in request.POST:
            backurl = url + "/db/" + dbid
            return redirect(to=backurl)
    
    dbid = request.GET['id']
    score = Score.objects.filter(id=dbid)
    params = {
        'id': dbid,
        'score': score,
        }
    return render(request, 'web/dbdel.html', params)