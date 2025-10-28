class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        while len(sandwiches)!=0 and sandwiches[0] in students:
            if students[0]==sandwiches[0]:
                del students[0]
                del sandwiches[0]

            else:
                students.append(students.pop(0))
        
        return len(students)