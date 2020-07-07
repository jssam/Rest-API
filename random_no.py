import random

def random_no():
	random_id = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
	return random_id