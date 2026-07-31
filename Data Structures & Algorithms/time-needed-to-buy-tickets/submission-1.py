class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        result = 0
        for index, ticket in enumerate(tickets):
            if index <= k and ticket >= tickets[k]:
                result = result + tickets[k]
                
            elif index <= k and ticket < tickets[k]:
                result = result + ticket
                
            elif index > k and ticket >= tickets[k]:
                result = result + tickets[k] - 1
                
            else:
                # FIX: They want fewer tickets than person k, 
                # so they just buy their 'ticket' amount and leave!
                result = result + ticket

        return result