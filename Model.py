import arcpy

# Set the Workspace of the ArcGIS project
arcpy.env.workspace = "C:/Users/admin/Documents/ArcGIS/Projects/MyProject/MyProject.gdb"

# set the array of supermarkets (names of the layers)
supermarkets = ["HDL", "Franca_Geocoded", "Aroma_Geocoded", "Voli_Geocoded1", "Idea_Geocoded"]


def search_distances():
    field = "NEAR_DIST"

    for supermarket in supermarkets:
        output_table = "C:/Users/admin/Documents/ArcGIS/Projects/MyProject/MyProject.gdb/Output_" + supermarket
        with arcpy.da.SearchCursor(output_table, field) as cursor:
            for row in cursor:
                print(supermarket + " " + str(row[0]))


def calculate_closest():
    # set the outbreak layer
    in_features = "locate_feature_class_2"

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
            in_features, supermarket, out_table, search_radius, location, angle, closest, closest_count, method
        )
