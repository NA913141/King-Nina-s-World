/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
/***
public class Main
{
	public static void main(String[] args) {
	    int a = 10, b = 20, num = 0;
	    num=(a++)-b;
		System.out.printf("a=%d, b=%d, num=%d\n", a, b, num);
		
		a=10; b=20; num=0;
		num=(-b)*a;
		System.out.printf("a=%d, b=%d, num=%d\n", a, b, num);
		
		a=10; b=20; num=0;
		num=(a++)+(++b);
		System.out.printf("a=%d, b=%d, num=%d\n", a, b, num);
		
		a=10; b=20; num=0;
		num=(--a)+(b--);
		System.out.printf("a=%d, b=%d, num=%d\n", a, b, num);
		
		a=10; b=20; num=0;
		a+=a*(b++);
		System.out.printf("a=%d, b=%d, num=%d\n", a, b, num);
	}
}

***/
import java.util.Scanner;
public class Main
{
	public static void main(String[] args) {
	    int a, b;
	    Scanner scn=new Scanner(System.in);
	    System.out.print("Input Days:");
	    a = scn.nextInt(); 
	    b = a / 7;
	    a = a % 7;
	    System.out.printf("%d days is %d weeks and %d days.\n", a + b * 7, b, a);
	}
}	    