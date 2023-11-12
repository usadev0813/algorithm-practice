n = int(input())

for i in range(n):
     result = 0
     combo = 0
     ox_game = input()
     for j in range(len(ox_game)):
         if ox_game[j] == 'O':
             combo += 1
             result += combo
         else:
             combo = 0
     print(result)