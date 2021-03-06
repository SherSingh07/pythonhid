# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.40
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pymouse', [dirname(__file__)])
        except ImportError:
            import _pymouse
            return _pymouse
        if fp is not None:
            try:
                _mod = imp.load_module('_pymouse', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pymouse = swig_import_helper()
    del swig_import_helper
else:
    import _pymouse
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["err"] = _pymouse.data_err_set
    __swig_getmethods__["err"] = _pymouse.data_err_get
    if _newclass:err = _swig_property(_pymouse.data_err_get, _pymouse.data_err_set)
    __swig_setmethods__["c"] = _pymouse.data_c_set
    __swig_getmethods__["c"] = _pymouse.data_c_get
    if _newclass:c = _swig_property(_pymouse.data_c_get, _pymouse.data_c_set)
    __swig_setmethods__["x"] = _pymouse.data_x_set
    __swig_getmethods__["x"] = _pymouse.data_x_get
    if _newclass:x = _swig_property(_pymouse.data_x_get, _pymouse.data_x_set)
    __swig_setmethods__["y"] = _pymouse.data_y_set
    __swig_getmethods__["y"] = _pymouse.data_y_get
    if _newclass:y = _swig_property(_pymouse.data_y_get, _pymouse.data_y_set)
    __swig_setmethods__["z"] = _pymouse.data_z_set
    __swig_getmethods__["z"] = _pymouse.data_z_get
    if _newclass:z = _swig_property(_pymouse.data_z_get, _pymouse.data_z_set)
    def __init__(self): 
        this = _pymouse.new_data()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymouse.delete_data
    __del__ = lambda self : None;
data_swigregister = _pymouse.data_swigregister
data_swigregister(data)

class descriptor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, descriptor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, descriptor, name)
    __repr__ = _swig_repr
    __swig_setmethods__["bLength"] = _pymouse.descriptor_bLength_set
    __swig_getmethods__["bLength"] = _pymouse.descriptor_bLength_get
    if _newclass:bLength = _swig_property(_pymouse.descriptor_bLength_get, _pymouse.descriptor_bLength_set)
    __swig_setmethods__["bDescriptorType"] = _pymouse.descriptor_bDescriptorType_set
    __swig_getmethods__["bDescriptorType"] = _pymouse.descriptor_bDescriptorType_get
    if _newclass:bDescriptorType = _swig_property(_pymouse.descriptor_bDescriptorType_get, _pymouse.descriptor_bDescriptorType_set)
    __swig_setmethods__["bcdUSB"] = _pymouse.descriptor_bcdUSB_set
    __swig_getmethods__["bcdUSB"] = _pymouse.descriptor_bcdUSB_get
    if _newclass:bcdUSB = _swig_property(_pymouse.descriptor_bcdUSB_get, _pymouse.descriptor_bcdUSB_set)
    __swig_setmethods__["bDeviceClass"] = _pymouse.descriptor_bDeviceClass_set
    __swig_getmethods__["bDeviceClass"] = _pymouse.descriptor_bDeviceClass_get
    if _newclass:bDeviceClass = _swig_property(_pymouse.descriptor_bDeviceClass_get, _pymouse.descriptor_bDeviceClass_set)
    __swig_setmethods__["bDeviceSubClass"] = _pymouse.descriptor_bDeviceSubClass_set
    __swig_getmethods__["bDeviceSubClass"] = _pymouse.descriptor_bDeviceSubClass_get
    if _newclass:bDeviceSubClass = _swig_property(_pymouse.descriptor_bDeviceSubClass_get, _pymouse.descriptor_bDeviceSubClass_set)
    __swig_setmethods__["bDeviceProtocol"] = _pymouse.descriptor_bDeviceProtocol_set
    __swig_getmethods__["bDeviceProtocol"] = _pymouse.descriptor_bDeviceProtocol_get
    if _newclass:bDeviceProtocol = _swig_property(_pymouse.descriptor_bDeviceProtocol_get, _pymouse.descriptor_bDeviceProtocol_set)
    __swig_setmethods__["bMaxPacketSize0"] = _pymouse.descriptor_bMaxPacketSize0_set
    __swig_getmethods__["bMaxPacketSize0"] = _pymouse.descriptor_bMaxPacketSize0_get
    if _newclass:bMaxPacketSize0 = _swig_property(_pymouse.descriptor_bMaxPacketSize0_get, _pymouse.descriptor_bMaxPacketSize0_set)
    __swig_setmethods__["idVendor"] = _pymouse.descriptor_idVendor_set
    __swig_getmethods__["idVendor"] = _pymouse.descriptor_idVendor_get
    if _newclass:idVendor = _swig_property(_pymouse.descriptor_idVendor_get, _pymouse.descriptor_idVendor_set)
    __swig_setmethods__["idProduct"] = _pymouse.descriptor_idProduct_set
    __swig_getmethods__["idProduct"] = _pymouse.descriptor_idProduct_get
    if _newclass:idProduct = _swig_property(_pymouse.descriptor_idProduct_get, _pymouse.descriptor_idProduct_set)
    __swig_setmethods__["bcdDevice"] = _pymouse.descriptor_bcdDevice_set
    __swig_getmethods__["bcdDevice"] = _pymouse.descriptor_bcdDevice_get
    if _newclass:bcdDevice = _swig_property(_pymouse.descriptor_bcdDevice_get, _pymouse.descriptor_bcdDevice_set)
    __swig_setmethods__["iManufacturer"] = _pymouse.descriptor_iManufacturer_set
    __swig_getmethods__["iManufacturer"] = _pymouse.descriptor_iManufacturer_get
    if _newclass:iManufacturer = _swig_property(_pymouse.descriptor_iManufacturer_get, _pymouse.descriptor_iManufacturer_set)
    __swig_setmethods__["iProduct"] = _pymouse.descriptor_iProduct_set
    __swig_getmethods__["iProduct"] = _pymouse.descriptor_iProduct_get
    if _newclass:iProduct = _swig_property(_pymouse.descriptor_iProduct_get, _pymouse.descriptor_iProduct_set)
    __swig_setmethods__["iSerialNumber"] = _pymouse.descriptor_iSerialNumber_set
    __swig_getmethods__["iSerialNumber"] = _pymouse.descriptor_iSerialNumber_get
    if _newclass:iSerialNumber = _swig_property(_pymouse.descriptor_iSerialNumber_get, _pymouse.descriptor_iSerialNumber_set)
    __swig_setmethods__["bNumConfigurations"] = _pymouse.descriptor_bNumConfigurations_set
    __swig_getmethods__["bNumConfigurations"] = _pymouse.descriptor_bNumConfigurations_get
    if _newclass:bNumConfigurations = _swig_property(_pymouse.descriptor_bNumConfigurations_get, _pymouse.descriptor_bNumConfigurations_set)
    def __init__(self): 
        this = _pymouse.new_descriptor()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymouse.delete_descriptor
    __del__ = lambda self : None;
descriptor_swigregister = _pymouse.descriptor_swigregister
descriptor_swigregister(descriptor)


def initialize():
  return _pymouse.initialize()
initialize = _pymouse.initialize

def open_device(*args):
  return _pymouse.open_device(*args)
open_device = _pymouse.open_device

def detach_kernel_driver():
  return _pymouse.detach_kernel_driver()
detach_kernel_driver = _pymouse.detach_kernel_driver

def claim_interface():
  return _pymouse.claim_interface()
claim_interface = _pymouse.claim_interface

def readData():
  return _pymouse.readData()
readData = _pymouse.readData

def get_device_descriptor():
  return _pymouse.get_device_descriptor()
get_device_descriptor = _pymouse.get_device_descriptor

def release_interface():
  return _pymouse.release_interface()
release_interface = _pymouse.release_interface

def close_device():
  return _pymouse.close_device()
close_device = _pymouse.close_device

def finalize():
  return _pymouse.finalize()
finalize = _pymouse.finalize


