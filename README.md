# helpdesk-repeat-caller-finder

Spot repeat callers — anyone at or above a ticket threshold — most tickets first, so a recurring root cause gets fixed instead of re-logged.

## How to run

```sh
python3 main.py tickets.csv --threshold 3
```

## Example output

```
ali@example.com: REPEAT (5 tickets)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
