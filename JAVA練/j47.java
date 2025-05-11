/*public class j47
{
	public static void main(String[] args)
	{
		for (int i= 1; i<=10; i++)
		{
			if(i==7)//
				break;//
			System.out.printf("%d, ", i);
		}	
		System.out.println();

		for (int i= 1; i<=10; i++)
		{
			if(i%3==0)//
				continue;//
			System.out.printf("%d, ", i);
		}	
		System.out.println();		
	}
}                                                           
*/
public class j47
{
	public static void main(String[] args)
	{
		String name[]={"John","Mary","Tom","Iris"};
		String subject[]={"Lang","Math","Science"};
		int score[][]={{89,87,79},{98,56,78},{99,89,59},{78,56,98}};
		
		System.out.print("\t");
		for (int i=0; i<subject.length; i++)
			System.out.printf("%s \t", subject[i]);
		System.out.println("Total \t Average");
		System.out.println("==========================================");
		
		for (int i=0; i<score.length;i++)
		{
			int rsum=0;
			System.out.printf("%s\t",name[i]);
			for (int j=0; j<score[i].length;j++)
			{
				rsum+=score[i][j];
				System.out.printf("%d \t",score[i][j]);
			}
			System.out.printf("%d \t %>1f \n",rsum, (double)rsum/3);
		}
	}
}                                                           