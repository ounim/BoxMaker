from dxfwrite import DXFEngine as dxf
from dxfwrite import const

#space between each drawing
margin = 10

class Box(object):
    """Properties of the box we want to create"""
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.open = True #Let one side open

class Material(object):
    def __init__(self, thickness):
        self.thickness = thickness

class CNC(object):
    def __init__(self, tool_size):
        self.tool_size = tool_size

def output_dxf(box, material, cnc, filename):
    """ Output the drawing """
    drawing = dxf.drawing(filename)

    drawing.add_layer('TOP')
    top = dxf.polyline(flags=const.POLYLINE_CLOSED, layer='TOP')
    top.add_vertices([(0, 0),
                      (box.length, 0),
                      (box.length, box.width),
                      (0, box.width)])
    drawing.add(top)

    drawing.add_layer('BOTTOM')
    bottom = dxf.polyline(flags=const.POLYLINE_CLOSED, layer='BOTTOM')
    bottom_coord = [(0, 0),
                    (box.length, 0),
                    (box.length, box.width),
                    (0, box.width)]
    bottom_coord = [ (x + box.length + margin, y) for x,y in bottom_coord ]
    bottom.add_vertices(bottom_coord)
    drawing.add(bottom)

    drawing.add_layer('SIDE')
    side = dxf.polyline(flags=const.POLYLINE_CLOSED, layer='SIDE')
    perimeter = (box.length + box.width)*2
    side_coord = [(0, 0),
                  (perimeter, 0),
                  (perimeter, box.height),
                  (0, box.height)]
    side_coord = [ (x + 2*(box.length + margin), y) for x,y in side_coord ]
    side.add_vertices(side_coord)
    drawing.add(side)


    drawing.save()


if __name__ == "__main__":
    b = Box(100,200,50)
    m = Material(3)
    c = CNC(1)
    output_dxf(b, m, c, "test.dxf")
