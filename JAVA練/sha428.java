public class sha428
{
	public static void main(String[] args)
	{
		line();
		square(8);
		line(99);
		square(4);
		line(75, '$');
		System.out.printf("%d's square is %d \n", 7 , square2(7));
	}
	
	public static void line()// non-static method square(int) cannot be referenced from a static context
	{
		System.out.println("----------------------------------------");
	}
	
	public static void line(int n)
	{
		for(int i = 0; i< n; i++)//int
			System.out.print("=");
		System.out.println();
	}
	
	public static void line(int n, char c)
	{
		for(int i = 0; i< n; i++)//int
			System.out.print(c);
		System.out.println();
	}
	
	public static void square(int n)//public供外部調用
	{
		System.out.printf("%d's square is %d \n", n , n*n);
	}
	public static int square2(int n)//常用simple;注意int
	{
		return n*n;
	}
} 