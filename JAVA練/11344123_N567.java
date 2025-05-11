public class N567//u7 5
{
	public static void main(String[] args)
	{
		double celsius = 20;
		double fahrenheit = fahrenheit(celsius);
		System.out.printf("攝氏 %.1f 度 = 華氏 %.1f 度\n", celsius, fahrenheit);
	}

	public static double fahrenheit(double c)
	{
		return (9.0 / 5) * c + 32;
	}

}
//u7 16
public class N567 
{
	public static void main(String[] args)
	{
		int a[][] = 
		{
			{2, 4, 6},
			{1, 3, 5},
			{8, 9}
		};

		double avg = average(a);
		System.out.printf("所有元素的平均值為：%.2f\n", avg);
	}

	public static double average(int[][] array)
	{
		int sum = 0;
		int count = 0;

		for (int i = 0; i < array.length; i++) 
		{
			for (int j = 0; j < array[i].length; j++) 
			{
				sum += array[i][j];
				count++;
			}
		}

		return (double) sum / count;
	}
}