class CBox
{
	int length, width, height;
	int volume()
	{
		return length*width*height;
	}
	int surface()
	{
		return 2*(length*width+length*height+width*height);
	}
	void show()
	{
		System.out.printf("length= %d, width= %d, height= %d \n", length, width, height);
		System.out.printf("Volume= %.1f \n", this.volume());
		System.out.printf("Surface= %.1f \n", this.surface());
		
	}
}