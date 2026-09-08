# Thread A: general odd-k MMM shadow-path decoration recursion

Date: 2026-07-29

Status: exact construction criterion and exact deterministic recursion for the
full rotation-equivariant strict-spiral owner-factor class; rigorous obstruction to the
natural MMM gluing-tree/parallel-label decoration class.  This note does
**not** prove that the recursion accepts for every odd `k`, and it does not
claim the exact contiguous-OR formula from a cyclic carrier alone.

## 0. Result and proved boundary

For every odd

\[
 k=2m+1\ge3,\qquad r=m+1,\qquad
 \mathcal L=\binom{\mathbb Z_k}{r-1},\qquad
 \mathcal U=\binom{\mathbb Z_k}{r},\qquad
 W=\binom{k}{r},\qquad N=W/k=\operatorname {Cat}_m,
\tag{0.1}
\]

the Merino--Mička--Mütze theorem supplies a rotation-equivariant strict
middle-levels spiral with perfect lower depth-one ownership.  The rigorous
advance here is the following.

1.  An oriented owner-exact factor is exactly a pair of equivariant
    extension bijections.  These two bijections determine one successor
    permutation \(\sigma\) on \(\mathcal U\).
2.  Every deeper lower and upper state path is then forced by

    \[
      \lambda_{q+1}(X)=X\cap\lambda_q(\sigma X),
      \qquad
      \mu_{q+1}(X)=X\cup\mu_q(\sigma X).
      \tag{0.2}
    \]

    Thus there is no independent deep-shadow decoration after the
    depth-one diamonds have been chosen.
3.  The full residence and fixed-depth shadow data form a finite associative
    endpoint-typed path-signature semigroupoid.  Quotient concatenation is a
    semidirect product by rotation; in particular the closing prefix must be
    rotated by the accumulated voltage.
4.  Enumerating sign-compatible alternating-circuit sums from one MMM factor
    and retaining the lexicographically first accepting signature is a
    deterministic, terminating, necessary-and-sufficient recursive rule for
    the entire equivariant strict-spiral class.
5.  For composite odd `k`, the lift condition is

    \[
       \gcd(v,k)=1,
       \tag{0.3}
    \]

    not merely `v != 0`.  Target stabilizers also force witness-load
    divisibility.

This does **not** give an unconditional all-odd construction.  In fact, the
complete audited natural MMM gluing-tree family fails the joint constraints
already at `k=11`.  Therefore any positive theorem within this equivariant
owner-factor route must use unrestricted alternating-circuit choices outside
that family, or the broader component-and-seam architecture exhibited by the
exact `k=13` certificate.  Architectures outside this route are not excluded.

## 1. Equivariant diamonds and the owner successor

Let `rho` be rotation by one coordinate.  Both central actions in (0.1) are
free.  Indeed, a subset fixed by a nonidentity rotation is a union of cycles
of some length `s>1` dividing `k`, hence its cardinality is divisible by
`s`; but

\[
 \gcd(k,m)=\gcd(k,m+1)=1.
\tag{1.1}
\]

### Theorem 1.1 (diamond parametrization)

Suppose that for each \(L\in\mathcal L\) we choose distinct coordinates

\[
 a_L,b_L\notin L
\tag{1.2}
\]

equivariantly under `rho`, such that both maps

\[
 p^-(L)=L\cup\{a_L\},
 \qquad
 p^+(L)=L\cup\{b_L\}
\tag{1.3}
\]

are bijections from \(\mathcal L\) to \(\mathcal U\).  Then

\[
 \sigma=p^+\circ(p^-)^{-1}
\tag{1.4}
\]

is a rotation-equivariant permutation of \(\mathcal U\); every arrow
\(X\to\sigma X\) is a Johnson edge; and

\[
 X\longmapsto X\cap\sigma X
\tag{1.5}
\]

is a bijection from \(\mathcal U\) to \(\mathcal L\).  Thus every lower
depth-one owner occurs exactly once.

Conversely, every oriented rotation-equivariant Johnson 2-factor for which
(1.5) is a bijection arises uniquely from (1.2)--(1.4), once a
rotation-compatible orientation has been fixed on each component orbit.

#### Proof

