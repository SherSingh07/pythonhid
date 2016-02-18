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

#ifndef __MY_C_EXT_H__
#define __MY_C_EXT_H__

#include "libusb.h"

typedef struct data {
    int err;
    int c;
    int x;
    int y;
    int z;
} data;

typedef struct descriptor {
    unsigned char  bLength;
    unsigned char  bDescriptorType;
    unsigned short bcdUSB;
    unsigned char  bDeviceClass;
    unsigned char  bDeviceSubClass;
    unsigned char  bDeviceProtocol;
    unsigned char  bMaxPacketSize0;
    unsigned short idVendor;
    unsigned short idProduct;
    unsigned short bcdDevice;
    unsigned char  iManufacturer;
    unsigned char  iProduct;
    unsigned char  iSerialNumber;
    unsigned char  bNumConfigurations;
}descriptor;

int initialize();
int open_device(int vid, int pid);
int detach_kernel_driver();
int claim_interface();
data readData();
descriptor get_device_descriptor();

void release_interface();
void close_device();
void finalize();


#endif // __MY_C_EXT_H__
