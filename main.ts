input.onButtonPressed(Button.A, function () {
    a += 10
    basic.showNumber(a)
})
input.onGesture(Gesture.LogoUp, function () {
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        # . . . .
        `)
})
input.onButtonPressed(Button.AB, function () {
    a += a * 0.02
    basic.showNumber(a)
})
input.onButtonPressed(Button.B, function () {
    a += 1
    basic.showNumber(a)
})
input.onGesture(Gesture.Shake, function () {
    basic.showNumber(randint(1, 6))
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showLeds(`
        . . # # #
        . . # # #
        . . # # #
        . . . . .
        . . . . .
        `)
})
input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    coinflip = randint(0, 1)
    if (coinflip == 0) {
        basic.showLeds(`
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    }
})
let coinflip = 0
let a = 0
a = 0
basic.showNumber(a)
