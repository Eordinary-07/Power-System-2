# Exam prep — what you actually need to be able to do

> This appendix lists (a) the formulas you will need to recall from memory, (b) the five exam-question shapes that appear in almost every Power Systems-II paper, and (c) the mistakes that lose the most marks. Read it after you have worked through the five units and the practice problems.

---

## A. Formulas to know cold

You do not need to memorize *every* derivation, but the following list is what shows up on essentially every RTMNU (and equivalent) PS-II paper. If any of these looks foreign, go back to the section noted.

### Unit I — Symmetrical components
- `a = e^{j120°} = −0.5 + j√3/2`; `a³ = 1`; `1 + a + a² = 0` (§1.3)
- `V_{a1} = (1/3)(V_a + a V_b + a² V_c)`
- `V_{a2} = (1/3)(V_a + a² V_b + a V_c)`
- `V_{a0} = (1/3)(V_a + V_b + V_c)` (§1.6, Eqs. 1.11–1.13)
- `I_n = 3 I_{a0}` (§1.7, Fact 1)
- Y<sub>g</sub>-Δ transformer: +1→30° shift, −1→−30° shift, zero-sequence blocked from Δ side / circulates inside Δ (§1.9)
- Z<sub>n</sub> appears as **3Z<sub>n</sub>** in the zero-sequence network (§1.12)

### Unit II — Fault analysis
- DC offset worst case: `i_asym(peak) ≈ 2·√2 · I_sym` when α = 0 (voltage-zero switching) (§2.2)
- X″<sub>d</sub> < X′<sub>d</sub> < X<sub>d</sub> (subtransient < transient < synchronous) (§2.3)
- 3-phase fault: `I_f = V_f / Z_1` (§2.4)
- LG fault: `I_a = 3 V_f / (Z_1 + Z_2 + Z_0 + 3Z_f)` (§2.5.1, Eq. 2.1)
- LL fault: `I_b = −j√3 V_f / (Z_1 + Z_2 + Z_f)`, I<sub>a0</sub> = 0 (§2.5.2, Eq. 2.3)
- LLG fault: Z<sub>1</sub>, Z<sub>2</sub>, Z<sub>0</sub> in parallel (§2.5.3, Eq. 2.4)
- Fault MVA: `S_f = S_base / |Z_th|` (pu form)
- I<sub>base</sub> = S<sub>base</sub>/(√3 V<sub>base</sub>) for ampere conversions (§2.4)

### Unit III — Stability
- Swing equation: `(2H/ω_s) d²δ/dt² = P_m − P_e` (§3.2, Eq. 3.2)
- Power-angle curve: `P_e = (EV/X) sin δ`, P<sub>max</sub> = EV/X at δ = 90° (§3.3, Eq. 3.4)
- Steady-state stable iff `dP_e/dδ > 0` (δ < 90° for cylindrical rotor) (§3.3)
- Equal-area: A<sub>accel</sub> = ∫(P<sub>m</sub> − P<sub>e,during</sub>) dδ = A<sub>decel</sub> = ∫(P<sub>e,post</sub> − P<sub>m</sub>) dδ at critical clearing (§3.4)
- For P<sub>e,during</sub> = 0, P<sub>e,post</sub> = P<sub>max,post</sub> sin δ:
  `cos δ_cr = (P_m(δ_max − δ_0) − P_max,post cos δ_max) / P_max,post` with δ<sub>max</sub> = π − arcsin(P<sub>m</sub>/P<sub>max,post</sub>) (all angles in radians).

### Unit IV — Economic operation
- IC<sub>i</sub> = dC<sub>i</sub>/dP<sub>i</sub>; for quadratic C<sub>i</sub> = α<sub>i</sub> + b<sub>i</sub>P<sub>i</sub> + c<sub>i</sub>P<sub>i</sub>², IC<sub>i</sub> = b<sub>i</sub> + 2c<sub>i</sub>P<sub>i</sub> (§4.2)
- Lossless dispatch: **IC₁ = IC₂ = … = λ** at optimum; ΣP<sub>i</sub> = P<sub>D</sub> (§4.3)
- With losses: **IC<sub>i</sub> · L<sub>i</sub> = λ** where L<sub>i</sub> = 1/(1 − ∂P<sub>L</sub>/∂P<sub>i</sub>) is the penalty factor (§4.5, Eq. 4.9)
- Quadratic-loss approximation: P<sub>L</sub> = ΣΣ B<sub>ij</sub> P<sub>i</sub> P<sub>j</sub> (B-coefficients)

### Unit V — Control
- Speed droop: `R = −Δf/(ΔP · f_nom/P_rated)` (pu); gain = P<sub>rated</sub>/(R·f<sub>nom</sub>) in MW/Hz (§5.2)
- Multi-unit sharing: ΔP<sub>i</sub> = −(P<sub>rated,i</sub>/(R<sub>i</sub> f<sub>nom</sub>)) Δf; units share ΔP in proportion to P<sub>rated</sub>/R<sub>i</sub> (§5.2 example)
- System stiffness: `β = D + Σ (1/R_i)` (pu); `Δf = −ΔP/β` for a generation-loss step (§5.2)
- Primary (droop): fast, proportional, leaves steady-state error. Secondary (AGC): slow, integral, restores f to 50 Hz and corrects tie-line flows. Tertiary: economic re-dispatch (§5.3).
- Reactive-power devices: generators (AVR), shunt capacitors/inductors, SVC/STATCOM, tap-changing transformers; these control **voltage**, not frequency (§5.4).

---

## B. The five standard exam-question shapes

Almost every PS-II exam paper is built from these five problem types. The narrated worked examples and practice problems cover each shape.

