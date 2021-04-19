import math

import numpy as np

from data import Data


def run(data: Data):
    # 현금이 주식 평가금액보다 30% 이상 많아지면
    if data.money > data.valuation_amount * 1.3:
        # 현금이 많음으로 가진 현금의 15%를 주식 매수
        data.buy(15)
    # 반대로 현금이 주식 평가금액보다 30% 이상 적어지면
    elif data.money * 1.3 < data.valuation_amount:
        # 현금이 적음으로 가진 주식의 15%를 매도
        data.sell(15)

