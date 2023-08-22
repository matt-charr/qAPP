/** COPYRIGHT(C) 2021 QA - Matthieu Charrier.
 * All rights reserved.No part of this document may be used in any form for professional
 * or commercial purposes without the express permission of Matthieu Charrier 
 */

#ifndef _SCHEME_HPP_INCLUDED
#define _SCHEME_HPP_INCLUDED

#include <memory>
#include <string>
#include <vector>

// begin CalendarFactory

typedef uint8_t weekday_t;

#define mon 0
#define tue 1
#define wed 2
#define thu 3
#define fri 4
#define sat 5
#define sun 6

namespace qa {

    namespace Architecture {

        class Calendar;
        class Date;

    }; // namespace Calendar.

} // namespace qa.

typedef std::shared_ptr<qa::Architecture::Calendar> calendar_t;

calendar_t operator&&(
    const calendar_t&, // lhs.
    const calendar_t&  // rhs.
);

calendar_t operator||(
    const calendar_t&, // lhs.
    const calendar_t&  // rhs.
);

calendar_t operator!(
    const calendar_t& // calendar.
);

calendar_t eq(
    const qa::Architecture::Date& // date.
);

calendar_t leq(
    const qa::Architecture::Date& // date.
);

calendar_t l(
    const qa::Architecture::Date& // date.
);

calendar_t g(
    const qa::Architecture::Date& // date.
);

calendar_t geq(
    const qa::Architecture::Date& // date.
);

calendar_t eq(
    const weekday_t& // week_day.
);

calendar_t leq(
    const weekday_t& // week_day.
);

calendar_t l(
    const weekday_t& // week_day
);

calendar_t g(
    const weekday_t& // week_day.
);

calendar_t geq(
    const weekday_t& // week_day.
);

// end CalendarFactory

// begin DateFactory

typedef uint64_t timestamp_t;
typedef uint16_t year_t;
typedef uint8_t  month_t;
typedef uint8_t  week_t;
typedef uint8_t  day_t;

typedef uint8_t  shift_kind_t;
typedef uint64_t shift_value_t;
typedef char     shift_sign_t;

#define mon 0
#define tue 1
#define wed 2
#define thu 3
#define fri 4
#define sat 5
#define sun 6

#define _days            0
#define _business_days   1
#define _weeks           2
#define _months          3
#define _months_sticky   4
#define _months_business 5
#define _years           6
#define _years_sticky    7

namespace qa {

    namespace Architecture {

        class Date {
        public:
            Date(const char*);
            Date(year_t, month_t, day_t);
        public:
            day_t   day;
            month_t month;
            year_t  year;
        }; // class Date.

        class DateShift {
        public:
            DateShift(const char*);
            DateShift();
        public:
            class Shift {
            public:
                Shift(shift_kind_t, shift_value_t, shift_sign_t);
            public:
                shift_kind_t  kind;
                shift_value_t value;
                shift_sign_t  sign;
            }; // struct Shift.
            std::vector<Shift> shift;
        }; // class DateShift.

    } // namespace Architecture.

} // namespace qa.

typedef qa::Architecture::Date      date_t;
typedef qa::Architecture::DateShift date_shift_t;

date_t today(
    void
);

day_t day(
    const date_t&
);

month_t month(
    const date_t&
);

year_t year(
    const date_t&
);

day_t week_day(
    const date_t&
);

bool operator<=(const date_t&, const date_t&);
bool operator<(const date_t&, const date_t&);
bool operator>=(const date_t&, const date_t&);
bool operator> (const date_t&, const date_t&);
bool operator==(const date_t&, const date_t&);
bool operator!=(const date_t&, const date_t&);

date_t shift(
    const date_t&,
    const date_shift_t&,
    const calendar_t& = nullptr
);

bool is_end_of_month(
    const date_t&,
    const calendar_t& = nullptr
);

bool is_closed(
    const date_t&
);

date_t end_of_month(
    const date_t&,
    const calendar_t& = nullptr
);

// end DateFactory

