import pyglet
from camera import Camera

window = pyglet.window.Window()

camera = Camera()

@window.event
def on_mouse_scroll(x, y, scroll_x, scroll_y):
    print(camera.zoom)
    if scroll_y > 0:
        camera.zoom *= 1.1
    else:
        camera.zoom *= 0.9

@window.event
def on_key_press(k, b):
    if k == b"a"[0]:
        camera.x -= 10
    elif k == b"d"[0]:
        camera.x += 10

image = pyglet.resource.image('bg.png')
image.anchor_y = image.width/2
image.anchor_x = image.height/2
sprite = pyglet.sprite.Sprite(image, 200, 200)


@window.event
def on_draw():
    window.clear()
    with camera:
        sprite.draw()
    

pyglet.app.run()
