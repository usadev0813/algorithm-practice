import java.util.*;

class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        ArrayList<Integer> answer = new ArrayList<>();
        
        for (int i = 0; i < photo.length; i++) {
            int temp = 0;
            for (int j = 0; j < photo[i].length; j++) {
                for(int k = 0; k < name.length; k++) {
                    if(name[k].equals(photo[i][j])) {
                        temp += yearning[(Arrays.asList(name).indexOf(photo[i][j]))];
                    }
                }
            }
            answer.add(temp);
        }
        
        int[] result = new int[answer.size()];
        for (int i = 0; i < answer.size(); i++) {
            result[i] = answer.get(i);
        }
        
        return result;
    }
}