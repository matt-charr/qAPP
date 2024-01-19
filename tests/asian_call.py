from device.qalgebra import *

CONTRACT(
    "asian_call",
    PAY(
        MAX(
            (
                SPOT("undl1", "2022-05-03") / SPOT("undl1", "2021-06-03") +
                SPOT("undl1", "2022-02-03") / SPOT("undl1", "2021-06-03") +
                SPOT("undl1", "2021-11-03") / SPOT("undl1", "2021-06-03") +
                SPOT("undl1", "2021-08-03") / SPOT("undl1", "2021-06-03")
            ) / 4 - 1., 
            0
        ),
        "2022-05-03",
        "cc1"
    )
)