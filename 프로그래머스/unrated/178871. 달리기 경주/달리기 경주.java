import java.util.*;

class Solution {
    public String[] solution(String[] players, String[] callings) {
        Map<String, Integer> indexMap = new HashMap<>();

        for (int i = 0; i < players.length; i++) {
            indexMap.put(players[i], i);
        }

        for (String calling : callings) {
            int idx = indexMap.get(calling);
            if (idx > 0) {
                String temp = players[idx - 1];
                players[idx - 1] = players[idx];
                players[idx] = temp;

                indexMap.put(players[idx - 1], idx - 1);
                indexMap.put(players[idx], idx);
            }
        }
        return players;
    }
}