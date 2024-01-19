from qapy.algebra.language import *

CONTRACT(
    "factory/tests/output/digital",
    IF(SPOT("undl1", "2021-11-03") > 100.)(
        BUY(
            "2021-11-05",
            2.,
            PAY(
                MAX(
                    SPOT("undl1", "2022-05-03") / SPOT("undl1", "2021-05-03") - 1., 
                    0.
                ),
                "2022-05-03",
                "cc1"
            )
        ),
        SELL(
            "2021-11-05",
            2.,
            PAY(
                MAX(
                    1. - SPOT("undl1", "2022-05-03") / SPOT("undl1", "2021-05-03"), 
                    0.
                ),
                "2022-05-03",
                "cc1"
            )
        )
    )
)