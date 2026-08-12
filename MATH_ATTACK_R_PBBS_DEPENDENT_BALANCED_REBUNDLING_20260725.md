# Lane R: dependent PBBS rebundling and the Gaussian collision gate

Date: 2026-07-25

## Status

The verified PBBS clean `C4`/alternating-`C8` reservoir is **not** turned
here into one balanced exact wreath factor with Catalan collision excess at
all Gaussian depths.  The requested gate remains open.

What is proved is a sharper and quantitative boundary.

1. Almost the whole vertex-disjoint clean reservoir can be partitioned into
   exact four-core ownership dependencies

   \[
   \mathbf 1_A+\mathbf 1_B=\mathbf 1_C+\mathbf 1_D.
   \]

   This gives at least

   \[
   \left(\frac1{256}-o(1)\right)\operatorname{Cat}_m
   \]

   pairwise switch-disjoint algebraic dependency packets.  It does not give
   endpoint-compatible sewing or bounded shadow-target congestion.

2. Balanced rebundling is exactly a vector-valued circulation on the
   residual-path incidence graph.  Every nonzero residual path must lie on
   an incidence cycle.  A literal two-piece short/long reassembly of exact
   wreaths is rigid: it can only rejoin equal-core fibres.  Thus the
   four-core relation cannot be implemented by merely cutting each source
   wreath once.

3. There are

   \[
   (1-O(m^{-1}))\operatorname{Cat}_m
   \]

   separated load-one core orbits for which all cyclic translates of the
   explicit clean `C8` are mutually vertex-disjoint.  This proves internal
   joint applicability of each rotation packet as an integral spanning
   `2`-factor.  It does not prove simultaneous applicability of different
   packets or exact-wreath output.

4. The canonical cyclic relation that cancels the centered short-path
   charges does not internally cancel any nonzero first-shadow increment.
   More precisely, translated first-shadow supports inside a separated
   packet are orthogonal.  This statement is conditional only in the sense
   that nonvanishing of the individual clean PBBS increment is not presently
   proved.

5. Arbitrary selector dependence is handled exactly.  The collision ledger
   is a covariance-minus-quota-variance identity, not an independent-sign
   estimate.  A common multidepth fractional point in the exact floor slabs,
   together with `O(1)` total packet mass and `O(1)` target congestion per
   depth, would imply an `O_A(W/sqrt(m))` weighted collision ledger for every
   already feasible integral selector.

6. That sufficient statement is sharp at the missing scale.  There are
   abstract integral, nonnegative, exact-mass load systems with a common
   perfectly balanced fractional point, target congestion `2`, and packet
   mass `4q`, for which **every** integral selector has collision `Pq` at
   depth `q`.  Consequently its Gaussian weighted collision is
   `Theta_A(W)`.  This is an exact load-system obstruction, not a PBBS or
   exact-factor counterexample.

The remaining theorem must therefore construct extra-cut, endpoint-valid,
cross-core circuits whose multidepth necklace charges cancel a
`1-O(1/q)` fraction of their raw quadratic energy, or else prove that the
actual PBBS packet increments have uniformly bounded total mass.  Centered
ownership balance alone does neither.

All factor and trade statements below are integral.  No independently
chosen rankwise factors are identified with one exact factor, and no
spanning `2`-factor is identified with a literal wreath factor.

## 1. Standing notation and imported audited input

Put

\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
B=\frac Wn=\operatorname{Cat}_m,
\]

and, for `1 <= q <= m-1`,

\[
\Omega_q=\binom{[n]}{m-q},\qquad
N_q=|\Omega_q|,\qquad
d_q=\left\lfloor\frac W{N_q}\right\rfloor.
\tag{1.1}
\]

For an integral load vector `mu` on `Omega_q`, define the exact floor
collision excess

\[
Q_q(\mu)
=\frac12\sum_{S\in\Omega_q}
 (\mu(S)-d_q)(\mu(S)-d_q-1).
\tag{1.2}
\]

The following input from the fully audited preceding PBBS package is used,
and is not reproved here.

### Audited PBBS reservoir input

Every load-one PBBS first-angle core

\[
K\in\binom{[n]}{m-1}
\]

supports an explicit clean directed `C4`, hence a clean common-core
alternating `C8` in `KG(n,m)`.  There is a family `R_m` of such cycles,
with distinct cores and pairwise disjoint vertex sets, satisfying

\[
|\mathcal R_m|
\ge
\frac{(m-2)(2m+1)}{128m(m+2)}B
=\left(\frac1{64}-o(1)\right)B.
\tag{1.3}
\]

Every subfamily of `R_m` is jointly toggleable and gives an integral
spanning `2`-factor.  This input does **not** say that the new components
all have length `n`.

For the distinguished three-vertex residual path of a load-one switch, its
centered charge is

\[
\zeta_K=n\mathbf 1_K-(m-1)\mathbf 1.
\tag{1.4}
\]

## 2. Exact residual-path topology

For a path `P` of middle vertices, define

\[
\zeta(P)
=n\sum_{X\in V(P)}\mathbf 1_X
 -m|V(P)|\mathbf 1.
\tag{2.1}
\]

A component is point-regular exactly when its total centered charge is
zero.  Because `gcd(n,m)=1`, every nonempty point-regular component has
length divisible by `n`.

### Theorem 2.1 — residual-path circulation criterion

Let `F` be a componentwise point-regular spanning `2`-factor of
`KG(n,m)`.  Apply any jointly applicable family of alternating switches,
and let `F'` be the resulting spanning `2`-factor.  Delete from `F` all old
switch edges and denote the resulting residual paths by `P`.  Untouched
components, which remain unchanged and balanced, are omitted from the
incidence graph below.

Form a bipartite multigraph `H` as follows:

- a left vertex represents an old component of `F`;
- a right vertex represents a new component of `F'`;
- the edge corresponding to a residual path `P` joins the old and new
  components containing `P` and has weight `zeta(P)`.

Then:

1. at every old vertex `C`,

   \[
   \sum_{P\subseteq C}\zeta(P)=0;
   \tag{2.2}
   \]

2. a new component `D` is point-regular if and only if

   \[
   \sum_{P\subseteq D}\zeta(P)=0;
   \tag{2.3}
   \]

3. `F'` is componentwise point-regular if and only if the edge weights are
   a vector-valued circulation on `H`;

4. in a balanced rebundling, every bridge of `H` has weight zero.
   Equivalently, after all zero-charge edges are deleted, every remaining
   edge lies on a cycle.

#### Proof

Equation (2.2) follows by additivity of (2.1) on each old point-regular
component.  The same additivity gives (2.3) for a new component.

For the bridge assertion, orient every incidence edge from old to new.  On
one side of a bridge, sum the old equations and subtract the new equations.
Every internal edge occurs once with each sign and cancels.  The bridge is
the sole remaining term, so its weight is zero.  ∎

A forest incidence topology is therefore possible only when every
residual-path charge is zero.  A pure merge is balanced because it assigns
each old component wholly to one new component.  Every nonneutral genuine
split requires an old/new incidence cycle.

