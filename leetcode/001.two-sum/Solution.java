import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int findNum = target - nums[i];
            if (map.containsKey(findNum)) {
                return new int[]{map.get(findNum), i};
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }

    public int[] twoSum1(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return new int[]{};
    }

    public static void main(String[] args) {
        int[] items = {1, 2, 5, 8};
        int[] result = new Solution().twoSum(items, 10);
        System.out.print(Arrays.toString(result));
    }
}