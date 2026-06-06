import logging

logging.basicConfig(level=logging.DEBUG)

def add(x, y):
    logging.info("entering some function")
    z = x + y
    return z

z = add(10, 20)
logging.info(f"sum is {z}")

# logging in loop

for i in range(1,7):
    logging.debug(f"data is {i+1}")
