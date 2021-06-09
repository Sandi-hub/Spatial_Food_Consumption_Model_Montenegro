import arcpy

# Set the Workspace of the ArcGIS project (Options > Current Setting > Default geodatabase)
arcpy.env.workspace = r'C:\Users\srude\Documents\ArcGIS\Packages\MyProject_970f65\p20\myproject.gdb'

# set the array of supermarkets (names of the layers)
supermarkets = ["HDL", "Franca_Geocoded", "Aroma_Geocoded", "Voli_Geocoded1", "Idea_Geocoded"]
# set the outbreak layer
outbreak = "locate_feature_class_2"


def calculate_closest():

    # set optional parameters
    search_radius = "100000 Meters"
    location = "NO_LOCATION"
    angle = "NO_ANGLE"
    closest = "CLOSEST"
    closest_count = 1
    method = "Geodesic"

    # calculate the distance to the nearest supermarket of each chain defined in the array supermarkets
    for supermarket in supermarkets:
        out_table = "Output_" + supermarket
        arcpy.GenerateNearTable_analysis(
            outbreak, supermarket, out_table, search_radius, location, angle, closest, closest_count, method
        )


def search_distances():
    field = "NEAR_DIST"

    for supermarket in supermarkets:
        output_table = "C:/Users/admin/Documents/ArcGIS/Projects/MyProject/MyProject.gdb/Output_" + supermarket
        with arcpy.da.SearchCursor(output_table, field) as cursor:
            for row in cursor:
                print(supermarket + " " + str(row[0]))

calculate_closest()
