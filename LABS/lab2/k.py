bad_char = {
    44 : '',
    33 : '',
    46 : '',
    63 : '',
}

s = input()
s = s.translate(bad_char)

st = {}
st = set(st)

words = s.split(' ')

for c in words:
    st.add(c)

words.clear()
for c in st:
    words.append(c)
words.sort()


print(len(words))
for i in words:
    print(i)