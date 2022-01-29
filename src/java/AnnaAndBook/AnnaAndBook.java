package AnnaAndBook;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class AnnaAndBook {

    public final static int[] coins = {1, 2, 5, 10, 20, 50};
    private final static Set<Map<Integer, Integer>> finalResults = new HashSet<>();

    private static void collectMoney(int participants, int target) {
        collectMoney(participants, target, null);
    }

    private static void collectMoney(int participants, int target, Map<Integer, Integer> tmpResult) {
        if (tmpResult == null) {
            tmpResult = new HashMap<>();
            for(int coin: coins) {
                tmpResult.put(coin, 0);
            }
        }
        for (int coin: coins) {
            int collected = coin * participants;
            if (collected > target)
                    continue;
            HashMap<Integer, Integer> updatedResult = new HashMap<>(tmpResult);
            updatedResult.put(coin , updatedResult.get(coin) + 1);
            if (collected == target) {
                finalResults.add(updatedResult);
                continue;
            }
            collectMoney(participants, target-collected, updatedResult);
        }
    }

    public static void main(String[] cmd) {
        collectMoney(26, 780);
        System.out.println(String.format("Number of results found: %s", finalResults.size()));
        for (Map<Integer, Integer> result: finalResults) {
            System.out.println(result);
        }
    }
}
