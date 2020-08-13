import os

# from strategies import *

import backtrader as bt


def run(data_filepath, output_filepath, strategy):
    if not os.path.exists(f"{output_filepath}"):
        os.mkdir(f"{output_filepath}")

    filename = os.path.basename(data_filepath)
    # strategy = eval(strategy_name)

    data0 = bt.feeds.BacktraderCSVData(dataname=data_filepath)
    cerebro = bt.Cerebro()
    cerebro.adddata(data0)
    cerebro.addstrategy(strategy)
    cerebro.addwriter(
        bt.WriterFile,
        csv=True,
        out=f"{output_filepath}/{os.path.splitext(filename)[0]}.csv",
    )
    cerebro.run()
