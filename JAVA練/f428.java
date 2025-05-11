public class f428
{
	public static void main(String[] args)
	{
		System.out.printf("%d factorial is %d \n ",5 , fact(5));
		System.out.printf("%d factorial is %d \n ",10 , fact(10));
	}
	
	public static int fact(int n)
	{
		if (n==1 || n==0)//可以只寫其一
			return 1;
		else
			return n* fact(n-1);
	}
}