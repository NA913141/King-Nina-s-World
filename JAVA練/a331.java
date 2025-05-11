public class a331
{
	public static void main(String[] args)
	{
		int kfc[]={65, 84, 38, 16, 92, 55, 8};
		int sum= 0;//2.
		int max= 0;//int sum= 0, max= 0;
		int min= kfc[0];//int min= 10;myself
		for (int i= 0; i< kfc.length; i++)
		{
			sum+=kfc[i];//2.
			System.out.printf("kfc[%d]-->%d %n", i, kfc[i]);
			if (kfc[i]> max)
				max=kfc[i];
			if (kfc[i]< min)//if (min> kfc[i]) myself
				min=kfc[i];
		}
		System.out.printf("Total= %d; Max= %d; Min= %d %n", sum, max, min);//sum全域變數
	}
}                      