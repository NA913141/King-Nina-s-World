public class n428
{
	public static void main(String[] args)
	{
		int[] arr={65, 89, 45, 46, 56, 78, 32};
		int[][] arr2={{65, 89, 45, 46}, {56, 78, 32, 89}};//兩列 二維
		max_min(arr);
		max_min(arr2);
	} 
	
	public static void max_min(int[][] a)
	{
		int max=a[0][0], min=a[0][0];
		for (int i= 0;i<a.length;i++)
		{
			for (int j= 0;j< a[i].length; j++)
			{
				System.out.printf("%d, ",a[i][j]);
				if (max<a[i][j])
					max=a[i][j];
				if (min>a[i][j])
					min=a[i][j];
			}
			System.out.println();
			/*
			System.out.printf("%d, ",a[i]);
			if (max<a[i])
				max=a[i];
			if (min>a[i])
				min=a[i];
			*/
		}
		System.out.println("-----------------------------");
		System.out.printf("Max: %d and Min: %d \n",max ,min);
	}
	
	public static void max_min(int[] a)
	{
		int max=a[0], min=a[0];
		for (int i= 0;i<a.length;i++)
		{
			System.out.printf("%d, ",a[i]);
			if (max<a[i])
				max=a[i];
			if (min>a[i])
				min=a[i];
		}
		System.out.println();
		System.out.printf("Max: %d and Min: %d \n",max ,min);
	}
}