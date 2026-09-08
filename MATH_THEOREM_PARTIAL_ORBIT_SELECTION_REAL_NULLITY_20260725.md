# Partial prime-orbit selection: exact count equations and the real-nullity gate

Date: 2026-07-25

Method: pure mathematics only.

## 1. Exact selection variables

Let `p=2m+1` be prime, let `sigma` be a coordinate `p`-cycle, and let `F`
be an exact middle factor.  For every base row `C in F` and phase
`a in F_p`, let

\[
                         x_{C,a}\in\{0,1\}                    \tag{1.1}
\]

record whether `sigma^a C` is selected from the `p`-fold orbit closure
`union_a sigma^aF`.  Put

\[
                         r_C=\sum_a x_{C,a}.                   \tag{1.2}
\]

For a middle necklace `O`, retain the phase signature
`P_(C,O) subseteq F_p` and let

\[
                         B(O,C)=|P_{C,O}|.                    \tag{1.3}
\]

Every row and every necklace has total multiplicity `p`, so `B` is a
square nonnegative integer matrix with

\[
                         B\mathbf1=p\mathbf1,qquad
                         \mathbf1^TB=p\mathbf1^T.             \tag{1.4}
\]

### Theorem 1.1 (exact middle constraints)

The selected rows form an exact middle factor if and only if, for every
middle necklace `O` and phase `t`,

\[
 \boxed{
 \sum_{C,a}x_{C,a}{\bf1}_{P_{C,O}+a}(t)=1.}                  \tag{1.5}
\]

Consequently every exact selection satisfies

\[
 \boxed{
 Br=p\mathbf1,qquad B(r-\mathbf1)=0,qquad
 \sum_Cr_C=|F|.}                                              \tag{1.6}
\]

#### Proof

Equation (1.5) says exactly that every physical member of every necklace
has one selected owner.  Sum it over `t` to obtain `Br=p1`; subtract
(1.4).  Left-multiply by `1^T` and use (1.4) again to get the final
identity. \(\square\)

Thus partial-orbit selection changes the row-count vector only through
the **ordinary real kernel** of `B`.  In particular,

\[
                         \det B\ne0\quad\Longrightarrow\quad r=\mathbf1.
                                                                  \tag{1.7}
\]

In that case exactly one shift of every base row is selected and the
problem collapses to the row-power phase lift.  Real nullity is only a
first gate: one also needs a bounded integral kernel vector with
`0<=1+v_C<=p`, and then the phase equations (1.5).  The projected flow
equation `Br=p1` is necessary but not sufficient.

The existing finite-field rank certificate is already enough to force
`r=1` in the exact problem.

### Corollary 1.2 (maximal `p`-rank kills mixed orbit counts)

If

\[
                         \ker_{\mathbb F_p}B=\langle\mathbf1\rangle,
                                                                  \tag{1.8}
\]

then every exact partial-orbit selection has `r=1`.

#### Proof

Reduce `Br=p1` modulo `p`.  Condition (1.8) gives
`r_C congruent c (mod p)` for every `C`.  Since `0<=r_C<=p`, if
`1<=c<=p-1` then every `r_C=c`; the identity `sum r_C=|F|` forces
`c=1`.  If `c=0`, every `r_C` is zero or `p`, so their sum is divisible
by `p`.  This is impossible because

\[
                         |F|=\operatorname {Cat}_m\equiv\pm2\pmod p.
\]

Thus only `r=1` remains. \(\square\)

Consequently partial-orbit selection and one-shift-per-row phase lifting
share the same first phase-free gate.  Mixed counts can help only on a
cycle whose multiplicity matrix has extra `p`-nullity (or after a leave,
where the corresponding rectangular boundary kernel appears).

## 2. Orbit mass is no longer frozen when the count moves

For a depth-`q` target necklace `Rhat`, let

\[
 a_{C,q}(\widehat R)
 =\#\{S\in\widehat R:S\hbox{ is a depth-}q\hbox{ interval of }C\}.
                                                                  \tag{2.1}
\]

This contribution is unchanged when `C` is shifted.  Hence the selected
factor has orbit mass

\[
 \boxed{
 M_q(\widehat R)=\sum_Cr_Ca_{C,q}(\widehat R).}               \tag{2.2}
\]

The one-shift-per-row lift has `r=1` and freezes (2.2).  Partial-orbit
selection can move it precisely through vectors

\[
                         v=r-\mathbf1\in\ker_{\mathbb R}B,     \tag{2.3}
\]

