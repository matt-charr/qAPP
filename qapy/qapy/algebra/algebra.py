# ##################################################################### #
# Copyright © 2023 QA - Quantitative Analytics. All rights reserved.### #
# This file is part of the project 'QA - Quantitative Analytics'. ##### #
# Hence the latter remains the exclusive property of its author. ###### #
# Accordingly, no part of this document may be used or transmitted #### #
# in any form for professional, educational or commercial purposes #### #
# without the express permission of Matthieu Charrier. ################ #
# ##################################################################### #

class CTypes:
    CBuySellType = 1
    CNotType = 2
    CPayRecType = 3
    CSetType = 4
    CRefType = 5
    CIfThenElseType = 6
    CIfExerciseThenElseType = 7
    CBinOpType = 8
class ETypes:
    EABinOpLeType = 0
    EAHybOpRgtLeType = 1
    EAHybOpLftLeType = 2
    EABinOpLtType = 3
    EAHybOpRgtLtType = 4
    EAHybOpLftLtType = 5
    EABinOpGeType = 6
    EAHybOpRgtGeType = 7
    EAHybOpLftGeType = 8
    EABinOpGtType = 9
    EAHybOpLftGtType = 10
    EABinOpEqType = 11
    EAHybOpRgtEqType = 12
    EAHybOpLftEqType = 13
    EABinOpNeqType = 14
    EAHybOpRftNeqType = 15
    EAHybOpLftNeqType = 16
    EBinOpAndType = 17
    EBinOpOrType = 18
    EUnOpNotType = 19
    EAHybOpRgtGtType = 20
    EDetType = 21
class ATypes:
    ABinOpAddType = 1
    AHybOpRgtAddType = 2
    AHybOpLftAddType = 3
    ABinOpSubType = 4
    AHybOpRgtSubType = 5
    AHybOpLftSubType = 6
    ABinOpMulType = 7
    AHybOpRgtMulType = 8
    AHybOpLftMulType = 9
    ABinOpDivType = 10
    AHybOpRgtDivType = 11
    AHybOpLftDivType = 12
    AFixType = 13
    ARefType = 14
    ADetType = 15
    ARefAmType = 16
    AHybOpRgtPowType = 17
    AUnOpAbsType = 18
    AUnOpCosType = 19
    AUnOpSinType = 20
    AUnOpTanType = 21
    AUnOpExpType = 22
    AUnOpLogType = 23
    AUnOpSqrtType = 24
    ABinOpMaxType = 25
    AHybOpRgtMaxType = 26
    AHybOpLftMaxType = 27
    ABinOpMinType = 28
    AHybOpRgtMinType = 29
    AHybOpLftMinType = 30
    AIfThenElseType = 31
    AUnOpSubType = 32
    AUnOpNegType = 33
    AUnOpPosType = 34

