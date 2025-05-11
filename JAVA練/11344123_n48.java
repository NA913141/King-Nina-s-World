// 1. 使用給定的數據初始化二維陣列。
public class n48 {

    public static void main(String[] args) {
        int[][] matrix = {
                {77, 45, 69, 21},
                {36, 48, 94, 45},
                {55, 86, 94, 16}
        };

        System.out.println("Process started (PID=6156) >>>"); //  符合圖片的輸出
        for (int i = 0; i < matrix.length; i++) {
            double average = calculateAverage(matrix[i]);
            System.out.println(matrix[i][0] + " " + matrix[i][1] + " " + matrix[i][2] + " " + matrix[i][3] + " ==>Avg=" + String.format("%.1f", average)); //  符合圖片的輸出
        }
    }

    // 计算给定整数数组的平均值
    public static double calculateAverage(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return (double) sum / numbers.length;
    }
}

        // 2. 找出矩陣中的最大值和最小值。
public class n48 {

    public static void main(String[] args) {
        // 1. 使用給定的數據初始化二維陣列。
        int[][] matrix = {
                {77, 45, 69, 21},
                {36, 48, 94, 45},
                {55, 86, 94, 16}
        };

        // 計算並印出每行的平均值。
        System.out.println("Process started (PID=6156) >>>");
        for (int i = 0; i < matrix.length; i++) {
            double average = calculateAverage(matrix[i]);
            System.out.println(matrix[i][0] + " " + matrix[i][1] + " " + matrix[i][2] + " " + matrix[i][3] + " ==>Avg=" + String.format("%.1f", average));
        }

        // 2. 找出矩陣中的最大值和最小值，並印出來。
        System.out.println("--------------------");
        findMinMax(matrix);
    }

    /**
     * 計算給定整數陣列的平均值。
     *
     * @param numbers 整數陣列。
     * @return 陣列的平均值。
     */
    public static double calculateAverage(int[] numbers) {
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return (double) sum / numbers.length;
    }

    /**
     * 找出二維陣列中的最大值和最小值，並印出來。
     *
     * @param matrix 二維整數陣列。
     */
    public static void findMinMax(int[][] matrix) {
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;

        for (int[] row : matrix) {
            for (int value : row) {
                if (value < min) {
                    min = value;
                }
                if (value > max) {
                    max = value;
                }
            }
        }
        System.out.println("Max=" + max + ", Min=" + min);
    }
}
