from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.shortcuts import reverse, redirect, render
from django.http.response import JsonResponse


def index(request):
    return HttpResponse("Index Page remaining")