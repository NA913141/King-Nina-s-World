//5.Even or Odd / 3.value
/*
import java.util.Scanner;
public class aa{
	public static void main(String args[]){
		int n=0, abs=0;
		Scanner scn=new Scanner(System.in);
		System.out.print("Enter a number:");
		n=scn.nextInt();
		if (n%2==0){
			System.out.printf("%d is an Even number.%n",n);
		}//大誇號
		else
			System.out.printf("%d is an Odd number.%n",n);
		/*if (n<0)
			abs=-n;
		else
            abs=n;
		/
		abs=(n<0?-n:n);
		System.out.printf("%d, abs value= %d.%n",n, abs);
		
	}
}
/
import java.util.Scanner;
public class aa{
	public static void main(String args[]){
		double n=0, abs=0;
		Scanner scn=new Scanner(System.in);
		System.out.print("Enter your score:");
		n=scn.nextDouble();
		if (n>=90){
			System.out.printf("%.1f is Graded A.%n",n);
		}
		else if (n>=80)
			System.out.printf("%.1f is Graded B.%n",n);
		else if (n>=70)
			System.out.printf("%.1f is Graded C.%n",n);
		else if (n>=60)
			System.out.printf("%.1f is Graded D.%n",n);
		else
			System.out.printf("%.1f is Fail.%n",n);
		
	}
}
/
import java.util.Scanner;
public class aa{
	public static void main(String args[]){
		int n=0, abs=0;
		Scanner scn=new Scanner(System.in);
		System.out.print("Enter the digit of month:");
		n=scn.nextInt();
		switch(n){
			case 1:
				System.out.printf("Month %d is Winter.%n",n);
			break;
			case 2:
				System.out.printf("Month %d is Winter.%n",n);
			break;
			case 3:
				System.out.printf("Month %d is Spring.%n",n);
			break;
			case 4:
				System.out.printf("Month %d is Spring.%n",n);
			break;
			case 5:
				System.out.printf("Month %d is Spring.%n",n);
			break;
			case 6:
				System.out.printf("Month %d is Summer.%n",n);
			break;
			case 7:
				System.out.printf("Month %d is Summer.%n",n);
			break;
			case 8:
				System.out.printf("Month %d is Summer.%n",n);
			break;
			case 9:
				System.out.printf("Month %d is Fall.%n",n);
			break;
			case 10:
				System.out.printf("Month %d is Fall.%n",n);
			break;
			case 11:
				System.out.printf("Month %d is Fall.%n",n);
			break;
			case 12:
				System.out.printf("Month %d is Winter.%n",n);
			break;
			default:
				System.out.printf("You enter wrong month number.%n",n);
		}
		
	}
}
/
import java.util.Scanner;
public class aa{
	public static void main(String args[]){
		int n=0, abs=0;
		Scanner scn=new Scanner(System.in);
		System.out.print("Enter the digit of month:");
		n=scn.nextInt();
		switch(n){
			case 12:
			case 1:				
			case 2:
				System.out.printf("Month %d is Winter.%n",n);
			break;
			case 3:				
			case 4:				
			case 5:
				System.out.printf("Month %d is Spring.%n",n);
			break;
			case 6:				
			case 7:				
			case 8:
				System.out.printf("Month %d is Summer.%n",n);
			break;
			case 9:				
			case 10:				
			case 11:
				System.out.printf("Month %d is Fall.%n",n);
			break;
			default:
				System.out.printf("You enter wrong month number.%n",n);
		}
		
	}
}
*/
import java.util.Scanner;
public class aa{
	public static void main(String args[]){
		int n=0, abs=0;
		Scanner scn=new Scanner(System.in);
		System.out.print("Enter the digit of month:");
		n=scn.nextInt();
		switch(n){
			case 1:				
			case 2:
				System.out.printf("Winter break.%n",n);
			break;
			case 3:				
			case 4:				
			case 5:
			case 6:	
				System.out.printf("Semester II.%n",n);
			break;
			case 7:				
			case 8:
				System.out.printf("Summer break.%n",n);
			break;
			case 9:				
			case 10:				
			case 11:
			case 12:
				System.out.printf("Semester I.%n",n);
			break;
			default:
				System.out.printf("Not Exist.%n",n);
		}
		
	}
}
