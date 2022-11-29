from machine import Pin

cable_write_ground = Pin(20, mode=Pin.OUT)
cable_write_siganl = Pin(21, mode=Pin.OUT)

cable_read_ground = Pin(16, mode=Pin.IN)
cable_read_siganl = Pin(17, mode=Pin.IN)

status_led = Pin(22, mode=Pin.OUT)


while True:
    error = False

    cable_write_ground.value(1)
    if not [cable_read_ground.value(), cable_read_value.value()] == [True, False]:
        error = True

    cable_write_ground.value(0)
    cable_write_value.value(1)

    if not [cable_read_ground.value(), cable_read_value.value()] == [False, True]:
        error = True

    cable_write_value.value(0)


    status_led.value(not error)