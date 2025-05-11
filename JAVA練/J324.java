/*
public class J324{
	public static void main(String args[]){
		int sum=0;
		for (int i=1; i<=100; i++){
			sum+=i;
		}
		System.out.printf("1+2+3+...+100=%d %n",sum);
		
		sum=0;
		for (int i=1; i<=100; i+=2)
			sum+=i;
		//System.out.printf("1+3+...+99=%d %n",sum);
		System.out.printf("All odd=%d %n", sum);
		
		sum=0;
		for (int i=0; i<=100; i+=2)
			sum+=i;
		//System.out.printf("2+4+...+100=%d %n",sum);
		System.out.printf("All Even=%d %n", sum);
		}
}
*/
/*
public class J324{
	public static void main(String args[]){
		int i=0, sum=0;
		while(i<=100)
		{
			sum+=i;
			i++;
		}
		System.out.printf("1+2+3+...+100=%d %n",sum);
		
		i=1; sum=0;
		while(i<=100)
		{
			sum+=i;
			i+=2;
		}
		//System.out.printf("1+3+...+99=%d %n",sum);
		System.out.printf("All odd=%d %n", sum);
		
		i=2; sum=0;
		while(i<=100)
		{
			sum+=i;
			i+=2;
		}
		//System.out.printf("2+4+...+100=%d %n",sum);
		System.out.printf("All Even=%d %n", sum);
		}
}
*/
/*
public class J324
{
	public static void main(String args[])
	{
		for (int i=2; i<=9; i++)
		{
			for (int j=2; j<=9; j++)
			{	
				System.out.printf("%d*%d=%d; \t",i, j, i* j);
			}
			System.out.println();
		}
	}
}
//3*8?
*/
public class J324
{
	public static void main(String args[])
	{
		for (int i=1; i<=9; i++)//i=1
		{
			for (int j=1; j<=i; j++)//j=1,j<=i
			{	
				System.out.print(j);//print(j)
			}
			System.out.println();
		}
	}
}