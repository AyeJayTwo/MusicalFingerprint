def color_intensity(r,g,b,i):
    
    from colorsys import *
    h,s,v = rgb_to_hsv(r/255., g/255., b/255.)
    v *= i
    r2,g2,b2 = hsv_to_rgb(h,s,v)
    return int(r2*255),int(g*1.),int(b2*255)