If `X=p^-(L)`, then `sigma X=p^+(L)`.  The two sets are distinct extensions
of the same `(r-1)`-set, so they are Johnson adjacent and their intersection
is exactly `L`.  Since `p^-` and `p^+` are bijections, `sigma` is a
permutation.  Equivariance of the data gives equivariance of `sigma`.

Conversely, orient each component orbit coherently under rotation and put

\[
 L_X=X\cap\sigma X.
\]

The lower-rainbow assumption makes `X -> L_X` a bijection.  Define
`p^-(L_X)=X` and `p^+(L_X)=sigma X`; these are bijections and recover the
factor.  Their two added coordinates are distinct because the Johnson edge
is nontrivial.  Uniqueness is immediate.  \(\square\)

The two selected incidences over `L` will be called its **diamond**.  The
theorem shows why independent rankwise balancing is not a chronology: one
common family of diamonds must generate every depth.

## 2. The forced all-depth shadow tower

For \(X\in\mathcal U\), define

\[
 \lambda_0(X)=\mu_0(X)=X
\tag{2.1}
\]

and, for `q>=0`,

\[
 \lambda_{q+1}(X)=X\cap\lambda_q(\sigma X),
 \qquad
 \mu_{q+1}(X)=X\cup\mu_q(\sigma X).
\tag{2.2}
\]

### Theorem 2.1 (forced common-successor recursion)

For every `q>=0`,

\[
 \lambda_q(X)=\bigcap_{j=0}^{q}\sigma^jX,
 \qquad
 \mu_q(X)=\bigcup_{j=0}^{q}\sigma^jX.
\tag{2.3}
\]

Consequently, for `1<=q<=m`, the following are equivalent.

* Every rank-`r-q` target has a lower `q`-edge state path.
* Equivalently,
  \[
    \operatorname {im}\lambda_q
       \supseteq\binom{\mathbb Z_k}{r-q}.
    \tag{2.4}
  \]

Likewise the following are equivalent.

* Every rank-`r+q` target has an upper `q`-edge state path.
* Equivalently,
  \[
    \operatorname {im}\mu_q
       \supseteq\binom{\mathbb Z_k}{r+q}.
    \tag{2.5}
  \]

The full depth-one diamond

\[
 \bigl(X\cap\sigma X,\ X\cup\sigma X\bigr)
\tag{2.6}
\]

determines `sigma X`; hence (2.2) leaves no independent decoration at any
larger depth.

#### Proof

Equation (2.3) follows from (2.2) by induction.  A lower target `S` occurs
as `lambda_q(X)` exactly when the consecutive states

\[
 X,\sigma X,\ldots,\sigma^qX
\]

are all supersets of `S` and have intersection `S`; this is precisely a
lower state-path witness.  The union proof is dual.  Finally, if both terms
of (2.6) and `X` are known, then

\[
 \sigma X=(X\cap\sigma X)
       \cup\bigl((X\cup\sigma X)\setminus X\bigr),
\]

so the successor, and then every expression in (2.2), is forced.  \(\square\)

This theorem uses the physical masks themselves, rather than an incomplete
catalogue of deletion/insertion templates.  In particular it retains the
valid same-outer-added-to-the-centre lower-`q=2` paths exhibited by the
audited `k=11` target orbit represented by `201`.  One physical witness is

\[
 (u,v,w)=(1590,1650,630),\qquad u\cap v\cap w=562,
\]

with \(u\setminus v=w\setminus v=\{2\}\), although the directed insertion
labels along \(u\to v\to w\) are `6` and `2`.  Thus this is not a repeated
directed insertion or a residence defect.  A blanket outer-addition
distinctness DNF would incorrectly delete all eleven rotated witnesses.

### Residence

Write the unique exchanged coordinates as

\[
 a(X)\in X\setminus\sigma X,
 \qquad
 b(X)\in\sigma X\setminus X.
\tag{2.7}
\]

Call the carrier **`d`-delay resident** if a coordinate inserted by one
transition is not deleted in any of the next `d` transitions.  Equivalently,
each resulting positive coordinate run has at least `d+1` central states.

### Lemma 2.2 (exact residence equations)

The carrier is `d`-delay resident if and only if

\[
 b(X)\ne a(\sigma^tX)
 \qquad
 (X\in\mathcal U,\ 1\le t\le d).
\tag{2.8}
\]

