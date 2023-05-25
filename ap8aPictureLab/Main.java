import javax.swing.*;
import java.awt.event.*;
import java.util.*;
import java.awt.*;
import java.io.File;


// Picture Lab Exploration

// Follow the description and write five additional methods besides the example switchcolors.

// Write all methods in Picture.java.  All other files should remain untouched.

// To demo each method, we will simply change the code in the main method below.



public class Main {
  public static void main(String[] args) { 

        String meme = Picture.randomMeme();

        Scanner scan = new Scanner(System.in);
        String pic = meme;//"rollsafe.jpg";
        Picture image = new Picture(pic);
        image.rot(45);  //change this line to test other methods
        //image.show();


/*
        while(true)
        {
          image.decay();
          image.show();
          String x = scan.nextLine();
          image.hide();
        }
        */
      }

} 
