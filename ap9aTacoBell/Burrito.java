import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;

//This is the subclass Burrito, which is child to parent class MenuItem.
public class Burrito extends MenuItem {

    private ArrayList<String> ingredients = new ArrayList<String>();

    //TASK 6: Use the super() constructor to call the no-argument constructor from the parent class.
    public Burrito()
    {
        super();
        System.out.println("");
    }

    //TASK 7: Use the super(~) constructor to call the ArrayList argument constructor from the parent class.  Initialize the private instance ArrayList ingredients from newBurrito (hint--get the proper index)
    public Burrito(ArrayList<Object> newBurrito) {super(newBurrito);ingredients = (ArrayList<String>)newBurrito.get(6);}

    //TASK 8: Use the super.toString method to add the ingredients list to the output from toString.

    public String toString()
    {
        return "\nThis is a Burrito:\n" + super.toString() + "\nIngredients: " + ingredients;
    }

}