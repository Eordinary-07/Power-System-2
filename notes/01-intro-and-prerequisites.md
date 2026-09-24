# Power Systems-II — Notes for a First-Time Reader

> *A complete first-pass introduction for someone who has never studied power systems analysis at this level.*
>
> Primary source: D.P. Kothari & I.J. Nagrath, *Modern Power System Analysis*, 3rd ed. (Tata McGraw-Hill, 2003) — abbreviated **K&N** in citations.
> Supporting source: A.R. Bergen & V. Vittal, *Power Systems Analysis*, 2nd ed. (Prentice Hall, 2000) — abbreviated **B&V**.
> Syllabus reference: Rashtrasant Tukadoji Maharaj Nagpur University, B.Tech. (Electrical Engg.), Sem-V, Course BEL5T15 "Power Systems-II" (see syllabus PDF in repo, pp. 101–102).

---

## 0.1 Why this subject exists — a one-paragraph tour

🟡 **Pay attention.**

Imagine being responsible for an entire country's electric grid. Every moment of every day, thousands of generators (at coal plants, hydro dams, gas turbines, nuclear reactors, wind farms, solar plants) must together feed hundreds of millions of loads (lights, factories, trains, phone chargers, air conditioners) through hundreds of thousands of kilometers of wire.

This grid has to keep working through five simultaneous challenges:

1. **Balanced, normal operation is a special case.** In normal "happy" conditions, all three phases carry equal-magnitude sine waves offset by exactly 120°. But the instant a tree falls on a line, lightning strikes, or one phase opens, the three phases are no longer balanced — and your entire bag of single-phase AC circuit tricks stops working directly. **Unit I** gives you the mathematical tool — *symmetrical components* — that converts messy unbalanced problems back into three easy balanced problems.
2. **Faults (short circuits) create enormous currents.** A fault on a transmission line can dump thousands of amperes through equipment built to carry hundreds. Circuit breakers must be sized to interrupt that current without exploding. **Unit II** teaches you to compute those currents for every type of fault: three-phase, line-ground, line-line, double-line-ground, and open-conductor.
3. **Generators must stay in sync.** A synchronous generator is physically a rotating electromagnet. If, after a fault, one generator speeds up or slows down even a little bit relative to the others, they "slip a pole" and the grid tears itself apart — blackouts. **Unit III** (stability) tells you whether the machines will stay synchronized, and how big a disturbance they can survive.
4. **It must run cheaply.** Fuel is money. With many generators able to supply the load, which combination produces the required power at the lowest total fuel bill, accounting for energy lost as heat in the wires? **Unit IV** (economic dispatch) answers this.
5. **Frequency and voltage must stay near their targets.** If total generation drops below total load, frequency falls; if it exceeds load, frequency rises. Similarly, voltage at every bus must stay near rated. **Unit V** (control) explains the automatic feedback loops (governor droop, AGC, excitation/AVR) that keep frequency and voltage on target.

These five topics are the heart of the course. Each one solves a concrete problem that shows up every day in real power-system operation.

---

## 0.2 The subject map — how the five units connect

The diagram below is your mental skeleton; refer back to it whenever you feel lost.

```
     UNIT I: Symmetrical Components (the mathematical tool)
               │
               ▼
     UNIT II: Fault Analysis (what goes wrong — and how big?)
               │
               ▼
     UNIT III: Stability (after the fault, do we survive?)
               │
               ├───► UNIT IV: Economic Operation (while running steady, who generates?)
               └───► UNIT V: Load-Frequency & Voltage Control
                            (how do we hold frequency and voltage steady?)
```

Units I→II→III must be read in order (each depends on the previous). Units IV and V depend on I, but only lightly on II and III, so they can be read in either order once Unit I is done.

---

## 0.3 Prerequisites — stated honestly 🟡

I will not pretend you know things you don't. Here is what I am assuming you have seen *before* opening these notes:

