import arcpy
import numpy as np
import pandas as pd

# Set the Workspace of the ArcGIS project (Options > Current Setting > Default geodatabase)
workspace = r'C:\Users\srude\Documents\ArcGIS\Packages\MyProject_970f65\p20\myproject.gdb'

# set the array of supermarkets (names of the layers)
supermarkets = ["HDL", "Franca_Geocoded", "Aroma_Geocoded", "Voli_Geocoded1", "Idea_Geocoded"]

# set the outbreak layer
outbreak = "locate_feature_class_2"

# Set up Output Dataframe
df_distances = pd.DataFrame(columns = ["Supermarket", "Distance"])

arcpy.env.overwriteOutput = True

def calculate_closest():
    index = 1 
    
    # calculate the distance of the outbreak case to the nearest supermarket of each chain defined in the array supermarkets
    for supermarket in supermarkets:
        arcpy.GenerateNearTable_analysis(
            (workspace + '/' + outbreak), 
            (workspace+'/'+ supermarket), r'memory\tempOutput' , location= "NO_LOCATION", angle= "NO_ANGLE", closest="CLOSEST", method= "Geodesic"
        )

        # write result in dataframe
        with arcpy.da.SearchCursor(r'memory\tempOutput', "NEAR_DIST") as cursor:
            for row in cursor:
                df_distances.loc[index] =[supermarket,row[0]]
                index = index + 1
                
    arcpy.Delete_management(r'memory\tempOutput')
    print(df_distances)

calculate_closest()
