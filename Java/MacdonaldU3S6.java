import java.util.Random;
import java.lang.Math;
import java.util.Scanner;
import java.util.Arrays;

public class MacdonaldU3S6 {
    public static void main(String[] args) {
        int[] evenOdd={1,2,3,2,1,6,3,4,5,2,3,6,8,9,9,0};
        int[] isSort={21,11,9,7,5,4,4,3,1,1};
        int[] isNotSort={10,1,5,16,61,9,11,1};
        int[] list1={1,5,16,61,111};
        int[] list2={2,4,5,6};
        //evenOddChecker(evenOdd);
        /*if (isSorted(isSort)==false){
            System.out.println("The list is not sorted");
        }
        else if (isSorted(isSort)==true){
            System.out.println("The list is sorted");
        }
        if (isSorted(isNotSort)==false){
            System.out.println("The list is not sorted");
        }
        else if (isSorted(isNotSort)==true){
            System.out.println("The list is sorted");
        }*/
        printArray(merge(list1,list2));
    }

    private static void evenOddChecker(int[] listy){
        Scanner ui = new Scanner(System.in);
        //asking the user for numbers
        //ArrayList <Integer> numbers= new ArrayList<Integer>();
        //ArrayList <Integer> odd= new ArrayList<Integer>();
        //ArrayList <Integer> even= new ArrayList<Integer>();
        int oddNum=0;
        int evenNum=0;
        for(int i=0;i<listy.length;i++){
            //System.out.println("Give me a number: ");
            //double newNumber=ui.nextDouble();
            //numbers.add(newNumber);
            if (listy[i]%2==0){
                evenNum+=1;
            }
            else if (listy[i]%2==1){
                oddNum+=1;
            }
           

        }
        System.out.println("The number of odd numbers: "+ oddNum);
        System.out.println("The number of even numbers: "+ evenNum);

    }

  


    private static boolean isSorted(int[] listy){
        boolean bool=false;
        for(int i=0;i<listy.length-1;i++){
                System.out.println(bool+" "+i);
           
                if (listy[i]> listy[i+1]){
                    bool=true;
                }
                else if (listy[i]== listy[i+1]){
                    bool=true;
                }
                else if(listy[i]<listy[i+1]){
                    bool=false;
                    return bool;
                }
            
            
        }
        return bool;
    }

    private static int[] merge(int[] list1, int[] list2){
        int[] allNum= new int[list1.length+list2.length];
        //System.out.println(allNum.length);
        for (int i=0; i<list1.length;i++){
            allNum[i]=list1[i];
            //System.out.println(list1[i]);
            //System.out.println(i);
            //System.out.println(allNum[i]);

        }
        int r = list1.length ;
        for (int i=0;i<list2.length;i++){
            
            //System.out.println(r);
            allNum[r]=list2[i];
            //System.out.println(allNum[r]);
            r=r+1;
            //System.out.println(i+r);
        }
        //System.out.println(allNum);
        Arrays.sort(allNum);
        
        return allNum;
    }

    private static void printArray(int[] listy){
        for(int i=0;i<listy.length;i++){
            System.out.println(listy[i]);
        }
    }


}
