import java.awt.*;
import java.awt.font.*;
import java.awt.geom.*;
import java.awt.image.BufferedImage;
import java.text.*;
import java.util.*;
import java.util.List; // resolves problem with java.awt.List and java.util.List
import java.lang.Math;

/**
 * A class that represents a picture.  This class inherits from 
 * SimplePicture and allows the student to add functionality to
 * the Picture class.  
 * 
 * Copyright Georgia Institute of Technology 2004-2005
 * @author Barbara Ericson ericson@cc.gatech.edu
 */
public class Picture extends SimplePicture 
{
  ///////////////////// constructors //////////////////////////////////
  
  /**
   * Constructor that takes no arguments 
   */
  public Picture ()
  {
    /* not needed but use it to show students the implicit call to super()
     * child constructors always call a parent constructor 
     */
    super();  
  }
  
  /**
   * Constructor that takes a file name and creates the picture 
   * @param fileName the name of the file to create the picture from
   */
  public Picture(String fileName)
  {
    // let the parent class handle this fileName
    super(fileName);
  }
  
  /**
   * Constructor that takes the width and height
   * @param width the width of the desired picture
   * @param height the height of the desired picture
   */
  public Picture(int width, int height)
  {
    // let the parent class handle this width and height
    super(width,height);
  }
  
  /**
   * Constructor that takes a picture and creates a 
   * copy of that picture
   */
  public Picture(Picture copyPicture)
  {
    // let the parent class do the copy
    super(copyPicture);
  }
  
  /**
   * Constructor that takes a buffered image
   * @param image the buffered image to use
   */
  public Picture(BufferedImage image)
  {
    super(image);
  }
  
  ////////////////////// methods ///////////////////////////////////////
  
   /** switchColors() traverses the 2D pixel array and 
      * switches the RGB colors.
      */
     public void switchColors()
     {
       Pixel[][] pixels = this.getPixels2D();
       int red, green, blue = 0;

       for (Pixel[] rowArray : pixels)
        {
          for (Pixel p: rowArray)
          {
           red = p.getRed();
           green = p.getGreen();
           blue = p.getBlue();
           p.setRed(green);
           p.setGreen(blue);
           p.setBlue(red);
         }
       }
     }

  /** negate() will get the current red, blue, and green values of each pixel
   * then subtract all three values from 255 and set each pixel to those new values
   */
  public void negate() {
    Pixel[][] pixels = this.getPixels2D();
    int red, green, blue = 0;

    for (Pixel[] row : pixels) {
      for (Pixel pixel: row) {
        red = pixel.getRed();
        green = pixel.getGreen();
        blue = pixel.getBlue();
        pixel.setRed(255 - red);
        pixel.setGreen(255 - green);
        pixel.setBlue(255 - blue);
      }
    }
  }

