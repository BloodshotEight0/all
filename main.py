def on_button_pressed_a():
    global a
    a += 10
    basic.show_number(a)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_logo_up():
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # . . . .
    """)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

def on_button_pressed_ab():
    global a
    a += a * 0.02
    basic.show_number(a)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global a
    a += 1
    basic.show_number(a)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.show_number(randint(1, 6))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_logo_down():
    basic.show_leds("""
        . . # # #
                . . # # #
                . . # # #
                . . . . .
                . . . . .
    """)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_logo_pressed():
    global coinflip
    coinflip = randint(0, 1)
    if coinflip == 0:
        basic.show_leds("""
            # # # # #
                        . . # . .
                        . . # . .
                        . . # . .
                        . . # . .
        """)
    else:
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

coinflip = 0
a = 0
a = 0
basic.show_number(a)