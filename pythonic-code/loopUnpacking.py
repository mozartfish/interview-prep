from typing import List, Tuple

def best_student(scores: List[Tuple[str, int]]) -> str:
    curr_score = float("-inf")
    curr_name = "tbd"
    for name, score in scores:
        if score > curr_score:
            curr_score = score 
            curr_name = name 
    
    return curr_name


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
