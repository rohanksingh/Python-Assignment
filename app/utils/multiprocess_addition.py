from multiprocessing import Pool
from typing import List

def add_lists(sublist:List[int]) -> int:
	return sum(sublist)

def process_list_additions(lists: List[List[int]], num_processes: int) -> List[int]:
	with Pool(processes= num_processes) as pool:
		results = pool.map(add_lists , lists)
	return results









