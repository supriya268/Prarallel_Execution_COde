'''
This file Fetches  required device details of all connected devices.
'''
class ParseFile():
    '''
       methodname:parseDeviceFile()
       description: required device info is written to parseDeviceDetails
       arguments: Nothing
       returns: Nothing
       '''
    def parseDeviceFile(self):
        deviceInfo=["ro.system.build.version.release","ro.serialno","ro.product.device"]
        with open("devicesDetails.txt") as deviceDetails, open('parseDeviceDetails.txt','w') as parsedInfo:
            for line in deviceDetails:
                if any(deviceInformation in line for deviceInformation in deviceInfo):
                    parsedInfo.write(line)

    '''
          methodname:fetchDeviceDetails()
          description:  Device details of each device is fetched using slicing
          arguments:Nothing
          returns: udid,platformVersion,deviceName

          '''


    def fetchDeviceDetails(self):
        self.parseDeviceFile()
        requiredDeviceDetails=[]
        with open('parseDeviceDetails.txt','r') as parsedInfo:
            for line in parsedInfo:
               requiredDeviceDetails.append(line)
        # print(requiredDeviceDetails)
        udid=None
        platformVersion=None
        deviceName=None
        for details in requiredDeviceDetails:
            if "system" in details:
                platformVersion=details[details.index(":")+3:len(details)-2]
            if "serial" in details:
                udid=details[details.index(":")+3:len(details)-2]
            if "device" in details:
                deviceName=details[details.index(":")+3:len(details)-2]
        # print(udid,platformVersion,deviceName)
        return udid,platformVersion,deviceName

# def fetchMultipleDeviceDetails:
# obj=ParseFile()
# udid,platformVersion,deviceName=obj.fetchDeviceDetails()
# print(udid[0],platformVersion[0],deviceName[0])