// begin AlgebraFactory

/* Definition of date, currency, maturity, frequency, underlying. */

typedef std::string ticker_t;
typedef std::string currency_t;

typedef std::vector<date_t>     dates_t;
typedef std::vector<ticker_t>   tickers_t;
typedef std::vector<currency_t> currencies_t;

typedef uint8_t strike_t;
typedef uint8_t performance_t;

/* ************************************************************** */

/* Definition of amount, referenced amount. */

namespace qa {

    namespace Architecture {

        class Amount;
        class RefAmount;

    } // namespace Architecture.

} // namespace qa.

typedef std::shared_ptr<qa::Architecture::Amount>    amount_t;
typedef std::shared_ptr<qa::Architecture::RefAmount> ref_amount_t;

#define BASKET       0
#define WORST_OF     1
#define BEST_OF      2

#define ASIAN        0
#define LOOKBACK_MIN 1
#define LOOKBACK_MAX 2

/* **************************************** */

/* Operation with amount. */

amount_t operator+(const amount_t&);
amount_t operator+(const amount_t&, const amount_t&);
amount_t operator+(const amount_t&, const double&);
amount_t operator+(const double&, const amount_t&);
amount_t operator-(const amount_t&);
amount_t operator-(const amount_t&, const amount_t&);
amount_t operator-(const amount_t&, const double&);
amount_t operator-(const double&, const amount_t&);
amount_t operator*(const amount_t&, const amount_t&);
amount_t operator*(const amount_t&, const double&);
amount_t operator*(const double&, const amount_t&);
amount_t operator/(const amount_t&, const amount_t&);
amount_t operator/(const amount_t&, const double&);
amount_t operator/(const double&, const amount_t&);

amount_t spot(const ticker_t&, const date_t&, const date_shift_t& = "");
amount_t spot_composite(const ticker_t&, const date_t&, const currency_t&, const date_shift_t& = "");
amount_t ref(const std::string&, const double&);
amount_t cst(const double&);
amount_t amount(const ticker_t&);
amount_t pow(const amount_t&, const unsigned&);
amount_t abs(const amount_t&);
amount_t cos(const amount_t&);
amount_t sin(const amount_t&);
amount_t tan(const amount_t&);
amount_t exp(const amount_t&);
amount_t log(const amount_t&);
amount_t sqrt(const amount_t&);
amount_t _max(const amount_t&, const amount_t&);
amount_t _max(const amount_t&, const double&);
amount_t _max(const double&, const amount_t&);
amount_t _max(const ticker_t&, const dates_t&);
amount_t _min(const amount_t&, const amount_t&);
amount_t _min(const amount_t&, const double&);
amount_t _min(const double&, const amount_t&);
amount_t _min(const ticker_t&, const dates_t&);
amount_t mean(const ticker_t&, const dates_t&);
amount_t perf(const ticker_t&, const date_t&, const date_t&);
amount_t perf(const ticker_t&, const dates_t&, const dates_t&, const strike_t&);
amount_t perf(const tickers_t&, const std::vector<double>&, const dates_t&, const dates_t&, const strike_t&, const performance_t&);

template<typename Type, typename... Args>
amount_t _max(
    const Type& p_amount,
    Args... p_args
) {
    return _max(p_amount, _max(p_args...));
}
template<typename Type, typename... Args>
amount_t _min(
    const Type& p_amount,
    Args... p_args
) {
    return _min(p_amount, _min(p_args...));
}

/* ********************** */

/* Definition of event. */

namespace qa {

    namespace Architecture {

        class Event;

    } // namespace Architecture.

} // namespace qa.

typedef std::shared_ptr<qa::Architecture::Event> event_t;

/* ******************** */

/* Operation with event and amount. */

