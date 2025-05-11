public class b331{
	public static void main(String[] args){
		for (int i=1; i<=9; i++){// i,j =0; i,j<9 or i,j=1; i,j<10
			for (int j=1; j<=i; j++){//動態:內迴圈
				System.out.print(j);//printf("*") ;print(j); printf("%d", j)
			}
			System.out.println();
		}
		for (int i=1; i<=9; i++){
			for (int j=1; j<=9-i; j++){
				System.out.print(j);
			}
			System.out.println();
		}
		System.out.println("----------------------------------");
		for (int i=1; i<=9; i++){
			for (int j=9; j>=10-i; j--){//j>=i
				System.out.print(j);
			}
			System.out.println();
		}
	}
}