subject to integrality, box constraints, and (1.5).  Even nonzero real
nullity is useless if all lower orbit-signature vectors `a_(.,q)`
annihilate that kernel.

The extreme choices have familiar meanings:

* `r=1` is the rigid phase-lift architecture;
* `r_C in {0,p}` is a union of full translate decks and requires the
  selected row neighborhoods to partition the middle necklace vertices.

Mixed integer points interpolate between them, but their existence and
lower-shadow range are unproved.

## 3. Exact mean real-Gram identity

The zero-frequency matrix itself has an exact prime-cycle average.

### Theorem 3.1

For a uniformly random coordinate `p`-cycle,

\[
 \boxed{
 \mathbb E_\sigma B_\sigma^*B_\sigma
 =pI+{p^2(p-1)\over W}J.}                                    \tag{3.1}
\]

Thus the mean squared action is `p` on `1^perp` and `p^2` on the
constant line.

#### Proof

Expanding a Gram entry over physical middle sets gives the kernel

\[
 I+(p-1){\cal K}_p,
\]

where `cal K_p` is the normalized class sum of coordinate `p`-cycles.
On the middle Johnson module

\[
                         {\cal K}_p=\Pi_0-{1\over p-1}\Pi_1.
\]

Each wreath-row indicator has zero `Pi_1` component and mass `p`, while
distinct factor rows have disjoint supports.  Hence the diagonal Gram
entry has mean `p+(p-1)p^2/W` and every off-diagonal entry has mean
`(p-1)p^2/W`, proving (3.1). \(\square\)

Equation (3.1) excludes a fixed universal real-kernel direction but does
not prove that one cycle has nonsingular `B_sigma`: a cycle-dependent
kernel can rotate just as in the nonzero-frequency Fourier problem.  The
exact next question for this architecture is therefore a determinant or
smallest-singular-value theorem for `B_sigma`, followed--if singularity
does occur--by the bounded integral and phase-completion gates above.

## 4. The real-nullity gate collapses to the old `p`-rank gate

In the present Catalan instance the bounded integral condition is strong
enough to remove a possible ambiguity in Section 1.  Put

\[
 T=|F|={1\over p}\binom p m=C_m,
 \qquad p=2m+1.
\]

For prime `p`, the standard binomial congruence gives

\[
 \boxed{T\equiv 2(-1)^m\pmod p,}
 \tag{4.1}
\]

so in particular `p` does not divide `T`.

### Theorem 4.1 (maximal `p`-rank forces one translate per row)

Suppose

\[
 \ker_{\mathbb F_p}B=\langle\mathbf1\rangle.
 \tag{4.2}
\]

If `r in {0,1,...,p}^T` satisfies `Br=p1`, then

\[
 \boxed{r=\mathbf1.}
 \tag{4.3}
\]

Consequently every exact selection from the `p`-fold translate closure
selects exactly one translate of each original row and is already a
row-power phase lift.

#### Proof

Reduce `Br=p1` modulo `p`.  By (4.2),

\[
                         r\equiv c\mathbf1\pmod p
\tag{4.4}
\]

for some `c in F_p`.  Also `sum_C r_C=T` by Theorem 1.1.

If `1<=c<=p-1`, the interval `0<=r_C<=p` contains only the representative
`c` of that residue, so every `r_C=c`; the sum equation and `T>0` force
`c=1`.  If `c=0`, every `r_C` is either zero or `p`, so `sum_Cr_C` is
divisible by `p`, contradicting (4.1).  This proves (4.3). \(\square\)

Thus **partial-orbit selection and row-power selection have the same first
linear gate**.  Extra real nullity by itself is irrelevant: a usable
bounded integral multiplicity change forces extra modular nullity.

### Theorem 4.2 (maximal `p`-rank also implies real nonsingularity)

Let `A` be any `b by b` integer matrix with

\[
 A\mathbf1=p\mathbf1,
 \qquad \mathbf1^TA=p\mathbf1^T,
 \qquad p\nmid b.
\tag{4.5}
\]

If `rank_(F_p) A=b-1`, then

\[
 \boxed{\det A\ne0.}
\tag{4.6}
\]

More precisely, if `kappa` is any nonzero cofactor of `A modulo p`, then

\[
 \boxed{{\det A\over p}\equiv b\,\kappa\pmod p,}
\tag{4.7}
\]

after choosing the common cofactor sign so that
`adj(A)=kappa J modulo p`.  In particular `v_p(det A)=1`.

#### Proof

Modulo `p`, both the right and left kernels are the constant line, hence

