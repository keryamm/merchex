from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from listings.models import Listing



def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django</h1>
        <p<Mes groupes sont : </p>
        <ul>
            <li>{bands[0].name}</li>
            <li>{bands[1].name}</li>
            <li>{bands[2].name}</li>            
        </ul>
""")


def about(request):
    return HttpResponse("<h1>A propos</h1><p>Nous adorons merch !</p>")


def listings(request):
    listing = Listing.objects.all()
    return HttpResponse(f"""
            <h1>Hello Django</h1>
            <p>Les titres sont : </p>
            <ul>
                <li>{listing[0].title}</li>
                <li>{listing[1].title}</li>
                <li>{listing[2].title}</li> 
                <li>{listing[3].title}</li>          
            </ul>
""")


def contact(request):
    return HttpResponse("<h1></h1><p></p>")
