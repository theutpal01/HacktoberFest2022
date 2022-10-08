
public class pattern
{
	public static void main(String[] args) {
	    int j=0;
	    for(int i=0;i<4;i++){
	        for(j=0;j<=i;j++){
	            System.out.print("*");
	        }
	        for(j=0;j<(4-i-1);j++){
	            System.out.print(" ");
	        }
	         for(j=0;j<(4-i-1);j++){
	            System.out.print(" ");
	        }
	         for(j=0;j<=i;j++){
	            System.out.print("*");
	        }
	        System.out.print("\n");
	    }
	    for(int i=4;i>0;i--){
	        for(j=0;j<i;j++){
	            System.out.print("*");
	        }
	        for(j=0;j<(4-i);j++){
	            System.out.print(" ");
	        }
	        for(j=4-i;j>0;j--){
	            System.out.print(" ");
	        }
	        for(j=i;j>0;j--){
	            System.out.print("*");
	        }
	        
	        System.out.print("\n");
	    }
	}
}
