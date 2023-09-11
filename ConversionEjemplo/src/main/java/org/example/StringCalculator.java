package org.example;

public class StringCalculator {

    public static int add(String input) {
        if (input.isEmpty()) {
            return 0;
        } else {
            String[] numbers = input.split(",");
            int sum = 0;
            for (String number : numbers) {
                sum += Integer.parseInt(number);
            }
            return sum;
        }
    }

    public static void main(String[] args) {
        System.out.println(add(""));         // Output: 0
        System.out.println(add("4"));        // Output: 4
        System.out.println(add("10"));       // Output: 10
        System.out.println(add("2,4"));      // Output: 6
        System.out.println(add("17,100"));   // Output: 117
    }
}
