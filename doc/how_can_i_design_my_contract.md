# 📺 How can I design my contract ?

First you need to make sure you have the latest version of `qapy`, our python extension package for `qa`. Open a terminal and execute:

```bash
pip install qapy
```

1. **Create your contract script**

Open your favorite code editor (example: vscode) and create a python file called <em>my_contract.py</em>

2. **Implement your contract**

Let say you want to design a call on a share named `undl1` with strike `100`, payment currency `cc1`, exercise date `2022-05-01`, fixing date `2022-05-01` and payment date `2022-05-03`. The question to ask is:

<center><em>"If I sell this contract, what will happen ?"</em></center><br>

In this case what happens is the following: if the client chooses to exercise at date `2022-05-01`, I will have to pay the spot of `undl1` in `cc1` (the currency of `undl1`) at `2022-05-03` in exchange of `100` units of `cc1`. If the client doesn't choose to exercise then the contract just stops. From now you can start implementing. For example, <em>my_contract.py</em> can look like:

```python
from qapy.algebra import *

CONTRACT(
    'my_contract', # this is the name of my contract.
    EITHER(CALL '2022-05-01') ( # The client can choose to exercise at 2022-05-01
        [
            PAY(SPOT('undl1', '2022-05-03'), '2022-05-03', 'cc1') & # if he does then at 2022-05-03 I give the share to him ...
            RECEIVE(100., '2022-05-03', 'cc1'), # ... and at 2022-05-03 (on the same date) he gives 100 cc1 to me
            END() # if not then the contract stops.
        ]
    )
)
```

You see ? Simple, intuitive and easily readable. 

Checkout the [Dictionary](dictionary.md) to explore all the symbols available to describe any derivatives you have in mind.

You can find other examples of contract scripts in `factory/examples` located in your `qa` installation folder.

1. **Execute your contract script**

```bash
python -u my_contract.py
```

A file named `my_contract` is created. This is the file you need to provide to `qa` when a contract is required as an input.

Congratulations ! You built your first contract.