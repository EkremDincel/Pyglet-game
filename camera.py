# Most of the code copied from https://github.com/pyglet/pyglet/blob/master/examples/camera.py
import pyglet
from contextmanager import activatable

@activatable
class Camera:
    """ A simple 2D camera that contains the speed and offset."""

    def __init__(self):
        self.x = 0
        self.y = 0
        self.zoom = 1

    @property
    def position(self):
        """Query the current offset."""
        return self.offset_x, self.offset_y

    @position.setter
    def position(self, value):
        """Set the scroll offset directly."""
        self.offset_x, self.offset_y = value

    def begin(self):
        # Set the current camera offset so you can draw your scene.
        # Translate using the zoom and the offset.
        pyglet.gl.glTranslatef(-self.x * self.zoom, -self.y * self.zoom, 0)

        # Scale by zoom level.
        pyglet.gl.glScalef(self.zoom, self.zoom, 1)

    def end(self):
        # Since this is a matrix, you will need to reverse the translate after rendering otherwise
        # it will multiply the current offset every draw update pushing it further and further away.

        # Reverse scale, since that was the last transform.
        pyglet.gl.glScalef(1 / self.zoom, 1 / self.zoom, 1)

        # Reverse translate.
        pyglet.gl.glTranslatef(self.x * self.zoom, self.y * self.zoom, 0)