#### Proof

The coordinate `b(X)` first appears in `sigma X`.  Its deletion at the
transition out of `sigma^tX` is exactly the equality
`b(X)=a(sigma^tX)`.  Thus one of the first `d` possible deletions occurs if
and only if one of the equalities in (2.8) occurs.  \(\square\)

### Scope of the upper condition

Condition (2.5) is an exact fixed-depth state-path condition and is always a
sufficient certificate for contiguous upper coverage.  It is not the exact
same notion as arbitrary-length interval coverage for all `q`.

* At `q=2`, every Johnson interval with union of rank `r+2` contains a
  three-state subinterval with the same union.
* For every `q>=3`, there are Johnson paths of `q+2` states whose full union
  has rank `r+q`, while neither of their two `(q+1)`-state subpaths has that
  union.

These are Theorems 5.1 and 6.1 of
`MATH_CODE_AUDIT_AD_UPPER_SHADOW_STATE_PATH_20260729.md`.  Therefore (2.5)
is a legitimate strong construction target, but failure of (2.5) for
`q>=3` is not a no-go for arbitrary contiguous-OR coverage.  Section 5 below
gives the exact variable-length replacement.

## 3. Composite odd `k`: voltage and orbit multiplicity

Let an oriented quotient successor component have length `n`, and choose a
section of the cyclic cover.  After one quotient lap, suppose its lift has
shifted by \(v\in\mathbb Z_k\).

### Theorem 3.1 (exact lift count)

The physical lift of that quotient component has

\[
 \gcd(k,v)
\tag{3.1}
\]

cycles, each of length

\[
 n\,\frac{k}{\gcd(k,v)}.
\tag{3.2}
\]

In particular a connected quotient factor is one physical strict spiral if
and only if

\[
 \boxed{\gcd(k,v)=1.}
\tag{3.3}
\]

#### Proof

Successive quotient laps act on the sheet group \(\mathbb Z_k\) by addition of
`v`.  Its orbits are the cosets of the subgroup generated by `v`; this
subgroup has order `k/gcd(k,v)` and index `gcd(k,v)`.  Multiplying the number
of laps in one sheet orbit by \(n\) gives (3.2).  \(\square\)

Thus `v != 0` is sufficient only when `k` is prime.  Multiplication of
coordinates by a unit and reversal replace `v` by `cv` and `-v`,
respectively, and preserve `gcd(k,v)`; affine relabelling cannot repair a
nonunit voltage.

Off the two central levels, target orbits need not have size `k`.

### Lemma 3.2 (stabilizer-weighted witness load)

Let `S` be any target, with stabilizer

\[
 H_S=\{g\in C_k:\rho^gS=S\}.
\tag{3.4}
\]

Suppose an equivariant family of based state paths contains `c` quotient
path orbits whose target lies in the orbit of `S`.  Then every physical
target in that orbit has load exactly

\[
 c\,|H_S|.
\tag{3.5}
\]

#### Proof

The action on the based central starts is free.  Rotate one based witness
through all `k` phases.  Its target runs through the orbit of `S`, and it
returns to `S` precisely for the elements of `H_S`.  Hence one based path
orbit contributes `|H_S|` witnesses to each target in the orbit.  Sum over
the \(c\) path orbits.  \(\square\)

It follows that an equivariant construction generally cannot give exactly
one witness to a short-orbit target.  Coverage must be tested on the actual
Burnside orbits, with (3.5) used whenever multiplicity matters.

There is also an exact lower bound on the memory needed by a serial voltage
recursion.

### Lemma 3.3 (unit-voltage memory)

Let

\[
 U_k=\{u\in\mathbb Z_k:\gcd(u,k)=1\}.
\]

Declare two prefix totals `a,b` equivalent when every continuation `c`
satisfies

\[
 a+c\in U_k\quad\Longleftrightarrow\quad b+c\in U_k.
\tag{3.6}
\]

Then the equivalence classes are exactly the cosets of

\[
 \operatorname {rad}(k)\mathbb Z_k,
\tag{3.7}
\]

