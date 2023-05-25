import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;

//This is the subclass Chalupa, which is child to parent class MenuItem.  
public class Chalupa extends MenuItem {

  private ArrayList<String> ingredients = new ArrayList<String>();

  //TASK 6: Use the super() constructor to call the no-argument constructor from the parent class.
  public Chalupa()
  {
    super();
    System.out.println("");
  }

    //TASK 7: Use the super(~) constructor to call the ArrayList argument constructor from the parent class.  Initialize the private instance ArrayList ingredients from newChalupa (hint--get the proper index)
  public Chalupa(ArrayList<Object> newChalupa) {super(newChalupa);ingredients = (ArrayList<String>)newChalupa.get(6);}

  //TASK 8: Use the super.toString method to add the ingredients list to the output from toString.

  public String toString()
  {
    return "\nThis is a Chalupa:\n" + super.toString() + "\nIngredients: " + ingredients;
  }
  
}