class A:
     s_cpt = 0
     def __init__(self, p_type):
          self.name = A.s_cpt
          A.s_cpt += 1
          self.type = p_type
     def count(self):
          raise NotImplementedError
     def write(self, f):
          self.write_internal(f)
     def write_internal(self, f):
          f.write(f'a {self.name} {self.type} ')
          self.write_internal_core(f)
     def __add__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return AHybOpRgt(ATypes.AHybOpRgtAddType, self, p_rhs)
          else:
               return ABinOp(ATypes.ABinOpAddType, self, p_rhs)
     def __radd__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return AHybOpLft(ATypes.AHybOpLftAddType, p_lhs, self)
          else:
               return ABinOp(ATypes.ABinOpAddType, p_lhs, self)
     def __sub__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return AHybOpRgt(ATypes.AHybOpRgtSubType, self, p_rhs)
          else:
               return ABinOp(ATypes.ABinOpSubType, self, p_rhs)
     def __rsub__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return AHybOpLft(ATypes.AHybOpLftSubType, p_lhs, self)
          else:
               return ABinOp(ATypes.ABinOpSubType, p_lhs, self)
     def __mul__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return AHybOpRgt(ATypes.AHybOpRgtMulType, self, p_rhs)
          else:
               return ABinOp(ATypes.ABinOpMulType, self, p_rhs)
     def __rmul__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return AHybOpLft(ATypes.AHybOpLftMulType, p_lhs, self)
          else:
               return ABinOp(ATypes.ABinOpMulType, p_lhs, self)
     def __truediv__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return AHybOpRgt(ATypes.AHybOpRgtDivType, self, p_rhs)
          else:
               return ABinOp(ATypes.ABinOpDivType, self, p_rhs)
     def __rtruediv__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return AHybOpLft(ATypes.AHybOpLftDivType, p_lhs, self)
          else:
               return ABinOp(ATypes.ABinOpDivType, p_lhs, self)
     def __le__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return EAHybOpRgt(ETypes.EAHybOpRgtLeType, self, p_rhs)
          else:
               return EABinOp(ETypes.EABinOpLeType, self, p_rhs)
     def __rle__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return EAHybOpLft(ETypes.EAHybOpLftLeType, p_lhs, self)
          else:
               return EABinOp(ETypes.EABinOpLeType, p_lhs, self)
     def __lt__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return EAHybOpRgt(ETypes.EAHybOpRgtLtType, self, p_rhs)
          else:
               return EABinOp(ETypes.EABinOpLtType, self, p_rhs)
     def __rlt__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return EAHybOpLft(ETypes.EAHybOpLftLtType, p_lhs, self)
          else:
               return EABinOp(ETypes.EABinOpLtType, p_lhs, self)
     def __ge__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return EAHybOpRgt(ETypes.EAHybOpRgtGeType, self, p_rhs)
          else:
               return EABinOp(ETypes.EABinOpGeType, self, p_rhs)
     def __rge__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return EAHybOpLft(ETypes.EAHybOpLftGeType, p_lhs, self)
          else:
               return EABinOp(ETypes.EABinOpGeType, p_lhs, self)
     def __gt__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return EAHybOpRgt(ETypes.EAHybOpRgtGtType, self, p_rhs)
          else:
               return EABinOp(ETypes.EABinOpGtType, self, p_rhs)
     def __rgt__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return EAHybOpLft(ETypes.EAHybOpLftGtType, p_lhs, self)
          else:
               return EABinOp(ETypes.EABinOpGtType, p_lhs, self)
     def __eq__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return EAHybOpRgt(ETypes.EAHybOpRgtEqType, self, p_rhs)
          else:
               return EABinOp(ETypes.EABinOpEqType, self, p_rhs)
     def __req__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return EAHybOpLft(ETypes.EAHybOpLftEqType, p_lhs, self)
          else:
               return EABinOp(ETypes.EABinOpEqType, p_lhs, self)
     def __ne__(self, p_rhs):
          if isinstance(p_rhs, float) or isinstance(p_rhs, int):
               return EAHybOpRgt(ETypes.EAHybOpLftNeqType, self, p_rhs)
          else:
               return EABinOp(ETypes.EABinOpNeqType, self, p_rhs)
     def __rne__(self, p_lhs):
          if isinstance(p_lhs, float) or isinstance(p_lhs, int):
               return EAHybOpLft(ETypes.EAHybOpLftNeqType, p_lhs, self)
          else:
               return EABinOp(ETypes.EABinOpNeqType, p_lhs, self)
     def __neg__(self):
          return AUnOp(ATypes.AUnOpNegType, self)
     def __pos__(self):
          return AUnOp(ATypes.AUnOpPosType, self)

class E:
    s_cpt = 0
    def __init__(self, p_type):
        self.name = E.s_cpt
        E.s_cpt += 1
        self.type = p_type
    def count(self):
        raise NotImplementedError
    def write_internal(self, f):
        f.write(f'e {self.name} {self.type} ')
        self.write_internal_core(f)
    def write_internal_core(self, f):
        raise NotImplementedError
    def __or__(self, rhs):
        return EBinOp(ETypes.EBinOpOrType, self, rhs)
    def __and__(self, rhs):
        return EBinOp(ETypes.EBinOpAndType, self, rhs)
    def __not__(self):
        return EUnOp(ETypes.EUnOpNotType, self)
class EABinOp(E):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        lhs_na, lhs_ne = self.lhs.count()
        rhs_na, rhs_ne = self.rhs.count()
        return lhs_na + rhs_na, lhs_ne + rhs_ne + 1
    def write_internal_core(self, f):
        f.write(f'{self.lhs.name},{self.rhs.name}\n')
        self.lhs.write_internal(f)
        self.rhs.write_internal(f)

class C:
    s_cpt = 0
    def __init__(self, p_type):
        self.name = C.s_cpt
        C.s_cpt += 1
        self.type = p_type
    def write(self, f):
        self.write_header(f)
        self.write_internal(f)
    def write_internal(self, f):
        f.write(f'c {self.name} {self.type} ')
        self.write_internal_core(f)
    def count(self):
        raise NotImplementedError
    def write_header(self, f):
        na, ne , nc = self.count()
        f.write(f'{self.name} {na} {ne} {nc}\n')
    def write_internal_core(self, f):
        raise NotImplementedError
    def __and__(self, p_rhs):
        return CBinOp(self, p_rhs)
    
class O:
    s_cpt = 0
    def __init__(self, p_observation_date, p_amount):
       self.name = O.s_cpt
       O.s_cpt += 1
       self.observation_date = p_observation_date
       self.amount = p_amount
    def count(self):
        return self.amount.count()
    def write(self, f):
        f.write(f'o {self.name} 0 {self.observation_date},{self.amount.name}\n')
        self.amount.write(f)

