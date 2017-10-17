
# coding: utf-8

# In[1]:


import folium
import pandas
import statistics as stats
import json


# In[2]:


#creat data frame from values read from csv
df_volcanoes = pandas.read_csv("Volcanoes_USA.txt")


#list unique values in the type column of volcanoes database
df_volcanoes.TYPE.unique()
#make a new column binning attributes into catagories based volcanoe type


#iterate through volcanoes data frame and assign colors from dictionary based on common 'TYPE' attribute
def colorProducer(kind):
    type_colors = {
    'Stratovolcanoes': "#AA08B2",
    'Stratovolcano':   "#FFDD13",
    'Volcanic field':  "#FF2704",
    'Shield volcanoes':"#0075CC",
    'Maar':            "#00B226",
    'Cinder cones':"    #B27F15",
    'Shield volcano':  "#00FF88",
    'Complex volcano': "#FFAD04",
    'Caldera':         "#9518CC",
    'Calderas':        '#800CB2',
    'Fissure vents':   "#B24015",
    'Lava domes':      "#63FF00",
    'Maars':           "#FF4904",
    'Cinder cone':     "#182DCC"
    
    }
    return type_colors[kind]
    



#print list of column names and shape of table
#print(list(df_volcanoes))
#print(df_volcanoes.shape)


# In[3]:


#convert columns to list objects
lat = list(df_volcanoes["LAT"])
lon = list(df_volcanoes["LON"])
name = list(df_volcanoes["NAME"])
elev = list(df_volcanoes["ELEV"])
kind = list(df_volcanoes["TYPE"])

df_volcanoes['colors']= "green"

# In[4]:


#get mean center
mean_lat = stats.mean(lat)
mean_lon = stats.mean(lon)


# In[5]:


#make folium feature group and map object
volcanoes = folium.FeatureGroup(name='Volcanoes')

countries = folium.FeatureGroup(name='Countries')


m = folium.Map(location = [mean_lat,mean_lon],zoom_start=2)


# In[6]:


#import data into feature group

#why is this breaking my map???  Make sure the check the parenthases!!!  I know, there's a lot of them.
countries.add_child(folium.GeoJson(data=open("world.json","r", encoding = "utf-8-sig").read(),
    style_function = lambda x: {
        'fillColor':'blue' if x['properties']['POP2005'] < 7000000 
        else 'yellow' if 7000000 <= x['properties']['POP2005'] <= 15000000
        else 'green' 
        } ))

                    
for lat,lon,name,elev,kind in zip(lat,lon,name,elev,kind):
    volcanoes.add_child(folium.CircleMarker(
        radius = 5,
        location = [lat,lon],
        #the extra bit for the popup eliminates the blank page error due to quotation marks in the string input
        popup = folium.Popup(name+": "+str(elev)+"m, "+kind,parse_html=True),
        color=colorProducer(kind),
        fill_color = colorProducer(kind),
        opacity = 0.7,
        fill = True
        ))

#add features to map object
volcanoes.add_to(m)
countries.add_to(m)
m.add_child(folium.LayerControl())
#m.add_child(volcanoes)
#m.add_child(countries)

#display map
m.save("volcanoes.html")

