import os
import commands

class Battery:

    def __init__(self, file_name = "/sys/class/power_supply/BAT0/uevent"):
        self.__file_name = file_name
        self.__percentage = None
        self.__status = None
        self.__imgpath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "batfull.png")

    @property
    def __read_file(self):
        self.fobj = open(self.__file_name)
        self.bat_details = self.fobj.readlines()
        self.fobj.close()
        return self.bat_details
    
    @property
    def bat_percentage(self):
        for detail in self.__read_file:
            if "POWER_SUPPLY_CAPACITY=" in detail:
                self.__percentage = detail.strip().split("=")[1]
                break
        return self.__percentage

    @property
    def bat_status(self):
        for detail in self.__read_file:
            if "POWER_SUPPLY_STATUS=" in detail:
                self.__status = detail.strip().split("=")[1]
                break
        return self.__status

    def notification(self, message="'Battery Full'"):
        status, output = commands.getstatusoutput("notify-send -i "+self.__imgpath+" "+ message)
