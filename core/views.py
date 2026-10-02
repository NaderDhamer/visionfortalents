from django.shortcuts import render, get_object_or_404
from .models import WorkPackage, SABMember, ConsortiumPartner, TrainingProgram, ContactSubmission
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from activities.models import Event, BenchmarkingEntry
def home(request):
    work_packages = WorkPackage.objects.all()
    latest_events = Event.objects.all()[:3]
    latest_training = TrainingProgram.objects.all()[:3]
    latest_benchmarks = BenchmarkingEntry.objects.all()[:3]
    
    # DEBUG
    print(f"DEBUG home view: events={list(latest_events)}, training={list(latest_training)}, benchmarks={list(latest_benchmarks)}")
    
    return render(request, 'core/home.html', {
        'work_packages': work_packages,
        'latest_events': latest_events,
        'latest_training': latest_training,
        'latest_benchmarks': latest_benchmarks,
    })

def about(request):
    return render(request, 'core/about.html')


def training(request):
    programs_list = TrainingProgram.objects.all()
    paginator = Paginator(programs_list, 6)  # 6 items per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'core/training.html', {'page_obj': page_obj}) 


def work_package_detail(request, slug):
    work_package = get_object_or_404(WorkPackage, slug=slug)
    return render(request, 'core/work_package_detail.html', {'work_package': work_package})


def sab_members(request):
    members = SABMember.objects.all()
    return render(request, 'core/sab_members.html', {'members': members})


def consortium(request):
    partners = ConsortiumPartner.objects.all()
    return render(request, 'core/consortium.html', {'partners': partners})





def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            submission = form.save()
            
            # Send email (console output in dev, real SMTP in production)
            send_mail(
                subject=f"New contact form submission: {submission.subject}",
                message=f"From: {submission.name} ({submission.email})\n\n{submission.message}",
                from_email='noreply@visionfortalents.com',
                recipient_list=['visionproject@pasteur.utm.tn'],  # real project email
            )
            
            # Show success message
            messages.success(request, 'Thank you! Your message has been received.')
            return redirect('core:contact')
    else:
        form = ContactForm()
    
    return render(request, 'core/contact.html', {'form': form})  