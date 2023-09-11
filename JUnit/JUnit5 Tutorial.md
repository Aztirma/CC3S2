# JUnit5 Tutorial

# ****Tutorial JUnit5****

**JUnit**

- JUnit es uno de los marcos populares utilizados para implementar pruebas unitarias en código Java.
- JUnit ayuda principalmente a los desarrolladores a probar ellos mismos su código en la JVM .

**Arquitectura JUnit**

![Untitled 0.png](Imagenes%2FUntitled%200.png)
      JUnit Platform: Lanza marcos de prueba en la JVM.

JUnit Jupiter: Combinación de un nuevo modelo de programación para pruebas de escritura y un modelo de extensión para extensiones.

JUnit Vintage: Proporciona soporte para ejecutar pruebas anteriores de JUnit versión 3 y 4 en esta nueva plataforma.

**Dependencias de JUnit Maven**

Para implementar casos de prueba basados en JUnit5 en un proyecto, agregue la siguiente dependencia al archivo pom.xml del proyecto:

• Biblioteca JUnit 5

```
<dependency>
     <groupId>org.junit.jupiter</groupId>
     <artifactId>junit-jupiter-engine</artifactId>
     <version>5.1.1</version>
     <scope>test</scope>
</dependency>
<dependency>
     <groupId>org.junit.platform</groupId>
     <artifactId>junit-platform-runner</artifactId>
     <version> 1.1.1</version>
     <scope>test</scope>
</dependency>
```

• JUnit5 maven surefire provider para ejecutar las pruebas unitarias donde IDE no tiene soporte JUnit5 (si IDE tiene soporte entonces este punto no es necesario)

```
<plugin>
     <artifactId>maven-surefire-plugin</artifactId>
     <version>2.19.1</version>
     <dependencies>
          <dependency>
               <groupId>org.junit.platform</groupId>
               <artifactId>junit-platform-surefire-provider</artifactId>
               <version>1.0.2</version>
          </dependency>
     </dependencies>
</plugin>
```

**Nuevas características de JUnit5**

Requiere Java 8 o superior en tiempo de ejecución. Pero todavía se puede probar el código que se compila utilizando versiones anteriores de Java. Se han introducido varias características nuevas.

**Anotaciones JUnit**

A continuación se enumeran algunas anotaciones de uso común que se proporcionan en él:

| Annotation   | Description |
|--------------| --- |
| @test        | Denota un método de prueba |
| @displayname | Declara un nombre para mostrar personalizado para la clase de prueba o el método de prueba. |
| @beforeeach  | Indica que el método anotado debe ejecutarse antes de cada método de prueba. |
| @aftereach   | Indica que el método anotado debe ejecutarse después de cada método de prueba. |
| @beforeall   | Indica que el método anotado debe ejecutarse antes que todos los métodos de prueba. |
| @afterall    | Indica que el método anotado debe ejecutarse después de todos los métodos de prueba. |
| @disable     | Se utiliza para deshabilitar una clase de prueba o un método de prueba. |
| @nested       | Denota que la clase anotada es una clase de prueba anidada y no estática. |
| @tag          | Declarar etiquetas para filtrar pruebas. |
| @extendwith   | Registrar extensiones personalizadas. |

```
package com.journaldev;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

public class JUnit5Sample1Test {

  @BeforeAll
  static void beforeAll() {
    System.out.println("**--- Executed once before all test methods in this class ---**");
  }

  @BeforeEach
  void beforeEach() {
    System.out.println("**--- Executed before each test method in this class ---**");
  }

  @Test
  void testMethod1() {
    System.out.println("**--- Test method1 executed ---**");
  }

  @DisplayName("Test method2 with condition")
  @Test
  void testMethod2() {
    System.out.println("**--- Test method2 executed ---**");
  }

  @Test
  @Disabled("implementation pending")
  void testMethod3() {
	  System.out.println("**--- Test method3 executed ---**");
  }

  @AfterEach
  void afterEach() {
    System.out.println("**--- Executed after each test method in this class ---**");
  }

  @AfterAll
  static void afterAll() {
    System.out.println("**--- Executed once after all test methods in this class ---**");
  }

}
```

