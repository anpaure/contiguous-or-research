# Audit of the long-run prerequisites for fractional global sharing

## Verdict

The canonical move-to-front factorization, its one-entry continuation, the
radius-`d` symmetric chain, and the `2d+2` initialization bound are
correct.  The Goddyn--Gvozdjak long-run theorem also supplies the required
long nonrepeating Gray-code blocks, after the harmless replacement of the
displayed real-valued `H` by an integer floor.

There is one scope error in the submitted Section 1:

> Two-sided `d`-buffering by itself does **not** imply the full Pascal-strip
> incidence law
> `A_t^u subseteq A_s^v iff 0 <= s-t <= v-u`.

That law needs the additional long-run/nonrepetition hypothesis on the whole
block.  The Gray-code atoms used later do have such an additional hypothesis,
so this is repairable and does not invalidate the fractional incidence
ledger.

## 1. Exact MTF transition: pass

The precise hypotheses and construction are at
`GLOBAL_LONG_RUN_MTF_ATOMS.md`, lines 71--170.  With

\[
 F_t=\{p_t,\ldots,p_{t+d-1}\},\qquad L_t=S_t\setminus F_t,
\]

direct calculation gives

\[
 L_{t+1}=(L_t\setminus\{p_{t+d}\})\cup\{q_t\}.
\]

Consequently updating the state

\[
 (L_t,p_{t+d-1},\ldots,p_t,p_{t-1},\ldots,p_{t-d},\mathcal R_t)
\]

by the single nonempty mask `L_(t+1)` leaves the blocks in exactly the
order required at time `t+1`.  The prefix unions before the tail are the
displayed saturated chain from rank `m-d` through rank `m+d`.

Putting all remaining coordinates into one tail block gives at most
`1+d+d+1=2d+2` blocks.  Writing these blocks in reverse initializes the
state in that many array entries.  Each subsequent MTF update is one array
entry.  This agrees with the exact MTF convention in
`GLOBAL_MTF_SCD_HANDOFF.md`, lines 20--44 and 74--104.

## 2. Long-run Gray-code prerequisite: pass with rounding

Goddyn and Gvozdjak, *Binary Gray Codes with Long Bit Runs*, EJC 10 (2003),
R27, prove the existence of a cyclic `m`-bit Gray code in which the same
transition direction does not recur within at least
`m-3 log_2(m)` steps.  The primary source is
<https://doi.org/10.37236/1720>.

In the all-split orientation cube, each flip is a Johnson move.  If

\[
 H+h\le \rho,
\]

then the same block of `H` starts is valid for every radius `d<=h`.
Thus one may take, for example,

\[
 H=\left\lfloor m-3\log_2m\right\rfloor-h,
\]

which is `(1-o(1))m` for
`h=ceil(sqrt(m log m))` and satisfies `h/H=o(1)`.  The submitted
formula without a floor is not literally an integer length, but this has no
asymptotic effect.

## 3. First false implication: buffering does not imply the Pascal law

Take the standard cyclic Gray four-cycle in `Q_2`, with transition
directions

\[
 \ldots,1,0,1,0,1,0,\ldots
\]

and radius `d=1`.  At every one of its four starts:

* the current and next departure coordinates are distinct members of the
  current middle set; and
* the previous departure coordinate is absent.

Hence every start is two-sided 1-buffered and the MTF theorem applies.
Nevertheless, with pair coordinates written as `(direction,orientation)`,

\[
 A_2^{-1}=\{(1,1)\}
 \subset
 A_0^{1}=\{(0,0),(1,0),(1,1)\},
\]

whereas the proposed criterion would require
`0 <= 0-2 <= 1-(-1)`, whose first inequality is false.  The repeated
transition direction creates the extra containment.

The executable certificate is
`scratch/check_long_residence_pascal_scope.py`.  It checks every local
buffer condition and the contradicting containment.

The proof of the Pascal law in `GLOBAL_MTF_ATOM_INTEGRALITY.md`, lines
130--189, explicitly assumes transition directions are distinct throughout
the block and its halos.  Accordingly, the submitted statement should first
introduce the long-run block hypothesis, and only then assert the incidence
law.  Merely citing the local factorization lemma is insufficient.

## 4. Consequence for the submitted global theorem

This scope correction is not a counterexample to the later fractional
construction: those atoms are selected from a long-run Gray cycle with
`H+d<=rho`.  It does mean that the first Section 1 deduction is not valid
as written, and the exact amount of nonrepetition used by the incidence-law
proof should be stated rather than conflated with two-sided buffering.

