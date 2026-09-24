# Unit V — Power System Dynamics: Load-Frequency and Voltage Control

> *Why this unit exists:* A power system is not a static circuit — the load changes minute-to-minute, generators drift, and closed-loop control systems must constantly adjust turbine inputs and field excitation to keep frequency at 50/60 Hz and voltages near rated. This unit describes how turbines, governors, and excitation systems provide that control.
>
> Source: K&N Ch. 8 (book pp. 289–325; PDF pp. 154–171), plus supporting qualitative discussion of reactive power from K&N §6.9 (voltage control discussion, book pp. 230–235).

---

## 5.1 Two separate control problems — a fundamental split 🟡

The first thing to grasp is that **active power and frequency** are controlled by *different* mechanisms than **reactive power and voltage**.

- Active power (watts) is produced by the turbine driving the generator. If total generation of watts does not match total watts consumed (plus losses), the *rotational speed* of all generators changes — i.e., frequency changes. → Control loop: **turbine governor + AGC (Automatic Generation Control)**.
- Reactive power (VARs) is produced or absorbed by the generator's field excitation, shunt capacitors/inductors, SVCs, STATCOMs, and line charging. If reactive supply does not match reactive demand at a bus, that bus's *voltage* drops or rises. → Control loop: **exciter + AVR (Automatic Voltage Regulator)**, plus shunt/series compensation.

> 🟡 *Why are these decoupled?* In high-voltage transmission (where X >> R), the flow of real power P across a line depends primarily on the *angle difference* δ between the two ends, while reactive power Q depends primarily on the *voltage magnitude difference* |V<sub>s</sub>| − |V<sub>r</sub>|. Controlling P controls angles (hence frequency); controlling Q controls magnitudes (hence voltage). This decoupling is why we can design separate controllers. This is the single most important conceptual point in this unit.

> ⚠️ **Common misconception:** "If I increase mechanical power to a generator, its voltage goes up." No — increasing P<sub>m</sub> (more steam to turbine) initially makes the rotor accelerate, increasing δ and delivering more *real* power to the grid; voltage is controlled separately by the DC field current (excitation). If you want to change voltage, change excitation; if you want to change real-power output, change the turbine's steam/gate/water setting.

---

## 5.2 Turbines and speed governors — basic frequency control 🔴 Slow down

### The physical hardware
Every steam/hydro/gas turbine has a **speed governor** that senses shaft speed and adjusts the steam valve (or water gate, or fuel valve) to keep speed constant. The classic mechanical-hydraulic speed-governing system for a steam turbine (K&N Fig. 8.2) has four parts — a flyball speed sensor, a hydraulic amplifier (pilot valve + main piston), a linkage (ABC, CDE), and a speed-changer (the setpoint adjustment):

![Fig. 8.2](figures/fig8_2.png)

**Figure 5.1** — Turbine speed governing system: the flyball governor senses speed and moves point B; the linkage relays that motion to a pilot valve; high-pressure oil drives the main piston to open/close the steam valve; a feedback link from the valve to point D provides the proportional (droop) action; the speed changer at A lets the operator (or AGC) adjust the load setpoint. *(Reproduced from Olle I. Elgerd, Electric Energy Systems Theory: An Introduction, 1971, p. 322, as reprinted in K&N.)* *Source: K&N Fig. 8.2, book p. 291, PDF p. 154.*

How it works in plain words:
1. If the turbine speeds up (frequency rises), the flyballs fly outward and pull point B *down*.
2. That moves the pilot valve down, letting high-pressure oil push the main piston *up*, which **closes** the steam valve a bit.
3. Closing the valve reduces steam flow, which reduces mechanical power, slowing the turbine back down.
4. The linkage from the valve stem back to point D creates mechanical feedback: the valve doesn't keep closing forever — it stops when the linkage recenters the pilot valve. This built-in feedback is what produces **droop** (proportional, not integral, action).
5. The speed changer at A (a motor-driven screw controlled by the operator or AGC) moves the entire setpoint up or down, raising or lowering the power output at a given frequency.

### Generator-load model (𝚫 structure)
We linearize everything around a nominal operating point (small-signal model). Let Δ denote deviation from nominal. The power balance on the rotating mass (same M as in Unit III) is:
```
ΔP_m - ΔP_e = M dΔf/dt + D Δf                                       (5.1)
```
(K&N Eq. 8.11, book p. 299, with equivalent notation.) Here:
- M = inertia constant (same 2H/ω<sub>s</sub> as in Unit III),
- Δf = frequency deviation (pu),
- D = load-damping constant: the natural tendency of loads to draw less power when frequency drops (e.g., motor loads slow down, reducing P). D is typically 1–2% per 1% frequency change.
- ΔP<sub>m</sub> = change in mechanical power from governor action,
- ΔP<sub>e</sub> = change in electrical load (the disturbance).

