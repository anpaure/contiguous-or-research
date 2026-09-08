# Audit of `MATH_ATTACK_K_CATALAN_REBUNDLING_REPORT_RAW_20260724.md`

## 1. Verdict

The principal quantitative results are correct:

* the tail-component `L^1` and support estimate;
* the `O(W/sqrt(L))` tail diameter;
* the positive-density limit `3/8`;
* the explicit `K_0` preparation and its `1/8` seam count;
* the Johnson-spectral seam lower bound;
* the constants

  ```text
  25(2-sqrt(3))/64,
  gamma=(14+25sqrt(3))/64,
  beta=(1287-700sqrt(3))/512;
  ```

* the commutator table;
* the local-chart speed limit and group-orbit invariant;
* the conditional NAE gain calculation.

Four corrections or qualifications are required.

1. The proof of Theorem 1 must treat suffix depth `r=0` separately.  The
   phrase “`r-1` slots containing `n`” is meaningless there.  The claimed
   bound remains valid, because retaining all `n=2j+5` old slots gives
   exactly the same bound.
2. The tail theorem concerns the `3/8`-mass deep-suffix subcube, not the
   entire fixed Catalan cube.  It does not prove that an exceptional
   deterministic choice of the remaining shallow components cannot repair
   the first shadow.  The opening and closing claims that the whole fixed
   hierarchy “cannot perform the required repair” are therefore too strong.
3. The finite-energy theorem needs a uniform conditional-probability
   hypothesis under every positive-probability exposure history.  Its
   conclusion is an expectation obstruction; it does not exclude rare good
   assignments or deterministic search.
4. The NAE statement becomes a precise theorem only when “risk” is defined
   as the **total fair expected number of new holes over all initially
   covered sigma-orbits**.  Conditional expectation then gives one legal
   cube vertex (a simultaneous subset of recomputed components), not
   necessarily one component switch.

No claimed synchronization, MWB, or component-dispersion theorem follows
from the audited results.  The raw report correctly acknowledges those
missing implications in its final section.

## 2. Catalan bookkeeping

Write `C_j=Cat_j`, `B=C_m`, `n=2m+1`, and `W=nB`.  The component sizes and
counts are

```text
|K_(j,R)|=C_j+C_(j+1),
r=m-j-2,
#{R}=C_r.
```

They have the required total mass:

```text
sum_(j+r=m-2) C_r(C_j+C_(j+1))
 = C_(m-1)+(C_m-C_(m-1))
 = C_m=B.
```

This confirms that component mass is being measured in wreaths, while
middle-owner mass is larger by the exact factor `n`.

## 3. Section 1: Catalan-tail obstruction

### 3.1 Component support bound

For `r>=1`, the slot count is consistent.  In the step-two order

```text
(n,X_A,U_R,Y_A,D_R),
```

the lengths are `1,a,r,a,r`, where `a=j+2`.  Of the `n` old rank-`(m-1)`
occurrence slots:

* `r+1` avoiding-`n` slots depend on `A` only through a whole `X_A` or
  `Y_A` multiset;
* `r-1` containing-`n` slots do likewise.

Their component sums cancel by tau-invariance.  The number of un-cancelled
old occurrences per root is therefore

```text
n-(r+1)-(r-1)=n-2r=2a+1=2j+5.
```

Applying `(tau-I)` introduces at most one removed and one added occurrence,
so

```text
||Delta_(j,R)||_1 <= 2(2j+5)|K_(j,R)|
                   = (4j+10)(C_j+C_(j+1)).
```

The histogram is integral, hence every supported coordinate contributes at
least one to the `L^1` norm and the same expression bounds support size.

#### Required `r=0` repair

At `r=0`, the quoted cancellation split would contain `r-1=-1` slots.  One
must instead make no cancellation claim and retain all `n` old slots.  Here
`j=m-2`, so

```text
2n=4m+2=4j+10.
```

Thus the boxed theorem remains true for the top component, but its proof
needs this separate sentence.  The asymptotic tail application has
`L->infinity` and is unaffected.

### 3.2 Catalan tail sum

Substituting `j=m-r-2` gives the coefficient

```text
4j+10=4m-4r+2,
```

