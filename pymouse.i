%module pymouse

%{
#define SWIG_FILE_WITH_INIT
#include "pymouse.h"
%}

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
