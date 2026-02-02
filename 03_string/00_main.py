# string in python 

# print("hello , sunil bhai") 

# Quotes Insise quotes 

# print(" He is the 'politician' of our city!! ") 

# assign string to a variable 

x = " hello" 
n = "sunil narayan" 

# print(f"{x} , {n}") 

# multiline string 

s = """ In the glass-walled labs of Asterion Institute of Sciences, where petri dishes glowed softly under incubators and lines of code pulsed on dark screens, Kiran first noticed Mira. She sat alone at a workstation, headphones on, her fingers moving fast as if she were coaxing patterns out of chaos on the monitor. The display showed sprawling networks of molecules and numbers, but Kiran was more intrigued by the quiet focus in her eyes.

He had come in late to run a physics simulation on molecular motion, laptop under his arm, half-asleep on cold coffee. When he passed her desk, a flicker on her screen caught his eye: a tangled graph that looked like a constellation map. “That looks like a star chart pretending to be science,” he said before he could stop himself.

Mira pushed her headphones down, surprised, then smiled. “It’s just an interaction network,” she replied. “But I like that better—star chart of molecules.” Her voice held a calm warmth that made the humming lab feel less mechanical. Kiran set his laptop on the station next to hers. “I am trying to teach particles how to dance without breaking the laws of physics,” he said. “Maybe your stars and my dancers should meet.”

Days turned into a pattern. They shared the same corner of the lab, screens facing each other like quiet mirrors. Mira chased hidden relationships in her data: which tiny compounds might one day help someone breathe easier, stand longer, live better. Kiran wrote simulations to see how those same compounds might behave under strange conditions, like testing gravity in a virtual sky. Sometimes they spoke in technical terms, other times in metaphors, pretending the lab was a small universe and they were just two curious observers charting it.

One evening, a storm rolled over the city, turning the institute’s windows into silver sheets of rain. Most students had left hours ago, but their corner still glowed. The air smelled faintly of ethanol and coffee. Mira leaned back and rubbed her eyes. “I think I broke it,” she said, nodding at her screen. “The model stopped learning.”

Kiran wheeled his chair over. On the monitor, the lines of the network refused to converge. “Maybe it’s not broken,” he said. “Maybe it just needs a different way to be seen.” He adjusted a parameter, added a small tweak to her code, and they watched as the graph shifted, compressing into a new pattern. “There,” he whispered. “Your stars moved.”

Mira stared at the screen, then at him. “You know, you talk about code like it has feelings,” she said.

“Only because I met someone who treats data like constellations,” he replied.

The storm outside deepened, thunder rolling in distant waves. The institute’s hallway lights dimmed for the night, leaving their lab a pool of soft white and blue. Mira opened a small box from her bag and pulled out a vial of faintly glowing solution. “Experimental demo,” she said, her tone suddenly playful. “Fluorescent proteins under the right light. Want to see something?”

She placed the vial under a handheld lamp. The liquid shimmered, slowly blooming into a pale, otherworldly glow. Kiran watched, the reflection dancing in his eyes. “It’s like a bottled galaxy,” he murmured.

“Everything looks like space to you,” she teased.

“Only the beautiful things,” he answered, before he could second-guess the words.

For a moment, the only sound was the rain and the quiet hum of the machines. Mira set the vial down and turned to him. “You know,” she said softly, “I started this project because I wanted to prove something to myself. That I could build something that mattered. But lately it feels like…it’s more than just the project.”

Kiran’s heart beat louder than the storm. “More than the project?” he asked, the corner of his mouth lifting.

She held his gaze, steady and brave. “More than the project,” she repeated. “I like our late nights. The way you defend your simulations like they’re shy creatures. The way you see galaxies in my messy plots. I don’t want this to end when the experiment does.”

He swallowed, then laughed quietly, relief and wonder mixing in his voice. “Mira,” he said, “I’ve been rewriting my code for weeks just to have an excuse to stay in this lab a little longer with you.”

Her eyes softened. “You could have just said it.”

“I’m better at talking to particles.”

“Then try talking to me instead,” she whispered.

He stepped closer, the glow of the vial casting soft light between them. “Mira,” he said, more firmly now, “I like you. Not as a collaborator or a convenient neighbor in the lab. As the person who makes this fluorescent chaos feel like home.”

Her reply was a smile that unfolded slowly, like a sunrise. “Good,” she said. “Because I was starting to design hypothetical scenarios in my head where you didn’t feel the same, and the statistics were getting depressing.”

They both laughed, tension breaking like the rain outside. Kiran reached for her hand, hesitant, and she met him halfway. Her fingers were cool from the lab, but the touch sent a warm, steady current through him, like a circuit finally closing.

“May I?” he asked, the question hanging gently between them.

She nodded.

Their first kiss was not cinematic or perfectly staged. It was quiet, surrounded by workstations, stacked journals, and a half-finished simulation running in the background. But to them, it felt like the moment two lines of code finally compiled without error after countless attempts. Simple, inevitable, and right.

When they pulled apart, Mira rested her forehead lightly against his. “So,” she said softly, “how does this fit into your model of the universe?”

Kiran smiled. “In my model,” he said, “this is the new initial condition. Everything else can be recalculated.”

Years later, people at Asterion would talk about the breakthrough that came from a small, stubborn project in that lab: a smarter way to search for useful compounds, a tool that quietly made many lives better. They would trace graphs in presentations and nod at the elegance of it all.

Very few would know that, in a corner of that same lab, on a stormy night, two researchers had stood hand-in-hand, watching a tiny vial glow like a private constellation, realizing that somewhere between data and dreams, they had written themselves into each other’s stories.

And for Kiran and Mira, no matter how complicated the models became, the memory of that moment stayed simple: just two people, one quiet lab, and a universe that finally made sense. """

print(s) 

# string slicing 

name = "sunil narayan" 

print(name[-3])
print(name[4])  
print(name[::]) 
print(name[: 8]) 
print(name[4:]) 

# looping through a string 

for x in "sunil narayan": 
    for y in "aman prakash":
     print(x , y) 
     
# Only pair characters one-by-one (not nested)

for x in "sunil narayan , aman prakash yadav": 
    print(x) 

# skip spaces 

for x in "sunil narayan": 
    if x == " ": 
        continue 
    for y in "aman prakash yadav": 
        if y == " ": 
            continue 
        print(x ,y) 

# string length 

name = "mohd. sadik" 
print(len(name)) 

# check string 

text = " The is programing related to string slicing !!" 
print("string" in text) 

# using if statement 

text = " The is programing related to string slicing !!"
if "string" in text: 
    print("Yes , 'string' is present") 

# check if NOT 

text = " The is programing related to string slicing !!"
print("string" not in text) 

# using if statement 

text = " The is programing related to string slicing !!" 
if "string" not in text: 
    print("NO , 'string' is NOT present.") 