# Finite endpoint-rotation seam trades at `m=10,11`

**Date:** 2026-08-13  
**Status:** candidate relative-incidence pattern, verified at `m=10,11` but
not yet a uniform theorem.  A first attempted symbolic root-family proof fails
at `m=12`; the exact stable path formula remains open.  The finite pattern does
not by itself prove that the changed factor rows admit the required
positive-resident chronology.

## 1. Host and notation

Let `m\in\{10,11\}`, `n=2m+1`, and let `F_m` be the complete offset-zero
first-aligned MSW packet factor.  For each rank-`m` facet `L`, write

\[
                         e_0(L)=\{P_L,V_L\}               \tag{1.1}
\]

for its two incident rank-`m+1` owners in `F_m`.  We use the endpoint-
rotation convention of
`MATH_THEOREM_ENDPOINT_ROTATION_RELATIVE_TRADE_AND_UPPER_SUPPORT_MONOTONE_M7_M8_20260813.md`:
an old coloured edge `\{P,V\}` may be changed to `\{P,W\}` whenever
`P,V,W` contain the same facet `L`.

Put

\[
\begin{aligned}
C&=C_4, & U&=U_5, & L_0&=C\cap U,\\
A&=L_0\cup\{2m-3\},& B&=L_0\cup\{2m-5\}.
\end{aligned}                                             \tag{1.2}
\]

For `m=10,11`, the old seam-colour edge is `\{A,B\}` and the desired one
is `\{C,U\}`.  This endpoint formula is not asserted beyond those two
dimensions.

For a set `X`, let `X-x+y=(X\setminus\{x\})\cup\{y\}`.  Define the
moving-owner paths

\[
\begin{array}{c|ccccc}
\text{path }\mathcal P&-(2m-4)+3&-5+2&-(2m)+(2m-4)&-3+(2m-3)&-2+(2m)\\
\hline
&C=P_0&P_1&P_2&P_3&P_4&A=P_5
\end{array}                                                \tag{1.3}
\]

and

\[
\begin{array}{c|ccc}
\text{path }\mathcal Q&-(2m-2)+(2m-9)&-10+(2m-5)&-(2m-9)+(2m-2)\\
\hline
&U=Q_0&Q_1&Q_2&B=Q_3.
\end{array}                                                \tag{1.4}
\]

Thus each table entry is the exchange producing the next owner.

For the repair circuit, put

\[
 E_m=\{16,18,\ldots,2m-4\}                                \tag{1.5}
\]

(empty at `m=9`, though the finite result starts at `m=10`) and define the lift

\[
 \lambda_m(X)=
 (X\cap\{0,\ldots,14\})\cup E_m
 \cup\{2m-3:15\in X\}
 \cup\{2m-2:16\in X\}
 \cup\{2m-1:17\in X\}
 \cup\{2m:18\in X\}.                                    \tag{1.6}
\]

Let `R_0,...,R_6=R_0` be the lifts under `(1.6)` of

\[
\begin{array}{c|l}
0&2689(10)(12)(14)(15)(16)(17)\\
1&26789(10)(12)(14)(15)(16)\\
2&026789(12)(14)(15)(16)\\
3&012679(12)(14)(15)(16)\\
4&01269(10)(12)(14)(15)(16)\\
5&0269(10)(12)(14)(15)(16)(17)\\
6&2689(10)(12)(14)(15)(16)(17).
\end{array}                                               \tag{1.7}
\]

Parenthesized entries in `(1.7)` are single labels; the compressed notation
is only to keep the table on one page.

## 2. Literal factor membership

### Lemma 2.1 (finite verified membership)

For `m=10,11`:

1. the old edge of `L_0` in `F_m` is `\{A,B\}`;
2. for every step `X->Y` of `\mathcal P`, `\mathcal Q`, or the closed walk
   `R_0->...->R_6=R_0`, the facet `X\cap Y` has `X` as one endpoint of its
   old edge in `F_m`;
3. all fourteen step facets and `L_0` are pairwise distinct.

#### Proof

Reconstruct the complete first-aligned factor from the canonical MSW flip
recursion.  The eight path steps occur in positive packet rows whose roots
at `m=10` and `m=11` are given by the corresponding specializations of

\[
\begin{aligned}
101110011100(10)^{m-8}00,&\quad
101111011100(10)^{m-9}0000,\\
101100111100(10)^{m-9}0010,&\quad
111001001100(10)^{m-9}1010,\\
111111000001(01)^{m-9}0010,&\quad
101111000110(10)^{m-8}00,\\
101111000110011(01)^{m-11}(10)00,&\quad
101111000111(01)^{m-10}00011000,
\end{aligned}                                             \tag{2.1}
\]

with the displayed `1100` block replaced by `1010` for its negative mate.
Direct evaluation of `rho` puts the consecutive owners `(1.3)-(1.4)` at
the indicated cyclic positions in those two dimensions.  These displayed
expressions are an interpolation of the two finite rows, not a claimed
all-`m` root identity.

For the six repair steps, four are unchanged canonical rows and two are
positive first-aligned rows.  Direct reconstruction at `m=10,11` gives
the following interpolating root formulas:

\[
\begin{aligned}
110111010001(01)^{m-9}0010,&
110111000011(01)^{m-9}0010,\\
111111000001(01)^{m-9}0010,&
111001110001(01)^{m-9}0010,\\
111001011001(01)^{m-9}0010,&
110111011001(01)^{m-9}0000.
\end{aligned}                                             \tag{2.2}
\]

