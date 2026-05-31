
# -----------------------------
# تعریف یک لیست از اعداد
# -----------------------------
number = [5, 6, 6, 7, 9]

# len() تعداد اعضای لیست را برمی‌گرداند
print(f"Length: {len(number)}")

# min() کوچک‌ترین عضو لیست را پیدا می‌کند
# چون با متن ترکیب شده از str استفاده کرده‌ایم
print(f"min: " + str(min(number)))

# max() بزرگ‌ترین عضو لیست را پیدا می‌کند
print(max(number))

# بررسی می‌کند آیا عدد 6 داخل لیست وجود دارد یا نه
# خروجی True یا False خواهد بود
print(6 in number)

# set() داده‌های تکراری را حذف می‌کند
# sorted() لیست را مرتب می‌کند
#print(list(set(number)))
print(sorted(set(number)))

# clear() همه اعضای لیست را حذف می‌کند
#number.clear()
#print(number)


# Slicing (برش لیست)


# از اندیس 1 تا قبل از 4
sub = number[1:4]

# برعکس کردن لیست
# [شروع : پایان : گام]
# گام -1 یعنی از آخر به اول
sub_1 = number[::-1]

print(sub_1)

# پیدا کردن اندیس اولین عدد 6
print(f"index: {number.index(6)}")

# اتصال دو لیست با +
new = number + [3, 4]

print(new)


# حلقه for

magicians = ['ali', 'david', 'hamid']

# حلقه روی اعضای لیست حرکت می‌کند
for m in magicians:

    # title() حرف اول را بزرگ می‌کند
    print(m.title() + ", that was a good trick!")


# range(start, stop, step)

# شروع از 2
# تا قبل از 10
# با گام 2
for i in range(2,10,2):
    print(i)

# ساخت لیست مربع اعداد

squares = []

for value in range(1,11):

    # توان 2
    square = value ** 2

    # افزودن عضو به لیست
    squares.append(square)

print(squares)


# List Comprehension

# روش کوتاه‌تر برای ساخت لیست
squares = [value ** 2 for value in range(1,5)]

print(squares)


# تبدیل دمای سانتی‌گراد به فارنهایت

temp_c = [0, 10, 20, 30]

# فرمول تبدیل:
# F = (9/5) * C + 32
temp_f = [(9/5) * c + 32 for c in temp_c]

print(f"F: {temp_f}")


# گرفتن طول کلمات

words = ["apple", "banana", "kiwi"]

# len(word) تعداد کاراکترهای هر کلمه را می‌دهد
lengths = [len(word) for word in words]

print(lengths)




