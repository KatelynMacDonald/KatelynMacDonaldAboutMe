import java.util.Scanner;
import java.lang.Math;


public class MacdonaldU1S1Problems {
    public static void main(String[] args){
        //static means,no object required
        //convertMiletoKM();
        //calculateEnergy();
        futureInvestments();
        //drivingCosts();

    }

    private static void convertMiletoKM(){
        Scanner ui = new Scanner(System.in);
        //recreate the Scanner object and close the scanner object in each function
        //System.out.println("Convert Miles to KM");
        System.out.println("What is the miles? ");
        Double miles = ui.nextDouble();  
        Double kilometers= miles * 1.6;
        System.out.println(miles+" miles is "+ kilometers+ " kilometers");

        ui.close();
    }

    private static void calculateEnergy(){
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter the amount of water in kilograms ");
        Double m = ui.nextDouble();
        System.out.println("Enter the initial temperature ");
        Double intitalTemp = ui.nextDouble();
        System.out.println("Enter the final temperature ");
        Double finalTemp= ui.nextDouble();
        Double q= m*(finalTemp - intitalTemp) *4184;
        System.out.println("The energy needed is "+q);

        ui.close();
    }
    
    private static void futureInvestments(){
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter investment amount ");
        Double investmentAmount=ui.nextDouble();
        System.out.println("Enter annual interest rate in percentage ");
        Double monthlyInterestRate=(ui.nextDouble())/12/100;
        System.out.println("Enter number of years ");
        Double numberOfYears=ui.nextDouble();
        Double power=numberOfYears*12;
        Double pow= Math.pow(1+monthlyInterestRate,power);
        Double futureInvestmentValue=(investmentAmount*pow);
        //DecimalFormat df = new DecimalFormat("#.##");
        String newfiv = String.format("%.02f", futureInvestmentValue);              //https://www.java67.com/2014/06/how-to-format-float-or-double-number-java-example.html
        System.out.println("Future value is $" + newfiv);
        ui.close();

    }

    private static void drivingCosts(){
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter the driving distance ");
        Double distance= ui.nextDouble();
        System.out.println("Enter miles per gallon ");
        Double miles=ui.nextDouble();
        System.out.println("Enter prince per gallon ");
        Double price= ui.nextDouble();
        Double cost= (distance/miles)*price;
        //DecimalFormat df = new DecimalFormat("#.##");       //https://stackoverflow.com/questions/8137218/trim-double-to-2-decimal-places
        String newcost = String.format("%.02f", cost);
        System.out.println("The cost of driving is $"+ newcost);
        

        ui.close();

    }
}
