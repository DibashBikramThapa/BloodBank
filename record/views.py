from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView,DetailView,UpdateView
from record.models import History
from accounts.models import Donor
from .import historyform

from braces.views import SelectRelatedMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class HomeView(ListView):
    model = Donor

    def get_queryset(self):
        return Donor.objects.order_by('-user')

    template_name='record/index.html'

@login_required()
def CreateHistoryForm(request):
    if request.method == 'POST':
        history_form = historyform.HistroyForm(data=request.POST)

        if history_form.is_valid():
            historycheck=history_form.save(commit=False)
            history=History.objects.get_or_create(
                        user=request.user,
                        lastdonateddate=historycheck.lastdonateddate)
            return redirect("record:historylist")
        else:
            print(history_form.errors)
    else:
        history_form=historyform.HistroyForm()
    context={'history_form':history_form}
    return render(request,'record/history_form.html',context)


class HistoryView(LoginRequiredMixin, ListView):
    model = History
    template_name='record/historylist.html'

    def get_queryset(self):
        return History.objects.order_by('-lastdonateddate')

class ProfileDetailView(LoginRequiredMixin, SelectRelatedMixin, DetailView):
    model = History
    template_name='record/profiledetail.html'
    select_related=('user',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            user__username__iexact=self.kwargs.get('username')
        )

class HistoryUpdateView(LoginRequiredMixin, SelectRelatedMixin,UpdateView):
    login_url='/login'
    redirect_field_name='record/historylist.html'
    template_name='record/profile_form.html'
    select_related=('user',)

    model = History
    form_class=historyform.HistroyForm
