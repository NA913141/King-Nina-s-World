public class N568//u8 7
{
	public static void main(String[] args) 
	{
		CTest ct = new CTest();

		ct.test(3); 
		ct.test(8);  
		ct.test(0);  
	}
}
//u8 12
class CTest 
{
	public void test(int x) 
	{
		if (x == 0) 
		{
			System.out.println(x + " 為 0");
		} else if (x % 2 == 0) 
		{
			System.out.println(x + " 為偶數");
		} else 
		{
			System.out.println(x + " 為奇數");
		}
	}
}
*/
class CWin {
    int width;
    int height;
    String name;

    // (a) 如果在建立 CWin 物件後沒有立即設定寬度和高度，它們將保持初始的預設值。
    //     之後可以使用 setW() 和 setH() 方法來設定這些屬性。
    void setW(int w) {
        width = w;
    }

    void setH(int h) {
        height = h;
    }

    void setName(String n) {
        name = n;
    }

    public void show() {
        System.out.println("Name=" + name);
        System.out.println("Width=" + width + ", Height=" + height);
    }

    // (b) 試撰寫 setWindows(int w, int h) 函式，使得它可以同時設定 CWin 物件的 width 與 height。
    public void setWindows(int w, int h) {
        width = w;
        height = h;
    }

    // (c) 承上題，請擴充 setWindows() 函式，使得它可以同時設定 CWin 物件的 width、height 與 name。
    public void setWindows(int w, int h, String n) {
        width = w;
        height = h;
        name = n;
    }
}

public class N568 {
    public static void main(String[] args) {
        CWin cw = new CWin();
        cw.setName("My Windows");
        cw.setW(5);
        cw.setH(8);
        cw.show();

        // 測試修改後的 setWindows 方法
        CWin cw2 = new CWin();
        cw2.setWindows(10, 20); // 使用 (b) 的方法
        cw2.show();

        CWin cw3 = new CWin();
        cw3.setWindows(15, 25, "Another Window"); // 使用 (c) 的方法
        cw3.show();
    }
}