**Shape 1 — Sequence-component decomposition (Unit I).**
Given three phase voltages/currents (in polar form), compute V<sub>a0</sub>, V<sub>a1</sub>, V<sub>a2</sub> (or current versions), then re-synthesize to verify. Watch the 1/3 factor; forget it and every component is 3× too big.
- *Where to practise:* Worked example in §1.6; Practice problems I-P1, I-P2.

**Shape 2 — Fault-current calculation (Unit II).**
Given a one-line diagram with per-unit reactances of generators, transformers, and lines, compute fault current for (a) a 3-phase fault, (b) an LG fault, sometimes LL or LLG as a third part. Steps: (i) get all X onto a common base, (ii) build Z<sub>th</sub> from the fault point, (iii) plug into the matching formula above. Remember the **3Z<sub>f</sub>** for LG through fault impedance, and **3Z<sub>n</sub>** in Z<sub>0</sub> for neutral-grounding reactors.
- *Where to practise:* Worked examples §2.4 (3φ) and §2.7 (LG); Practice problems II-P1, P3, P4, P5.

**Shape 3 — Equal-area criterion / critical clearing angle (Unit III).**
Given an OMIB system with pre-fault, during-fault, and post-fault P<sub>max</sub>, plus P<sub>m</sub>, find δ<sub>0</sub>, δ<sub>max</sub>, and δ<sub>cr</sub>. Convert all angles to radians before integrating; answer in degrees. Common twist: P<sub>e,during</sub> ≠ 0 (some power still transferred during the fault).
- *Where to practise:* Worked example §3.4; Practice problems III-P3, P4.

**Shape 4 — Economic dispatch (Unit IV).**
Two or three generators with quadratic cost curves, total load given; find optimal P<sub>i</sub> and λ. With generator limits: solve unconstrained first, clamp any unit that violates its limit, re-solve. With losses: the coordination equation IC<sub>i</sub>L<sub>i</sub> = λ.
- *Where to practise:* Worked example §4.3; Practice problems IV-P2, P3, P4.

**Shape 5 — Load-frequency control (Unit V).**
Two or three generators in parallel with given % droop and ratings; a load step occurs; find Δf and ΔP<sub>i</sub>. May add D (load damping) or ask for the effect of adding AGC.
- *Where to practise:* Worked example §5.2; Practice problems V-P1, P2, P3.

> 🟡 *A typical 5-question RTMNU paper will have one of each shape plus a handful of short-answer/explain questions.*

---

## C. The five most-common point-losing mistakes

1. **Forgetting the factor of 3.**
   Neutral I<sub>n</sub> = 3 I<sub>a0</sub>; neutral impedance appears as 3Z<sub>n</sub> in Z<sub>0</sub>; LG fault-path impedance is 3Z<sub>f</sub>; the A⁻¹ matrix has a 1/3 out front. Every one of these "3"s is examinable; forgetting any single one loses 50–75% of the marks on that problem.

2. **Mixing up degrees and radians in the equal-area integral.**
   sin δ and cos δ can be evaluated in degrees on your calculator, but *δ<sub>max</sub> − δ<sub>0</sub>* in the cos δ<sub>cr</sub> formula must be in **radians**. If you use degrees there, δ<sub>cr</sub> comes out nonsense.

3. **Using X<sub>d</sub> instead of X″<sub>d</sub> for momentary (breaker) fault current.**
   The first-cycle current is governed by X″<sub>d</sub>. X<sub>d</sub> is for steady-state short-circuit current many seconds later. Breakers must survive and interrupt the big current, not the small steady-state one.

4. **Zero-sequence across Y-Δ transformers.**
   Zero sequence *does not* "pass through" a Δ winding to the other side. On the Y-grounded side it sees a short to reference through transformer leakage; on the Δ side zero-sequence current circulates inside the delta and cannot appear in the line currents. Draw the zero-sequence network correctly; if you draw Z<sub>0</sub> continuing through a Δ to a line, the fault current you compute will be wildly wrong.

5. **Confusing primary (droop) and secondary (AGC) control in essays.**
   If asked "how does the grid restore frequency to 50 Hz after a load step?" the answer is **not** "governors" — governors arrest the fall but leave a steady-state error. It is AGC (secondary control, integral action) that restores f to 50 Hz. If asked "how do generators share the load instantly and stably?" the answer *is* droop. Read the question carefully.

---

## D. Ten short-answer questions that appear on almost every paper

1. Why do we use symmetrical components for fault analysis?
2. What are positive-, negative-, and zero-sequence components?
3. Why is zero-sequence impedance of a transmission line higher than positive-sequence?
4. Explain DC offset in fault currents; when is it maximum?
5. Distinguish between subtransient, transient, and steady-state reactance.
6. What is the equal-area criterion, and what does the critical clearing angle mean?
7. State and explain the equal-incremental-cost criterion for economic dispatch.
8. What is a penalty factor? Why is it greater than 1 for remote plants?
9. Explain speed droop in a governor. Why is droop necessary for stable parallel operation?
10. Distinguish between primary, secondary, and tertiary control of frequency.

Answers to all ten are somewhere in these notes (glossary entries in 08 give the one-line version; the relevant sections give the full explanation).

---

## E. Three-day study plan (if you're short on time)

- **Day 1:** Read Units I and II. Do worked examples §1.6 and §2.4/§2.7 on scrap paper. Do practice problems I-P5, II-P1, II-P3.
- **Day 2:** Read Units III and IV. Do worked examples §3.4 and §4.3. Do practice problems III-P3, IV-P2, IV-P3.
- **Day 3:** Read Unit V. Do worked example §5.2 and practice problem V-P2. Then read 07-quick-reference.md twice, the ten short-answer questions above, and re-do all five narrated worked examples with the answers covered. If you can do those five blind, you can pass comfortably.

Good luck.
