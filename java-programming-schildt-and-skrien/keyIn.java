//using a cast
class keyIn1 {
  public static void main(String[] args)
    throws java.io.IOException {

      System.out.print("Press a key followed by ENTER: ");

      String string1 = new String (System.in.read()); // get a char

      System.out.println("Your key is: " + string1);

    }
  }
