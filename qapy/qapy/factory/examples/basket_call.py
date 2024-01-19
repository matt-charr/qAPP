from qapy.algebra.language import *

CONTRACT(
    "factory/tests/output/basket_call",
    PAY(
        MAX(
            (
                0.25 * SPOT("undl1", "2022-05-03") / SPOT("undl1", "2021-05-03") +
                0.35 * SPOT("undl2", "2022-05-03") / SPOT("undl2", "2021-05-03") +
                0.40 * SPOT("undl3", "2022-05-03") / SPOT("undl3", "2021-05-03")
            ) - 1.,
            0
        ),
        "2022-05-07",
        "cc1"
    )    
)