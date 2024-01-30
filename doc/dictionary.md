# 📺 Dictionary

- **syn**: <FONT COLOR="BLUE">SPOT</FONT>(`underlying ticker`, `fixing date`, `fixing date shift` = '')
**doc**: <em><FONT COLOR="GREEN">The value of the fixing of the underlying identified by the ticker `underlying ticker` recorded at date `fixing date` (updated with a date shift of `fixing date shift` if provided)</FONT></em>

<br>

- **syn**: <FONT COLOR="BLUE">SPOT_COMPOSITE</FONT>(`underlying ticker`, `composite currency`, `fixing date`, `fixing date shift` = '')
**doc**: <em><FONT COLOR="GREEN">The value of the fixing of the underlying identified by the ticker `underlying ticker` recorded at date `fixing date` (updated with a date shift of `fixing date shift` if provided). This value is then converted into the currency identified by the ticker `composite currency`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">REF</FONT>(`contract feature name`, `contract feature value`)
**doc**: <em><FONT COLOR="GREEN">The deterministic quantity `contract feature value` attached to the contract feature identified by the name `contract feature name`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">CST</FONT>(`deterministic value`)
**doc**: <em><FONT COLOR="GREEN">The deterministic quantity `deterministic value`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">AMOUNT</FONT>(`amount name`)
**doc**: <em><FONT COLOR="GREEN">A reference to the amount identified by the name `amount name`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">POW</FONT>(`amount`, `exponent`)
**doc**: <em><FONT COLOR="GREEN">The power of `amount` with exponent `exponent`(</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">ABS</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The absolute value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">COS</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The cosinus value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">SIN</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The sinus value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">TAN</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The tangente value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">LOG</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The natural logarithm value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">EXP</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The exponential value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">SQRT</FONT>(`amount`)
**doc**: <em><FONT COLOR="GREEN">The square root value of `amount`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">MAX</FONT>(`amount left`, `amount right`)
**doc**: <em><FONT COLOR="GREEN">The maximum value of `amount left` and `amount right`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">MIN</FONT>(`amount left`, `amount right`)
**doc**: <em><FONT COLOR="GREEN">The minimum value of `amount left` and `amount right`</FONT><em>.

<br>

- **syn**: <FONT COLOR="BLUE">BUY</FONT>(`transaction date`, `quantity`, `contract`)
**doc**: <em><FONT COLOR="GREEN">Buy `quantity` `contract` at date `transaction date` </FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">SELL</FONT>(`transaction date`, `quantity`, `contract`)
**doc**: <em><FONT COLOR="GREEN">Sell `quantity` `contract` at date `transaction date` </FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">END</FONT>()
**doc**: <em><FONT COLOR="GREEN">The contract stops</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">RECEIVE</FONT>(`amount`, `transaction date`, `transaction currency`)
**doc**: <em><FONT COLOR="GREEN">Receive `amount` units of currency `transaction currency` at date `transaction date`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">PAY</FONT>(`amount`, `transaction date`, `transaction currency`)
**doc**: <em><FONT COLOR="GREEN">Pay `amount` units of currency `transaction currency` at date `transaction date`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">SET</FONT>(`amount name`, `amount`)
**doc**: <em><FONT COLOR="GREEN">Set the name of `amount` as `amount name`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">CASHFLOW</FONT>(`contract file`)
**doc**: <em><FONT COLOR="GREEN">A reference to the contract represented in the file `contract file` </FONT><em>.

<br>

- **syn**: <FONT COLOR="BLUE">IF</FONT>(`event`)(`contract left`, `contract right`)
**doc**: <em><FONT COLOR="GREEN">If the event `event` happens then apply the terms of contract `contract left` else apply the terms of contract `contract right`</FONT></em>.

<br>

- **syn**: <FONT COLOR="BLUE">EITHER</FONT>(`selection date`, `selection side`)([`first contract`, `second contract`, ...])
**doc**: <em><FONT COLOR="GREEN">At date `selection date`, the buyer (if `selection side` is on `CALL`) or the seller (if `selection side` is on `PUT`) selects a contract among `first contract`, `second contract`, ... and enters into it</FONT></em>.