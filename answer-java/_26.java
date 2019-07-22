class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        for (int index = 1; index < nums.length;index++) {
            if (nums[k] != nums[index]) {
                k++;
                nums[k] = nums[index];
            }
        }
        return k + 1;
    }
}