so there are exactly `rad(k)` classes.  For the unrestricted additive
continuation alphabet in (3.6), a serial exact unit-test therefore needs at
least `rad(k)` states, and needs `k` states when `k` is squarefree.  A
particular restricted dart-voltage alphabet may induce fewer distinguishable
prefix states.

#### Proof

Writing \(h=b-a\) and substituting \(u=a+c\), condition (3.6) says exactly
that translation by \(h\) stabilizes \(U_k\).
Adding a multiple of every prime divisor of `k` preserves divisibility or
nondivisibility by each such prime, and therefore preserves membership in
`U_k`.  Conversely, if a translation `h` is not divisible by some prime
`p|k`, the Chinese remainder theorem gives a unit `u` with
`u=-h (mod p)` and with `u` nonzero modulo every other prime divisor of
`k`.  Then `u` is a unit and `u+h` is not.  Hence the translation stabilizer
of `U_k` is exactly (3.7), and its cosets are precisely the equivalence
classes in (3.6).  \(\square\)

For physical phase reconstruction one should retain the full residue modulo
`k`, even though `rad(k)` states suffice for the terminal unit predicate.

## 4. The exact finite shadow-signature recursion

Fix a maximum required depth `H<=m` and a residence delay `d`.  A
**half-open decorated block** is

\[
 P=(X_0,e_0,X_1,e_1,\ldots,X_{\ell-1},e_{\ell-1};Y_P),
\tag{4.0}
\]

where `e_i` has head `X_(i+1)` for `i<ell-1`, while the last stored dart
`e_(ell-1)` has head `Y_P`.  The exit state `Y_P` is not repeated among the
listed vertices; it is the first state of the next compatible block.  Thus
every selected dart, including a seam or a quotient-lap closing dart, belongs
to exactly one half-open block.  Parallel quotient darts remain distinct.

For the vertex word of `P`, define

\[
 \mathcal L_q(P)=
 \left\{\bigcap_{j=0}^{q}X_{i+j}:0\le i<\ell-q\right\},
\tag{4.1}
\]

\[
 \mathcal U_q(P)=
 \left\{\bigcup_{j=0}^{q}X_{i+j}:0\le i<\ell-q\right\}.
\tag{4.2}
\]

Let the voltage-free boundary signature `A_(H,d)(P)` contain

1. the entry and exit quotient types and their physical boundary masks;
2. the first and last `min(H,ell)` listed vertices, in order;
3. the first and last `min(d,ell)` directed darts, including the stored
   outgoing dart;
4. a bit recording any residence violation whose two darts lie in the
   block; and
5. the two families (4.1)--(4.2) for every `1<=q<=H`.

It also records `ell` clipped at `max(H,d)+1`.  Separately let `g(P)` be the
accumulated phase displacement.  The complete typed signature is the pair

\[
 \Sigma_{H,d}(P)=\bigl(A_{H,d}(P),g(P)\bigr).
\tag{4.2a}
\]

### Lemma 4.1 (associative endpoint-typed concatenation)

If the exit of `P` is the entry of `Q`, their concatenation uses the already
stored final dart of `P` and does not duplicate the boundary state.  Its
signature is determined uniquely by the two typed signatures.  For each
`q`, the new shadow values which occur in neither factor are exactly

\[
 \left(\bigcap\operatorname {suf}_s(P)\right)
 \cap
 \left(\bigcap\operatorname {pre}_{q+1-s}(Q)\right),
\tag{4.3}
\]

and

\[
 \left(\bigcup\operatorname {suf}_s(P)\right)
 \cup
 \left(\bigcup\operatorname {pre}_{q+1-s}(Q)\right),
 \qquad 1\le s\le q,
\tag{4.4}
\]

whenever the indicated suffix and prefix exist.  New residence failures are
determined by the last `d` darts of `P` and the first `d` darts of `Q`.
Consequently the signatures form a finite associative semigroupoid under
endpoint-compatible concatenation.  Declaring every incompatible product
to be one absorbing symbol \(\perp\) gives a total finite associative
semigroup.

#### Proof

