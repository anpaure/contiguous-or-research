# Audit: binary-rotor divergence and the one-sided compiler

> **Correction.**  The switch-count compatibility conclusion in Section 4
> is superseded by
> `MATH_THEOREM_BINARY_ROTOR_GLOBAL_ADJACENT_SWAP_TOLL_20260726.md`.
> Telescoping adjacent-swap support over an entire component proves
> (W\le nC+2a-2c_1).  Thus (C=o(W/m)) forces
> (a\ge(1/2-o(1))W), and the scalar condition (Ha=o(W)) is impossible
> for growing (H).  The exact divergence identity remains correct; the
> surviving requirement is signed cancellation
> \(\frac12\sum_q\|R_q-L_q\|_1=o(W)\).

Date: 2026-07-26

Audited source:
`MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md`.

## Verdict

The clustered de Bruijn reduction, the all-depth upper--lower divergence
identity, and the one-sided coefficient-one compiler are correct.  They
strictly weaken the surviving rotor gate: exact upper-prefix coverage is
unnecessary.

## 1. Clustered de Bruijn equivalence

An injective ((n-1))-word is an arc from its first (n-2) entries to
its last (n-2) entries.  Each such vertex has exactly two incoming and
two outgoing arcs.  The two outgoing choices are precisely the (A)- and
(B)-rotor successors.

All outgoing arcs of one vertex have the same middle-owner colour.  Hence
one selected arc per owner plus flow balance forces selected indegree and
outdegree to be zero or one at every vertex.  The support is therefore a
disjoint directed cycle factor.  This verifies the exact equivalence, not
merely a projection.

## 2. Divergence identity

For a selected state

\[
 e=(x_1,\ldots,x_{n-1}),
\]

let (x_n) be its missing coordinate and put

\[
 K_r(e)=\{x_{n-r+1},\ldots,x_{n-1}\}.
\]

Stationarity around the selected de Bruijn cycles identifies lower-prefix
load with the last internal (r)-block load.  A (B)-successor contributes
(K_r(e)\cup\{x_n\}), which is the complement of the corresponding upper
prefix.  An (A)-successor contributes (K_r(e)\cup\{x_1\}).  Thus

\[
 R_r-L_r=
 \sum_{e\ {m selected\ with}\ A}
 \left(
  \mathbf e_{K_r(e)\cup\{x_n\}}-
  \mathbf e_{K_r(e)\cup\{x_1\}}
 \right).
\]

If (a) (A)-arcs are selected, triangle inequality gives

\[
 \frac12\|R_r-L_r\|_1\le a,
 \qquad
 M(R_r)\le M(L_r)+a.
\]

The rank indices agree: for (r=m-q), an (r)-suffix is the complement
of a rank-((m+1+q)) prefix.

## 3. Literal compiler

With (C) support cycles and aggregate lower holes

\[
 \mathcal M_H^-=
 \sum_{q=0}^{H}M(L_{m-q}),
\]

linearizing each cycle costs \(C(m+H)\).  Appending lower holes and then
the upper holes bounded by the divergence identity gives length at most

\[
 W+C(m+H)+2\mathcal M_H^-+(H+1)a.
\]

Therefore

\[
 C=o(W/m),\qquad
 \mathcal M_H^-=o(W),\qquad
 Ha=o(W),\qquad H=o(m)
\]

are sufficient.

## 4. Former switch-toll audit (superseded as noted above)

Every pure (B)-component has (n) states.  Every (B)-run in a
non-pure component has at most (n-1) states; otherwise its selected
(A)-successor and the already-selected (B)-successor share an owner.
Consequently

\[
 W\le(n-1)a+nC,
 \qquad
 a\ge\frac{W-nC}{n-1}.
\]

When (C=o(W/m)), the necessary scale is

\[
 a\ge(1-o(1))W/(2m).
\]

For (H=\sqrt m\,\omega(m)=o(m)), this remains compatible with
(Ha=o(W)).  The exact common fractional circulation achieves
(a=W/(n-1)) and balanced lower loads at every rank.

## 5. Remaining theorem

The corrected rotor endgame is now one-sided:

\[
 \boxed{
 \begin{gathered}
 \text{choose one de Bruijn arc per middle owner, with flow balance},\\
 C=o(W/m),\qquad a=o(W/H),\\
 \sum_{q\le H}M(L_{m-q})=o(W),
 \qquad H=\sqrt m\,\omega(m)=o(m).
 \end{gathered}}
\]

The maximally uniform (B^{n-2}A) run skeleton is owner-degenerate, so
the required integral rounding must use nonuniform run lengths.  This is
the only unresolved step in this rotor architecture.
