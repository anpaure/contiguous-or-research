# Equivariant necklace quotients and the strict k=11 spiral

Date: 2026-07-28

Status: independent proof audit of
`/Users/amir.nuriyev/Downloads/opusproblem/work`. The central-layer quotient
and voltage arguments are correct after two scope qualifications: freeness is
rank-dependent for composite `k`, and the scalar voltage criterion requires a
regular cyclic cover of a quotient cycle. The claimed strict k=11 identity is
exact for the derived carrier, not for the raw compiler word.

## 1. Freeness for odd composite k

Let `C_k=<rho>` act on the rank-`t` subsets of `Z_k` by translation.

### Theorem 1.1

For `0<t<k`, the action on the entire rank-`t` layer is free if and only if

```text
gcd(k,t)=1.
```

#### Proof

A nonidentity shift `rho^s` has order

```text
d = k/gcd(k,s) > 1.
```

Its coordinate cycles all have length `d`. Every invariant subset is a union
of these cycles, so its size is divisible by `d`. Thus `gcd(k,t)=1` excludes
every nontrivial stabilizer.

Conversely, let `d>1` divide `gcd(k,t)`. The shift by `k/d` has order `d` and
has `k/d` coordinate cycles. A union of any `t/d` of them is an invariant
rank-`t` subset. □

### Corollary 1.2 (the two central layers)

Put `k=2m+1`. Then

```text
gcd(k,m)=gcd(k,m+1)=1.
```

Hence the rank-`m` and rank-`m+1` actions are free for every odd `k`, prime
or composite. Their common physical size is

```text
W = C(2m+1,m)=C(2m+1,m+1)
  = (2m+1)/(m+1) C(2m,m)
  = k Cat(m).
```

Every orbit has size `k`, so both quotient layers contain exactly

```text
N=W/k=Cat(m)
```

orbits. This validates the central assertions in `equi.py` and `equisat.py`.
Equivalently, the cycle lemma sends each rank-`m+1` necklace to its unique
rotation with all signed prefix sums positive; deleting its first up-step
gives a Dyck word of semilength `m`.

## 2. Correct sizes away from the center

Freeness does not extend automatically to other ranks when `k` is composite.

### Theorem 2.1 (Burnside layer formula)

Let `n(k,t)` be the number of translation orbits of rank-`t` subsets. Then

```text
n(k,t) = (1/k) sum_{d | gcd(k,t)} phi(d) C(k/d,t/d).
```

#### Proof

There are `phi(d)` rotations of order `d`. Such a rotation has `k/d` cycles,
each of length `d`, and fixes a rank-`t` subset exactly when `d|t`; the fixed
set is then determined by choosing `t/d` of those cycles. Burnside's lemma
gives the formula. □

Complementation is equivariant, so `n(k,t)=n(k,k-t)`. In particular, deeper
lower and upper quotient layers must use this formula or explicit orbit
enumeration.

Two sharp counterexamples to all-layer freeness are:

```text
k=9:  {0,3,6} is fixed by +3; rank 6 has 10 orbits.
k=15: rank 9 has (C(15,9)+2C(5,3))/15 = 335 orbits,
      while the central ranks 7 and 8 each have Cat(7)=429.
```

Thus `quotient.py`'s phrase “assumes free action” is misleading as a general
layer statement. Its canonical-representative set still counts nonfree
orbits correctly; what fails is replacing the count by `C(k,t)/k`.

## 3. Voltage and gcd lifting

Use undirected multigraphs with darts: a loop has two incidences and degree
two, and parallel edges remain distinct.

### Theorem 3.1 (regular cyclic lift of a quotient cycle)

Suppose `C_k=<rho>` acts freely on the vertices of an invariant graph and
without edge inversions. Choose one representative `x_u` for every quotient
vertex. For an oriented quotient dart `e:u->v`, let `alpha(e) in Z_k` be
defined by saying that the lift of `e` leaving `x_u` ends at
`rho^alpha(e) x_v`. Then

```text
alpha(reverse(e))=-alpha(e).
```

For an oriented quotient cycle `C=e_0...e_(n-1)`, put

```text
v = sum_i alpha(e_i) mod k.
```

Its physical lift consists of exactly

```text
gcd(k,v)
```

cycles, each of length

```text
n k / gcd(k,v).
```

Therefore an invariant 2-factor lifts to one physical cycle if and only if
its quotient is connected and `gcd(k,v)=1`.

