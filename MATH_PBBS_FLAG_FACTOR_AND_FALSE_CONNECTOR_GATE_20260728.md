# The PBBS factor already carries every flag: components are cheap, residence is not

Date: 2026-07-28

Status: synthesis of previously proved PBBS lemmas with the odd-graph flag
normal form.  The flag theorem and the resulting gate separation are
unconditional; the displayed literal-word bounds retain their stated
residence hypotheses.  No PBBS Hamiltonization theorem is claimed.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 B=\frac{W}{n}=\operatorname {Cat}_m.
\]

The canonical PBBS odd-graph factor already solves the simultaneous support
problem at **every** depth.  Its step-two projected factor has at most `B`
components, and those components cost only `O(HB)` letters when opened and
collared through depth `H`.  In particular, at Gaussian depth
`H=O(\sqrt m)` the component cost is `O(W/\sqrt m)=o(W)`.

Consequently, a theorem which merely Hamiltonizes the PBBS factor is not the
missing coefficient-one theorem.  The unresolved asymptotic quantity is the
packing/transversal number of short positive coordinate runs.  In the exact
finite problem an additional independent obstruction remains: one common
owner/Hall extension of the nested flag rows.  A connector matters only when
it improves one of those two quantities.

## 1. PBBS is an all-depth flag factor

Let `f` be the canonical PBBS permutation of the `m`-sets, and let
`g=f^2`.  Along a directed `g`-cycle write

\[
 B_0,B_1,\ldots .
\]

For `q>=1`, define its depth-`q` flag occurrence by

\[
 \mathcal F_q(i)=\bigcap_{t=0}^{q}B_{i+t}.
 \tag{1.1}
\]

### Theorem 1.1 (complete PBBS flag support)

For every `1<=q<=m` and every

\[
 S\in\binom{[n]}{m-q},
\]

there is a directed `q`-edge `g`-path with intersection `S`.  Moreover its
correct-rank load obeys

\[
 1\le \#\{i:\mathcal F_q(i)=S\}
 \le \binom{2q+1}{q}.
 \tag{1.2}
\]

#### Proof

This is exactly Theorem 21.2 of
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.  Its global-maximum corridor
chooses the two-sided unmatched-mark boundary and constructs the states

\[
 B_t=S\cup
 \{C_0,\ldots,C_{q-t-1}\}\cup
 \{A_0,\ldots,A_{t-1}\},\qquad0\le t\le q.
\]

The deficit-three PBBS law gives `g(B_t)=B_(t+1)`, while the selected
`A`- and `C`-labels have empty common intersection.  Thus (1.1) equals
`S`.  The deleted label set is a `q`-subset of the `2q+1` reverse-unmatched
zeros and determines the oriented path, giving (1.2).  \(\square\)

Now complement the states:

\[
 X_i=[n]\setminus B_i\in\binom{[n]}{m+1}.
\]

Consecutive intersections of the `B_i` are complements of consecutive
unions of the `X_i`.  The complement-projected step-two identities used in
Theorems 19.1--22.2 of the PBBS note identify the intended lower owner
intersections with shifted PBBS intersections on the opposite parity and
the intended upper unions with their complements.  Hence Theorem 1.1 gives
the complete lower and upper target support required by the
erosion/dilation compiler.
In the notation of
`MATH_K15_COMPLEMENT_ANTIPODAL_MIDDLE_LEVELS_REDUCTION_20260728.md`, these
are precisely the descending odd-graph flags of Theorem 2.6, with the index
shift `mathcal F_q(i)=F_i^(q+1)`.
The turn shadow is only the first nontrivial row of this tower.

## 2. The component count is already below the coefficient-one scale

The PBBS orbit lengths are `ell*n`, with the sum of the `ell`'s equal to
`B`.  The step-two map has at most `B` cycles.  Let `c<=B` be their number.

### Theorem 2.1 (collared components cost `o(W)`)

Fix `H<m`.  Suppose first that every positive coordinate run on every
complement-projected owner cycle has length at least `H+1`.  Then there is a
literal nonzero word of length at most

\[
 W+2Hc\le W+2HB
 \tag{2.1}
\]

which realizes all PBBS lower intersections and upper unions through depth
`H`.  In particular, if `H=O(\sqrt m)`, its excess is `O(W/\sqrt m)`.

#### Proof

On a projected cycle `X_0,...,X_(L-1)`, take the cyclic `(H+1)`-fold
erosion

\[
 D_i=\bigcap_{j=0}^{H}X_{i+j}
\]

and repeat its first `2H` entries.  Coordinatewise erosion followed by
dilation represents every intersection and union of at most `H+1`
consecutive owners, including windows crossing the opened seam.  This costs
`L+2H`.  Sum over the `c` cycles and use `c<=B`.  Theorem 1.1 supplies every
intended target before literalization.  Finally

\[
 \frac{HB}{W}=\frac{H}{2m+1}=O(m^{-1/2})
\]

at Gaussian depth.  \(\square\)

