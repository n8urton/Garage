/*
  This program displays a conversion table of gallons to liters
  Call this program "GalToLitTable.java"
*/

class galHex {
  public static void main(String[] args) {
    double gallons, liters;
    int counter = 0;

    for (gallons = 0x1; gallons <= 0x40; gallons++) {
      liters = gallons * 3.7854; // convert to liters
      System.out.println(gallons + " gallons is " + liters + " liters.");

      counter++;
      //every 10th line, print a blank line
      if (counter == 10) {
        System.out.println();
        counter = 0; //reset line counter
      }
    }
  }
}