\[
                         \operatorname{adj}(A)\equiv\kappa J\pmod p
\tag{4.8}
\]

with `kappa ne0`.  Since `A1=p1`, the adjugate identity gives

\[
 p\,\operatorname{adj}(A)\mathbf1=(\det A)\mathbf1.
\tag{4.9}
\]

The determinant is divisible by `p`, and summing the coordinates in
(4.9) yields

\[
 b\,{\det A\over p}
 =\mathbf1^T\operatorname{adj}(A)\mathbf1
 \equiv \kappa b^2\pmod p.
\tag{4.10}
\]

Cancel `b` modulo `p`.  Equation (4.7) follows and is nonzero. \(\square\)

Applied to the full Catalan matrix `B`, Theorem 4.2 shows that the old
maximal-`p`-rank certificate is strictly stronger than the proposed real
determinant gate.  Conversely,

\[
 \boxed{\det B=0\quad\Longrightarrow\quad
        \dim_{\mathbb F_p}\ker B\ge2.}
\tag{4.11}
\]

Therefore a genuinely new partial-orbit factor can exist only on one of
the same exceptional cycles that already has a nonconstant first-order
row-power direction.  It must then pass two additional filters: lift that
modular direction to a bounded integer count vector, and solve the
nonzero-frequency phase equations.

## 5. Every multiplicity change is a modular stopping set

Assume for clarity that the favorable cycle is transversal on the rows in
question, so `B` is the `0-1` biadjacency matrix of a `p`-regular bipartite
graph.  Let an exact partial-orbit selection have count vector `r`, and put

\[
S=\{C:r_C\ne1\}.
\tag{5.1}
\]

Before using the graph structure, the integer equation has an exact
positive-circuit normal form.  Let `b_C` denote column `C` of `B`.

### Proposition 5.0 (unit-negative column trade)

A nontrivial vector `r in {0,...,p}^T` satisfies `Br=p1` if and only if
there are disjoint nonempty row families `P,N` and integers
`a_C in {1,...,p-1}` for `C in P` such that

\[
 \boxed{
 \sum_{D\in N}b_D=\sum_{C\in P}a_Cb_C,
 \qquad
 |N|=\sum_{C\in P}a_C.}
\tag{5.1a}
\]

The corresponding counts are

\[
 r_D=0\ (D\in N),
 \qquad r_C=1+a_C\ (C\in P),
 \qquad r_E=1\ \hbox{otherwise}.
\tag{5.1b}
\]

#### Proof

Put `v=r-1`.  Its negative coordinates are necessarily exactly `-1`,
its positive coordinates are the `a_C`, and `Bv=0` is the first equality
in (5.1a).  Since every column has sum `p`, summing that equality gives
the second.  The converse is immediate. \(\square\)

Thus real singularity is much weaker than a usable partial-orbit
direction.  The kernel must contain an **oriented integral circuit whose
entire negative side has unit coefficients** and whose positive
coefficients are at most `p-1`.  Equivalently, two disjoint equal-size
multisets of row incidence columns have the same necklace degree vector.
The nonzero-frequency equations must then refine this coarse multiset
trade phase by phase.

### Proposition 5.1 (unique-neighbor obstruction)

If `r ne1`, then every necklace adjacent to `S` has at least two neighbors
in `S`.  In particular `S` is a stopping set in the row--necklace graph.

#### Proof

The vector `v=r-1` satisfies `Bv=0` over the integers.  Its reduction
modulo `p` has support exactly `S`: for `-1<=v_C<=p-1`, the only zero
residue is `v_C=0`.  A necklace with a unique neighbor `C` in `S` would
give the nonzero equation `v_C=0` modulo `p`, a contradiction. \(\square\)

Thus a unique-neighbor expansion theorem would rule out partial-orbit
changes without any determinant calculation.  There is also a useful
pair-codegree consequence.

### Corollary 5.2 (support lower bound from pair codegrees)

If every two row vertices have at most `L` common necklace neighbors, then
every nontrivial exact partial-orbit selection changes at least

\[
                         \boxed{|S|\ge2\left\lceil{p\over L}\right\rceil}
\tag{5.2}
\]

rows.  In particular a linear (`L=1`) favorable core has no multiplicity
change supported on fewer than `2p` rows.

#### Proof

Write

\[
 P=\{C:r_C>1\},
 \qquad N=\{C:r_C=0\}.
\tag{5.3}
\]

