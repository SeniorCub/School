package csc202.primenumber;

import java.util.Scanner;
import java.util.logging.Logger;

public class PrimeChecker {
    private static final Logger LOGGER = Logger.getLogger(PrimeChecker.class.getName());

    private PrimeChecker() {
    }

    public static void main(String[] args) {
        int number;
        if (args.length > 0) {
            number = Integer.parseInt(args[0]);
        } else {
            try (Scanner scanner = new Scanner(System.in)) {
                LOGGER.info("Enter a number: ");
                number = scanner.nextInt();
            }
        }

        if (isPrime(number)) {
            LOGGER.info(number + " is a prime number.");
        } else {
            LOGGER.info(number + " is not a prime number.");
        }
    }

    public static boolean isPrime(int number) {
        if (number <= 1) {
            return false;
        }

        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) {
                return false;
            }
        }

        return true;
    }
}