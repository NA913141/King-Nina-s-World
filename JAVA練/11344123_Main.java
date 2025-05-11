/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

//7
import java.util.Scanner;//import java.util Scanner;
public class Main{
    public static void main(String[] args){
        int n=0;
    System.out.print("Enter numbers:");
    Scanner scn = new Scanner(System.in);//Scanner scn=new Scanner(print.in);
    n = scn.nextInt();//n=nextInt();
    if (n % 5 == 0 && n % 6 == 0)//if (n/5==0 && n/6==0)
    System.out.println("Divisible by both five and six!");// ！ 是全形符號，應該改為半形 !
    else
    System.out.println("Not divisible by both five and six!");//printf 主要用於格式化輸出，但這裡沒有變數需要格式化，println 更適合。
    }

}


//19-解法1 switch!!!
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        int n = 0;
        System.out.print("Enter day of week: ");
        Scanner scn = new Scanner(System.in);
        n = scn.nextInt();

        switch (n) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                System.out.println("Have to go to work today.");
                break;
            case 6:
            case 7:
                System.out.println("Rest today.");
                break;
            default:
                System.out.println("Input error.");
                break;
        }
    }
}
/*
//19-解法2
import java.util.Scanner;//import java.util Scanner;
public class Main{
    public static void main(String[] args){
        int n= 0;
    System.out.print("Enter day of week:");
    Scanner scn=new Scanner(System.in);
    n=scn.nextInt();
    if (n<=5 && n>=1)
    System.out.println("Have to go to work today.");
    else if (n>=6 && n<=7)
    System.out.println("Rest today.");
    else
    System.out.println("Input error.");
    }

}

//19-解法3
public class Main{
    public static void main(String[] args){
         int day = 3; // 直接設定 day 的值 (可以修改為 1~7 之間的任何整數)

        if (day >= 1 && day <= 5) {
            System.out.println("Have to go to work today.");
        } else if (day >= 6 && day <= 7) {
            System.out.println("Rest today.");
        } else {
            System.out.println("Input error.");
    
        }
    }

}
*/
//19-解法4 switch!!!
public class Main{
    public static void main(String[] args){
         int day = 6; // 直接設定 day 的值 (可以修改為 1~7 之間的任何整數)

        switch (day) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                System.out.println("Have to go to work today.");
                break;
            case 6:
            case 7:
                System.out.println("Rest today.");
                break;
            default:
                System.out.println("Input error.");
                break;
        }
    }

}


