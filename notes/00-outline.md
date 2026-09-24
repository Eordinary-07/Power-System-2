# Power Systems-II — Notes Outline & Prerequisite Map

This is the short road-map for the full notes. The complete first-time notes will follow this structure, unit by unit, citing *Modern Power System Analysis*, 3rd ed., by D.P. Kothari & I.J. Nagrath (Tata McGraw-Hill, 2003) — hereafter **"K&N"** — as the primary source, with cross-reference to *Power Systems Analysis*, 2nd ed., by A.R. Bergen & V. Vittal (Prentice Hall, 2000) — hereafter **"B&V"** — for additional intuition where helpful. (Saadat's *Power System Analysis* is also in the repo but is a scanned image-only PDF; it will be used only for cross-checking ideas, not as a primary source because figures cannot be extracted cleanly from it.)

---

## Prerequisites — what the reader is assumed to already know (stated honestly)

The syllabus treats Power Systems-II as a 5th-semester B.Tech. course. It therefore assumes the reader has already completed:

1. **Basic circuit theory** — Ohm's law, KCL/KVL, phasor analysis of AC circuits, complex impedance, complex power (S = P + jQ).
2. **Three-phase circuits** — balanced Y and Δ connections, line vs phase quantities, per-phase analysis.
3. **Per-unit system** — choosing bases, converting impedances to per-unit.
4. **Transformers** — single-phase equivalent circuit, Y-Δ connections, three-phase transformer banks.
5. **Synchronous machines** — the steady-state model (voltage behind synchronous reactance), subtransient/transient/synchronous reactances (at a qualitative level, since Power Systems-I covers them).
6. **Transmission lines** — series impedance and shunt admittance, short-line model at minimum.

**What these notes will briefly re-teach inline** (because beginners don't reliably remember it):
- Complex-number algebra with the `a` operator (`a = e^{j120°}`)
- Phasor notation and what "phase sequence" physically means
- The per-unit idea (one short refresher, not a full course)

**What these notes will *not* re-teach** (flagged upfront so the reader can go learn it first):
- How a synchronous generator physically turns and produces voltage (that's Electric Machines / Power Systems-I).
- How to build a Y<sub>bus</sub> matrix from line data (that's Power Systems-I / load flow).

---

## Big-picture map — how the five units fit together

Power systems are designed to operate in a very specific happy state: three-phase balanced, voltages near rated, frequency near 50/60 Hz, each generator producing the cheapest possible mix of power, all generators staying in synchronism.

The five units of this course each answer a different question about what happens **when that happy state is disturbed**:

```
 UNIT I   Symmetrical Components
            └─ the mathematical tool: how to turn UNBALANCED 3-phase
               problems into THREE BALANCED single-phase problems
                  │
                  ▼
 UNIT II  Fault Analysis (Symmetrical & Unsymmetrical)
            └─ using that tool to compute currents/voltages when a short
               circuit happens: L-G, L-L, L-L-G, open conductor, 3-phase.
               Tells you how big a circuit breaker must be.
                  │
                  ▼
 UNIT III Power System Stability
            └─ after a fault is cleared, do the generators stay in sync, or
               do they "slip a pole" and tear the system apart? Swing
               equation, equal-area criterion, transient stability.
                  │
                  ▼
 UNIT IV  Economic Operation
            └─ while the system is running stably, which generators should
               produce how much power so that the fuel bill is minimised,
               accounting for transmission losses?
                  │
                  ▼
 UNIT V   Power System Dynamics & Control
            └─ when the load drifts up or down, how does the system bring
               frequency and voltage back to set-point? Turbines/governors,
               droop, AGC, excitation systems, AVR.
```

Read top-to-bottom: you must understand Unit I before Unit II (it's the tool), and Unit II motivates Unit III (faults are the most common "large disturbance"), but Units IV and V are somewhat independent — they answer "how do we run it well" rather than "what happens when it breaks".

---

## Per-unit list of topics (keyed to K&N sections)

### Unit I — Symmetrical Component Transformation (≈ 8 lectures)
- Source: K&N Ch. 10, §10.1–10.9 (K&N PDF pages ~193–206; book pp. 369–393)
- Topics:
  1. Why balanced analysis fails for unbalanced faults (§10.1)
  2. The `a` operator and the idea of three balanced sets adding to one unbalanced set (§10.2)
  3. The matrix **A** and **A**⁻¹: synthesis (V<sub>p</sub> = A V<sub>s</sub>) and analysis (V<sub>s</sub> = A⁻¹ V<sub>p</sub>) (§10.2)
  4. Zero-sequence facts: line voltages have no V<sub>0</sub>; neutral current = 3 I<sub>a0</sub>; delta connection traps I<sub>0</sub> (§10.2)
  5. Power invariance: why there is a factor of 3 (§10.2, Eq. 10.33)
  6. Phase shift in Y-Δ transformers: +30°/−30° for positive/negative sequence (§10.3)
  7. Sequence impedances of transmission lines — why Z<sub>1</sub> = Z<sub>2</sub> but Z<sub>0</sub> ≠ Z<sub>1</sub> (§10.4 / §10.7)
  8. Sequence impedances of synchronous machines — Z<sub>1</sub>, Z<sub>2</sub>, Z<sub>0</sub> and why there is an EMF only in the positive-sequence network (§10.6)
  9. Sequence impedances of transformers (§10.8)
  10. Sequence networks of a complete power system and how they connect at a fault point (§10.9)
- Key diagrams to extract from K&N: Fig. 10.1, 10.2, 10.5, 10.6, 10.7, 10.8, 10.9, 10.10, 10.12 and any others verified.

### Unit II — Symmetrical & Unsymmetrical Fault Analysis (≈ 11 lectures)
- Source: K&N Ch. 9 (symmetrical faults, PDF pages ~172–193; book pp. 327–365) and Ch. 11 (unsymmetrical, PDF pages ~207–225; book pp. 397–429), plus end-of-chapter sections on circuit-breaker ratings and reactors.
- Topics:
  1. What a fault physically is; why we study it (§9.1 intro + §11.1 intro)
  2. Transients on a short-circuited transmission line (qualitative, §9.2)
  3. Short circuit of a synchronous machine on no load — subtransient, transient, steady-state currents and the corresponding reactances X″<sub>d</sub>, X′<sub>d</sub>, X<sub>d</sub> (§9.3)
  4. Short circuit of a loaded machine (§9.4)
  5. Algorithm for symmetrical fault studies; selection of circuit-breaker ratings; current-limiting reactors (§9.5, §9.6, §9.7)
  6. Single Line-to-Ground (LG) fault — connection of sequence networks in series (§11.3)
  7. Line-to-Line (LL) fault — parallel connection of Z<sub>1</sub> and Z<sub>2</sub>, no Z<sub>0</sub> (§11.4)
  8. Double Line-to-Ground (LLG) fault — parallel of Z<sub>1</sub>, Z<sub>2</sub>, Z<sub>0</sub> (§11.5)
  9. Open-conductor faults (series-type) (§11.6)
  10. Brief mention of Z<sub>bus</sub> method (§11.7)
- Key diagrams to extract from K&N: Fig. 9.3/9.4/9.5 (SC of synchronous machine, AC + DC offset, reactance decay), Fig. 11.1–11.11 as verified (each fault type network connection).

### Unit III — Power System Stability (≈ 10 lectures)
- Source: K&N Ch. 12 (PDF pages ~225–280; book pp. 433–508)
- Topics:
  1. Why stability matters; definitions: steady-state, dynamic, transient (§12.1)
  2. Dynamics of the synchronous machine: the rotor as a rotating inertia, the swing equation, inertia constant H, M = 2H/ω<sub>s</sub> (§12.2)
  3. Power-angle equation: P<sub>e</sub> = (E V / X) sin δ, why it's a sine (§12.3)
  4. Node elimination / simple two-machine and one-machine-infinite-bus systems (§12.4, §12.5)
  5. Steady-state stability: meaning of dP/dδ > 0; steady-state stability limit = E V / X (§12.6)
  6. Transient stability: the physical picture, swing curve (§12.7)
  7. Equal-area criterion: accelerating area = decelerating area; derivation; critical clearing angle (§12.8)
  8. Applications of equal-area criterion: sudden load change, fault with/without line tripping, auto-reclosing (§12.9)
  9. Point-by-point (step-by-step) solution of swing equation (§12.10 start)
  10. Factors affecting and methods of improving transient stability (within §12)
- Key diagrams: swing-equation equivalent, P-δ curve, equal-area diagrams for various cases.

### Unit IV — Economic Operation of Power Systems (≈ 8 lectures)
- Source: K&N Ch. 7, §7.1–7.6 (PDF pages ~129–151; book pp. 242–284). Hydrothermal scheduling (§7.7) will be mentioned only briefly, since the syllabus specifies thermal economic dispatch.
- Topics:
  1. Why we care: fuel cost is the largest running expense; what economic dispatch is (§7.1)
  2. Input-output curves, heat-rate curves, incremental fuel cost (dC/dP) (§7.2)
  3. Equal incremental-cost criterion for units on the same bus (no losses) — derivation by Lagrange multipliers; what equal λ means physically (§7.2)
  4. Worked example with two and three units; handling generator limits (§7.2 + Example 7.1)
  5. Brief qualitative mention of unit commitment (why we must also decide which units to turn on/off) (§7.3)
  6. Transmission losses as a function of generator outputs: B-coefficients (loss formula) P<sub>L</sub> = ΣΣ B<sub>ij</sub>P<sub>i</sub>P<sub>j</sub> (§7.5)
  7. Coordination equation (exact): dC<sub>i</sub>/dP<sub>i</sub> + λ ∂P<sub>L</sub>/∂P<sub>i</sub> = λ; the penalty factor L<sub>i</sub> = 1/(1 − ∂P<sub>L</sub>/∂P<sub>i</sub>) (§7.5)
  8. Derivation sketch of B-coefficients (§7.5 — conceptually, not full algebra)
- Key diagrams: incremental cost curves (Fig. 7.1–7.4), two-plant loss geometry (Fig. 7.9).

### Unit V — Power System Dynamics / Load-Frequency & Voltage Control (≈ 8 lectures)
- Source: K&N Ch. 8, §8.1–8.6 (PDF pages ~154–171; book pp. 289–325) plus discussion of reactive power / excitation from Ch. 5 (voltage control discussion) as needed.
- Topics:
  1. Why the system has two separate control problems: frequency ↔ active power, voltage ↔ reactive power (§8.1 intro)
  2. Turbines and speed governors — how a flyball governor physically works (§8.2, Fig. 8.1, 8.2)
  3. Generator-load model: ΔP<sub>m</sub> − ΔP<sub>e</sub> = M dΔf/dt + D Δf (§8.2)
  4. Droop control and why several generators in parallel share a load in proportion to rating; the frequency-load characteristic (§8.2)
  5. Frequency dependence of loads; the damping term D (§8.2)
  6. Automatic Generation Control (AGC) / secondary control — integral action to restore frequency to 50/60 Hz and tie-line flows to schedule (§8.3, §8.4 – two-area will be mentioned briefly)
  7. Where reactive power is generated and absorbed in the system — generators, shunt capacitors/inductors, line charging, transformers (drawn from Ch. 5 voltage-control discussion)
  8. Excitation systems and Automatic Voltage Regulators (AVR) on synchronous generators (§8.6 + B&V Ch. 6)
- Key diagrams: load-frequency control schematic (Fig. 8.1), governor model (Fig. 8.2), two-area block diagram, AVR block diagram.

---

## Added characteristic (not in the original 11 but I'll apply it throughout)

**12. Pacing labels in the margin.** In the full notes I'll mark each paragraph/section with one of three pacing tags:
  - 🔵 **Routine** — book-keeping or algebra you can skim on first read once the idea has landed.
  - 🟡 **Pay attention** — a new idea is being introduced and the reasoning matters.
  - 🔴 **Slow down** — conceptually hard; expect to re-read, draw it out, and do the self-check.

Reason: first-time readers have no way to tell whether a page is new physics or just crunching, and the biggest source of frustration is getting stuck on routine algebra thinking it's profound, or skimming a crucial derivation thinking it's routine.

---

## Diagram inventory (to be built and verified as I write)

I will maintain a running table in a separate file `diagram_log.md` listing every figure used: (figure number, source book, source page number, where placed in notes, verification status). Every diagram will be cropped from K&N (primary) or B&V (secondary) using pymupdf, then visually re-opened and checked against its caption before the notes are considered done.
