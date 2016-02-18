import pymouse
import time

#resolution X,Y
MAX_X=1024
MAX_Y=768

def print_descriptor(desc):
    """print the information in USB device descriptor"""
    print "bLength                 : ", desc.bLength
    print "bDescriptorType         : ", desc.bDescriptorType
    print "bcdUSB                  : ", desc.bcdUSB
    print "bDeviceClass            : ", desc.bDeviceClass
    print "bDeviceSubClass         : ", desc.bDeviceSubClass
    print "bDeviceProtocol         : ", desc.bDeviceProtocol
    print "bMaxPacketSize0         : ", desc.bMaxPacketSize0
    print "idProduct               : ", desc.idProduct
    print "iManufacturer           : ", desc.iManufacturer
    print "iProduct                : ", desc.iProduct
    print "iSerialNumber           : ", desc.iSerialNumber
    print "bNumConfigurations      : ", desc.bNumConfigurations

def main():

    # 1. initial x,y in center of resolution/screen
    x=MAX_X/2
    y=MAX_Y/2

    # 2. Initialize libusb
    err = pymouse.initialize()
    if int(err) < 0:
        print "Failed to initialized USB lib"
        return

    # 3. Open your device by Vendor ID and Product ID
    err = pymouse.open_device(0x04F3, 0x0230)
    if int(err) < 0:
        print "Failed to open device"
        return

    # 4. Get descriptor for USB device
    desc=pymouse.get_device_descriptor()
    print_descriptor(desc)

    # 5. Ask kernel to detach the driver for given device,
    # so that we can access the device
    err = pymouse.detach_kernel_driver()
    if int(err) < 0:
        print "[WARNING] :: Failed to claim interface"

    # 6. Claim the interface for the device
    err = pymouse.claim_interface()
    if int(err) < 0:
        print "Failed to claim interface"
        return

    # 7. Read data from device forever
    try:
        while 1:
            data = pymouse.readData()
            if data.err == 0 :
                x = x + data.x
                y = y + data.y
                #confine x,y within screen
                if x>MAX_X: x=MAX_X
                if x<0: x=0
                if y>MAX_Y: y=MAX_Y
                if y<0: y=0
                print "(%d, %d)" % (x, y)
                print "click=", data.c
    except KeyboardInterrupt:
        print "Exiting...."
        pymouse.release_interface()
        pymouse.close_device()
        pymouse.finalize()

if __name__ == "__main__":
    main()
