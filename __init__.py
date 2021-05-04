from modules import cbpi
from modules.core.props import Property
from modules.core.hardware import ActorBase
import requests
#import time

@cbpi.actor
class DefinedState(ActorBase):
    #custom property
    actordesc = "select an actor to control state"
    actor01 = Property.Actor("Actor 1", description=actordesc)
    actor01_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor02 = Property.Actor("Actor 2", description=actordesc)
    actor02_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor03 = Property.Actor("Actor 3", description=actordesc)
    actor03_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor04 = Property.Actor("Actor 4", description=actordesc)
    actor04_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor05 = Property.Actor("Actor 5", description=actordesc)
    actor05_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor06 = Property.Actor("Actor 6", description=actordesc)
    actor06_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor07 = Property.Actor("Actor 7", description=actordesc)
    actor07_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    actor08 = Property.Actor("Actor 8", description=actordesc)
    actor08_On_Off = Property.Select("On or OFF", options = ["On","Off"], description = "On or Off") 
    #ta_stop  = Property.Number("Pause Timer", configurable=True, description="Defines how long the Agitator should stop before run again.")
    
    def init(self):
        self.actors = []
        self.YesNo = []

        if isinstance(self.actor01, unicode) and self.actor01:
            self.actors.append(int(self.actor01))
            self.YesNo.append(self.actor01_On_Off)
        if isinstance(self.actor02, unicode) and self.actor02:
            self.actors.append(int(self.actor02))
            self.YesNo.append(self.actor02_On_Off)
        if isinstance(self.actor03, unicode) and self.actor03:
            self.actors.append(int(self.actor03))
            self.YesNo.append(self.actor03_On_Off)
        if isinstance(self.actor04, unicode) and self.actor04:
            self.actors.append(int(self.actor04))
            self.YesNo.append(self.actor04_On_Off)
        if isinstance(self.actor05, unicode) and self.actor05:
            self.actors.append(int(self.actor05))
            self.YesNo.append(self.actor05_On_Off)
        if isinstance(self.actor06, unicode) and self.actor06:
            self.actors.append(int(self.actor06))
            self.YesNo.append(self.actor06_On_Off)
        if isinstance(self.actor07, unicode) and self.actor07:
            self.actors.append(int(self.actor07))
            self.YesNo.append(self.actor07_On_Off)
        if isinstance(self.actor08, unicode) and self.actor08:
            self.actors.append(int(self.actor08))
            self.YesNo.append(self.actor08_On_Off)


    def set_power(self, power):
        for actor in self.actors:
            self.api.actor_power(actor, power=power)
	   #self.sleep(int(self.ta_stop))

    def on(self, power=None):
        i = 0
        for actor in self.actors:
            if self.YesNo[i] == "On":
                self.api.switch_actor_on(actor, power=power)
            else:
                self.api.switch_actor_off(actor)
            i = i+1
        #self.sleep(int(self.ta_stop))
        #self.api.cache.get("actors").get(int(self.id)).timer = int(time.time()) + int(self.ta_stop) -1
	#self.api.notify(headline="Timed Agitator", message="Timed Agitator started", type="info")

    def off(self):
        for actor in self.actors:
            self.api.switch_actor_off(actor)
        #self.sleep(int(self.ta_stop))

