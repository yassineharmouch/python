from django.shortcuts import render, redirect
from .models import Member, Document, Ajax, CsvUpload,Fourations,Sautage,Avance,Stock,Pfourations
import datetime
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from crud.forms import *
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def index(request):
    fouration_count = Fourations.objects.all().count()
    stock_count = Stock.objects.all().count()

    fouration_count1 = Fourations.objects.filter(profondeur='20').count()
    stock_count1 = Stock.objects.filter(ammonix='20').count()

    labels = []
    data = []

    queryset = Fourations.objects.order_by('-dossage')[:5]
    for fouration in queryset:
        labels.append(fouration.machine)
        data.append(fouration.dossage)


    context = {
        "fouration_count": fouration_count,
        "stock_count": stock_count,
        "fouration_count1": fouration_count1,
        "stock_count1": stock_count1,
        "labels": labels,
        "data": data,

    }

    return render(request, 'index.html' , context)


@login_required
def list(request):
    members_list = Member.objects.all()
    paginator = Paginator(members_list, 5)
    page = request.GET.get('page')
    try:
        members = paginator.page(page)
    except PageNotAnInteger:
        members = paginator.page(1)
    except EmptyPage:
        members = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'members': members})

@login_required
def create(request):
    if request.method == 'POST':
        member = Member(
            firstname=request.POST['firstname'],
            lastname=request.POST['lastname'],
            mobile_number=request.POST['mobile_number'],
            description=request.POST['description'],
            location=request.POST['location'],
            date=request.POST['date'],
            gender=request.POST['gender'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            member.full_clean()
        except ValidationError as e:
            pass
        member.save()
        messages.success(request, 'Member was created successfully!')
        return redirect('/list')
    else:
        return render(request, 'add.html')

@login_required
def edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'edit.html', context)


@login_required
def update(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['firstname']
    member.lastname = request.POST['lastname']
    member.mobile_number = request.POST['mobile_number']
    member.description = request.POST['description']
    member.location = request.POST['location']
    member.date = request.POST['date']
    member.gender = request.POST['gender']
    member.save()
    messages.success(request, 'Member was updated successfully!')
    return redirect('/list')

@login_required
def delete(request, id):
    member = Member.objects.get(id=id)
    member.delete()
    messages.error(request, 'Member was deleted successfully!')
    return redirect('/list')


@login_required
def list8(request):
    fourations_list = Fourations.objects.all()
    paginator = Paginator(fourations_list, 5)
    page = request.GET.get('page')
    try:
        fourations = paginator.page(page)
    except PageNotAnInteger:
        fourations = paginator.page(1)
    except EmptyPage:
        fourations = paginator.page(paginator.num_pages)
    return render(request, 'list8.html', {'fourations': fourations})


@login_required
def list6(request):
    fourations_list = Fourations.objects.all()
    paginator = Paginator(fourations_list, 5)
    page = request.GET.get('page')
    try:
        fourations = paginator.page(page)
    except PageNotAnInteger:
        fourations = paginator.page(1)
    except EmptyPage:
        fourations = paginator.page(paginator.num_pages)
    return render(request, 'list6.html', {'fourations': fourations})


@login_required
def list1(request):
    fourations_list = Fourations.objects.all()
    stocks_list = Stock.objects.all()
    paginator = Paginator(fourations_list, 5)
    page = request.GET.get('page')
    try:
        fourations = paginator.page(page)
    except PageNotAnInteger:
        fourations = paginator.page(1)
    except EmptyPage:
        fourations = paginator.page(paginator.num_pages)
    return render(request, 'list1.html', {'fourations': fourations,
                                          'stocks':stocks_list })

@login_required
def create1(request):
    if request.method == 'POST':
        stock_id = request.POST.get('stocks')
        stocks = Stock.objects.get(id=stock_id)
        observation= request.POST.get('observation')
        num_com = request.POST.get('num_com')
        machine = request.POST.get('machine')
        dossage = request.POST.get('dossage')
        profondeur = request.POST.get('profondeur')
        tranche = request.POST.get('tranche')
        nbr_trou_range = request.POST.get('nbr_trou_range')
        largeur = request.POST.get('largeur')
        panneau = request.POST.get('panneau')
        niveau = request.POST.get('niveau')
        type_tir = request.POST.get('type_tir')
        mode_tir = request.POST.get('mode_tir')
        mode_charge = request.POST.get('mode_charge')
        nbr_trou = request.POST.get('nbr_trou')
        maille = request.POST.get('maille')
        longueur = request.POST.get('longueur')
        nbr_range = request.POST.get('nbr_range')

        fouration = Fourations(
            num_com=request.POST['num_com'],
            observation=request.POST['observation'],
            machine=request.POST['machine'],
            mode_tir=request.POST['mode_tir'],
            type_tir=request.POST['type_tir'],
            mode_charge=request.POST['mode_charge'],
            niveau=request.POST['niveau'],
            panneau=request.POST['panneau'],
            largeur=request.POST['largeur'],
            nbr_trou_range=request.POST['nbr_trou_range'],
            tranche=request.POST['tranche'],
            profondeur=request.POST['profondeur'],
            dossage=request.POST['dossage'],
            nbr_trou=request.POST['nbr_trou'],
            maille=request.POST['maille'],
            longueur=request.POST['longueur'],
            nbr_range=request.POST['nbr_range'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            fouration.full_clean()
        except ValidationError as e:
            pass
        fouration = Fourations(stock_id=stocks, nbr_range=nbr_range, longueur=longueur, maille=maille,
                          nbr_trou=nbr_trou, dossage=dossage, profondeur=profondeur,
                          tranche=tranche, nbr_trou_range=nbr_trou_range, largeur=largeur, panneau=panneau,observation=observation,
                      niveau=niveau, mode_charge=mode_charge ,type_tir=type_tir,machine=machine,num_com=num_com,mode_tir=mode_tir)
        fouration.save()
        messages.success(request, 'Fourations was created successfully!')
        return redirect('/list1')
    else:

        stocks_list = Stock.objects.all()
        return render(request, 'add1.html' ,  {
                   'stocks': stocks_list,


                   })

@login_required
def show1(request, id):
    fourations= Fourations.objects.get(id=id)
    context = {'fourations': fourations}
    return render(request, 'show1.html', context)




@login_required
def edit1(request, id):
    fourations = Fourations.objects.get(id=id)
    context = {'fourations': fourations}
    return render(request, 'edit1.html', context)


@login_required
def update1(request, id):
    fouration = Fourations.objects.get(id=id)
    fouration.num_com = request.POST['num_com']
    fouration.observation = request.POST['observation']
    fouration.machine = request.POST['machine']
    fouration.mode_tir = request.POST['mode_tir']
    fouration.type_tir = request.POST['type_tir']
    fouration.mode_charge = request.POST['mode_charge']
    fouration.niveau = request.POST['niveau']
    fouration.panneau = request.POST['panneau']
    fouration.largeur = request.POST['largeur']
    fouration.nbr_trou_range = request.POST['nbr_trou_range']
    fouration.tranche = request.POST['tranche']
    fouration.profondeur = request.POST['profondeur']
    fouration.dossage = request.POST['dossage']
    fouration.nbr_trou = request.POST['nbr_trou']
    fouration.maille = request.POST['maille']
    fouration.longueur = request.POST['longueur']
    fouration.nbr_range = request.POST['nbr_range']
    fouration.save()
    messages.success(request, 'Fourations was updated successfully!')
    return redirect('/list1')

@login_required
def delete1(request, id):
    fouration = Fourations.objects.get(id=id)
    fouration.delete()
    messages.error(request, 'Fourations was deleted successfully!')
    return redirect('/list1')



@login_required
def list2(request):
    sautages_list = Sautage.objects.all()
    fourations_list = Fourations.objects.all()
    paginator = Paginator(sautages_list, 5)
    page = request.GET.get('page')
    try:
        sautages = paginator.page(page)
    except PageNotAnInteger:
        sautages = paginator.page(1)
    except EmptyPage:
        sautages = paginator.page(paginator.num_pages)
    return render(request, 'list2.html',
                  {'sautages': sautages,
                   'fourations': fourations_list
                   })

@login_required
def create2(request):
    if request.method == 'POST':
        fouration_id = request.POST.get('fouration')
        fouration = Fourations.objects.get(id=fouration_id)
        type_tir  =  request.POST.get('type_tir')
        case_debut = request.POST.get('case_debut')
        equipe = request.POST.get('equipe')
        son = request.POST.get('son')
        frequence = request.POST.get('frequence')
        vitesse = request.POST.get('vitesse')
        vitesse_vent = request.POST.get('vitesse_vent')
        humiditer = request.POST.get('humiditer')
        temp = request.POST.get('temp')
        taux_abattage = request.POST.get('taux_abattage')
        taux_deplacement = request.POST.get('taux_deplacement')
        nammonix = request.POST.get('nammonix')
        ntovex = request.POST.get('ntovex')
        nartifice = request.POST.get('nartifice')

        sautage = Sautage(
            fouration_id=fouration,
            type_tir=type_tir,
            case_debut=request.POST.get('case_debut'),
            equipe=request.POST.get('equipe'),
            son=request.POST.get('son'),
            frequence=request.POST.get('frequence'),
            vitesse=request.POST.get('vitesse'),
            vitesse_vent=request.POST.get('vitesse_vent'),
            humiditer=request.POST.get('humiditer'),
            temp=request.POST.get('temp'),
            taux_abattage=request.POST.get('taux_abattage'),
            taux_deplacement=request.POST.get('taux_deplacement'),
            nammonix=request.POST.get('nammonix'),
            ntovex=request.POST.get('ntovex'),
            nartifice=request.POST.get('nartifice'),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            sautage.full_clean()
        except ValidationError as e:
            pass
        sautage = Sautage(nartifice=nartifice,ntovex=ntovex,nammonix=nammonix,fouration_id=fouration,type_tir=type_tir,case_debut=case_debut,equipe=equipe,taux_deplacement=taux_deplacement,taux_abattage=taux_abattage,temp=temp,humiditer=humiditer,vitesse_vent=vitesse_vent,vitesse=vitesse,frequence=frequence,son=son)
        sautage.save()
        messages.success(request, 'Sautage was created successfully!')
        return redirect('/list2')
    else:
        fourations_list = Fourations.objects.all()
        return render(request, 'add2.html',  {
                   'fourations': fourations_list
                   })

@login_required
def edit2(request, id):
    sautages = Sautage.objects.get(id=id)
    context = {'sautages': sautages}
    return render(request, 'edit2.html', context)


@login_required
def update2(request, id):
    sautage = Sautage.objects.get(id=id)
    sautage.type_tir = request.POST['type_tir']
    sautage.case_debut = request.POST['case_debut']
    sautage.equipe = request.POST['equipe']
    sautage.son = request.POST['son']
    sautage.frequence = request.POST['frequence']
    sautage.vitesse = request.POST['vitesse']
    sautage.vitesse_vent = request.POST['vitesse_vent']
    sautage.humiditer = request.POST['humiditer']
    sautage.temp = request.POST['temp']
    sautage.taux_abattage = request.POST['taux_abattage']
    sautage.taux_deplacement = request.POST['taux_deplacement']
    sautage.nammonix = request.POST['nammonix']
    sautage.ntovex = request.POST['ntovex']
    sautage.nartifice = request.POST['nartifice']
    sautage.save()
    messages.success(request, 'Sautage was updated successfully!')
    return redirect('/list2')
@login_required
def delete2(request, id):
    sautage = Sautage.objects.get(id=id)
    sautage.delete()
    messages.error(request, 'Sautage was deleted successfully!')
    return redirect('/list2')




@login_required
def list4(request):
    avances_list = Avance.objects.all()
    fourations_list = Fourations.objects.all()
    paginator = Paginator(avances_list, 5)
    page = request.GET.get('page')
    try:
        avances = paginator.page(page)
    except PageNotAnInteger:
        avances = paginator.page(1)
    except EmptyPage:
        avances = paginator.page(paginator.num_pages)
    return render(request, 'list4.html', {'avances': avances,
                                          'fourations':fourations_list})

@login_required
def create4(request):
    if request.method == 'POST':
        fouration_id = request.POST.get('fouration')
        fouration = Fourations.objects.get(id=fouration_id)
        avance_foration = request.POST.get('avance_foration')
        machine = request.POST.get('machine')
        avance = Avance(
            fouration_id=fouration,
            avance_foration=request.POST['avance_foration'],
            machine=request.POST['machine'],

            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            avance.full_clean()
        except ValidationError as e:
            pass
        avance = Avance(fouration_id=fouration, avance_foration=avance_foration,machine=machine)
        avance.save()
        messages.success(request, 'Avance was created successfully!')
        return redirect('/list4')
    else:
        fourations_list = Fourations.objects.all()
        return render(request, 'add4.html' , {
                   'fourations': fourations_list
                   })

@login_required
def edit4(request, id):
    avances = Avance.objects.get(id=id)
    context = {'avances': avances}
    return render(request, 'edit4.html', context)


@login_required
def update4(request, id):
    avance = Avance.objects.get(id=id)
    avance.avance_foration = request.POST['avance_foration']

    avance.save()
    messages.success(request, 'Avance was updated successfully!')
    return redirect('/list4')

@login_required
def delete4(request, id):
    avance = Avance.objects.get(id=id)
    avance.delete()
    messages.error(request, 'Avance was deleted successfully!')
    return redirect('/list4')




@login_required
def list5(request):
    stocks_list = Stock.objects.all()
    paginator = Paginator(stocks_list, 5)
    page = request.GET.get('page')
    try:
        stocks = paginator.page(page)
    except PageNotAnInteger:
        stocks = paginator.page(1)
    except EmptyPage:
        stocks = paginator.page(paginator.num_pages)
    return render(request, 'list5.html', {'stocks': stocks})

@login_required
def create5(request):
    if request.method == 'POST':
        stock = Stock(
            num_stock=request.POST['num_stock'],
            ammonix=request.POST['ammonix'],
            tovex=request.POST['tovex'],
            raccord42ms=request.POST['raccord42ms'],
            raccord17ms=request.POST['raccord17ms'],
            raccord25ms=request.POST['raccord25ms'],
            ligne_tir=request.POST['ligne_tir'],
            aei=request.POST['aei'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            stock.full_clean()
        except ValidationError as e:
            pass
        stock.save()
        messages.success(request, 'Stock was created successfully!')
        return redirect('/list5')
    else:
        return render(request, 'add5.html')

@login_required
def edit5(request, id):
    stocks = Stock.objects.get(id=id)
    context = {'stocks': stocks}
    return render(request, 'edit5.html', context)


@login_required
def update5(request, id):
    stock = Stock.objects.get(id=id)
    stock.num_stock = request.POST['num_stock']
    stock.ammonix = request.POST['ammonix']
    stock.tovex = request.POST['tovex']
    stock.raccord42ms = request.POST['raccord42ms']
    stock.raccord17ms = request.POST['raccord17ms']
    stock.raccord25ms = request.POST['raccord25ms']
    stock.ligne_tir = request.POST['ligne_tir']
    stock.aei = request.POST['aei']
    stock.save()
    messages.success(request, 'Stock was updated successfully!')
    return redirect('/list5')

@login_required
def delete5(request, id):
    stock = Stock.objects.get(id=id)
    stock.delete()
    messages.error(request, 'Stock was deleted successfully!')
    return redirect('/list5')








@login_required
def fileupload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        document = Document(
            description=request.POST['description'],
            document=myfile.name,
            uploaded_at=datetime.datetime.now(), )
        document.save()
        messages.success(request, 'Member was created successfully!')
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return redirect('fileupload')
    else:
        documents = Document.objects.order_by('-uploaded_at')[:3]
        context = {'documents': documents}
    return render(request, 'fileupload.html', context)


@login_required
def ajax(request):
    if request.method == 'POST':
        if request.is_ajax():
            data = Ajax(
                text=request.POST['text'],
                search=request.POST['search'],
                email=request.POST['email'],
                telephone=request.POST['telephone'],
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
            )
            data.save()
            astr = "<html><b> you sent an ajax post request </b> <br> returned data: %s</html>" % data
            return JsonResponse({'data': 'success'})
    else:
        ajax_list = Ajax.objects.order_by('-created_at')
        context = {'ajax_list': ajax_list}
    return render(request, 'ajax.html', {'ajax_list': ajax_list})


@csrf_protect
def getajax(request):
    if request.method == 'GET':
        if request.is_ajax():
            data = Ajax.objects.order_by('-created_at').first()
            created = data.created_at.strftime('%m-%d-%Y %H:%M:%S')
            datas = {"id": data.id, "text": data.text, "search": data.search, "email": data.email,
                     "telephone": data.telephone, "created_at": created}
            return JsonResponse(datas)
    else:
        return JsonResponse({'data': 'failure'})


@csrf_protect
def ajax_delete(request):
    if request.method == 'GET':
        if request.is_ajax():
            id = request.GET['id']
            ajax = Ajax.objects.get(id=id)
            ajax.delete()
            return JsonResponse({'data': 'success'})
    else:
        return JsonResponse({'data': 'failure'})


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                is_staff=True,
                is_active=True,
                is_superuser=True,
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def register_success(request):
    return render(request, 'success.html')

@login_required
def users(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list, 5)
    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request, 'users.html', {'users': users})

@login_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/users')

@login_required
def upload_csv(request):
    if 'GET' == request.method:
        # csv_list = CsvUpload.objects.all()
        # paginator = Paginator(csv_list, 7)
        # page = request.GET.get('page')
        # try:
        #     csvdata = paginator.page(page)
        # except PageNotAnInteger:
        #     csvdata = paginator.page(1)
        # except EmptyPage:
        #     csvdata = paginator.page(paginator.num_pages)
        # return render(request, 'upload_csv.html', {'csvdata': csvdata})
        csvdata = CsvUpload.objects.all()
        context = {'csvdata': csvdata}
        return render(request, 'upload_csv.html', context)
    try:
        csv_file = request.FILES["csv_file"]

        if len(csv_file) == 0:
            messages.error(request, 'Empty File')
            return render(request, 'upload_csv.html')

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return render(request, 'upload_csv.html')

        if csv_file.multiple_chunks():
            messages.error(request, 'Uploaded file is too big (%.2f MB).' % (csv_file.size / (1000 * 1000),))
            return render(request, 'upload_csv.html')

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")
        for index, line in enumerate(lines):
            fields = line.split(",")
            if index == 0:
                if (fields[0] == 'name') and (fields[1] == 'description') and (fields[2] == 'end_date') and (
                        fields[3] == 'notes'):
                    pass
                else:
                    messages.error(request, 'File is not Correct Headers')
                    return render(request, 'upload_csv.html')
                    break
            else:
                print(index)
                if (len(fields[0]) != 0) and (len(fields[1]) != 0) and (len(fields[2]) != 0) and (len(fields[3]) != 0):
                    data = CsvUpload(
                        name=fields[0],
                        description=fields[1],
                        end_date=datetime.datetime.now(),
                        notes=fields[3]
                    )
                    data.save()
        messages.success(request, "Successfully Uploaded CSV File")
        return redirect('/upload/csv/')

    except Exception as e:
        messages.error(request, "Unable to upload file. " + e)
        return redirect('/upload/csv/')


@login_required
def changePassword(request):
    print('changepasword')
    return render(request, 'change_password.html')


@login_required
def deleteFiles(request, id):
    file = Document.objects.get(id=id)
    file.delete()
    messages.error(request, 'User was deleted successfully!')
    return redirect('/fileupload')


@login_required
def list7(request):
    pfourations_list = Pfourations.objects.all()
    paginator = Paginator(pfourations_list, 5)
    page = request.GET.get('page')
    try:
        pfourations = paginator.page(page)
    except PageNotAnInteger:
        pfourations = paginator.page(1)
    except EmptyPage:
        pfourations = paginator.page(paginator.num_pages)
    return render(request, 'list7.html', {'pfourations': pfourations})

@login_required
def create7(request):
    if request.method == 'POST':
        pfouration = Pfourations(
            densite_r=request.POST['densite_r'],
            niveau=request.POST['niveau'],
            panneau=request.POST['panneau'],
            largeur=request.POST['largeur'],
            tranche=request.POST['tranche'],
            diametre=request.POST['diametre'],
            de=request.POST['de'],
            hauteur=request.POST['hauteur'],
            longueur=request.POST['longueur'],
            espacement=request.POST['espacement'],
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now(), )
        try:
            pfouration.full_clean()
        except ValidationError as e:
            pass
        pfouration.save()
        messages.success(request, 'Fourations was created successfully!')
        return redirect('/list7')
    else:
        return render(request, 'add7.html')

@login_required
def edit7(request, id):
    pfourations = Pfourations.objects.get(id=id)
    context = {'pfourations': pfourations}
    return render(request, 'edit7.html', context)


@login_required
def update7(request, id):
    pfouration = Pfourations.objects.get(id=id)

    pfouration.niveau = request.POST['niveau']
    pfouration.panneau = request.POST['panneau']
    pfouration.largeur = request.POST['largeur']
    pfouration.diametre = request.POST['diametre']
    pfouration.tranche = request.POST['tranche']
    pfouration.de = request.POST['de']
    pfouration.espacement = request.POST['espacement']
    pfouration.hauteur = request.POST['hauteur']
    pfouration.longueur = request.POST['longueur']
    pfouration.save()
    messages.success(request, 'Fourations was updated successfully!')
    return redirect('/list7')

@login_required
def delete7(request, id):
    pfouration = Pfourations.objects.get(id=id)
    pfouration.delete()
    messages.error(request, 'Fourations was deleted successfully!')
    return redirect('/list7')
