# A four-target obstruction to the lexicographic excursion lemma

## 1. Result

Let

\[
 P_m=[0,m]^4,\qquad V_m=\{v:|v|=2m-1\},\qquad
 Z_m=\{z:|z|=2m\}.
\]

As in `CENTRAL_EULER_UPPER_UNIVERSALITY.md`, the edge below
`z in Z_m` joins the lower covers obtained by subtracting from the first
two positive coordinates of `z`.  At a degree-three vertex a transition
system pairs two incident edge half-edges and leaves the third as a trail
end; degree-two transitions are forced.

The open **Lexicographic excursion lemma**, in its stated within-one-trail
form, is false.

> **Theorem 1.**  For every `m>=2` and every transition system on the
> lexicographic selected-cover graph, at least one of the four targets
> \[
> \begin{aligned}
> Y_1&=(0,m,1,m),&Y_2&=(0,m,2,m-1),\\
> Y_3&=(1,m,0,m),&Y_4&=(1,m,1,m-1)
> \end{aligned}                                      \tag{1.1}
> \]
> has no facet-spanning restricted transition component.  Equivalently,
> it is impossible that every one of the four targets is represented by a
> maximal `Y_i`-run contained in one transition trail.

All four targets have rank `2m+1`.  The obstruction is a minimal one:
each proper three-target subfamily is compatible with some choice of the
three relevant local transitions.

This theorem does **not** disprove the width-plus-surface construction.
After the transition trails are oriented and concatenated, an interval
crossing a trail boundary can implement a missing transition virtually.
The theorem says that such a cross-trail repair is necessary: the earlier
proposal cannot be proved by finding a transition system for which every
target already works inside a trail.

## 2. Three branch vertices and nine colours

Put

\[
 a=(0,m-1,0,m),\quad
 b=(0,m-1,1,m-1),\quad
 c=(0,m,0,m-1).                                  \tag{2.1}
\]

The following middle colours will be used:

\[
\begin{array}{lll}
 x=(0,m-1,1,m), & u=(0,m,0,m), & r=(1,m-1,0,m),\\
 s=(0,m-1,2,m-1), & v=(0,m,1,m-1), & t=(1,m-1,1,m-1),\\
 &&w=(1,m,0,m-1).
\end{array}                                      \tag{2.2}
\]

All of them lie in `Z_m`.  Directly from the first-two-positive-coordinate
rule, the three incident selected edges at the branch vertices are

\[
 \begin{array}{c|c}
  \text{vertex}&\text{incident edge colours}\\ \hline
  a&x,u,r\\
  b&s,v,t\\
  c&u,v,w.
 \end{array}                                      \tag{2.3}
\]

These vertices really have degree three in the full graph.  For example,
the legal selected increments at `a` are in coordinates `1,2,3`; at `b`
they are in coordinates `1,2,3`; and at `c` they are in coordinates
`1,3,4`.  Thus a transition system may choose exactly one pair in each row
of (2.3).

## 3. The four forced clauses

Because every target in (1.1) has rank `2m+1`, its allowed middle colours
are exactly the points obtained by subtracting one unit in a positive
coordinate.  This makes each induced graph completely explicit.

For `Y_1`, its three colours form the edge path

\[
                       x\;--_a\;u\;--_c\;v.       \tag{3.1}
\]

No individual edge has maximum `Y_1`, whereas either consecutive pair
does.  Hence `Y_1` requires

\[
                 (xu)_a\quad\mathbin{\lor}\quad(uv)_c.       \tag{C1}
\]

For `Y_2`, the colours `s` and `v` meet at `b`.  Their maximum is `Y_2`.
The third colour

\[
                    (0,m,2,m-2)                    \tag{3.2}
\]

is a disjoint selected edge and misses the fourth facet.  Thus

\[
                              (sv)_b.               \tag{C2}
\]

For `Y_3`, the induced path is

\[
                       r\;--_a\;u\;--_c\;w,       \tag{3.3}
\]

and the requirement is

\[
                 (ur)_a\quad\mathbin{\lor}\quad(uw)_c.       \tag{C3}
\]

Finally, for `Y_4`, the relevant path is

\[
                       t\;--_b\;v\;--_c\;w.       \tag{3.4}
\]

