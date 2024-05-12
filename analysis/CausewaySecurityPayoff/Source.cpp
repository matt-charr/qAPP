/* ********************************************************************* *
 * Copyright © 2024 qAPP - Quantitative Analytics. All rights reserved.* *
 * This file is part of the project 'qAPP - Quantitative Analytics'. *** *
 * Hence the latter remains the exclusive property of its author. ****** *
 * Accordingly, no part of this device may be used or transmitted ****** *
 * in any form for professional, educational or commercial purposes **** *
 * without the express permission of Matthieu Charrier. **************** *
 * ********************************************************************* */

// std.
#include <algorithm>

// qDSL.
#include <qDSL/Algebra.hpp>

using namespace qDSL;

int main() {

    // contract parameters.
    const std::vector<std::string> schedule = {
        "2021-08-02", "2021-09-03", "2021-10-03", "2021-11-04", "2021-12-03",
        "2022-01-06", "2022-02-03", "2022-03-05", "2022-04-02", "2022-05-07", 
        "2022-06-03", "2022-07-03", "2022-08-04", "2022-09-02", "2022-10-03", 
        "2022-11-03", "2022-12-03", "2023-01-06", "2023-02-02", "2023-03-05", 
        "2023-04-02", "2023-05-06", "2023-06-02", "2023-07-03", "2023-08-03", 
        "2023-09-03", "2023-10-05", "2023-11-02", "2023-12-03", "2024-01-06", 
        "2024-02-02", "2024-03-05", "2024-04-06", "2024-05-04", "2024-06-03", 
        "2024-07-05", "2024-08-02", "2024-09-03", "2024-10-04", "2024-11-02", 
        "2024-12-03", "2025-01-06", "2025-02-02", "2025-03-06", "2025-04-03", 
        "2025-05-04", "2025-06-05", "2025-07-03"
    };
    const auto coupon(CstRef("Coupon", 0.4625)); // in %.
    const auto notional(CstRef("Notional", 10'000));
    const auto barrier(CstRef("Barrier", 65)); // in %.
    const auto spread(CstRef("Spread", 1)); // in %.
    const auto payment_currency("cc1");
    const auto underlying("undl1");

    // construction of the payoff.
    CashFlowType cashflow;
    const auto& last_observation_date(schedule.back());
    const auto spot(Spot(underlying, last_observation_date));
    std::for_each(
        std::cbegin(schedule), std::cend(schedule),
        [&cashflow, &notional, &coupon, &payment_currency](const auto& p_date) {
            cashflow = cashflow & Pay(0.01 * notional * coupon, p_date, payment_currency);
        }
    );
    cashflow = cashflow & (
        Pay(
            0.01 * notional * (
                If(spot <= barrier) (
                    barrier / (barrier - spread) * spot, 
                    0
                ) + 
                If(spot >= barrier - spread && spot <= barrier) (
                    barrier + (100 - barrier) / spread * (spot - (barrier - spread)),
                    0
                ) + 
                If(spot >= barrier) (
                    100, 
                    0
                )
            ),
            last_observation_date, 
            payment_currency
        )
    );

    // Save payoff into a file.
    if(Save(cashflow, "CausewaySecurityPayoff")) {
        return EXIT_SUCCESS;
    }
    else {
        return EXIT_FAILURE;
    }
}