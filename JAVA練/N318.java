/* 7
import java.util.Scanner;//import java.util Scanner;
public class N318{
	public static void main(String args[]){
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
*/
import java.util.Scanner;
public class N318{
	public static void main(String args[]){
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