## 3. Arithmetic of the compulsory load-one charges

Write

\[
r=m-1,\qquad
g=\gcd(n,r)=\gcd(3,m-1)\in\{1,3\}.
\tag{3.1}
\]

### Theorem 3.1 — exact unit-charge relations

Assume `m>=2`.

Let `K_1,...,K_t` be `r`-sets and let

\[
\varepsilon_i\in\{-1,1\}.
\]

Put `A=sum_i epsilon_i`.  Then

\[
\sum_{i=1}^t\varepsilon_i\zeta_{K_i}=0
\tag{3.2}
\]

if and only if

\[
n\sum_{i=1}^t\varepsilon_i\mathbf 1_{K_i}
=rA\mathbf 1.
\tag{3.3}
\]

Every such relation satisfies

\[
\frac ng\mid A.
\tag{3.4}
\]

Consequently:

1. a positive-only unit relation has at least `n/g` terms;
2. if `t<n/g`, then `A=0`, the positive and negative sides have equal
   cardinality, and

   \[
   \sum_{\varepsilon_i=1}\mathbf 1_{K_i}
   =
   \sum_{\varepsilon_i=-1}\mathbf 1_{K_i};
   \tag{3.5}
   \]

3. two unit charges cancel only as

   \[
   \zeta_K-\zeta_K=0;
   \tag{3.6}
   \]

4. for `m>=5`, no three-term unit relation exists.

#### Proof

Expanding (1.4) gives the equivalence of (3.2) and (3.3).  At every
coordinate, (3.3) implies `n | rA`, which is equivalent to (3.4).

If all signs are positive, `A=t`, proving the first assertion.  If
`t<n/g`, then `|A|<n/g`, so (3.4) forces `A=0`; (3.5) follows from
(3.3).  With two terms, `n/g>=3` excludes the same-sign values `A=2` and
`A=-2`; the only remaining zero sign sum is one positive and one negative,
and equality of the two incidence vectors forces equality of the cores.
Finally, for `m>=5` one has `n/g>=5`; a three-term relation
would have `A=0`, impossible for a sum of three signs.  ∎

For arbitrary integral coefficients `sigma_i`, the same proof controls
coefficient mass, not support size.  In particular, the correct smallness
hypothesis is

\[
\sum_i|\sigma_i|<n/g,
\]

not merely that few distinct cores occur.

### Theorem 3.2 — almost-complete four-core partition

Let

\[
\mathcal K\subseteq\binom{[n]}r,
\qquad |\mathcal K|=T,
\]

be a family of distinct cores.  Define

\[
M_{n,r}
=\sum_{j=0}^{r-1}
 \binom nj\binom{n-j}{2r-2j}
\tag{3.7}
\]

and

\[
R_{n,r}
=\left\lfloor
 \frac{1+\sqrt{1+8M_{n,r}}}{2}
 \right\rfloor.
\tag{3.8}
\]

All but at most `R_{n,r}` members of `K` can be partitioned into disjoint
quadruples `(A,B;C,D)` satisfying

\[
\mathbf 1_A+\mathbf 1_B
=\mathbf 1_C+\mathbf 1_D.
\tag{3.9}
\]

Consequently,

\[
\zeta_A+\zeta_B=\zeta_C+\zeta_D.
\tag{3.10}
\]

Moreover,

\[
R_{n,r}
\le 1+\sqrt2\,3^{n/2}
=o(B).
\tag{3.11}
\]

#### Proof

Map an unordered distinct pair `{A,B}` to

\[
\mathbf 1_A+\mathbf 1_B\in\{0,1,2\}^n.
\]

If `j=|A\cap B|`, the image is specified by choosing the `j` coordinates
of value `2` and the `2r-2j` further coordinates of value `1`.  Thus the
number of possible images is exactly (3.7).

If

\[
\binom T2>M_{n,r},
\]

two distinct pairs have the same image.  They cannot share exactly one
member, because cancelling that member would make the other two members
equal.  Hence they give four distinct cores satisfying (3.9).  Delete
those four cores and repeat.  If the process stops with `U` cores, then

\[
\binom U2\le M_{n,r},
\]

and therefore `U<=R_{n,r}`.

Finally `M_{n,r}<=3^n`.  Solving the quadratic inequality gives

\[
R_{n,r}\le1+\sqrt{2M_{n,r}}
\le1+\sqrt2\,3^{n/2}.
\]

Also

\[
B\ge\frac{2^n}{n(n+1)},
\]

so

\[
\frac{R_{n,r}}B
\le n(n+1)\left[
2^{-n}+\sqrt2\left(\frac{\sqrt3}{2}\right)^n
\right]
\longrightarrow0.
\]

This proves the final assertion.  ∎

### Corollary 3.3 — Catalan algebraic dependency supply

Apply Theorem 3.2 to the distinct cores of the audited reservoir
`R_m`.  Then there are at least

\[
\left(\frac1{256}-o(1)\right)B
\tag{3.12}
\]

four-cycle packets satisfying (3.10).

Each reservoir cycle occurs in exactly one packet, so the **switch-cycle**
congestion is one.  This says nothing about shadow-target congestion.  The
identity (3.10) also supplies neither endpoint-compatible seams nor an
exact-factor trade.

## 4. Sharp rigidity of one-cut exact-wreath reassembly

The algebraic four-core supply cannot be implemented by the most direct
short/long architecture.

### Theorem 4.1 — two-piece exact-factor rigidity

Let `n=2m+1>=5`.  Suppose `k` old exact `n`-wreaths are cut as follows.
For each source `i`, there are exactly two nonempty residual paths:

\[
|S_i|=3,\qquad |L_i|=n-3,
\tag{4.1}
\]

with

\[
\zeta(S_i)=\zeta_{K_i},\qquad
\zeta(L_i)=-\zeta_{K_i}.
\tag{4.2}
\]

Reassemble all `2k` paths, without subdividing them, into exact
`n`-vertex point-regular components.  Then every output contains one short
path and one long path, and their cores are equal.  Hence:

- if all `K_i` are distinct, every `S_i` rejoins `L_i`;
- if cores repeat, the only freedom is a permutation inside each equal-core
  fibre.

#### Proof

If one output contains `p` short paths and `ell` long paths, its exact
length gives

\[
3p+(n-3)\ell=n.
\tag{4.3}
\]

For `n>=7`, the nonnegative solutions are

\[
(p,\ell)=(1,1)
\tag{4.4}
\]

and, when `3|n`, the possible short-only solution

\[
(p,\ell)=(n/3,0).
\tag{4.5}
\]

Indeed, `ell>=2` leaves for the short pieces only

\[
n-(n-3)\ell\le6-n<0.
\]

For `n=5`, direct substitution in `3p+2ell=5` gives only `(1,1)`.

