trip_dig = {
    "ZER": "0",
    "ONE": "1",
    "TWO": "2",
    "THR": "3",
    "FOU": "4",
    "FIV": "5",
    "SIX": "6",
    "SEV": "7",
    "EIG": "8",
    "NIN": "9"

}

dig_trip = {
    "0": "ZER",
    "1": "ONE",
    "2": "TWO",
    "3": "THR",
    "4": "FOU",
    "5": "FIV",
    "6": "SIX",
    "7": "SEV",
    "8": "EIG",
    "9": "NIN"
}

s = input()

if "+" in s:
    sign = "+"
elif "-" in s:
    sign = "-"
else:
    sign = "*"

parts = s.split(sign)
first = parts[0]
sec = parts[1]

num1 = ""
for i in range(0,len(first), 3):
    part = first[i:i+3]
    num1 += trip_dig[part]

num2 = ""
for i in range(0, len(sec), 3):
    part = sec[i:i+3]
    num2 += trip_dig[part]

num1 = int(num1)
num2 = int(num2)

if sign == "+":
    res = num1 + num2
elif sign == "-":
    res = num1 - num2
else:
    res = num1 * num2

res_trip = str(res)
ans = ""

for dig in res_trip:
    ans += dig_trip[dig]

print(ans)
