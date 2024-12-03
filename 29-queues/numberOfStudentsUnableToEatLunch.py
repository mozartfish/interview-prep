from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        stuQ, sandQ = deque(students), deque(sandwiches)
        while stuQ and sandQ and sandQ[0] in stuQ:
            if stuQ[0] == sandQ[0]:
                stuQ.popleft()
                sandQ.popleft() 
            else:
                student = stuQ.popleft() 
                stuQ.append(student)
        return len(stuQ)
        