These sets partition `S`, because `v=r-1` has negative entries exactly
`-1`.  Fix `D in N`.  Every one of its `p` necklace neighbors must also
contain a row from `P`, or the equation `sum_C B(O,C)v_C=0` would have a
strictly negative left side.  One positive row can meet `D` in at most
`L` necklaces, hence

\[
                         |P|\ge\left\lceil{p\over L}\right\rceil.
\tag{5.4}
\]

The identity `sum_Cv_C=0` gives

\[
 |N|=\sum_{C\in P}(r_C-1)\ge|P|.
\tag{5.5}
\]

Therefore `|S|=|P|+|N|>=2|P|`, proving (5.2). \(\square\)

If `a=max_C(r_C-1)>0`, the same count at a row attaining `a` is sharper:
each of its `p` necklaces needs at least `a` negative-row incidences, while
one negative row can meet it at most `L` times.  Hence

\[
 |N|\ge\left\lceil{ap\over L}\right\rceil,
 \qquad
 \boxed{|S|\ge
 \left\lceil{p\over L}\right\rceil+
 \left\lceil{p(r_{\max}-1)\over L}\right\rceil.}
\tag{5.5a}
\]

Thus a row used with high multiplicity forces a quadratically larger local
support when `L=1`; for example `r_max=p` forces at least `p^2` changed
rows.  This remains polynomial and so does not settle the macroscopic
case.

For comparison, an arbitrary nonconstant modular kernel vector, without
the bounded count-vector sign pattern, only gives the weaker estimate
`|S|>=1+p/L` by the pair-collision argument of Proposition 19.5.

This is the strongest conclusion available from the maximum pair
codegree and the sign pattern alone.  It does **not** imply that all
multiplicity changes lie in a polynomial leave.  Even when `L=1`, the
bound is only `2p`, whereas `T=C_m` is exponential; and the entire row
side is a stopping set in every regular graph.  Ruling out a macroscopic
support therefore requires an algebraic maximal-rank or dense-vector
anticoncentration theorem, not a local pair-codegree estimate.

There is a residue-wise strengthening which is sometimes useful in such
an expansion argument.  For every `c in F_p`, put

\[
 S_c=\{C:r_C\not\equiv c\pmod p\}.
\tag{5.6}
\]

Since `r-c1 lies in ker_(F_p)B`, every nonempty `S_c` is a stopping set.
Thus if the incidence graph has no stopping set of size at most `s`, then
every residue class occupied by `r` has complement larger than `s`.
This gives a whole family of forbidden cuts, but still no upper bound on
their sizes; a macroscopic stopping set remains compatible with every
local estimate above.

In fact an all-scale unique-neighbor theorem is combinatorially
impossible.  If `S` has complement of size at most `p-2`, then every
necklace has at least

\[
                         p-|S^c|\ge2
\]

neighbors in `S`; hence `S` is automatically a stopping set.  The exact
division of labor is therefore:

* unique-neighbor expansion and pair codegrees can eliminate sparse
  modular kernels;
* dense kernels must be excluded by coefficient cancellation, a
  determinant/arborescence theorem, or a genuine dense-vector
  anticoncentration estimate.

This is why (5.2) does not turn mixed counts into a polynomial-leave
phenomenon.

The bound is sharp under all the local hypotheses above.  Indeed, take
the incidence matrix between points of `F_p^2` and nonvertical affine
lines.  It is square, `p`-regular and has pair codegree one, while two
vertical fibers `V_0,V_1` each meet every row once.  Hence

\[
 B(\mathbf1_{V_0}-\mathbf1_{V_1})=0,
 \qquad
 r=\mathbf1+\mathbf1_{V_0}-\mathbf1_{V_1}
\tag{5.7}
\]

is a mixed count supported on exactly `2p` columns.  By padding with
projective-plane incidence blocks with a perfect matching deleted, and
using zero-coefficient two-switches, one obtains a connected linear
`p`-regular example of the exact Catalan side size `T=C_m`; the full
construction is Theorem 32.1 of the prime-cycle rigidity file.  Thus the
coordinate-wreath origin of `B_sigma`, not its local incidence parameters,
must supply any stronger rigidity theorem.

Moreover equality in (5.2) at `L=1` is rigid: it forces `p` omitted rows,
`p` doubled rows, and exactly one distinct common necklace for every
omitted--doubled pair.  Thus the changed subgraph is the subdivision of a
`K_(p,p)`.  This follows by equality in the two counts in Corollary 5.2;
the detailed proof is Theorem 32.3 of the prime-cycle rigidity file.  The
affine vertical-fiber example realizes precisely this collision grid.