1. **DC circuit theory** — Ohm's law (V = IR), KCL (sum of currents at a node = 0), KVL (sum of voltages around a loop = 0), series/parallel resistors.
2. **AC circuit theory** — Inductors and capacitors as jωL and 1/(jωC), phasors (rotating vectors), complex impedance Z = R + jX, complex power S = P + jQ = V I*, power factor.
3. **Three-phase circuits** — Balanced Y (wye) and Δ (delta) connections, the √3 factor between line and phase quantities in Y, per-phase analysis of balanced systems, why we can "drop a wire" and just analyze one phase when everything is balanced.
4. **Transformers** — Turns ratio, impedance reflection, standard three-phase connections (Y-Y, Y-Δ, Δ-Y, Δ-Δ), the idea of a neutral, what "grounding" means.
5. **Synchronous machines** (from Electric Machines / Power Systems-I) — A synchronous generator produces AC via a rotating DC field on the rotor; the simple steady-state model is a voltage source E behind a synchronous reactance X<sub>d</sub>. You should have heard of subtransient (X″<sub>d</sub>), transient (X′<sub>d</sub>), and synchronous (X<sub>d</sub>) reactances, even if you don't remember the exact definitions — I will re-explain them in Unit II.
6. **The per-unit system** — Impedances, voltages, currents, and powers can all be expressed as dimensionless ratios ("per unit") relative to chosen voltage and power bases. This makes calculations across transformers vastly simpler. I will give a *one-page refresher* below, not a full treatment.

### 0.3.1 One-page prerequisites I am NOT going to re-teach

If any of the following phrases are completely unfamiliar, you should set these notes aside for an hour or two and review them from your circuits/machines textbook before continuing. I will use them without apology:

- *j* as the imaginary unit: j² = −1, multiplying by j rotates a phasor 90° counterclockwise.
- A phasor is a complex number representing a sinusoidal quantity at a known frequency; e.g. 10∠30° V means a sine wave of amplitude (or RMS) 10 that reaches its peak 30° (in time) after the reference.
- **Complex power** delivered to a load: S = P + jQ, where P is real power (watts, does work) and Q is reactive power (VAR, sloshes back and forth between inductors/capacitors and sources).
- In an inductive load, current lags voltage (Q > 0); in a capacitive load, current leads voltage (Q < 0).
- In a **balanced** three-phase system, V<sub>a</sub> + V<sub>b</sub> + V<sub>c</sub> = 0 and I<sub>a</sub> + I<sub>b</sub> + I<sub>c</sub> = 0.

### 0.3.2 Per-unit refresher (taught inline because everyone forgets) 🟡

Engineers in a power system hate carrying around volts, ohms, and amperes that change every time you cross a transformer. Instead we normalize everything to a chosen **base**:

- Pick a **base power** S<sub>base</sub> (commonly 100 MVA for whole-system studies).
- Pick a **base voltage** V<sub>base</sub> at one voltage level (e.g. 220 kV for the transmission side).
- Base current and base impedance are *derived*:
  - I<sub>base</sub> = S<sub>base</sub> / (√3 V<sub>base</sub>) for three-phase (line) values
  - Z<sub>base</sub> = V<sub>base</sub>² / S<sub>base</sub> (in per-phase ohms)

Then any actual quantity divided by its base is its **per-unit (pu) value**:
```
V_pu  = V_actual / V_base
I_pu  = I_actual / I_base
Z_pu  = Z_actual / Z_base
S_pu  = S_actual / S_base
```

The beautiful fact: when everything is in per-unit on consistent bases, transformers disappear from the circuit — they become 1:1 ideal transformers — and Ohm's law (V = IZ) and S = VI* hold without any √3 factors. This is why all fault and stability calculations in this course are done in per-unit.

> 🟡 *Why this matters:* If a worked example later gives "X = j0.2 pu" on 100 MVA, 220 kV base, it means "the reactance is 0.2 × Z<sub>base</sub>", where Z<sub>base</sub> = (220 kV)²/100 MVA = 484 Ω, so X = 96.8 Ω. But we rarely need that actual ohm value — we just do all the arithmetic in pu and convert only at the very end.

---

## 0.4 How to read these notes 🔵 / 🟡 / 🔴

Every paragraph in these notes carries a colored dot:

- 🔵 **Routine** — book-keeping, arithmetic, or algebra you can skim once you've understood the idea. Don't get stuck here.
- 🟡 **Pay attention** — a new idea is being introduced. This is where the concepts live.
- 🔴 **Slow down** — conceptually hard; expect to read twice, draw the diagram yourself, and do the self-check before moving on.

You'll also see these signposts throughout:

- **❓ Understanding checkpoint.** A short question you can answer in your head right now, with the answer hidden in the next line. Cover the answer, think, then check.
- **⚠️ Common misconception.** A mistake beginners predictably make.
- **📖 Source citation.** K&N §10.2 = section 10.2 of Kothari & Nagrath; K&N p. 370 = printed page 370 of the book (PDF page 193 in the scanned copy).

---

## 0.5 Added convention I'll use 🔵

Because these notes are for a zero-background reader, I will **re-define every symbol the first time it appears in each unit**, even if it appeared in an earlier unit. Twenty pages from now you will not remember what "X<sub>m</sub>" stood for in Unit I, and you shouldn't have to flip back.

Let us begin.
