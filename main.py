import pyglet
from pyglet.window import key
from pyglet.window import mouse

window = pyglet.window.Window()

cursorImg = pyglet.image.ImageGrid(pyglet.image.load('assets/Cursors.png'), 2, 2)
cursors = {
    'normal': (cursorImg[2], (0, 16)),
}

SETTINGS = {
    'cursor': 'normal',
    'scale': 80
}

class Cursor(pyglet.window.MouseCursor):
    def draw(self, x, y):
        hot = cursors[SETTINGS['cursor']][1]
        txture = cursors[SETTINGS['cursor']][0].get_texture()
        txture.width = SETTINGS['scale']
        txture.height = SETTINGS['scale']
        txture.blit(x - hot[0], y - hot[1], 0)

window.set_mouse_cursor(Cursor())

@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.A:
        print('The "A" key was pressed.')
    elif symbol == key.LEFT:
        print('The left arrow key was pressed.')
    elif symbol == key.ENTER:
        print('The enter key was pressed.')

@window.event
def on_mouse_press(x, y, button, modifiers):
    if button == mouse.LEFT:
        print('The left mouse button was pressed.')

@window.event
def on_draw():
    window.clear()

pyglet.app.run()
