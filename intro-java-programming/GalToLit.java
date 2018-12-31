/*
Try This 1-1

This program converts gallons to liters.

Call this program GaltoLit.java
*/

class GalToLit {
  public static void main(String[] args) {
    double gallons, liters; //varible declaration

    gallons = 10; //start with 10 gallons

    liters = gallons * 3.7854; //convert to liters

    System.out.println(gallons + " gallons is " + liters
      + " liters.");

  }
}
