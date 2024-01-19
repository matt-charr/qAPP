from device.qalgebra import *

schedule = [
    "2022-05-03",
    "2023-05-03",
    "2024-05-03",
    "2025-05-03",
    "2026-05-03",
    "2027-05-03",
    "2028-05-03",
    "2029-05-03",
    "2030-05-03",
    "2031-05-03"
]

def convertible_bond(i = 0):
    if i == len(schedule) - 1: 
        next = END()
        refund = 1000. 
    else: 
        refund = 0.
        next = convertible_bond(i + 1)
    return (
        IF_PUTTED(schedule[i])(
            PAY(
                10 * SPOT("undl1", schedule[i]),
                schedule[i],
                "cc1"
            ),
            PAY(
                100. + refund,
                schedule[i],
                "cc1"
            ) & next
        )
    )

CONTRACT(
    "convertible_bond",
    convertible_bond()
)