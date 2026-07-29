class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        for brackets in s:
            if brackets == "[" or brackets == "{" or brackets == "(":
                bracket_stack.append(brackets)
            elif len(bracket_stack) == 0:
                return False    
            elif brackets== "]" and bracket_stack[-1] == '[':
                bracket_stack.pop()
            elif brackets== "}" and bracket_stack[-1] == '{':
                bracket_stack.pop()
            elif brackets== ")" and bracket_stack[-1] == '(':
                bracket_stack.pop()
            else:
                return False

        if len(bracket_stack) == 0:
            return True
        else:
            return False            