Every `(q+1)`-vertex subpath of `PQ` is contained in `P`, contained in `Q`,
or crosses their unique boundary.  In the last case it uses a suffix of
`s` vertices and a prefix of `q+1-s` vertices, giving exactly (4.3)--(4.4).
The first and last `H` vertices determine the new boundary lists.  An
inequality in (2.8) can change truth at concatenation only when its insertion
dart and deletion dart lie on opposite sides of the boundary, at distance
at most `d`, so the two dart collars suffice.  The stored outgoing dart of
`P` fixes the joining transition, including its parallel-edge phase label;
no external seam choice is suppressed.  Phase displacement adds.  These
rules compute the signature of the actual concatenated half-open word, so
associativity follows from associativity of word concatenation.  Finiteness
follows because \(k,H,d\) and all target families are finite.  \(\square\)

### The quotient twist

If normalized quotient blocks have accumulated shifts `g,h`, rotate the
second block to the physical exit phase of the first.  Their correct typed
product is

\[
 (A,g)\star(B,h)=\bigl(A\cdot\rho^g B,\ g+h\bigr),
\tag{4.5}
\]

when the rotated endpoints match, and is \(\perp\) otherwise.  Here `A` and
`B` are the voltage-free data in (4.2a), so voltage is not double-counted.

Let one quotient lap have voltage-free signature `A`, contain all `N`
quotient states and all `N` selected darts as in (4.0), and have its last
dart point to `rho^v X_0`.  Put `c=gcd(k,v)`.  One physical lift cycle,
arising from one sheet coset, is
evaluated from

\[
 \operatorname {Cyc}\!\left((A,v)^{k/c}\right).
\tag{4.6}
\]

The full lift is the union of the `c` rotated sheet-coset copies.  In the
strict case `c=1`, (4.6) is the whole physical cycle.  The operator `Cyc`
uses the stored final outgoing dart and compares the terminal suffix/dart
collar with the initial prefix/dart collar.  In particular, after one lap
the relevant prefix is `rho^v Pref(A)`, not `Pref(A)`.  Formula (4.6)
handles without exception the small cases in which a depth-`H` window
crosses more than one quotient boundary.

### Theorem 4.2 (deterministic complete decoration recursion)

Fix an MMM quotient factor `F_0` in the full phase-labelled quotient
middle-levels multigraph.  Fix total orders on its darts, orientations, and
binary switch vectors.  Perform the following finite recursion.

1. Enumerate in lexicographic order every

   \[
      z\in\{-1,0,1\}^{E}
   \]

   satisfying

   \[
      Bz=0,
      \qquad z_e=-1\Rightarrow e\in F_0,
      \qquad z_e=+1\Rightarrow e\notin F_0,
      \tag{4.7}
   \]

   where `B` is the full two-shore incidence matrix.  Put
   `F=F_0+z`.
2. Retain only connected quotient factors and orient each retained cycle in
   both possible directions.
3. Contract every two-dart passage through a lower quotient vertex,

   \[
      X\longrightarrow L\longrightarrow Y,
   \]

   to one directed upper-shore Johnson dart `e:X->Y`, with voltage equal to
   the sum of the two inclusion-dart voltages.  Write this contracted
   traversal as half-open upper-owner atoms `(X,e)`, each containing its
   selected outgoing Johnson dart, and recursively multiply their typed
   signatures by (4.5) and Lemma 4.1.
4. Accept exactly when

   \[
      \gcd(v,k)=1,
      \tag{4.8}
   \]

   the cyclic signature has no residence defect, and for every
   `1<=q<=H` it contains every actual target orbit in

   \[
      \binom{\mathbb Z_k}{r-q}
      \quad\hbox{and}\quad
      \binom{\mathbb Z_k}{r+q}.
      \tag{4.9}
   \]

Return the lexicographically first accepting factor, or `NONE` if the
finite recursion is exhausted.

Then the returned object, if any, is an equivariant strict spiral with exact
middle ownership, `d`-delay residence, and every lower and upper fixed-depth
state path through `H`.  Conversely, every equivariant strict spiral with
those properties occurs in the recursion.  Thus `NONE` is an exact no-go
for this full symmetric carrier class, not merely for the MMM gluing family.

#### Proof

The alternating-circuit generation theorem says that (4.7) is precisely the
set of binary owner-exact quotient factors: for any second factor `F_1`,
`z=1_(F_1)-1_(F_0)` satisfies (4.7), and every such `z` is a sign-compatible
sum of alternating even circuits.  Connectedness and Theorem 3.1 give one
physical cycle exactly under (4.8).  Lemma 4.1 and the twisted product (4.5)
compute all physical residence and shadow windows, including quotient and
physical closing seams.  Theorem 2.1 identifies (4.9) with the requested
state paths.  The search space and signature space are finite, so the rule
terminates and the fixed total orders make it deterministic.  \(\square\)

