# coding=utf-8

import time
from datetime import datetime

from tumbler.engine import MainEngine

from tumbler.event import EventEngine
from tumbler.event import (
    EVENT_MERGE_TICK,
    EVENT_LOG
)

from tumbler.constant import Exchange, Interval
from tumbler.event import EventEngine
from tumbler.engine import MainEngine
from tumbler.gateway.huobi import HuobiGateway
from tumbler.gateway.gateio import GateioGateway
from tumbler.gateway.okex import OkexGateway
from tumbler.apps.market_maker import MarketMakerApp
from tumbler.apps.monitor import MonitorApp
from tumbler.event import EVENT_LOG, EVENT_TRADE, Event
from tumbler.object import SubscribeRequest, TradeData
from tumbler.function import load_json

from tumbler.apps.backtester.backtesting import BacktestingEngine, BacktestingMode
from tumbler.apps.cta_strategy.strategies.adaptive_system_strategy import AdaptiveSystemV1Strategy


def run():
    setting = {
        "bar_window": 4,
        "apower": 0.75,
        "highthreshold": 0.5,
        "lowthreshold": 1.05
    }
    symbol = "btc_usdt"
    filename = "/Users/szh/git/personal_tumbler/run_tumbler/tools/produce_csv_data/.tumbler/{}_1h_1.csv".format(
        symbol)
    # filename = "/Users/szh/git/personal_tumbler/run_tumbler/tools/produce_csv_data/.tumbler/fix_{}_min1.csv".format(
    #     symbol)

    engine = BacktestingEngine()

    engine.set_parameters(vt_symbol=f"{symbol}.BINANCE", interval=Interval.HOUR.value,
                          start=datetime(2017, 11, 1, 8, 10), rate=0.001,
                          slippage=0.00, size=1, price_tick=0.00000001, capital=0, end=datetime(2022, 1, 29, 9, 50),
                          mode=BacktestingMode.BAR.value)

    engine.add_strategy(AdaptiveSystemV1Strategy, setting)
    engine.load_data(filename=filename)
    engine.run_backtesting()
    df = engine.calculate_result()
    engine.calculate_statistics()

    engine.show_chart()

    input()


if __name__ == "__main__":
    run()
