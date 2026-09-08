# Exact age-level stocking of the canonical multi-hole actuator bank

Date: 2026-08-01

Status: unconditional marked-profile stocking theorem, with a sharp
Hall/min-cut criterion.  Every canonical multi-hole bad row, its donor, and
its complete reservoir chain can be placed in the existing `W` named owner
occurrences, without an additional marked row slot or owner-role, for all
sufficiently large `k`.
This is a theorem about the age-level marked incidence table.  It does **not**
prove that the residual age law is stationary, nor that the selected rows
have a protected one-copy Catalan realization.

## 1. Marked rows as a capacitated incidence table

Let

```text
r=ceil(k/2),  W=C(k,r),  d=d(k).
```

In the triangular marked law, deficit `t` has multiplicity `n_t`, and

```text
N=sum_t n_t <= dW.                                  (1.1)
```

There are `W` named rows, one for each prospective owner occurrence.  A row
may contain at most `d` distinct marked deficits.  Thus a marked-profile
assignment is a simple bipartite incidence graph between deficit labels and
the `W` named rows, with left degrees `n_t` and right degrees at most `d`.

Suppose `M` named rows are reserved and prescribed full profiles of size
`d`.  Let

```text
g_t = number of prescribed rows containing deficit t.       (1.2)
```

Put `U=W-M` and `n'_t=n_t-g_t`.

### Theorem 1.1 (sharp stocking criterion)

The prescribed rows extend to a marked-profile assignment on all `W` rows
with the original deficit multiplicities if and only if

```text
M <= W,
0 <= g_t <= n_t                                  for every t,
sum_t n'_t <= dU,
n'_t <= U                                        for every t.  (1.3)
```

Equivalently, the exact Hall family is

```text
sum_(t in S) n'_t <= U min(d,|S|)                for every S.  (1.4)
```

### Proof

Use the flow network

```text
source -> deficit t -> free row u -> sink,
```

with fixed source capacity `n'_t`, unit capacity on every deficit-row edge,
and row-sink capacity `d`.  Max-flow/min-cut gives (1.4).

Conditions (1.3) imply every cut in (1.4).  If `|S|<d`, then

```text
sum_(t in S)n'_t <= |S|U
```

by the individual bounds.  If `|S|>=d`, the total bound gives

```text
sum_(t in S)n'_t <= sum_t n'_t <= dU.
```

Conversely, singleton cuts and the cut containing every deficit give the
individual and total bounds.  Integral max flow supplies the extension.
QED.

This criterion is exact, not asymptotic.  It is also constructive.  Adding
blank symbols to make every row have exactly `d` slots shows that the old
and new marked incidence tables differ by alternating row/deficit circuits;
so the extension is a count-neutral regrouping, not a creation of marks.

## 2. The complete canonical actuator bank

For every selected occurrence of a canonical bad row, fix parameters

```text
d>=3, q>=2, 1<=m<=d-1, r>=d+q+2,
j=d-m+1.
```

Reserve the following `j+1` full rows:

```text
A_(q,m)=({1,...,d-1}\{m}) union {d+q-1,r-1},
H_q    ={1,...,d-2,d,d+q},
K_p    ={1,...,d+1}\{d-p+1},  1<=p<=j-1.       (2.1)
```

The first row is the actual bad row, the second is its mark-exchange donor,
and the remaining rows are the complete reservoir chain from the
multi-hole-collapse theorem.

Let `a_(q,m)` be the number of selected bad occurrences, and put

```text
A=sum_(q,m) a_(q,m),
M=sum_(q,m) (j+1)a_(q,m).                       (2.2)
```

Because every bad row contains deficit `r-1`, and those rows are distinct,

```text
A <= n_(r-1) <= C(k,1)=k,
M <= (d+1)A <= k(d+1).                          (2.3)
```

All profiles in (2.1) are `d`-subsets of `{1,...,r-1}`.  Apart from the bad
row's `r-1`, every used deficit is at most `r-2`.

## 3. Uniform stocking theorem

### Theorem 3.1 (canonical bank stocks inside the one-copy row population)

Assume the `a_(q,m)` occurrences in (2.2) are actual rows of the systematic
triangular marked assignment.  Then, for all sufficiently large `k`, those
rows can be retained and distinct additional rows can be assigned all the
donor and reservoir profiles in (2.1), while:

1. using exactly the original `W` named rows;
2. using no row more than once;
3. putting at most `d` distinct marks on every row; and
4. preserving every global deficit multiplicity `n_t` exactly.

