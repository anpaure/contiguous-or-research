# The two-coordinate incidence gate is automatic

Date: 2026-07-31  
Status: complete all-`n>=4` theorem.  This closes the synchronized
**incidence** part of the `a=1` collar recursion for every child Catalan
linear forest.  It does not close the punctured side-degree or physical
linear-forest conditions.

## 0. Verdict

Let `F` be any oriented Catalan linear matching at parameter `n`.  For an
atom `q` write

```text
L_q = tail(q) intersect head(q),
U_q = tail(q) union head(q).
```

In the exact two-coordinate recursion, use the inherited ports

```text
p^-(U_q)=tail(q),                 p^+(L_q)=head(q).       (0.1)
```

For every `n>=4` there is **automatically** a set `Q subset F` of the
required order `Cat_(n+1)` for which both diagonal complements admit their
saturating containment matchings.  No symmetry of `F`, no special SCD and
no search are needed.

The proof has two ingredients.

1. A strengthened Kruskal--Katona chord inequality says that the dual of
   the two-step Boolean incidence transversal matroid has rank density at
   least `Cat_(n+1)/binom(2n,n-1)` on every family of at most
   `binom(2n,n-1)` middle sets.
2. Applying this bound to the tail and head injections makes Edmonds'
   common-basis inequality hold term by term.

Consequently Hypotheses 1--3 of Theorem 6.1 in
`MATH_THEOREM_CATALAN_BALANCED_SUBCUBE_RESERVE_AND_EXACT_COLLAR_DEFECT_20260731.md`
are automatic.  The exact remaining theorem is purely **physical**: choose
the common basis and its two saturating matchings so that the two punctured
side graphs obey the anchor degree caps and the total support is a linear
forest.

## 1. Constants and the two incidence matroids

Let `Omega=[2n]` and put

```text
X = C(Omega,n),        M=|X|=binom(2n,n),
N = binom(2n,n-1),     P=binom(2n,n-2),
z = M-N=Cat_n,
C = M-P=Cat_(n+1),     R=N-C.                           (1.1)
```

Let `T_down` be the transversal matroid on ground set `X` represented by
containment in the `P` sets of rank `n-2`: a family of middle sets is
independent when its members can be assigned distinct contained
`(n-2)`-sets.  Define `T_up` dually using distinct containing `(n+2)`-sets.
Complementation identifies the two matroids.  Each has rank `P` (for
example, an SCD saturates the smaller rank), so each dual has rank `C`.

For a family `A` of `n`-sets, write `partial_2 A` for its two-step lower
shadow.

## 2. The Catalan endpoint-bank lemma

### Lemma 2.1

For `n>=4`, every family `A subset X` of order at most `z=Cat_n` has an
injective assignment to distinct members of `partial_2 A`.  It also has an
injective assignment to distinct `(n+2)`-supersets.

### Proof

The empty subfamily is trivial.  For every nonempty `B subset A`, it is
enough by Hall to prove

```text
|partial_2 B| >= |B|                                  (2.1)
```

for every `B subset A`.  Write `|B|=binom(x,n)` with real `x>=n-1`.
Kruskal--Katona in Lovasz form gives

```text
|partial_2 B| >= binom(x,n-2).                         (2.2)
```

Moreover

```text
z = M/(n+1) <= binom(2n-2,n)                           (2.3)
```

because (2.3), after division by `M`, is

```text
1/(n+1) <= (n-1)/(2(2n-1)),
```

equivalent to `n^2-4n+1>=0`.  Hence `x<=2n-2`, and

```text
binom(x,n-2)/binom(x,n)
 = n(n-1)/[(x-n+1)(x-n+2)] >= 1.
```

This proves (2.1).  Complementation proves the upper statement. `square`

This recovers the endpoint-bank theorem independently.  The next lemma is
the extra synchronization input.

## 3. A sharp enough Kruskal--Katona chord

### Lemma 3.1 (Catalan chord inequality)

For `n>=4` and every `A subset X` with `z<=a=|A|<=M`,

```text
|partial_2 A| >= P - (R/N)(M-a)
                = a - (C/N)(a-z).                     (3.1)
```

### Proof

For real `x` define `B_j(x)=binom(x,j)`.  Let `x_0` be determined by
`B_n(x_0)=z`.  By (2.3), `x_0<=2n-2`.  If `a=B_n(x)` then
`x_0<=x<=2n`, and Lovasz--Kruskal--Katona reduces (3.1) to

```text
F(x):=B_(n-2)(x)-P+(R/N)(M-B_n(x)) >= 0.               (3.2)
```

At the right endpoint `F(2n)=0`.  At the left endpoint,
`B_(n-2)(x_0)>=B_n(x_0)=z`, while the affine right side of (3.1) also
equals `z`; hence `F(x_0)>=0`.

It remains only to see that `F` has no interior minimum.  Put
`t=x-n+1>0` and

```text
A(t)=sum_(j=2)^(n-1) 1/(t+j).
```

Direct differentiation gives

```text
B'_(n-2)(x)/B'_n(x)
 = n(n-1) / [t(t+1)+(2t+1)/A(t)].                      (3.3)
```

The denominator in (3.3) is strictly increasing: `t(t+1)` and `2t+1`
increase, while `A(t)` decreases.  Thus the derivative ratio is strictly
decreasing.  Since

```text
F'(x)=B'_n(x)[B'_(n-2)(x)/B'_n(x)-R/N],
```

the derivative changes sign at most once, and only from positive to
negative.  Therefore `F` is first increasing and then decreasing (with one
part possibly empty), so its minimum on the interval is at an endpoint.
Both endpoint values are nonnegative, proving (3.2). `square`

## 4. Dual rank density

### Theorem 4.1

