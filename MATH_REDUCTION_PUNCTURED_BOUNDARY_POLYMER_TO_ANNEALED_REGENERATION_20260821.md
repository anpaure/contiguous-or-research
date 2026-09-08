# Boundary polymers imply annealed regeneration below the square-root scale

**Date:** 2026-08-21  
**Status:** proved reduction; the boundary-codegree inequality and quenched
trajectory upgrade remain the two live inputs

## 1. Why raw factorial moments must be renormalized

Let `H_r` be the directed punctured-configuration hypergraph, let `e` be a
fixed configuration, and put `D=D_M`.  The raw conjecture

\[
 M_s(e)/D=O(C^s r^{2-s})                              \tag{1.1}
\]

is false.  The boundary `C_4` family proved in
`MATH_OBSTRUCTION_PUNCTURED_BOUNDARY_C4_BREAKS_RAW_FACTORIAL_MOMENT_HIERARCHY_20260821.md`
already gives `M_4(e)/D=Omega(1/r)`.

The square is not a global obstruction.  It is one connected polymer in a
bounded-degree graph.  This note records the correct graph-weighted
reduction.

## 2. The boundary graph and the live codegree gate

Put `b=2r+1` and identify the `b` cyclic cuts of the base word with
`Z_b`.  A retained middle window with start `i` is represented by the
boundary edge

\[
                         \{i,i+r\},                    \tag{2.1}
\]

and a retained lower window by

\[
                         \{i,i+r-1\}.                  \tag{2.2}
\]

The start `i=0` is punctured.  The resulting simple graph `B_r` has `4r`
edges and maximum degree at most four.  Multiplication by `-2` sends its
two edge families to steps `1` and `3`, with the edges `{0,1}` and `{0,3}`
deleted.

Here is a uniform density proof, including the case `3|b`.  For a proper
nonempty `S subset Z_b`, let `partial_d(S)` be the number of step-`d`
edges crossing its boundary in the full Cayley graph.  The number of full
Cayley edges induced by `S` is

`2|S|-(partial_1(S)+partial_3(S))/2`.

The step-one cycle is connected, so `partial_1(S)>=2`.  If
`partial_3(S)>0`, its parity gives `partial_3(S)>=2`.  If instead it is
zero, then `3|b` and `S` is a nontrivial union of the three residue classes
modulo three; in that case `partial_1(S)>=2b/3`.  Thus every proper `S`
induces at most `2(|S|-1)` edges.  Deleting the two punctured edges can
only decrease this number, while the full vertex set spans exactly
`2b-2`.  Consequently every subgraph with `m` edges and `v` nonisolated
vertices satisfies

\[
                         m\le2(v-1).                    \tag{2.3}
\]

For `T subseteq e`, let `B(T)` be the edge subgraph of `B_r` represented
by its targets and write `v(T)=|V(B(T))|`.

> **Boundary-codegree gate `BC(C)`.**  There is an absolute constant `C`
> such that, for every `T subseteq e` with `|T|>=2`,
> \[
>             {\deg(T)\over D}\le C^{|T|}r^{2-v(T)}.   \tag{2.4}
> \]

The exact pair table and the complete triple census satisfy (2.4).  The
critical boundary square has `|T|=v(T)=4` and
`deg(T)/D=Theta(r^-2)`, so it also satisfies (2.4) sharply.  Unlike
(1.1), the gate charges a cycle only for its distinct boundary cuts; the
cycle is then handled by the polymer enumeration below.

The intended proof of (2.4) is the exact Venn-cell formula.  Once the
positional arcs are fixed, every new distinct boundary cut refines one
factorial cell, and

\[
 {p!q!\over(p+q)!}={1\over{p+q\choose p}}.             \tag{2.5}
\]

The finite pair/triple/four-cycle calculations prove the first nontrivial
instances, but (2.4) is not claimed proved here.

## 3. A bounded-degree polymer estimate

For `z>=0`, define

\[
 {cal P}_2(z)=
 \sum_{\substack{T\subseteq E(B_r)\\|T|\ge2}}
          |T|^2 z^{|T|}r^{-v(T)}.                      \tag{3.1}
\]

### Lemma 3.1

There are absolute constants `c_0,c_1` such that, whenever
`0<=z<=c_0 sqrt(r)`,

\[
             \boxed{\quad
 {cal P}_2(z)\le c_1\left({z^2\over r^2}+{z^4\over r^2}\right).
             \quad}                                    \tag{3.2}
\]

#### Proof

Decompose a nonempty edge subgraph into its connected components.  In a
graph of maximum degree four, the number of connected `m`-edge subgraphs
containing a prescribed vertex is at most `A^m` for an absolute `A`.
Consequently the total activity of connected `m`-edge polymers is at most

