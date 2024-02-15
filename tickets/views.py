
from django.db import models
from django.utils import timezone
from django.shortcuts import redirect

from django.shortcuts import render, get_object_or_404
from .models import Ticket,Note

def ticket_list(request, status='Open'):
    tickets = Ticket.objects.filter(status=status)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets, 'status': status})

def ticket_closed(request, status='Closed'):
    tickets = Ticket.objects.filter(status=status)
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets, 'status': status})

def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

def ticket_add(request):
    return render(request,'tickets/ticket_add.html')

def create_ticket(request):
    name = request.POST['name']
    phone = request.POST['phone']
    email = request.POST['email']
    city = request.POST['city']
    state = request.POST['state']
    description = request.POST['description']
    category = request.POST['category']
    notes_text = request.POST['notes']

    # Create a new Note instance
    note = Note.objects.create(text=notes_text)

    # Create a new Ticket instance and associate the note using set()
    ticket = Ticket.objects.create(
        name=name,
        phone=phone,
        email=email,
        city=city,
        state=state,
        description=description,
        category=category
    )
    ticket.notes.set([note])
    ticket.last_modified_date = timezone.now()
    return redirect("/")

def ticket_edit(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    return render(request,'tickets/ticket_edit.html', {'ticket': ticket})

def update_ticket(request,pk):
    name=request.POST['name']
    phone=request.POST['phone']
    email=request.POST['email']
    city=request.POST['city']
    state=request.POST['state']
    description=request.POST['description']
    category=request.POST['category']
    status=request.POST['status']
    notes=request.POST['notes']
    ticket=Ticket.objects.get(pk=pk)
    ticket.name=name
    ticket.phone=phone
    ticket.email=email
    ticket.city=city
    ticket.state=state
    ticket.description=description
    ticket.category=category
    ticket.status=status
    new_note = Note.objects.create(text=notes)

    # Retrieve the existing notes and append the new note
    existing_notes = list(ticket.notes.all())
    existing_notes.append(new_note)

    # Set the updated set of notes for the ticket
    ticket.notes.set(existing_notes)
    ticket.last_modified_date = timezone.now()
    ticket.save()
    return redirect("/")

def search(request):
    query = request.GET.get('q', '')
    tickets = Ticket.objects.filter(
        models.Q(phone__icontains=query) |  # Search by Phone
        models.Q(email__icontains=query) |  # Search by Email
        models.Q(category__icontains=query)  # Search by Category
    )

    context = {
        'tickets': tickets,
        'query': query,
    }

    return render(request, 'tickets/ticket_list.html', context)
