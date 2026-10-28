# Python - Async

## Description
This project introduces asynchronous programming in Python using the `asyncio` module.
It covers writing coroutines with `async` and `await`, running multiple coroutines
concurrently, measuring execution time, and creating `asyncio` tasks.

## Learning Objectives
- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

## Requirements
- Ubuntu 20.04 LTS
- Python 3.8
- `pycodestyle` 2.5.x
- All files start with `#!/usr/bin/env python3` and end with a new line
- All modules and functions are documented and type-annotated

## Files
| File | Description |
|------|-------------|
| `0-basic_async_syntax.py` | `wait_random`: waits for a random delay between 0 and `max_delay` seconds and returns it |
| `1-concurrent_coroutines.py` | `wait_n`: runs `wait_random` n times concurrently and returns the delays in ascending order |
| `2-measure_runtime.py` | `measure_time`: measures the total runtime of `wait_n` and returns the average time per call |
| `3-tasks.py` | `task_wait_random`: returns an `asyncio.Task` that runs `wait_random` |
| `4-tasks.py` | `task_wait_n`: same as `wait_n`, but uses `task_wait_random` |

## Usage
```bash
./0-main.py
```

## Author
Khaled Al-Yahya
