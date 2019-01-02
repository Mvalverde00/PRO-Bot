"""
This program Decrypts Pokemon Revolution Online chat/text messages

Pokemon Revolution Online pairs together characters based on ASCII values.  A and @ are a pair, B and C are a pair, etc.  Characters in a message are switched with their partner
"""


def decode(plainText):
    #Shift in PRO is 1 character
    shift = 1
    
    cipherText = ""
    for ch in plainText:
        value = ord(ch)
        if value % 2 == 1:
            value -= 1
        else:
            value += 1
        cipherText += chr(value)
    return cipherText
print(decode("ql}/}Wnmndrrdnquhltr,<,@oesdvj200}/}@oesdvj200!r`xr;!lhih!onldo!dru!qnu`un}/]"))#v}/})@mm(!Zo<R`mhfh`\Z.o\;!jj!ehrodxm`oe!hr!uid!cdru!nquhno}/]TYhnn032}92}24}s10111111216365}11075}1111}1}/]"))               
print(decode("t.+5"))
print(decode("....3l"))
