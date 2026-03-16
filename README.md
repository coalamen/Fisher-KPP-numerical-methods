# Fisher-KPP Equation: Numerical Study

This project was developed as part of the Scientific Computing course in **L3 Magistère Mathématiques** at the **University of Strasbourg** (2025-2026).

## 📌 Project Overview
The goal of this study is the numerical analysis and simulation of the **Fisher-KPP equation**:
$$\partial_{t}u - \partial_{x}^{2}u = u(1-u).$$

This reaction-diffusion equation models population dynamics, specifically the spread of a beneficial allele within a population, resulting in traveling wave solutions moving at speed $c=2$.

## ⚙️ Numerical Methods
We implemented and compared two Finite Difference methods:
1. **Explicit Scheme**: First-order in time and second-order in space. It is computationally fast but subject to the stability condition: $\frac{\Delta t}{\Delta x^2} \le \frac{1}{2+{\Delta x}^2}$.
2. **Semi-Implicit (Crank-Nicolson)**: Unconditionally stable. While the semi-implicit scheme allows for larger time steps, the practical computation time increases significantly as the number of spatial points grows due to the matrix inversion process.

## 📂 Repository Structure
* `src/`
    * `schemes_and_plots.py`: Core implementation of the numerical schemes (Explicit and Semi-Implicit) and generation of comparative graphs.
    * `anim_implicit.py`: Animation of the solution using the implicit scheme.
    * `anim_semi_implicit.py`: Animation of the solution using the **Crank-Nicolson** (semi-implicit) scheme.
* `docs/`
    * `Projet_Fisher_KPP.pdf`: Full technical report (French).
    * `presentation_Fisher_KPP.pdf`: Oral presentation slides (French).

## 👥 Co-autors
* **Luka Beklemishev** - [coalamen](https://github.com/coalamen)
* **Julien Gross** - [jgrossmp](https://github.com/jgrossmp)
