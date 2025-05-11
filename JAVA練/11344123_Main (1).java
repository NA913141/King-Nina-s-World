/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
//1
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入你的身高（公分）：");
        double h_cm = scanner.nextDouble();  
        System.out.print("請輸入你的體重（公斤）：");
        double w = scanner.nextDouble();

        double h_m = h_cm / 100;  
        double bmi = w / (h_m * h_m);  

        String category;
        if (bmi < 18.5) {
            category = "過輕";
        } else if (bmi < 24) {
            category = "正常";
        } else if (bmi < 27) {
            category = "過重";
        } else {
            category = "肥胖";
        }

        System.out.printf("身高: %.1f cm, 體重: %.1f kg, BMI值: %.1f\n", h_cm, w, bmi);
        System.out.println("BMI 等級: " + category);

        scanner.close();
    }
}


//2

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("請輸入你的身高（公分）：");
        double h_cm = scanner.nextDouble();  
        System.out.print("請輸入你的體重（公斤）：");
        double w = scanner.nextDouble();

        double h_m = h_cm / 100; 
        double bmi = w / (h_m * h_m); 

        String category;
        int caseNum;  
        if (bmi < 18.5) {
            category = "過輕";
            caseNum = 1;
        } else if (bmi < 24) {
            category = "正常";
            caseNum = 2;
        } else if (bmi < 27) {
            category = "過重";
            caseNum = 3;
        } else {
            category = "肥胖";
            caseNum = 4;
        }

        System.out.printf("身高: %.1f cm, 體重: %.1f kg, BMI值: %.1f\n", h_cm, w, bmi);
        System.out.println("BMI 等級: " + category);

        switch (caseNum) {
            case 1:
                System.out.println("建議: 須注意，體重太輕。");
                break;
            case 2:
                System.out.println("建議: 正常請保持。");
                break;
            case 3:
                System.out.println("建議: 適度減重。");
                break;
            case 4:
                System.out.println("建議: 須注意，立即減肥。");
                break;
            default:
                System.out.println("建議: 無法判斷。");
        }

        scanner.close();
    }
}

