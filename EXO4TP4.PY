degrees = 0

def on_gesture_shake():
    pass
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    global degrees
    degrees = input.compass_heading()
    if degrees < 45 or degrees > 315:
        basic.show_string("" + str((input.sound_level())))
    elif degrees < 135:
        basic.show_string("" + str((input.light_level())))
        basic.show_string("" + str((input.temperature())))
    elif degrees < 225:
        basic.show_string("" + str((input.sound_level())))
    elif degrees < 315:
        basic.show_string("" + str((input.light_level())))
        basic.show_string("" + str((input.temperature())))
    else:
        basic.clear_screen()
basic.forever(on_forever)
