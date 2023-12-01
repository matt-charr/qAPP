#include <qalgebra>

cashflow_t my_asian_call() {
    return (
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
            "2022-05-05",
            "cc1"
        )
    );
}

int main() {
    return (
        CONTRACT(
            "examples/asian_call.json",
            my_asian_call()
        )
    );
}