so the displayed sum for `A_(m,L)` is correct.  For `1<=L<=m-2`, standard
two-sided Catalan estimates reduce a normalized summand to

```text
O( sqrt(m) / ((r+1)^(3/2) sqrt(m-r-1)) ).
```

On `r<=m/2` this is `O((r+1)^(-3/2))`, whose tail is
`O(L^(-1/2))`.  On `r>m/2`, summing in `j=m-r-2` gives `O(m^(-1/2))`, which
is also `O(L^(-1/2))`.  Therefore

```text
A_(m,L)=O(W/sqrt(L))
```

uniformly in the stated range.  The report should explicitly take `L>=1`,
since the displayed right-hand side is undefined at `L=0`.

### 3.3 The `3/8` mass

When `L->infinity` and `m-L->infinity`, the endpoint with fixed suffix
depth is excluded, the convolution mass with both indices growing is
`o(C_m)`, and fixed `j` contributes

```text
C_(m-j-2)/C_m -> 4^(-j-2).
```

Using the Catalan generating function `C(1/4)=2`,

```text
sum_(j>=0) (C_j+C_(j+1))/4^(j+2)
 = (1/16) sum_(j>=0) C_j/4^j
   +(1/4) sum_(l>=1) C_l/4^l
 = 1/8+1/4
 = 3/8.
```

Thus switching the `r>=floor(m/2)` tail changes exactly
`(3/8+o(1))B` wreath owners and `(3/8+o(1))W` middle owners, while its
first-shadow histogram and support change by `O(W/sqrt(m))`.

For two vertices of this tail cube, the histogram difference is a signed
sum over a subset of the same component effects, so the triangle inequality
gives diameter at most `A_(m,L)`, not twice that value.  If the canonical
vertex has `delta W` holes, filling one old hole costs at least one unit of
`L^1` change.  Hence every tail vertex has at least
`(delta-o(1))W` holes.  This corollary is correctly conditional on a uniform
positive canonical hole fraction.

### 3.4 Scope correction

The result freezes the shallow component signs and varies only a
`3/8`-mass tail.  It proves that positive-density owner replacement **inside
that tail** is insufficient.  It does not bound the effects of the remaining
`5/8` of wreath mass, nor exclude an exceptional correlated vertex of the
full fixed Catalan cube.  Accordingly:

* “the fixed Catalan hierarchy cannot perform the required repair” should
  read “the deep-suffix tail of the fixed Catalan hierarchy cannot perform
  the repair by itself”;
* “the static Catalan hierarchy is ... asymptotically inert” should read
  “the exhibited `3/8`-mass static tail subcube is asymptotically inert.”

This also agrees with the report's later admission that exceptional
deterministic correlated assignments are not excluded.

## 4. Section 2: exact seam creation

### 4.1 Explicit `K_0` preparation

Every nonempty Dyck suffix has the unique first-return form `R=1u0v`, with
`u in D_t`.  Directly swapping positions `4,5` gives

```text
sigma(1100R)=11010u0v,
sigma(1010R)=10110u0v.
```

Both images lie in `K_(t+1,v)`, which is not among the switched `K_0`
blocks.  Hence every one of the `2C_(m-2)` roots produces a crossing
sigma-orbit.  The orbits are distinct: each has exactly one endpoint in a
switched `K_0` block.  Finally,

```text
2C_(m-2)/C_m -> 2/16=1/8.
```

Thus both `1/8` constants are correct.

### 4.2 Spectral seam lower bound

For a canonical tau-block `K`, the target block `E_K` has

```text
|E_K|=n|K|,
degree_i(E_K)=m|K|,
p_K=|E_K|/W=|K|/B.
```

It is therefore a `1`-design.  Its centred indicator has no Johnson degrees
zero or one.  The next Laplacian eigenvalue is `2(n-1)`, so

```text
boundary(E_K) >= 2(n-1)W p_K(1-p_K).
```

Summing over `K` counts every inter-block edge twice and yields

```text
e_cross >= (n-1)W(1-sum_K p_K^2).
```

Every nontrivial Johnson edge has one unique transposition label.  The tau
label contributes zero because every `E_K` is tau-invariant.  Averaging over
the other `C(n,2)-1` labels and then taking a block max-cut gives

