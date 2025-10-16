# Translation Notes
## B. Translation of Fortran Code

The original Fortran files (`main.f90` and `weather.f90`) were translated into Python using an object-oriented approach.  
In the Fortran version, procedures handled data for temperature, wind, and humidity calculations in a procedural order.  
In the Python version, I organized these routines into a class called `WeatherModel` inside `src/weather.py`.

Key changes:
- Fortran subroutines and modules were mapped to **Python classes and methods**.  
- Arrays and loops were replaced with **NumPy vectorized operations** for better performance and readability (Harris et al., 2020).  
- The main program logic in `main.f90` became `main.py`, which creates a `WeatherModel` object and calls its methods in sequence.  
- Print statements were replaced with formatted `print()`  for clarity.

This translation maintains the same functionality as the Fortran program but uses object-oriented design to make the code easier to maintain and test.

---

## C. Language Choice

I chose **Python** as the target language because of its simplicity, readability, and large ecosystem of scientific libraries.  
Python’s **NumPy** library allows array operations similar to Fortran but with more flexibility (Harris et al., 2020).  
Its syntax is closer to pseudocode, which makes debugging easier and the translated logic easier to verify (Python Software Foundation, 2001–2025).

Other languages considered:
- **Java:** Strong object-oriented support but more for numeric computations.  
- **C#:** Good performance and tooling, but unnecessary complexity for this scientific task.  
- **C++:** High performance but less productive for fast development.

Python provided the best balance between readability, community support, and numerical power (Harris et al., 2020).

---

## D. Translation Method and AI Use

**Method used:**  
I used a **manual, semantics-preserving translation**.  
Each Fortran subroutine was rewritten as a Python class method with equivalent logic.  
I verified correctness by comparing outputs from the Python and Fortran versions using test data.

Steps followed:
1. Rewrote Fortran procedures in Python methods.  
2. Replaced loops and array indexing with NumPy operations.  
3. Created unit tests for each function.  
4. Validated outputs using sample input data.

**AI involvement:**  
AI tools were used only for syntax clarification and debugging suggestions, not for generating final production code.  
All logic, structure, and testing were performed manually. (Python Software Foundation, 2001–2025).

---

