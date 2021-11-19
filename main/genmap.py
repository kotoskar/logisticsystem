import gmplot
def gen(drones, dir, zoom):
    cx = sum(list(zip(*drones))[0])/len(drones)
    cy = sum(list(zip(*drones))[1])/len(drones)
    apikey = ""
    gmap = gmplot.GoogleMapPlotter(cx, cy, zoom, apikey=apikey)
    gmap.circle(60.015553, 29.985312, 200, face_alpha=0.33, ew=3, color='red')
    gmap.circle(60.019842, 29.999110, 200, face_alpha=0.33, ew=3, color='orange')
    intellect  =  zip ( * [
        ( 60.012197, 30.099825 ),
        ( 60.011480, 30.078058 ),
        ( 60.017798, 30.076834 ),
        ( 60.017862, 30.100308 )])
    for drone in drones:
        gmap.marker(drone[0], drone[1], precision = 2,  color = 'lightblue', label = int(drone[2]))
    gmap.polygon(*intellect, face_color='red', edge_color='cornflowerblue', edge_width=5)
    gmap.draw(dir)
