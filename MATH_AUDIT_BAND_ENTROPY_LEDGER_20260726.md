# Band-covering entropy ledger: rigorous content and exact limitations

Date: 2026-07-26

Method: pure mathematics only.

## 1. Supply of cyclic-order families

Put

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad T={W\over n}=\operatorname{Cat}_m.
\]

There are

\[
 R={(n-1)!\over2}={(2m)!\over2}
\]

unoriented cyclic orders.  Hence the number of `T`-row families is at
most `binom(R,T)`.  Since

\[
 {R\over T}={m!(m+1)!\over2},
\]

Stirling's formula gives

\[
 \boxed{
 \log\binom RT
 \le T\log{eR\over T}
 =W(\log m-1+o(1)).}
\tag{1.1}
\]

This is an unconditional upper bound on the available catalogue.  It is
deliberately generous: it does not impose exact middle ownership.

## 2. The random-family first moment

For a target `S` of size `m-q`, a uniform cyclic order contains `S` as an
interval with probability

\[
                         {n\over N_q},\qquad
 N_q=\binom{n}{m-q}.
\]

Consequently a uniform `T`-row family misses `S` with probability

\[
 \left(1-{n\over N_q}\right)^T
 =\exp(-\lambda_q+o(1)),\qquad
 \lambda_q={W\over N_q}.
\tag{2.1}
\]

Uniformly for `q=O(sqrt(m))`,

\[
 \lambda_q=\exp\left({q(q+1)\over m}
                 +O\left({q^3\over m^2}+{q\over m}\right)\right).
\tag{2.2}
\]

If `X_q` is the number of missed lower targets at depth `q`, then

\[
 \mathbb E X_q=(1+o(1))N_qe^{-\lambda_q}.
\tag{2.3}
\]

Therefore

\[
 \boxed{
 \sum_{q\ge0}\mathbb E X_q
 =(I+o(1))W\sqrt m,
 \qquad
 I=\int_0^\infty e^{-u^2-e^{u^2}}\,du\approx0.2121.}
\tag{2.4}
\]

This proves the random benchmark.  It does **not** estimate the lower tail
`Pr[sum X_q=o(W)]`.

## 3. Complementation removes the apparent factor two

For every cyclic order,

\[
 [n]\setminus I(j,m-q)=I(j+m-q,m+1+q).
\tag{3.1}
\]

Thus a lower target is covered if and only if its complementary upper
target is covered.  The number of missed masks in a two-sided band is
twice the number in one representative from every complementary pair, but
the **event** that the total is `o(W)` is the same one-sided event.

Accordingly `2I=0.4242` is the expected number of missed masks on both
sides, but it is not the number of independent constraints and must not be
used as a large-deviation exponent.  Under the same informal
mean-as-cost heuristic the catalogue comparison is

\[
 {I\sqrt m\over\log m-1},
\tag{3.2}
\]

not `2I sqrt(m)/(log(m)-1)`.  It still diverges.

For a shallow half-width `Q=o(sqrt(m))`, the one-sided expected defect is

\[
                         (e^{-1}+o(1))QW.
\tag{3.3}
\]

Hence that same heuristic predicts the scale

\[
                         Q\asymp e\log m,
\tag{3.4}
\]

rather than `(e/2)log(m)`.  Neither constant is a theorem about exact
designs.

## 4. The missing theorem in an entropy no-go

Let `P` be a uniformly chosen `T`-subset of the `R` cyclic orders and let

\[
 X(P)=\sum_{q\le H}X_q(P).
\]

To deduce nonexistence from (1.1), one would need an upper-tail-counting
theorem of the form

\[
 \boxed{
 \Pr[X(P)=o(W)]
 \le \exp[-c\sqrt m\,W]}
\tag{4.1}
\]

for some fixed `c>0` on a Gaussian window.  Indeed, (1.1) and (4.1)
would make the number of good families smaller than one for all large
`m`.

Equation (2.4) gives only `E X`; it does not imply (4.1).  The same mean
is compatible with a probability `exp[-O(W log m)]` of zero defect and a
defect of order `sqrt(m)W` on the complement.  Such a distribution would
leave enough exceptional families for existence.  Positive association
of hole events makes the all-covered event more, not less, likely than the
independent product benchmark.

Moreover, when `lambda_q` is close to one the hole probability is a
constant.  The coefficient depends strongly on the surrogate model.  In
an independent-Bernoulli hole model the zero-hole cost is
`-N_q log(1-e^{-lambda_q})`; in the independent-ball occupancy model with
`N` balls and `N` bins it is

\[
 -\log(N!/N^N)=N+o(N),
\]