class ABinOp(A):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.op = p_op
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        lhs_na, lhs_ne = self.lhs.count()
        rhs_na, rhs_ne = self.rhs.count()
        return (lhs_na + rhs_na + 1, lhs_ne + rhs_ne)
    def write_internal_core(self, f):
          f.write(f'{self.lhs.name},{self.rhs.name}\n')
          self.lhs.write_internal(f)
          self.rhs.write_internal(f)
class ADet(A):
    def __init__(self, p_val):
        super().__init__(ATypes.ADetType)
        self.val = p_val
    def count(self):
        return 1, 0
    def write_internal_core(self, f):
        f.write(f'{self.val:0.4f}\n')
class AFix(A):
    def __init__(self, p_ticker, p_fixing_date, p_currency_composite, p_fixing_date_shift):
        super().__init__(ATypes.AFixType)
        self.ticker = p_ticker
        self.fixing_date = p_fixing_date
        self.currency_composite = p_currency_composite
        self.fixing_date_shift = p_fixing_date_shift
    def count(self):
        return 1, 0
    def write_internal_core(self, f):
        f.write(f'{self.ticker},{self.fixing_date},{self.currency_composite},{self.fixing_date_shift}\n')
class AHybOpLft(A):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        na, ne = self.rhs.count()
        return na + 1, ne
    def write_internal_core(self, f):
        f.write(f'{self.lhs:0.4f},{self.rhs.name}\n')
        self.rhs.write_internal(f)
class AHybOpRgt(A):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        na, ne = self.lhs.count()
        return na + 1, ne
    def write_internal_core(self, f):
        f.write(f'{self.lhs.name},{self.rhs:0.4f}\n')
        self.lhs.write_internal(f)
class AIfThenElse(A):
    def __init__(self, p_event, p_then, p_otherwise):
        super().__init__(ATypes.AIfThenElseType)
        self.event = p_event
        self.then = p_then
        self.otherwise = p_otherwise
    def count(self):
        event_na, event_ne = self.event.count()
        then_na, then_ne = self.then.count()
        otherwise_na, otherwise_ne = self.otherwise.count()
        return event_na + then_na + otherwise_na + 1, event_ne + then_ne + otherwise_ne
    def write_internal_core(self, f):
        f.write(f'{self.event.name},{self.then.name},{self.otherwise.name}\n')
        self.then.write_internal(f)
        self.otherwise.write_internal(f)
class ARef(A):
    def __init__(self, p_id, p_val):
        super().__init__(ATypes.ARefType)
        self.id = p_id
        self.val = p_val
    def count(self):
        return 1, 0
    def write_internal_core(self, f):
        f.write(f'{self.id},{self.val:0.4f}\n')
class ARefAm(A):
    def __init__(self, p_id):
        super().__init__(ATypes.ARefAmType)
        self.id = p_id
    def count(self):
        return 1, 0
    def write_internal_core(self, f):
        f.write(f'{self.id}\n')
class AUnOp(A):
    def __init__(self, p_op, p_amount):
        super().__init__(p_op)
        self.amount = p_amount
    def count(self):
        na, ne = self.amount.count()
        return na + 1, ne
    def write_internal_core(self, f):
        f.write(f'{self.amount.name}\n')
        self.amount.write_internal(f)

class EAHybOpLft(E):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        na, ne = self.rhs.count()
        return na, ne + 1
    def write_internal_core(self, f):
        f.write(f'{self.op} {self.lhs},{self.rhs.name}\n')
        self.rhs.write_internal(f)
class EAHybOpRgt(E):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        na, ne = self.lhs.count()
        return na, ne + 1
    def write_internal_core(self, f):
        f.write(f'{self.lhs.name},{self.rhs}\n')
        self.lhs.write_internal(f)
class EBinOp(E):
    def __init__(self, p_op, p_lhs, p_rhs):
        super().__init__(p_op)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        lhs_na, lhs_ne = self.lhs.count()
        rhs_na, rhs_ne = self.rhs.count()
        return lhs_na + rhs_na, lhs_ne + rhs_ne + 1
    def write_internal_core(self, f):
        f.write(f'{self.lhs.name},{self.rhs.name}\n')
        self.lhs.write_internal(f)
        self.rhs.write_internal(f)
class EDet(E):
    def __init__(self, p_val):
        super().__init__(ETypes.EDetType)
        self.val = p_val
    def count(self):
        return 0, 1
    def write_internal_core(self, f):
        f.write(f'{self.val}\n')
class EUnOp(E):
    def __init__(self, p_op, p_event):
        super().__init__(p_op)
        self.event = p_event
    def count(self):
        na, ne = self.event.count()
        return na, ne + 1
    def write_internal_core(self, f):
        f.write(f'{self.event.name}\n')
        self.event.write_internal(f)

