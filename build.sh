swig -python pymouse.i
gcc -O2 -fPIC -c pymouse.c -I/home/navrooh/work/libusb/src/build/include/libusb-1.0
gcc -O2 -fPIC -c pymouse_wrap.c -I/usr/include/python2.6 -I/home/navrooh/work/libusb/src/build/include/libusb-1.0
gcc -shared pymouse.o pymouse_wrap.o -L/home/navrooh/work/libusb/src/build/lib -lusb-1.0 -o _pymouse.so
