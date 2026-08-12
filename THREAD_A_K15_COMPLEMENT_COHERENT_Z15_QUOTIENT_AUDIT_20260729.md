# Thread A: complement coherence in the k=15 cyclic quotient

Date: 2026-07-29

Status: theorem and frozen-cycle audit.  No search is used.  The theorem
identifies the exact symmetry which would merge the upper-q1 and lower-q2
gates.  The canonical Merino--Mička--Mütze shift-one cycle does not have that
symmetry.

## 1. Verdict

There are three distinct statements which must not be conflated.

1. At `k=15`, a complement-invariant Middle Levels Hamilton cycle exists.
2. A rotation-equivariant strict-spiral Middle Levels Hamilton cycle exists.
3. One cycle can have both symmetries with their exact sheet phases.

The first two statements are known separately.  They do not imply the third.
If statement 3 holds, complementation identifies upper depth `q` with lower
depth `q+1`, occurrence by occurrence.  In particular upper-q1 and lower-q2
become one cyclic raw-shadow gate.

For the canonical shift-one strict spiral, however, the two 550-element
missing families are not complements.  Their direct-complement overlap is
only 160.  The equality `550=550` is an equality of load histograms, not an
identification of targets.

The correct quotient condition is an antipodal self-duality of the selected
**alternating incidence cycle**, including its voltage carry.  It is not an
arbitrary offset or reversal of the Johnson quotient order.

## 2. The unconditional relation for an arbitrary Middle Levels cycle

Put `k=2m+1` and

\[
 W=\binom{k}{m+1}.
\]

Write a Middle Levels Hamilton cycle as

\[
 B_0,X_0,B_1,X_1,\ldots,B_{W-1},X_{W-1},
 \qquad X_i=B_i\cap B_{i+1},                         \tag{2.1}
\]

where `B_i` has rank `m+1`, `X_i` has rank `m`, and all indices are modulo
`W`.  The `X_i` enumerate the entire rank-`m` layer.  Define

\[
 U_i=B_i\cup B_{i+1},\qquad
 D_i=B_i\cap B_{i+1}\cap B_{i+2}=X_i\cap X_{i+1}.    \tag{2.2}
\]

Thus `U_i` is the upper-q1 trace and `D_i` is the lower-q2 trace.

Because the `X_i` are all distinct, there is a unique permutation
`pi in S_W` such that

\[
 X_{\pi(i)}=\overline{B_i}.                            \tag{2.3}
\]

### Proposition 2.1 (exact two-cycle relation)

For every `i`,

\[
 \boxed{\overline{U_i}
 =X_{\pi(i)}\cap X_{\pi(i+1)}.}                       \tag{2.4}
\]

Consequently the complemented upper-q1 word is the intersection-colour word
of the Johnson Hamilton cycle

\[
 X_{\pi(0)},X_{\pi(1)},\ldots,X_{\pi(W-1)},           \tag{2.5}
\]

whereas the lower-q2 word is the intersection-colour word of the original
Johnson Hamilton cycle `(X_i)`.

#### Proof

De Morgan and (2.3) give

\[
 \overline{U_i}
 =\overline{B_i}\cap\overline{B_{i+1}}
 =X_{\pi(i)}\cap X_{\pi(i+1)}.
\]

Consecutive complements in (2.5) are Johnson-adjacent because the
corresponding `B_i` are Johnson-adjacent.  This proves every assertion.
\(\square\)

If `M_U` and `M_D` denote the two missing families, Proposition 2.1 is the
exact general relation:

\[
 \overline{M_U}
 =\binom{[k]}{m-1}
   \setminus\{X_{\pi(i)}\cap X_{\pi(i+1)}:i\in\mathbb Z_W\},              \tag{2.6}
\]

\[
 M_D
 =\binom{[k]}{m-1}
   \setminus\{X_i\cap X_{i+1}:i\in\mathbb Z_W\}.                         \tag{2.7}
\]

Thus equal deficit cardinalities do not imply equal missing sets.  Equality
of missing sets is precisely equality of the two colour supports in
(2.6)--(2.7); equality of loads requires equality of their full colour
multisets.

## 3. Genuine complement coherence halves all cyclic shadow gates

Let set complementation preserve the cycle (2.1).  Its action on the abstract
cycle of length `2W` is an involutive dihedral automorphism which swaps the
two rank classes.

### Lemma 3.1 (complement cannot be a cycle reflection)

Set complementation cannot act as a reflection of the Middle Levels cycle.

#### Proof

A reflection which swaps the two bipartition classes has its axis through
two opposite edges and fixes those edges setwise.  A complement-fixed
inclusion edge would have endpoints `X subset B` with

\[
 X=\overline B,
\]

