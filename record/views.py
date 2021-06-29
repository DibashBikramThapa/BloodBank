from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from django.views.generic import ListView,CreateView
from record.models import History
from accounts.models import Donor
from .import historyform

from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    model = Donor

    def get_queryset(self):
        return Donor.objects.order_by('-user')

    template_name='record/index.html'


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
    return render(request,'record/createhistory.html',context)


class HistoryView(ListView):
    model = History
    template_name='record/historylist.html'

    def get_queryset(self):
        return History.objects.order_by('-lastdonateddate')
