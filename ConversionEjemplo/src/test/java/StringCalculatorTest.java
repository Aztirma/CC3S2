import org.example.StringCalculator;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class StringCalculatorTest {

    @Test
    public void testAddEmptyString() {
        assertEquals(0, StringCalculator.add(""));
    }

    @Test
    public void testAddSingleNumber4() {
        assertEquals(4, StringCalculator.add("4"));
    }

    @Test
    public void testAddSingleNumber10() {
        assertEquals(10, StringCalculator.add("10"));
    }

    @Test
    public void testAddTwoNumbers2And4() {
        assertEquals(6, StringCalculator.add("2,4"));
    }

    @Test
    public void testAddTwoNumbers17And100() {
        assertEquals(117, StringCalculator.add("17,100"));
    }
}
