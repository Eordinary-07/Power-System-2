# Quick Reference Card — Power Systems-II

> This appendix collects the most-used formulas, tables, and rules of thumb from Units I–V in one place for quick lookup after you have already read the notes. **Do not read this first** — come back to it after you have worked through the units.

---

## Symmetrical components (Unit I)

**`a` operator:**
```
a  = e^{j120°} = −1/2 + j√3/2
a² = e^{j240°} = −1/2 − j√3/2
a³ = 1;   1 + a + a² = 0;   a* = a²
```

**Synthesis (components → phases):** V<sub>p</sub> = A V<sub>s</sub>
```
[Va]   [1  1  1][Va1]
[Vb] = [a² a  1][Va2]
[Vc]   [a  a² 1][Va0]
```

**Analysis (phases → components):** V<sub>s</sub> = A⁻¹ V<sub>p</sub>
```
Va1 = (1/3)(Va + a Vb + a² Vc)    positive sequence
Va2 = (1/3)(Va + a² Vb + a Vc)    negative sequence
Va0 = (1/3)(Va + Vb + Vc)         zero sequence (= average)
```

**Zero-sequence facts:**
- Neutral current: I<sub>n</sub> = 3 I<sub>a0</sub>
- Line-to-line voltages: V<sub>0</sub><sup>LL</sup> = 0 always
- No neutral connection ⇒ I<sub>a0</sub> = 0
- Δ windings circulate I<sub>0</sub> internally but block it from the line terminals

**Y-Δ transformer phase shift (ANSI/IEEE standard used by K&N):**
- Positive sequence: HV leads LV by **+30°**
- Negative sequence: HV lags LV by **−30°**
- Zero sequence: no shift, but connection-dependent whether it flows

**Sequence impedances (typical):**

| Element | Z<sub>1</sub> | Z<sub>2</sub> | Z<sub>0</sub> |
|---|---|---|---|
| Transposed transmission line | Z<sub>L</sub> = R + jX<sub>L</sub> | = Z<sub>1</sub> | ≈ (2–3.5) Z<sub>1</sub> (returns through ground) |
| Transformer | Z<sub>leak</sub> | = Z<sub>1</sub> | Z<sub>leak</sub> (if grounded-Y path exists), else open/short per connection |
| Synchronous machine | jX″<sub>d</sub> (subtransient), jX′<sub>d</sub> (transient), jX<sub>d</sub> (steady) | ≈ j(X″<sub>d</sub> + X″<sub>q</sub>)/2, no EMF | Z<sub>0g</sub> + 3Z<sub>n</sub>, no EMF |

Only the **positive-sequence** network contains internal EMFs.

---

## Fault analysis (Unit II)

**Three-phase fault (symmetrical):**
```
If = Vf / Z1
```

**Fault connection table (for Z<sub>f</sub> = 0 solid fault, V<sub>f</sub> = 1∠0° pu):**

| Fault | Sequence networks at F | Key current |
|---|---|---|
| 3φ | Positive only, shorted to ref | I<sub>f</sub> = 1/Z<sub>1</sub> |
| LG (phase a) | Z<sub>1</sub>, Z<sub>2</sub>, Z<sub>0</sub> **in series** (+3Z<sub>f</sub>) | I<sub>a</sub> = 3/(Z<sub>1</sub> + Z<sub>2</sub> + Z<sub>0</sub> + 3Z<sub>f</sub>) |
| LL (b–c) | Z<sub>1</sub> ∥ Z<sub>2</sub> (opposing), Z<sub>0</sub> open | I<sub>b</sub> = −I<sub>c</sub> = −j√3/(Z<sub>1</sub> + Z<sub>2</sub> + Z<sub>f</sub>) |
| LLG (b,c–gnd) | Z<sub>1</sub>, Z<sub>2</sub>, Z<sub>0</sub> **in parallel** | I<sub>a1</sub> = 1/(Z<sub>1</sub> + Z<sub>2</sub>Z<sub>0</sub>/(Z<sub>2</sub>+Z<sub>0</sub>)) ; I<sub>g</sub> = 3I<sub>a0</sub> |
| 1 open conductor | Series networks in parallel across break | See K&N §11.6 |

**Synchronous machine reactance stages** (3-phase short at terminals):
| Period | Timeframe | Reactance | Current |
|---|---|---|---|
| Subtransient | first 1–2 cycles | X″<sub>d</sub> (smallest, damper windings still acting) | I″ = E/X″<sub>d</sub> |
| Transient | a few cycles to seconds | X′<sub>d</sub> (field winding still constraining flux) | I′ = E/X′<sub>d</sub> |
| Steady-state | seconds onward | X<sub>d</sub> (synchronous) | I = E/X<sub>d</sub> |

DC offset: worst case (fault at voltage zero) can nearly **double** the first peak — circuit breakers must survive the first-cycle (momentary) peak and interrupt a few cycles later (interrupting duty).

---