#### Proof

A lift starting at sheet `a` returns after one quotient circuit at sheet
`a+v`. The orbits of addition by `v` on `Z_k` number `gcd(k,v)` and each has
length `k/gcd(k,v)`. Multiplying by the quotient-cycle length gives the
displayed physical lengths. A connected finite 2-regular quotient multigraph
is one cycle, including the one-loop and two-parallel-edge conventions. □

Changing representatives by `x_u'=rho^(b_u)x_u` replaces an edge voltage by

```text
alpha'(e)=b_u+alpha(e)-b_v.
```

The sum around a cycle telescopes, so `v` is gauge invariant. Reversing the
cycle changes only its sign.

The hypotheses hold on the odd middle layers. Vertex freeness follows from
Theorem 1.1. If a group element inverted an undirected edge, its square would
fix an endpoint; freeness would give `g^2=1`, impossible in an odd-order group
unless `g=1`.

### Necessary qualifications

1. If every vertex has one common stabilizer/kernel `H`, use the effective
   group `C_k/H`. With `q=|C_k/H|`, the formula becomes
   `gcd(q,v_bar)` cycles of length `nq/gcd(q,v_bar)`.
2. With varying stabilizers or a non-covering edge orbit, edge labels are
   double cosets rather than elements of one cyclic group; there is no scalar
   gcd theorem.
3. For a connected quotient not known to be 2-regular, one voltage is not
   enough. If closed-walk voltages generate `L<=Z_k`, the derived graph has
   index `[Z_k:L]` components. Equivalently, for fundamental voltages
   `v_1,...,v_beta`, the number is `gcd(k,v_1,...,v_beta)`.

The shift convention in `cpsat.py`, `t=s_w-s_u`, is correct. Excluding
quotient self-loops is harmless for connected Hamilton quotients with more
than one vertex, but omits the `k=3`, one-vertex quotient boundary.
`equisat.py` leaves `cycle_voltage` as a stub but checks the physical cycles
directly. The unused `greedy_canon.py` helper ambiguously calls cumulative
shifts “cycle shifts”; its actual DFS closure uses the correct cumulative
voltage.

## 4. Exact k=11 spiral audit

Let `A` be `scratch/sigma_sat_k11_465.word`, with SHA-256

```text
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850.
```

This file is byte-identical to the `k11.word` loaded by the Opus scripts.
Define

```text
D(A)_i=A_i OR A_(i+1),
T=D^3(A),
rho(x)=((x<<1)|(x>>10)) & 2047.
```

Thus `T_i=A_i OR A_(i+1) OR A_(i+2) OR A_(i+3)`. Exact evaluation gives
`|T|=462=C(11,6)`. Put `N=462/11=42` and `R_i=T_i` for `0<=i<42`.

### Proposition 4.1 (strict spiral identity)

All 462 equalities

```text
T_(42j+i) = rho^(2j)(R_i),
0<=j<11, 0<=i<42,
```

hold. Equivalently,

```text
T_((q+42) mod 462)=rho^2(T_q)
```

for every `q`. Shift `2` is the unique shift in `Z_11` satisfying this.

Moreover:

* all 462 entries are distinct rank-six masks;
* the first 42 entries represent 42 distinct free rotation orbits;
* every orbit occurs exactly at `i+42j`, `0<=j<11`;
* every cyclic physical adjacency has intersection rank five;
* the quotient seam is `R_41=636 -> rho^2(R_0)=876`, also of intersection
  rank five; and
* `gcd(11,2)=1`, so Theorem 3.1 gives one 462-cycle.

This proves the claimed strict occurrence spacing and single-sheet spiral
lift. The exact derived carrier equals `work/k11_carrier.txt`.

The scope correction is essential: the raw 465-letter word `A` is not itself
equivariant. Exactly 54 of the 423 linear tests fail, beginning with

```text
A_42=76 != rho^2(A_0)=548.
```

## 5. Reproducible certificate

The standalone checker
`scratch/audit_opus_equivariant_quotient_k11.py` performs only small exact
orbit counts and certificate comparisons. Its output is
`scratch/audit_opus_equivariant_quotient_k11.json`. It verifies the composite
examples, all 462 strict spiral equalities, cyclic Johnson adjacency, the
unique voltage, and the raw-word countercheck. No SAT solver or search is
invoked.
