from django.core.management.base import BaseCommand
from elements.models import MovieElement

class Command(BaseCommand):
    help = 'Populate the MovieElement table with predefined data'

    def handle(self, *args, **kwargs):
        elements = [
            {"symbol": "Sp", "name": "Spliced in 1/24 second clip or image", "definition": "Inserting a still image or clip into a video in order to tell the audience what a character is thinking at a certain moment.", "category": "editing-techniques"},
            {"symbol": "Jc", "name": "Jump Cuts", "definition": "An editing cut that breaks a single continuous sequential shot into two parts, creating the effect of jumping forward in time.", "category": "editing-techniques"},
            {"symbol": "Sr", "name": "Speed Ramp", "definition": "Gradual increase or decrease in speed within a shot.", "category": "editing-techniques"},
            {"symbol": "Df", "name": "Double fade/Triple shot", "definition": "A dissolve made by double printing a fade-in of the incoming scene with a fade-out of the outgoing scene.", "category": "editing-techniques"},
            {"symbol": "Fw", "name": "Fade to white", "definition": "Fading to white at the end of the movie or scene as opposed to fading to black.", "category": "scene-transitions"},
            {"symbol": "Ot", "name": "One continuous take 'oner'", "definition": "A shot with a duration longer than the conventional editing pace either of the film itself or of films in general.", "category": "scene-transitions"},
            {"symbol": "Sas", "name": "Screen aspect ratio shift", "definition": "A change in the ratio of width and height of the image for logistical or metaphorical reasons.", "category": "scene-transitions"},
            {"symbol": "Sb", "name": "Sound Bridge", "definition": "A transitional device used in film to connect one visual scene to another through sound.", "category": "scene-transitions"},
            {"symbol": "Cm", "name": "Cutting to Music", "definition": "Editing technique that times cuts with the beat of a song.", "category": "action-timing"},
            {"symbol": "Ca", "name": "Cutting on Action", "definition": "Editing practice of cutting on either action or camera movement.", "category": "action-timing"},
            {"symbol": "Pt", "name": "Putting a timer on characters", "definition": "Placing a visible timer or countdown in the scene to indicate time constraints for characters.", "category": "action-timing"},
            {"symbol": "Mo", "name": "Montage", "definition": "Series of short shots or clips into one sequence, often, but not always, set to music.", "category": "action-timing"},
            {"symbol": "Ms", "name": "Macro shot (Eye shot)", "definition": "Extreme close-up photography.", "category": "close-ups-shots"},
            {"symbol": "Ss", "name": "Silhouette Shot", "definition": "A silhouette is created by a subject photographed against a dark background.", "category": "close-ups-shots"},
            {"symbol": "Fs", "name": "Face Framed in Shadow", "definition": "Using a stark contrast between dark and light in an image, usually for dramatic effect.", "category": "close-ups-shots"},
            {"symbol": "Is", "name": "Insert Shot", "definition": "A shot focusing the viewer’s attention on a specific detail within a scene.", "category": "close-ups-shots"},
            {"symbol": "Vm", "name": "Visual motif", "definition": "A repeating idea told through imagery.", "category": "imagery-style"},
            {"symbol": "Oi", "name": "Otherworldly Imagery", "definition": "Imagery that could not exist within reality, often remembered for its technical difficulty and narrative impossibility.", "category": "imagery-style"},
            {"symbol": "Gm", "name": "Graphic Match", "definition": "Occurs when the shapes, colors, and/or overall movement of two shots match in composition.", "category": "imagery-style"},
            {"symbol": "Mp", "name": "Movie Poster from a still frame", "definition": "Creating a movie poster from a still frame of the film.", "category": "imagery-style"},
            {"symbol": "Ct", "name": "Cinematic Titles", "definition": "Incorporating video in text as a visual effect.", "category": "imagery-style"},
            {"symbol": "Da", "name": "Dutch Angle", "definition": "A skewed camera angle indicating the character is off in some way.", "category": "angles-perspectives"},
            {"symbol": "So", "name": "Subjective versus objective point of view", "definition": "Scenes that contrast a subjective point of view with an objective one.", "category": "angles-perspectives"},
            {"symbol": "Fr", "name": "Focus Racking", "definition": "Separating foreground and background by shifting focus.", "category": "angles-perspectives"},
            {"symbol": "En", "name": "Elliptical narrative", "definition": "The narrative device of omitting a portion of the sequence of events, allowing the reader to fill in the narrative gaps.", "category": "story-structure"},
            {"symbol": "Co", "name": "Cold Open and/or Nonlinear storytelling", "definition": "Jumping directly into a story at the beginning of the show before the title sequence or opening credits are shown.", "category": "story-structure"},
            {"symbol": "Fl", "name": "Flashback/Forward (x2)", "definition": "Flashback within a flashback or flash-forward within a flash-forward.", "category": "story-structure"},
            {"symbol": "Dt", "name": "Dialogue as the title", "definition": "The title of the film is said in the film as dialogue, excluding a character’s name as the title.", "category": "character-dialogue"},
            {"symbol": "Id", "name": "Incomprehensible dialogue/dialect", "definition": "Dialogue that is hard to understand either because of inadequate sound recording or purposeful dialect that is part of a character.", "category": "character-dialogue"},
            {"symbol": "Bi", "name": "Banger Character Introduction", "definition": "A memorable character introduction.", "category": "character-dialogue"},
            {"symbol": "Pa", "name": "Protagonist to Antagonist shift", "definition": "The antagonist becomes the protagonist and vice versa.", "category": "character-dialogue"},
            {"symbol": "Th", "name": "The Heavy", "definition": "The character that provides the most conflict in the story.", "category": "character-dialogue"},
            {"symbol": "Cg", "name": "Chekov’s Gun", "definition": "A dramatic principle that suggests details within a story or play will contribute to the overall narrative.", "category": "plot-devices"},
            {"symbol": "Mg", "name": "MacGuffin", "definition": "A plot device that motivates the characters.", "category": "plot-devices"},
            {"symbol": "Ve", "name": "Verisimilitude", "definition": "The appearance of being true or real. A film’s believability or ability to convey truth.", "category": "plot-devices"},
            {"symbol": "Fw", "name": "Fish out of water", "definition": "A character removed from their normal environment who has to adapt to a new one.", "category": "plot-devices"},
            {"symbol": "Ef", "name": "Ending with a freeze frame", "definition": "Ending a scene or the movie with a still image.", "category": "endings-conclusions"},
            {"symbol": "Ae", "name": "Ambiguous ending", "definition": "Any ending in which the outcome of the story is left ambiguous and open-ended.", "category": "endings-conclusions"},
            {"symbol": "Ce", "name": "Credits over ending of film", "definition": "Displaying the credits over the final scenes of the film.", "category": "endings-conclusions"},
            {"symbol": "Bw", "name": "Breaking the fourth wall", "definition": "The convention in which an invisible, imagined wall separating the audience from the actors is broken.", "category": "audience-engagement"},
            {"symbol": "Rj", "name": "Rule of 3s for Jokes", "definition": "The theory that effective jokes revolve around the number 3.", "category": "audience-engagement"},
            {"symbol": "St", "name": "Show & Tell", "definition": "The process of both telling and showing within a scene.", "category": "audience-engagement"},
            {"symbol": "Lr", "name": "Literary reference", "definition": "Any reference to literature within a film.", "category": "audience-engagement"},
            {"symbol": "Nl", "name": "Needle-drops and Leitmotifs", "definition": "Using a pre-existing song in a movie and recurring musical phrases associated with themes or characters.", "category": "sound-audio"},
            {"symbol": "Ws", "name": "The Wilhelm Scream", "definition": "A stock scream that has been used in numerous films and TV series.", "category": "sound-audio"},
            {"symbol": "Wt", "name": "Walk & Talk", "definition": "Involves both walking and talking at the same time, with the camera in motion with the actors.", "category": "movement-flow"},
            {"symbol": "Io", "name": "Indoor to outdoor scene", "definition": "One continuous scene that begins indoors and ends outdoors (or vice versa or at the same time).", "category": "movement-flow"},
            {"symbol": "Mm", "name": "Motivated Camera Movement", "definition": "Camera movement that has a purpose or motivation within the scene.", "category": "movement-flow"},
            {"symbol": "Rs", "name": "Reshoots", "definition": "Reshooting scenes out of necessity.", "category": "movement-flow"}
        ]

        for element in elements:
            MovieElement.objects.update_or_create(
                symbol=element['symbol'],
                defaults={
                    'name': element['name'],
                    'definition': element['definition'],
                    'category': element['category'],  # Ensure category is included
                    'example': ''
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully populated the MovieElement table'))
