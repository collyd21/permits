from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Mewp
from .forms import MewpForm

# Create your views here.

@login_required
def mewp(request):
    """ A view to return the MEWP page """
    mewps = Mewp.objects.all()

    context = {
        'mewps': mewps,
    }

    return render(request, 'mewp.html', context)

@login_required
def add_checksheet(request):
    """ A view to add a new checksheet """
    if request.method == 'POST':
        checksheet = MewpForm(request.POST)
        if checksheet.is_valid():
            checksheet.save()
            messages.add_message(request, messages.INFO, 'Checksheet Submitted.')
            return redirect(reverse('mewp'))
    else:
        checksheet = MewpForm()
        
    return render(request, 'add_checksheet.html', {'form': checksheet})

def view_checksheet(request, id):
    """ A view to view a checksheet """
    checksheet = get_object_or_404(Mewp, pk=id)
    
    context = {
        'checksheet': checksheet,
    }

    return render(request, 'view_checksheet.html', context)


@login_required
def delete_checksheet(request, id):
    """ Delete an individual checksheet """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admin can do that.')
        return redirect(reverse('mewp'))

    checksheet = get_object_or_404(Mewp, pk=id)
    checksheet.delete()
    messages.success(request, 'Checksheet successfully deleted!')

    return redirect(reverse('mewp'))