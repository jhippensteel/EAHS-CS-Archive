import java.util.Scanner;

/**
 * A simple class to run the Magpie class.
 * @author Laurie White
 * @version April 2012
 */
public class Main
{

	/**
	 * Create a Magpie, give it user input, and print its replies.
	 */
	public static void main(String[] args)
	{
		Magpie4 maggie = new Magpie4();

		System.out.println (maggie.getGreeting());
		Scanner in = new Scanner (System.in);
		String statement = in.nextLine();
		statement = statement.toLowerCase();


		while (!statement.equals("Bye"))
		{

			while (statement.trim().length() == 0){
				System.out.println("Say something, please.");
				statement = in.nextLine();
				statement = statement.toLowerCase();
			}

			System.out.println (maggie.checkSpelling(statement));
			statement = in.nextLine();
		}
		System.out.println("Goodbye!");
	}
}