class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []
        bracket_map = {"]": "[", "}": "{", ")": "("}

        for bracket in s:
            if bracket in bracket_map.values():
                bracket_stack.append(bracket)

            elif bracket in bracket_map:
                if not bracket_stack or bracket_map[bracket] != bracket_stack[-1]:
                    return False
                bracket_stack.pop()

            else:
                return False

        return not bracket_stack                            