which is impossible for `m>0`, since `B` and `B^c` are disjoint.  A
vertex-axis reflection would preserve rather than swap the bipartition.
\(\square\)

It follows that complementation must be the unique nontrivial involutive
rotation, the half-turn.  Because it swaps the bipartition, `W` must be odd.
Write

\[
 W=2s+1.
\]

Then, after a cyclic reindexing,

\[
 \boxed{\overline{B_i}=X_{i+s},\qquad
        \overline{X_i}=B_{i+s+1}.}                     \tag{3.1}
\]

### Theorem 3.2 (all-depth complement duality)

For `q>=0`, put

\[
 U_i^{(q)}=\bigcup_{j=0}^{q}B_{i+j},\qquad
 L_i^{(q+1)}=\bigcap_{j=0}^{q+1}B_{i+j}.                \tag{3.2}
\]

Under complement coherence,

\[
 \boxed{\overline{U_i^{(q)}}=L_{i+s}^{(q+1)}}           \tag{3.3}
\]

for every `i,q`, including multiplicities.  Therefore

\[
 \boxed{\overline{M_q^+}=M_{q+1}^-}                    \tag{3.4}
\]

and the two load functions agree under complementation.

#### Proof

By (3.1),

\[
 \overline{U_i^{(q)}}
 =\bigcap_{j=0}^{q}X_{i+s+j}
 =\bigcap_{j=0}^{q}(B_{i+s+j}\cap B_{i+s+j+1})
 =L_{i+s}^{(q+1)}.
\]

Complementation is a bijection between the two target layers, proving
(3.4) with loads. \(\square\)

For `k=15,m=7`, (3.3) identifies upper-q1 rank 9 exactly with lower-q2
rank 6.  It does not identify either one with lower q1, and it says nothing
by itself about residence, a linear cut, common ownership, or compiler Hall.

Lucas' theorem gives

\[
 \binom{2m+1}{m}\equiv1\pmod2
 \iff m\mathbin{\&}(m+1)=0
 \iff m=2^a-1.                                         \tag{3.5}
\]

Thus the possible odd dimensions are precisely `k=2^(a+1)-1`; `k=15` is
the first live Mersenne case in the present problem.

## 4. The exact Z_k quotient constraint

Let rotation `rho` act freely on the two central layers, put `N=W/k`, and
write a connected alternating quotient cycle as

\[
 H_0,H_1,\ldots,H_{2N-1}.                              \tag{4.1}
\]

Choose the one-jump voltage gauge, extended to integer indices by

\[
 H_{t+2N}=\rho^vH_t,                                   \tag{4.2}
\]

where `v` is the quotient voltage.  A unit `v` gives one physical Hamilton
lift.

### Theorem 4.1 (antipodal quotient and forced carry)

If the physical lift is complement coherent, then on necklace classes

\[
 [\overline{H_t}]=[H_{t+N}],                            \tag{4.3}
\]

and on the chosen representatives

\[
 \boxed{\overline{H_t}=\rho^{mv}H_{t+N}}               \tag{4.4}
\]

with the right side interpreted using (4.2).  Equivalently, on a reduced
wrapped quotient position `0<=j<2N` and sheet `a`, complementation is

\[
 (j,a)\longmapsto
 \left(j+N\pmod{2N},\ a+b+v\mathbf1_{\{j\ge N\}}\right),
 \qquad b=mv,\quad 2b+v=0\pmod k.                      \tag{4.5}
\]

Conversely, the literal representative equalities encoded by (4.5), on
every selected incidence dart, give a complement-coherent physical lift.
The necklace relation (4.3) and the numerical congruence `2b+v=0` without
those literal equalities are not sufficient.

#### Proof

The physical complement is the half-turn by `W` alternating vertices.
Since

\[
 W=kN=(2m+1)N=N+m(2N),
\]

the half-turn advances `N` quotient positions and `m` complete quotient
laps.  Each lap adds sheet voltage `v`, proving (4.4).  Wrapping `t+N`
across the quotient seam adds one more `v`, which is (4.5).  Applying the
map twice gives `2b+v=0`; this also follows from `2m+1=k`.  The converse is
immediate by reversing the calculation. \(\square\)

At `k=15`,

\[
 N=429,\qquad h=(N-1)/2=214.
\]

Write `B_(i,a)=rho^a B_i` and `X_(i,a)=rho^a X_i` for the physical sheet
lifts of the upper and lower quotient representatives.

For voltage `v=1`, (4.5) becomes

\[
 \boxed{
 \overline{B_{i,a}}=
 \begin{cases}
  X_{i+214,a+7},&0\le i\le214,\\
  X_{i-215,a+8},&215\le i\le428.
 \end{cases}}                                           \tag{4.6}
\]