Again the flip recursion gives exactly the lifted old edges of `(1.7)` at
`m=10,11`.
All claimed facets are then the displayed consecutive intersections.
Their symmetric differences, together with their distinct exceptional
markers, prove pairwise distinctness.  The same calculation at `L_0`
gives its endpoints `A,B`. \(\square\)

## 3. Exact relative trade

At every step `X->Y`, retain the other endpoint of the old edge at
`X\cap Y` and rotate the endpoint `X` to `Y`.  At `L_0`, replace
`\{A,B\}` by `\{C,U\}`.

### Theorem 3.1 (finite seam trade at `m=10,11`)

For `m=10,11`, these fifteen facet replacements

1. preserve every rank-`m` facet exactly once;
2. preserve degree two at every rank-`m+1` owner;
3. install the compound seam `C_4-U_5`; and
4. preserve the support of the old rank-`m+2` immediate-upper load vector.

#### Proof

The open path `\mathcal P` removes one moving occurrence of `C` and creates
one of `A`; `\mathcal Q` does the same from `U` to `B`.  The seam replacement
reverses precisely these two endpoint deficits.  The repair walk is closed.
Hence the moving-endpoint multiset, and therefore every owner degree, is
unchanged.  Facet exactness is termwise.

For upper support, apply the current identity

\[
 \Delta\mu^+=\sum
  \bigl(e_{P_L\cup W_L}-e_{P_L\cup V_L}\bigr).           \tag{3.1}
\]

The two seam paths plus the seam edge have one potential singleton-load
loss,

\[
 H_m=\{0,2,6,7,8,9,10,12,14\}\cup E_m
       \cup\{2m-3,2m-2\}.                                \tag{3.2}
\]

The first repair step creates `H_m`.  Every other net removed upper value
has old load at least two, and after summing `(3.1)` its final load is at
least one.  Thus
`\operatorname{supp}\mu_0^+\subseteq\operatorname{supp}\mu_1^+`.
\(\square\)

## 4. Protected portal rows

### Theorem 4.1 (selected internal portals are frozen at `m=10,11`)

Let `d` satisfy the portal deadline `m>=3d+2`.  None of the fifteen facets
in Theorem 3.1 lies on a selected positive portal row from
`MATH_THEOREM_PBBS_INTERNAL_HEIGHT_SPINE_TARGETS_HAVE_PAIRWISE_CONFORMAL_MSW_PORTALS_20260813.md`.
Hence every selected portal row, pointed source interval, and literal clean
package survives unchanged.

#### Proof

A selected positive portal row has exceptional normal form

\[
                         (2,3,E,0,1,O).                    \tag{4.1}
\]

For `m=10,11`, enumerate the unique length-`m` window at each exceptional
cut.  The calculation shows
that a changed facet containing `0` and omitting `1` would have to be
`E\cup\{0\}`, which contains `2m-1`; inspection of `(1.3)-(1.7)` excludes
that equality.  The complementary cases are separated by the ordered
exceptional markers `2,3,0,1` and the fact that the alternating tail of a
selected portal begins no earlier than the protected deadline.  Therefore
no changed facet is a portal-row facet. \(\square\)

## 5. Scope

The calculation extends the finite middle-incidence and relative upper-support
coexistence witnesses from `m=7,8` to `m=10,11`.  It is evidence for a
uniform bounded trade, but it is not that theorem: the literal second path
already changes its form at `m=12`.

It does **not** yet supply the chronology of the fifteen modified coloured
edges inside a positive-resident row/cycle system.  Nor does it install all
later seams `C_h-U_(h+1)`.  Those are the next topology/palette tasks.

The H100 verifier

* `scratch/test_uniform_endpoint_trade_formula_20260813.py`

reconstructs `F_m`, all fifteen old edges, portal avoidance, owner/facet
exactness, and the complete upper-support current.  The proof above is the
symbolic claim; finite replay is only an audit.

## 6. Postscript: the first non-stabilization and a tail-ladder pattern

At `m=12` the three-step path `(1.4)` is no longer literal.  The shortest
portal-avoiding replacement has length four, while the five-step `\mathcal P`
path remains literal.  More generally, the finite data `m=8,...,12` reveal a
parity-dependent tail ladder of length

\[
                         \left\lfloor{m-4\over2}\right\rfloor. \tag{6.1}
\]

Put `b=11` for even `m` and `b=13` for odd `m`, and
`t=floor((m-4)/2)`.  Starting at `U_5`, perform

\[
 -(2m-2)+b,\qquad -10+(b+4),\qquad
 -(b+4j)+(b+4j+8)\ (0\le j<t-3),\qquad
 -(b+4(t-3))+(2m-2).                                  \tag{6.2}
\]

For `m=10,11,12`, this exactly reproduces the literal shortest second
path.  Together with the lifted six-step repair circuit it gives respectively
fifteen, fifteen, and sixteen changed facets and preserves old upper support
in the exact H100 replay.
This is H100-verified evidence for an `O(m)` relative seam trade, not an
all-`m` theorem: a symbolic induction through the MSW flip recursion is still
missing, and an `O(m)` trade is too large if repeated independently at
`Theta(d)` seams without further sharing.
