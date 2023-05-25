import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;

//This is the superclass MenuItem.  It is the parent class of the subclasses Chalupa, Burrito, Quesarito, Gordita, and Taco.

public class MenuItem {
		
    private String itemName;
		private double itemPrice;
		private int calories;
		private int fat;
		private int carbs;
		private int protein;

    //TASK 1: create instance variables for the four pieces of nutrition data



    //TASK 2: finish this no-argument constructor for a menu item.  This will be called using super() from subclasses.
    public MenuItem()
    {
      this.itemName = "";
      this.itemPrice = 0.0;
	  this.calories = 0;
	  this.fat = 0;
	  this.carbs = 0;
	  this.protein = 0;
      
    }

    //TASK 3: finish this constructor for a menu item.  This will be called using super(~) from subclasses.
		public MenuItem(ArrayList<Object> newItem) {
			this.itemName = (String) newItem.get(0);
			this.itemPrice = (double) newItem.get(1);
			this.calories = (int) newItem.get(2);
			this.fat = (int) newItem.get(3);
			this.carbs = (int) newItem.get(4);
			this.protein = (int) newItem.get(5);

      

		}



    //TASK 4: create get methods for all of the instance variables
		public double getPrice() {
			return itemPrice;
		}

  		public String getItemName() {
			return itemName;
		}

		/**getCalories() returns the number of calories as an int*/
		public int getCalories() {return calories;}

		/**getFat() returns the amount of fat as an int*/
		public int getFat() {return fat;}

		/**getCarbs() returns the number of carbs as an int*/
		public int getCarbs() {return carbs;}

		/**getProtein returns the amount of protein as an int*/
		public int getProtein() {return protein;}
		
		//TASK 5: Finish this toString method that prints out a line-separated summary of the menuItem.  This will be called using super.toString() from subclasses.
		public String toString() {
			return "\n\nItem: " + itemName + "\nPrice: " + itemPrice + "\nCalories: " + calories + "\nFat: " + fat + "\nCarbs: " + carbs + "\nProtein: " + protein;
		}




	}