### Droop control — how generators share load 🟡
A governor cannot hold frequency *exactly* constant in an interconnected system with multiple generators, because then the load split between generators would be indeterminate (multiple ways to match total P). Instead, governors are deliberately given **droop**: as a generator picks up more load, its speed setpoint *drops* slightly.

The steady-state governor characteristic is:
```
ΔP_m = - (1/R) Δf                                                   (5.2)
```
where R is the **droop** (speed regulation) in pu Hz / pu MW, or equivalently in percent. Typical R = 5% (0.05 pu): a 5% drop in frequency (from 50 Hz to 47.5 Hz) causes the unit to go from zero to full output. (K&N §8.2, book p. 297 onward.)

In words: if frequency falls (Δf < 0), ΔP<sub>m</sub> > 0 — the governor opens the valve and the unit picks up more power, opposing the frequency drop.

### Why droop, not perfect isochronous?
If two generators had zero droop (perfect "isochronous" control), they would "fight" — each would try to control frequency to its own setpoint, with unstable results. With 5% droop on both, load is shared automatically in proportion to each unit's rating: if a 100 MW and a 200 MW unit are on the same bus with R = 5% each, a ΔP load increase is split 1:2 between them (smaller unit picks up less, larger picks up more), because each requires the same Δf and R is on its own base. That is how grids operate.

> 🟡 *Everyday analogy:* Think of two springs supporting a board. If both springs have identical stiffness per unit weight, the load splits according to how much they deflect (droop). If one spring had infinite stiffness (zero droop) it would carry all load, and the other would carry nothing — brittle and bad for sharing. Droop = finite stiffness; essential for parallel operation.

### Steady-state frequency after a step load change
Substituting ΔP<sub>m</sub> = −(1/R)Δf into (5.1) at steady state (derivatives zero):
```
- Δf/R - ΔP_e = D Δf   ⇒   Δf = - ΔP_e / (D + 1/R)                   (5.3)
```
Frequency drops (Δf negative) proportionally to the size of the load step, divided by the total "frequency stiffness" (D + 1/R), with 1/R from the governor and D from load damping.

**❓ Understanding checkpoint:** Two parallel units have R = 0.05 (5%) and R = 0.04 (4%). For the same Δf, which picks up more power per unit MW rating?
  - *Answer:* The unit with smaller R (4%) has higher gain (1/R = 25 vs 20), so it picks up more. That's why units meant to carry more frequency-responsive load (spinning reserve) are set to lower droop.

---

## 5.3 Automatic Generation Control (AGC) 🔵 (secondary control)

Droop control (primary control) stabilizes frequency after a disturbance but leaves a *steady-state error* — Δf is nonzero, as Eq. (5.3) shows. To restore frequency to its setpoint (50 or 60 Hz) and to restore scheduled inter-area (tie-line) power flows, a slow outer loop — **AGC** or **secondary control** — slowly adjusts the governor setpoints (raises or lowers the "load reference" on each unit).

AGC implements integral action on the **Area Control Error (ACE)**:
```
ACE = ΔP_tie - B Δf                                                  (5.4)
```
where ΔP<sub>tie</sub> is deviation of tie-line flow from schedule and B is frequency-bias setting (MW/Hz). The AGC integrates ACE and adjusts generation setpoints until ACE = 0, which drives both frequency and tie-line error to zero. (K&N §8.3–§8.4, book pp. 305–310.)

> 🟡 *Time scale:* Primary (droop) response acts in 2–10 seconds; secondary (AGC) acts in 30 seconds to a few minutes; tertiary (economic dispatch from Unit IV) re-optimizes every few minutes to an hour. These are separate time scales, which is why they are designed separately.

---

## 5.4 Reactive power, excitation, and voltage control 🟡

### Where VARs come from — and go
Reactive power is produced or absorbed by nearly every component in the system:
- **Generators** can produce or absorb VARs by adjusting field current. Overexcited ⇒ generator supplies VARs (Q > 0); underexcited ⇒ generator absorbs VARs (Q < 0).
- **Shunt capacitors** supply VARs (fixed or switched); shunt inductors absorb VARs.
- **Transmission lines:** when heavily loaded, series reactance absorbs VARs; when lightly loaded, shunt capacitance supplies VARs (the Ferranti effect causes open-circuit voltage rise).
- **Transformers** absorb VARs due to their series leakage reactance and magnetizing current.
- **Loads** (induction motors especially) absorb VARs.

The balance of VARs near a bus determines that bus's voltage. Unlike watts, VARs cannot be shipped long distances efficiently (VAR flow causes large I²X drops and voltage collapse), so VARs must be managed **locally**. That is why voltage control is a local problem (excitation, capacitor banks, SVCs at substations) while frequency control is system-wide (watts travel freely across the grid, frequency is the same everywhere in steady state).

