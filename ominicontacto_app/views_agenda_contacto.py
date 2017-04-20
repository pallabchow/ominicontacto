# -*- coding: utf-8 -*-

from __future__ import unicode_literals


from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView
)
from django.views.generic.detail import DetailView
from ominicontacto_app.models import AgendaContacto, Contacto, AgenteProfile
from ominicontacto_app.forms import AgendaContactoForm


class AgendaContactoCreateView(CreateView):

    template_name = 'agenda_contacto/create_agenda_contacto.html'
    model = AgendaContacto
    context_object_name = 'agendacontacto'
    form_class = AgendaContactoForm

    def get_initial(self):
        initial = super(AgendaContactoCreateView, self).get_initial()
        contacto = Contacto.objects.get(pk=self.kwargs['pk_contacto'])
        agente = AgenteProfile.objects.get(pk=self.kwargs['id_agente'])
        initial.update({'contacto': contacto,
                        'agente': agente})
        return initial

    def get_context_data(self, **kwargs):
        context = super(
            AgendaContactoCreateView, self).get_context_data(**kwargs)
        context['contacto'] = Contacto.objects.get(pk=self.kwargs['pk_contacto'])
        return context

    def get_success_url(self):
        return reverse(
            'agenda_contacto_detalle', kwargs={'pk': self.object.pk})


class AgendaContactoDetailView(DetailView):
    template_name = 'agenda_contacto/agenda_detalle.html'
    model = AgendaContacto

    def get_context_data(self, **kwargs):
        context = super(
            AgendaContactoDetailView, self).get_context_data(**kwargs)
        return context
