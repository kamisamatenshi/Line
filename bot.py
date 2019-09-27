# -*- coding: utf-8 -*-
import LineAlpha
from LineAlpha.lib.curve.ttypes import *
from datetime import datetime
# from imgurpython import ImgurClient - Digunain kalo make imgur buat upload image
import time,random,sys,json,codecs,threading,glob,os,subprocess,multiprocessing

#login type bisa, token, qr
#bot.login(qr=True)
#bot.login(token="AuthToken")

cl = LineAlpha.LINE()
cl.login(token="U1afa490979eb023cf3ed0db8c233f61e")
cl.loginResult()

kk = LineAlpha.LINE()
kk.login(token="U1afa490979eb023cf3ed0db8c233f61e")
kk.loginResult()

ki = LineAlpha.LINE()
ki.login(token="U1afa490979eb023cf3ed0db8c233f61e")
ki.loginResult()

kc = LineAlpha.LINE()
kc.login(token="U1afa490979eb023cf3ed0db8c233f61e")
kc.loginResult()

kg = LineAlpha.LINE()
kg.login(token="U1afa490979eb023cf3ed0db8c233f61e")
kg.loginResult()

#selfbot (akun sendiri) cuman dibutuhin kalo mau auto join kalo di kick

adm = LineAlpha.LINE()
adm.login(token="U1afa490979eb023cf3ed0db8c233f61e")
adm.loginResult()

#imgur stuff
# client_id = ''
# client_secret = ''
# access_token = ''
# refresh_token = ''

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

# album = None
# image_path = 'tmp/tmp.jpg'

# kk=ki=kc=cl

helpMessage ="""Haku bot(s) Command list:

Use Prefix 「Ar」 to use the Bot(s)
Prefix is Case sensitive but the commands is not.

[Gid] - Show Group ID
[Mid all] - Show all the Bot(s) MID
[Bot 1/2/3/4/5] - Shows the specific Bot MID
[Bot all] - Show all the Bot(s) Contact
[Bot 1/2/3/4/5] - Shows the specific Bot Contact
[Yid] - Show your ID
[Contact 「mid」] - Give Contact by MID
[Join on/off] - Auto join group
[Leave on/off] - Allows the bot to leave the group

[*] Command in the groups [*]
[Ginfo] - Group Info
[Banlist] - Check Banlist
[Cancel] - Cancel all pending(s) invitation
[Stalk 「ID」] - Upload lastest instagram picture from ID

[*] Admin and Staff Commands [*]
[Absen] - Check if bot is Online
[Glink on/off] - Turn invitation link for group on/off
[Cancel on/off] - Turn auto cancel invite on/off 
[Gn 「group name」] - Change Group Name
[Sp/Speed] - Check bot response speed
[Random:「A」] - Randomize group name A times
[Bc 「text」] - Let the bot send a text

[*] Admin only Commands [*]
[Cleanse] - Clear all members in the group
[Bye all] - Bot Leave
[Ban 「@」] - Ban By Tag
[Unban 「@」] - Unban By Tag
[Ban] - By Sharing Contact
[Unban] - By Sharing Contact
[Kill ban] - Kick all banned contact(s)
[Staff add/remove @] - Add or Remove Staff By Tag
"""