  /** grayscale() will get the current red, blue, and green values of each pixel
   * then average the three values (rounding down to the integer below)
   * set all three color values to the average
   */
  public void grayscale() {
    Pixel[][] pixels = this.getPixels2D();
    int red, green, blue, avg = 0;

    for (Pixel[] row: pixels) {
      for (Pixel pixel: row) {
        red = pixel.getRed();
        green = pixel.getGreen();
        blue = pixel.getBlue();

        avg = (red + green + blue) / 3;
        pixel.setRed(avg);
        pixel.setGreen(avg);
        pixel.setBlue(avg);
      }
    }
}

/** grayWindowColorBorder() will apply the grayscale method only to the interior
 * of a rectangle centered inside the image, thus showing a picture with only
 * a grayscale image in the window but color on the border
 */
public void grayWindowColorBorder() {
  Pixel[][] pixels = this.getPixels2D();
  int red, green, blue, avg = 0;

  for (int k = (int) (pixels.length * 0.15); k < pixels.length - (int) (pixels.length * 0.15);k++){
    for (int j = (int) (pixels[0].length * 0.15); j < pixels[0].length - (int) (pixels[0].length * 0.15);j++){
      red = pixels[k][j].getRed();
      green = pixels[k][j].getGreen();
      blue = pixels[k][j].getBlue();

      avg = (red + green + blue) / 3;
      pixels[k][j].setRed(avg);
      pixels[k][j].setGreen(avg);
      pixels[k][j].setBlue(avg);
    }
  }
}

/** stripes() will create three horizontal stripes within the image such that
 * the top stripe remove all red, the center stripe removes all green, and the
 * bottom most strip removes all blue
 */
public void stripes() {
    Pixel[][] pixels = this.getPixels2D();
    int red, green, blue, rowNum = 0;

    for (Pixel[] row: pixels) {
      rowNum++;
      for (Pixel pixel: row) {
        if (rowNum <= pixels.length / 3) {
          pixel.setRed(0);
        }
        if(rowNum > pixels.length / 3 && rowNum <= pixels.length / 3 * 2) {
          pixel.setGreen(0);
        }
        if(rowNum > pixels.length / 3 * 2) {
          pixel.setBlue(0);
        }
      }
    }
}

/** randomMeme() selects the name of a random meme and applies it to the
 * object declaration
 * @return the name of the random meme
 */
public static String randomMeme() {
  String[] fileNames = {"charlie.jpg", "doge.jpg", "keanu.jpg", "likeitalot.jpg",
  "loverboy.jpg", "rollsafe.jpg", "roz.jpg", "spongebob.jpg"};

  return fileNames[(int) (Math.random() * fileNames.length)];
}

/** randomBlack() will randomly turn  about 25% of the pixels black
 *
 */
public void randomBlack() {
  Pixel[][] pixels = this.getPixels2D();
  int changedPixels = 0;
  int randoRow, randoColumn = 0;

  while (changedPixels < pixels.length * pixels[0].length / 4) {
    randoRow = (int) (Math.random() * pixels.length);
    randoColumn = (int) (Math.random() * pixels[0].length);
    Pixel pixel = pixels[randoRow][randoColumn];

    if(pixel.getRed() != 0 || pixel.getGreen() != 0 || pixel.getBlue() != 0){
      pixel.setRed(0);
      pixel.setGreen(0);
      pixel.setBlue(0);
      changedPixels++;
    }
  }
}

/** decay() will traverse through each pixel and reset the largest of the three
 * color values to one less than its current value
 */
public void decay() {
  Pixel[][] pixels = this.getPixels2D();

  for (Pixel[] row: pixels) {
    for (Pixel pixel : row) {
      if (pixel.getRed() >= pixel.getGreen() && pixel.getRed() >= pixel.getBlue()){pixel.setRed(pixel.getRed() - 10);}
      if (pixel.getGreen() >= pixel.getRed() && pixel.getGreen() >= pixel.getBlue()){pixel.setGreen(pixel.getGreen() - 10);}
      if (pixel.getBlue() >= pixel.getRed() && pixel.getBlue() >= pixel.getGreen()){pixel.setBlue(pixel.getBlue() - 10);}
    }
  }
}

/** flip() will flip the image 90 degrees*/
public void flip() {
  Pixel[][] pixels = this.getPixels2D();
  Pixel[][] out = new Pixel[pixels[0].length][pixels.length];

  for (int y=0; y<pixels.length; y++) {
    for (int x=0; x<pixels[y].length; x++) {
      out[x][y] = pixels[y][x];
    }
  }
  SimplePicture sp = new SimplePicture(pixels.length, pixels[0].length);
  for (int y=0; y<sp.getHeight(); y++) {
    for (int x=0; x<sp.getWidth(); x++) {
      sp.getPixel(x,y).setColor(out[y][x].getColor());
    }
  }
  sp.show();
}

public void rot(int deg) {
    Pixel[][] pixels = this.getPixels2D();
    Pixel[][] out = new Pixel[pixels[0].length][pixels.length];

    int orginY = pixels.length/2;
    int orginX = pixels[0].length/2;
    for (int y=0; y<pixels.length; y++) {
      for (int x=0; x<pixels[y].length; x++) {
        try{
          int newX = (int) (x*Math.cos(deg) - y *Math.sin(deg));
          int newY = (int) (y*Math.cos(deg) + x *Math.sin(deg));

          out[y+orginY][x+orginX] = pixels[newY][newX];
        } catch(Exception ignored) {}
      }
    }
    SimplePicture sp = new SimplePicture(pixels.length, pixels[0].length);
    for (int y=0; y<sp.getHeight(); y++) {
      for (int x=0; x<sp.getWidth(); x++) {
        try {
          sp.getPixel(x, y).setColor(out[y][x].getColor());
        } catch (Exception ignored) {
        }

      }
    }
    sp.show();
  }
  /**
   * Method to return a string with information about this picture.
   * @return a string with information about the picture such as fileName,
   * height and width.
   */
  public String toString()
  {
    String output = "Picture, filename " + getFileName() + 
      " height " + getHeight() 
      + " width " + getWidth();
    return output;

  }
 

  
} // this } is the end of class Picture, put all new methods before this
 