event_t operator<=(const amount_t&, const amount_t&); 
event_t operator<=(const amount_t&, const double&); 
event_t operator<=(const double&, const amount_t&); 
event_t operator<(const amount_t&, const amount_t&);
event_t operator<(const amount_t&, const double&);
event_t operator<(const double&, const amount_t&);
event_t operator>=(const amount_t&, const amount_t&); 
event_t operator>=(const amount_t&, const double&); 
event_t operator>=(const double&, const amount_t&); 
event_t operator>(const amount_t&, const amount_t&);
event_t operator>(const amount_t&, const double&);
event_t operator>(const double&, const amount_t&);
event_t operator==(const amount_t&, const amount_t&);
event_t operator==(const amount_t&, const double&);
event_t operator==(const double&, const amount_t&);
event_t operator!=(const amount_t&, const amount_t&);
event_t operator!=(const amount_t&, const double&);
event_t operator!=(const double&, const amount_t&);

/* ******************************** */

/* Operation with event. */

event_t operator&&(const event_t&, const event_t&);
event_t operator||(const event_t&, const event_t&);
event_t operator!(const event_t&);

event_t cst(const bool&);

/* ********************* */

/* Definition of cashflow. */

namespace qa {

    namespace Architecture {

        class CashFlow;

    } // namespace Architecture.


} // namespace qa.

typedef std::shared_ptr<qa::Architecture::CashFlow> cashflow_t;

/* *********************** */

/* Operation with cashflow. */

cashflow_t operator&(const cashflow_t&, const cashflow_t&);

cashflow_t buy(const double&, const cashflow_t&);
cashflow_t buy(const cashflow_t&);
cashflow_t sell(const double&, const cashflow_t&);
cashflow_t sell(const cashflow_t&);
cashflow_t end(void);

/* *********************** */

/* Operation with cashflow and amount. */

cashflow_t pay(const amount_t&, const date_t&, const currency_t&);
cashflow_t pay(const double&, const date_t&, const currency_t&);
cashflow_t rec(const amount_t&, const date_t&, const currency_t&);
cashflow_t rec(const double&, const date_t&, const currency_t&);
cashflow_t set(const ticker_t&, const amount_t&);

/* *********************************** */

/* Operation with amount/cashflow and event. */

#define _then(instruction) (instruction,
#define _else(instruction) instruction)

class _if {
private:
    const event_t _cm_statement_iptr;
    const double  _cm_spread_lhs;
    const double  _cm_spread_rhs;
public:
    amount_t operator()(const amount_t&, const amount_t&);
    amount_t operator()(const double&, const amount_t&);
    amount_t operator()(const amount_t&, const double&);
    amount_t operator()(const double&, const double&);
    amount_t operator()(const double&);
    amount_t operator()(const amount_t&);
    cashflow_t operator()(const cashflow_t&, const cashflow_t&);
    cashflow_t operator()(const cashflow_t&);
public:
    _if(const event_t&, const double&, const double&);
    _if(const event_t&, const double& = 0.);
}; // class _if.

class _if_exercise {
private:
    const date_t _cm_exercise_date_str;
    const bool   _cm_exercise_type;
public:
    _if_exercise(const bool&, const date_t&);
    cashflow_t operator()(const cashflow_t&, const cashflow_t&);
    cashflow_t operator()(const cashflow_t&);
}; // class _if_exercise.

class _if_called : public _if_exercise {
public:
    _if_called(const date_t&);
}; // class _if_called.

class _if_putted : public _if_exercise {
public:
    _if_putted(const date_t&);
}; // class _if_putted.

/* ***************************************** */

// end AlgebraFactory

#ifdef __cplusplus
extern "C"
{
#endif

#ifdef _WIN32
#ifdef BUILD_DLL
#define _EXPORT __declspec(dllexport)
#else
#define _EXPORT __declspec(dllimport)
#endif
#else 
#define _EXPORT
#endif

#ifdef __cplusplus
}
#endif

#ifdef __cplusplus
#define _DECLARE extern "C"    
#else
#define _DECLARE
#endif

#define contract_t   _DECLARE _EXPORT cashflow_t
#define schedule_t   _DECLARE _EXPORT calendar_t
#define observable_t _DECLARE _EXPORT amount_t

#endif // _SCHEME_HPP_INCLUDED.