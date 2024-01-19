from qapy.algebra.language import *
from enum import Enum

class StrikeType(Enum):
    ASIAN = 0
    LOOKBACKMIN = 1
    LOOKBACKMAX = 2

class PerformanceType(Enum):
    BASKET = 0
    WORSTOF = 1
    BESTOF = 2

def MEAN(ticker, dates):
    return sum([SPOT(ticker, date) for date in dates]) / len(dates)
 
def BEST(ticker, dates):
    if len(dates) >= 1:
        return MAX(SPOT(ticker, dates[0]), BEST(ticker, dates[1:]))
    else:
        return SPOT(ticker, dates[0])

def WORST(ticker, dates):
    if len(dates) >= 1:
        return MAX(SPOT(ticker, dates[0]), WORST(ticker, dates[1:]))
    else:
        return SPOT(ticker, dates[0])

def PERFORMANCE(tickers, weights, asian_out_dates, asian_in_dates, strike_type, performance_type):
    if len(tickers) >= 1:
        match performance_type:
            case PerformanceType.BASKET:
                return (
                    weights[0] * PERFORMANCE(tickers[0], asian_out_dates, asian_in_dates, strike_type) + 
                    PERFORMANCE(tickers[1:], weights[1:], asian_out_dates, asian_in_dates, strike_type, performance_type)
                )
            case PerformanceType.WORSTOF:
                return MIN(
                    PERFORMANCE(tickers[0], asian_out_dates, asian_in_dates, strike_type),
                    PERFORMANCE(tickers[1:], weights[1:], asian_out_dates, asian_in_dates, strike_type, performance_type)
                )
            case PerformanceType.BESTOF:
                return MAX (
                    PERFORMANCE(tickers[0], asian_out_dates, asian_in_dates, strike_type),
                    PERFORMANCE(tickers[1:], weights[1:], asian_out_dates, asian_in_dates, strike_type, performance_type)
                )
            case _:
                raise Exception("Performance type not found")
    else:
        return PERFORMANCE(tickers[0], asian_out_dates, asian_in_dates, strike_type)

def PERFORMANCE(ticker, start_date, end_date):
    return SPOT(ticker, end_date) / SPOT(ticker, start_date)

def PERFORMANCE(ticker, asian_out_dates, asian_in_dates, strike_type):
    match strike_type:
        case StrikeType.ASIAN:
            return MEAN(ticker, asian_out_dates) / MEAN(ticker, asian_in_dates);
        case StrikeType.LOOKBACKMIN:
            return MEAN(ticker, asian_out_dates) / MIN(ticker, asian_in_dates);
        case StrikeType.LOOKBACKMAX:
            return MEAN(ticker, asian_out_dates) / MAX(ticker, asian_in_dates);
        case _:
            raise Exception("Strike type not found")