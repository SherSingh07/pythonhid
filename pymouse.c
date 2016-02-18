/****************************************************************************
*                                                                           *
* Copyright (c) 2011 onwards by WeaveBytes InfoTech Pvt. Ltd.               *
* Please reports bugs at weavebytes@gmail.com                               *
*                                                                           * 
* This file may be distributed and/or modified under the terms of the       *
* GNU General Public License version 2 as published by the Free Software    *
* Foundation. (See COPYING.GPL for details.)                                *
*                                                                           *
* This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE   *
* WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. *
*                                                                           *
*****************************************************************************/

#include "pymouse.h"
#include "stdio.h"

static struct libusb_device_handle *devh = NULL;
int initialize() { return libusb_init(NULL); }

int open_device(int vid, int pid) {
    devh = libusb_open_device_with_vid_pid(NULL, vid, pid);
    if(!devh) return -1;
    return 0;
}

descriptor get_device_descriptor() {
    descriptor desc;
    int err;
    err  = libusb_get_device_descriptor(libusb_get_device(devh),
            (struct libusb_device_descriptor*)&desc);
    return desc;
}

int detach_kernel_driver() { return libusb_detach_kernel_driver(devh, 0); }
int claim_interface()      { return libusb_claim_interface(devh, 0); }

data readData() {
    data d;
    char tmp[4];
    int actual_length;
    d.err = libusb_interrupt_transfer(devh, 129, tmp, 4, &actual_length, 1000);
    d.c = tmp[0];
    d.x = tmp[1];
    d.y = tmp[2];
    d.z = tmp[3];
    printf("\nactual_length=%d\n",actual_length);
    return d;
}

void release_interface() { libusb_release_interface(devh, 0); }
void close_device()      { if(devh) libusb_close(devh); }
void finalize()          { libusb_exit(NULL); }
