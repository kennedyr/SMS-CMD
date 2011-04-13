#
#SMS Parsing with google Voice
#
#Eric Kennedy
#ekennedy50@gmail.com
#

from googlevoice import Voice,util,settings
from BeautifulSoup import BeautifulSoup
import time,threading,sys
from pprint import pprint
import yaml

#global
"""
# Possibly going to implement threads for processing text messages
class VoiceThread ( threading.Thread ):
        def __init__(self, message):
                self.message = message
                threading.Thread.__init__ ( self )
        def run ( self ):
                print 'recieved this message: ', str(self.message)      
"""
class ConversationData:         
        #Scrape a Text Message conversation from voice.google.com
        #parameters: the HTML data, conversation ID
        #       #Adapted From:
        #       #SMS test via Google Voice
        #       #John Nagle
        #       #nagle@animats.com
        #
        def extractSMS(self,htmlsms, convID):
                 """
                 extractsms  --  extract SMS messages from BeautifulSoup tree of Google Voice SMS HTML.
                
                 Output is a list of dictionaries, one per message.
                 """
                 msgitems = []
                 # Extract all conversations by searching for a DIV with an ID at top level.
                 tree = BeautifulSoup(htmlsms)  # parse HTML into tree
                 conversations = tree.findAll("div",attrs={"id" : convID},recursive=False)
                 
                 for conversation in conversations :
                     # For each conversation, extract each row, which is one SMS message.
                     rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
                     
                     for row in rows :          # for all rows
                         # For each row, which is one message, extract all the fields.
                         msgitem = {"id" : conversation["id"]}          # tag this message with conversation ID
                         spans = row.findAll("span",attrs={"class" : True}, recursive=False)
                         
                         for span in spans :            # for all spans in row
                             cl = span["class"].replace('gc-message-sms-', '')
                             msgitem[cl] = (" ".join(span.findAll(text=True))).strip()  # put text in dict
                         msgitems.append(msgitem)       # add msg dictionary to list
                 return msgitems
                
        def newMessage( self, message ):
                con = convo.extractSMS(voice.sms.html, message.id)
                latest = con[0]
                msg = latest["text"]
                if msg[0] == '!':       # if the text is a command
                        commands.command_switch(msg)    #parse command
                        return True
                else:
                        return False
"""
        def fetch(self):        #fetch the sms from Google Voice
                for msg in convo.extractSMS(voice.sms.html):
                        #list.append({'id': msg['id'], 'text': msg['text']})
                        print msg['id']
                        print msg['text']
                        print msg['time']
                        print msg['from']
                for message in voice.sms().messages:
                        print "ID: " + str(message.id) + "\n"
                        print "phoneNumber: " + str(message.phoneNumber) + "\n"
                        print "displayNumber: " + str(message.displayNumber) + "\n"
                        print "startDateTime: " + str(message.displayStartDateTime) + "\n"
                        print "isRead: " + str(message.isRead) + "\n"
                        print "isTrash: " + str(message.isTrash) + "\n"
"""
"""
Command Structure:
![command] [arg1] [arg2]... [argN]
"""
class Commands:
        def gmap(self, args):
                print "funct1"
        def funct2(self, args):
                print "funct2"
        def funct3(self, args):
                print "funct3"
        def default(self):
                print "no such command"
        def command_switch(self, command):
                args = command[1:].lower().split()
                switch = {
                        'map': gmap(args),
                        'command2': funct2(args),
                        'command3': funct3(args)
                        }
                switch.get(args[0], default)()
                
class GoogleMaps:
        def getRequest(self, query):
                query = parseRequest(query)
                extractDirections(urllib2.urlopen("http://maps.google.com/?q=" + "%20".join(query)))

        def parseRequest(self, commands):
                if "from" in commands:
                        return commands.append("from 49428")
        def extractDirections(self, page):
                
                 diritems = {}
                 dirs = []
                 
                 tree = BeautifulSoup(page)     # parse HTML into tree
                 dirpanel = tree.findAll("div",attrs={"id" : "panel_dir"},recursive=False)
                 diritems["title"] = dirpanel.find("div", attrs={"id" : "dir_title"})
                
                 for conversation in conversations:
                     # For each conversation, extract each row, which is one SMS message.
                     rows = conversation.findAll(attrs={"class" : "gc-message-sms-row"})
                     for row in rows :                                                  # for all rows
                         # For each row, which is one message, extract all the fields.
                         msgitem = {"id" : conversation["id"]}                  # tag this message with conversation ID
                         spans = row.findAll("span",attrs={"class" : True}, recursive=False)
                         for span in spans :                                            # for all spans in row
                             cl = span["class"].replace('gc-message-sms-', '')
                             msgitem[cl] = (" ".join(span.findAll(text=True))).strip()  # put text in dict
                         msgitems.append(msgitem)                                       # add msg dictionary to list
#main - Run Once                
voice = Voice()
voice.login("ekennedy50", "kennedymko06tfc")
voice.sms()
convo = ConversationData()
commands = Commands()
"""
for thing in voice.sms().messages:
        print "\n\n" 
        pprint(convo.extractSMS(voice.sms.html, thing.id))
"""
while True:
        for message in voice.sms().messages:
                if not message.isRead: 
                        if(convo.newMessage(message)):          #if it contains a command (starts with a !)
                                message.mark()
                                message.delete()
        time.sleep(30)

