class Circle
{
	double r, pi=3.14;
	void setR(double n)
	{
		r=n;
	}
	double area()
	{
		return pi*r*r;
	}
	double peri()
	{
		return 2*pi*r;                                                                                                                                                                                                                                                                  
	}
	void show()
	{
		System.out.printf("Radius= %.1f \n", r);
		System.out.printf("Area= %.1f \n", this.area());
		System.out.printf("Peri= %.1f \n", peri());
	}
}