No additional marked row slot or owner-role is required at this
marked-profile level; physical chronology is outside the theorem.

### Proof

We verify (1.3).

The total condition is automatic because every prescribed row is full:

```text
sum_t n'_t = N-dM <= dW-dM=d(W-M).             (3.1)
```

Also `M<=k(d+1)=o(W)`.

For mark supply, `g_(r-1)=A<=n_(r-1)`.  Every other mark used by the bank is
at most `r-2`, so monotonicity of the triangular multiplicities gives

```text
n_t >= n_(r-2)
    = C(k,2)-b_2
    >= C(k,2)-C(d+1,2)                         (3.2)
```

for every such `t`.  The last inequality uses that the entire triangular
boundary has only `C(d+1,2)` cells.  Since `d=Theta(sqrt(k))`, the right side
of (3.2) is `Theta(k^2)`, whereas `g_t<=M=O(kd)=O(k^(3/2))`.  Hence
`g_t<=n_t` for all sufficiently large `k`.

It remains to check the individual residual-row bounds, equivalently

```text
M-g_t <= W-n_t.                                 (3.3)
```

For `t=1`, every donor `H_q` contains `1`, and every `K_p` contains `1`
because its omitted mark `d-p+1` lies in `{m+1,...,d}`.  The only prescribed
rows omitting `1` are the actual bad rows with `m=1`.  Therefore

```text
M-g_1=sum_q a_(q,1).                            (3.4)
```

Those are already distinct rows missing mark `1` in the original systematic
assignment, so

```text
sum_q a_(q,1) <= W-n_1.                         (3.5)
```

Thus the unique potentially tight column is automatic.

For every `t>=2`, monotonicity gives `n_t<=n_2`, and hence

```text
W-n_t >= W-n_2 >= W-C(k,r-2).                  (3.6)
```

The last quantity is exponential in `k` up to a polynomial factor, while

```text
M-g_t <= M <= k(d+1)=O(k^(3/2)).                (3.7)
```

So (3.3) holds for all sufficiently large `k`.  Theorem 1.1 now supplies
the desired assignment.  QED.

The proof is deliberately robust: the bad multiplicities may be split among
arbitrarily many values of `(q,m)`, and no compatibility between different
reservoir chains is assumed beyond their shared global mark counts.

## 4. Exact finite test and the only possible failures

The asymptotic proof used only two coarse inequalities.  For any fixed
dimension, Theorem 1.1 is the exact test:

```text
g_t <= n_t,
M-g_t <= W-n_t                              for every t,  (4.1)
```

together with `M<=W` and `N<=dW`.

Thus every finite failure has a transparent certificate of one of two forms:

* **supply failure:** the bank requests more copies of a deficit than exist;
* **missing-slot failure:** the bank omits a deficit on more reserved rows
  than the original population can omit it.

There are no higher-order Hall obstructions.  In the canonical family,
deficit `1` is the only asymptotically tight missing-slot column, and its cut
is inherited from the selected bad rows themselves.

## 5. Orbit-compressed stationary residual gate

Theorem 3.1 stocks marked profiles.  It does not prove the stronger
decomposition

```text
pi = sigma + (prescribed stationary actuator cycles)          (5.1)
```

with stationary `sigma`.  The exact residual age-level gate can nevertheless
be stated without row variables.

Let `C_(r,d)` be the age types, let `c->c'` mean
`Q(c')<=P(c)`, and let `h_c` be the prescribed actuator-cycle type counts.
After removing the bank, put `U=W-M` and residual mark demands `n'_t`.
There is a stationary residual age law supporting all residual marks if and
only if there are nonnegative **integral** variables

```text
f_(c,c')  on legal age arcs,
sigma_c=sum_c' f_(c,c')=sum_c' f_(c',c),
sum_c sigma_c=U,                                      (5.2)
```

such that

```text
n'_t <= sum_(c:t in R(c)) sigma_c             for every t.  (5.3)
```

For fixed `sigma`, (5.3) is sufficient: marks of distinct deficit ranks do
not compete, and each of the `sigma_c` copies may simultaneously carry all
available distinct suffix ranks in `R(c)`.

Equivalently, after normalization, `sigma` must satisfy the exact Strassen
cuts for age stationarity and the coordinate capacities (5.3).  This is the
sharp orbit-compressed circulation formulation of the remaining age-level
problem.  Theorem 3.1 proves that **profile stock itself creates no further
Hall obstruction**; what remains is stationarity of the residual type law.

## 6. A one-copy owner-moving lift of a short age path

The fixed-owner lift of an age cycle repeats one owner.  A useful partial
replacement is available for paths.

