from diaries.DiarySample import DiarySample
from diaries.KimuraDiary import KimuraDiary
from diaries.SakashitaDiary import SakashitaDiary
# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), KimuraDiary(), SakashitaDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()