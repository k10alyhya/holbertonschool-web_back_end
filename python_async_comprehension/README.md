# Python - Async Comprehension

## Description
This project covers asynchronous generators and asynchronous comprehensions in Python.
It shows how to yield values asynchronously, collect them with an async comprehension,
and run several coroutines concurrently with `asyncio.gather` while measuring the runtime.

## Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8
- `pycodestyle` 2.5.x
- All files start with `#!/usr/bin/env python3` and end with a new line
- All modules and functions are documented and type-annotated

## Files
| File | Description |
|------|-------------|
| `0-async_generator.py` | `async_generator`: loops 10 times, waits 1 second each time, then yields a random number between 0 and 10 |
| `1-async_comprehension.py` | `async_comprehension`: collects 10 random numbers from `async_generator` using an async comprehension |
| `2-measure_runtime.py` | `measure_runtime`: runs `async_comprehension` four times concurrently with `asyncio.gather` and returns the total runtime |

## Why is the runtime about 10 seconds?
Each `async_comprehension` takes about 10 seconds (10 values x 1 second).
Running four of them with `asyncio.gather` lets them wait at the same time,
so the total runtime stays around 10 seconds instead of 40.

## Usage
```bash
./0-main.py
```

## Author
Khaled Al-Yahya