The remaining colour `(1,m,1,m-2)` is a disjoint edge and misses the
fourth facet.  Therefore

\[
                 (vt)_b\quad\mathbin{\lor}\quad(vw)_c.       \tag{C4}
\]

Here `(pq)_z` means that the half-edges of colours `p,q` are paired at the
physical vertex `z`.

The descriptions above also prove necessity, not merely sufficiency.
Every component with maximum `Y_i` must join two edges supplying the two
facets which no individual edge supplies.  The displayed path contains the
only possible join.  In (3.2) and its `Y_4` analogue, the extra edge is
vertex-disjoint from that path for every `m>=2`, including the boundary
case `m=2`.

## 4. Contradiction and minimality

Clause (C2) pairs `s` with `v` at `b`.  It rules out `(vt)_b`, so (C4)
forces

\[
                              (vw)_c.               \tag{4.1}
\]

At `c`, equation (4.1) rules out both `(uv)_c` and `(uw)_c`.  Consequently
(C1) and (C3) force, respectively,

\[
                              (xu)_a,
                  \qquad     (ur)_a.                \tag{4.2}

But a degree-three transition at `a` can pair `u` with only one of `x,r`.
This proves Theorem 1.

The four clauses are minimally inconsistent.  If one clause is removed,
the following choices satisfy the other three:

\[
\begin{array}{c|ccc}
\text{omitted}&a&b&c\\ \hline
C1&(ur)&(sv)&(vw)\\
C2&(ur)&(vt)&(uv)\\
C3&(xu)&(sv)&(vw)\\
C4&(ur)&(sv)&(uv).
\end{array}                                      \tag{4.3}
\]

Unused local pairs may be chosen arbitrarily.  Thus neither two nor three
of these particular targets witness the failure.

## 5. What arbitrary trail concatenation changes

A transition component and a subarray of the final concatenated word are
different notions.  There is an exact one-seam repair of the local gadget.
Choose

\[
                       (ur)_a,\qquad(sv)_b,\qquad(uv)_c.      \tag{5.1}
\]

These transitions satisfy (C1)--(C3), while (C4) fails internally.  The
half-edge of colour `t` at `b` and the half-edge of colour `w` at `c` are
both unpaired, hence they are ends of two transition trails.  Orient the
first trail so its final edge has colour `t` and ends at `b`; orient the
second so its initial edge has colour `w` and begins at `c`; then concatenate
them in that order.  The four letters around the seam have maximum

\[
                              t\vee w=Y_4.          \tag{5.2}
\]

They are all below `Y_4`, so this crossing interval represents the one
target missing from the internal transition system.  More general seams
can likewise join suffixes and prefixes at different vertices.

Therefore Theorem 1 has the following exact consequence and no stronger
one without an additional argument:

> In every concatenation of the transition trails, at least one of the
> four targets in (1.1) must use a witness crossing a trail boundary.

It does not force an additional asymptotic cost, because the proposed
construction already has `O(m^2)` trail boundaries.  A single boundary can
repair this local four-target conflict.

This caveat is real rather than hypothetical.  For `m=2`, the checker

```text
python3 scratch/check_lex_excursion_obstruction.py
```

verifies an explicit seven-piece trail concatenation of length 26 which
covers every upper target `y in [0,2]^4`, `|y|>=4`.  One of the four
obstruction targets, `(1,2,1,1)`, has no witness internal to a piece but has
a witness crossing a piece boundary.  The same checker verifies the
all-`m` induced graphs and clauses for `2<=m<=100`; Sections 2--4 are exact
symbolic proofs for every `m`.

## 6. Corrected next target

The former open lemma should be replaced by a seam-aware statement.
A sufficient form is:

> Choose the degree-three transitions, cuts, orientations, and a linear
> order of the resulting `O(m^2)` pieces so that every upper target has a
> facet-spanning run either inside one piece or across one of the chosen
> piece boundaries.

The four-target gadget shows why the seam clause is indispensable.  It
also identifies the smallest local resource that must be budgeted: four
targets demand incompatible through-pairings, and at least one demand must
be supplied virtually by a cut and concatenation.  Any successful
recursive-facet proof must allocate and coordinate these virtual
transitions; a pure rotation system on the original graph cannot work.
