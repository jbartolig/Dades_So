def on_button_pressed_a():
    basic.show_icon(IconNames.SMALL_DIAMOND)
    serial.write_line("Inici gravació nivell de so")
    for index in range(25):
        serial.write_line("" + str((input.sound_level())))
        basic.show_icon(IconNames.YES)
    serial.write_line("Fi gravació nivell de so")
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_forever():
    pass
basic.forever(on_forever)
