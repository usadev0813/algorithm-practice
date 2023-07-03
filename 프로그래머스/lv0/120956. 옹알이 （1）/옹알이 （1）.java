class Solution {
    public int solution(String[] babbling) {
        String[] useCase = {"aya", "ye", "woo", "ma"};
        int answer = 0;

        for (int i = 0; i < babbling.length; i++) {
            for(int j = 0; j < useCase.length; j++) {
                if(babbling[i].contains(useCase[j])) {
                        babbling[i] = babbling[i].replace(useCase[j], "*");
                }
            }
            if(babbling[i].replace("*", "").equals("")) {
                answer++;
            }
        }
        return answer;
    }
}