Podemos ejecutar la clase de prueba JUnit

![Untitled 00.png](Imagenes%2FUntitled%2000.png) 

**Aserciones de JUnit**

Cada método de prueba debe evaluarse contra la condición de verdadero mediante aserciones para que la prueba pueda continuar ejecutándose. Las afirmaciones de JUnit Júpiter se mantienen en la clase org.junit.jupiter.api.Assertions. Todos los métodos son estáticos.

| Assertion | Description |
| --- | --- |
| assertEquals(expected, actual) | Falla cuando lo esperado no es igual a lo real |
| assertFalse(expression) | Falla cuando la expresión no es falsa |
| assertNull(actual) | Falla cuando lo real no es nulo |
| assertNotNull(actual) | Falla cuando lo real es nulo |
| assertAll() | Agrupe muchas aserciones y cada aserción se ejecutará incluso si una o más de ellas falla |
| assertTrue(expression) | Falla si la expresión no es verdadera |
| assertThrows() | Se espera que la clase que se va a probar genere una excepción |

```
@Test
void testAssertEqual() {
	 assertEquals("ABC", "ABC");
	 assertEquals(20, 20, "optional assertion message");
	 assertEquals(2 + 2, 4);
}
@Test
void testAssertFalse() {
	 assertFalse("FirstName".length() == 10);
	 assertFalse(10 > 20, "assertion message");
}
@Test
void testAssertNull() {
     String str1 = null;
	 String str2 = "abc";
	 assertNull(str1);
	 assertNotNull(str2);
}
@Test
void testAssertAll() {
	 String str1 = "abc";
	 String str2 = "pqr";
	 String str3 = "xyz";
	 assertAll("numbers",
	      () -> assertEquals(str1,"abc"),
		  () -> assertEquals(str2,"pqr"),
		  () -> assertEquals(str3,"xyz")
	 );
	 //uncomment below code and understand each assert execution
     /*assertAll("numbers",
		  () -> assertEquals(str1,"abc"),
		  () -> assertEquals(str2,"pqr1"),
		  () -> assertEquals(str3,"xyz1")
	 );*/
}
@Test
void testAssertTrue() {
	 assertTrue("FirstName".startsWith("F"));
	 assertTrue(10  {
	      throw new IllegalArgumentException("Illegal Argument Exception occured");
	 });
	 assertEquals("Illegal Argument Exception occured", exception.getMessage());
}
```

**Importaciones JUnit5**

Sus clases de prueba necesitan `org.junit.jupiter.api.Test`una declaración de importación y no `org.junit.Test`. Además, no es necesario que los métodos de prueba sean un paquete público y local.

`import org.junit.jupiter.api.Test;`

**Suposiciones JUnit5**

Los supuestos son métodos estáticos en la `org.junit.jupiter.api.Assumptions`clase. Ejecutarán una prueba solo cuando se cumpla la condición especificada; de lo contrario, la prueba se cancelará. La prueba abortada no provocará un error de compilación. Cuando una suposición falla, `org.opentest4j.TestAbortedException`se descarta y se omite la prueba.

| Assumptions | Description |
| --- | --- |
| assumeTrue | Ejecutar el cuerpo de lamda cuando se mantenga la condición positiva; de lo contrario, se omitirá la prueba |
| assumeFalse | Ejecutar el cuerpo de la lamda cuando la condición negativa se mantiene, de lo contrario la prueba será omitida. |
| assumingThat | La parte del método de prueba se ejecutará si una suposición es verdadera y todo lo que sigue a la lambda se ejecutará independientemente de si la suposición en assumingThat() es verdadera. |

