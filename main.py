from diaries.DiarySample import DiarySample
from diaries.KimuraDiary import KimuraDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), KimuraDiary()]
for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()