This is an exact recursive constructor/decision procedure, not an efficient
algorithm and not an existence proof.  A compressed bottom-up implementation
would also have to retain the complete open-component pairing/connectivity
state and parallel-dart compatibility; the displayed shadow signature alone
does not encode those factor constraints.  Coverage must be tested at the
root: the `k=13` artifacts show that exact support can be lost and recovered
nonmonotonically along the exhibited repair.

## 5. Exact arbitrary-upper-interval augmentation

If the goal is literal arbitrary-length upper coverage rather than the
strong fixed-depth condition (2.5), augment each path signature by

* its total union;
* every nonempty prefix and suffix union, with length; and
* every internal interval union.

For path concatenation,

\[
\begin{aligned}
 \operatorname {Tot}(PQ)
   &=\operatorname {Tot}(P)\cup\operatorname {Tot}(Q),\\
 \operatorname {Pref}(PQ)
   &=\operatorname {Pref}(P)\cup
     \{\operatorname {Tot}(P)\cup A:A\in\operatorname {Pref}(Q)\},\\
 \operatorname {Suff}(PQ)
   &=\operatorname {Suff}(Q)\cup
     \{A\cup\operatorname {Tot}(Q):A\in\operatorname {Suff}(P)\},\\
 \operatorname {Int}(PQ)
   &=\operatorname {Int}(P)\cup\operatorname {Int}(Q)\\
   &\qquad\cup
     \{A\cup C:A\in\operatorname {Suff}(P),
                    C\in\operatorname {Pref}(Q)\}.
\end{aligned}
\tag{5.1}
\]

In every cross term, the stored length is the sum of the two constituent
lengths.  Lengths disambiguate the full-cycle interval from a proper interval, and
the semidirect rotation (4.5) is applied to every set in the signature.
At final cyclic closure on `W` physical positions, a suffix of length `a`
may be joined to a prefix of length `b` only when

\[
 1\le a+b\le W.
\tag{5.2}
\]

The based lengths are retained, so (5.2) prevents a purported interval from
wrapping far enough to reuse a position.  With this restriction, the same
three-case proof as Lemma 4.1 proves (5.1) and its cyclic closure.  This is
the exact prefix/suffix/interval alternative to the too-strong upper
condition (2.5) for `q>=3`.

## 6. The strict and component-and-seam construction theorems

The preceding results can be packaged as the following exact conditional
construction statement.

### Theorem 6.1 (strict all-depth carrier criterion)

For a fixed odd `k`, residence delay `d`, and MMM base factor `F_0`, the
following are equivalent.

1. There exists a rotation-equivariant strict spiral with perfect lower
   depth-one ownership, `d`-delay residence, and every lower/upper
   fixed-depth state path through depth `m`.
2. There exists a sign-compatible alternating-circuit sum `z` from `F_0`
   such that `F_0+z` is connected, has unit voltage modulo `k`, and its
   forced arrays (2.2) satisfy (2.4)--(2.5) for every `1<=q<=m`.
3. The recursion in Theorem 4.2 with `H=m` returns a factor.

#### Proof

The equivalence of 2 and 3 is Theorem 4.2.  The implication 2 to 1 follows
from Theorems 1.1, 2.1, and 3.1.  Conversely, expand the strict spiral to its
oriented two-shore factor and subtract `F_0`; the alternating-cycle theorem
gives the required sign-compatible `z`, while its physical properties give
the terminal conditions.  \(\square\)

The exact `k=13` construction shows that condition 1 is stronger than the
architecture needed for an optimal word.  The broader exact variant is:

* allow a quotient 2-factor with components `C_j` and voltages `v_j`;
* lift `C_j` into `gcd(k,v_j)` physical cycles by Theorem 3.1;
* cut and splice those cycles by specified Johnson seams; and
* apply the same signature semigroupoid to the resulting ordered physical
  segments, with every seam included.

