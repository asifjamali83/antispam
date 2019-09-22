#THAKS TO @shahzain786

from LineAPI.linepy import *
from LineAPI.akad.ttypes import Message
from LineAPI.akad.ttypes import ContentType as Type
#from LineAPI.akad.ttypes import ChatRoomAnnouncementC>
from LineAPI.akad.ttypes import ChatRoomAnnouncement
from datetime import datetime, timedelta
from time import sleep
from bs4 import BeautifulSoup
#from humanfriendly import format_timespan, format_siz>
#import time, random, multiprocessing, sys, json, code>
from gtts import gTTS
from googletrans import Translator

dz = LINE("")
int1 = len(dz.getGroupIdsInvited())
if int1 == 0:
    print("No groups inviting")
else:
    for groups in dz.getGroupIdsInvited():
        print("Reject " + dz.getGroup(groups).name)
        sleep(0.7)
        dz.rejectGroupInvitation(groups)
#    print("\nYou reject" + str(int1) + "groups invita>
