public class c331
{
	public static void main(String[] args)
	{
		int kkk[][]={{1,2,3,4,},{5,6,7,8},{9,10,11,12}};//3列
		for (int i= 0; i<kkk.length; i++)
		{
			int rsum= 0;//2
			for (int j= 0; j<kkk[i].length; j++)
			{
				rsum+= kkk[i][j];//2
				System.out.printf("%d\t", kkk[i][j]);
			}
			System.out.printf("%d \t %.1f %n", rsum, (double)rsum/kkk[i].length);//System.out.println(); (double)很重要,test強制執行
		}
	}
}                      