class CBinOp(C):
    def __init__(self, lhs, rhs):
        super().__init__(CTypes.CBinOpType)
        self.lhs = lhs
        self.rhs = rhs
    def write_internal_core(self, f):
        f.write(f'{self.lhs.name},{self.rhs.name}\n')
        self.lhs.write_internal(f)
        self.rhs.write_internal(f)
    def count(self):
        lhs_na, lhs_ne, lhs_nc = self.lhs.count()
        rhs_na, rhs_ne, rhs_nc = self.rhs.count()
        return lhs_na + rhs_na, lhs_ne + rhs_ne, lhs_nc + rhs_nc + 1
    def write_internal_core(self, f):
        f.write(f'{self.lhs.name},{self.rhs.name}\n')
        self.lhs.write_internal(f)
        self.rhs.write_internal(f)
class CBuySell(C):
    def __init__(self, p_transaction_date, p_buysell, p_quantity, p_cashflow):
        super().__init__(CTypes.CBuySellType)
        self.transaction_date = p_transaction_date
        self.buysell = p_buysell
        self.quantity = p_quantity
        self.cashflow = p_cashflow
    def count(self):
        na, ne, nc = self.cashflow.count()
        return na, ne, nc + 1
    def write_internal_core(self, f):
        f.write(f'{self.transaction_date},{self.quantity},{self.cashflow.name},{self.buysell}\n')
        self.cashflow.write_internal(f)
class CIfExerciseThenElse(C):
    def __init__(self, p_exercise_kind, p_exercise_date, p_then, p_otherwise):
        super().__init__(CTypes.CIfExerciseThenElseType)
        self.exercise_kind = p_exercise_kind
        self.exercise_date = p_exercise_date
        self.then = p_then
        self.otherwise = p_otherwise
    def count(self):
        then_na, then_ne, then_nc = self.then.count()
        otherwise_na, otherwise_ne, otherwise_nc = self.otherwise.count()
        return then_na + otherwise_na, then_ne + otherwise_ne, then_nc + otherwise_nc + 1
    def write_internal_core(self, f):
        f.write(f'{self.exercise_kind},{self.exercise_date},{self.then.name},{self.otherwise.name}\n')
        self.then.write_internal(f)
        self.otherwise.write_internal(f)
class CIfThenElse(C):
    def __init__(self, p_event, p_then, p_otherwise, p_spread_lhs, p_spread_rhs):
        super().__init__(CTypes.CIfThenElseType)
        self.event = p_event
        self.then = p_then
        self.otherwise = p_otherwise
        self.spread_lhs = p_spread_lhs
        self.spread_rhs = p_spread_rhs
    def count(self):
        event_na, event_ne = self.event.count()
        then_na, then_ne, then_nc = self.then.count()
        otherwise_na, otherwise_ne, otherwise_nc = self.otherwise.count()
        return event_na + then_na + otherwise_na, event_ne + then_ne + otherwise_ne, then_nc + otherwise_nc + 1
    def write_internal_core(self, f):
        f.write(f'{self.event.name},{self.then.name},{self.otherwise.name},{self.spread_lhs:0.4f},{self.spread_rhs:0.4f}\n')
        self.event.write_internal(f)
        self.then.write_internal(f)
        self.otherwise.write_internal(f)
class CNot(C):
    def __init__(self):
        super().__init__(CTypes.CNotType)
    def count(self):
        return 0, 0, 1
    def write_internal_core(self, f):
        f.write('\n')
class CPayRec(C):
    def __init__(self, p_payment_date, p_payment_currency, p_amount, p_payreceive):
        super().__init__(CTypes.CPayRecType)
        self.payment_date = p_payment_date
        self.payment_currency = p_payment_currency
        self.amount = p_amount
        self.payreceive = p_payreceive
    def count(self):
        na, ne = self.amount.count()
        return na, ne, 1
    def write_internal_core(self, f):
        f.write(f'{self.amount.name},{self.payment_date},{self.payment_currency},{self.payreceive}\n')
        self.amount.write_internal(f)
class CRef(C):
    def __init__(self, p_file):
        super().__init__(CTypes.CRefType)
        self.file = p_file
    def count(self):
        return 0, 0, 1 
    def write_internal_core(self, f):
        f.write(f'{self.file}\n')
class CSet(C):
    def __init__(self, p_lhs, p_rhs):
        super().__init__(CTypes.CSetType)
        self.lhs = p_lhs
        self.rhs = p_rhs
    def count(self):
        na, ne, nc = self.rhs.count()
        return na, ne, nc + 1
    def write_internal_core(self, f):
        f.write(f'{self.lhs},{self.rhs.name}\n')
        self.rhs.write_internal(f)