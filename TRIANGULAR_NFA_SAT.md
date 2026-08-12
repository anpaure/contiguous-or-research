# Exact NFA/SAT encoding for triangular spanning words

## 1. Purpose and current exact consequence

For the triangular subproblem used by the four-box construction, let

\[
 \mathcal T_R=\{(0,0)\}\cup
 \{(s,y):1\le s\le R,\ 0\le y<s\}.
\]

A word over `\mathcal T_R` is spanning when it contains every alphabet cell
and, for every

\[
             0\le u<r\le R,\qquad 0\le x<r,
\]

some contiguous interval has minimum first coordinate `u`, maximum first
coordinate `r`, maximum second coordinate `x`, and contains a peak `(s,0)`.
The number of target triples is

\[
                         \sum_{r=1}^R r^2.
\]

The C++ generator
[`scratch/triangular_nfa_sat.cpp`](scratch/triangular_nfa_sat.cpp) gives a
sound and complete SAT encoding for a prescribed word length.  Its first
proof-certified new consequence is

\[
                              \boxed{\rho(4)=2}.       \tag{1.1}
\]

Here `rho(R)` is the number of repeated positions beyond
`|\mathcal T_R|`.  Length `12=|\mathcal T_4|+1` is UNSAT, with a checked
DRAT certificate, while the following length-13 word is spanning:

```text
(4,1) (4,3) (3,2) (3,0) (2,1) (1,0) (0,0)
(1,0) (2,0) (3,0) (4,0) (3,1) (4,2)
```

The generic independent interval analyzer reports

```text
SUMMARY missing=0 alphabet_valid=1 span=1 distinct_cells=11/11
```

## 2. Provider-mask automaton

Fix one target `z=(u,r,x)`.  A cell `c=(s,y)` is allowed inside a witness
exactly when

\[
                         u\le s\le r,\qquad y\le x.   \tag{2.1}
\]

For an allowed cell define its four-bit provider mask

\[
 f_z(c)=
 1_{s=u}+2\,1_{s=r}+4\,1_{y=x}+8\,1_{y=0}.          \tag{2.2}
\]

An interval witnesses `z` exactly when every cell in it is allowed and the
bitwise OR of its provider masks is `15`.

Scan the proposed word from left to right with states

\[
                         0,1,\ldots,15,\mathrm{done}.
\]

State `0` means that no candidate suffix is being retained.  A state
`m in {1,...,15}` records the provider mask of one currently retained
allowed suffix.  At the next cell `c`:

* `done` remains `done`;
* state `15` moves to `done`;
* a forbidden cell sends every unfinished state to `0`;
* at an allowed cell, an unfinished state `m` may move to `0`, to `f_z(c)`
  (restart at the current cell), or to `m OR f_z(c)` (extend).

The initial state is `0`; after the last cell the state must be `15` or
`done`.

### Lemma 1

The automaton has an accepting trajectory if and only if the word contains
a witnessing interval for `z`.

### Proof

Given a witness, stay in state `0` before its left endpoint, restart at that
endpoint, extend through the interval, and then enter `done`.  Conversely,
the first transition reaching state `15` was obtained by consecutive
extensions since the most recent restart.  Every cell in that segment was
allowed, and the accumulated provider mask is `15`; hence that segment is
a witness.  QED.

Allowing abandonment and restart is essential: the automaton existentially
selects one interval without introducing one Boolean selector for every
physical interval.

## 3. CNF encoding

Let

\[
 C=1+\frac{R(R+1)}2,
 \qquad T=\sum_{r=1}^Rr^2.
\]

The variables are:

* `X_(p,c)`, saying that position `p` contains alphabet cell `c`;
* `Q_(t,z,m)`, saying that target `z` is in automaton state `m` after `t`
  word positions.

Exactly one `X_(p,c)` is true at each position, and every alphabet cell is
required to occur.  Exactly one state is true for every `(t,z)`.  For each
current state and current cell, one transition clause requires the next
state to lie in the allowed transition set from Section 2.  Lemma 1 then
proves soundness and completeness independently for every target.

