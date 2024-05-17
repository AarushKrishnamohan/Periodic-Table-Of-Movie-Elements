from django.shortcuts import render
from .models import MovieElement

def index(request):
    elements = MovieElement.objects.all()
    editing_techniques = MovieElement.objects.filter(category="editing-techniques")
    scene_transitions = MovieElement.objects.filter(category="scene-transitions")
    action_timing = MovieElement.objects.filter(category="action-timing")
    imagery_style = MovieElement.objects.filter(category="imagery-style")
    story_structure = MovieElement.objects.filter(category="story-structure")
    character_dialouge = MovieElement.objects.filter( category="character-dialogue")
    plot_devices = MovieElement.objects.filter(category="plot-devices")
    sound_audio = MovieElement.objects.filter(category="sound-audio")
    close_ups_shots = MovieElement.objects.filter(category="close-ups-shots")
    movement_flow = MovieElement.objects.filter(category="movement-flow")
    audience_engagement = MovieElement.objects.filter(category="audience-engagement")
    endings_conclusions = MovieElement.objects.filter(category="endings-conclusions")
    angles_perspectives = MovieElement.objects.filter(category="angles-perspectives")


    context = {
        'elements': elements,
        'editing_techniques': editing_techniques,
        'scene_transitions': scene_transitions,
        'action_timing': action_timing,
        'imagery_style': imagery_style,
        'story_structure': story_structure,
        'character_dialouge': character_dialouge,
        'plot_devices': plot_devices,
        'sound_audio': sound_audio,
        'close_ups_shots': close_ups_shots,
        'movement_flow': movement_flow,
        'audience_engagement': audience_engagement,
        'endings_conclusions': endings_conclusions,
        'angles_perspectives': angles_perspectives,
    }
    return render(request, 'index.html', context)