Let `T` be either `T_down` or `T_up`.  For every `A subset X` with
`a=|A|<=N`,

```text
r_(T^*)(A) >= (C/N)a.                                  (4.1)
```

Of course the integer left side is at least `ceil(Ca/N)`.

### Proof

For a family `Y subset X`, the transversal-matroid rank formula is

```text
r_T(Y)=min_(Z subset Y)(|Y|-|Z|+|partial_2 Z|).         (4.2)
```

For `T_up`, apply the same formula after complementation.

Take `Y=X-A`, so `|Y|=M-a`.  We claim every term of (4.2) is at least

```text
P-a+(C/N)a.                                            (4.3)
```

If `s=|Z|<=z`, Lemma 2.1 gives `|partial_2 Z|>=s`, so the term is at least
`M-a`; this dominates (4.3) because their difference is
`C(1-a/N)>=0`.

If `s>=z`, Lemma 3.1 gives

```text
M-a-s+|partial_2 Z|
 >= P-a+(C/N)(M-s)
 >= P-a+(C/N)a,
```

where the last inequality uses `Z subset X-A`, hence `M-s>=a`.
Thus (4.3) holds.  Dual rank is

```text
r_(T^*)(A)=a-P+r_T(X-A),
```

and (4.1) follows. `square`

The factor `C/N` is exactly what synchronization needs; the ordinary
normalized-matching bound `C/M` would be too weak.

## 5. The synchronized common basis

### Theorem 5.1 (automatic common basis)

Let `E` be any set of order `N`, and let

```text
tau:E -> X,       eta:E -> X
```

be arbitrary injections.  Pull back `T_up^*` along `tau` and `T_down^*`
along `eta`, obtaining matroids `M_tau,M_eta` on `E`.  Then these two
matroids have a common basis of order `C`.

### Proof

Theorem 4.1 applied to all of `E` shows that each pullback has rank at
least `C`; its ambient dual has rank exactly `C`, so both ranks equal `C`.
For every `S subset E`, Theorem 4.1 gives

```text
r_tau(S)+r_eta(E-S)
 >= (C/N)|S|+(C/N)(N-|S|)=C.                           (5.1)
```

Edmonds' matroid-intersection min--max theorem says that the maximum order
of a common independent set is

```text
min_(S subset E)[r_tau(S)+r_eta(E-S)].
```

It is therefore at least `C`, and cannot exceed the common rank `C`.
The resulting common independent set is a basis of both matroids. `square`

### Corollary 5.2 (balanced common-basis distribution)

There is a probability distribution on common bases `Q` for which every
`e in E` has the exact marginal

```text
                         Pr(e in Q)=C/N.                (5.2)
```

Consequently, for every nonnegative cost function `w:E -> R`, some common
basis satisfies

```text
                         w(Q) <= (C/N) w(E).             (5.3)
```

### Proof

The constant vector `x_e=C/N` has total weight `C`.  Theorem 4.1 says that
for every subset `S` it obeys the rank inequalities of each pulled-back
matroid, so it belongs to both base polytopes.  Edmonds' matroid-
intersection polytope is integral; its order-`C` face is therefore the
convex hull of common bases.  Decomposing `x` on that face gives (5.2), and
averaging the linear functional `w` gives (5.3). `square`

This is stronger than bare existence and may be useful for the physical
row: any *additive* collision or boundary-risk cost can be paid at its
uniform-density average.  It gives no negative-dependence or simultaneous
concentration statement, so it does not by itself construct the two side
forests.

### Corollary 5.3 (Theorem 6.1, incidence rows)

Let `F` be any oriented Catalan linear matching at parameter `n>=4`.
There is a set `Q subset F`, `|Q|=C`, such that, with (0.1),

```text
X - {tail(q):q in Q}
```

matches bijectively to all `(n+2)`-sets, and all `(n-2)`-sets match
bijectively into

```text
X - {head(q):q in Q}.
```

### Proof

The tail and head maps are injections because the oriented physical support
of `F` is a path forest.  Apply Theorem 5.1.  A `C`-set is a basis of
`T_up^*` exactly when its `P`-element complement is a basis of `T_up`, and
similarly below.  A basis of either transversal matroid is precisely the
required saturating containment matching. `square`

Thus the answer to the common-basis trichotomy is sharp:

```text
automatic for every Catalan linear forest F (indeed, for every pair of
injective tail/head maps), for every n>=4.                              (5.2)
```

No inductive symmetry hypothesis is required.

## 6. What remains

This theorem supplies the two diagonal matchings as **incidence** objects.
It does not assert that arbitrary such matchings lift to acceptable
physical side graphs.  The exact unresolved condition is still Theorems
3.1 and 4.1 of
`MATH_THEOREM_CATALAN_TWO_COORDINATE_PORT_INHERITANCE_AND_SIDE_FOREST_GATE_20260731.md`:

1. each side graph has maximum degree at most two;
2. seam anchors have side degree at most one; and
3. after contracting `F-Q` and the two side forests, the seam attachment
   multigraph is a forest.

In other words, the `a=1` recursion no longer has an outer-palette Hall
gate or a synchronized port-bank gate.  Its only remaining row is a
**forest-compatible realization of an already guaranteed common basis**.

## 7. Exact audit

The standard-library audit

```text
scratch/audit_catalan_two_coordinate_common_basis_automatic_20260731.py
```

computes the exact Kruskal--Katona two-shadow function for every family
size at `n=4,...,9`.  It verifies Lemma 2.1, the integer form of (3.1), the
full transversal/dual rank profile (4.1), and the common-basis rank-sum
bound (5.1).  Its retained output is

```text
scratch/catalan_two_coordinate_common_basis_automatic_20260731.audit.json.
```

The finite audit corroborates the proof; it is not used to infer the
all-`n` statement.
