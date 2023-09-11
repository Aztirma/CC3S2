# Replicación JUnit5 Tutorial

A continuación, se llevará a cabo la replicación de un tutorial sobre JUnit, en el cual se presentarán los conceptos básicos de JUnit 5 y sus nuevas funcionalidades. Para este propósito, se utilizará el entorno de desarrollo integrado (IDE) IntelliJ IDEA

En esta actividad, se creó un proyecto denominado 'JUnit' y se configuró el archivo 'pom.xml' al agregar una dependencia para utilizar JUnit 5

**Anotaciones JUnit** 

Se creó una clase llamada `JUnit5Sample1Test` en la cual se utilizan las anotaciones de JUnit5 para implementar las pruebas. 

A continuación, se proporciona el resultado de la ejecución de las pruebas en esta clase además de una explicación detallada de la misma.

 ![Untitled.png](Imagenes%2FUntitled.png)

**Ejecución de Pruebas en la Clase JUnit5Sample1Test**

1. Configuración Inicial
    - **`@BeforeAll`**: Este método, marcado con la anotación **`@BeforeAll`**, se ejecuta una vez antes de todas las pruebas en la clase. En el ejemplo proporcionado, se utiliza para establecer un contexto común antes de ejecutar las pruebas.
    - **`@BeforeEach`**: El método **`beforeEach()`**, marcado con la anotación **`@BeforeEach`**, se ejecuta antes de cada prueba en la clase.
2. **Eje**cución de Pruebas
    - **`@Test`**: Los métodos marcados con la anotación **`@Test`** representan las pruebas reales. En este ejemplo, se tienen tres pruebas: **`testMethod1()`**, **`testMethod2()`**, y **`testMethod3()`**.
    - **`@DisplayName`**: La anotación **`@DisplayName`** se utiliza para proporcionar un nombre personalizado a una prueba. Esto facilita la identificación de la prueba en los informes.
    - **`@Disabled`**: La anotación **`@Disabled`** se usa para deshabilitar una prueba. En este caso, **`testMethod3()`** está deshabilitada y se muestra un mensaje indicando que la implementación está pendiente.
3. Limpieza después de las Pruebas
    - **`@AfterEach`**: El método **`afterEach()`**, marcado con la anotación **`@AfterEach`**, se ejecuta después de cada prueba en la clase.
    - **`@AfterAll`**: El método **`afterAll()`**, marcado con la anotación **`@AfterAll`**, se ejecuta una vez después de ejecutar todas las pruebas en la clase.
4. Resultado de Ejecución
    
    La ejecución de las pruebas se refleja en la salida, que muestra la secuencia en la que se ejecutan los métodos de configuración, las pruebas reales y los métodos de limpieza. La prueba **`testMethod3()`** está deshabilitada debido a la anotación **`@Disabled`**.
    

**Aserciones de JUnit5**

Se creó una clase llamada `JUnit5Sample2Test` en la cual se utilizan las aserciones de JUnit5 para implementar las pruebas. 

A continuación, se proporciona la explicación de cada método de esta clase junto con sus salidas correspondientes 

Método `testAssertEqual()`

Este método es una prueba unitaria que utiliza el método **`assertEquals()`** de JUnit5 para verificar afirmaciones. La prueba verifica lo siguiente:

1. Caso 1: Comprueba si las cadenas "ABC" y "ABC" son iguales.
2. Caso 2: Comprueba si los números enteros 20 y 20 son iguales, con un mensaje de aserción opcional.
3. Caso 3: Comprueba la expresión **`2 + 2`** es igual a 4.

Si todas estas afirmaciones son verdaderas, la prueba se considera exitosa y se obtiene la siguiente salida para este método
![Untitled 1.png](Imagenes%2FUntitled%201.png)
De no ser ser así, se obtiene la siguiente salida para cada caso

Caso 1:

Al no ser las cadenas “ABC” y “ABD” iguales, la prueba falla.
![Untitled 2.png](Imagenes%2FUntitled%202.png)
Caso 2:

Al comparar “20” y “21” y no ser los números iguales, la prueba falla
![Untitled 3.png](Imagenes%2FUntitled%203.png)
Caso 3:

Al no ser “2+2” igual a “5”, la prueba falla.
 ![Untitled 4.png](Imagenes%2FUntitled%204.png)
