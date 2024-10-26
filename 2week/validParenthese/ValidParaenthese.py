class Solution:
    def isValid(self, s: str) -> bool:

        answerStack = []

        for word in s:
            if "(" == word:
                answerStack.append(")")
            elif "{" == word:
                answerStack.append("}")
            elif "[" == word:
                answerStack.append("]")
            elif not answerStack or word != answerStack.pop():
                return False
        return True


print(Solution.isValid(Solution, "()"))