Every one of the `k` long paths must be consumed, and every output that
contains a long path consumes exactly one long path.  Hence there are at
least `k` outputs of type `(1,1)`.  The total number of exact `n`-outputs
is exactly `k`, because the total vertex count is `kn`.  Thus all outputs
have type `(1,1)`, and no short-only output occurs.

Balance of an output containing `S_i` and `L_j` is

\[
\zeta_{K_i}-\zeta_{K_j}=0.
\]

Theorem 3.1 forces `K_i=K_j`, proving the result.  ∎

For a PBBS component of length `hn` with `h>1`, the complement of its
distinguished three-vertex path has length `hn-3>n`.  It cannot occur in
any exact `n`-vertex output without being cut again.  Thus extra cuts are
forced even before balance is considered.

A four-core relation would formally group

\[
S_A,S_B,L_C,L_D
\quad\hbox{and}\quad
L_A,L_B,S_C,S_D.
\tag{4.6}
\]

If endpoint-compatible sewing existed, these would have length `2n`, not
length `n`.  Relation (3.10) therefore gives an algebraic balanced merge,
not an exact-factor trade.

No unrestricted lower bound such as “`2k+2a` residual pieces for `a`
mixed outputs” is asserted here.  Neutral paths and charges created by
additional cuts invalidate that count without further hypotheses.

## 5. Cyclic packets: abundant applicability but packet-local shadow rigidity

Identify the coordinate set with `Z_n`, and write `tau(x)=x+1`.

### 5.1 The exact first-shadow support envelope

Let a clean common-core `C8` have core

\[
K\in\binom{\mathbb Z_n}{m-1}.
\]

Its four vertices on one side contain `K`; its other four vertices are
disjoint from `K`.  Let `delta_{K,1}` be its first-shadow histogram
increment.

### Lemma 5.1 — support envelope

Every target in `supp(delta_{K,1})` lies in

\[
\Sigma(K)
=\left\{
T\in\binom{\mathbb Z_n}{m-1}:
|T\cap K|\in\{0,m-2\}
\right\}.
\tag{5.1}
\]

#### Proof

At a cycle vertex containing `K`, every odd-graph neighbour is disjoint
from that vertex.  Both the old and new first angles are therefore
disjoint from `K`.

At a cycle vertex `X` disjoint from `K`, write

\[
X^c=K\cup\{u,v\}.
\]

The two cycle neighbours are `K+u` and `K+v`.  The retained off-cycle
factor neighbour has the form

\[
X^c-\{s\}
\]

with `s\in K`; otherwise it would equal one of the two cycle neighbours.
Its intersection with either cycle neighbour contains exactly `m-2`
points of `K`.  These intersections are the old and new first angles.  ∎

### Lemma 5.2 — separation of two support envelopes

For two `(m-1)`-sets `K,K'`,