Método `testAssertFalse()`

Este método es una prueba unitaria que emplea el método `assertFalse()` de JUnit5 para verificar afirmaciones negativas. La prueba evalúa lo siguiente:

1. Caso 1: Comprueba si la longitud de la cadena "FirstName" no es igual a 10 (es decir, verifica que la longitud no sea 10).
2. Caso 2: Comprueba 10 es mayor que 20, con un mensaje de aserción opcional.

Si ambas afirmaciones son falsas, la prueba se considera exitosa y se obtiene la siguiente salida para este método
![Untitled 5.png](Imagenes%2FUntitled%205.png)
De no ser así, es decir las afirmaciones son verdaderas, se obtiene la siguiente salida para cada caso

Caso 1: 

Para este caso, se modifico la longitud de la cadena para que sea la correcta, es decir, 9. Por tanto la prueba falla.
![Untitled 6.png](Imagenes%2FUntitled%206.png)

Caso 2:

Para este caso, se coloco que 30 > 20, lo cual es correcto. Por tanto, la prueba falla.

![Untitled 7.png](Imagenes%2FUntitled%207.png)

Método `testAssertNull()`

Este método es una prueba unitaria que emplea las aserciones `assertNull()` y `assertNotNull()` de JUnit 5 para verificar la nulidad de objetos. La prueba verifica lo siguiente:

1. Caso 1: Comprueba si la cadena `str1` es nula (`null`) utilizando `assertNull()`. Esta aserción pasa si `str1` es nulo.
2. Caso 2: Comprueba si la cadena `str2` no es nula (`null`) utilizando `assertNotNull()`. Esta aserción pasa si `str2` no es nulo.

Si ambas aserciones son exitosas, la prueba se considera exitosa y se obtiene la siguiente salida para este método

![Untitled 8.png](Imagenes%2FUntitled%208.png)

De no ser así, es decir las afirmaciones son verdaderas, se obtiene la siguiente salida para cada caso

Caso 1:

Se modifico`str1` para que sea no nula (`null`), por tanto la prueba no pasa. 

![Untitled 9.png](Imagenes%2FUntitled%209.png)

Caso 2:

Se modifico `str2` para que sea nula (`null`), por tanto la prueba no pasa.

![Untitled 10.png](Imagenes%2FUntitled%2010.png)

**Método `testAssertAll()`**

Este método es una prueba unitaria que utiliza la aserción **`assertAll()`** de JUnit 5 para agrupar múltiples aserciones relacionadas bajo una misma categoría o contexto. La prueba verifica lo siguiente:

Si las cadenas **`str1`**, **`str2`**, y **`str3`** son iguales a "abc", "pqr", y "xyz" respectivamente, utilizando **`assertEquals()`**.

Si las aserciones dentro de **`assertAll()`** son correctas, la prueba se considera exitosa y se obtiene la siguiente salida para este método

![Untitled 11.png](Imagenes%2FUntitled%2011.png)
                
Si alguna aserción dentro de **`assertAll()`** falla, se mostrarán todas las aserciones que fallaron

![Untitled 12.png](Imagenes%2FUntitled%2012.png)

