# Sierpinskis Pyramid
import bpy
from itertools import combinations
from mathutils import *

iterations = 3  # number of recursions

legLength = 1
vertexNum = 4

vertexMatrix = Matrix((
    ( 0, 0, 0 ),
    ( legLength, 0, 0 ),
    ( 0, legLength, 0 ),
    ( legLength / 3, legLength / 3, legLength / 2 )
))

vertices = []
faces = []

currentTetrahedron = 0
def createTetraHedron( vector = Vector( [0, 0, 0] ) ):
    global currentTetrahedron
    for vert in vertexMatrix:
        vertices.append( vert + vector )
        
    faces.extend( combinations( range( currentTetrahedron * vertexNum, currentTetrahedron * vertexNum + vertexNum), r = 3) )
    currentTetrahedron += 1

def createSierpinskiPyramid(iterations, vector=Vector([0,0,0])):

    if iterations < 0:
        return 0 
    
    if iterations==0:
        createTetraHedron( vector )
        
    else:
        iterations -= 1
        for vertex in vertexMatrix:
            createSierpinskiPyramid( iterations, 2**iterations * vertex + vector )

       
createSierpinskiPyramid(iterations)

# create mesh
mesh_data = bpy.data.meshes.new("sierpinskiPyramid")
mesh_data.from_pydata(vertices, [], faces)

# create object
obj = bpy.data.objects.new("SierpinskyPyramid", mesh_data)
bpy.context.collection.objects.link(obj)

#EXTRA: fractal shader = Mandelbrot set
fractal = bpy.data.materials.get("Fractal")
obj.active_material = fractal