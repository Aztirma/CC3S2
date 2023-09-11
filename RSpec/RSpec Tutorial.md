# RSpec Tutorial

Status: Not started

## **Conceptos básicos de RSpec**

Este tutorial de RSpec se basará en la implementación de una parte de una *calculadora de cadenas* . El plan es:

- Crea una calculadora de cadenas simple con un método`int Add(string numbers)`
- El método puede tomar 0, 1 o 2 números y devolverá su suma. Para una cadena vacía devolverá 0. Por ejemplo, la entrada puede ser "" o "1" o "1,2".
- Permita que el `Add`
    
    método maneje una cantidad desconocida de números.
    

## **Configurando RSpec**

Comencemos un nuevo proyecto Ruby donde configuraremos RSpec como una dependencia a través de [Bundler](https://bundler.io/) .

Creamos un nuevo directorio y colocamos el siguiente código en nuestro Gemfile:

```
# Gemfile
source "https://rubygems.org"

gem "rspec"
```

A través del terminal de VScode se creó el directorio

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled.png)

Además que se colocó en el Gemfile lo indicado anteriormente 

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%201.png)

Abrimos el directorio del proyecto en el terminal y escribimos `bundle install --path .bundle`para instalar la última versión de RSpec y todas las dependencias relacionadas. 

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%202.png)

## **Escribiendo la primera especificación**

Por convención, las pruebas escritas con RSpec se denominan "especificaciones" (abreviatura de "especificaciones") y se almacenan en el `spec`directorio del proyecto. 

Se creo este directorio en nuestro proyecto → `mkdir spec` 

Comencemos a escribir nuestra primera especificación de la calculadora de cadenas

```markdown
# Gemfile
source "https://rubygems.org"

gem "rspec"
```

Para ejecutar las especificaciones, se escribio: 

```markdown
$ bundle exec rspec
```

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%203.png)

La especificación fallo con el `uninitialized constant StringCalculator`error. Eso es de esperarse, ya que aún no hemos creado esa clase.

---

Creamos un nuevo directorio llamado`lib`

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%204.png)

Declaramos `StringCalculator`en `string_calculator.rb`:

```markdown
# lib/string_calculator.rb
class StringCalculator
end
```

Y solicitamos en nuestra especificación:

```markdown
# spec/string_calculator_spec.rb
require "string_calculator"

describe StringCalculator do
end
```

Una vez realizado esto, ahora nuestra prueba pasará.

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%205.png)

Lo que hemos logrado aquí es que hemos establecido una configuración de trabajo de nuestro proyecto.

Lo más sencillo que puede hacer nuestra calculadora de cadenas es aceptar una cadena vacía, en cuyo caso podríamos decidir que queremos que devuelva un cero. El método que debemos describir primero es `add`.

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%206.png)

Si ejecutamos nuestra especificación ahora, obtendremos un error de que el método no está definido

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%207.png)

Escribamos la cantidad mínima de código para que se cumpla esa especificación, si ejecutamos `bundle exec rspec`ahora, la especificación pasa.

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%208.png)

## Hacia un código de trabajo

Nuestra siguiente tarea es hacer que la calculadora funcione dado un solo número en una cadena. 

```markdown
# spec/string_calculator_spec.rb
describe StringCalculator do

  describe ".add" do
    context "given '4'" do
      it "returns 4" do
        expect(StringCalculator.add("4")).to eql(4)
      end
    end

    context "given '10'" do
      it "returns 10" do
        expect(StringCalculator.add("10")).to eql(10)
      end
    end
  end
end
```

Modificamos las especificaciones, para probar nuevos ejemplos de RSpec.

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%209.png)

Después de haber ejecutado las especificaciones, se obtendrá lo siguiente 

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%2010.png)

De nuevo, nuestro objetivo es hacerlos pasar, implementando lo siguiente 

```markdown
# lib/string_calculator.rb
class StringCalculator

  def self.add(input)
    if input.empty?
      0
    else
      input.to_i
    end
  end
end
```

De esto modo, nuestra prueba pasará 

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%2011.png)

Ahora escribamos algunos ejemplos basados en cadenas que contienen números separados por comas. Podría tener sentido introducir un contexto anidado, "dos números":

```markdown
# spec/string_calculator_spec.rb
describe StringCalculator do

  describe ".add" do
    context "two numbers" do
      context "given '2,4'" do
        it "returns 6" do
          expect(StringCalculator.add("2,4")).to eql(6)
        end
      end

      context "given '17,100'" do
        it "returns 117" do
          expect(StringCalculator.add("17,100")).to eql(117)
        end
      end
    end
  end
end
```

Implementamos en nuestro proyecto 

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%2012.png)

Estas especificaciones fallan, como era de esperar.

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%2013.png)

Aquí hay una forma de hacer que se cumplan las especificaciones

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%2014.png)

RSpec tiene más de una forma de mostrar su salida. Una alternativa muy popular al formato de puntos predeterminado es el formato de "documentación", para el caso anterior, la salida será

![Untitled](RSpec%20Tutorial%205827ddc6b0a848669f37270e11cfa68c/Untitled%2015.png)