- Método `testAssertTrue()`
    
    Este método es una prueba unitaria que emplea la aserción `assertTrue()` de JUnit 5 para verificar afirmaciones positivas. La prueba evalúa lo siguiente:
    
    1. Caso 1: Comprueba si la cadena "FirstName" comienza con la letra "F" utilizando `assertTrue()`. Esta aserción pasa si la condición es verdadera, es decir, si la cadena comienza con "F".
    2. Caso 2: Comprueba si 10 es menor que 20, con un mensaje de aserción opcional utilizando `assertTrue()`. Esta aserción pasa si la condición es verdadera, es decir, si 10 es menor que 20.
    
    Si ambas aserciones son verdaderas, la prueba se considera exitosa y se obtiene la siguiente salida para este método
    
    ![Untitled 13.png](Imagenes%2FUntitled%2013.png)
  
    De no ser así, es decir las afirmaciones son falsas, se obtiene la siguiente salida para cada caso
    
    Caso 1:
    
    Para este caso, cambiamos la cadena por “LastName”, como esta comienza con “L” y no con “F” como se esta comparando, la aserción es falsa, por tanto la prueba falla. 
    
    ![Untitled 14.png](Imagenes%2FUntitled%2014.png)
    
    Caso 2:
    
    Para este caso comprobamos si 30<20, como esta aserción es falsa, la prueba falla 
    
    ![Untitled 15.png](Imagenes%2FUntitled%2015.png)
    
    Método `testAssertThrows()`
    
    Este método es una prueba unitaria que utiliza la aserción `assertThrows()` de JUnit 5 para verificar que se lanza una excepción de un tipo específico durante la ejecución de un bloque de código. La prueba realiza lo siguiente:
    
    1. Utiliza `assertThrows(IllegalArgumentException.class, () -> { ... })` para verificar que se lanza una excepción del tipo `IllegalArgumentException` durante la ejecución del bloque de código proporcionado.
    2. Verifica si el mensaje de la excepción lanzada es igual a "Illegal Argument Exception occured" utilizando `assertEquals()`.
    
    Si el mensaje de la excepción se lanza y coincide con el esperado, la prueba será exitosa
    
    ![Untitled 16.png](Imagenes%2FUntitled%2016.png)

    De no ser así, la prueba fallará.

    ![Untitled 17.png](Imagenes%2FUntitled%2017.png)
     

**Supuestos de JUnit5**

Se creó una clase llamada `JUnit5Sample3Test` en la cual se utilizan las aserciones de JUnit5 para implementar las pruebas. A continuación, se proporciona la explicación de cada método de esta clase junto con sus salidas correspondientes 

- **Método `testAssumeTrue()`**
    
    Este método es una prueba unitaria que utiliza **`assumeTrue()`** para condicionar la ejecución de la prueba en función de una afirmación booleana. La prueba realiza lo siguiente:
    
    1. Evalúa una condición booleana, en este caso, **`boolean b = 'A' == 'A';`**. 
    2. Utiliza **`assumeTrue(b)`** para condicionar la ejecución de la prueba en función del valor de **`b`**. 
    3. Luego, verifica si "Hello" es igual a "Hello" utilizando **`assertEquals()`**. Esta aserción es independiente de la afirmación anterior y siempre se ejecutará si la afirmación **`b`** es verdadera.
    
    Al ser la condición booleana verdadera, al ser **`b`**, la prueba continúa.
    
    ![Untitled 18.png](Imagenes%2FUntitled%2018.png)
     
    De lo contrario, se considera exitosa sin ejecutar ninguna afirmación adicional, como este caso que se definió  **`boolean b = 'A' == 'B';`**
   
    ![Untitled 19.png](Imagenes%2FUntitled%2019.png)
     
    Sin embargo, si modificamos la aserción **`assertEquals("Hello", "Bye")`** en nuestra prueba, esta fallará.
    
    ![Untitled 20.png](Imagenes%2FUntitled%2020.png)

    Método `testAssumeTrueSaturday()`
    
    Este método es una prueba unitaria que utiliza la aserción **`assumeTrue()`** de JUnit5 para condicionar la ejecución de la prueba en función del día de la semana actual. La prueba realiza lo siguiente:
    
    1. Obtiene la fecha y hora actual utilizando `LocalDateTime dt = LocalDateTime.now();`.
    2. Verifica si el día de la semana actual es sábado, utilizando `dt.getDayOfWeek().getValue() == 6`, donde el valor 6 representa el sábado en la clase `DayOfWeek`.
    3. Utiliza `assumeTrue(...)` para condicionar la ejecución de la prueba en función de si el día de la semana actual es sábado. 
    4. Imprime un mensaje indicando que el código subsiguiente se ejecutará solo si la suposición anterior es verdadera. 
    
    Si la suposición es verdadera (es sábado), la prueba continuará; de lo contrario, se considerará exitosa sin ejecutar ninguna afirmación adicional.
    
    Como se observa en la siguiente imagen, la prueba no continuo debido a que no es Sábado.
    
    ![Untitled 21.png](Imagenes%2FUntitled%2021.png)
- 
    Sin embargo, si modificamos el “6” por el “7”, la prueba continuará, ya que el día actual es Domingo.
    
    ![Untitled 22.png](Imagenes%2FUntitled%2022.png)

Método `testAssumeFalse()`