Acceptance of the final path/cycle signature is again sufficient, and is
necessary within the specified splice catalogue.  This is not merely a
formal relaxation: the exact `k=13` source has quotient component lengths
`119` and `13`, voltages `8` and `6`, hence physical cycles of lengths
`1547` and `169`.  One certified physical seam joins them, preserves every
upper depth and every lower depth at least two, and leaves one lower-q1 hole
for the exact compiler.  Thus quotient Hamiltonicity must be labelled a
sufficient subclass, not a necessary general-odd hypothesis.

## 7. Exact obstruction to natural MMM edge decoration

### Theorem 7.1 (audited finite-family obstruction)

No deterministic rule whose range is confined to the natural MMM
gluing-tree factors and their parallel-edge labels can produce the required
depth-three-resident, lower-q2-complete, upper-q1-complete strict carrier for
every odd `k`.  Here depth-three residence means `d(11)=3`, equivalently
minimum positive-run length four, at the obstructing `k=11` instance.

#### Proof

The independently audited `k=11` enumeration in
`MATH_AUDIT_MMM_GLUING_SWITCH_PARAMETRIZATION_20260729.md` contains

* every labelled spanning tree in the full MMM plane-tree auxiliary
  multigraph;
* every simultaneous gluing toggle yielding a quotient Hamilton cycle; and
* every parallel-edge label and every unit-voltage lift.

It finds exactly 74 quotient-Hamilton gluing-tree occurrences, 1496
parallel-labelled variants, and 1360 unit-voltage variants.  The separate
minima for upper-q1 holes and lower-q2 holes are zero, but the minimum number
of forbidden short runs is 143, and no member passes all three gates.
Therefore the entire stated family fails at `k=11`.  \(\square\)

This theorem is family-exact; its counts are frozen in the hashed audit note,
although no separate frozen stdout census was found.  It does not rule out
the full alternating-circuit class of Theorem 4.2.  The distinction is
material.  The comparison of one good `k=11` factor with the dynamically
downloaded canonical MMM payload changes `41/42` lower choices; that payload
was audited but not frozen locally.  The fully local comparison between the
two stored good carriers changes `42/42` choices.  Either comparison exhibits
a quotient-global rethreading, but only the latter is a wholly frozen
artifact fact.

There is a second, independent fixed-order obstruction at composite
`k=15`.  The canonical shift-one factor misses 550 rank-nine targets, which
form 38 rotation orbits.  Every rank-nine interval witness already contains
an adjacent Johnson edge with that union, so an upper-complete repair must
insert at least 38 new quotient edge orbits.  The entire phase-labelled
quotient incidence graph has 3404 singleton endpoint groups and only 14
double endpoint groups.  Hence any fixed quotient factor meets at most 14
places admitting a parallel-label substitution.  These endpoint groups are
not contracted Johnson self-loops.  Thus label/voltage decoration of that
fixed order cannot be upper-complete; global successor changes are forced.

## 8. Constraints extracted from the exact `k=11` and `k=13` artifacts

The theorem above is calibrated against the following exact constraints.

### `k=11`

* The strict equivariant carrier has quotient length 42 and voltage `2`.
* Its physical lift is one 462-cycle, is depth-three resident, and has
  complete lower and upper shadows at all depths.
* Its upper-q1 physical loads are `1^198 2^132`.
* A safe opening can lose one lower-q1 and one lower-q2 witness while an
  exact common compiler still produces the optimal word of length 465.
* The final compiled word is not itself equivariant.  Carrier equivariance
  must not be silently imposed on the compiler.

Frozen word:

```text
scratch/sigma_sat_k11_465.word
SHA-256 746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850
```

### `k=13`

* The exact source is a two-component equivariant factor, not a strict
  quotient spiral.
* Component voltages are `8,6`; at prime 13 both are units.
* The physical source cycles have lengths `1547,169` and complete all-depth
  shadows with depth-three residence.
* Of 24960 two-cut orientations, 6032 preserve all upper shadows and 1092
  also satisfy the exact linear depth-three factorability/residence identity
  `D^3 P=T`.  The selected seam loses one lower-q1 colour, which the exact
  compiler repairs.
* Upper-q1 loads are `1^936 2^273 3^78`; a cap-two decoration rule would
  wrongly exclude the exact certificate.

