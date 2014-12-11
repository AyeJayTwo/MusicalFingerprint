import json
import urllib2
from song_search import song_chooser
import Image
import ImageDraw
from rgb_convert import color_intensity
from math import ceil

###Import the datums###
url, artist, song = song_chooser()
j = urllib2.urlopen(url)
j_obj = json.load(j)

###Initialize dem variables to get filled in###
song_segments = len(j_obj["segments"])

#Relative intensities of each pitch
p1 = [0] * song_segments # C
p2 = [0] * song_segments # C#
p3 = [0] * song_segments # D
p4 = [0] * song_segments # D#
p5 = [0] * song_segments # E
p6 = [0] * song_segments # F
p7 = [0] * song_segments # F#
p8 = [0] * song_segments #G
p9 = [0] * song_segments # G#
p10 = [0] * song_segments # A
p11 = [0] * song_segments # A#
p12 = [0] * song_segments # B

#time = [0] * song_segments
# Timbre vectors. See EchoNest API documentation on what each basis element signifies
t1 = [0] * song_segments
t2 = [0] * song_segments
t3 = [0] * song_segments
t4 = [0] * song_segments
t5 = [0] * song_segments
t6 = [0] * song_segments
t7 = [0] * song_segments
t8 = [0] * song_segments
t9 = [0] * song_segments
t10 = [0] * song_segments
t11 = [0] * song_segments
t12 = [0] * song_segments
duration = [0] * song_segments

#Loop through the segments and parse out the details I need
for i in range(0,len(j_obj["segments"])):
	## Loop through each sound segment and pick out the pitch vector
	p1[i],p2[i],p3[i],p4[i],p5[i],p6[i],p7[i],p8[i],p9[i],p10[i],p11[i],p12[i] = j_obj["segments"][i]["pitches"]

	## Loop through each sound segment and identify the start time
	#time[i]= j_obj["segments"][i]["start"]
	duration[i] = round(j_obj["segments"][i]["duration"],2)

	#Loop through each sound segment and identify the timbre vector
	t1[i],t2[i],t3[i],t4[i],t5[i],t6[i],t7[i],t8[i],t9[i],t10[i],t11[i],t12[i] = j_obj["segments"][i]["timbre"]

## Draw it!!###
p = [p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12]


bar_width = 5
window_size = (int(ceil(sum(duration)*bar_width/10)*10), 600)
black = (0,0,0)

im = Image.new('RGBA', window_size ,color=black)

draw = ImageDraw.Draw(im)
start0 = (0,0)
h = 50
color2 = (0, 25, 150) #This color can be whatever you want

for k in range(12):
    start = (start0[0],start0[1] + h*k)
    for i in range(song_segments-1):
        point1 = start
        point2 = (start[0], start[1] + h)
        point3 = (start[0] + duration[i] * 5, start[1] + h)
        point4 = (start[0] + duration[i] * 5, start[1])
        start = point4
        
        ## New color takes the original color, and adjusts the intensity based on the pitches' relative intensity
        ## Made a new function which takes an RGB value and an intensity value, p[k][i] in this instance
        ## to return the rgb value back. Turns out PIL doesn't play well with HSV values, so this was a quick
        ## workaround.
        
        new_color =  color_intensity(color2[0],color2[1],color2[2],p[k][i])
        draw.polygon((point1,point2,point3,point4), fill=new_color,outline=None)
    
#save
file_name =  song+" by "+artist+".png"
im.save(file_name,'PNG')
print "Complete!"