### Excitation system and AVR 🟡
Each synchronous generator has an **exciter** — a separate DC or AC source supplying DC current to the rotor field winding. Increasing field current increases the internal voltage E, which increases terminal voltage and boosts reactive output. The **Automatic Voltage Regulator (AVR)** senses terminal voltage, compares it to a setpoint, and adjusts the exciter output to close the gap.

The basic AVR loop (K&N §8.6, book pp. 318–320) is a feedback controller with:
- A voltage transducer measuring |V<sub>t</sub>|,
- An error amplifier (setpoint − measurement),
- The exciter (a gain plus time constant),
- The generator field (which turns field voltage into E, which then determines |V<sub>t</sub>| through the synchronous reactance).

Like any feedback loop, the AVR must be tuned to be stable (adequate phase margin). Excitation systems also have limits on maximum field current (overexcitation limit, to protect rotor from overheating) and minimum field current (underexcitation limit, to prevent loss of synchronism).

> 🟡 *Coordination:* AVRs act fast (fractions of a second to seconds) to hold voltage; slower, plant-level or system-level reactive-power optimization adjusts setpoints over minutes.

---

## 5.5 Putting Unit V together 🟡

You can remember the whole unit as two separate control stacks, operating at three time scales each:

**Frequency / Active Power (P-f control):**
1. Inertia (instantaneous): rotors store/release kinetic energy — the "M" term.
2. Primary / droop control (seconds): governors open valves/ gates, restoring power balance at a slightly off-nominal frequency.
3. Secondary / AGC (30 sec to minutes): integral control restores frequency to 50/60 Hz and tie flows to schedule.
4. Tertiary / Economic dispatch (minutes to hour): re-optimizes unit outputs for cost (Unit IV).

**Voltage / Reactive Power (Q-V control):**
1. Inherent voltage sensitivity of loads (instantaneous): D-like effect.
2. Excitation/AVR (fractions of seconds to seconds): adjusts generator field current to hold terminal voltage.
3. Shunt/series compensation switching, SVC/STATCOM action (cycles to seconds): fast power-electronic voltage support.
4. Operator / SCADA dispatch of capacitors and transformer taps (minutes to hours): adjusts to schedule voltages and manage losses.

---

## 5.6 Unit V self-check

1. If frequency drops, what does that tell you about P<sub>m</sub> versus P<sub>e</sub>? What happens to the rotors?
   - *It means P<sub>e</sub> > P<sub>m</sub> (more electrical load than mechanical input). Each rotor decelerates (loses kinetic energy) because there is a net retarding torque — that is what the swing equation says, and that is why governors detect speed and open valves.*
2. What is the purpose of droop?
   - *To allow multiple generators to share load stably without fighting; with zero droop load division is indeterminate.*
3. Why can't AGC rely on governors alone?
   - *Because droop leaves a steady-state frequency error (Eq. 5.3); AGC adds integral action to drive that error to zero.*
4. If you need to raise voltage at a bus that's sagging under heavy inductive load, do you add a shunt capacitor or a shunt inductor?
   - *A shunt capacitor — it supplies the VARs the load is consuming locally, reducing the VAR flow through the line reactance and reducing the voltage drop. A shunt inductor would absorb VARs and make voltage lower still (used for overvoltage on lightly loaded lines).*
5. Why is voltage control "local" whereas frequency control is "system-wide"?
   - *Because frequency is an integral of power imbalance across the entire synchronous system (one frequency everywhere) and watts travel easily across the grid; by contrast, VARs cause large voltage drops through line reactance, so VARs must be supplied close to where they're needed — each bus is largely responsible for its own voltage magnitude.*

---

## 5.7 Where these notes leave off 🟡

If you have read these five units in order and worked the self-checks, you now have the conceptual skeleton of an introductory power-systems analysis course:

- You can decompose any unbalanced three-phase situation into its three symmetrical components and see why that makes the problem tractable (Unit I).
- You can compute fault currents for the four main shunt fault types and know how to size a circuit breaker (Unit II).
- You understand the physics of synchronism, can read a P-δ curve, and can apply the equal-area criterion to judge transient stability (Unit III).
- You know why economic dispatch is a marginal-cost problem, how losses introduce penalty factors via B-coefficients, and what the coordination equation says (Unit IV).
- You can explain how governors, droop, AGC, and AVRs divide the work of holding frequency and voltage on target across timescales from milliseconds to hours (Unit V).

From here the natural next topics (taught in advanced power-systems courses) are: load-flow computation in detail (Newton-Raphson, fast-decoupled), state estimation, protection relaying in depth, power-system dynamics with multi-machine models, HVDC and FACTS devices, renewable integration, and power-system restructuring/markets. Each of these builds on the skeleton these notes have put in place.
