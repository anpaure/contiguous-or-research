# Independent audit: rank-filtration stability and the Rayleigh onion law

## Verdict

The canonical reduction, exceptional-entry budget, segment-capacity lemma,
and the near-extremal stability inequality

```text
h_r(A)+delta_r(A)+s_r(A)-1 <= n-beta_r(k)
```

are valid.  Here `s_r(A)` is the number of nonempty rank-below-`r`
components after the canonical reduction.  Restoring the deleted exceptional
positions gives the valid original-word consequence

```text
kappa_r(A) <= n-beta_r(k)+1.
```

This is a genuine all-dimensional strengthening of the earlier exact
boundary--core theorem.  In the current project it also streamlines and
strengthens Proposition 7.1 of `BOUNDARY_CORE_PIN_COUPLING.md`.

The rank--dimension transform and the Rayleigh lower-tail consequence are
also sound after one harmless rounding repair.  The odd-dimensional and
`k=11` case splits are correct.

Two scope corrections are essential:

1. in the Rayleigh proof one must take `q=ceil(x sqrt(m))`, not the displayed
   floor, when proving the event `D_m>=x sqrt(m)`;
2. exact equality at rank `r` forces **one** boundary--core peel.  It does
   not force an automatically recursive exact onion.  A second exact peel
   is available only when the boundary mass saturates the record gap, exactly
   as stated in `ITERATED_BOUNDARY_CORE_RIGIDITY.md`.

Neither correction changes the main stability inequality or the stated
`k=11` architectures.  The results remain necessary structure, not an
existence theorem and not a proof or disproof of `nu(k)=B(k)`.

## 1. Canonical reduction

Fix `r`.  Delete every entry of rank greater than `r`, and retain only one
literal occurrence of each distinct rank-`r` mask.

The preservation argument is exact:

* a witness for a target `S` of rank below `r` contains only nonempty
  submasks of `S`, hence only entries of rank below `r`;
* if `|S|=r` and `S` occurs literally, the retained occurrence represents
  it;
* if `|S|=r` and it does not occur literally, no witness for `S` can contain
  any rank-`r` entry `R`, since `R subseteq S` would imply `R=S`.

After deletion, the surviving members of an old interval remain consecutive
in the compressed word.  Thus the canonical reduction covers the full
rank-at-most-`r` ideal.

If its original length is `beta_r(k)+c`, its reduced length is

```text
beta_r(k)+c-h_r-delta_r.
```

The rank-`r` lower bound therefore gives

```text
h_r+delta_r <= c.
```

No uniqueness of witnesses, fixed row, or prescribed endpoint schedule is
used.

## 2. Segment-capacity lemma

Re-index a segment of length `q+t` by `1,...,q+t`.  Select witnesses for `q`
distinct rank-`r` targets.  Equal-rank incomparability gives distinct left
and right endpoints, and ordering by left endpoint orders the right endpoints
as well.  Consequently the `i`th interval satisfies

```text
I_i subseteq [i,i+t].
```

Every interval `[a,b]` of length at least `t+1` has `a<=q` and contains
`I_a`.  Its OR therefore has rank at least `r`.  All targets below rank `r`
represented in the segment use one of its intervals of length at most `t`,
of which there are exactly

```text
F(q,t)=tq+C(t+1,2).
```

The `q=0` case is simply the total-interval count.  The lemma is sound and is
the same side-capacity mechanism already audited in handoff Section 260.

## 3. Near-extremal stability

Put

```text
e=h_r+delta_r,          epsilon=c-e.
```

The canonical reduction has length `M_r+d_r+epsilon`.  Let `z` be its number
of distinct literal rank-`r` entries.  Delete these entries, obtaining `s`
nonempty low-rank segments of lengths `n_j`.  Every one of the `M_r-z`
nonliteral rank-`r` targets has a witness wholly inside one of these segments;
choose one and let `q_j` be the number assigned to segment `j`.  Then

```text
sum q_j=M_r-z,
t_j:=n_j-q_j,
sum t_j=d_r+epsilon.
```

Each `t_j` is positive.  If `t_j=0`, then `q_j=n_j` incomparable intervals
would have all `n_j` possible left endpoints and all `n_j` possible right
endpoints, forcing all of them to be singletons.  That is impossible because
the segment entries have rank below `r`.

Set

```text
u=d_r+epsilon-s+1.
```

Then `t_j<=u`, so

```text
sum t_j q_j <= u(M_r-z).
```

Convexity of `C(t+1,2)` over positive integral `t`, with fixed total, gives

```text
sum C(t_j+1,2) <= C(u+1,2)+s-1.
```

Every lower target has a witness in one low segment, hence the segment lemma
gives

```text
L_r <= u(M_r-z)+C(u+1,2)+s-1.
```

At least `s-1` retained literal rank-`r` positions separate the segments,
so `z>=s-1`.  Since `u>=1`, the last display implies

```text
L_r <= u M_r+C(u+1,2).
```

Minimality of `d_r` forces `u>=d_r`, and therefore

```text
s<=epsilon+1,
e+s-1<=c.
```

