/*
This demonstrates the difference between int and double

Call this file Example3.java
*/

class Example3 {
  public static void main(String[] args) {
    int w; //this declares an int variable
    double x; // this declares floating point variable

    w = 10;

    x = 10.0;

    System.out.println("Original value of w: " + w);
    System.out.println("Original value of x: " + x);
    System.out.println();

    //now, divide both by 4
    w = w / 4;
    x = x / 4;

    System.out.println("w after division: " + w);
    System.out.println("x after division: " + x);

  }
}
