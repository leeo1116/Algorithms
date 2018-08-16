package leetcode._198_house_robber;


public class TestDriver {
    public static void main(String[] args) {
        HouseRobber houseRobber = new HouseRobber();
        int[] money = new int[] {1, 2, 3, 1};
        int maxMoneyRobbed = houseRobber.rob(money);
        System.out.println(maxMoneyRobbed);
    }
}