\[
                       bA^m z^m r^{-v}.                \tag{3.3}
\]

For `m=1,2,3`, simplicity and the absence of triangles in the step
`{1,3}` graph for `b>=11` give respectively `v>=2,3,4`.  Indeed, three
signed steps from `{1,3}` have odd integer sum of absolute value at most
nine, so they cannot sum to zero modulo `b>=11`.  Their
activities are therefore

\[
               O(z/r),\qquad O(z^2/r^2),\qquad O(z^3/r^3).       \tag{3.4}
\]

The finitely many values `b<11` can be absorbed into the constants.  For
`m>=4`, (2.3) gives `v>=m/2+1`, so (3.3) is at most

\[
                         (Az/\sqrt r)^m.                \tag{3.5}
\]

Let `eta_j` be the sum of `m^j` times the activities of all connected
polymers, and let `eta_j^(>=2)` omit the one-edge polymers.  Equations
(3.4)--(3.5), after reducing `c_0` if necessary, give

\[
 \eta_0=O(z/r+z^4/r^2),
 \qquad
 \eta_2^{(\ge2)}=O(z^2/r^2+z^4/r^2),
 \qquad
 \eta_1=O(z/r+z^4/r^2).                                \tag{3.6}
\]

Dropping the vertex-disjointness constraint between connected components
only increases the sum.  For a subgraph with at least two edges,
`|T|^2<=2|T|(|T|-1)`.  The exponential formula with an ordered pair of
distinct marked edges therefore bounds (3.1) by

\[
 2e^{\eta_0}\left(\eta_2^{(\ge2)}+\eta_1^2\right).      \tag{3.7}
\]

Under `z<=c_0 sqrt(r)`, (3.6)--(3.7) imply (3.2).  \(\square\)

## 4. Consequence for an independent residual

Retain lower targets independently with density `x` and middle targets
independently with density

\[
                         y={rx+2\over r+2}.              \tag{4.1}
\]

conditioned on retaining a fixed edge `e`.  Let `calE_x(e)` be its expected
duplicate conflict excess, and put

\[
                         d_x=D x^{2r}y^{2r-1}.           \tag{4.2}
\]

### Theorem 4.1 (boundary polymers imply annealed regeneration)

Assume `BC(C)`.  For every fixed `alpha<1/3`, uniformly for

\[
                         r^{-\alpha}\le x\le1,           \tag{4.3}
\]

one has

\[
                    \boxed{\quad {\cal E_x(e)\over r d_x}=o(1).\quad}    \tag{4.4}
\]

#### Proof

For `t_F=|e cap F|`, put `a=x^{-1}-1`.  Exactly as in the factorial-moment
expansion,

\[
 {\cal E_x(e)\over r d_x}
 \le {y\over rDx^2}
   \sum_{s=2}^{4r}{s\choose2}a^{s-2}
       \sum_{T\in{e\choose s}}\deg(T).                 \tag{4.5}
\]

Apply (2.4), put `z=Ca`, and use `(s choose2)<=s^2/2`.  For `a>0`, the sum
in (4.5), after division by `D`, is at most

\[
 {r^2\over2a^2}{\cal P}_2(z)
 =O_C(1+a^2)                                             \tag{4.6}
\]

by Lemma 3.1.  At `a=0`, define the middle expression in (4.6) by its
continuous limit: `calP_2(Ca)` is a polynomial whose lowest power is
`a^2`.  Equivalently, only the `s=2` term remains in (4.5), and the same
bound follows directly.  The hypothesis `alpha<1/3` in particular gives
`z=o(sqrt(r))`.  Also `y/x=1+O(1/(rx))`.  Hence (4.5)--(4.6) give

\[
 {\cal E_x(e)\over r d_x}
 =O_C\!\left({1+a^2\over rx}\right)
 =O_C\!\left({1\over r x^3}\right)=o(1),               \tag{4.7}
\]

uniformly on (4.3).  \(\square\)

## 5. Exact remaining scope

The reduction leaves two explicit steps.

1. Prove the Venn-cell boundary inequality `BC(C)` uniformly through all
   target subsets.  This is a deterministic statement about two cyclic
   interval representations.
2. Upgrade the independent-residual estimate (4.4) to the residual created
   by the slow isolated-edge process.  This requires a trajectory
   martingale or coupling and is not a consequence of annealed moments
   alone.

The boundary-square obstruction shows why raw factorial moments were the
wrong variables.  Lemma 3.1 also shows that the obstruction is safely
subcritical: the connected-polymer activity is controlled whenever
`x >> r^-1/2`, and the coarser conclusion `alpha<1/3` already gives a
vanishing matching leave.
