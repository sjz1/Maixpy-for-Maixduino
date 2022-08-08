import sensor, image, lcd, time

lcd.init()
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.run(1)

blob_threshold = (46, 74, 13, 41, -46, 24)
while True:
    img=sensor.snapshot()
    blobs = img.find_blobs([blob_threshold])
    if blobs:
        for b in blobs:
            tmp=img.draw_rectangle(b[0:4])
            tmp=img.draw_cross(b[5],b[6])
            c=img.get_pixel(b[5],b[6])
            lcd.display(img)
            print(b[5],b[6])