## Stability (Unit III)

**Swing equation:**
```
M d²δ/dt² = Pm − Pe = Pa
M (pu) = 2H/ωs
H = stored kinetic energy at rated speed (MJ) / machine rating (MVA)
```
Typical H: 3–10 MJ/MVA (steam turbo), 2–3 (hydro), 1–1.5 (condenser).

**Power-angle curve (OMIB, E behind X to infinite bus V):**
```
Pe(δ) = (E V / X) sin δ
Pmax = E V / X   at δ = 90°
```

**Steady-state stability criterion:** dP<sub>e</sub>/dδ > 0 at the operating point (i.e., δ < 90°).

**Equal-area criterion:**
```
∫_{δ0}^{δc} (Pm − Pe,during) dδ  =  ∫_{δc}^{δmax} (Pe,post − Pm) dδ
```
- Accelerating area A<sub>1</sub> = KE gained during the fault
- Decelerating area A<sub>2</sub> = KE that can be absorbed after clearing
- Stable iff A<sub>2</sub> ≥ A<sub>1</sub>
- Critical clearing angle δ<sub>cr</sub>: A<sub>1</sub> = A<sub>2</sub> exactly

**Improving transient stability:** faster clearing, higher excitation (bigger E), fast valving, braking resistors, single-pole switching, stronger transmission (more lines, series comp.), dynamic VAR support, controlled islanding.

---

## Economic operation (Unit IV)

**Quadratic cost model:**
```
Ci(Pi) = ai + bi Pi + ci Pi²       Rs/h
ICi = dCi/dPi = bi + 2ci Pi        Rs/MWh   (incremental / marginal cost)
```

**Equal-lambda rule (no losses, no limits hit):**
```
dC1/dP1 = dC2/dP2 = ··· = dCn/dPn = λ
```
λ = system marginal cost (Rs/MWh), the cost of serving one more MW of load.

If a unit hits P<sub>min</sub> or P<sub>max</sub>, clamp it and re-solve λ over the rest.

**Loss formula (B-coefficients):**
```
PL = ΣiΣj Bij Pi Pj  (+ linear and constant terms often dropped)
```

**Coordination equation (with losses):**
```
ICi · Li = λ
Li = 1 / (1 − ∂PL/∂Pi)        penalty factor
```
Far-from-load plants → high ∂P<sub>L</sub>/∂P<sub>i</sub> → large L<sub>i</sub> → must run at lower IC<sub>i</sub> (lower output).

---

## Load-frequency & voltage control (Unit V)

**Two fundamental splits:**
- Real power (watts, P) ↔ frequency (f) ↔ turbine governor + AGC ↔ system-wide
- Reactive power (VARs, Q) ↔ voltage magnitude (|V|) ↔ exciter/AVR + shunt compensation ↔ local

**Generator-load model (Δ small-signal):**
```
ΔPm − ΔPe = M dΔf/dt + D Δf
```
D = load-damping constant (~1–2% / 1% frequency).

**Droop:**
```
ΔPm = −(1/R) Δf
```
Typical R = 5% (0.05 pu). Droop allows multiple generators to share load stably in proportion to rating.

**Steady-state frequency after step load ΔP<sub>e</sub>:**
```
Δf = −ΔPe / (D + 1/R)
```

**AGC (secondary control):** integral action on ACE = ΔP<sub>tie</sub> − B Δf; restores frequency to 50/60 Hz and tie flows to schedule. Operates over 30 sec to minutes.

**Timescales stack (P-f side):**
1. Inertia (instantaneous)
2. Primary / droop (2–10 s)
3. Secondary / AGC (30 s – min)
4. Tertiary / economic dispatch (min – hour)

**VAR sources / sinks:** generators (over/underexcited), shunt capacitors/inductors, line charging (lightly loaded), line reactance (heavily loaded), transformers, induction motor loads. Add a **shunt capacitor** to raise a sagging voltage; a **shunt inductor** to suppress overvoltage on lightly loaded lines.

---

## Per-unit refresher

```
S_base (chosen, often 100 MVA)
V_base (chosen at one level; propagates through transformers by turns ratio)
I_base = S_base / (√3 V_base)
Z_base = V_base² / S_base
X_pu = X_actual / Z_base
```
In per-unit, transformers disappear (1:1 ideal), √3 factors vanish, and V=IZ and S=VI* hold directly. Convert from one base to another:
```
X_new_pu = X_old_pu · (S_new/S_old) · (V_old/V_new)²
```

---

## Three things to remember if you remember nothing else

1. **Symmetrical components turn one messy unbalanced problem into three simple balanced problems. Only the positive-sequence network has voltage sources.**
2. **For faults, memorize the connection table:** LG = series, LL = pos∥neg (no zero), LLG = all three in parallel, 3φ = positive-only. That is the entire practical payoff of Unit I.
3. **Frequency is everyone's problem (system-wide); voltage is a local problem.** Watts travel easily; VARs do not.
