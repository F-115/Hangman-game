import random
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from modules.shapes import update_chicken, toggle_chicken
from modules.config import config

def stage1animate():
    # Codes for any changes in Models, Camera
    glutPostRedisplay()

    # Use the config object to access and modify properties
    if not config.get_end_status() and not config.get_pause_status() and not config.get_stop_status():
        config.set_diamondY(config.get_diamondY() - config.get_speed())
        toggle_chicken()
        update_chicken()
        if round(config.get_diamondX()) >= round(config.get_boat_position()[0]) and round(config.get_diamondX()) <= round(config.get_boat_position()[0]) + 60:
            if round(config.get_diamondY()) - 9 == config.get_boat_position()[1]:
                config.set_points(config.get_points() + 1)
                config.set_speed(config.get_speed() * 2)
                config.set_random_colors(random.randint(0, 255) / 255, random.randint(0, 255) / 255, random.randint(0, 255) / 255)
                print('Score: ' + str(config.get_points()))
                
                x_origin, y_origin = config.get_chicken_position()

                y_origin = y_origin + config.birdY_offset
                config.set_diamondY(y_origin)
                config.set_diamondX(x_origin)
                # config.set_diamond_position(random.randint(-240, 240), 230)
        if round(config.get_diamondY()) - 9 < config.get_boat_position()[1]:
            print('Game Over! Score:' + str(config.get_points()))
            config.set_stop_status(True)
            config.set_diamondY(-300)

    if config.get_end_status():
        return
