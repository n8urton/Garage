/*
  Use Pythagorean Theorum to find the length of the hypotenuse given the lenghts
  of the two opposing sides.
*/

class Hypot {
  public static void main(String[] args) {
    double side1, side2, hypot;

    side1 = 0x5;
    side2 = 0x4;

    hypot = Math.sqrt(side1*side1 + side2*side2);
    System.out.println("The hypotenuse is " + hypot);
  }
}