For arbitrary PBBS cycles, let `nu_H(P_m)` be the maximum number of
projected-edge-disjoint positive coordinate residence intervals of length at
most `H`.  The circular interval transversal theorem and the linear
dominance-staircase seam give the already proved exact ledger

\[
 \boxed{
 L_H\le W+2HB+2(5H-1)\nu_H(P_m).}
 \tag{2.2}
\]

Equation (2.2) is equation (24.7) of the PBBS reduction, now read together with
Theorem 1.1.  It has a useful logical consequence.

### Corollary 2.2 (Hamiltonization is a false standalone gate)

An `O(B)`-switch or `O(B)`-component Hamiltonization theorem, by itself,
does not improve the sufficient bound (2.2).  Conversely, connectivity is
not needed for coefficient one: the original `c<=B` cycles already have
negligible collar cost.  A joining theorem advances the problem only if it
also proves one of the following:

1. it reduces the short-residence packing term by the required amount;
2. it supplies a common exact owner/Hall extension in the finite compiler;
3. it is flag-neutral and is part of a separate argument establishing 1 or
   2.

#### Proof

The first assertion follows because (2.2) contains the component cost only
in `2HB`; the potentially critical term is `H nu_H`.  The second assertion
is Theorem 2.1.  A pure component merge leaves all old internal short runs
in place, so no decrease of `nu_H` follows from connectivity alone.  The
finite owner/Hall condition is not implied by support of the flag rows, as
the exact `k=15` Hall-deficiency certificates demonstrate.  \(\square\)

There is a sharper statement: at the critical scale, Catalan-many local
joins cannot materially alter the residence packing number at all.

### Theorem 2.3 (seam-Lipschitz residence packing)

Let `F` and `F'` be cycle/path covers on the same owner vertices.  Suppose
`F'` is obtained from `F` by deleting a set `S_-` of `J_-` transition edges,
retaining the resulting path interiors (with either orientation), and adding
a set `S_+` of `J_+` seam edges.  For every `H`, let `nu_H(F)` denote the
maximum number of pairwise transition-edge-disjoint positive coordinate-run
intervals of length at most `H`.  Then

\[
 \boxed{|\nu_H(F')-\nu_H(F)|\le\max(J_-,J_+).}
 \tag{2.3}
\]

In particular, if `J_-=J_+=J`, the bound is `J`, independently of `H`.

#### Proof

Let `U` be the residence intervals lying wholly inside the retained path
interiors.  Reversing an interior preserves the same coordinate runs as
sets of transition edges, so `U` is a common subfamily of the old and new
interval systems.

Every old interval outside `U` contains an edge of `S_-`.  In an
edge-disjoint packing, distinct such intervals contain disjoint subsets of
`S_-`; choosing one contained deleted edge from each interval is therefore
injective.  At most `J_-` members of a packing lie outside `U`.  Hence

\[
 \nu_H(U)\le\nu_H(F)\le\nu_H(U)+J_-.
\]

The identical argument with `S_+` gives

\[
 \nu_H(U)\le\nu_H(F')\le\nu_H(U)+J_+.
\]

Subtract the two intervals.  An interval crossing several seams causes no
problem: edge-disjointness still makes the selected seam-edge charge
injective.  \(\square\)

### Corollary 2.4 (critical residence is invariant under local Hamiltonization)

Let `H_A=ceil(A sqrt(m))`.  Any sequence of switches whose total number of
deleted transition slots is `O_A(B)` satisfies

\[
 \nu_{H_A}(F')=\nu_{H_A}(F)+O_A(B)
               =\nu_{H_A}(F)+o_A(B\sqrt m).
 \tag{2.4}
\]

Therefore the critical condition

\[
 \nu_{H_A}=o_A(B\sqrt m)
\]

holds after such a Hamiltonization if and only if it held before it.  A
Catalan-size local connector atlas can preserve or expose the PBBS
residence theorem, but it cannot manufacture the missing vanishing factor
from a genuinely critical `Theta(B sqrt(m))` seed.

## 3. Exact remaining gates

The asymptotic coefficient-one route is reduced to the proved threshold

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)
   =o_A(B\sqrt m)
 \qquad\text{for every fixed }A>0,
 \tag{3.1}
\]

or to any stronger residence-clustering statement which makes the last term
of (2.2) `o(W)`.  The known height argument gives the matching-order
`O_A(B\sqrt m)` bound, so the missing improvement is genuinely a vanishing
factor.

For the exact conjecture `nu(k)=B(k)`, Theorem 1.1 removes support but not
ownership.  The `k=15` frontier already contains a one-path, depth-three
resident, upper-all-depth-complete carrier, yet its best exact compiler Hall
deficiency is positive.  Thus a PBBS connector theorem would not finish the
finite case unless its local surgery changes the trace-two owner incidence in
the required direction.

The research priorities should therefore be ordered as follows:

1. residence-improving or residence-clustering PBBS surgery;
2. trace-two/nested owner extension for the exact compiler;
3. flag-neutral connectors only as a tool for one of the preceding items;
4. pure Hamiltonization last.
