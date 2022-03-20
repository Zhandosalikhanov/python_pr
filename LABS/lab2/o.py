l = ["ONE", "TWO", "THR", "FOU", "FIV", "SIX", "SEV", "EIG", "NIN"]
num_to_char = {
}
char_to_num = {
}
i = 1
for c in l:
    num_to_char.update({i: c})
    char_to_num.update({c: i})
    i += 1

num_to_char.update({0: "ZER"})
char_to_num.update({"ZER": 0})

def tr_ch_to_num(string):
    tem_l = []
    for c in range(3, len(string) + 1, 3):
        tem_l.append(str(char_to_num[str(string[c - 3 : c])]))
    st = ""
    st = st.join(tem_l)
    return st

def tr_num_to_ch(my_list):
    tem_s = ""
    for c in my_list:
        tem_s += num_to_char[int(c)]
    return tem_s

def str_to_list(string):
    tem_l = []
    tem_l[: 0] = string
    return tem_l

s = input().split('+')
Sum = str(int(tr_ch_to_num(s[0])) + int(tr_ch_to_num(s[1])))
ans = tr_num_to_ch(str_to_list(Sum))
print(ans)