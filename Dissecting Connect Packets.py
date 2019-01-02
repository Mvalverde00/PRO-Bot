info = "448|9750872|100|0|253|253|410|413|219|431|20|15|30|20|17|15|30|20|25203425|0|None|M|210|162|304|317|159|204|Bnm567|8|17|29|19|14|3|10|232|80|383|Black Glasses|1|0|252|252|3|2|1|"
info2 = "94|579868|100|0|246|246|215|315|413|251|10|15|15|15|10|15|15|15|23473779|0|None|M|173|149|348|342|170|190|Generalmajtki|30|17|29|31|31|16|14|78|26|441|Leftovers|35|29|252|185|9|0|1|"

info = "19|5527949|32|0|69|0|70|294|56|403|15|10|15|5|15|9|15|5|87005|1|None|F|57|37|56|25|31|57|Generalmajtki|31|29|9|17|14|23|3|212|50|441|Leftovers|16|14|30|8|2|10|1|"
info2 = "130|1229459|100|0|314|314|437|73|56|415|15|20|15|10|15|20|15|10|26438887|0|None|M|383|181|189|150|220|214|Sneezie|31|6|1|23|10|7|3|96|22|441|Leftovers|252|51|84|75|20|28|1|"
"""
0: Pokemon Pokedex ID
1: Pokemon Unique ID No.
2: Pokemon Level
3: ????
4: Pokemon Max HP
5: Pokemon Current HP
6: Move 1 ID
7: Move 2 ID
8: Move 3 ID
9: Move 4 ID
10: Move 1 max PP
11: Move 2 max PP
12: Move 3 max PP
13: Move 4 max PP
14: Move 1 current PP
15: Move 2 current PP
16: Move 3 current PP
17: Move 4 current PP
18: Total EXP gained
19: (Possibly) Is Shiny
20: (Possibly) Status Condition
21: Gender
22: Attack
23: Defense
24: Speed
25: Special Attack
26: Special Defense
27: ????
28: Original Trainer
29: Attack IV
30: Defense IV
31: Speed IV
32: Special Attack IV
33: Special Defense IV
34: Health IV
35: ????
36: Happiness
37: ????
38: (Possibly) Nature ID
39: Held Item
40: Attack EV
41: Defense EV
42: Speed EV
43: Special Attack EV
44: Special Defense EV
45: Health EV
46: ???
"""


info = info.split('|')
info2 = info2.split('|')
for i in range(len(info)):
    print(str(i) + ": " + info[i] + ", " + info2[i])