\[
\Sigma(K)\cap\Sigma(K')\ne\varnothing
\]

implies

\[
|K\cap K'|\le1
\quad\hbox{or}\quad
|K\cap K'|\ge m-4.
\tag{5.2}
\]

#### Proof

If a common target is disjoint from both cores, then their union lies in
its complement, which has size `m+2`; hence

\[
|K\cap K'|\ge2(m-1)-(m+2)=m-4.
\]

If it meets each core in `m-2` points, then both cores differ from the
target in one deleted and one inserted point, so

\[
|K\cap K'|\ge m-3.
\]

If it is disjoint from one core and meets the other in `m-2` points, the
two cores intersect only inside the unique point of the latter core not in
the target.  Thus their intersection has size at most one.  ∎

Call `K` **rotation-separated** if, for every nonzero `a in Z_n`,

\[
2\le |K\cap\tau^aK|\le m-5.
\tag{5.3}
\]

Equivalently,

\[
8\le |K\triangle\tau^aK|\le2m-6.
\tag{5.4}
\]

This interval is nonempty for `m>=7`.

### Theorem 5.3 — almost all load-one core orbits are separated

Let `E_m` be the number of `(m-1)`-sets that are not rotation-separated.
For `m>=7`,

\[
E_m
\le(n-1)\left[
2^{n/3}\sum_{j=0}^{3}\binom n{2j}
 +(n+1)\varphi^n
\right],
\qquad
\varphi=\frac{1+\sqrt5}{2}.
\tag{5.5}
\]

In particular,

\[
E_m=o(B).
\tag{5.6}
\]

The number of separated PBBS load-one core orbits is at least

\[
\frac1n\left(
\frac{m-2}{m+2}W-E_m
\right)
=(1-O(m^{-1}))B.
\tag{5.7}
\]

#### Proof

Fix a nonzero shift `a`.  Put

\[
d=\gcd(n,a),\qquad \ell=n/d.
\]

The permutation `tau^a` is the disjoint union of `d` cycles of odd length
`ell>=3`; hence `d<=n/3`.

The number

\[
|K\triangle\tau^aK|
\]

is the number of binary transitions around those cycles.  If it is at
most six, choose its `0`, `2`, `4`, or `6` transition edges.  Once those
edges are fixed, one initial bit per cycle remains free, with two choices,
so there are at most `2^d<=2^{n/3}` assignments.  This gives the first term
of (5.5).

At the opposite end, suppose

\[
|K\cap\tau^aK|\le1.
\]

This is the number of occupied directed adjacency edges in the union of
the `d` cycles.  Deleting at most one vertex makes the occupied set
independent.  There are at most `n+1` choices for the deleted set.  An odd
cycle of length `ell` has

\[
F_{\ell-1}+F_{\ell+1}
=\varphi^\ell-\varphi^{-\ell}<\varphi^\ell
\]

independent sets.  Thus the cycle union has fewer than `varphi^n`
independent sets.  Summing the two bad cases over the `n-1` nonzero shifts
proves (5.5).

Since

\[
B=\frac1n\binom nm
\ge\frac{2^n}{n(n+1)},
\]

(5.6) follows exponentially.  The audited PBBS multiplicity identities
give at least

\[
\frac{m-2}{m+2}W
\]

load-one cores.  PBBS is equivariant under `tau`.  Every separated core
has a full orbit, so division by `n` proves (5.7).  ∎

### Theorem 5.4 — internal applicability and shadow orthogonality

Let `K` be a separated PBBS load-one core and let `Z_K` be its explicit
clean common-core `C8`.

1. The `n` alternating cycles

   \[
   Z_K,\tau Z_K,\ldots,\tau^{n-1}Z_K
   \]

   are pairwise vertex-disjoint.  Every subset can therefore be toggled
   jointly, producing an integral spanning `2`-factor.

2. The translated first-shadow supports are pairwise disjoint.  For every
   real coefficient vector `(a_j)`,

   \[
   \left\|\sum_{j=0}^{n-1}
   a_j\tau^j\delta_{K,1}\right\|_2^2
   =\|\delta_{K,1}\|_2^2
    \sum_{j=0}^{n-1}a_j^2.
   \tag{5.8}
   \]

   For every `J subseteq Z_n`,

   \[
   \left\|\sum_{j\in J}\tau^j\delta_{K,1}\right\|_1
   =|J|\,\|\delta_{K,1}\|_1.
   \tag{5.9}
   \]

#### Proof

For vertex disjointness, suppose a vertex is shared by `Z_K` and a
nontrivial translate.  If it contains both cores, their intersection has
size at least `m-2`.  If it is disjoint from both, their intersection has
size at least `m-3`.  In the mixed case the two cores are disjoint.  Every
case contradicts (5.3).

By Lemmas 5.1 and 5.2,

\[
\Sigma(K)\cap\Sigma(\tau^aK)=\varnothing
\quad(a\ne0).
\]

Thus all translated supports are disjoint.  Equations (5.8) and (5.9)
follow by summing on disjoint coordinate sets.  ∎

In particular,

\[
\sum_{j=0}^{n-1}\tau^j\delta_{K,1}=0
\quad\Longleftrightarrow\quad
\delta_{K,1}=0.
\tag{5.10}
\]

It is **not proved** that every clean load-one PBBS seed has
`delta_{K,1} != 0`.  The unique retained `K`-angle lies on an unchanged
residual path and is not a private changed coordinate.  Thus the rigorous
statement is conditional transversality: every nonzero seed increment is
orthogonal to all of its nontrivial translates.

Theorem 5.4 is internal to one core orbit.  It does not say that packets
from distinct core orbits have disjoint vertices or disjoint shadow
supports.

## 6. Exact centered dependencies and monodromy

For a fixed core `K`, put

\[
v_j=n\mathbf 1_{\tau^jK}-(m-1)\mathbf 1
\qquad(j\in\mathbb Z_n).
\tag{6.1}
\]

These are exactly the centered charges of the translated distinguished
short paths.

### Theorem 6.1 — cyclic-design criterion

For `J subseteq Z_n`,

\[
\sum_{j\in J}v_j=0
\tag{6.2}
\]

if and only if

\[
\#\{j\in J:x\in\tau^jK\}
=\frac{|J|(m-1)}n
\quad\hbox{for every }x\in\mathbb Z_n.
\tag{6.3}
\]

Consequently,

\[
\frac n{\gcd(n,m-1)}\mid |J|.
\tag{6.4}
\]

Thus:

- if `m` is not congruent to `1 mod 3`, the only positive selections are
  the empty and full selections;
- if `m` is congruent to `1 mod 3`, the only possible proper sizes are
  `n/3` and `2n/3`, and the full design equations (6.3) are still
  necessary.

The exceptional cardinality is sharp.  Write `n=3h` and let
`J=3 Z_n`.  Since `h` is odd, choose `K` to contain `(h-1)/2` points in
each residue class modulo `3`.  Then (6.3) holds.

#### Proof

At coordinate `x`, equation (6.2) reads

\[
n\#\{j\in J:x\in\tau^jK\}
=(m-1)|J|,
\]

which is exactly (6.3).  Integrality gives (6.4), and (3.1) gives the two
cases.  The displayed residue-balanced example has exactly `(h-1)/2`
selected translates through every coordinate.  ∎

### Theorem 6.2 — complete prime-order signed kernel

Define

\[
p_K(z)=\sum_{x\in K}z^x,
\qquad
a(z)=\sum_{j=0}^{n-1}a_jz^j.
\]

For arbitrary complex coefficients `a_j`,

\[
\sum_ja_jv_j=0
\tag{6.5}
\]

if and only if

\[
a(\omega)p_K(\omega)=0
\tag{6.6}
\]

for every nontrivial `n`-th root of unity `omega`.

If `n>3` is prime and the `a_j` are rational, then (6.5) forces

\[
a_0=a_1=\cdots=a_{n-1}.
\tag{6.7}
\]

In particular, for coefficients in `{-1,0,1}`, the only relations are the
all-minus, all-zero, and all-plus relations.

#### Proof

The nontrivial Fourier coefficients of the vector in (6.5) are the
products in (6.6); the constant term in `v_j` contributes only at the
trivial character.

If `n` is prime and `p_K(omega)=0` at a nontrivial root, the cyclotomic
polynomial

\[
1+z+\cdots+z^{n-1}
\]

would divide the proper nonzero `0/1` polynomial `p_K`, which is
impossible.  Hence `a` vanishes at all nontrivial roots.  The same
cyclotomic divisibility forces `a` to be a scalar multiple of
`1+z+...+z^{n-1}`, proving (6.7).  ∎

### Corollary 6.3 — exact positive-short-path obstruction

Suppose a balanced output component is made from positive distinguished
three-vertex paths and zero-charge paths only.

- If `gcd(n,m-1)=1`, the presence of one distinguished path forces all
  `n` rotations, already contributing `3n` vertices.  Such a component
  cannot be an exact `n`-wreath.
- If `gcd(n,m-1)=3`, the only possible exact-length exception consists of
  exactly `n/3` distinguished paths satisfying (6.3), with no additional
  vertices.

This corollary does not treat arbitrary mixtures with negative long-path
charges.  For prime `n`, Theorem 6.2 gives the corresponding complete
signed centered-coefficient kernel classification.

### Theorem 6.4 — conditional cyclic-monodromy classification

Assume the translated short paths can actually be sewn so that the end of
path `j` is followed by path `j+a`.  Put

\[
d=\gcd(a,n).
\]

The sewing has `d` components, indexed by the cosets of the subgroup
`<a>`, and the component through `c` has charge

\[
\sum_{h\in\langle a\rangle}v_{c+h}.
\tag{6.8}
\]

It is balanced if and only if `K` meets every coset of `<a>` in exactly
`(m-1)/d` points.  Hence `d` must divide both `n` and `m-1`, so

\[
d\in\{1,3\}.
\tag{6.9}
\]

- Unit monodromy (`d=1`) is always balanced, but its one component has
  length `3n`, not `n`.
- The case `d=3` is balanced exactly for the residue-balanced cores and
  then gives three length-`n` short-path components.
- Every other monodromy is arithmetically obstructed.

#### Proof

The cycles of the permutation `j -> j+a` are the cosets of `<a>`, each of
size `n/d`.  Summing (6.1) on one coset gives (6.8).  Coordinatewise
vanishing says that every coordinate belongs to exactly `(m-1)/d` of the
selected translates, which is equivalent to the stated uniform coset
intersection.  Integrality forces `d|(m-1)`, and (3.1) gives (6.9).  The
length assertions follow because every short path has three vertices.  ∎

The endpoint-compatible sewing assumed in Theorem 6.4 is not supplied by
the PBBS reservoir.  Even in the exceptional `d=3` case, all complementary
long pieces still have to be placed in exact balanced components.

## 7. Quantified seam dependence inside a rotation packet

Vertex-disjoint switches need not have additive multidepth shadow
increments.  A depth-`q` target is read from a centered `2q`-edge window,
and one window can cross seams belonging to more than one switch.

For one full rotation packet, define the interaction graph `H_q` on
`Z_n`: two rotations are adjacent if some old or new centered `2q`-edge
window meets switch seams from both rotations.

### Theorem 7.1 — sparse local interaction can be globally connected

For every `1<=q<=m-1`:

1. `H_q` is a Cayley graph of `Z_n`;
2. its maximum degree satisfies

   \[
   \Delta(H_q)\le32q+8;
   \tag{7.1}
   \]

3. at most `8qn` old windows and at most `8qn` new windows are affected;
4. the connected components are cosets of the subgroup generated by the
   connection shifts;
5. if `n` is prime, then `H_q` is either empty or connected.

#### Proof

Rotation equivariance makes `H_q` Cayley.  A switch has four old seams.
The radius-`2q` edge-neighbourhood of one seam has at most `4q+1` seam
positions, so the four old seams can interact with at most

\[
4(4q+1)
\]

other rotations.  The same bound holds for the four new seams.  This gives
(7.1).  Each seam belongs to at most `2q` centered `2q`-edge windows, so
the four seams of each of the `n` rotations affect at most `8qn` windows
on each side.

The component statement is standard for a Cayley graph: components are
cosets of the subgroup generated by its connection set.  A nonzero element
generates `Z_n` when `n` is prime.  ∎

Thus `O(q)` local degree does not justify independent packet signs.  For
prime `n`, one interaction makes all `n` rotations a single dependent
cluster.  When `H_q` is nonempty, an additive sum of isolated-switch
increments must be replaced by the actual cluster increment.

## 8. The exact collision interaction ledger

### Proposition 8.1 — deterministic quadratic expansion

Let `delta_q` be an integral mass-zero change:

\[
\sum_{S\in\Omega_q}\delta_q(S)=0.
\]

Then the exact floor cancels and

\[
Q_q(\mu_q+\delta_q)-Q_q(\mu_q)
=\langle\mu_q,\delta_q\rangle
 +\frac12\|\delta_q\|_2^2.
\tag{8.1}
\]

If an actual simultaneous increment decomposes as

\[
\delta_q=\sum_{i=1}^P\delta_{i,q},
\]

then

\[
Q_q(\mu_q+\delta_q)-Q_q(\mu_q)
=\sum_i\left(
\langle\mu_q,\delta_{i,q}\rangle
 +\frac12\|\delta_{i,q}\|_2^2
\right)
 +\sum_{i<j}\langle\delta_{i,q},\delta_{j,q}\rangle.
\tag{8.2}
\]

#### Proof

Expand the quadratic in (1.2).  The linear floor term is

\[
-(d_q+1/2)\sum_S\delta_q(S),
\]

which is zero.  Expanding the squared norm of the sum gives (8.2).  ∎

Accordingly, the Gaussian weighted collision

\[
\mathcal G_H(\mu)
=\sum_{q=1}^H\frac{Q_q(\mu_q)}{d_q}
\tag{8.3}
\]

contains the exact cross-packet Gram terms

\[
\sum_{q=1}^H
\frac{\langle\delta_{i,q},\delta_{j,q}\rangle}{d_q}.
\tag{8.4}
\]

No independent-sign estimate can discard them.

### Theorem 8.2 — floor-exact covariance identity

Let `M_q(S)` be any jointly distributed integral loads with finite second
moments.  Suppose

\[
\mathbb E M_q(S)=d_q+p_{q,S},
\qquad 0\le p_{q,S}\le1.
\tag{8.5}
\]

Then, with no independence hypothesis,

\[
\boxed{
\mathbb E Q_q(M_q)
=\frac12\sum_{S\in\Omega_q}
\left(
\operatorname{Var}M_q(S)
 -p_{q,S}(1-p_{q,S})
\right).}
\tag{8.6}
\]

Every summand is nonnegative.  Equality at coordinate `S` holds exactly
when

\[
M_q(S)\in\{d_q,d_q+1\}
\quad\hbox{almost surely}.
\tag{8.7}
\]

#### Proof

Put `Z=M_q(S)-d_q`, so `Z` is integer-valued and `E Z=p`.  Then

\[
\operatorname{Var}Z-p(1-p)
=\mathbb E[Z(Z-1)].
\]

The integer product `Z(Z-1)` is always nonnegative and is zero exactly
for `Z in {0,1}`.  Summing the identity proves (8.6).  ∎

The subtraction in (8.6) is essential.  The diagonal covariance itself is
not a collision obstruction: the Bernoulli variance needed to choose exact
floor/ceiling quotas is free.

### Corollary 8.3 — arbitrary dependent selectors

Let `X=(X_1,...,X_P)` be any random feasible `0/1` selector, put

\[
s=\mathbb E X,
\qquad
\Gamma=\operatorname{Cov}(X),
\]

and suppose

\[
M_q(S)=a_q(S)+\sum_iX_i\Delta_{i,q}(S).
\tag{8.8}
\]

If the mean satisfies (8.5), then

\[
\mathbb E Q_q
=\frac12\sum_{S\in\Omega_q}
\left(
\Delta_{q,S}^{T}\Gamma\Delta_{q,S}
 -p_{q,S}(1-p_{q,S})
\right),
\tag{8.9}
\]

where

\[
\Delta_{q,S}
=(\Delta_{1,q}(S),\ldots,\Delta_{P,q}(S))^T.
\]

This is the exact correlated-sign ledger.

## 9. What a common fractional slab would actually prove

The next theorem is deterministic.  It does not construct a feasible
selector and must not be called a rounding theorem.

### Theorem 9.1 — floor-slab stability for already feasible selectors

Fix positive integers `P,H` with `H<=m-1`, and one nonempty common
feasible set

\[
\varnothing\ne\mathcal X\subseteq\{0,1\}^P.
\]

For every `q<=H`, suppose

\[
\mu_q(x)
=a_q+\sum_{i=1}^P x_i\Delta_{i,q}
\in\mathbb Z_{\ge0}^{\Omega_q}
\tag{9.1}
\]

has total mass `W` for every `x in X`.

Assume there is one vector

\[
s\in[0,1]^P
\]

such that, simultaneously for every `q<=H` and every `S in Omega_q`,

\[
d_q
\le
\bar\mu_q(S)
:=a_q(S)+\sum_i s_i\Delta_{i,q}(S)
\le d_q+1.
\tag{9.2}
\]

Define

\[
R_q=\max_i\|\Delta_{i,q}\|_1,
\qquad
L_q=\max_{S\in\Omega_q}
 \sum_i|\Delta_{i,q}(S)|.
\tag{9.3}
\]

Then **every** `x in X` satisfies

\[
\boxed{
Q_q(\mu_q(x))
\le\frac12 P R_q(1+L_q).}
\tag{9.4}
\]

Consequently,

\[
\mathcal G_H(\mu(x))
\le
\frac P2\sum_{q=1}^H
\frac{R_q(1+L_q)}{d_q}.
\tag{9.5}
\]

#### Proof

Put

\[
p_q(S)=\bar\mu_q(S)-d_q\in[0,1],
\qquad
y_q=\mu_q(x)-\bar\mu_q.
\]

For every real `y` and every `p in [0,1]`,

\[
\frac12(p+y)(p+y-1)
=\frac12\bigl(y^2+(2p-1)y-p(1-p)\bigr)
\le\frac12(y^2+|y|).
\tag{9.6}
\]

Let

\[
k_q(S)=\sum_i|\Delta_{i,q}(S)|.
\]

Because `|x_i-s_i|<=1`,

\[
|y_q(S)|\le k_q(S),
\qquad
\sum_Sk_q(S)
\le PR_q,
\qquad
k_q(S)\le L_q.
\tag{9.7}
\]

It follows that

\[
\|y_q\|_1\le PR_q
\tag{9.8}
\]

and

\[
\|y_q\|_2^2
\le\sum_Sk_q(S)^2
\le L_q\sum_Sk_q(S)
\le L_qPR_q.
\tag{9.9}
\]

Sum (9.6) over the coordinates and use (9.8)-(9.9).  This proves (9.4),
and division by the exact `d_q` gives (9.5).  ∎

In the sign normalization

\[
\mu_q(\sigma)=a_q+\sum_i\sigma_i\delta_{i,q},
\qquad \sigma_i\in\{-1,1\},
\]

the corresponding bound is

\[
Q_q\le P R_q^{\pm}(1+2L_q^{\pm}),
\tag{9.10}
\]

where `delta_{i,q}` is **half** the full endpoint difference.  One may not
insert a full-switch norm into (9.10) without the factor-two correction.

### Corollary 9.2 — the genuinely sufficient bounded-mass regime

Fix `A>0` and put

\[
H_m=\lceil A\sqrt m\rceil.
\]

Suppose the hypotheses of Theorem 9.1 hold and, for constants independent
of `m` and `q<=H_m`,

\[
P\le C_0B,
\qquad
R_q\le R_A,
\qquad
L_q\le L_A.
\tag{9.11}
\]

Then, for all sufficiently large `m` (so that `H_m<=m-1`),

\[
\mathcal G_{H_m}
\le
\frac{C_0R_A(1+L_A)(A+1)}4
\frac W{\sqrt m}.
\tag{9.12}
\]

#### Proof

Use `d_q>=1`,

\[
H_m\le(A+1)\sqrt m,
\]

and

\[
B=\frac W{2m+1}\le\frac W{2m}
\]

in (9.5).  ∎

The unproved PBBS hypotheses in this corollary are precisely:

1. endpoint-valid topology-feasible packet orientations inside one exact
   factor;
2. an exact affine increment system using the same selectors at every
   depth;
3. one common `s` satisfying every floor slab (9.2);
4. uniform `O_A(1)` packet mass `R_q`;
5. uniform `O_A(1)` target congestion `L_q`.

The algebraic four-core partition proves none of items 1-5 beyond a
centered ownership identity at the distinguished residual paths.

## 10. Exact Gaussian floor scale and a sharp abstract obstruction

Put

\[
\rho_{m,q}=\frac W{N_q}.
\]

### Proposition 10.1 — exact reciprocal-floor Gaussian scale

For every `1<=q<=m-1`,

\[
\rho_{m,q}
=\prod_{j=1}^q
\left(1+\frac{q+1}{m-q+j}\right).
\tag{10.1}
\]

For every fixed `A>0`, with `H_m=ceil(A sqrt(m))`,

\[
\frac1{\sqrt m}
\sum_{q=1}^{H_m}\frac1{d_q}
\longrightarrow
I_0(A)
:=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
\tag{10.2}
\]

and

\[
\frac1m
\sum_{q=1}^{H_m}\frac q{d_q}
\longrightarrow
I_1(A)
:=\int_0^A\frac{x\,dx}{\lfloor e^{x^2}\rfloor}.
\tag{10.3}
\]

In particular,

\[
I_1(A)>0
\quad\hbox{and}\quad
\sum_{q=1}^{H_m}\frac q{d_q}=\Theta_A(m).
\tag{10.4}
\]

#### Proof

The binomial quotient gives (10.1).  Uniformly for
`q<=A sqrt(m)`, Taylor expansion with

\[
\frac{q+1}{m-q+j}=O_A(m^{-1/2})
\]

gives

\[
\log\rho_{m,q}
=\frac{q^2}{m}+O_A(m^{-1/2}).
\tag{10.5}
\]

The functions

\[
x\longmapsto\frac1{\lfloor e^{x^2}\rfloor},
\qquad
x\longmapsto\frac{x}{\lfloor e^{x^2}\rfloor}
\]

are bounded on `[0,A]` and have only finitely many discontinuities there,
at points `sqrt(log k)`.  Outside arbitrarily small fixed neighbourhoods
of those points, (10.5) makes the convergence of the floored summands
uniform.  The neighbourhoods contribute arbitrarily little to the
normalized sums; the single endpoint added by the ceiling is negligible.
Riemann summation proves (10.2)-(10.3).  Positivity of `I_1(A)` is
immediate.  ∎

There is also an explicit finite lower bound.  Put

\[
L_m=\left\lfloor
\min\left\{\frac A2,\frac14\right\}\sqrt m
\right\rfloor.
\tag{10.6}
\]

For `1<=q<=L_m`,

\[
\log\rho_{m,q}
\le\frac{q(q+1)}{m-q+1}
\le\frac14,
\]

so

\[
d_q=1.
\tag{10.7}
\]

Therefore

\[
\sum_{q=1}^{H_m}\frac q{d_q}
\ge\frac{L_m(L_m+1)}2.
\tag{10.8}
\]

Thus an absolute-value packet bound with mass proportional to `q` is at
the critical `Theta_A(m)` Gaussian scale; selector dependence alone does
not make it smaller.

### Theorem 10.2 — exact abstract sharpness example

Fix constants `A>0` and `c_0>0`, and put

\[
P=\lfloor c_0B\rfloor,
\qquad
H_m=\lceil A\sqrt m\rceil.
\]

For all sufficiently large `m`, there are, simultaneously for every
`q<=H_m`, affine integral nonnegative load systems on the correct target
sets `Omega_q`, using the same selectors

\[
x\in\{0,1\}^P,
\]

such that:

1. every integral load has total mass exactly `W`;
2. the common fractional selector

   \[
   s_i=1/2
   \]

   lies exactly in the floor/ceiling slab at every coordinate;
3. the full endpoint increments satisfy

   \[
   R_q=4q,
   \qquad
   L_q=2;
   \tag{10.9}
   \]

4. every integral selector, with arbitrary dependence or global
   restriction among selector signs, satisfies

   \[
   Q_q=Pq.
   \tag{10.10}
   \]

Consequently,

\[
\mathcal G_{H_m}
=P\sum_{q=1}^{H_m}\frac q{d_q}
=\left(\frac{c_0I_1(A)}2+o(1)\right)W.
\tag{10.11}
\]

#### Proof

Start with any exact floor/ceiling quota vector of total `W`: exactly

\[
W-d_qN_q
\]

coordinates have value `d_q+1`, and the rest have value `d_q`.  One of
these two classes has at least `N_q/2` coordinates.

For each selector `i`, choose `q` coordinate pairs in that majority class,
with all `2Pq` selected coordinates distinct.  This is possible uniformly
for `q<=H_m`, because (10.5) makes `rho_{m,q}=O_A(1)` and

\[
\frac{2Pq}{N_q}
\le
\frac{2c_0q}{2m+1}\rho_{m,q}
=O_A(m^{-1/2}).
\tag{10.12}
\]

If the common quota level of one selected pair is `h`, replace its two
states by

\[
(h-1,h+1)
\quad\hbox{and}\quad
(h+1,h-1).
\tag{10.13}
\]

The midpoint is `(h,h)`, so `s_i=1/2` returns the exact balanced quota
vector.  Both states are nonnegative because `d_q>=1`.  Each pair preserves
its total mass and contributes exactly one unit to `Q_q`: for `h=d_q`, the
loads are `d_q-1,d_q+1`; for `h=d_q+1`, they are `d_q,d_q+2`.

One selector flips `q` disjoint pairs.  Its full increment has two entries
of magnitude `2` per pair, hence `l1` norm `4q`.  Since no target coordinate
is used by two selectors, the congestion is `2`.  Every selector state
contributes exactly `q` collisions, proving (10.9)-(10.10).  Finally use
(10.3) and

\[
P=(c_0+o(1))\frac W{2m+1}
\]

to obtain (10.11).  ∎

Theorem 10.2 is not asserted to arise from PBBS shadows, a spanning
`2`-factor, or a literal OR word.  It proves the precise logical point that
a common floor-balanced fractional solution, arbitrary sign dependence,
and constant target congestion do not suffice when packet mass remains
`Theta(q)`.

## 11. Full rotation packets in necklace coordinates

Let `rho` denote cyclic rotation on `Omega_q`.  For an additive seed
increment `delta_{i,q}`, define its full developed packet by

\[
\Delta_{i,q}
=\sum_{t=0}^{n-1}\rho^t\delta_{i,q}.
\tag{11.1}
\]

For a target necklace `O subseteq Omega_q`, put

\[
\ell_O=|O|,
\qquad
h_O=\frac n{\ell_O},
\qquad
c_{i,q,O}=\sum_{S\in O}\delta_{i,q}(S).
\tag{11.2}
\]

### Theorem 11.1 — exact orbit projection

For every `S in O`,

\[
\boxed{
\Delta_{i,q}(S)=h_Oc_{i,q,O}.}
\tag{11.3}
\]

Consequently,

\[
\|\Delta_{i,q}\|_2^2
=n^2\sum_O\frac{c_{i,q,O}^2}{\ell_O},
\tag{11.4}
\]

and the full rotation packet cancels at depth `q` if and only if

\[
c_{i,q,O}=0
\quad\hbox{for every target necklace }O.
\tag{11.5}
\]

#### Proof

As `t` runs through `Z_n`, the target `rho^{-t}S` runs through every member
of `O` exactly `h_O` times.  This proves (11.3).  Summing its square over
the `ell_O` coordinates of each necklace gives (11.4), and (11.5) follows.
∎

Thus total mass zero, or centered ownership charge zero, is only the sum of
the necklace equations.  It does not imply any individual equation in
(11.5).

### Corollary 11.2 — exact residue obstruction

Suppose a cyclic-invariant integral baseline has value `u_{q,O}` on
necklace `O`, and only full rotation packets (11.1) are used.  Then every
obtainable load satisfies

\[
\mu_q(S)\equiv u_{q,O}\pmod{h_O}
\qquad(S\in O).
\tag{11.6}
\]

Define

\[
r_O=min_{z\equiv u_{q,O}\pmod{h_O}}
\operatorname{dist}\bigl(z,\{d_q,d_q+1\}\bigr).
\tag{11.7}
\]

Then every such load satisfies

\[
Q_q(\mu_q)
\ge
\sum_O\ell_O\frac{r_O(r_O+1)}2.
\tag{11.8}
\]

If `O` is periodic, then `h_O>1` divides both `n` and `m-q`, hence

\[
h_O\mid2q+1.
\tag{11.9}
\]

In particular, if

\[
\gcd(n,2q+1)=1,
\tag{11.10}
\]

every rank-`(m-q)` necklace is aperiodic.  In general, the number of
periodic targets is at most

\[
\sum_{\substack{h\mid\gcd(n,m-q)\\h\ge3}}
\binom{n/h}{(m-q)/h}
\le n2^{n/3}.
\tag{11.11}
\]

#### Proof

Equation (11.6) follows from (11.3).  If an allowed integer load is at
distance `r` below `d_q` or above `d_q+1`, its coordinate contribution to
`Q_q` is at least `r(r+1)/2`, proving (11.8).

The stabilizer of a periodic target has order `h_O`, so the target is a
union of stabilizer orbits.  Therefore `h_O` divides its size `m-q` as well
as `n`; subtracting twice the former from the latter gives (11.9).  Since
`n` is odd, every nontrivial `h_O` is at least three.  For each possible
stabilizer order, choose `(m-q)/h` of the `n/h` stabilizer orbits.  Summing
and then bounding each binomial coefficient by `2^{n/h}` proves (11.11).
∎

The universal congruence obstruction is supported on exponentially few
targets in the Gaussian range.  The substantive issue is the simultaneous
necklace-charge lattice at all depths.

### Theorem 11.3 — exact negative-dependence requirement

Fix a depth `q` satisfying (11.10), so every necklace is aperiodic.  Use a
sign normalization distinct from the full `0/1` increments in (11.1): let
`eta_{i,q}` be a seed direction, put

\[
\Xi_{i,q}=\sum_{t=0}^{n-1}\rho^t\eta_{i,q},
\qquad
b_{i,q,O}=\sum_{S\in O}\eta_{i,q}(S),
\qquad
\mathsf C_q=(b_{i,q,O})_{O,i}.
\tag{11.12}
\]

Thus `2 Xi_{i,q}` is the full difference between the two sign endpoints;
equivalently, `Xi_{i,q}` is the half-increment.  The directions and charges
may be real, but the realized loads below are required to be integral.

Let `sigma in {-1,1}^P` have any joint law with

\[
\mathbb E\sigma=0,
\qquad
\Gamma=\operatorname{Cov}(\sigma),
\]

and suppose every realized affine load

\[
\mu_q(\sigma)
=u_q+\sum_{i=1}^P\sigma_i\Xi_{i,q}
\tag{11.13}
\]

is integral and the cyclic-invariant midpoint `u_q` is coordinatewise in
`{d_q,d_q+1}`.  Then

\[
\boxed{
\mathbb E Q_q
=\frac n2\operatorname{tr}(\mathsf C_q^T\mathsf C_q\Gamma).}
\tag{11.14}
\]

If the packet columns have pairwise disjoint necklace supports, arbitrary
correlations cannot reduce the energy:

\[
\mathbb E Q_q
=\frac n2\sum_{i=1}^P\|b_{i,q}\|_2^2.
\tag{11.15}
\]

More generally, assume constants `c,kappa>0` satisfy

\[
nP\ge cB,
\qquad
\|b_{i,q}\|_2^2\ge\kappa q
\quad(1\le i\le P).
\tag{11.16}
\]

If

\[
\mathbb E Q_q\le CB
\tag{11.17}
\]

for a constant `C`, the off-diagonal covariance contribution must cancel
at least

\[
\left(\kappa q-\frac{2C}{c}\right)P
\tag{11.18}
\]

of the diagonal trace.  Relative to the lower bound on the diagonal, this
is the fraction

\[
1-\frac{2C}{c\kappa q}.
\tag{11.19}
\]

This is a nontrivial positive cancellation requirement when
`q>2C/(c\kappa)`; below that threshold the displayed lower bound is
vacuous.

#### Proof

Aperiodicity means `ell_O=n` and `h_O=1`.  The sign-normalized packet
direction is constant with value `b_{i,q,O}` on each necklace.  Apply
Theorem 8.2 to
the quota-valued midpoint.  The free Bernoulli term is zero because the
mean is integral, and summing over the `n` coordinates in every necklace
gives (11.14).

For disjoint column supports, `mathsf C_q^T mathsf C_q` is diagonal.
Since every unbiased sign has variance one, (11.15) follows.

Under (11.16), the diagonal trace is at least `kappa qP`.  Equations
(11.14), (11.17), and `B/n<=P/c` give

\[
\operatorname{tr}(\mathsf C_q^T\mathsf C_q\Gamma)
\le\frac{2CB}{n}
\le\frac{2C}{c}P.
\]

Subtracting this upper bound from the diagonal lower bound proves
(11.18)-(11.19).  ∎

Theorem 11.3 does not assert the PBBS lower bound in (11.16), nor does it
assert additive packet increments when the interaction graph `H_q` is
nonempty.  It identifies the exact dependency that a successful raw
rotation architecture would have to construct: cross-core necklace
overlap and a feasible covariance lying in an approximate common kernel of
the matrices \(\mathsf C_q\).

## 12. Precise proved and conditional boundary

### Proved

1. The audited clean reservoir contains at least

   \[
   (1/256-o(1))B
   \]

   disjoint four-core centered-charge dependencies.  This is a
   switch-cycle packing statement only.

2. Balanced rebundling is exactly residual-path circulation.  Every
   nonzero residual piece lies on an incidence cycle.

3. The literal one-cut short/long architecture cannot mix distinct cores
   inside an exact factor.  Long PBBS components require further cuts even
   to reach the correct output length.

4. There are `(1-O(1/m))B` separated load-one core orbits with internally
   vertex-disjoint full rotation packets.

5. Inside a separated rotation packet, all nonzero translated first-shadow
   increments are orthogonal.  Hence the canonical centered full-orbit
   relation cannot create first-shadow cancellation from a nonzero seed.

6. Positive centered short-path relations are exactly cyclic `1`-designs;
   the divisibility obstruction is `n/g`, with the sole proper cardinality
   exception coming from `g=3`.  The prime-order signed kernel is one
   dimensional.

7. The actual seam dependency graph has degree at most `32q+8`, but for
   prime `n` it is either empty or connected.  Sparse local interaction
   therefore does not imply independent signs.

8. Equations (8.6), (8.9), and (11.14) are exact covariance formulas with
   the floor/ceiling Bernoulli variance subtracted.

9. A common exact floor slab plus uniformly bounded packet mass and target
   congestion gives the deterministic bound (9.12), with no product-sign
   hypothesis.

10. The Gaussian floor sum with a `q` numerator is `Theta_A(m)`, with the
    exact limit (10.3).  The abstract construction of Theorem 10.2 proves
    that `R_q=Theta(q)` is genuinely too large for this method, even under
    perfect fractional balance and arbitrary selector dependence.

11. Full rotation packets are governed by necklace charges, not by their
    total centered charge.  Sign-normalized necklace charge of squared
    size `Theta(q)` requires
    cancellation of a `1-O(1/q)` fraction of its diagonal quadratic energy.

### Conditional

Fix `A>0` and put `H_m=ceil(A sqrt(m))`.  If, for all sufficiently large
`m`, one can construct inside one exact factor `P=O_A(B)` endpoint-valid
`0/1` packet variables with one common fractional point satisfying all
floor slabs and with

\[
R_q,L_q=O_A(1)
\quad(1\le q\le H_m),
\]

then Theorem 9.1 gives

\[
\mathcal G_{H_m}
=O_A(W/\sqrt m).
\]

This is only a collision-ledger conclusion under the displayed
hypotheses.  No exact factor satisfying them is constructed here.

### Still unproved

1. extra-cut, endpoint-compatible sewing that turns a positive fraction of
   the algebraic four-core packets into exact `n`-wreath trades;
2. componentwise, rather than aggregate, centered cancellation after that
   sewing;
3. nonvanishing of every individual clean load-one PBBS first-shadow
   increment;
4. an affine common-selector description of the actual simultaneous PBBS
   shadow increments when seam clusters interact;
5. a common multidepth fractional point in all exact floor slabs;
6. uniform `O_A(1)` packet mass and shadow-target congestion, or instead
   explicit cross-core necklace circuits giving the cancellation quantified
   in (11.18);
7. one balanced exact factor, and therefore any literal contiguous-OR word,
   arising from this lane.

The clean Catalan reservoir has therefore solved supply but not the
dependent Gaussian rebundling gate.  The obstruction is now exact: the
canonical ownership dependencies are either topologically too coarse
(two-piece rigidity), too long (full cyclic monodromy), or, for a separated
rotation packet with nonzero seed increment, orthogonal to the first-shadow
cancellation that packet would need.  Any successful PBBS proof
must introduce genuinely nonlocal extra-cut cross-core circuits whose
necklace charges cancel simultaneously across the Gaussian window.

## 13. Independent audit record

The decisive arguments were separately audited in three blocks before
this report was closed.

- The topology audit verified Theorems 2.1, 3.1, 3.2, and 4.1, and removed
  an initially proposed unrestricted `2k+2a` piece-count claim because
  neutral pieces and non-atomic extra cuts invalidate it.
- The rotation audit verified the sharpened interval (5.3), the exact bad
  core count (5.5), both orthogonality identities, the cyclic-design and
  Fourier kernels, and the constants in Theorem 7.1.  It also forced the
  explicit caveat that `delta_{K,1} != 0` is unproved.
- The dependency audit verified Sections 8-10, supplied the exact abstract
  sharpness construction, and corrected the normalization in Theorem 11.3
  so that its packet directions are explicitly half endpoint increments.

No audit treats an algebraic ownership relation as a legal endpoint trade,
an integral spanning `2`-factor as an exact wreath factor, or an abstract
load-system obstruction as a PBBS counterexample.
