/*

CONVOLUTION DAY : PERFORM LINEAR & CIRCULAR CONVOLUTION ON INPUT SIGNALS

*/
import java.io.*;
import java.util.*;

class Convolution{
  
  static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
  
  public static List<Integer> readSignal(String s){
      return new LinkedList<Integer>(){
          List<Integer> n=new LinkedList<Integer>();
          n.add(2);
          return n;
      };
  }
  
  public static void main(String[] args)throws IOException{
    
    System.out.println("Enter values of x(n){Ex:1,2,3}");
    String inputResponse="";
    inputResponse=br.readLine();
    List<Integer> x=readSignal(inputResponse);
    System.out.println(x.toString());
    
  }
  
  
}