```text
(n-1)W chi_m / (2(C(n,2)-1))
 = n(n-1) chi_m B/(n(n-1)-2),
```

exactly as reported.

### 4.3 The constants `gamma` and `beta`

The square-mass limit is dominated by fixed suffix depth `r`.  Since

```text
(C_(m-r-2)+C_(m-r-1))/C_m -> 5/4^(r+2),
```

we get

```text
q := lim sum_K p_K^2
   = sum_(r>=0) C_r * 25/16^(r+2)
   = (25/256) C(1/16)
   = 25(2-sqrt(3))/64.
```

Therefore

```text
gamma=1-q=(14+25sqrt(3))/64=0.895332... .
```

The balanced-cut constant also checks.  Give each block an independent fair
sign and let `X` be the selected wreath mass divided by `B`.  Then

```text
E X=1/2,
Var X=(1/4)sum_K p_K^2,
P(|X-1/2|>=1/4) <= 4sum_Kp_K^2=4q+o(1).
```

For the transposition supplied before the max-cut step, the inter-block edge
count is at least `(2gamma-o(1))B`.  If `Y` is its random cut size, then

```text
E[Y 1_balanced]
 >= E Y-|E|P(unbalanced)
 >= |E|(1/2-4q-o(1)).
```

Hence some balanced cut has at least

```text
gamma(1-8q)B-o(B)
 = ((14+25sqrt(3))/64)((25sqrt(3)-42)/8)B-o(B)
 = (1287-700sqrt(3))B/512-o(B).
```

This is the stated positive `beta=0.1456...`.  The balance interval means
both the switched and unswitched wreath masses lie between `B/4` and
`3B/4`.  This is an asymptotic statement; positivity uses `q<1/8` and thus
holds for all sufficiently large `m`.

## 5. Section 3: commutators and component scope

The owner formula

```text
o_H(X)=tau^a o_F(tau^a X)
```

is correct for the sign `a` of the canonical block containing `X`.  To map
the pulled-back target `tau^a X` to `tau^b sigma X`, the required
permutation is

```text
c=tau^b sigma tau^a.
```

This gives exactly

```text
(a,b)=(0,0): sigma,
(a,b)=(1,1): tau sigma tau,
(a,b)=(0,1): tau sigma,
(a,b)=(1,0): sigma tau.
```

If `tau` and `sigma` overlap, the two mixed orientations are inverse
three-cycles.  Thus mixed block signs certify noncommuting target seams.
They do not certify separate components of the recomputed `H` versus
`sigma H` overlay.  If that overlay is connected, its two cube vertices are
`H` and `sigma H`, which have identical hole counts by coordinate
permutation.  The report's obstruction is therefore correct.

The auxiliary component-count constant is also correct:

```text
sum_(r=0)^(m-2) C_r
 ~ (4/3)C_(m-2)
 ~ C_m/12.
```

A connected quotient on this many vertices has a max-cut with at least half
the edges of a spanning connected graph, giving the reported weaker but
valid `(1/24+o(1))B` seam lower bound.  Connectivity before preparation does
not imply connectivity or dispersion after preparation, which the raw
report correctly notes.

## 6. Section 4: the three barriers

### 6.1 Local-chart speed limit

A disjoint two-for-two chart has two positive first-shadow coordinates, so
it can fill at most two old holes.  With `R_t` disjoint charts,

```text
M(F_(t-1))-M(F_t) <= 2R_t,
R_t<=B/2.
```

Telescoping gives a maximum improvement `BT`.  Since `W=nB`, reducing
`delta W` holes to `o(W)` requires

```text
T >= (delta-o(1))n.
```

This argument is unchanged when charts are recomputed.  It says nothing
about nonlocal components, as correctly stated.

### 6.2 Finite-energy random signs

The probability argument is valid under the following precise hypothesis:
there is an exposure order of component bits such that, for every
positive-probability history, each of the two conditional choices has
probability at least `eta`.  Marginal lower bounds alone are insufficient.

For a canonical hole `S`, keeping it a hole requires one specified choice
from every component carrying an occurrence of `tau S`.  If their number is
`h_S`, the uniform conditional hypothesis gives probability at least
`eta^(h_S)`.  Moreover,

```text
sum_(S in H) h_S
 <= sum_(S in H) mu(tau S)
 <= W.
```