Frozen hashes:

```text
two-component source
2987fe2e3ef6de56c538038688835246e6aafafc5c6a7dd576b3df986ee44ef9

selected seam/path
baa204bf8208c531cc1905c6cf53a2438db85a0b778231c0e59a631eef4b7973

Hall audit
2a7b7eb4ece4711214dd24f93ad216f8d77dd53c27bd7edda0162b3059f8c137

optimal word
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0
```

These artifacts impose narrower, exact design constraints.  Their displayed
carriers are not described by one fixed run gap; the displayed `k=13`
carrier is incompatible with an upper-load cap of two; quotient
Hamiltonicity is unnecessary for that optimum; its final compiled word is
not forced to remain equivariant; and the exhibited repair history is
nonmonotone.  They do not exclude every different fixed-gap or monotone
construction, nor a theorem that always finds some other Hamilton carrier.
They are compatible with the exact signature recursion because it retains
masks, component voltage, chronology, and boundary signatures jointly.

## 9. Minimum remaining hypothesis

The smallest unproved strict-spiral statement exposed by this note is the
following.

> **Accepting alternating-circuit lemma `AEC(k,d(k))`.**  Fix a prescribed
> admissible delay function with `1<=d(k)<=m`.  For every odd `k=2m+1`, some
> sign-compatible alternating-circuit sum from an MMM base factor has
> connected terminal quotient, voltage coprime to `k`, satisfies (2.8) at
> delay `d(k)`, and has forced images (2.4)--(2.5) for every `1<=q<=m`.

By Theorem 6.1 this lemma is necessary and sufficient for the requested
equivariant strict all-state-path carrier.  It is not proved.  Theorem 7.1
shows that it cannot be proved by selecting only among the natural MMM
gluing-tree/parallel-label outputs.

For exact contiguous-OR words, `AEC(k,d(k))` is deliberately stronger than
necessary on upper depths `q>=3`, and still does not solve two separate
linearization gates:

1. select cuts/seams which preserve the required cyclic witnesses; and
2. construct one common lower compiler satisfying the exact owner/Hall
   constraints.

The exact arbitrary-upper replacement is (5.1), and the `k=13`
component-and-seam theorem shows how one may tolerate compiler-repairable
lower boundary holes.  No constant-one or exact all-odd formula is claimed
here.

## 10. Adversarial audit

The strongest claim, Theorem 4.2, was checked against the following failure
modes.

1. **One-shore flow is insufficient.**  Equation (4.7) uses the full
   upper-and-lower incidence matrix.  Dropping the lower rows can preserve
   degree while destroying exact owner colours.
2. **The quotient seam is twisted.**  Formula (4.5) rotates the next prefix
   by the accumulated voltage; an unrotated closure gives wrong residence
   and shadow states.
3. **Composite voltage is tested by gcd.**  Nonzero nonunit voltage produces
   several physical cycles by Theorem 3.1.
4. **Short target orbits are weighted correctly.**  Lemma 3.2 prevents the
   false assumption that every off-central orbit has size `k` or admits
   load one.
5. **Higher depths are not independently balanced.**  The recursion uses
   the forced arrays (2.2), not separately selected marginal flags.
6. **The lower-q2 motif catalogue is not assumed complete.**  Full physical
   masks retain the audited same-insertion witnesses at `k=11`.
7. **Fixed-depth upper paths are not called necessary for arbitrary
   intervals when `q>=3`.**  Equation (5.1) is the exact alternative.
8. **Strict spirals are not called necessary for optimal words.**  The
   component-and-seam `k=13` certificate is an explicit counterexample to
   that architectural necessity.
9. **The finite recursion is not promoted to an existence theorem.**  Its
   termination proves only `factor or exact symmetric-class no-go`; the
   all-odd accepting-extension lemma remains open.
10. **The family-level no-go is not enlarged.**  The `k=11` census excludes
    the complete natural MMM gluing family, but not unrestricted
    alternating-circuit sums, unrelated non-equivariant architectures, or
    non-equivariant terminal seams.

After these qualifications, the exact positive theorem is stable: the
diamond data force one common successor, the semidirect signature recursion
tests every requested physical state path, and `gcd(v,k)=1` is the complete
strict-lift condition for every odd `k`.