The encoding uses

\[
 nC+(n+1)T\cdot17
\]

variables and

\[
\begin{split}
 &n\left(1+\binom C2\right)+C
 +T(n+1)\left(1+\binom{17}2\right)+2T\\
 &\hspace{35mm}+Tn\cdot17C+\binom C2
\end{split}                                           \tag{3.1}
\]

clauses.  The final `binom(C,2)` clauses choose the reversal-symmetric
orientation whose first alphabet index does not exceed its last.  Reversing
a spanning word preserves every property, so this restriction is safe.

### Theorem 2

The generated CNF is satisfiable exactly when a spanning word of the
prescribed length exists.

### Proof

Any spanning word determines the `X` variables and, by Lemma 1, one
accepting state trajectory for every target.  Reverse the word if necessary
to meet the symmetry clause.  This gives a satisfying assignment.

Conversely, the exactly-one clauses decode the `X` variables into one word.
The occurrence clauses make it span the alphabet.  For every target, the
state clauses and transition clauses describe an accepting automaton
trajectory, so Lemma 1 supplies a witnessing interval.  QED.

### Structurally independent interval-selector encoding

[`scratch/triangular_interval_sat.cpp`](scratch/triangular_interval_sat.cpp)
implements a second exact encoding.  For each target it selects exactly one
physical interval of length at least two.  A selected interval implies, at
every contained position, that the chosen cell lies in the target Ferrers
box; four additional clauses require occurrences attaining the two first-
coordinate extrema, the second-coordinate maximum, and height zero.  A Sinz
sequential counter enforces exactly one selected interval per target.

This encoding does not use the NFA recurrence.  Its soundness and
completeness follow directly from the four-provider characterization, and it
independently reproduces the `R=3` and `R=4` SAT/UNSAT boundary.  The two
encodings therefore provide useful protection against a shared
implementation error.

## 4. Proof-producing `R=4` computation

For `R=4,n=12`, the generator reports

```text
variables=6762 clauses=121548 cells=11 targets=30
```

Kissat returned UNSAT and emitted an ASCII DRAT proof.  `drat-trim` checked
the proof against the exact generated CNF and returned

```text
s VERIFIED
```

The preserved artifacts are:

* [`scratch/certificates/tri_r4_n12.cnf.gz`](scratch/certificates/tri_r4_n12.cnf.gz)
* [`scratch/certificates/tri_r4_n12.drat.gz`](scratch/certificates/tri_r4_n12.drat.gz)
* [`scratch/certificates/tri_r4_n12_dratcheck.log`](scratch/certificates/tri_r4_n12_dratcheck.log)
* [`scratch/certificates/tri_r4_n13.model`](scratch/certificates/tri_r4_n13.model)
* [`scratch/certificates/tri_r4_n13.txt`](scratch/certificates/tri_r4_n13.txt)

Their SHA-256 values are recorded in the certificate manifest below.  The
UNSAT proof supplies the lower bound `rho(4)>=2`; the independently checked
length-13 word supplies `rho(4)<=2`, proving (1.1).

[`scratch/certificates/TRIANGULAR_NFA_MANIFEST.sha256`](scratch/certificates/TRIANGULAR_NFA_MANIFEST.sha256)

## 5. Scope

This is an exact solver for the triangular auxiliary problem, not for the
original `k`-bit OR problem.  Its mathematical value is that small optimal
cores constrain and test the proposed fold recurrence.  A SAT result gives a
fully explicit word; an UNSAT result is promoted to a theorem only after its
proof trace is independently checked.

The two `decode` modes only extract the word variables from a reported SAT
assignment; they are not independent model checkers.  For the certified
`R=4` result, the complete stored model was separately checked against every
regenerated clause, and the decoded word was separately checked by exhaustive
interval enumeration.  These checks are documented in
`TRIANGULAR_SAT_AUDIT.md`.
