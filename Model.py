import arcpy
import numpy as np
import pandas as pd

# Set the Workspace of the ArcGIS project (Options > Current Setting > Default geodatabase)
arcpy.env.workspace = r'C:\Users\srude\Documents\ArcGIS\Packages\MyProject_970f65\p20\myproject.gdb'

# set the array of supermarkets (names of the layers)
supermarkets = ["HDL", "Franca_Geocoded", "Aroma_Geocoded", "Voli_Geocoded1", "Idea_Geocoded"]
# set the outbreak layer
outbreak = "locate_feature_class_2"
field = "NEAR_DIST"

# Set up Output Dataframe
column_names = ["Supermarket", "Distance"]
df_distances = pd.DataFrame(columns = column_names)


def calculate_closest():
    index = 1 
    # set optional parameters
    search_radius = "100000 Meters"
    location = "NO_LOCATION"
    angle = "NO_ANGLE"
    closest = "CLOSEST"
    closest_count = 1
    method = "Geodesic"

    # calculate the distance to the nearest supermarket of each chain defined in the array supermarkets
    for supermarket in supermarkets:
        print(supermarket)
        arcpy.Delete_management(r'memory\tempOutput_5')
        arcpy.GenerateNearTable_analysis(
            outbreak, supermarket,r'memory\tempOutput_5' , search_radius, location, angle, closest, closest_count, method
        )

        with arcpy.da.SearchCursor(r'memory\tempOutput_5', field) as cursor:
            for row in cursor:
                df_distances.loc[index] =[supermarket,row[0]]
                index = index + 1
                print(supermarket + " " + str(row[0]))

    print(df_distances)

calculate_closest()