Restoring the `e` deleted non-low positions can increase the number of
low-rank components by at most `e`, so the original word has at most `c+1`
such components.  Every step is valid, including the cases `q_j=0` and
segments touching an endpoint.

This proof is stronger and cleaner than the existing surplus inequality in
`BOUNDARY_CORE_PIN_COUPLING.md`.  In the latter's notation (`h_r=0` and
`x=delta_r`) it yields directly

```text
x+s-1<=c,
```

whereas Proposition 7.1 first retains a more complicated capacity condition
and specializes it to `k=11`.

## 4. Exact equality and boundary mass

For `c=0`, the stability result gives

```text
h_r=delta_r=0,  s=1.
```

Thus every entry has rank at most `r`, the literal rank-`r` entries are
distinct, and all lower-rank entries form one interval.  The literal
rank-`r` entries consequently occupy two possibly empty boundary blocks, and
the core represents the complete lower ideal.  This agrees with
`BOUNDARY_CORE_RIGIDITY_AUDIT.md`.

If `z` is the total boundary mass, the two displayed bounds are valid:

```text
z <= beta_r-max_(s<r) beta_s,
d_r z <= sigma_r.
```

The first follows because the core covers every lower rank.  For the second,
the core has length `(M_r-z)+d_r`, represents the remaining `M_r-z`
rank-`r` targets, and represents all `L_r` lower targets, so the segment
capacity lemma gives

```text
L_r <= d_r(M_r-z)+C(d_r+1,2).
```

The quotient `floor(sigma_r/d_r)` should, as usual, be stated only when
`d_r>0`; this is automatic in the intended `r>=2` applications.

The phrase "recursive boundary--core onion" needs the qualification from
`ITERATED_BOUNDARY_CORE_RIGIDITY.md`.  If

```text
g_r=beta_r-max_(s<r)beta_s,
```

then the core reaches the next lower equality length only when `z=g_r`.
For `z<g_r` it has positive excess and the stability theorem supplies
component/exception budgets, but not another exact boundary peel.  Known
optimal words in dimensions `8,9,10,12` have zero literal mass at their
active record rank, demonstrating why this distinction is substantive.

## 5. Rank--dimension transform

For an `ell`-set `Y`, retain the entries satisfying both

```text
A_i subseteq Y,   |A_i|<=r.
```

Every witness for a target `S subseteq Y`, `|S|<=r`, survives, so the
retained subsequence has length at least `nu_{<=r}(ell)`.  Summing over `Y`
gives the correct transform

```text
sum_(s=1)^r a_s C(k-s,ell-s)
    >= C(k,ell) nu_{<=r}(ell)
    >= C(k,ell) beta_r(ell).                       (5.1)
```

The binomial coefficient in (5.1) must be read as
`C(k-s,ell-s)`; the vertically garbled version in the supplied text can be
misread in the reverse order.  Setting `ell=k` gives cumulative rank
truncation, while setting `r=ell` gives the earlier dimension restriction.
The result is valid and is a useful two-parameter packaging of those two
deletion principles.

## 6. Rayleigh lower tail and moment

Let `k=2m`, `W=C(2m,m)`, and `n=(1+epsilon_m)W` with `epsilon_m->0`.  For
fixed `x>=0`, take

```text
q=ceil(x sqrt(m)).
```

Then

```text
P(D_m>=x sqrt(m))
 = P(|A_I|<=m-q)
 >= C(2m,m-q)/n
 = exp(-x^2)-o(1).
```

The original use of `floor(x sqrt(m))` proves the slightly weaker event
`D_m>=floor(x sqrt(m))`; it does not literally imply the displayed real
threshold.  Replacing floor by ceiling repairs the proof without changing
the limit.

The central ratio is

```text
C(2m,m-q)/C(2m,m) -> exp(-x^2),
```

so the limiting tail and its constant are correct.  Tail integration (or the
subsequent exact finite identity) yields

```text
E D_m >= (sqrt(pi)/2+o(1)) sqrt(m).
```

The exact identity

```text
sum_i (m-|A_i|)_+
 = sum_(r=1)^(m-1) #{i:|A_i|<=r}
 >= 2^(2m-1)-W/2-1
```

is correct.  At exact middle-rank length every entry has rank at most `m`,
and division by `n=W+O(sqrt(m))` gives

```text
average_i |A_i| <= m-(sqrt(pi*m)/2)+1/2+o(1).
```

Thus the Rayleigh statement is a valid and attractive asymptotic corollary
of cumulative rank truncation.  It is not an independent new obstruction:
its full content follows by applying the already proved rank-specific bounds
at the `sqrt(m)` family of nearby ranks.

## 7. Laminar component bounds

Applying stability at every rank gives

```text
kappa_r(A)<=n-beta_r(k)+1,
```

and the position sets `{i:|A_i|<r}` are nested with `r`.  For
`k=2m`, `r=m-q`, and `q=o(m)`, the elementary middle-binomial estimate gives

```text
kappa_(m-q)
 <= n-C(2m,m-q)+1
 = O((epsilon_m+(q+1)^2/m)W).
```

