# ##################################################################### #
# Copyright © 2023 QA - Quantitative Analytics. All rights reserved.### #
# This file is part of the project 'QA - Quantitative Analytics'. ##### #
# Hence the latter remains the exclusive property of its author. ###### #
# Accordingly, no part of this document may be used or transmitted #### #
# in any form for professional, educational or commercial purposes #### #
# without the express permission of Matthieu Charrier. ################ #
# ##################################################################### #

from qapy.algebra.algebra import *

class IF:
    def __init__(self, p_event, p_spread_lhs = 0., p_spread_rhs = 0.):
        self.event = p_event
        self.spread_lhs = p_spread_lhs
        self.spread_rhs = p_spread_rhs
    def __init__(self, p_event, p_spread = 0.):
        self.event = p_event
        self.spread_lhs = p_spread
        self.spread_rhs = p_spread
    def __call__(self, lhs, rhs):
        if isinstance(lhs, float) and isinstance(rhs, float):
            return AIfThenElse(self.event, ADet(lhs), ADet(rhs))
        elif isinstance(lhs, float) and isinstance(rhs, A):
            return AIfThenElse(self.event, ADet(lhs), rhs)
        elif isinstance(rhs, float) and isinstance(lhs, A):
            return AIfThenElse(self.event, lhs, ADet(rhs))
        elif isinstance(lhs, A) and isinstance(rhs, A):
            return AIfThenElse(self.event, lhs, rhs)
        else:
            return CIfThenElse(self.event, lhs, rhs, self.spread_lhs, self.spread_rhs)
        
class IF_EXERCISED:
    def __init__(self, p_exercise_kind, p_exercise_date):
        self.exercise_kind = p_exercise_kind
        self.exercise_date = p_exercise_date
    def __call__(self, lhs, rhs):
        return CIfExerciseThenElse(self.exercise_kind, self.exercise_date, lhs, rhs)
class IF_CALLED(IF_EXERCISED):
    def __init__(self, exercise_date):
        super().__init__(True, exercise_date)
class IF_PUTTED(IF_EXERCISED):
    def __init__(self, exercise_date):
        super().__init__(False, exercise_date)

def SPOT(ticker, fixing_date, fixing_date_shift = ''):
    return AFix(ticker, fixing_date, '', fixing_date_shift)
def SPOT_COMPOSITE(ticker, fixing_date, composite_currency, fixing_date_shift = ''):
    return AFix(ticker, fixing_date, composite_currency, fixing_date_shift)
def REF(name, value):
    return ARef(name, value)
def CST(value):
    return ADet(value)
def AMOUNT(name):
    return ARefAm(name)
def POW(amount, power):
    return AHybOpRgt(ATypes.AHybOpRgtPowType, amount, power)
def ABS(amount):
    return AUnOp(ATypes.AUnOpAbsType, amount)
def COS(amount):
    return AUnOp(ATypes.AUnOpCosType, amount)
def SIN(amount):
    return AUnOp(ATypes.AUnOpSinType, amount)
def TAN(amount):
    return AUnOp(ATypes.AUnOpTanType, amount)
def LOG(amount):
    return AUnOp(ATypes.AUnOpLogType, amount)
def EXP(amount):
    return AUnOp(ATypes.AUnOpExpType, amount)
def SQRT(amount):
    return AUnOp(ATypes.AUnOpSqrtType, amount)
def MAX(lhs, rhs):
    if isinstance(lhs, float) or isinstance(lhs, int):
        return AHybOpLft(ATypes.AHybOpLftMaxType, lhs, rhs)
    elif isinstance(rhs, float) or isinstance(rhs, int):
        return AHybOpRgt(ATypes.AHybOpRgtMaxType, lhs, rhs)
    else:
        return ABinOp(ATypes.ABinOpMaxType, lhs, rhs)
def MIN(lhs, rhs):
    if isinstance(lhs, float) or isinstance(lhs, int):
        return AHybOpLft(ATypes.AHybOpLftMinType, lhs, rhs)
    elif isinstance(rhs, float) or isinstance(rhs, int):
        return AHybOpRgt(ATypes.AHybOpRgtMinType, lhs, rhs)
    else:
        return ABinOp(ATypes.ABinOpMinType, lhs, rhs)
def CST(value):
    return EDet(value)
def BUY(transaction_date, quantity, cashflow):
    return CBuySell(transaction_date, +1, quantity, cashflow)
def SELL(transaction_date, quantity, cashflow):
    return CBuySell(transaction_date, -1, quantity, cashflow)
def END():
    return CNot()
def PAY(amount, payment_date, payment_currency):
    if isinstance(amount, float) or isinstance(amount, int):
        return CPayRec(payment_date, payment_currency, ADet(amount), +1)
    else:
        return CPayRec(payment_date, payment_currency, amount, +1)
def RECEIVE(amount, payment_date, payment_currency):
    if isinstance(amount, float) or isinstance(amount, int):
        return CPayRec(payment_date, payment_currency, ADet(amount), -1)
    else:
        return CPayRec(payment_date, payment_currency, amount, -1)
def SET(name, amount):
    return CSet(name, amount)
def CASHFLOW(file):
    return CRef(file)
def OBSERVE(observation_date, amount):
    return O(observation_date, amount)

def CONTRACT(file, cashflow):
    try:
        with open(file, "w") as stream:
            cashflow.write(stream)
            stream.close()
            return True
    except FileNotFoundError:
        print(f'Cannot find file {file}')
        return False
    
def OBSERVABLE(file, observables):
    try :
        with open(file, "w") as stream:
            na = 0
            ne = 0
            no = 0
            for observable in observables:
                no += 1
                observable_na, observable_ne = observable.count()
                na += observable_na
                ne += observable_ne
            stream.write(f'{na} {ne} {no}\n')
            for observable in observables:
                observable.write(stream)
            stream.close()
            return True
    except FileNotFoundError:
        print(f'Cannot find file {file}')
        return False