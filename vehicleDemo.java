// Vehicle class
class Vehicle {
  int passengers; // # of passengers
  int fuelCap; // fuel capacity in gallons
  int mpg; // fuel consumptionin miles per gallons

// Display the range.
  void range() {
    System.out.println("Range is " + fuelCap * mpg);
  }
}


class vehicleDemo {
  public static void main (String[] args) {
    Vehicle minivan = new Vehicle();
    Vehicle sportscar = new Vehicle();

    int range1, range2;

    // assign values to fields in minvan
    minivan.passengers = 7;
    minivan.fuelCap = 16;
    minivan.mpg = 21;

    // assign values to fields in sportscar
    sportscar.passengers = 2;
    sportscar.fuelCap = 14;
    sportscar.mpg = 12;

    System.out.println("Minivan can carry " + minivan.passengers + ". ");
    minivan.range(); // display range of minivan

    System.out.println("Sportsca can carry " + sportscar.passengers + ". ");
    sportscar.range(); // display range of minivan

  }
}
