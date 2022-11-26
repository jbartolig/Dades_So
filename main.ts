input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.SmallDiamond)
    serial.writeLine("Inici gravació nivell de so")
    for (let index = 0; index < 25; index++) {
        serial.writeLine("" + (input.soundLevel()))
        basic.showIcon(IconNames.Yes)
    }
    serial.writeLine("Fi gravació nivell de so")
    basic.clearScreen()
})
basic.forever(function () {
	
})
