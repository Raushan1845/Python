import logging

logging.basicConfig(level=logging.DEBUG)

def div(x, y):
    return x / y

try:
    result = div(2, 0)
    logging.info(f"Result: {result}")
except ZeroDivisionError as e:
    logging.error(f"Cannot divide by zero: {e}")
