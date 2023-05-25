import java.util.*;
import java.util.ArrayList;
import java.util.Scanner;



public class Menu 
{
	private ArrayList<MenuItem> order;
	private int totalItems;
	
	public Menu()
  {
		order = new ArrayList<MenuItem>();
		totalItems = 0;
	}
	
	public void add(MenuItem i) {
		order.add(i);
		totalItems++;
	}
	

	public void printOrder() {
		System.out.println(order);
	}

  //TASK 10: Complete this loop 
  public void printByType(String request) {
    for(MenuItem i: order)
      {
        if((i.getClass().getName().equals(request)))
        {
          System.out.println(i);
        }

      }
  }
	

	
	
}