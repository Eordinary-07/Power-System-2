# Power Systems-II — Complete First-Time Notes

This directory contains a complete set of introductory notes for **Power Systems-II** (B.Tech. Electrical Engg., Sem-V, RTM Nagpur University syllabus BEL5T15), written for a reader who is meeting every concept for the first time.

## Source material
- **Primary textbook:** D.P. Kothari & I.J. Nagrath, *Modern Power System Analysis*, 3rd ed. (Tata McGraw-Hill, 2003) — PDF: `../modern-power-systems-analysis-d-p-kothari-i-j-nagrath_compress.pdf`
- Supporting reference: A.R. Bergen & V. Vittal, *Power Systems Analysis*, 2nd ed. (Prentice Hall, 2000) — PDF: `../arthur-r-bergen-vijay-vittal-power-systems-analysis-ocr_compress.pdf`
- Additional reference: Hadi Saadat, *Power System Analysis* (TMH, 2002) — PDF: `../power-system-analysis-hadi-saadatpdf_compress.pdf` (image-only scan; cross-checks only)
- Syllabus: `../SOE_EE_NEP_1st_2nd_3rd_4th_5th_and_6th_sem_syllabus.pdf` (see pp. 101–102 for BEL5T15)

---

## Reading order

Start at the top of this list and read straight through — each file builds on the previous one.

| Order | File | Contents |
|------|------|----------|
| 1 | [`00-outline.md`](00-outline.md) | Prerequisite map, big-picture subject overview, pacing convention |
| 2 | [`01-intro-and-prerequisites.md`](01-intro-and-prerequisites.md) | Why the subject exists, subject map, per-unit refresher, how to read the notes |
| 3 | [`02-unit-i-symmetrical-components.md`](02-unit-i-symmetrical-components.md) | Unit I — Symmetrical components, `a` operator, **A** and **A**⁻¹, Y-Δ phase shift, sequence impedances of lines/generators/transformers |
| 4 | [`03-unit-ii-fault-analysis.md`](03-unit-ii-fault-analysis.md) | Unit II — DC offset, synchronous-machine transients (X″<sub>d</sub>, X′<sub>d</sub>, X<sub>d</sub>), symmetrical faults, LG/LL/LLG/open-conductor connection rules, breaker ratings, worked LG example |
| 5 | [`04-unit-iii-stability.md`](04-unit-iii-stability.md) | Unit III — Swing equation, H constant, P-δ curve, steady-state stability, equal-area criterion, critical clearing angle, improving stability |
| 6 | [`05-unit-iv-economic-operation.md`](05-unit-iv-economic-operation.md) | Unit IV — Incremental fuel costs, equal-λ rule, penalty factors, B-coefficients, coordination equation, brief unit commitment |
| 7 | [`06-unit-v-control.md`](06-unit-v-control.md) | Unit V — Governor hardware, droop, AGC, frequency vs. voltage control split, excitation/AVR, reactive-power sources, timescales stack |
| 8 | [`07-quick-reference.md`](07-quick-reference.md) | **After you've read the notes** — one-card summary of every key formula, table, and rule of thumb |
| ref | [`diagram_log.md`](diagram_log.md) | Every figure cited: source book, page, caption match, final verification status |

All figures are stored in [`figures/`](figures/).

---

## Pacing dots used throughout
- 🔵 **Routine** — book-keeping/algebra you can skim once the idea has landed
- 🟡 **Pay attention** — a new idea is being introduced
- 🔴 **Slow down** — conceptually hard; re-read, draw, do the self-check

Other signposts:
- **❓ Understanding checkpoint** — a short question you can answer right now, with answer on the next line
- **⚠️ Common misconception** — a predictable beginner mistake
- **📖 Source citation** — section and page in K&N so you can look up the original

---

## Characteristics satisfied (per the writing brief)
1. Assumes zero background in Power Systems-II; prerequisites stated and per-unit refreshed inline.
2. One new idea at a time; reasoning narrated in worked examples.
3. Concrete before abstract — physical picture/analogy before each formula.
4. Each core concept given in words, in pictures (where the source has a figure), and in equations.
5. "Why" questions answered explicitly (why marginal cost, why droop, why three sequences decouple, why Z<sub>0</sub> behaves differently between lines and machines, etc.).
6. Understanding checkpoints (❓) with immediate answers after every major concept; common misconceptions (⚠️) flagged explicitly.
7. Prerequisites listed honestly; per-unit retaught; other prior topics named.
8. Pacing dots (🔵/🟡/🔴) on every section.
9. Each unit opens with a "why this matters" paragraph — a real-world problem that forces the topic, never "what will be on the exam."
10. Technical terms introduced once and used consistently; synonyms flagged.
11. Subject map in `00-outline.md` and `01-intro` shows how units connect before diving in.
12. **Added** (not in brief): explicit pacing dots, recurring symbol-redefinition convention (every symbol re-defined at first use in each unit), and a complete diagram-verification log.

## Figure count
- Unit I: 10 placed K&N figures
- Unit II: 13 placed K&N figures
- Unit III: 8 placed K&N figures
- Unit IV: 4 placed K&N figures
- Unit V: 1 placed K&N figure (the governor schematic), with detailed prose walk-through of the hardware

**Total: 36 placed diagrams**, all cropped directly from K&N (no invented or redrawn diagrams), each cited with book page and PDF page directly beneath the figure. The diagram log records verification status honestly, including ⚠️ notes where a scan crop has a minor edge-clip from the original book scan.