Since `eta^x` is convex and decreasing,

```text
E M(F_epsilon)
 >= |H| eta^(W/|H|).
```

For `|H|>=delta W`, this is at least
`delta eta^(1/delta)W`.  The theorem therefore rules out expected
`o(W)` performance, and in particular rules out `o(W)` holes with
probability tending to one under such a distribution.  It does **not**
exclude a rare good outcome, repeated rare-event search, or an exceptional
deterministic correlated assignment.  “Cannot solve” should be narrowed to
this expectation/high-probability scope.

### 6.3 Group-orbit invariant

Every recomputed component move has

```text
mu_t-mu_(t-1)=(tau_t-I)a_t.
```

Summation over an orbit of the generated group annihilates every increment.
When the transposition graph has coordinate components `V_i`, its generated
group is the product of the symmetric groups on the `V_i`, so its rank-`r`
orbits are precisely the profiles `(|S intersect V_i|)_i`.  An orbit of
size `|O|` and total invariant integer mass `T_O` can cover at most
`min(|O|,T_O)` coordinates, proving

```text
M_r(F_T) >= sum_O (|O|-T_O)_+.
```

This is an obstruction whenever a positive profile deficit is present.
Graph connectivity removes this particular profile invariant but is not a
sufficient repair theorem.  Thus the report's “connected, or prove the
profile deficits negligible” disjunction is the correct scope.

## 7. Section 5: exact NAE formulation

Fix a recomputed sigma-cube and expose independent fair component signs.  For
each two-point shadow orbit `O={S,sigma S}`, switching a component swaps all
of that component's occurrences between the two sides.

If the initial counts are `(0,d)` with `d>=2`, and the `d` occurrences occupy
`h>=2` components, both coordinates become covered exactly when the `h`
relevant signs are not all equal.  Hence

```text
P(gain on O)=1-2^(1-h) >= 1/2.
```

This is the precise NAE gain.  If all duplicate occurrences lie in one
component, switching merely moves the hole and gives no gain.

For a fully covered initial orbit, define its risk weight by

```text
r_O = E[number of holes on O after the fair cube choice].
```

Since the orbit has positive invariant total mass, this is simply the
probability that all mass consolidates on one side.  Let

```text
R_cov=sum_(O initially covered) r_O.
```

Other one-hole orbits can only supply additional gain, while zero-mass and
single-mass orbits have invariant hole count.  Therefore, if `ell` distinct
split hole-duplicate orbits have been certified and

```text
R_cov <= theta ell,  theta<1/2,
```

then

```text
E M(G_epsilon)
 <= M(G)-(1/2-theta)ell.
```

Conditional expectation yields a legal **cube vertex**, meaning a
simultaneous subset of recomputed components, with the same bound.  This is
the rigorous version of the raw report's conditional lemma.

A middle-target mixed seam supplies neither of the two missing facts by
itself:

1. it need not land on a first-shadow hole-duplicate orbit;
2. even if it does, it need not place the duplicate occurrences in distinct
   recomputed components.

Thus the requested injective seam-to-pair map, component dispersion, and
global expected-risk bound are genuine additional hypotheses, not
consequences of the seam count.  If a uniform `ell=Omega(B)` version were
renewed for `O(n)` adaptive rounds, the arithmetic would indeed permit an
`Omega(B)` gain per round and repair `Theta(W)=Theta(nB)` holes.  Renewal,
simultaneous control of a Gaussian rank window, and common labelled owners
remain separate unproved requirements.

## 8. Corrected implication ledger

The audited theorems establish:

* an exact `3/8`-density tail rebundling with `o(W)` first-shadow diameter;
* exact `Theta(B)` mixed seams, including balanced positive-density
  preparations;
* a correct noncommutative cocycle law;
* several necessary barriers and a precise conditional NAE repair lemma.

They do not establish:

* impossibility of every deterministic assignment in the full fixed
  Catalan cube;
* dispersion of mixed seams among recomputed components;
* correlation of seams with first-shadow hole-duplicate pairs;
* the required global covered-pair risk bound;
* MWB across multiple ranks;
* labelled synchronization.

With the `r=0`, finite-energy, NAE-risk, and whole-cube scope corrections
above, the mathematical core of the raw report is sound.
