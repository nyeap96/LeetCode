#You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.
#
#At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:
#
#An integer x - Record a new score of x.
#"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
#"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
#"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
#Return the sum of all the scores on the record.
#
# 
#
#Example 1:
#
#Input: ops = ["5","2","C","D","+"]
#Output: 30
#Explanation:
#"5" - Add 5 to the record, record is now [5].
#"2" - Add 2 to the record, record is now [5, 2].
#"C" - Invalidate and remove the previous score, record is now [5].
#"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
#"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
#The total sum is 5 + 10 + 15 = 30.
#Example 2:
#
#Input: ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27
#Explanation:
#"5" - Add 5 to the record, record is now [5].
#"-2" - Add -2 to the record, record is now [5, -2].
#"4" - Add 4 to the record, record is now [5, -2, 4].
#"C" - Invalidate and remove the previous score, record is now [5, -2].
#"D" - Add 2 * -2 = -4 to the record, record is now [5, -2, -4].
#"9" - Add 9 to the record, record is now [5, -2, -4, 9].
#"+" - Add -4 + 9 = 5 to the record, record is now [5, -2, -4, 9, 5].
#"+" - Add 9 + 5 = 14 to the record, record is now [5, -2, -4, 9, 5, 14].
#The total sum is 5 + -2 + -4 + 9 + 5 + 14 = 27.
#Example 3:
#
#Input: ops = ["1"]
#Output: 1
# 
#
#Constraints:
#
#1 <= ops.length <= 1000
#ops[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 104, 3 * 104].
#For operation "+", there will always be at least two previous scores on the record.
#For operations "C" and "D", there will always be at least one previous score on the record.

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        # so this seems like it can be done in just one pass. You could even maybe do some dynamic programming stuff, but it doesnt seems like it should be required
        # so it looks like there will be only 4 operations. You could do a switch case to just keep track of the score while also remembering 2 past scores. only 4 things can also be if elif else territory though
        # i would prefer to just do a bit of both by creating a list and recording the score at each point
        # error checking is goin to be minimal since the problem guarantees operations should be able to happen so no need to error check those
        
        
        score = []
        
        for i in range(0,len(ops)):
            if ops[i] == "+":
                score.append(score[len(score) - 1] + score[len(score) - 2])
            elif ops[i] == "D":
                score.append(score[len(score) - 1] * 2)
            elif ops[i] == "C":
                score = score[:-1]
            else:
                score.append(int(ops[i]))
        print(score)
        return sum(score)
    