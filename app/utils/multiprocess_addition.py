import logging 
from multiprocessing import Pool, current_process
from typing import List, Tuple

# Set up logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')

def add_list(pair: List[int]) -> int:
    try:
        logging.info(f"Process {current_process().name} adding {pair}")
        result= sum(pair)
        return result
    except Exception as e:
        logging.error(f"Error in process {current_process().name}: {e}")
        raise

def process_list_additions(list_pairs: List[List[int]], num_processes: int) -> List[int]:
    results = []
    with Pool(processes= num_processes) as Pool:
        try:
            results= pool.map(add_lists, list_pairs)
        except Exception as e:
            logging.error(f"Error during multiprocessing: {e}")
            raise e 
    return results










