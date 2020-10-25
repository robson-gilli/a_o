# THE OYSTER CARD PROBLEM
Demonstrates a user loading a card with £30, and taking the following trips, and then viewing the balance.
1. Tube Holborn to Earl’s Court
2. 328 bus from Earl’s Court to Chelsea
3. Tube from Earl’s court to Hammersmith

---------
### Playbook

```
> python src/main.py
```

### Tests

```
> pip install -r requirements.txt
> py.test
```

### Test coverage
Name            |  Stmts|   Miss|   Cover|
----------------|-------|-------|--------|
src/__init__.py |      0|      0|    100%|
src/card.py     |     14|      0|    100%|
src/fares.py    |      1|      0|    100%|
src/main.py     |     30|     30|      0%|
src/stations.py |     1 |      0|    100%|
src/trip.py     |     48|      3|     94%|
TOTAL           |     94|     33|     65%|
