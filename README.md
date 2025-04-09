# 🧮 BMI Calculator (GUI)

A simple and user-friendly Body Mass Index (BMI) Calculator built using Python with a graphical user interface (GUI). This app allows users to input their height and weight, calculates their BMI instantly, and shows their health category in a clean interface.

---

## 📚 Table of Contents

- [Features](#features)
- [Technologies-Used](#technologies-used)
- [How-to-Run](#how-to-run)
- [BMI-Formula](#bmi-formula)
- [Example](#example)
- [Screenshot](#screenshot)
- [Project-Structure](#project-structure)
- [License](#license)

---

## Features

- Graphical User Interface using **Tkinter**
- Input fields for height and weight
- Calculates BMI using the standard formula
- Displays BMI result with category:
  - Underweight
  - Normal weight
  - Overweight
  - Obesity
- Real-time, easy-to-use interface

---

## Technologies Used

- Python 3
- Tkinter (Python's standard GUI library)

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/sanjana0329/BMI-Calculator.git
   cd bmi-calculator
   ```

2. Run the script:

   ```bash
   python bmi_calculator_gui.py
   ```

   > Make sure you have Python 3 installed.

---

## BMI Formula

The Body Mass Index is calculated using the formula:

```
BMI = weight (kg) / (height (m))²
```

---

## Example

Let’s say you enter:

- **Weight**: 70 kg  
- **Height**: 1.75 m

Then your BMI would be:

```
Your BMI is 22.86
You are in the Normal weight range.
```

---

## Screenshot

![BMI Calculator GUI Screenshot](screenshot.png)

> _Make sure the screenshot image file is named `screenshot.png` and placed in the root of your project directory._

---

## Project Structure

```
bmi-calculator/
│
├── bmi_calculator_gui.py     # Main Python script with GUI logic
├── screenshot.png            # Screenshot of the GUI
├── README.md                 # Project documentation
├── LICENSE                   # License info (e.g., MIT)
```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to contribute, report issues, or suggest improvements!
