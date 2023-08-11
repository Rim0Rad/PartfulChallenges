import bpy
import random

#Location
positions = [
    [4,6,3],
    [6,6,3],
    [3,3,3],
    [3,2,3],
    [7,3,3],
    [7,2,3],
    [4,1,3],
    [5,1,3],
    [6,1,3]
]

#Material
colorStep = 100

#Animation
frameNum = 100
maxJitters = 1000
minJitters = 800
eulerRotationCap = 4

for p in positions:
  
    # add cube object to the scene
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align="WORLD",location=(p[0],p[1],p[2]), scale=(1,1,1))
    
    # create color
    matColor = bpy.data.materials.new("Color")
    
    redComponent = random.randrange(0, colorStep) / colorStep
    greenComponent = random.randrange(0, colorStep) / colorStep
    matColor.diffuse_color = ( redComponent, greenComponent, 0, 1)
    
    obj = bpy.context.object
    obj.active_material = matColor
    
    # add random jitter to rotation  
    numJitters = random.randrange(minJitters, maxJitters)
    interval = frameNum / numJitters 
    
    for frame in range(0, numJitters): 
        
        frameStart = frame * interval
        frameEnd = frameStart + interval
    
        for i in range(0, 3):
            obj.rotation_euler[i] = obj.rotation_euler[i]
            obj.keyframe_insert(data_path="rotation_euler", frame=frameStart)
            
            obj.rotation_euler[i] = random.randrange(-eulerRotationCap, eulerRotationCap) / 100
            obj.keyframe_insert(data_path="rotation_euler", frame=frameEnd)