KAC=[cl,ki,kk,kc,kg]
mid = cl.getProfile().mid
Amid = kk.getProfile().mid
Bmid = ki.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kg.getProfile().mid
Bots = [mid,Amid,Bmid,Cmid,Dmid]
#nyalain bot dulu baru ketik "Ar Yid buat ngedapetin MID akun line mu"
admin = ["U1afa490979eb023cf3ed0db8c233f61e"]
staff = ["U1afa490979eb023cf3ed0db8c233f61e"]
adminMID = "U1afa490979eb023cf3ed0db8c233f61e"
wait = {
    'contact':True,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Thanks for add me",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":True,
    "cName":"Haku",
    "cName2":"Haku BOT2",
    "cName3":"Haku BOT3",
    "cName4":"Haku BOT4",
    "cName5":"Haku BOT5",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protectionOn":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

cancelinvite = {
    'autoCancel':True,
    'autoCancelUrl':True
}

setTime = {}
setTime = wait2['setTime']

#imgur stuff too
# def upload_tempimage(client):
#     '''
#         Upload a picture of a kitten. We don't ship one, so get creative!
#     '''

#     # Here's the metadata for the upload. All of these are optional, including
#     # this config dict itself.
#     config = {
#         'album': album,
#         'name':  'bot auto upload',
#         'title': 'bot auto upload',
#         'description': 'bot auto upload'
#     }

#     print("Uploading image... ")
#     image = client.upload_from_path(image_path, config=config, anon=False)
#     print("Done")
#     print()

#     return image


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = cl.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass


def bot(op):
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if cancelinvite["autoCancelUrl"] == True:
                if cl.getGroup(op.param1).preventJoinByTicket == False:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        cl.reissueGroupTicket(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        print "Url Opened, Autokick on"
                else:
                    print "random group update"
            else:
                pass

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    print "BOT 1 Joined"
                else:
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    kk.acceptGroupInvitation(op.param1)
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"

            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    print "BOT 3 Joined"
                else:
                    print "autoJoin is Off"

            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    kc.acceptGroupInvitation(op.param1)
                    print "BOT 4 Joined"
                else:
                    print "autoJoin is Off"
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    kg.acceptGroupInvitation(op.param1)
            else:
                if cancelinvite["autoCancel"] == True:
                    try:
                        X = cl.getGroup(op.param1)
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(op.param1, gInviMids)
                        print gInviMids + "invite canceled"
                    except:
                        try:
                            print "Retry canceling invitation"
                            X = random.choice(KAC).getGroup(op.param1)
                            gInviMids = [contact.mid for contact in X.invitee]
                            random.choice(KAC).cancelGroupInvitation(op.param1, gInviMids)
                            print gInviMids + "invite canceled"
                        except:
                            print "Bot can't cancel the invitation"
                            pass

        if op.type == 15:
            random.choice(KAC).sendText(op.param1, "Good Bye :)")
            print op.param3 + "has left the group"

        if op.type == 17:
            if op.param3 in wait["blacklist"]:
                try:
                    cl.kickoutFromGroup(op.param1, op.param3)
                except:
                    random.choice(KAC).kickoutFromGroup(op.param1, op.param3)

        if op.type == 19:
            print "someone was kicked"
            if op.param3 in admin:
                print "Admin has been kicked"
                if op.param2 in Bots:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        adm.acceptGroupInvitation(op.param1)
                print "Admin Joined"      

            if mid in op.param3:
                print "BOT1 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kk.inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        cl.acceptGroupInvitation(op.param1)
                    print "BOT1 Joined"

            if Amid in op.param3:
                print "BOT2 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        ki.inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kk.acceptGroupInvitation(op.param1)
                    print "BOT2 Joined"

            if Bmid in op.param3:
                print "BOT3 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kc.inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        ki.acceptGroupInvitation(op.param1)
                    print "BOT3 Joined"

            if Cmid in op.param3:
                print "BOT4 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        kg.inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kc.acceptGroupInvitation(op.param1)
                    print "BOT4 Joined"

            if Dmid in op.param3:
                print "BOT5 has been kicked"
                if op.param2 in Bots:
                    pass
                if op.param2 in admin:
                    pass
                else:
                    cl.kickoutFromGroup(op.param1,[op.param2])
                    wait["blacklist"][op.param2] = True
                    print "kicker kicked"
                    try:
                        cl.inviteIntoGroup(op.param1,op.param3)
                        kg.acceptGroupInvitation(op.param1)
                    except:
                        random.choice(KAC).inviteIntoGroup(op.param1,op.param3)
                        kg.acceptGroupInvitation(op.param1)
                    print "BOT5 Joined"

            else:
                cl.kickoutFromGroup(op.param1,[op.param2])
                kk.kickoutFromGroup(op.param1,[op.param2])
                ki.kickoutFromGroup(op.param1,[op.param2])
                kc.kickoutFromGroup(op.param1,[op.param2])
                kg.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
                print "autokick executed"

        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
                print "BOT(s) Leaving chat Room"

        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"Already in the Blacklist")
                        wait["wblacklist"] = False
                        print "MID Already in the Blacklist"
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Added to the Blacklist")
                        print [msg.contentMetadata["mid"]] + " Added to the Blacklist"

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Deleted from the Blacklist")
                        wait["dblacklist"] = False
                        print [msg.contentMetadata["mid"]] + " Removed from the Blacklist"

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Contact not in Blacklist")
                        print "MID not in blacklist"
               elif wait["contact"] == True:
                    if msg.from_ in admin:
                        msg.contentType = 0
                        if 'displayName' in msg.contentMetadata:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[Display Name]:\n" + msg.contentMetadata["displayName"] + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
                        else:
                            contact = cl.getContact(msg.contentMetadata["mid"])
                            try:
                                cu = cl.channel.getCover(msg.contentMetadata["mid"])
                            except:
                                cu = ""
                            cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n\n[MID]:\n" + msg.contentMetadata["mid"] + "\n\n[Status Message]:\n" + contact.statusMessage + "\n\n[Profile Picture]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\n[Cover Picture]:\n" + str(cu))
                            print "Contact sent"
#-----------------------[Help Section]------------------------                
            elif msg.text in ["haku /help","Help"]:
                if wait["lang"] == "JP":
                    random.choice(KAC).sendText(msg.to,helpMessage)
                    print "[Command]/help executed"
                else:
                    cl.sendText(msg.to,helpt)
#-----------------------[Group Name Section]------------------------
            elif "haku gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("haku gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
            elif "Haku gn " in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.name = msg.text.replace("Haku gn ","")
                        random.choice(KAC).updateGroup(X)
                        print "[Command]Gn executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
                    print "Gn executed outside group chat"
#-----------------------[Kick Section]------------------------
            elif "haku kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("haku kick ","")
                    cl.sendText(msg.to,"Good bye.")
                    random.choice(KAC).kickoutFromGroup(msg.to,[midd])
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif "Haku kick " in msg.text:
                if msg.from_ in admin:
                    midd = msg.text.replace("Haku kick ","")
                    cl.sendText(msg.to,"Good bye.")
                    random.choice(KAC).kickoutFromGroup(msg.to,[midd])
                    print "[Command]Kick executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Haku kill ban","haku kill ban"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        group = cl.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        if matched_list != []:
                            cl.sendText(msg.to,"Blacklisted contact noticed...")
                            cl.sendText(msg.to,"Begin Kicking contact")
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            cl.sendText(msg.to,"It looks empty here.")
                            return
                        for jj in matched_list:
                            random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        print "[Command]Kill ban executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Send Profile Section]------------------------                    
            elif msg.text in ["Haku bot all","haku bot all"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot all executed"

            elif msg.text in ["Haku bot 1","haku bot 1"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                print "[Command]Bot 1 executed"

            elif msg.text in ["Haku bot 2","haku bot 2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                kk.sendMessage(msg)
                print "[Command]Bot 2 executed"

            elif msg.text in ["Haku bot 3","haku bot 3"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                ki.sendMessage(msg)
                print "[Command]Bot 3 executed"

            elif msg.text in ["Haku bot 4","haku bot 4"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                print "[Command]Bot 4 executed"

            elif msg.text in ["Haku bot 5","haku bot 5"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                kg.sendMessage(msg)
                print "[Command]Bot 5 executed"
#-----------------------[Cancel invitation Section]------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:                    
                    X = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"Canceling all pending(s) invitation")
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        print "[Command]Cancel executed"
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"This group doesn't have any pending invitation")
                            print "[Command]Group don't have pending invitation"
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "Cancel executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group link Section]------------------------                        
            elif msg.text in ["Haku Glink off","Haku Link off","Haku glink off","haku link off"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = True
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned off")
                            print "[Command]Glink off executed"
                        else:
                            cl.sendText(msg.to,"Already turned off")
                            print "[Command]Glink off executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink off executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Haku Glink on","Haku Link on","Haku glink on","haku link on"]:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        X = cl.getGroup(msg.to)
                        X.preventJoinByTicket = False
                        cl.updateGroup(X)
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation link turned on")
                            print "[Command]Glink on executed"
                        else:
                            cl.sendText(msg.to,"Already turned on")
                            print "[Command]Glink on executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Glink on executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Group info Section]------------------------
            elif msg.text in ["Haku Ginfo","haku ginfo"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\nMembers:" + str(len(ginfo.members)) + "\nPending:" + sinvitee)
                        print "[Command]Ginfo executed"
                    else:
                        random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Status]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                        print "[Command]Ginfo executed"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                        print "[Command]Ginfo executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[Bot/User/Group ID Section]------------------------
            elif msg.text in ["Haku Gid","haku gid"]:
                cl.sendText(msg.to,msg.to)
                print "[Command]Gid executed"
            elif msg.text in ["Haku mid all","haku mid all"]:
                cl.sendText(msg.to,"[Ardh-]Bot(s) ID\n[Ardh-]BOT1\n" + mid + "\n\n[Ardh-]BOT2\n" + Amid + "\n\n[Ardh-]BOT3\n" + Bmid + "\n\n[Ardh-]BOT4\n" + Cmid + "\n\n[Ardh-]BOT5\n" + Dmid)
                print "[Command]Mid executed"
            elif msg.text in ["Haku Mid 1","haku mid 1"]:
                cl.sendText(msg.to,mid)
                print "[Command]Mid 1 executed"
            elif msg.text in ["Haku Mid 2","haku mid 2"]:
                kk.sendText(msg.to,Amid)
                print "[Command]Mid 2 executed"
            elif msg.text in ["Haku Mid 3","haku mid 3"]:
                ki.sendText(msg.to,Bmid)
                print "[Command]Mid 3 executed"
            elif msg.text in ["Haku Mid 4","haku mid 4"]:
                kc.sendText(msg.to,Cmid)
                print "[Command]Mid 4 executed"
            elif msg.text in ["Haku Mid 5","haku mid 5"]:
                kc.sendText(msg.to,Dmid)
                print "[Command]Mid 5 executed"
            elif msg.text in ["Haku Yid","haku yid"]:
                cl.sendText(msg.to,msg.from_)
                print "[Command]Yid executed"
#-----------------------[Send Contact Section]------------------------
            elif "Haku Contact" in msg.text:
                mmid = msg.text.replace("Haku Contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
            elif "haku contact" in msg.text:
                mmid = msg.text.replace("haku contact ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
                print "[Command]Contact executed"
#-----------------------[Auto Join Section]------------------------
            elif msg.text in ["Haku Join on","haku join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join already on")
                        print "[Command]Join on executed"
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned on")
                        print "[Command]Join on executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned on")
                        print "Join on executed"
            elif msg.text in ["Haku Join off","haku join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join already off")
                        print "[Command]Join off executed"
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
                    else:
                        cl.sendText(msg.to,"Auto join turned off")
                        print "[Command]Join off executed"
#-----------------------[Group Url Section]------------------------
            elif msg.text in ["Haku Gurl","haku gurl"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        x = cl.getGroup(msg.to)
                        if x.preventJoinByTicket == True:
                            x.preventJoinByTicket = False
                            cl.updateGroup(x)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)
                        print "[Command]Gurl executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                        print "[Command]Gurl executed outside group chat"
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
#-----------------------[All bots join group Section]------------------------
            elif msg.text in ["kemarilah para haku","ikeh","baka","jitak"]:
                if msg.from_ in admin:
                    try:
                        ginfo = cl.getGroup(msg.to)
                        ginfo.preventJoinByTicket = False
                        cl.updateGroup(ginfo)

                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kg.acceptGroupInvitationByTicket(msg.to,Ticket)

                        ginfo = random.choice(KAC).getGroup(msg.to)
                        ginfo.preventJoinByTicket = True
                        random.choice(KAC).updateGroup(ginfo)
                    except:
                        print "Somethings wrong with the url"
                    print "[Command]Join all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
#-----------------------[Bot(s) Leave Section]------------------------
            elif msg.text in ["pulanglah para haku","bubar bubar","udah, pergi sana"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                            kk.leaveGroup(msg.to)
                            ki.leaveGroup(msg.to)
                            kc.leaveGroup(msg.to)
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye all executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Haku bot 1","haku bot 1"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = cl.getGroup(msg.to)
                        try:
                            cl.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 1 executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Haku bot 2","haku bot 2"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kk.getGroup(msg.to)
                        try:
                            kk.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 2 executed"
                    else:
                        kk.sendText(msg.to,"Command denied.")
                        kk.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Haku bot 3","haku bot 3"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = ki.getGroup(msg.to)
                        try:
                            ki.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 3 executed"
                    else:
                        ki.sendText(msg.to,"Command denied.")
                        ki.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Haku bot 4","haku bot 4"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kc.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 4 executed"
                    else:
                        kc.sendText(msg.to,"Command denied.")
                        kc.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"

            elif msg.text in ["Haku bot 5","haku bot 5"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        ginfo = kc.getGroup(msg.to)
                        try:
                            kg.leaveGroup(msg.to)
                        except:
                            pass
                        print "[Command]Bye bot 5 executed"
                    else:
                        kg.sendText(msg.to,"Command denied.")
                        kg.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Cleanse Section (USE AT YOUR OWN RISK!)]------------------------
            elif msg.text in ["Haku Cleanse","haku cleanse"]:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Cleanse executing"
                        _name = msg.text.replace("Cleanse","")
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        kk.sendText(msg.to,"Group cleansing begin")
                        kc.sendText(msg.to,"Goodbye :)")
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        # --------------[Bot and Admin MID]----------------
                        targets.remove(adminMID)
                        targets.remove(mid)
                        targets.remove(Amid)
                        targets.remove(Bmid)
                        targets.remove(Cmid)
                        targets.remove(Dmid)
                        # --------------[Bot and Admin MID]----------------
                        if targets == []:
                            ki.sendText(msg.to,"Not found.")
                        else:
                            for target in targets:
                                try:
                                    klist=[ki,kk,kc,cl,kg]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Group cleansed")
                        print "[Command]Cleanse executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
                        print "[Error]Command denied - Admin permission required"
#-----------------------[Ban/Unban Section]------------------------
            elif "haku ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("haku ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "haku unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("haku unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif "Haku ban @" in msg.text:
                    if msg.toType == 2:
                        if msg.from_ in admin:
                            print "[Command]Ban executed"
                            _name = msg.text.replace("Haku ban @","")
                            _nametarget = _name.rstrip('  ')
                            gs = ki.getGroup(msg.to)
                            gs = kk.getGroup(msg.to)
                            gs = kc.getGroup(msg.to)
                            gs = kg.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                                if _nametarget == g.displayName:
                                    targets.append(g.mid)
                            if targets == []:
                                ki.sendText(msg.to,"Contact not found")
                            else:
                                for target in targets:
                                    try:
                                        wait["blacklist"][target] = True
                                        f=codecs.open('st2__b.json','w','utf-8')
                                        json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                        cl.sendText(msg.to,"Added to Blacklist")
                                    except:
                                        ki.sendText(msg.to,"Error")
                        else:
                            cl.sendText(msg.to,"Command denied.")
                            cl.sendText(msg.to,"Admin permission required.")
            elif "Haku unban @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[Command]Unban executed"
                        _name = msg.text.replace("Haku unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = ki.getGroup(msg.to)
                        gs = kk.getGroup(msg.to)
                        gs = kc.getGroup(msg.to)
                        gs = kg.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            ki.sendText(msg.to,"Contact not found")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Added to Whitelist")
                                except:
                                    ki.sendText(msg.to,"Added to Whitelist")
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Admin permission required.")
            elif msg.text in ["Haku ban","haku ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Ban")
                    print "[Command]Ban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Haku unban","haku unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    cl.sendText(msg.to,"Send Contact to Unban")
                    print "[Command]Unban executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")
                    print "[Error]Command denied - Admin permission required"
            elif msg.text in ["Haku banlist","haku banlist"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"No user is Blacklisted")
                else:
                    cl.sendText(msg.to,"Blacklisted user(s)")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Banlist executed"
#-----------------------[Bot Speak Section]------------------------
            elif "haku bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("haku bc ","")
                    random.choice(KAC).sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            elif "Haku bc " in msg.text:
                if msg.from_ in staff:
                    bctxt = msg.text.replace("Haku bc ","")
                    cl.sendText(msg.to,(bctxt))
                    print "[Command]Bc executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Bot speed test Section]------------------------
            elif msg.text in ["Haku Sp all","Haku Speed all","haku sp all","haku speed all","sp"]:
                if msg.from_ in staff:

                    start = time.time()
                    cl.sendText(msg.to, "Bot 1 Processing Request")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))

                    start2 = time.time()
                    kk.sendText(msg.to, "Bot 2 Processing Request")                    
                    elapsed_time2 = time.time() - start2
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time2))
                    
                    start3 = time.time()
                    ki.sendText(msg.to, "Bot 3 Processing Request")                    
                    elapsed_time3 = time.time() - start3
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time3))
                    
                    start4 = time.time()
                    kc.sendText(msg.to, "Bot 4 Processing Request")                    
                    elapsed_time4 = time.time() - start4
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time4))
                    
                    start5 = time.time()
                    kg.sendText(msg.to, "Bot 5 Processing Request")                    
                    elapsed_time5 = time.time() - start5
                    kg.sendText(msg.to, "%sseconds" % (elapsed_time5))
                    print "[Command]Speed all executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku Sp 1","Haku Speed 1","haku sp 1","haku speed 1"]:
                if msg.from_ in staff: 
                    start = time.time()                   
                    cl.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 1 executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku Sp 2","Haku Speed 2","haku sp 2","haku speed 2"]:
                if msg.from_ in staff:
                    start = time.time()                    
                    kk.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    kk.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 2 executed"
                else:
                    kk.sendText(msg.to,"Command denied.")
                    kk.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Sp 3","Ar Speed 3","Ar sp 3","h speed 3"]:
                if msg.from_ in staff:
                    start = time.time()                   
                    ki.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    ki.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 3 executed"
                else:
                    ki.sendText(msg.to,"Command denied.")
                    ki.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku Sp 4","Haku Speed 4","haku sp 4","haku speed 4"]:
                if msg.from_ in staff: 
                    start = time.time()                   
                    kc.sendText(msg.to, "Progress...")                    
                    elapsed_time = time.time() - start
                    kc.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 4 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku Sp 5","Haku Speed 5","haku sp 5","haku speed 5"]:
                if msg.from_ in staff:    
                    start = time.time()                
                    kg.sendText(msg.to, "Progress...")                                       
                    elapsed_time = time.time() - start
                    kg.sendText(msg.to, "%sseconds" % (elapsed_time))
                    print "[Command]Speed 5 executed"
                else:
                    kc.sendText(msg.to,"Command denied.")
                    kc.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Auto Cancel Section]------------------------
            elif "haku staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("haku staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Haku staff add @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff add executing"
                    _name = msg.text.replace("Haku staff add @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.append(target)
                                cl.sendText(msg.to,"Added to the staff list")
                            except:
                                pass
                    print "[Command]Staff add executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "haku staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("haku staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif "Haku staff remove @" in msg.text:
                if msg.from_ in admin:
                    print "[Command]Staff remove executing"
                    _name = msg.text.replace("Haku staff remove @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Contact not found")
                    else:
                        for target in targets:
                            try:
                                staff.remove(target)
                                cl.sendText(msg.to,"Removed to the staff list")
                            except:
                                pass
                    print "[Command]Staff remove executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Admin permission required.")

            elif msg.text in ["Haku staff","haku staff"]:
                if staff == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Staff list:")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
#-----------------------[Auto cancel Section]------------------------
            elif msg.text in ["Haku cancel off","haku cancel off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == True:
                        cancelinvite["autoCancel"] = False
                        cl.sendText(msg.to, "Auto Cancel turned off")
                        print "[Command]Cancel off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Cancel off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku cancel on","haku cancel on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancel"] == False:
                        cancelinvite["autoCancel"] = True
                        cl.sendText(msg.to, "Auto Cancel turned on")
                        print "[Command]Cancel on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned on")
                        print "[Command]Cancel on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku url off","haku url off"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url off executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url off executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Ar Url on","Ar url on"]:
                if msg.from_ in staff:
                    if cancelinvite["autoCancelUrl"] == True:
                        cancelinvite["autoCancelUrl"] = False
                        cl.sendText(msg.to, "Auto Cancel Url turned off")
                        print "[Command]Url on executed"
                    else:
                        cl.sendText(msg.to, "Auto Cancel already turned off")
                        print "[Command]Url on executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