The `7/8` sheet jump is mandatory.  A test using only an affine permutation
of the 429 necklace representatives can therefore accept false modes or
reject a true mode if it ignores the carry.

There is also an order-free formulation.  In the alternating quotient,
require exact incidence-dart closure

\[
 (X\subset B)\text{ selected}
 \iff(\overline B\subset\overline X)\text{ selected},   \tag{4.7}
\]

including relative rotation labels.  Here the selected physical edge-orbit
set must be spanning and have degree two at every quotient vertex on both
central shores.  With those hypotheses, connectedness and unit voltage make
(4.7) equivalent to a complement-coherent strict spiral.  Complementation does not map one
contracted Johnson choice to one other contracted Johnson choice; it maps
the two incidence darts.  Hence (4.7) must be imposed before suppressing the
rank-`m` shore.  Exact labelled-dart closure makes the physical spanning
lift complement invariant; connectedness and unit voltage make it one
cycle, and Lemma 3.1 then forces the half-turn and the phases in
Theorem 4.1.

### Proposition 4.2 (the correct dihedral sign rule)

More generally, let a symmetry of a regular cyclic cover have the form

\[
K(i,a)=(\phi(i),\eta a+\beta_i),\qquad \eta\in\{1,-1\}.                 \tag{4.8}
\]

For an involution one must additionally have

\[
 \phi^2=1,\qquad \beta_{\phi(i)}+\eta\beta_i=0.          \tag{4.8a}
\]

Orient every quotient dart and use
`alpha_(e^(-1))=-alpha_e`.  For a dart `e:i->j`, let `alpha_(K(e))` mean
the voltage of the directed image dart `phi(i)->phi(j)`.  Exact lift
compatibility is

\[
 \boxed{\beta_j-\beta_i=\alpha_{K(e)}-\eta\alpha_e.}    \tag{4.9}
\]

If `K` maps an oriented quotient cycle `Q` to `Q'`, give `Q'` an independently
chosen orientation and let `epsilon` be the sign with which the image order
traverses it.  Then

