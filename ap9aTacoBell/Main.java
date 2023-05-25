import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    
    Menu menu1 = new Menu();

    //creating an ArrayList that can store different classes of objects
    ArrayList<Object> newItem = new ArrayList<>();
    
    Scanner scan = new Scanner(System.in);

    
    while(true)
      {
        newItem.clear();
        System.out.println("\033[H\033[2J");
        System.out.println("Enter the type of the menu item:");
        System.out.print("[C]halupa, [B]urrito, [Q]uesarito, [G]ordita, [T]aco\n>> ");
        String x = scan.nextLine();

        System.out.print("\nItem Name\n>> ");
        String name = scan.nextLine();
        newItem.add(name);

        System.out.print("\n-----------------\nItem Price\n>> ");
        double price = scan.nextDouble();
        newItem.add(price);

        System.out.print("\n-----------------\nCalories\n>> ");
        int cals = scan.nextInt();
        newItem.add(cals);

        System.out.print("\n-----------------\nFat (g)\n>> ");
        int fats = scan.nextInt();
        newItem.add(fats);

        System.out.print("\n-----------------\nCarbohydrates (g)\n>> ");
        int carbs = scan.nextInt();
        newItem.add(carbs);

        System.out.print("\n-----------------\nProteins (g)\n>> ");
        int proteins = scan.nextInt();
        newItem.add(proteins);


        //creating a new Chalupa
        if (x.equals("C"))
        {
          ArrayList<String> ingredients = new ArrayList<String>();
          ingredients.add("Chalupa Shell");
          String ing = "";
          String m = scan.nextLine();
          while(true)
            {
              System.out.print("\n-----------------\nAdd an ingredient (X to quit)\n>> ");
              String i = scan.nextLine();
              if (i.equals("X"))
              {
                break;
              }
              ingredients.add(i);
            }
          newItem.add(ingredients);
        

        Chalupa c = new Chalupa(newItem);

        menu1.add(c);

        } //end of new Chalupa

        if(x.equals("B")){
          ArrayList<String> ingredients = new ArrayList<String>();
          ingredients.add("Burrito Shell");
          String m = scan.nextLine();
          while(true)
          {
            System.out.print("\n-----------------\nAdd an ingredient (X to quit)\n>> ");
            String i = scan.nextLine();
            if (i.equals("X"))
            {
              break;
            }
            ingredients.add(i);
          }
          newItem.add(ingredients);


          Burrito c = new Burrito(newItem);

          menu1.add(c);
        }//End of Burrito

        if(x.equals("Q")){
          ArrayList<String> ingredients = new ArrayList<String>();
          ingredients.add("Quesarito Shell");
          String m = scan.nextLine();
          while(true)
          {
            System.out.print("\n-----------------\nAdd an ingredient (X to quit)\n>> ");
            String i = scan.nextLine();
            if (i.equals("X"))
            {
              break;
            }
            ingredients.add(i);
          }
          newItem.add(ingredients);


          Quesarito c = new Quesarito(newItem);

          menu1.add(c);
        }//End of Quesarito

        if(x.equals("G")){
          ArrayList<String> ingredients = new ArrayList<String>();
          ingredients.add("Gordita Shell");
          String m = scan.nextLine();
          while(true)
          {
            System.out.print("\n-----------------\nAdd an ingredient (X to quit)\n>> ");
            String i = scan.nextLine();
            if (i.equals("X"))
            {
              break;
            }
            ingredients.add(i);
          }
          newItem.add(ingredients);


          Gordita c = new Gordita(newItem);

          menu1.add(c);
        }//End of Gordita

        if(x.equals("T")){
          ArrayList<String> ingredients = new ArrayList<String>();
          ingredients.add("Taco Shell");
          String m = scan.nextLine();
          while(true)
          {
            System.out.print("\n-----------------\nAdd an ingredient (X to quit)\n>> ");
            String i = scan.nextLine();
            if (i.equals("X"))
            {
              break;
            }
            ingredients.add(i);
          }
          newItem.add(ingredients);


          Taco c = new Taco(newItem);

          menu1.add(c);
        }//End of Taco

          //TASK 9: Create the classes Burrito, Quesarito, Gordita, and Taco in the appropriate files.  Write proper if statements here in the main method to get the ingredients, create the correct Class of menuItem, and add to menu 1.
    
        System.out.print("\n\nWould you like to add another menu item? Q to quit or any other key to continue.\n>> ");
        String q = scan.nextLine();
        if (q.equals("Q"))
        {
          break;
        }
      } //end of menu item input loop


        //TASK 10: Write calls to the methods printOrder and printByType in Menu.java. You'll have to ask the user if they want to see all menu items, if they want to see a subclass of items (like Chalupas or Tacos), or if they are done with the program and want to quit.  Use an if-else if-else statement. The method printByType in Menu.java will need to be completed, but it's been started for you.
    while(true)
      {
        System.out.println("\n\nEnter 'All' to see the entire menu, or the name of an item such as 'Burrito' to see all of that type.  Press Q to quit.\n>> ");
        String request = scan.nextLine();
        
        if(request.equals("Q"))   //remove this later--just here to make the prgm run
        {
          break;
        }
        else if (request.equals("All")) {
          menu1.printOrder();
        }
        else{
          menu1.printByType(request);
        }
      }


       
    


  }  //end of main method
} //end of Main class