# Solución de Ecuaciones Diferenciales Ordinarias (ODEs)

Este proyecto resuelve ecuaciones diferenciales ordinarias (ODEs) utilizando diferentes métodos numéricos. Los métodos implementados incluyen:

- Euler Estándar
- Euler Modificado
- Runge-Kutta de 1er, 2do y 4to orden

## Descripción

El software permite al usuario ingresar una ecuación diferencial en términos de \( x \) y \( y \) separados por un asterisco (\*), junto con valores iniciales y el tamaño del paso para obtener una solución numérica. Este proyecto está orientado a proporcionar soluciones aproximadas de ODEs en intervalos específicos utilizando varios métodos numéricos.

## Métodos de Resolución

- **Euler Estándar**: Método básico para resolver ODEs, adecuado para problemas sencillos, pero con limitaciones en precisión.
- **Euler Modificado**: Mejora del método de Euler Estándar, con una mayor precisión.
- **Runge-Kutta**:
  - **1er Orden**: Método simple de Runge-Kutta para una aproximación más precisa que Euler.
  - **2do Orden**: Método de Runge-Kutta de segundo orden que mejora aún más la precisión.
  - **4to Orden**: Método de Runge-Kutta de cuarto orden, altamente preciso y recomendado para problemas más complejos.

## Requisitos

- Lenguaje de programación utilizado: [indicar el lenguaje, por ejemplo, Python]
- Librerías:
  - [Nombre de las librerías necesarias, por ejemplo, `numpy`, `matplotlib`]

### Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu-usuario/solucion-ode.git
    ```

3. **Ejecutar la aplicación**:
    Si es una aplicación de escritorio, ejecuta el archivo principal:
    ```bash
    python semestralMn.py
    ```


Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
