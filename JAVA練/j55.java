class Rectangle// no main method 不會執行，僅查調 , rect縮寫, class檔
{
	int length, width;
	int area()//int>>return
	{
		return length*width;
	}
	int peri()//int>>return
	{
		return 2*(length+width);
	}
	void show()
	{
		System.out.printf("Length= %d, Width= %d \n", length, width);
	}
}

public class j55
{
	public static void main(String[] args)
	{
		Rectangle obj1=new Rectangle();//宣告=建立在記憶體上(人類王曉明...
		obj1.length=3;
		obj1.width=5;
		obj1.show();
		System.out.printf("Area= %d \n", obj1.area());
		System.out.printf("Perimeter= %d \n", obj1.peri());
		
		Rectangle r1=new Rectangle();//宣告=建立在記憶體上(人類王曉明...
		r1.length=6;
		r1.width=4;
		r1.show();
		System.out.printf("Area= %d \n", r1.area());
		System.out.printf("Perimeter= %d \n", r1.peri());
	}
}