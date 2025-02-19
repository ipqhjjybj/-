# coding=utf-8

from datetime import datetime
from copy import copy

from tumbler.constant import Direction, Offset
from tumbler.function import FilePrint
from tumbler.service import ding_talk_service
import tumbler.function.risk as risk


class FutureSpotSpreadTemplate(object):
    author = ""
    class_name = "FutureSpotSpreadTemplate"

    inited = False
    trading = False

    # 订阅行情
    vt_symbols_subscribe = []

    # 参数列表
    parameters = []

    # 运行时  重点变量列表
    variables = []

    def __init__(self, fs_engine, strategy_name, settings):
        # 设置策略的参数
        if settings:
            d = self.__dict__
            for key in self.parameters:
                if key in settings:
                    d[key] = settings[key]

        self.fs_engine = fs_engine
        self.strategy_name = strategy_name

        self.variables = copy(self.variables)
        self.variables.insert(0, "inited")
        self.variables.insert(1, "trading")

        self.file_print = FilePrint(self.strategy_name + ".log", "strategy_run_log", mode="w")
        self.important_print = FilePrint(self.strategy_name + "_important.log", "important_strategy_log", mode="w")

        self.time_send_ding_msg = risk.TimeWork(60)

    def update_setting(self, setting):
        """
        Update strategy parameter wtih value in setting dict.
        """
        for name in self.parameters:
            if name in setting:
                setattr(self, name, setting[name])

    def write_log(self, msg):
        """
        Write a log message.
        """
        self.file_print.write(
            '{}:[{}]:{}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), self.strategy_name, msg))

    def write_important_log(self, msg):
        """
        Write important message
        """
        self.write_log(msg)
        self.important_print.write(
            '{}:[{}]:{}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), self.strategy_name, msg))

    def send_ding_msg(self, msg):
        if self.time_send_ding_msg.can_work():
            msg = '{}:[{}]:{}'.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), self.strategy_name, msg)
            ding_talk_service.send_msg(msg)

    def subscribe(self, contract):
        """
        subscribe
        """
        return self.fs_engine.subscribe(self, contract)

    def unsubscribe(self, contract):
        """
        unsubscribe
        """
        return self.fs_engine.unsubscribe(self, contract)

    def get_contract(self, vt_symbol):
        """
        获得合约信息 , 从 engine中
        """
        return self.fs_engine.get_contract(vt_symbol)

    def get_account(self, vt_account_id):
        """
        获得账户的信息 , 从 engine中
        """
        return self.fs_engine.get_account(vt_account_id)

    def get_position(self, vt_position_id):
        """
        获得position 期货持仓信息, 从engine
        """
        return self.fs_engine.get_position(vt_position_id)

    def batch_orders(self, reqs):
        """
        send batch orders to system
        """
        return []

    def cancel_orders(self, vt_order_ids):
        """
        cancel batch orders
        """
        pass

    def buy(self, symbol, exchange, price, volume, stop=False, lock=False):
        """
        Send buy order to open a long position.
        """
        return self.send_order(symbol, exchange, Direction.LONG.value, Offset.OPEN.value, price, volume, stop, lock)

    def sell(self, symbol, exchange, price, volume, stop=False, lock=False):
        """
        Send sell order to close a long position.
        """
        return self.send_order(symbol, exchange, Direction.SHORT.value, Offset.CLOSE.value, price, volume, stop, lock)

    def short(self, symbol, exchange, price, volume, stop=False, lock=False):
        """
        Send short order to open as short position.
        """
        return self.send_order(symbol, exchange, Direction.SHORT.value, Offset.OPEN.value, price, volume, stop, lock)

    def cover(self, symbol, exchange, price, volume, stop=False, lock=False):
        """
        Send cover order to close a short position.
        """
        return self.send_order(symbol, exchange, Direction.LONG.value, Offset.CLOSE.value, price, volume, stop, lock)

    def send_order(self, symbol, exchange, direction, offset, price, volume, stop=False, lock=False):
        """
        Send a new order.
        """
        if self.trading:
            if stop:
                vt_order_ids = self.fs_engine.send_order(self, symbol, exchange, direction, offset, price, volume,
                                                         stop=True, lock=lock)
                msg = "[send_stop_order] vt_order_ids:{} info:{},{},{},{},{},{}".format(vt_order_ids, symbol,
                                                                                        exchange, direction, offset,
                                                                                        price, volume)
                self.write_log(msg)
                return vt_order_ids
            else:
                vt_order_ids = self.fs_engine.send_order(self, symbol, exchange, direction, offset, price, volume)
                msg = "[send_order] vt_order_ids:{} info:{},{},{},{},{},{}".format(vt_order_ids, symbol,
                                                                                   exchange, direction, offset, price,
                                                                                   volume)
                self.write_log(msg)
                return vt_order_ids
        else:
            msg = "[send_order] trading condition is false!"
            self.write_log(msg)
            return []

    def cancel_order(self, vt_order_id):
        """
        Cancel an existing order.
        """
        if self.trading:
            self.fs_engine.cancel_order(self, vt_order_id)

    def get_parameters(self):
        """
        Get strategy parameters dict.
        """
        strategy_parameters = {}
        for name in self.parameters:
            strategy_parameters[name] = getattr(self, name)
        return strategy_parameters

    def get_variables(self):
        """
        Get strategy variables dict.
        """
        strategy_variables = {}
        for name in self.variables:
            strategy_variables[name] = getattr(self, name)
        return strategy_variables

    def get_data(self):
        """
        Get strategy data.
        """
        strategy_data = {
            "strategy_name": self.strategy_name,
            "class_name": self.__class__.__name__,
            "author": self.author,
            "parameters": self.get_parameters(),
            "variables": self.get_variables(),
        }
        return strategy_data

    def put_event(self):
        """
        Put an strategy data event for ui update.
        """
        if self.inited:
            self.fs_engine.put_strategy_event(self)

    def on_init(self):
        """
        Callback when strategy is inited.
        """
        pass

    def on_start(self):
        """
        Callback when strategy is started.
        """
        pass

    def on_stop(self):
        """
        Callback when strategy is stopped.
        """
        pass

    def on_merge_tick(self, merge_tick):
        """
        Callback of new merge tick data update.
        """
        pass

    def on_tick(self, tick):
        """
        Callback of new tick data update.
        """
        pass

    def on_trade(self, trade):
        """
        Callback of new trade data update.
        """
        pass

    def on_order(self, order):
        """
        Callback of new order data update.
        """
        pass

