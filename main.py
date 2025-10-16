from diaries.DiarySample import DiarySample

from diaries.KimuraDiary import KimuraDiary
from diaries.SakashitaDiary import SakashitaDiary
from diaries.K24084Diary import K24084Diary
from diaries.AyanaDiary import AyanaDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [DiarySample(), KimuraDiary(), SakashitaDiary(),K24084Diary(),AyanaDiary()]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()