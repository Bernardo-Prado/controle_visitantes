from django.contrib import messages
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
    )

from visitantes.models import Visitante
from visitantes.forms import (
    VisitanteForm, AutorizaVisitanteForm
)

from django.utils import timezone

def registrar_visitante(request):

    form = VisitanteForm()

    if request.method == "POST":
        form =  VisitanteForm(request.POST)

        # Valida o formulário, salva o visitante, seta o atributo "registrado_por"
        # Salva o visitante no banco de dados, redireciona ele para a pagina inicial da dashboard
        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.registrado_por = request.user.porteiro
            visitante.save()

            messages.success(request,"Visitante registrado com sucesso!!")

            return redirect("index")


    context = {
        "nome_pagina": "Registrar visitante",
        "form": form
    }

    return render(request, "registrar_visitante.html", context)

def informacoes_visitante(request, id):

    visitante = get_object_or_404(
        Visitante,
        id=id
    )

    form = AutorizaVisitanteForm()

    if request.method == "POST":
        form = AutorizaVisitanteForm(
            request.POST,
            instance=visitante
        )

        if form.is_valid():
            visitante = form.save(commit=False)

            visitante.status = "EM_VISITA"
            visitante.horario_autorizacao = timezone.now()

            visitante.save()

            messages.success(
                request,
                "Entrada de visitante autorizada com sucesso"
            )

            return redirect("index")

    context = {
        "nome_pagina": "Informações de visitante",
        "visitante": visitante,
        "form": form
    }

    return render(request, "informacoes_visitante.html", context)