Este método es una prueba unitaria que emplea la aserción `assumeFalse()` de JUnit5 para condicionar la ejecución de la prueba en función de una suposición negativa. La prueba realiza lo siguiente:

1. Evalúa una condición booleana, en este caso, `boolean b = 'A' != 'A';`. 
2. Utiliza `assumeFalse(b)` para condicionar la ejecución de la prueba en función del valor de `b`. 
3. Verifica si "Hello" es igual a "Hello" utilizando `assertEquals()`. Esta afirmación se ejecutará solo si la suposición (`assumeFalse()`) es falsa.

Al ser la condición booleana falsa, al ser **`b`**, la prueba continúa.

![Untitled 23.png](Imagenes%2FUntitled%2023.png)

De lo contrario, se considera exitosa sin ejecutar ninguna afirmación adicional, como este caso que se definió  **`boolean b = 'B' != 'A';`**

![Untitled 24.png](Imagenes%2FUntitled%2024.png)

Método `testAssumeFalseEnvProp()`

Este método es una prueba unitaria que emplea la aserción `assumeFalse()` de JUnit5 para condicionar la ejecución de la prueba en función de una propiedad del sistema. La prueba realiza lo siguiente:

1. Establece la propiedad del sistema "env" en "prod" utilizando `System.setProperty("env", "prod");`. Esto simula una configuración de entorno de producción.
2. Utiliza `assumeFalse("dev".equals(System.getProperty("env")))` para condicionar la ejecución de la prueba en función del valor de la propiedad del sistema "env".
3. Imprime un mensaje indicando que el código subsiguiente se ejecutará solo si la suposición anterior es falsa.

La prueba continuará solo si la suposición es falsa, es decir, si "env" no es igual a "dev". 

![Untitled 25.png](Imagenes%2FUntitled%2025.png)

Si la suposición es verdadera, la prueba se considerará exitosa sin realizar más acciones.

![Untitled 26.png](Imagenes%2FUntitled%2026.png)

Método `testAssumingThat()`

Este método es una prueba unitaria que utiliza `assumingThat()` de JUnit 5para condicionar la ejecución de aserciones en función de una condición específica. La prueba sigue estos pasos:

1. Establece la propiedad del sistema "env" en "test" utilizando `System.setProperty("env", "test");`. Esto simula una configuración de entorno de prueba.
2. Utiliza `assumingThat("test".equals(System.getProperty("env")), () -> { ... })` para condicionar la ejecución de un bloque de aserciones al resultado de la condición dada. 
3. Dentro del bloque condicional, se realizan las aserciones, como `assertEquals(10, 10);`.
4. A continuación, se ejecutan aserciones fuera del bloque condicional, como `assertEquals(20, 20);`. 

Las aserciones dentro del bloque condicional se ejecutan solo cuando el entorno es de prueba ("test"), mientras que las aserciones fuera del bloque se ejecutan en cualquier entorno. 

![Untitled 27.png](Imagenes%2FUntitled%2027.png)

La prueba falla al cambiar la condición dentro de **`assumingThat`,** para que no se cumpla en el entorno actual .

También la prueba falla si la condición de **`assertEquals`,** como se muestra a continuación 

![Untitled 28.png](Imagenes%2FUntitled%2028.png)

**Clases de prueba anidadas JUnit**

Clase de Prueba Anidada InnerClass

Esta clase de prueba anidada utiliza las anotaciones `@BeforeEach` y `@AfterEach` propias para configurar y limpiar el entorno específico de esta clase de prueba anidada.

Método `testMethod1()`: Este es un método de prueba que pertenece a la clase anidada `InnerClass`. Se ejecuta como una prueba independiente y realiza alguna lógica de prueba específica.

![Untitled 29.png](Imagenes%2FUntitled%2029.png)

Clase de Prueba Anidada InnerMostClass

Esta es otra clase de prueba anidada dentro de `InnerClass`. También utiliza las anotaciones `@BeforeEach` y `@AfterEach` propias para configurar y limpiar su entorno específico.

Método `testMethod2()`: Este es un método de prueba que pertenece a la clase anidada `InnerMostClass`. Al igual que `testMethod1()`, se ejecuta como una prueba independiente y realiza su propia lógica de prueba

![Untitled 30.png](Imagenes%2FUntitled%2030.png)