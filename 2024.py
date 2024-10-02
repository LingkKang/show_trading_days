import csv
from enum import Enum

import pandas as pd

date_arr = pd.date_range(start="2024-01-01", end="2024-12-31").tolist()


class Trading(Enum):
    Open = 1
    Close = 2
    EarlyClose = 3


class TradingDayInfo:
    def __init__(self, trading_info: Trading) -> None:
        self.CHN_trading_info = trading_info
        self.HKG_trading_info = trading_info
        self.USA_trading_info = trading_info

    def list_repr(self) -> list[str]:
        lis = []
        if self.CHN_trading_info == Trading.Open:
            lis.append("CHN trading day")
        elif self.CHN_trading_info == Trading.Close:
            pass
        elif self.CHN_trading_info == Trading.EarlyClose:
            raise TypeError("CHN do not have early close")

        if self.HKG_trading_info == Trading.Open:
            lis.append("HKG trading day")
        elif self.HKG_trading_info == Trading.Close:
            pass
        elif self.HKG_trading_info == Trading.EarlyClose:
            lis.append("HKG trading day w/ early close")

        if self.USA_trading_info == Trading.Open:
            lis.append("USA trading day")
        elif self.USA_trading_info == Trading.Close:
            pass
        elif self.USA_trading_info == Trading.EarlyClose:
            lis.append("USA trading day w/ early close")

        return lis


# Initialize trading day info
trading_day_info = {}
for date in date_arr:
    if date.day_of_week < 5:
        # day of week starts from 0 (mon)
        trading_day_info[date] = TradingDayInfo(Trading.Open)
    else:
        # day of week is 5 (sat) or 6 (sun)
        trading_day_info[date] = TradingDayInfo(Trading.Close)

# ======== USA ========
# https://www.ca2.uscourts.gov/clerk/calendars/federal_holidays.html
# https://www.nasdaq.com/market-activity/stock-market-holiday-schedule
# https://www.nyse.com/markets/hours-calendars

usa_close_days = [
    "2024-01-01",  # New Year's Day
    "2024-01-15",  # MLK Jr. Day
    "2024-02-19",  # Presidents' Day
    "2024-04-19",  # Good Friday
    "2024-05-27",  # Memorial Day
    "2024-06-19",  # Juneteenth
    "2024-07-04",  # Independence Day
    "2024-09-02",  # Labor Day
    "2024-11-28",  # Thanksgiving Day
    "2024-12-25",  # Christmas Day
]

usa_early_close = [
    "2024-07-03",  # Before Independence Day
    "2024-11-29",  # Day after Thanksgiving
    "2024-12-24",  # Christmas Eve
]

usa_close_days = set(pd.to_datetime(usa_close_days))
usa_early_close = set(pd.to_datetime(usa_early_close))

for date in date_arr:
    if date in usa_close_days:
        trading_day_info[date].USA_trading_info = Trading.Close
    if date in usa_early_close:
        trading_day_info[date].USA_trading_info = Trading.EarlyClose

# ======== HKG ========
# https://www.gov.hk/en/about/abouthk/holiday/2024.htm
# https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Reference-Materials/Trading-Hour,-Trading-and-Settlement-Calendar/2024-Calendar_pdf_c.pdf
# https://www.hkex.com.hk/-/media/HKEX-Market/Services/Circulars-and-Notices/Participant-and-Members-Circulars/SEHK/2023/ce_SEHK_CT_079_2023.pdf
# https://www.bluestonehk.com/help/list?aid=38
# https://www.sinotrade.com.tw/Ovs/Ovs_6_4

hkg_close_days = [
    "2024-01-01",  # The first day of January
    "2024-02-12",  # The third day of Lunar New Year
    "2024-02-13",  # The fourth day of Lunar New Year
    "2024-03-29",  # Good Friday
    "2024-04-01",  # Easter Monday
    "2024-04-04",  # Ching Ming Festival
    "2024-05-01",  # Labour Day
    "2024-05-15",  # The Birthday of the Buddha
    "2024-06-10",  # Tuen Ng Festival
    "2024-07-01",  # Hong Kong Special Administrative Region Establishment Day
    "2024-09-18",  # The day following the Chinese Mid-Autumn Festival
    "2024-10-01",  # National Day
    "2024-10-11",  # Chung Yeung Festival
    "2024-12-25",  # Christmas Day
    "2024-12-26",  # The first weekday after Christmas Day
]

hkg_early_close = [
    "2024-02-09",  # Lunar New Year's Eve
    "2024-12-24",  # Christmas Eve
    "2024-12-31",  # New Year's Eve
]

hkg_close_days = set(pd.to_datetime(hkg_close_days))
hkg_early_close = set(pd.to_datetime(hkg_early_close))

for date in date_arr:
    if date in hkg_close_days:
        trading_day_info[date].HKG_trading_info = Trading.Close
    if date in hkg_early_close:
        trading_day_info[date].HKG_trading_info = Trading.EarlyClose

# ======== CHN ========
# https://www.gov.cn/zhengce/zhengceku/202310/content_6911528.htm
# https://english.www.gov.cn/policies/latestreleases/202310/25/content_WS65387be8c6d0868f4e8e0a04.html
# https://www.szse.cn/disclosure/notice/t20231226_605108.html
# https://www.sse.com.cn/disclosure/announcement/general/c/c_20231226_5733939.shtml

chn_close_days = [
    "2024-01-01",  # New Year's Day
    "2024-02-09",  # Spring Festival
    "2024-02-12",  # Spring Festival
    "2024-02-13",  # Spring Festival
    "2024-02-14",  # Spring Festival
    "2024-02-15",  # Spring Festival
    "2024-02-16",  # Spring Festival
    "2024-04-04",  # Qingming Festival
    "2024-04-05",  # Qingming Festival
    "2024-05-01",  # Labour Day
    "2024-05-02",  # Labour Day
    "2024-05-03",  # Labour Day
    "2024-06-10",  # Dragon Boat Festival
    "2024-09-16",  # Mid-Autumn Festival
    "2024-09-17",  # Mid-Autumn Festival
    "2024-10-01",  # National Day
    "2024-10-02",  # National Day
    "2024-10-03",  # National Day
    "2024-10-04",  # National Day
    "2024-10-07",  # National Day
]

chn_close_days = set(pd.to_datetime(chn_close_days))

for date in date_arr:
    if date in chn_close_days:
        trading_day_info[date].CHN_trading_info = Trading.Close

# ======== Write to CSV ========
with open("2024_trading_days.csv", "w", encoding="UTF-8", newline="") as f:
    csv_writer = csv.writer(
        f, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC
    )
    csv_writer.writerow(["Subject", "Start Date", "All Day Event"])
    for date in date_arr:
        info_list = trading_day_info[date].list_repr()
        for info in info_list:
            csv_writer.writerow([info, date.strftime("%m/%d/%Y"), "True"])

print("Done")