#-----------------------[Misc Section]-------------------------------------------
            elif "haku random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("haku random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.05)
                                group.name = name
                                random.choice(KAC).updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif "Haku Random:" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in staff:
                        strnum = msg.text.replace("Haku random:","")
                        source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                        try:
                            num = int(strnum)
                            group = cl.getGroup(msg.to)
                            for var in range(0,num):
                                name = "".join([random.choice(source_str) for x in xrange(10)])
                                time.sleep(0.01)
                                group.name = name
                                cl.updateGroup(group)
                        except:
                            cl.sendText(msg.to,"Error")
                        print "[Command]Random executed"
                    else:
                        cl.sendText(msg.to,"Command denied.")
                        cl.sendText(msg.to,"Staff or higher permission required.")
                        print "[Error]Command denied - staff or higher permission required"

            elif msg.text in ["Haku absen","haku absen","cek"]:
                if msg.from_ in staff:
                    cl.sendText(msg.to, "ok")
                    kk.sendText(msg.to, "ok")
                    ki.sendText(msg.to, "ok")
                    kc.sendText(msg.to, "ok")
                    kg.sendText(msg.to, "ok")
                    print "[Command]Absen executed"
                else:
                    cl.sendText(msg.to,"Command denied.")
                    cl.sendText(msg.to,"Staff or higher permission required.")
                    print "[Error]Command denied - staff or higher permission required"
            #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            # elif msg.text in ["Ar Kernel","Ar kernel"]:
            #     if msg.from_ in admin:
            #         botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
            #         cl.sendText(msg.to, botKernel)
            #         print "[Command]Kernel executed"
            #     else:
            #         cl.sendText(msg.to,"Command denied.")
            #         cl.sendText(msg.to,"Admin permission required.")
            #         print "[Error]Command denied - Admin permission required"

            # elif "Ar Stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Ar Stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         print "[Command]Stalk executed - success"

            # elif "Ar stalk " in msg.text:
            #     print "[Command]Stalk executing"
            #     stalkID = msg.text.replace("Ar stalk ","")
            #     subprocess.call(["instaLooter",stalkID,"tmp/","-n","1"])   
            #     files = glob.glob("tmp/*.jpg")
            #     for file in files:
            #         os.rename(file,"tmp/tmp.jpg")
            #     fileTmp = glob.glob("tmp/tmp.jpg")
            #     if not fileTmp:
            #         cl.sendText(msg.to, "Image not found, maybe the account haven't post a single picture or the account is private")
            #         print "[Command]Stalk executed - no image found"
            #     else:
            #         image = upload_tempimage(client)
            #         cl.sendText(msg.to, format(image['link']))
            #         subprocess.call(["sudo","rm","-rf","tmp/tmp.jpg"])
            #         print "[Command]Stalk executed - success"

            elif "haku img" in msg.text:
                path = "a.png"
                try:
                    cl.sendImage(msg.to, path)
                except:
                    cl.sendText(msg.to, "Failed to upload image")        

            else:
                if cl.getGroup(msg.to).preventJoinByTicket == False:
                    cl.reissueGroupTicket(msg.to)
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                else:
                    if msg.from_ in Bots:
                        pass
                    else:
                        print "No Action"
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = kk.getProfile()
                profile2.displayName = wait["cName2"]
                kk.updateProfile(profile2)

                profile3 = ki.getProfile()
                profile3.displayName = wait["cName3"]
                ki.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = kg.getProfile()
                profile5.displayName = wait["cName5"]
                kg.updateProfile(profile5)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()


while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
