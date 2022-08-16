class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {'5': 0, '10': 0}
        for i, pay in enumerate(bills):
            if pay == 10 and money.get('5') > 0:
                money['10'] = money.get('10') + 1
                money['5'] = money.get('5') - 1
            elif pay == 20 and money.get('10') > 0 and money.get('5') > 0:
                money['10'] = money.get('10') - 1
                money['5'] = money.get('5') - 1
            elif pay == 20 and money.get('5') >= 3:
                money['5'] = money.get('5') - 3
            elif pay == 5:
                money['5'] = money.get('5') + 1
            else:
                return False
        return True
