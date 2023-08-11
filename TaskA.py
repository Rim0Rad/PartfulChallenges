import bpy
import math
import random


#Create a random name in a format : "abcde:123"
def getRandomName():
    randomName = ""
    for i in range(5): 
        randomName += chr( random.randrange(97, 122) )
    randomName += ":"
    randomName += str(random.randrange(100, 999))
    return randomName


#instantiate 200 cubes forming a double helix
count = 100
for c in range(0, count):
    t = c/5
    a = 2
    b = 2
    
    x = a * math.sin(t)
    y = a * math.cos(t)
    z = b * t
    
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align="WORLD",location=(x,y,z), scale=(1,1,1))    
    bpy.context.active_object.name = getRandomName()
    
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align="WORLD",location=(-x,-y,z), scale=(1,1,1))
    bpy.context.active_object.name = getRandomName()

    
#print out: number of objects, vertices and materials in use
objects = bpy.data.objects
object = bpy.context.object

totObjects = len( objects )
totVertices = totObjects * len(object.data.vertices)
totMaterials = len(objects.data.materials)

print( "Total number of objects: ", totObjects )
print( "Total number of vertices: ", totVertices )
print( "Total number of materials: ", totMaterials)
