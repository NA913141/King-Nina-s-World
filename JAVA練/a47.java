import java.util.Random;
public class a47
{
	public static void main(String[] args)
	{
		Random rnd= new Random();
		int x=rnd.nextInt(100);
		double y=rnd.nextDouble();
		//System.out.printf("x= %d, y= %f",x, y);
		
		int arr[]=new int[10];
		for (int i= 0; i< 10; i++)
			arr[i]= rnd.nextInt(30,90);
		
		for (int i= 0; i< 10; i++)
			System.out.printf("Random#%d ==> %d %n",i+1, arr[i]);
		
	}
}                                                           