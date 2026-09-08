# The base Tamari associator transports one inverse slot but not its companion edge

## Status

The port-restored four-row Tamari trade changes the internal orders of four
shortest wreaths.  This note computes its native inverse-pair graph exactly.
On both sides, among the four named rows, the only native inverse-pair edge
is `A--L`.  The trade moves that edge to a different separated-double-swap
slot; it does not replace it by an edge incident with `C` or `D`.

Thus the phase-switched companion-generation theorem remains correct as an
abstract interface, but the present four-row packet does not by itself
supply two different companion matchings.  It is a **slot transporter on one
companion edge**, not a companion-graph switch.

No computation or search is used.

## 1. Cyclic orders

For a complement geodesic with deletion order `d_1,...,d_4` and insertion
order `e_1,...,e_4`, use the cyclic owner order

\[
              (d_1,d_2,d_3,d_4,e_1,e_2,e_3,e_4,\infty).
\tag{1.1}
\]

The negative packet gives

\[
\begin{array}{c|c}
A^-&(5,2,1,6,4,7,3,8,\infty)\\
L^-&(4,5,2,1,8,6,7,3,\infty)\\
C^-&(5,7,2,1,4,8,6,3,\infty)\\
D^-&(2,3,1,7,4,8,6,5,\infty),
\end{array}
\tag{1.2}
\]

and the port-restored packet gives

\[
\begin{array}{c|c}
A^*&(6,5,2,1,8,4,7,3,\infty)\\
L^*&(5,4,2,1,6,8,7,3,\infty)\\
C^*&(5,2,7,1,4,6,8,3,\infty)\\
D^*&(2,1,3,7,4,6,8,5,\infty).
\end{array}
\tag{1.3}
\]

These lists follow by subtracting consecutive states in the two displayed
geodesic tables.

## 2. Exact companion criterion

At semilength four a native inverse pair has, after a common cyclic cut and
choice of orientation, the form

\[
\begin{aligned}
 r_0&=(a,b,X,c,d,Y),\\
 r_1&=(b,d,X,a,c,Y),
\end{aligned}
\qquad |X|=2,\quad |Y|=3.
\tag{2.1}
\]

In particular the two aligned orders agree in five positions.  Therefore a
pair whose maximum positional agreement over all rotations and reversals is
at most four cannot be a native inverse pair.

For the six unordered row pairs, direct comparison of (1.2)--(1.3) gives

\[
\begin{array}{c|rrrrrr}
 &AL&AC&AD&LC&LD&CD\\ \hline
\mathcal P^-&5&3&3&4&2&4\\
\mathcal P^*&5&3&3&4&3&4.
\end{array}
\tag{2.2}
\]

One compact way to check the table is this.  If `p_R(x)` is the position of
label `x` in row `R`, the largest agreement under rotations is the largest
multiplicity of `p_S(x)-p_R(x) mod 9`; under reflections it is the largest
multiplicity of `p_S(x)+p_R(x) mod 9`.  Reading the nine positions in
(1.2)--(1.3) gives (2.2) literally.

Thus only `A,L` can be companions.  They really are companions, as the
following normal forms show.

In the negative phase, after cyclic alignment,

\[
\begin{aligned}
 L^-&=(8,6,73,\infty,4,521),\\
 A^-&=(6,4,73,8,\infty,521),
\end{aligned}
\tag{2.3}
\]

which is (2.1) with
`(a,b,c,d,X,Y)=(8,6,infinity,4,73,521)`.
In the restored phase,

\[
\begin{aligned}
 A^*&=(6,5,21,8,4,73\infty),\\
 L^*&=(5,4,21,6,8,73\infty),
\end{aligned}
\tag{2.4}
\]

which is (2.1) with `(a,b,c,d,X,Y)=(6,5,8,4,21,73infinity)`.

### Theorem 2.1 (companion edge is preserved, slot is changed)

The native companion graph induced by the four packet rows is

\[
                         A\mathbin{-}L
\tag{2.5}
\]

in both phases, with `C,D` isolated.  The literal inverse slot on `A--L`
changes from (2.3) to (2.4).

#### Proof

Equation (2.2) excludes every edge except `A--L`, and (2.3)--(2.4) verify
that edge in both phases.  Their active labels and their ordered `X,Y`
banks differ, so the slots are distinct. \(\square\)

## 3. Tensor and phase-switched scope

Appending the common complement-geodesic tail fixes the tail exchange
tokens row by row.  It therefore preserves the distinction in Theorem 2.1:
the tensor transports the displayed inverse slot on the same two tracked
rows, while the four-row base action supplies no new companion edge among
`A,L,C,D`.

Consequently the connected-union hypothesis in
`MATH_THEOREM_PHASE_SWITCHED_COMPANION_MATCHINGS_SUFFICE_20260806.md` cannot
be discharged by repeatedly citing this one packet.  A valid application
must add at least one of:

1. another associator whose relabelled row identification creates a
   genuinely different companion edge;
2. external helper rows which are companions of `C` or `D` in another
   phase; or
3. a larger exact trade which switches the companion graph itself.

The present packet remains dynamically useful: it proves literal birth of
a different inverse slot on an already existing edge.  What it does not
prove is moving-companion connectivity.
