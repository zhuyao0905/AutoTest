import os
import time


def device_info():
    brand = os.popen("adb shell getprop ro.product.brand").read().strip()
    model = os.popen("adb shell getprop ro.product.model").read().strip()
    release = os.popen("adb shell getprop ro.build.version.release").read().strip()
    wm = os.popen("adb shell wm size ").read().strip()
    density = os.popen("adb shell wm density").read().strip()
    android_id = os.popen("adb shell settings get secure android_id").read().strip()
    sdkVersion = os.popen('adb shell getprop ro.build.version.sdk').read().strip()


    print('Brand：'+ brand)
    print('Model:'+ model)
    print('Release：'+ release)
    print(wm)
    print(density)
    print('Android_id：'+android_id)
    print('SdkVersion：' + sdkVersion)

device_info()


