def on_forever():
    if input.button_is_pressed(Button.A):
        basic.show_number(input.temperature())
    elif input.light_level() > 100:
        # display the temperature
        # check the light level
        basic.show_icon(IconNames.ANGRY)
    else:
        basic.clear_screen()
basic.forever(on_forever)