### Lemma 6.1 (fresh-token Johnson lift)

Let

```text
c^0 -> c^1 -> ... -> c^ell
```

be a legal age-type path with `c^i_d>=1` for `0<=i<ell`.  If

```text
k-r >= ell,                                        (6.1)
```

then it has a literal lift to distinct rank-`r` owners

```text
T_0,T_1,...,T_ell
```

such that every step is a Johnson edge.  Moreover all lower `q1` colours
`T_i intersect T_(i+1)` are distinct, and all upper `q1` colours
`T_i union T_(i+1)` are distinct, provided `ell<=d+1`.

### Proof

Start with a partition

```text
T_0=C^0_0 dotunion ... dotunion C^0_d,
|C^0_h|=c^0_h.
```

For the transition to `c^(i+1)`, choose

```text
C^(i+1)_(h+1) subseteq C^i_h,
|C^(i+1)_(h+1)|=c^(i+1)_(h+1),  0<=h<d,
```

which is possible by legality.  Choose `alpha_i in C^i_d`, choose a globally
fresh `beta_i` outside `T_0` and all earlier fresh tokens, and put all
unselected old elements except `alpha_i`, together with `beta_i`, into
`C^(i+1)_0`.  Its size is exactly `c^(i+1)_0`, and

```text
T_(i+1)=T_i-{alpha_i}+{beta_i}.                     (6.2)
```

Thus the owners are distinct: if `i<j`, then `T_j` contains the not-yet-used
token `beta_(j-1)`, whereas `T_i` does not.  For the upper colours, if
`i<j`, the globally fresh token `beta_j` is absent from
`T_i union T_(i+1)` and present in `T_j union T_(j+1)`.

For the lower colours, `beta_i` is absent from
`T_i intersect T_(i+1)=T_i-{alpha_i}`.  At the source of edge `j` its age is
at most `j-i-1<=ell-2<=d-1`; refreshing it can only lower that age.  Hence
it cannot equal `alpha_j in C^j_d`, and it belongs to
`T_j intersect T_(j+1)`.  Thus all lower and upper q1 colours are pairwise
distinct.  QED.

For every canonical multi-hole actuator path, `ell<=d+1` and all displayed
terminal coordinates are positive.  Since `d=Theta(sqrt(k))` and
`k-r=Theta(k)`, (6.1) holds asymptotically.  This embeds each **cut** actuator
cycle as a one-copy, doubly-rainbow protected path.  Closing all such paths
into a stationary owner-moving circulation, retaining arbitrary-width upper
witnesses and the common cap, is still a physical Catalan problem.

### Corollary 6.2 (fixed-number q1 planting)

Assume the `H` selected lifts are pairwise vertex-disjoint alternating paths,
or more generally that their union is edge-simple with maximum degree at
most two.  In the odd middle-level incidence graph, a lifted path with `ell`
Johnson edges has `2ell` incidence edges.  Hence any fixed number `H` of
these paths has at most

```text
2H(d+1)=O_H(sqrt(k))
```

protected incidence edges.  The existing fixed-`H` Ore--Ryser extension
theorem therefore embeds the bank in a spanning owner/lower-q1 two-factor
for all sufficiently large middle rank `r_mid`, because eventually
`2H(d+1)<=r_mid-2`.

The pairwise-disjoint/global-degree hypothesis is not supplied by Lemma 6.1,
which is pathwise.  This corollary is intentionally fixed-`H`.  The complete
systematic actuator stock may contain `O(k)` path copies, with `Theta(k)` in
the extreme block, so its literal protected incidence bank has `O(kd)` edges
and `Theta(kd)` only in the long-path extreme.  It is outside the fixed-`H`
theorem.  Compressing those copies into rotation orbits, or proving a
positive-density protected extension, remains part of the physical Catalan
coupling.

## 7. What is now closed and what is not

Closed unconditionally:

* the exact capacitated Hall criterion for a prescribed full-profile bank;
* uniform simultaneous stocking of every canonical bad row, donor `H_q`,
  and reservoir row `K_p` inside the original `W` rows;
* absence of any higher-order marked-profile Hall cut;
* a one-copy Johnson-path lift of every short actuator type path.

Still open:

* an all-`k` proof that the residual type law in (5.2)--(5.3) is stationary;
* cyclic/Euler joining of all cut actuator paths without owner repetition;
* protected arbitrary-width upper and common-cap payloads;
* coupling to the rooted Catalan/pivot selector; and
* any new upper bound on `nu(k)`.
