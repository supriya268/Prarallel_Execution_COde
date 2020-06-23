'''
This file Fetches device details of all connected devices.
'''

import subprocess
import os
from Filefetching.parseFile import ParseFile

'''
class inhertis parsefile class and dynamically  fetches device details.
'''

class ADBCommands(ParseFile):
    udid=[]
    platformVersion=[]
    deviceName=[]

    '''
        methodname: getDeviceCount()
        description: which retrieves the list of connected devices using ADB commands
        arguments: nothing
        returns: nothing
    '''
    def getDeviceCount(self):
        subprocess.call("adb devices >deviceCount.txt",shell=True)

    '''
        methodname: fetchmultipledevice()
        description: This method count the number of device connected and fetches udid, platformVersion, deviceName
        arguments: nothing
        returns: udid,platformVersion,deviceName
    '''
    def fetchmultipledevice(self):
        self.getDeviceCount()
        # Opening a file
        file = open("deviceCount.txt", "r")
        # number of lines in a text file
        Counter = 0
        # Reading from file
        Content = file.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1
                counts = Counter - 1

        print(counts)

        for _ in range(0,counts):
            os.system("adb shell getprop >devicesDetails.txt")
            #Call to fetchDeviceDetails() method which is in parsefile.py
            udid,platformVersion,deviceName=self.fetchDeviceDetails()
            self.udid.append(udid)
            self.platformVersion.append(platformVersion)
            self.deviceName.append(deviceName)
        # print(self.udid[0],self.platformVersion[0],self.deviceName[0])
        return self.deviceName, self.platformVersion, self.udid
# obj=ADBCommands()
# obj.fetchmultipledevice()



