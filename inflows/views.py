from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from . import models
from . import form


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Inflows
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflows'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset


class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Inflows
    template_name = 'inflow_create.html'
    form_class = form.InflowForm
    success_url = reverse_lazy('inflow_list')
    permission_required = 'inflows.add_inflows'


class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Inflows
    template_name = 'inflow_detail.html'
    permission_required = 'inflows.view_inflows'
