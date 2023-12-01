#include <vector>
#include <qalgebra>

struct Period {
    date_t start_date;
    date_t end_date;
    date_t payment_date;
    currency_t payment_ccy;
    double notional;
    double coverage;
    double autocall_barrier;
    double knock_in_barrier;
    double phoenix_coupon;
    double knock_in_coupon;
};

struct Basket {
    ticker_t ticker;
    double weight;
};

// basket.
std::vector<Basket> basket = {
//   ticker | weight |
    {"undl1", 25.0}, // not quanto because ccy(undl1) = cc1 (premium currency).
    {"undl2", 35.0}, // quanto because ccy(undl2) = cc2 != cc1 (premium ccy). -> needs correl undl2/cc2-cc1 and vol cc2-cc1. (but cc2-cc1 IS IN the basket)
    {"undl3", 40.0}  // quanto because ccy(undl3) = cc3 != cc1 (premium ccy). -> needs correl undl3/cc3-cc1 and vol cc3-cc1. (but cc3-cc1 IS NOT IN the basket - no need to diffuse if MC)
};

// schedule.
std::vector<Period> periods = {
//   start date  | end date    | payment date | payment currency | notional | coverage | autocall barrier | knock-in barrier | phoenix coupon  | knock-in coupon  |
    {"2021-05-03", "2021-06-03", "2021-06-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             }, // 2021-05-14 <- strike date.
    {"2021-06-03", "2021-07-03", "2021-07-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2021-07-03", "2021-08-03", "2021-08-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             }, // 2021-07-15 <- we buy the autocall.
    {"2021-08-03", "2021-09-03", "2021-09-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2021-09-03", "2021-10-03", "2021-10-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2021-10-03", "2021-11-03", "2021-11-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             }, // 2021-10-07 <- pricing date.
    {"2021-11-03", "2021-12-03", "2021-12-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2021-12-03", "2022-01-03", "2022-01-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2022-01-03", "2022-02-03", "2022-02-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2022-02-03", "2022-03-03", "2022-03-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2022-03-03", "2022-04-03", "2022-04-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             },
    {"2022-04-03", "2022-05-03", "2022-05-05" , "cc1"            , 100.     , 1.       , 0.30             , 0.05             , 0.05            , 0.05             }
};

// purchase.
date_t strike_date = "2021-05-14";
date_t pricing_date = "2021-10-07";
date_t buy_date = "2021-07-15";
double quantity = 10.;
double strike = 0.80;

amount_t PERFORMANCE(int period_index = 0) {
    return (
        basket[0].weight * SPOT_COMPOSITE(basket[0].ticker, periods[period_index].end_date, "cc2") / SPOT_COMPOSITE(basket[0].ticker, strike_date, "cc2") + // -> needs cc1-cc2.
        basket[1].weight * SPOT(basket[1].ticker, periods[period_index].end_date) / SPOT(basket[1].ticker, strike_date) +
        basket[2].weight * SPOT(basket[2].ticker, periods[period_index].end_date) / SPOT(basket[2].ticker, strike_date)
    ) / (basket[0].weight + basket[1].weight + basket[2].weight);
}

cashflow_t CONTINUE(int period_index = 0) {
    if(period_index == periods.size() - 1) {
        return (
            PAY(
                periods[period_index].notional * MAX(strike - PERFORMANCE(period_index), 0.),
                periods[period_index].payment_date,
                periods[period_index].payment_ccy
            )
        );
    }
    return (
        IF(PERFORMANCE(period_index) > periods[period_index].autocall_barrier + strike)
        THEN(
            PAY(
                periods[period_index].notional * periods[period_index].phoenix_coupon *periods[period_index].coverage,
                periods[period_index].payment_date,
                periods[period_index].payment_ccy
            )
        )
        ELSE(
            IF(PERFORMANCE(period_index) > periods[period_index].knock_in_barrier + strike)
            THEN(
                PAY(
                    periods[period_index].notional * periods[period_index].knock_in_coupon *periods[period_index].coverage,
                    periods[period_index].payment_date,
                    periods[period_index].payment_ccy
                )
            )
            ELSE(
                END()
            )
            & CONTINUE(period_index + 1)
        )
    );
}

cashflow_t my_autocall() {
    return BUY(
        buy_date,
        quantity,
        CONTINUE()
    );
}

int main() {
    return CONTRACT(
        "examples/autocall.json",
        my_autocall()
    );
}