```
@Test
void testAssumeTrue() {
     boolean b = 'A' == 'A';
     assumeTrue(b);
     assertEquals("Hello", "Hello");
}

@Test
@DisplayName("test executes only on Saturday")
public void testAssumeTrueSaturday() {
     LocalDateTime dt = LocalDateTime.now();
     assumeTrue(dt.getDayOfWeek().getValue() == 6);
     System.out.println("further code will execute only if above assumption holds true");
}

@Test
void testAssumeFalse() {
     boolean b = 'A' != 'A';
     assumeFalse(b);
     assertEquals("Hello", "Hello");
}

@Test
void testAssumeFalseEnvProp() {
     System.setProperty("env", "prod");
     assumeFalse("dev".equals(System.getProperty("env")));
     System.out.println("further code will execute only if above assumption hold");
}

@Test
void testAssumingThat() {
     System.setProperty("env", "test");
     assumingThat("test".equals(System.getProperty("env")),
          () -> {
               assertEquals(10, 10);
               System.out.println("perform below assertions only on the test env");
               });

     assertEquals(20, 20);
     System.out.println("perform below assertions on all env");
}
```

**Clases de prueba anidadas JUnit**

Las pruebas anidadas permiten crear clases anidadas y ejecutar todos sus métodos de prueba. Las clases internas deben ser no estáticas. Simplemente anote las clases internas con @Nested y se ejecutarán todos los métodos de prueba dentro de ellas.

```
@BeforeAll
static void beforeAll() {
     System.out.println("**--- JUnit5Sample4Test :: beforeAll :: Executed once before all test methods ---**");
}

@BeforeEach
void beforeEach() {
	 System.out.println("**--- JUnit5Sample4Test :: beforeEach :: Executed before each test method ---**");
}

@AfterEach
void afterEach() {
	 System.out.println("**--- JUnit5Sample4Test :: afterEach :: Executed after each test method ---**");
}

@AfterAll
static void afterAll() {
	 System.out.println("**--- JUnit5Sample4Test :: afterAll :: Executed after all test method ---**");
}

     @Nested
     class InnerClass {

          @BeforeEach
          void beforeEach() {
               System.out.println("**--- InnerClass :: beforeEach :: Executed before each test method ---**");
          }

          @AfterEach
          void afterEach() {
        	   System.out.println("**--- InnerClass :: afterEach :: Executed after each test method ---**");
          }

          @Test
          void testMethod1() {
        	   System.out.println("**--- InnerClass :: testMethod1 :: Executed test method1 ---**");
          }

          @Nested
          class InnerMostClass {

               @BeforeEach
               void beforeEach() {
                    System.out.println("**--- InnerMostClass :: beforeEach :: Executed before each test method ---**");
               }

               @AfterEach
               void afterEach() {
            	    System.out.println("**--- InnerMostClass :: afterEach :: Executed after each test method ---**");
               }

               @Test
               void testMethod2() {
            	    System.out.println("**--- InnerMostClass :: testMethod2 :: Executed test method2 ---**");
               }
        }
    }
```

**Excepción de prueba JUnit**

Hay situaciones en las que se espera que los métodos lancen una excepción bajo una condición específica. assertThrows fallará la prueba si el método dado no lanza la excepción especificada.

```
Throwable exception = assertThrows(IllegalArgumentException.class, () -> {
     throw new IllegalArgumentException("Illegal Argument Exception occured");
});
assertEquals("Illegal Argument Exception occured", exception.getMessage());
```

**Ejecución de prueba JUnit**

Las pruebas unitarias se pueden ejecutar de muchas formas, dos de las cuales son las siguientes:

- Utilice la versión Eclipse IDE Oxygen.3a (4.7.3a) y abra el archivo de prueba para ejecutarlo. Haga clic derecho en el archivo y elija la opción Ejecutar como seguido de Prueba JUnit
- Utilice el comando mvn test en el símbolo del sistema de Windows

**Resumen**

Hemos explorado JUnit5 y sus nuevas características con algunos ejemplos. También vimos cómo podemos usar anotaciones, afirmaciones, suposiciones, excepciones de JUnit y escribir clases de prueba anidadas.