from django.shortcuts import render
from .models import C19Autoaval, C19Cadastro, C19Teste
from .forms import C19CadastroForm, C19TesteForm, C19AutoAvalForm

# Create your views here.

# Create your views here.
def c19menu(request):
    request.session['idsenha'] = '747'
    return render(request,"menu/menuc19.html")

def c19cadastro_list(request):
    context = {'c19cadastro_list':C19Cadastro.objects.all()}
    return render(request,"c19cadastro/c19cadastro_list.html",context)

def c19cadastro_form(request,idcad19=0):
    if request.method == "GET":
       if idcad19 == 0:
          form = C19CadastroForm()
       else:
          c19cadastro = C19Cadastro.objects.get(pk_c19_cadastro=idcad19)
          form = C19CadastroForm(instance=c19cadastro)
       return render(request,"c19cadastro/c19cadastro_form.html",{'form':form})
    else:
        if idcad19 == 0:
           form = C19CadastroForm(request.POST)
        else:
           c19cadastro = C19Cadastro.objects.get(pk_c19_cadastro=idcad19)
           form = C19CadastroForm(request.POST,instance=c19cadastro)
        if form.is_valid():
           if request.session.has_key('idsenha'):
              idsenha = request.session.get('idsenha')
           
           new_c19 = form.save(commit=False)
           new_c19.id_criado = idsenha
           new_c19.save()
           return redirect('c19cadastro_list/')
        else:
           return render(request,"c19cadastro/c19cadastro_form.html",{'form':form})

def c19cadastro_exclui(request,idcad19):
    c19cadastro = C19Cadastro.objects.get(pk_c19_cadastro=idcad19)
    if request.session.has_key('idsenha'):
       idsenha = request.session.get('idsenha')
    
    c19cadastro.id_cancel = idsenha
    c19cadastro.dt_cancel = datetime.now()
    c19cadastro.save()
    return redirect('c19cadastro_list/')

def c19teste_list(request):
    context = {'c19teste_list':C19Teste.objects.all()}
    return render(request,"c19teste/c19teste_list.html",context)

def c19teste_form(request,idtst19=0):
    if request.method == "GET":
       if idtst19 == 0:
          form = C19TesteForm()
       else:
          c19teste = C19Teste.objects.get(pk_c19_teste=idtst19)
          form = C19TesteForm(instance=c19teste)
       return render(request,"c19teste/c19teste_form.html",{'form':form})
    else:
        if idtst19 == 0:
           form = C19TesteForm(request.POST)
        else:
           c19teste = C19Teste.objects.get(pk_c19_teste=idtst9)
           form = C19TesteForm(request.POST,instance=c19teste)
        if form.is_valid():
           if request.session.has_key('idsenha'):
              idsenha = request.session.get('idsenha')
           
           new_t19 = form.save(commit=False)
           new_t19.id_criado = idsenha
           new_t19.save()
           return redirect('c19teste_list/')
        else:
           return render(request,"c19teste/c19teste_form.html",{'form':form})

def c19teste_exclui(request,idtst19):
    c19teste = C19Teste.objects.get(pk_c19_teste=idcad19)
    if request.session.has_key('idsenha'):
       idsenha = request.session.get('idsenha')
    
    c19teste.id_cancel = idsenha
    c19test.dt_cancel = datetime.now()
    c19teste.save()
    return redirect('c19teste_list/')


def c19autoaval_list(request):
    context = {'c19autoaval_list':C19Autoaval.objects.all()}
    return render(request,"c19autoaval/c19autoaval_list.html",context)

def c19autoaval_form(request,idaut19=0):
    if request.method == "GET":
       if idaut19 == 0:
          form = C19AutoAvalForm()
       else:
          c19autoaval = C19Autoaval.objects.get(pk_c19_autoaval=idaut19)
          form = C19AutoAvalForm(instance=c19autoaval)
       return render(request,"c19autoaval/c19autoaval_form.html",{'form':form})
    else:
        if idaut19 == 0:
           form = C19AutoAvalForm(request.POST)
        else:
           c19autoaval = C19Autoaval.objects.get(pk_c19_autoaval=idaut9)
           form = C19AutoAvalForm(request.POST,instance=c19autoaval)
        if form.is_valid():
           if request.session.has_key('idsenha'):
              idsenha = request.session.get('idsenha')
           
           new_a19 = form.save(commit=False)
           new_a19.id_criado = idsenha
           new_a19.save()
           return redirect('c19autoaval_list/')
        else:
           return render(request,"c19autoaval/c19autoaval_form.html",{'form':form})

def c19autoaval_exclui(request,idaut19):
    c19autoaval= C19Cadastro.objects.get(pk_c19_autoaval=idaut19)
    if request.session.has_key('idsenha'):
       idsenha = request.session.get('idsenha')
    
    c199autoaval.id_cancel = idsenha
    c19autoaval.dt_cancel = datetime.now()
    c19autoaval.save()
    return redirect('c19autoaval_list/')