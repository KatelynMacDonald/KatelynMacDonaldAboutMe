import java.util.Scanner;
import java.lang.Math;


public class MacdonaldU1S12Problems {
    public static void main(String[] args){
        //midPointTable();
        //triangleArea();
        //minuteYearConverter();
        //triangleVolume();

    }

    private static void triangleArea(){
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter x1: ");
        double x1 = ui.nextDouble();
        System.out.println("Enter y1: ");
        double y1 = ui.nextDouble();
        System.out.println("Enter x2: ");
        double x2 = ui.nextDouble();
        System.out.println("Enter y2: ");
        double y2 = ui.nextDouble();
        System.out.println("Enter x3: ");
        double x3 = ui.nextDouble();
        System.out.println("Enter y3: ");
        double y3 = ui.nextDouble();
        double side1= Math.sqrt(Math.pow((x2-x1 ),2)+ Math.pow((y2-y1),2));
        double side2=  Math.sqrt(Math.pow((x3-x2 ),2)+ Math.pow((y3-y2),2));
        double side3= Math.sqrt(Math.pow((x1-x3),2)+ Math.pow((y1-y3),2));
        
        
        double ss=(side1+side2+side3)/2;

        double area=Math.sqrt(ss*(ss-side1)*(ss-side2)*(ss-side3));
        System.out.println("The area of the triangle is"+area);


        

    }


    


    private static void midPointTable(){
        System.out.println("  a\t  b\tMiddle Point");
        System.out.printf("(0,0)\t(2,1)\t%s\r\n",midPoint(0,0,2,1));
        System.out.printf("(1,4)\t(4,2)\t%s\r\n",midPoint(1,4,4,2));
        System.out.printf("(2,7)\t(6,3)\t%s\r\n",midPoint(2,7,6,3));
        System.out.printf("(3,9)\t(10,5)\t%s\r\n",midPoint(3,9,10,5));
        System.out.printf("(4,11)\t(12,7)\t%s\r\n",midPoint(4,11,12,7));
    }

    private static String midPoint(double x1,double y1,double x2,double y2){
        
        double deltaX= (x2-x1)/2+x1;
        double deltay= (y2-y1)/2+y1;

        String output=("(" +deltaX+"," + deltay+")");



        return output;


    }

    private static void minuteYearConverter(){
        
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number of minutes:");
        int minutes = input.nextInt();
        int year = minutes / 525600;
        int day = minutes / 1440;
        int remainingMinutes = day % 525600;
        System.out.println(minutes + " is apporximately " + year + " years " + day +" days");
    }

    

    private static void triangleVolume(){
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter length of the sides and height of the Equilateral triangle: ");
        double length=ui.nextDouble();
        double area= Math.sqrt(3)/4*Math.pow(length,2);
        double volume =area*length;
        System.out.println(area);
        System.out.println(volume);
        
    }

}