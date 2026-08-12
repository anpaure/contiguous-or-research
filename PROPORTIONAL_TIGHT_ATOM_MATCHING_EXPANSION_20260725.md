# Proportional tight atoms: central augmentation and the exact cylinder-expansion gate

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computer experiment is used.

## 0. Outcome

This report attacks the matching lemma in
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md` positively.

The local `O(1/m)` overlap row sum and transitivity do **not**, by
themselves, justify a conventional residual-pseudorandom nibble.  The
report develops one valid positive mechanism: a nonlocal alternating
augmentation followed by an integral completion-fibre lift.

The following statements are proved.

1. Every partial atom matching satisfies exact integral multirank moment
   inequalities absent from the row-sum hypothesis.  At the two central
   ranks these inequalities form an integral hypersimplex constraint on
   the added endpoint labels.
2. The central rank-`m` to rank-`m+1` flags of any `s`-atom matching form
   an ordinary matching of size `sb` in the regular middle-incidence
   graph.  If the atom deficit is `ell>=1`, the `b` shortest alternating
   paths add one full atom's central quota while touching at most

   \[
   K(\ell)\le\left\lceil\frac{pb}{\ell}\right\rceil
   \tag{0.1}
   \]

   old atoms.
3. Every fixed ordered boundary type of the interval word contains an
   exact matching of

   \[
   F=\binom{2c}{c},
   \qquad c=m-H-b+1,
   \tag{0.2}
   \]

   atoms, indexed by their common cores.
4. Inside one boundary cylinder, strict augmentation is equivalent to the
   exact owner-neighbourhood inequality (6.3a).  The total blocker
   incidence and the resulting first-moment survivor bound are given
   exactly by (6.3c)--(6.3e).
5. The full matching lemma follows by an exact integral augmentation if,
   for the packet supplied in item 2, one boundary type retains at least
   `|J|+1` unblocked cores.  This is the explicit cylinder-fibre expansion
   inequality (FE) in Section 6.  Iteration stops with

   \[
   o(p/\sqrt m)
   \]

   missing atoms.

The remaining unproved statement for this route is (FE), or the weaker
packet-fibre matching inequality (Lift).  Initial transitivity and the
`O(1/m)` row sum do not imply a bound on this restricted completion fibre.
Thus the report does not claim the proportional matching lemma or constant
one.  It replaces the vague growing-rank nibble by one exact, bounded
nonlocal lift gate.

## 1. Exact central parameters

Retain the notation of the reduction:

\[
n=2m+1,
\qquad
W=\binom nm,
\qquad
b=\lfloor m^{3/4}\rfloor,
\qquad
p=\left\lfloor\frac Wb\right\rfloor,
\]

\[
H=\lceil\alpha\sqrt{m\log m}\rceil,
\qquad
\frac1{\sqrt2}<\alpha<\frac{\sqrt3}{2},
\]

and

\[
N_q=\binom n{m+q},
\qquad
b_q=\left\lfloor\frac{N_q}{p}\right\rfloor.
\tag{1.1}
\]

Write

\[
W=pb+\rho,
\qquad 0\le\rho<b.
\tag{1.2}
\]

### Lemma 1.1 — the two central start sets are forced

For all sufficiently large `m`,

\[
\boxed{b_0=b_1=b.}
\tag{1.3}
\]

Consequently

\[
I_0=I_1=\{0,1,\ldots,b-1\}.
\tag{1.4}
\]

#### Proof

Binomial symmetry gives `N_0=N_1=W`.  Since `p=floor(W/b)`,

\[
p\le W/b
\]

and hence `W/p>=b`.  Also

\[
p\ge W/b-1>W/(b+1)
\]

for all sufficiently large `m`, because `W>b(b+1)`.  Thus

\[
b\le W/p<b+1,
\]

which proves (1.3).  Each `I_q` is a `b_q`-subset of a `b`-set, so (1.4)
follows.  ∎

The edge rank is

\[
\kappa=\sum_{q=-H}^{H+1}b_q
=(\sqrt\pi+o(1))b\sqrt m
=\Theta(m^{5/4}).
\tag{1.5}
\]

Indeed the floor errors sum to `O(H)=o(b sqrt(m))`, while the local central
limit estimate gives

\[
\frac1{\sqrt m}\sum_{q=-H}^{H+1}\frac{N_q}{W}
\longrightarrow
\int_{-\infty}^{\infty}e^{-x^2}\,dx=\sqrt\pi.
\]

## 2. What the local row sum can and cannot drive

The reduction proves

\[
\max_{v,e\ni v}
\sum_{w\in e\setminus\{v\}}
\frac{\deg(v,w)}{\deg(v)}=O(1/m).
\tag{2.1}
\]

This controls repeated local conflicts, but it is not a hereditary
expansion statement.  The distinction can be made exact.

### Proposition 2.1 — transitive row-sum data permit a greedy jam

For every sufficiently large `m`, there is a `K`-partite, edge-transitive,
partwise vertex-transitive regular hypergraph with

\[
K=\lceil m^{5/4}\rceil
\]

and

\[
\max_{v,e\ni v}
\sum_{w\in e\setminus\{v\}}
\frac{\deg(v,w)}{\deg(v)}\le\frac1m,
\tag{2.2}
\]

yet it has a maximal matching covering exactly one half of every part.

#### Proof

Choose an odd prime `h` with

\[
m(K-1)\le h<2m(K-1),
\]

which exists by Bertrand's postulate, and put

\[
G=\mathbb Z_2\times\mathbb Z_h,
\qquad |G|=2h.
\]

Use `K` copies of `G`, indexed by

\[
\infty,0,1,\ldots,K-2.
\]

For `(r,c) in G^2`, make one edge whose entries are

\[
c\quad\text{in part }\infty,
\qquad
r+ac\quad\text{in part }a.
\tag{2.3}
\]

Every vertex has degree `2h`.  Two coordinates in distinct parts determine
at most two pairs `(r,c)`: on the `Z_h` coordinate the relevant nonzero
linear coefficient is invertible, and the kernel on the `Z_2` coordinate
has size at most two.  Hence every pair-codegree is at most two, and

\[
\sum_{w\in e\setminus\{v\}}
\frac{\deg(v,w)}{\deg(v)}
\le\frac{2(K-1)}{2h}
\le\frac1m.
\]

Translations of `(r,c)` act transitively on edges and transitively within
each part.

Now take the `h` edges

\[
r=c=(1,k),
\qquad k\in\mathbb Z_h.
\tag{2.4}
\]

They form a matching: in every slope part the second coordinate is
`(1+a)k`, and `1+a` is nonzero modulo `h`.  The unused vertices in the
`c` and `r` parts have first coordinate zero, while the unused vertices in
the `r+c` part have first coordinate one.  No edge can have all three of
these entries unused.  Thus the matching is maximal and covers exactly
half of each part.  ∎

This proposition does not say that its maximum matching is small.  It
proves the precise methodological point: transitivity, a fractional perfect
matching, and (2.1) do not force the restricted residual links encountered
by a random-greedy trajectory to remain expandable.

For the actual interval hypergraph, the independent-residual calculation
is even more direct.  The number `E` of labelled atoms satisfies

\[
\log E=O(m\log m),
\]

whereas `kappa=Theta(m^(5/4))`.  Retaining target vertices independently
with density `m^(-1/2)` leaves expected atom count

\[
E m^{-\kappa/2}=o(1).
\tag{2.5}
\]

Thus a successful construction must preserve interval cylinders by
nonlocal exchange.  The rest of the report constructs the exact central
exchange and isolates its full-cylinder lift.

## 3. Exact interval moment expansion along every matching trajectory

Let `M` be a matching of `s` proportional atoms.  For a coordinate set
`T`, define

\[
c_q^M(T)
=\#\{S:\ S\text{ is covered by }M\text{ in rank }m+q, T\subseteq S\},
\]

and let

\[
r_q^M(T)
=\#\{S:\ S\text{ is residual in rank }m+q, T\subseteq S\}.
\tag{3.1}
\]

Thus, whenever `|T|=j<=m+q`,

\[
r_q^M(T)
=\binom{n-j}{m+q-j}-c_q^M(T).
\tag{3.2}
\]

### Theorem 3.1 — all-depth interval moment slab

Fix `q<q'` in the atom band, put `h=q'-q`, and let `|T|=j`.  Then

\[
\boxed{
-s|I_q\setminus I_{q'}|
\le
c_{q'}^M(T)-c_q^M(T)
\le
s\left(
|I_{q'}\setminus I_q|
+\min\{|I_q\cap I_{q'}|,hj\}
\right).}
\tag{3.3}
\]

If in addition `j<=m+q`, then, for `t in {q,q'}`, with

\[
F_t(T)=\binom{n-j}{m+t-j},
\]

the residual satisfies

\[
\boxed{
F_{q'}(T)-F_q(T)
-s\left(
|I_{q'}\setminus I_q|
+\min\{|I_q\cap I_{q'}|,hj\}
\right)
\le r_{q'}^M(T)-r_q^M(T)
\le
F_{q'}(T)-F_q(T)+s|I_q\setminus I_{q'}|.}
\tag{3.4}
\]

#### Proof

For one atom `e`, write

\[
c_q^e(T)=\sum_{i\in I_q}\mathbf1_{\{T\subseteq A_{i,q}\}}.
\]

A start in `I_q\setminus I_{q'}` contributes at worst `-1` to the
difference, and a start in `I_{q'}\setminus I_q` contributes at most `+1`.
At a common start,

\[
A_{i,q}\subset A_{i,q'},
\]

and the indicator can change from zero to one only if one of the `j`
labels of `T` occurs in the `h` newly added word positions.  A fixed label
occurs once in the injective word and belongs to at most `h` such moving
segments as `i` varies.  Hence the total positive change over common starts
is at most `hj`, and trivially at most `|I_q\cap I_{q'}|`.  This proves the
one-atom inequality.  Sum over the `s` atoms and use (3.2) to obtain
(3.3)--(3.4).  ∎

The central pair has a sharper exact form.

### Theorem 3.2 — central hypersimplex and star-moment identities

For one atom put

\[
A_i=A_{i,0},
\qquad
B_i=A_{i,1}=A_i\cup\{x_{i+m}\},
\qquad 0\le i<b.
\tag{3.5}
\]

For `T in binom([n],j)` with `1<=j<=m+1`, define

\[
g_M(T)=c_1^M(T)-c_0^M(T).
\]

Then

\[
\boxed{
g_M(T)
=\sum_{e\in M}\sum_{i=0}^{b-1}
\mathbf1_{\{x_{i+m}\in T,\ T\setminus\{x_{i+m}\}\subseteq A_i\}}.}
\tag{3.6}
\]

Consequently

\[
0\le g_M(T)\le s\min(j,b),
\tag{3.7}
\]

and

\[
\boxed{
\sum_{T\in\binom{[n]}j}g_M(T)
=sb\binom m{j-1}.}
\tag{3.8}
\]

If `1<=j<=m` and

\[
D_j
=\binom{n-j}{m+1-j}-\binom{n-j}{m-j}
=\frac{j}{m+1-j}\binom{n-j}{m-j},
\tag{3.9}
\]

then

\[
\boxed{
D_j-s\min(j,b)
\le r_1^M(T)-r_0^M(T)
\le D_j.}
\tag{3.10}
\]

For points `x in [n]`, let `a_x=g_M({x})`.  Then

\[
0\le a_x\le s,
\qquad
\sum_xa_x=sb,
\tag{3.11}
\]

and, for every `X subseteq [n]`,

\[
\boxed{
s\bigl(b-(n-|X|)\bigr)_+
\le a(X)\le s\min(b,|X|).}
\tag{3.12}
\]

In residual notation,

\[
\boxed{
a_x=\frac Wn-\bigl(r_1^M(x)-r_0^M(x)\bigr).}
\tag{3.13}
\]

Finally, every integral vector satisfying (3.11) has a decomposition

\[
\boxed{
a=\mathbf1_{Y_1}+\cdots+\mathbf1_{Y_s},
\qquad |Y_h|=b.}
\tag{3.14}
\]

Thus (3.11)--(3.12) are not merely necessary fractional inequalities:
they are integrally sufficient for grouping the central added labels into
`s` bundles of `b` distinct labels.

#### Proof

For one central pair `A_i subset B_i`, the containment indicator of `T`
increases precisely when the unique added label lies in `T` and all other
labels of `T` already lie in `A_i`.  This proves (3.6).  The `b` labels
`x_{i+m}` in one atom are distinct, so at most `min(j,b)` of them lie in
`T`, proving (3.7).

For a fixed pair, the number of `j`-sets counted by (3.6) is
`binom(m,j-1)`: choose the other `j-1` labels inside `A_i`.  There are
`sb` pairs, proving (3.8).  Equations (3.9)--(3.10) follow by subtracting
the covered difference from the full-layer difference.

For `j=1`, (3.6) counts each added label.  This gives (3.11).  The upper
bound in (3.12) follows from the coordinate caps and the total mass.  The
lower bound follows by applying the upper bound to the complement:

\[
a(X)=sb-a([n]\setminus X)
\ge sb-s\min(b,n-|X|).
\]

For a point, the full-layer difference `D_1` equals

\[
\binom{2m}{m}-\binom{2m}{m-1}
=\frac1{m+1}\binom{2m}m
=\frac Wn,
\]

which proves (3.13).

It remains to prove the integral decomposition.  Suppose the current
vector has coordinate cap `h` and total `hb`.  At most `b` coordinates
have value `h`, and at least `b` coordinates are positive.  Choose a
`b`-set containing every coordinate of value `h` and fill it with positive
coordinates.  Subtract its incidence vector.  The new vector is
nonnegative, has cap `h-1`, and has total `(h-1)b`.  Induction from `h=s`
to zero proves (3.14).  ∎

The inequalities above exclude balanced but unreachable opposite-junta
residuals.  They still do not arrange the `s` label bundles into sliding
tight rows; that is a genuinely higher-order condition.

## 4. Exact nonlocal central augmentation

Let `G_m` be the bipartite inclusion graph with left side
`binom([n],m)`, right side `binom([n],m+1)`, and an edge `A B` when
`A subset B`.  Both sides have size `W`, and `G_m` is `(m+1)`-regular.
In particular it has a perfect matching.

### Theorem 4.1 — the `b`-path central augmentation

Let `M` be an atom matching of size

\[
s=p-\ell,
\]

where `ell>=1`,

and put

\[
u=W-sb=\rho+\ell b.
\tag{4.1}
\]

The `sb` pairs (3.5) form a matching `P_M` in `G_m`.  Against any fixed
perfect matching `Q` of `G_m`, the symmetric difference `P_M\triangle Q`
has exactly `u` vertex-disjoint `P_M`-augmenting paths.  The `b` shortest
of them jointly add `b` central flags and delete at most

\[
\left\lfloor\frac{b s b}{u}\right\rfloor
\tag{4.2}
\]

old central flags.

If `J subseteq M` is the family of atoms owning those deleted flags, then

\[
\boxed{
|J|
\le K(\ell)
:=\left\lceil\frac{s b^2}{\rho+\ell b}\right\rceil
\le\left\lceil\frac{pb}{\ell}\right\rceil.}
\tag{4.3}
\]

After freeing all atoms in `J`, the available central resources contain an
inclusion matching of size

\[
|J|b+b,
\tag{4.4}
\]

which is exactly the central quota of `|J|+1` atoms.

#### Proof

Targets inside one atom are distinct, and different atoms of `M` are
disjoint, so (3.5) gives a matching of `sb` inclusion edges.

In `P_M\triangle Q`, every vertex unmatched by `P_M` has degree one and
lies on an alternating augmenting path.  There are `u` unmatched vertices
on each side, hence exactly `u` such path components.  If `lambda_j` is
the number of old `P_M`-edges on path `j`, then

\[
\sum_{j=1}^{u}\lambda_j\le sb.
\]

The sum of the `b` smallest values is therefore at most `b s b/u`.
Each augmenting path has one more `Q`-edge than `P_M`-edge, so the `b`
paths add `b` flags.  Every deleted flag belongs to one old atom, proving
(4.3).

Upon freeing `J`, retain its central flags which were not deleted.  There
are `|J|b-k` of them if the paths delete `k` old flags.  Add the `k+b`
new `Q`-flags on the paths.  Alternation makes all these edges disjoint,
and their total is `|J|b+b`, proving (4.4).  ∎

This is a genuine integral nonlocal augmentation of the **one-parent
central flag matching**.  It is not yet a physical central-row
augmentation.  A physical atom also needs the cross incidences

\[
A_{i+1,0}\subset A_{i,1}\qquad(0\le i<b-1).
\tag{4.4a}
\]

More canonically, `t` atoms on `tb` available vertices in each middle
rank require a spanning union of `t` fresh alternating `(b,b)` paths in
the induced middle-incidence graph, and therefore at least

\[
t(2b-1)=2tb-t
\tag{4.4b}
\]

induced incidences.  Theorem 4.1 certifies only a matching of `tb`
incidences.  The exact path-factor characterization and a construction
satisfying all the central moment laws but having only `tb` isolated
incidences are proved in
`PROPORTIONAL_TIGHT_ATOM_CENTRAL_PATH_FACTOR_OBSTRUCTION_20260725.md`.
Thus Theorem 4.1 selects a quantitatively small release packet; it is not
itself a lift certificate.

Fix any auxiliary function

\[
\omega_m\longrightarrow\infty
\]

and define

\[
L_m=\left\lceil\frac{p}{\sqrt m\,\omega_m}\right\rceil.
\tag{4.5}
\]

Whenever `ell>=L_m`, Theorem 4.1 gives

\[
\boxed{
|J|\le b\sqrt m\,\omega_m+1
=O(\kappa\omega_m).}
\tag{4.6}
\]

If `omega_m` is chosen polynomially bounded (for example
`omega_m=log m`), only a polynomial-size old-atom packet must be
resegmented at each augmentation.  For arbitrary `omega_m->infinity`,
the exact bound (4.6), without the adjective polynomial, is what is used.
The next sections identify the exact full-rank expansion needed for that
resegmentation.

## 5. Exact boundary-type fibres

Complete the atom word to positions `0,...,n-1`.  Every designated interval
lies in

\[
U_{\rm pos}=\{0,1,\ldots,m+b+H-1\}.
\]

All designated intervals contain

\[
C_{\rm pos}=\{b-1,b,\ldots,m-H-1\},
\]

whose size is

\[
c=m-H-b+1.
\tag{5.1}
\]

They avoid the `c` positions outside `U_pos`.  The remaining boundary
position set

\[
Y_{\rm pos}=U_{\rm pos}\setminus C_{\rm pos}
\]

has size

\[
R=2b+2H-1,
\qquad n-R=2c.
\tag{5.2}
\]

### Theorem 5.1 — every boundary type is an exact matching fibre

Fix an ordered injective assignment

\[
y:Y_{\rm pos}\hookrightarrow[n]
\]

and write `Y=im(y)`.  For every

\[
C\in\binom{[n]\setminus Y}{c},
\]

there is an atom `e(y,C)` whose targets have the form

\[
\boxed{
A_{i,q}(y,C)=C\cup B_{i,q}(y),}
\tag{5.3}
\]

where `B_iq(y) subseteq Y` depends only on the boundary type and the slot.
For fixed `y`, the atoms `e(y,C)` are pairwise disjoint.  Hence they form
an exact matching of size

\[
\boxed{F=\binom{2c}{c}.}
\tag{5.4}
\]

#### Proof

After fixing `y`, exactly `2c` coordinate labels remain.  Choose `C` as the
labels assigned to the common positions and assign the complementary
`c` labels to positions avoided by all designated targets.  The order
inside either class does not affect the designated target system.  This
constructs (5.3).

Suppose a target from `e(y,C)` equals a target from `e(y,C')`.  Targets in
different ranks have different cardinalities.  In the same rank, equality
gives

\[
C\mathbin\triangle C'
=B_{i,q}(y)\mathbin\triangle B_{j,q}(y).
\]

The left side lies outside `Y`, while the right side lies inside `Y`.
Both must be empty.  Thus `C=C'`; within one injective atom, equal-rank
intervals at distinct designated starts are distinct.  Hence different
cores give disjoint atoms.  There are `binom(2c,c)` choices of `C`.  ∎

There are

\[
G=(n)_R
\tag{5.5}
\]

ordered boundary types.  Since `R=O(m^(3/4))`,

\[
\log G=O(m^{3/4}\log m)=o(m),
\qquad
G=o(p/\sqrt m).
\tag{5.6}
\]

Also `F` is much larger than `p/G`.  More explicitly, Stirling's formula
and `R=o(n)` give

\[
\log F=2c\log2+O(\log m),
\qquad
\log G=R\log n+O(R^2/n),
\qquad
\log p=2m\log2+O(\log m).
\]

Since `c=m-H-b+1` and `R=2b+2H-1`,

\[
\log\frac{FG}{p}
=R\log n-2(b+H-1)\log2+O(R^2/n+\log m)
\longrightarrow\infty.
\tag{5.6a}
\]

Thus `F/(p/G)->infinity`.

### Corollary 5.2 — an exact type-balanced fractional schedule

Write

\[
p=aG+r,
\qquad 0\le r<G.
\tag{5.7}
\]

Give every atom in every boundary fibre weight `a/F`.  This has total
weight

\[
aG=p-r=p-o(p/\sqrt m),
\tag{5.8}
\]

uses exactly mass `a` in every boundary type, and gives every rank-`q`
target load

\[
\frac{aGb_q}{N_q}\le\frac{pb_q}{N_q}\le1.
\tag{5.9}
\]

#### Proof

By (5.6a), `a/F<=1` for all sufficiently large `m`.  The total mass and
type quota are immediate.  The multiset of all pairs
`(y,C)` is coordinate-transitive.  Double counting its incidences with a
fixed rank-`q` target gives degree `GF b_q/N_q`.  Multiplication by `a/F`
gives (5.9).  Equation (5.6) gives (5.8).  ∎

Thus the desired accuracy already has an exact, type-balanced fractional
solution built from integral matching fibres.  The missing step is solely
the correlation of different boundary types.

## 6. The exact cylinder-fibre expansion inequality

For an atom matching `M` and `J subseteq M`, let

\[
\mathcal U_M(J)
=V(\mathcal P)\setminus V(M\setminus J)
\tag{6.1}
\]

be the global residual resources together with all resources released by
`J`, and define the allowed packet fibre

\[
\mathcal H_M(J)
=\mathcal P[\mathcal U_M(J)]
=\{e\in\mathcal P:e\cap V(M\setminus J)=\varnothing\}.
\tag{6.2}
\]

The exact full lift requested by Theorem 4.1 is

\[
\boxed{
\nu(\mathcal H_M(J))\ge|J|+1.}
\tag{Lift}
\]

If (Lift) holds, replacing `J` by the larger allowed matching increases
the global atom matching by one.

There are two concrete expansion inequalities which imply (Lift).

### Theorem 6.1 — cover and edge-expansion criteria

Either of

\[
\boxed{
\tau(\mathcal H_M(J))>\kappa|J|}
\tag{CE}
\]

or

\[
\boxed{
|E(\mathcal H_M(J))|
>\kappa|J|\,\Delta(\mathcal H_M(J))}
\tag{CE'}
\]

implies (Lift).  Here `tau` is the minimum integral vertex-cover number and
`Delta` is maximum vertex degree in the allowed fibre.

#### Proof

If a maximal matching in `H_M(J)` had size at most `|J|`, the union of its
edges would be a vertex cover of size at most `kappa|J|`.  This contradicts
(CE), so (Lift) follows.

Every vertex cover `X` satisfies

\[
|E(\mathcal H_M(J))|
\le\sum_{v\in X}\deg(v)
\le|X|\Delta(\mathcal H_M(J)).
\]

Thus (CE') implies (CE).  ∎

The boundary fibres remove the factor `kappa` from the most concrete
criterion.  For a boundary type `y`, let

\[
\mathcal B_{M,J}(y)
=\left\{C\in\binom{[n]\setminus\operatorname{im}y}{c}:
e(y,C)\cap V(M\setminus J)\ne\varnothing\right\}
\tag{6.3}
\]

be its blocked cores.

Before using a prescribed packet, it is useful to record the exact Hall
object internal to one cylinder.  For fixed `M` and `y`, form a bipartite
graph `K_M(y)` whose left vertices are the `F` cores and whose right
vertices are the atoms of `M`; join `C` to `f` when
`e(y,C)\cap f` contains a target vertex.  Write `Gamma_{M,y}(A)` for the
right neighbourhood of a core family `A`.

### Theorem 6.2 — exact owner-neighbourhood criterion and cylinder ledger

There is a strict augmentation of `M` using replacement atoms from one
boundary fibre if and only if, for some type `y` and some core family
`A`,

\[
\boxed{|A|>|\Gamma_{M,y}(A)|.}
\tag{6.3a}
\]

Both sides of `K_M(y)` have degree at most `kappa`.  Moreover, if `M` has
`t` atoms and

\[
\Sigma_m=\sum_{q=-H}^{H+1}\frac{b_q^2}{N_q},
\tag{6.3b}
\]

then the target-incidence multiplicities obey the exact identity

\[
\boxed{
\sum_y\sum_C\sum_{f\in M}|e(y,C)\cap f|
=GFt\Sigma_m.}
\tag{6.3c}
\]

Consequently

\[
\frac{\kappa-(2H+2)}p<\Sigma_m\le\frac\kappa p,
\tag{6.3d}
\]

and, for every packet `J subseteq M`,

\[
\boxed{
\max_y\left[F-|\mathcal B_{M,J}(y)|\right]
\ge
\max\left\{0,
\left\lceil F\bigl(1-(|M|-|J|)\Sigma_m\bigr)\right\rceil
\right\}.}
\tag{6.3e}
\]

In particular, the right side of (6.3e) being at least `|J|+1` is a fully
proved numerical sufficient condition for (FE).

#### Proof

Suppose (6.3a) holds and put `J=Gamma_{M,y}(A)`.  The atoms
`{e(y,C):C in A}` are pairwise disjoint by Theorem 5.1 and meet no atom
of `M\setminus J`.  Replacing `J` by these atoms increases the matching
by `|A|-|J|`.  Conversely, if atoms indexed by `A` from one fibre replace
a family `J subseteq M`, every old atom meeting one of them must lie in
`J`.  Hence `Gamma_{M,y}(A) subseteq J`, and a strict augmentation gives
(6.3a).  This proves the equivalence.

A left atom has `kappa` target vertices, each belonging to at most one
atom of the matching `M`; hence its graph degree is at most `kappa`.
For a fixed type `y`, the fibre atoms form a matching, so each of the
`kappa` targets of a right atom belongs to at most one core atom.  The
right degree is also at most `kappa`.

The coordinate-transitive family of all `GF` pairs `(y,C)` contains each
fixed rank-`q` target exactly

\[
D_q=\frac{GFb_q}{N_q}
\]

times.  The matching `M` contains exactly `tb_q` distinct rank-`q`
targets.  Double counting triples consisting of a boundary atom, an old
atom, and one common rank-`q` target gives

\[
tb_qD_q=GFt\frac{b_q^2}{N_q}.
\]

Summing over `q` proves (6.3c).  Since

\[
pb_q\le N_q<p(b_q+1),
\]

we have

\[
\frac{b_q-1}{p}<\frac{b_q^2}{N_q}\le\frac{b_q}{p}.
\]

Summation proves (6.3d).

Apply (6.3c) to the matching `M\setminus J`.  For fixed `y`, the number
of nonisolated core vertices in `K_{M\setminus J}(y)` is at most its
number of graph edges, which in turn is at most the target-incidence
multiplicity.  Some type has multiplicity at most the average
`F(|M|-|J|)Sigma_m`.  Its number of isolated cores is therefore at least
the integer ceiling in (6.3e), with zero inserted when the displayed real
bound is negative.  Those isolated cores are exactly the unblocked cores
in (6.3).  This proves (6.3e).  ∎

The exact ledger (6.3e) is useful at sparse stages, but at the desired
near-perfect scale `( |M|-|J| )Sigma_m` is of order `kappa`; its
first-moment right side is then zero.  Thus the late augmentation requires
genuine concentration of many released target incidences into the same
owner neighbourhood, not a repetition of the uniform incidence count.

### Corollary 6.3 — cylinder-fibre expansion

If

\[
\boxed{
\max_y
\left[
\binom{2c}{c}-|\mathcal B_{M,J}(y)|
\right]
\ge|J|+1,}
\tag{FE}
\]

then (Lift) holds.

#### Proof

Choose a type attaining (FE).  Its unblocked core atoms all lie in
`H_M(J)`, and Theorem 5.1 says they are pairwise disjoint.  Any `|J|+1`
of them prove (Lift).  ∎

Condition (FE) is the interval-specific expansion inequality: after the
central alternating packet releases `J`, one ordered word-boundary cylinder
must retain `|J|+1` core completions.  It is much sharper than demanding an
edge in an arbitrary residual of the same part sizes.

### Theorem 6.4 — exact iteration to the required leave

Let `omega_m->infinity`.  Suppose that for every atom matching `M` with
deficit

\[
\ell=p-|M|\ge L_m
=\left\lceil\frac{p}{\sqrt m\,\omega_m}\right\rceil,
\tag{6.4}
\]

one packet `J` supplied by the `b` shortest central augmenting paths of
Theorem 4.1 satisfies (Lift).  It is enough instead to assume (FE), (CE),
or (CE').

Then `P_{m;b,H}` has a matching of size

\[
\boxed{
p-o(p/\sqrt m).}
\tag{6.5}
\]

Every augmentation changes at most

\[
b\sqrt m\,\omega_m+1=O(\kappa\omega_m)
\tag{6.6}
\]

old atoms.

#### Proof

Start with the empty matching.  While the deficit is at least `L_m`, apply
Theorem 4.1 and then (Lift) to replace `J` by `|J|+1` allowed atoms.  The
matching size increases by one and all objects remain integral atoms.
The process is finite and stops with deficit less than `L_m`.  Since
`omega_m->infinity`,

\[
L_m=o(p/\sqrt m).
\]

Equation (4.6) proves (6.6).  ∎

The theorem is constructive in the mathematical sense: at every stage it
specifies a central alternating packet and the exact allowed fibre in which
one larger integral matching must be found.  No independent rankwise factor
or fractional endpoint is substituted.

## 7. The leading `1/m` overlap is lossless flag transport

There is one further reason that (FE), rather than a rank-free pair estimate,
is the natural target.

### Proposition 7.1 — flag/far decomposition of the overlap row sum

In the labelled slot calculation, the terms with

\[
|P\setminus Q|+|Q\setminus P|=1
\]

are exactly adjacent-rank nested interval flags.  Their slot graph has
maximum degree at most four, and their conditional weights are `1/r` or
`1/(n-r)`.  All remaining slot pairs have total conditional row sum

\[
O(1/m^2).
\tag{7.1}
\]

Every leading adjacent-rank link has exact normalized Hall expansion.  If
`A subseteq binom([n],r)`, then

\[
\boxed{
\frac{|\partial^+\mathcal A|}{\binom n{r+1}}
\ge
\frac{|\mathcal A|}{\binom nr}.}
\tag{7.2}
\]

The dual lower-shadow inequality also holds.

#### Proof

If the two interval slots differ in exactly one position, one is obtained
from the other by adding or deleting one endpoint.  There are at most two
choices at each of the adjacent ranks, giving slot degree at most four.
Formula (3.1) of the reduction gives conditional weight `1/r` for one
deletion and `1/(n-r)` for one addition.

Every other pair has `a+c>=2` in that formula.  Summing

\[
\frac{a+c+1}{\binom ra\binom{n-r}c}
\]

over `a+c>=2`, with `a,c=o(m)`, gives `O(1/m^2)` by the same binomial-series
bound as the original row-sum proof.  In the intrinsic codegree calculation
one must also sum over the possible second slot occupied by the fixed
target.  This introduces the same `a+c+1` multiplicity a second time;
the series with `(a+c+1)^2` is still `O(1/m^2)`, so (7.1) survives
unchanged.

For (7.2), count containment edges from `A` into its upper shadow.  There
are `(n-r)|A|` such edges, while each upper vertex receives at most `r+1`.
Thus

\[
|\partial^+\mathcal A|
\ge\frac{n-r}{r+1}|\mathcal A|.
\]

Since

\[
\binom n{r+1}/\binom nr=(n-r)/(r+1),
\]

this is (7.2).  The lower statement is identical.  ∎

Thus the order-`1/m` modes are not merely harmful overlap: individually
they are lossless Boolean transports.  What is missing is their
simultaneous synchronization around the interval-slot diamonds, exactly as
encoded by the cylinder completion count in (FE).  Once those flag modes
are synchronized, the unsynchronized pair-overlap remainder is only
`O(1/m^2)`.

## 8. Precise proved and conditional boundary

### Proved

1. The generic residual-pseudorandom nibble is not justified by
   transitivity and the `O(1/m)` row sum alone.
2. Every actual atom-matching trajectory satisfies the all-depth interval
   moment slab (3.3)--(3.4), the exact central star identities
   (3.6)--(3.10), and the integral endpoint hypersimplex law
   (3.11)--(3.14).
3. At atom deficit `ell>=1`, the `b` shortest central alternating paths
   produce an exact net
   `+b`-flag packet touching at most `ceil(pb/ell)` old atoms at atom
   deficit `ell`.
4. Every fixed ordered boundary type is an exact matching of
   `binom(2c,c)` atoms.
5. There is an exact type-balanced fractional matching of weight
   `p-o(p/sqrt(m))`.
6. The single-cylinder owner-neighbourhood condition (6.3a) is exactly
   equivalent to an augmentation from that cylinder; its blocker-incidence
   identity (6.3c) and averaged survivor inequality (6.3e) are exact.
7. Any one of (Lift), (FE), (CE), or (CE') along the central packets
   iterates to the matching required by Theorem 2.1 of the original
   reduction.
8. The leading `1/m` overlap modes are adjacent-rank flag transports with
   exact normalized Hall expansion; the remaining row sum is `O(1/m^2)`.

### Still unproved

1. No theorem here proves (FE), (CE), or (Lift) for the packet `J` supplied
   by Theorem 4.1.
2. The central augmented flags need not by themselves resegment into
   `|J|+1` full tight interval rows.
   In particular, (Lift) does not require its replacement atoms to use the
   newly produced `Q`-flags, so no such correlation has been smuggled into
   the iteration theorem.
3. Pairwise flag Hall expansion does not automatically enforce all slot
   diamonds or preserve the longer interval colors.
4. Therefore the proportional tight-atom matching lemma, the literal word,
   and constant one remain unproved.

The exact positive frontier for this route is (FE): prove that one boundary cylinder
retains `|J|+1` common-core completions after freeing the
`O(kappa omega_m)` atom packet selected by the central alternating paths.
This is strictly more structured than a rank-sensitive random nibble and
strictly less diffuse than an arbitrary residual expansion theorem.
