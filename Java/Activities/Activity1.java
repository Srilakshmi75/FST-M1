package Activities;

public class Activity1 {
        public static void main(String[] args) {
            Car maruthi = new Car();
            maruthi.make = 2014;
            maruthi.color = "Black";
            maruthi.transmission = "Manual";

            maruthi.displayCharacteristics();
            maruthi.accelerate();
            maruthi.brake();
        }

    }