\[
 \boxed{\epsilon v(Q')=\eta v(Q).}                      \tag{4.10}
\]

#### Proof

The image of the lifted dart

\[
 (i,a)\longrightarrow(j,a+\alpha_e)
\]

has sheet displacement

\[
 \eta\alpha_e+\beta_j-\beta_i,
\]

which proves (4.9).  Summing (4.9) around the cycle telescopes the beta
terms and gives (4.10). \(\square\)

For pure complement, `eta=1`; a self-component carrying the same nonzero
unit voltage must have `epsilon=1`, so reversal is impossible.  For
coordinate reflection followed by complement, `eta=-1`, and temporal
reversal is the compatible self-component branch.  This is the correct sense
in which the quotient constraint is dihedral: on a unit-voltage
self-component, the spatial normalizer sign and temporal orientation sign
must agree.

There is also a voltage-independent fixed-edge obstruction to a pure-
complement self-reversal.  Such a quotient reflection fixes two edge orbits.
If complementation carries a representative of one fixed orbit to its
`rho^c` translate, involutivity and commutation with `rho` give `2c=0`.
For odd `k`, `c=0`, so a physical inclusion edge would be literally fixed by
complementation, contradicting Lemma 3.1.  A reflected complement has
`eta=-1` and does not have this particular `2c` obstruction.

## 5. Exact audit of the canonical shift-one cycle

The frozen normalized chronology is

```text
scratch/mmm_knuth_k15_shift1_middle_levels.txt
```

with SHA-256

```text
0f42e4ba0ac0ec63e7f5edc8f1c3966208080b0fa58ebf7ea9552f84865a4e19.
```

It contains 12,870 distinct states, has cyclic Hamming distance one, and
contains every rank-7 and rank-8 set exactly once.  The lightweight checker

```text
scratch/threadA_audit_mmm_k15_complement_missing.py
```

has SHA-256

```text
3ca8f2dab05026dbbdd9275646861160b0a8408fdff66f71a09a838216ed7b21.
```

It gives

\[
 |M_U|=|M_D|=550,
\]

but

\[
 |\overline{M_U}\cap M_D|=160,
 \qquad |\overline{M_U}\mathbin\triangle M_D|=780.      \tag{5.1}
\]

Each missing family consists of 38 rotation orbits: 36 of size 15 and two
of size 5.  Only 12 orbits are common, ten of size 15 and both size-5
orbits.  Their canonical representatives are

\[
 429,591,633,723,845,873,1325,2349,3171,4683,4685,5285.                 \tag{5.2}
\]

Thus each family has 390 physical masks, or 26 necklace orbits, absent from
the other.

The standard coordinate reflection `j -> -j`, followed by complement,
improves the overlap only to 340 masks in 24 orbits.  It leaves 210 masks,
or 14 full orbits, unmatched on each side.  Testing every unit multiplier
of `Z_15` gives overlaps

\[
\begin{array}{c|rrrrrrrr}
a&1&2&4&7&8&11&13&14\\ \hline
|a(\overline{M_U})\cap M_D|&160&145&85&70&145&70&85&340.
\end{array}                                               \tag{5.3}
\]

Rotational offsets do not change these numbers because both missing
families are rotation invariant.  Hence no coordinate-dihedral map makes
the missing sets equal.

The equality `550=550` comes from the following exact but unaligned load
histograms.  For a rank-6 target `R`, let

\[
 u(R)=|\{i:\overline{U_i}=R\}|,
 \qquad \ell(R)=|\{i:D_i=R\}|.
\]

Both marginal histograms are

\[
 \#\{R:u(R)=t\}=\#\{R:\ell(R)=t\}
 =\begin{cases}
 550,&t=0,\\
 2475,&t=1,\\
 1980,&t=2.
 \end{cases}                                             \tag{5.4}
\]

Their joint table is

\[
\begin{array}{c|rrr}
 &\ell=0&\ell=1&\ell=2\\ \hline
u=0&160&285&105\\
u=1&285&1260&930\\
u=2&105&930&945
\end{array}.                                              \tag{5.5}
\]

The table is symmetric, but it is far from diagonal.  This is an exact
histogram identity, not targetwise complement coherence.

The permutation `pi` from (2.3) has 225 distinct physical increments.  Its
best translation agrees at only 45 of 6,435 positions.  After coordinate
reflection, the best temporal reversal agrees at only 270 positions.  No
rotation/reflection of coordinates combined with any temporal offset and
either temporal direction gives a global chronology mode.  Most sharply,
the forced plain-complement half-turn (3.1) holds at zero of the 6,435 upper
positions.  The canonical strict spiral therefore does not satisfy the exact
symmetry, and equality of its two marginal deficits supplies no global mode.

## 6. Strict spiral versus an equivariant 2-factor

A complement-coherent strict spiral is a connected unit-voltage solution of
(4.7).  Neither the general complement-antipodal existence theorem nor the
general rotational MMM theorem presently supplies that conjunction.
Equation (4.5) shows that there is no arithmetic phase obstruction at
`k=15`; the missing condition is the incidence self-duality itself.

A complement-closed equivariant 2-factor is genuinely more flexible.
Complement may

1. preserve a quotient component having an odd number of vertices on each
   shore, act by its half-turn, and satisfy `2b+v=0`; or
2. exchange two equal-length quotient components through an exact
   complement-labelled incidence isomorphism and sheet cocycle.

In the second case, equal voltages are necessary when the chosen orientation
of one component maps to the chosen orientation of the other; opposite
voltages are necessary when it maps to the reverse chosen orientation.
These voltage relations alone are not sufficient.

The self-component assertion uses oddness of the deck group.  A quotient
component of voltage `v` lifts to `gcd(k,v)` physical cycles, an odd number
when `k` is odd.  Complementation therefore fixes at least one physical
cycle.  Lemma 3.1 excludes a reflected action on that cycle, so it acts
antipodally.  If the quotient component has `n` vertices on each shore, the
fixed physical cycle has `nk/gcd(k,v)` vertices on each shore; this number
is odd exactly when `n` is odd.  Thus a complement-fixed quotient component
at `k=15` necessarily has the odd half-turn form above.

In either case, if all components and incidence phases are included, the
global cyclic upper-q/lower-(q+1) load identity remains exact.  Thus the
2-factor fallback can halve the cyclic raw-shadow gates even when no one
component is a complement-coherent Hamilton cycle.

This does not finish the finite construction.  Opening one component at one
seam destroys exact complement pairing at its antipodal seam; opening paired
components produces more than one path.  Component fusion or linearization
must therefore carry an explicit paired-seam collar, residence, owner, and
compiler-Hall ledger.  Complement coherence halves cyclic shadow tests, not
the endpoint-conditioned exact compiler gate.

## 7. Reproducibility

The audit is a single pass over the frozen 12,870-state chronology.  Run

```text
python3 scratch/threadA_audit_mmm_k15_complement_missing.py \
  15 1 scratch/mmm_knuth_k15_shift1_middle_levels.txt
```

It verifies the Middle Levels cycle before computing the two trace words,
all load tables, orbit profiles, affine-coordinate overlaps, and chronology
modes.  This takes less than one second locally and performs no optimization,
SAT solving, or exhaustive carrier search.
