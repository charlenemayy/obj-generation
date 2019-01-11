# ideally would extract verticies, normals and faces from a given 2D image and pass it to our object generation function
# def extract_data:
#     for coord in range (0, n):
#         verts[coord] = [x, y, z]

# hardcoded values to replace data that should be mined from extract_data
verts = [[0.0, 0.0, 0.0],
         [0.0, 0.0, 1.0],
         [0.0, 1.0, 0.0],
         [0.0, 1.0, 1.0],
         [1.0, 0.0, 0.0],
         [1.0, 0.0, 1.0],
         [1.0, 1.0, 0.0],
         [1.0, 1.0, 1.0]]

# directional vector associated with a vertex
norms = [[0.000000, 0.000000, 1.000000],
         [0.000000, 0.000000, -1.000000],
         [0.000000, 1.000000, 0.000000],
         [0.000000, -1.000000, 0.000000],
         [1.000000, 0.000000, 0.000000],
         [-1.000000, 0.000000, 0.000000]]

# the face coordinates are in the format 'verts_index//norms_index'
faces = [['1//2', '7//2', '5//2'],
         ['1//2', '3//2', '7//2'],
         ['1//6', '4//6', '3//6'],
         ['1//6', '2//6', '4//6'],
         ['3//3', '8//3', '7//3'],
         ['3//3', '4//3', '8//3'],
         ['5//5', '7//5', '8//5'],
         ['5//5', '8//5', '6//5'],
         ['1//4', '5//4', '6//4'],
         ['1//4', '6//4', '2//4'],
         ['2//1', '6//1', '8//1'],
         ['2//1', '8//1', '4//1']]

def build_obj(verts, norms, faces):
    objfile = open('object.obj', 'w')
    objfile.write("#object.obj\n\n")

    for coord in verts:
        objfile.write("v {0} {1} {2}\n".format(coord[0],coord[1],coord[2]))
    objfile.write("\n")

    for coord in norms:
        objfile.write("vn {0} {1} {2}\n".format(coord[0],coord[1],coord[2]))
    objfile.write("\n")

    for coord in faces:
        objfile.write("f {0} {1} {2}\n".format(coord[0],coord[1],coord[2]))

    objfile.close()

build_obj(verts, norms, faces)