For fixed `q`,

```text
W-C(2m,m-q)=(q^2+o(1))W/m,
```

so the stated Catalan-scale first split (`q=1`) is correct.  These are real
component restrictions, but "onion" should be understood as a laminar
hierarchy of nested level sets and component budgets.  It does not mean that
each lower level is one centered interval or that all shells are literal
boundary blocks.

## 8. Odd dimensions

For `k=2m+1`, the two middle binomial layers both have size `M`, and their
lower-target counts differ by exactly `M`.  Therefore

```text
d_- <= d_+ <= d_-+1.
```

At length `M+d_+`, exact rank-`m+1` stability permits at most
`d_+-d_-<=1` literal upper-middle entries.  Such an entry is unique and lies
at a physical endpoint.

The two cases are correct:

* if the endpoint exists, then `d_+=d_-+1`, and deleting it leaves an exact
  rank-`m` equality word with its own rank-`m` boundary--core form;
* if it does not exist and `d_+=d_-`, the whole word is an exact rank-`m`
  equality word;
* if it does not exist and `d_+=d_-+1`, rank-`m` stability with `c=1` gives
  `delta_m+s-1<=1`.  Hence there is at most one duplicate occurrence and at
  most two lower components.  More precisely, if the duplicate exists then
  deleting it leaves one lower component; if no duplicate exists, two lower
  components remain possible.

That last conditional wording is preferable to the supplied sentence
"after removing the possible duplicate ... one component", which can be
misread as asserting one component even when no duplicate exists.

## 9. The `k=11` specialization

Exact arithmetic gives

```text
beta_4(11)=331,
beta_5(11)=464,
beta_6(11)=465.
```

The proposed dichotomy is correct.

**Type I.**  There is one literal six-set, occurring at an endpoint.  Its
deletion leaves an exact 464-position rank-five word.  The distinct literal
five-sets form its two boundary blocks, its rank-at-most-four core covers
all ranks through four and has length at least 331, and the rank-five
boundary mass is at most `464-331=133`.

**Type II.**  There is no literal six-set.  Every entry has rank at most five.
At rank five the word has excess one, so there is at most one extra literal
five-set occurrence and the rank-at-most-four entries form at most two
components.  Cumulative rank truncation forces at least 331 such entries,
and hence at most 134 rank-five entries.

This is globally WLOG.  It agrees with, and now derives uniformly, the more
specialized `k=11` surplus conclusion in handoff Item 1085.  It does not yet
encode the stronger coordinate-transversal, slack-`{1,2}`, or exact
adjacent-pair conclusion available there in the two-component subcase.

## 10. Novelty relative to the current project

The claims divide as follows.

* **Previously established:** the side/segment-capacity lemma; exact
  boundary--core rigidity; the boundary residual cap; conditional iteration
  through saturated record gaps; scalar cumulative rank truncation and
  coordinate restriction; the specialized one-surplus `k=11` component
  theorem.
* **Genuinely new in this formulation:** canonical deletion simultaneously
  charging high entries and duplicate literal active-rank occurrences;
  the sharp general inequality `h+delta+s-1<=c`; its uniform component law
  at every rank; and the clean two-parameter rank--dimension transform.
* **New interpretation/corollary rather than new independent machinery:**
  the Rayleigh tail and Catalan-scale laminar component language.

The stability theorem is mathematically valuable and should be incorporated
into the handoff.  Its principal strategic use is a lossless near-extremal
case split and a family of exact rank/component constraints.  It narrows the
geometry that any near-width construction must have, but it leaves the same
decisive existence issues: joint endpoint ordering, coordinate pin survival,
and upper-shadow coverage.

## 11. Strengthened corollaries and wording audit

The corrected theorem note now records two consequences of the same exact
cuts.  For every fixed `p>0`, tail integration and Fatou's lemma give

```text
liminf E[(D_m/sqrt(m))^p] >= Gamma(1+p/2).
```

For `q=ceil(x sqrt(m))`, the component inequality and the central local limit
give the full square-root-scale profile

```text
limsup kappa_(m-q)/W <= 1-exp(-x^2).
```

Both are valid.  The first is a moment lower bound, not convergence to a
Rayleigh distribution; the second extends the fixed-depth Catalan-scale edge
of the onion law.

In the `k=11` Type-II branch the sharper physical coupling

```text
delta_5+kappa_5<=2
```

also holds.  If `delta_5=1`, exactly one literal five-set value occurs twice.
The stability theorem is valid whichever copy is retained.  If the original
rank-at-most-four positions had two components, retaining the copy that lies
in any separating rank-five block would leave two reduced components and
contradict `delta_5+s<=2`.  Hence a duplicate forces one physical component.
This is exactly the coupled row used by the audited Type-II SAT module.

Finally, the odd-dimensional statement should be read for `m>=2`; the tiny
cases are checked separately.  Calling the reduction canonical requires a
fixed retention convention, but the proof and all bounds hold for every
choice, so no mathematical conclusion depends on that convention.
