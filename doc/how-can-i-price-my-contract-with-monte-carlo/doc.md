# 📺 How can I price my contract with Monte Carlo ?

> [!NOTE]
> Enjoy the below experience by opening the mockup <em>qa/mockup/how-can-i-price-my-contract.json</em> in `qapp` ([How can I report my issue ?](../features/how-can-i-report-my-issue/doc.md))

1. Load the contract json file <em>factory/examples/autocall.json</em> ([How can I load my contract ?](../features/how_can_i_load_my_contract/doc.md))

2. Go to <em>Model/Configuration</em> tab bar item, and set your model to <em>BlackScholes</em>

3. Go to <em>Pricer/Pricer</em> tab bar item and hit <em>price</em>. You can check the pricing configuration in the tab bar item <em>Pricer/Configuration</em> where you can play with a bunch of parameters such as:

- <em>antithetic factor</em>: Decrease the standard deviation. 
- <em>number of threads</em>: Decrease the computational time (in some cases)
- <em>trials</em>: Decrease the standard deviation.
- <em>confidence level</em>: Control the confidence interval.
- <em>smoothing type</em>: Smooth your payoff ([How can I smooth my payoff ?](../features/how-can-i-smooth-my-payoff/doc.md))