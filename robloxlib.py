import requests
import json
def checkFriends(userid1, userid2):
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method=IsFriendsWith&playerId="+str(userid1)+"&userId="+str(userid2))
    if "true" in r.text:
        return True
    else:
        return False
def userInGroup(mode, userid, groupid):
    #modes: GetGroupRank (number of rank), IsInGroup, GetGroupRole (rank name)
    r = requests.get("https://www.roblox.com/Game/LuaWebService/HandleSocialRequest.ashx?method="+str(mode)+"&playerid="+str(userid)+"&groupid="+str(groupid))
    if mode == "GetGroupRank":
        r2 = r.text[22:]
        r3 = r2.split("<")
        r4 = r3[0]
        return str(r4)
    if mode == "IsInGroup":
        if "true" in r.text:
            return True
        else:
            return False
    if mode == "GetGroupRole":
        return r.text
def userOwnsAsset(userid, assetid):
    r = requests.get("https://api.roblox.com/Ownership/HasAsset?userId="+str(userid)+"&assetId="+str(assetid))
    if "false" in r.text:
        return False
    else:
        return True
def usernameTaken(username):
    r = requests.get("https://www.roblox.com/UserCheck/DoesUsernameExist?username="+str(username))
    if "true" in r.text:
        return True
    else:
        return False
