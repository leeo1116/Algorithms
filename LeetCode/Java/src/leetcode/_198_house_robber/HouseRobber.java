/**
 * You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 * the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and
 * it will automatically contact the police if two adjacent houses were broken into on the same night.
 *
 * Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of
 * money you can rob tonight without alerting the police.
 *
 * Example 1:
 *
 * Input: [1,2,3,1]
 * Output: 4
 * Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
 *              Total amount you can rob = 1 + 3 = 4.
 * Example 2:
 *
 * Input: [2,7,9,3,1]
 * Output: 12
 * Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
 *              Total amount you can rob = 2 + 9 + 1 = 12.
 */

/**
 * Why DP
 * 1) nums.length == 1;
 * 2) moneyRobbed[i] ==> moneyRobbed[i + 1]
 *   2.1) moneyRobbed[i][0]
 *   2.2) moneyRobbed[i][1]
 */

package leetcode._198_house_robber;


public class HouseRobber {
    public int rob(int[] nums) {
        /**
         * Calculate the maximum money can be robbed given that two adjacent houses can not robbed simultaneously
         * @param  nums the money stored in each house
         * @return the maximum money that can be robbed
         */
        // Use moneyRobbed[i] to denote the maximum money robbed after visiting house 0 to house i, each house can be
        // either robbed or not robbed, so we need one step further, add a status flag to each house, 1: robbed, 0: not
        int[][] moneyRobbed = new int[nums.length][2];

        // Initial value - rob first house (or not)
        if (nums.length > 0) {
            moneyRobbed[0][0] = 0;
            moneyRobbed[0][1] = nums[0];
        }

        // Visit house 1 to house (nums.length - 1)
        for (int i = 1; i < nums.length; i++) {
            moneyRobbed[i][0] = Math.max(moneyRobbed[i - 1][0], moneyRobbed[i - 1][1]);
            moneyRobbed[i][1] = moneyRobbed[i - 1][0] + nums[i];
        }

        // The maximum money robbed after visiting house 0 to nums.length - 1 is
        return Math.max(moneyRobbed[nums.length - 1][0], moneyRobbed[nums.length - 1][1]);
    }

    // Optimization 1 - space complexity from O(n) to O(1)
    // Optimization 2 - merge initialization with visiting house 1 to the last house
}
