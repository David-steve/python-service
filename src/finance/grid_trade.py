"""
@Project: python-service
@File: grid_trade.py
@Author: David
@Date: 2025/6/4
@Brief: 网格交易
"""
from decimal import Decimal
from typing import List

from src.finance.modules import Stock, StockTrace


class GridTrade:
    def __init__(self, stock_code: str, base_price: float, top_price: float, bottom_price: float,
                 up_percent: float, down_percent: float, current_shares: int, max_share: int, min_share: int,
                 shares_per_time: int):
        """
        Constructor of GridTrade
        :param stock_code: 股票代码
        :param base_price: 基准价
        :param top_price: 上限价
        :param bottom_price: 下限价
        :param up_percent: 上涨百分比
        :param down_percent: 下降百分比
        :param current_shares: 当前持有数量
        :param max_share: 最大持有数量
        :param min_share: 最小持有数量
        :param shares_per_time: 每次操作的数量
        """
        self.stock_code = stock_code
        self.base_price = base_price
        self.top_price = top_price
        self.bottom_price = bottom_price
        self.up_percent = up_percent
        self.down_percent = down_percent
        self.current_shares = current_shares
        self.max_share = max_share
        self.min_share = min_share
        self.shares_per_time = shares_per_time

    def run(self, data: StockTrace):
        item = data
        high_price = item.high_price
        low_price = item.low_price

        # 判断当前价格是否在网格内
        if high_price > self.top_price:
            print("{} 价格太高 {}".format(item.date, item.high_price))
            return
        elif low_price < self.bottom_price:
            print("{} 价格太低 {}".format(item.date, item.low_price))
            return

        up_threshold = Decimal(self.base_price) * Decimal(1 + self.up_percent)
        down_threshold = Decimal(self.base_price) * Decimal(1 - self.down_percent)

        # 如果价格达到网格上涨设定百分比，且持有数量小于最大持有数量，则卖出
        if high_price >= up_threshold \
                and self.current_shares - self.shares_per_time >= self.min_share:
            self.base_price = high_price
            self.current_shares -= self.shares_per_time
            print("date {} Sell {} shares at {}  current shares {}"
                  .format(item.date, self.shares_per_time, self.base_price, self.current_shares))

        # 如果价格达到网格下跌设定百分比，且持有数量大于最小持有数量，则买入
        if low_price <= down_threshold \
                and self.current_shares + self.shares_per_time <= self.max_share:
            self.base_price = low_price
            self.current_shares += self.shares_per_time
            print("date {} Buy {} shares at {} current shares {}".
                  format(item.date, self.shares_per_time, self.base_price, self.current_shares))


def main():
    stock: Stock = Stock.objects.filter(name="比亚迪").first()
    if not stock:
        print('Stock not found')
        exit(1)

    records = StockTrace.objects.filter(stock=stock, date__gte='2018-08-02').order_by('date').all()
    grid_trade = GridTrade(stock_code=stock.code, base_price=90.910, top_price=280.0, bottom_price=30.0,
                           up_percent=0.03, down_percent=0.03, current_shares=500, max_share=10000, min_share=100,
                           shares_per_time=100)
    for record in records:
        grid_trade.run(record)


if __name__ == '__main__':
    main()