rather than `N/e`.  More generally the occupancy-surjection rate has
`I(1)=1` and tends to `e^{-lambda}` only when the holes are rare.  A row
of the wreath catalogue, however, contributes a structured block of `n`
distinct intervals, not independent balls.  Thus even the occupancy rate
is a surrogate, not a proved rate for wreath families.  The coefficient
in a putative version of (4.1) cannot be read from the expected-hole
constant.

After the exact complementation factor `1/2` and the occupancy correction
near `lambda=1`, a numerical constant of order `0.4` for the one-sided
large-deviation integral is plausible.  No particular value is presently
proved; the robust heuristic content is the scale `Theta(sqrt(m)W)`.

No inequality of the form (4.1) is presently proved for cyclic-order
families, still less for exact wreath factors.  Establishing it would be a
new supersaturation/counting theorem, not a first-moment calculation.

## 5. What the ledger does rule out

The calculation rigorously identifies the scale at which an
independent-shadow proof must fail.  Any construction theorem which also
proves that its band-hole lower tail has independent/Poisson cost
`exp[-Theta(sqrt(m)W)]` cannot produce a `T(1+o(1))` family, because its
entire catalogue has only `exp[O(W log m)]` members.

In particular the ledger is a strong warning against:

1. independent row selection;
2. free independent phase assignment;
3. a depthwise product estimate which treats `Theta(sqrt(m))` shadows as
   independent;
4. an entropy-compression argument whose reachable family has
   `exp[o(sqrt(m)W)]` states and whose good states are proved only by an
   independent lower-tail estimate.

It is not a statewise invariant.  It does not rule out a recursive design,
an exact algebraic identity, a correlated trade packet, or a small
reachable family containing a distinguished zero-defect state.

## 6. Exact counterweights to an impossibility interpretation

1. Without cyclic bundling, the integral balanced-deletion-flow theorem
   gives zero quota overload simultaneously at every rank.  Thus nesting
   and simultaneous rank constraints alone carry no intrinsic
   `sqrt(m)W` entropy cost.
2. At `m=3`, the explicit `Q_7` wreath factor covers every proper rank;
   its pair loads are `1^7 2^14` and its singleton loads are `5^7`.
3. At `m=4`, the six-switch factor in
   `WREATH_SHADOW_SWITCH_AUDIT.md` covers every rank of `Q_9`.  Two further
   switches give the optimally balanced first-shadow histogram
   `1^42 2^42` while preserving full verticality.

These finite designs do not settle the asymptotic problem, but they prove
that no universal finite-rank synchronization obstruction exists and they
are direct examples of the correlations omitted by (2.4).

## 7. Correct strategic conclusion

The entropy ledger is a **methodological no-go**, not an existence no-go:

\[
 \boxed{
 \text{a successful Gaussian-band proof must expose a deterministic
 cross-depth identity or an equally strong correlated design theorem.}}
\tag{7.1}
\]

The common-core Motzkin quotient, the `p+2` two-cross trade sector, and the
noncommuting affine-grid gate are retained precisely because they seek
such identities.  Random/free-phase variants of those lanes should be
discarded.

## 8. Exact conditional-cost formulation

There is one rigorous way to state the correlation requirement without
assigning an occupancy rate to a wreath shadow.  Let `mathfrak F_0` be
the set of exact middle wreath factors.  Fix nonnegative tolerances
`eta_q`, and let `mathfrak F_q subseteq mathfrak F_0` consist of the
factors satisfying the chosen shadow requirement through depths
`1,...,q` (for example `H_j(F)<=eta_j W` for every `j<=q`).  Whenever
`mathfrak F_q` is nonempty, put

\[
 \Delta_q=\log {|\mathfrak F_{q-1}|\over|\mathfrak F_q|}.
\tag{8.1}
\]

Then the identity

\[
 \boxed{
 \sum_{q=1}^Q\Delta_q
   =\log {|\mathfrak F_0|\over|\mathfrak F_Q|}
   \le \log\binom RT
   \le W(\log m-1+o(1))}
\tag{8.2}
\]

is exact.  In particular, if `Q=Theta(sqrt(m))` and a good factor exists,
the average conditional cost of a new depth is at most

\[
                   O\left({W\log m\over\sqrt m}\right)=o(W).
\tag{8.3}
\]

Thus a Gaussian-window theorem really does require almost all later
depths to become nearly free *conditional on the earlier depths*.  This
is a necessary counting statement, not a probabilistic heuristic.
Conversely, proving `Delta_q>=cW` for `Omega(sqrt(m))` depths would be a
valid nonexistence theorem.  No such conditional lower bound is known.

The often suggested estimate

\[
                    |\mathfrak F_0|\approx
                    \exp\{W(\log m-2)\}
\tag{8.4}
\]

is itself a random-perfect-matching heuristic.  It is not currently an
enumeration theorem for exact MSW/wreath factors and must not be used as
an input to (8.2).  The unconditional upper bound (1.1) is sufficient for
the necessary conclusion (8.3).
