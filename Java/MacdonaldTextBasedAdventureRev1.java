import java.util.Random;
import java.lang.Math;
import java.util.Scanner;

public class MacdonaldTextBasedAdventureRev1 {
    public static void main(String[] args) {
        //creates the scanner
        Scanner ui = new Scanner(System.in);
        System.out.println("Welcome to Spongebob's Adventure\nHere are the controls:\nLook where you are using the command 'ls'\nMove to a new location using the command 'cd LOCATION'\nYou can back track using the command 'cd ..'\nInteract with things using the command 'use ITEM'\nTo talk to people use the command 'talk to PERSON'\nIf you forget where you are type 'pwd'\nNow go explore Bikini Bottom. To start, type in 'ls' " );
        String input = ui.nextLine();
        //makes the game keep going
        while (input!="/"){
            // List<String> krabyPattyList = new ArrayList<>(); 
            if(input.equals("ls")){
                System.out.println("Location:   Spongebob's house\nPeople:     Gary the snail\nItems:      Welcome note");
            }
            String location="spongbob's house";
            System.out.println("Would you like to go outside? ");
            input = ui.nextLine();
            boolean doNotPass=true;
            while(doNotPass){           //this makes sure that the user inputs a yes or a no. If not it will ask the question again
                if (input.equals("yes") || input.equals("no")){        
                    doNotPass=false;}
                else{
                    System.out.println("Would you like to go outside? ");
                    input = ui.nextLine();
                    }
            }
            //will change the location if they want to go outside
            if (input.equals("yes")){
                System.out.println("Location:   Outside Spongebob's house\nPeople:     Patrick and Squidward\nItems:      Bubbles");
                location="outside spongebob's house";
                System.out.println(" ");
                input = ui.nextLine();
                }

            if (input.equals("no")){
                System.out.println("Location:   Spongebob's house\nPeople:     Gary the snail\nItems:      Welcome note");
                location="spongebob's house";
                System.out.println(" ");
                input = ui.nextLine();}

            if (input.equals("cd spongebob's house")){
                System.out.println("Location:   Spongebob's house\nPeople:     Gary the snail\nItems:      Welcome note");
                location="spongebob's house";
                System.out.println(" ");
                input = ui.nextLine();}

            if (input.equals("cd jellyfish fields")){
                System.out.println("Location:   Jellyfish Fields\nPeople:     Patrick\nItems:      Jellyfish Net");
                location="jellyfish fields";
                System.out.println(" ");
                input = ui.nextLine();}









            if (input.equals("use jellyfish net")){
                System.out.println("Location:   Jellyfish Fields\nPeople:     Patrick\nItems:      Jellyfish Net");
            location="jellyfish fields";
            System.out.println(" ");
            input = ui.nextLine();}
            if (input.equals("use jellyfish net")){
                System.out.println("How many jellyfish would you like to catch?\nFor each jellyfish you catch you get 3/4 oz of jelly! ");
                //takes the number that the user inputs and will calculate how much jelly
                int jellyfish = ui.nextInt();
                int total=0;
                total+=(jellyfish*0.75);
                for (int i =0; i<jellyfish;i++){        //will output however many jellyfish the user put 
                    System.out.println("=)");}
                    System.out.printf("You caught %s jellyfish",jellyfish);
                System.out.printf("You got %soz of jelly!",total);
                System.out.println(" ");
                input = ui.nextLine();  
            }
            



            if (input.equals("cd outside spongebob's house") || input.equals("cd outside")){
                System.out.println("Location:   Outside Spongebob's house\nPeople:     Patrick and Squidward\nItems:      Bubbles");
                location="outside spongebob's house";
                System.out.println(" ");
                input = ui.nextLine();}

            if (input.equals("cd the krusty krab") || input.equals("cd krusty krab")){
                System.out.println("Location:   The Krusty Krab\nPeople:     Mr. Krabs and Squidward\nItems:      Spatula");
                location="the krusty krab";
                System.out.println(" ");
                input = ui.nextLine();
                if (input.equals("use spatula")){
                    double total=3.00;
                    System.out.println("You get a krabby patty($3.00) for helping Mr. Krabs so much!\nBut you have to pay for this because Mr. krabs is stingy.\nEach item you add on your burger adds $0.25 to your order. \nType anything(except f) to continue.");
                    input = ui.nextLine();
                    while (input!="f"){         //while the user isn't finished(f) then it will keep asking the question below
                        System.out.println("Would you like toppings(t),\nwould you just like it plain(f), print out toppings(p),\nor are you finished(f)? ");
                            input = ui.nextLine();
                            if (input.equals("t")){
                                System.out.println("what would you like on your burger?\nPlease only put one item at a time.Ketchup(k),\nMustard(m), Tomatoes(t), Onions(o), Lettuce(l),\nPickles(p), or don't want anymore toppings(f)");
                                input = ui.nextLine();
                                //krabyPattyList.append(userInput)            //every topping that they pick it will put it in the list and prints it out at the end
                                total+=0.25     ;        //everytime the user wants a topping it will add 0.25 to the total and then print the total at the end
                                }
                            else if (input.equals("p")){
                                System.out.printf("Your kraby patty costs $ %s", total);}
                            System.out.println(" ");
                            input = ui.nextLine();
                        }
                }

    if (input.equals("ls") && location.equals("spongebob's house")){
        System.out.println("Location:   Spongebob's house\nPeople:     Gary the snail\nItems:      Welcome note");
        location="spongebob's house";
        System.out.println(" ");
        input = ui.nextLine();}








    
    if (input.equals("ls") && location.equals("jellyfish fields")){
        System.out.println("Location:   Jellyfish Fields\nPeople:     Patrick\nItems:      Jellyfish Net");
        location="jellyfish fields";
        System.out.println(" ");
        input = ui.nextLine();}
        if (input.equals("use jellyfish net")){
            System.out.println("How many jellyfish would you like to catch?\nFor each jellyfish you catch you get 3/4 oz of jelly! ");
            //takes the number that the user inputs and will calculate how much jelly
            int jellyfish = ui.nextInt();
            int total=0;    
            total+=(jellyfish*0.75);
            for (int i =0; i<jellyfish;i++){        //will output however many jellyfish the user put 
                System.out.println("=)");}
            System.out.printf("You got %s oz of jelly!",jellyfish);
            System.out.println(" ");
            input = ui.nextLine();  
        }
        else if (input.equals("|")) {
            System.out.println(" ");
            input = ui.nextLine();  
        }
    }







    if (input.equals("ls") && location.equals("outside spongebob's house")){
    System.out.println("Location:   Outside Spongebob's house\nPeople:     Patrick and Squidward\nItems:      Bubbles");
        location="outside spongebob's house";
        System.out.println(" ");
        input = ui.nextLine();}

    if (input.equals("ls") && location.equals("the krusty krab")){
        System.out.println("Location:   The Krusty Krab\nPeople:     Mr. Krabs and Squidward\nItems:      Spatula");
        location="the krusty krab";
        System.out.println(" ");
        input = ui.nextLine();
        if (input.equals("use spatula")){
            double total=3.00;
            System.out.println("You get a krabby patty($3.00) for helping Mr. Krabs so much!\nBut you have to pay for this because Mr. krabs is stingy.\nEach item you add on your burger adds $0.25 to your order. \nType anything(except f) to continue.");
            input = ui.nextLine();
            while (input!="f"){     //will keep asking the question until you type f
                System.out.println("Would you like toppings(t),\nwould you just like it plain(f), print out toppings(p),\nor are you finished(f)? ");
                input = ui.nextLine();
                if (input.equals("t")){
                    System.out.println("what would you like on your burger?\nPlease only put one item at a time.Ketchup(k),\nMustard(m), Tomatoes(t), Onions(o), Lettuce(l),\nPickles(p), or don't want anymore toppings(f)");
                    
                    input = ui.nextLine();
                    //krabyPattyList.add(input);
                    total+=0.25;
                }
                else if(input.equals("p")){
                    System.out.printf("Your last topping is %s",input);
                }
                else if (input.equals("f")){
                //     System.out.println(krabyPattyList);}
                System.out.printf("Your Kraby Patty is $%s", total);}
            }
                
            System.out.println(" ");
            input = ui.nextLine();
        }
    }
    


        }
    }
    
    }
