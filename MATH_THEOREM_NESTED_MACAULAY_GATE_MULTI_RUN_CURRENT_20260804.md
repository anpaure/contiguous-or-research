# Nested Macaulay gates: exact multi-run shielding and a full-colex current criterion

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical theorem.  It composes every
strict-aperture jump among the nontrivial aperture-at-least-two runs in a
canonical Macaulay expansion.  The maximal
constant-aperture run roots form a nested chain, and the active-core
intersection at an owner is determined solely by the uppermost active run.
All deeper jump gates are shielded.  This gives an exact multi-run
protected-current decomposition and one explicit scalar sufficient
criterion for the entire colex complement.  It does not prove that the
criterion holds for every localized colex profile.

No computation, search, or solver result is used.

## 0. Abstract nested-gate DNF

Put

\[
 n=2m-1,
 \qquad \mathcal L=\binom{[n]}{m-1}.
\]

Choose pairwise disjoint sets

\[
 R_0,G_1,\ldots,G_T,X_0,\ldots,X_T,
\]

and define nested roots

\[
 R_t=R_0\mathbin{\dot\cup}G_1\mathbin{\dot\cup}\cdots
      \mathbin{\dot\cup}G_t
 \qquad(0\le t\le T).
\tag{0.1}
\]

Assume

\[
 |R_T|+1\le m-2.
\tag{0.2}
\]

Run `t` carries the clauses `R_t+x`, `x in X_t`.  Define

\[
 \mathcal D
 =\bigcup_{t=0}^T
   \{L\in\mathcal L:R_t\subseteq L, L\cap X_t\ne\varnothing\}.
\tag{0.3}
\]

For an owner `U`, call run `t` active when

\[
 R_t\subseteq U,
 \qquad U\cap X_t\ne\varnothing.
\]

If some run is active, let `tau(U)` be the least active index, i.e. the
uppermost active run.

## 1. The uppermost-active-run law

### Theorem 1.1 (nested active-core intersection)

If no run is active, the owner fibre is empty.  Otherwise the intersection
`J_U` of all active clause cores is

\[
 \boxed{
 J_U=
 \begin{cases}
  R_{\tau(U)}\cup\{x\},&\text{exactly one clause is active},\\
  R_{\tau(U)},&\text{at least two clauses are active},
 \end{cases}}
\tag{1.1}
\]

where `x` is the unique active pivot in the first row.  The selected-facet
multiplicity is

\[
 \boxed{a_U=m-|J_U|.}
\tag{1.2}
\]

Every nonzero fibre has size at least two.

#### Proof

Within the uppermost active run, multiple active pivots intersect to its
root; a unique active pivot leaves `R_tau+x`.  Every lower active root
contains `R_tau`, but its gate coordinates and pivots are disjoint from
`X_tau`.  Thus intersecting with any lower active clause deletes the unique
upper pivot and leaves exactly `R_tau`.  This proves (1.1).  Accepted
facets delete outside the active-core intersection, proving (1.2).
Condition (0.2) bounds every clause core by `m-2`. \(\square\)

In particular, when `tau(U)=t`, every deeper gate

\[
 G_{t+1},\ldots,G_T
\]

is absent from `J_U` and therefore creates no protected loss at that owner.

## 2. Exact multi-run protected current

For a protected incidence `UL`, write `del(U,L)` for the coordinate in
`U-L`.  Define:

* `xi_0`: active-owner incidences deleting a coordinate of `R_0`;
* for `1<=i<=T`, `xi_i`: incidences deleting a coordinate of `G_i` at an
  owner with `tau(U)>=i`; and
* for `0<=t<=T`, `eta_t`: incidences at an owner with exactly one active
  clause, that clause belonging to run `t`, and deleting its unique pivot.

### Theorem 2.1 (exact nested-gate current)

For every protected bank of maximum degree at most two,

\[
 \boxed{
 \lambda_P(\mathcal D)
 =\xi_0+\sum_{i=1}^T\xi_i+\sum_{t=0}^T\eta_t.}
\tag{2.1}
\]

#### Proof

Every active fibre has size at least two, so protected loss consists of
protected deletions in `J_U`.  If the uppermost active run is `t`, its root
is

\[
 R_t=R_0\mathbin{\dot\cup}G_1\mathbin{\dot\cup}\cdots
     \mathbin{\dot\cup}G_t.
\]

These are exactly the root and gate currents `xi_0,...,xi_t`.  A pivot is
present in `J_U` exactly in the unique-active-clause row of (1.1), giving
one `eta_t`.  The current families are disjoint and exhaustive. \(\square\)

Now assume `P` is a union of resident simple owner paths.  Let
`mathscr P(B)` denote the paths containing an owner above `B`.

### Corollary 2.2 (linear all-run path bound)

\[
 \boxed{
 \xi_0\le2|\mathscr P(R_0)|,
 \qquad
 \xi_i\le2|\mathscr P(R_i)|\quad(1\le i\le T),}
\tag{2.2}
\]

and

\[
 \boxed{
 \eta_t\le2|X_t|\,|\mathscr P(R_t)|.}
\tag{2.3}
\]

Hence

\[
 \boxed{
 \lambda_P(\mathcal D)
 \le2\sum_{t=0}^T(|X_t|+1)|\mathscr P(R_t)|.}
\tag{2.4}
\]

#### Proof

Positions containing a fixed nested root form one interval on a resident
path.  A deletion in its newest gate, or in the base root, can occur only
on one of the two boundary incidences.  Each pivot coordinate likewise has
one occurrence interval and at most two boundary incidences.  State
restrictions in the definitions of `xi_i,eta_t` can only delete
contributions.  Sum over paths. \(\square\)

There is also the clause-wise bound

\[
 \boxed{
 \lambda_P(\mathcal D)
 \le\sum_{t=0}^T\sum_{x\in X_t}
       \lambda_P(\mathcal A_{R_t\cup\{x\}}).}
\tag{2.5}
\]

Indeed every deletion in `J_U` belongs to every active core and hence is
counted by at least one active individual clause.

## 3. Exact realization by all nontrivial Macaulay runs

Delete the isolated full-shore endpoint, if present, and partition the
remaining canonical Macaulay expansion into its maximal consecutive
constant-`rho_j` runs of aperture at least two.  Index these runs from the
highest Macaulay indices downward, so their apertures satisfy

\[
 \rho^{(0)}>\rho^{(1)}>\cdots>\rho^{(T)}.
\tag{3.1}
\]

Let `R_t,X_t` be the common root and pivot set of run `t`.

### Theorem 3.1 (Macaulay gate chain)

There are pairwise disjoint gates `G_1,...,G_T` such that

\[
 \boxed{
 R_t=R_0\mathbin{\dot\cup}G_1\mathbin{\dot\cup}\cdots
      \mathbin{\dot\cup}G_t,}
\tag{3.2}
\]

and

\[
 \boxed{|G_t|=\rho^{(t-1)}-\rho^{(t)}.}
\tag{3.3}
\]

All gates, roots, and run pivot sets have exactly the disjointness required
in Section 0.  When every nontrivial aperture is at least two, the full
principal-star DNF of the colex complement is therefore exactly (0.3).

#### Proof

The strict-jump root relation applied at every consecutive pair of runs
gives

\[
 R_t=R_{t-1}\mathbin{\dot\cup}G_t
\]

with the displayed gate size.  The gates occupy the coordinate intervals
between the last lower pivot of the higher-index run and the first pivot of
the next run.  These intervals are pairwise disjoint and avoid every run's
pivot interval.  Induction gives (3.2), and the common-root run identity
identifies the resulting DNF with the full colex complement. \(\square\)

## 4. One full-colex scalar criterion

Before using the global Macaulay identity, there is an exact disjoint
formula for the scalar slack of the nested DNF itself.  Put

\[
 \rho_t=m-|R_t|-1,
 \qquad h_t=|X_t|,
 \qquad H_t=\sum_{u<t}h_u.
\tag{4.1}
\]

Here `H_t` counts the pivot labels in runs that are earlier in the present
uppermost-first indexing.  For `q in {m-1,m}`, let `C_t(q)` be the rank-`q`
sets whose least active run is `t`.

### Theorem 4.1 (disjoint least-active scalar formula)

The categories `C_t(q)` are disjoint and exhaust the rank-`q` part of the
nested DNF, and

\[
 \boxed{
 |C_t(q)|
 =\binom{m+\rho_t-H_t}{q-|R_t|}
  -\binom{m+\rho_t-H_t-h_t}{q-|R_t|}.}
\tag{4.2}
\]

In particular, if every `rho_t>=2`, then

\[
\boxed{
 {\sigma(\mathcal D)\over2}
 =\sum_{t=0}^T\left[
   \binom{m+\rho_t-H_t}{\rho_t+1}
   -\binom{m+\rho_t-H_t-h_t}{\rho_t+1}
   -\binom{m+\rho_t-H_t}{\rho_t}
   +\binom{m+\rho_t-H_t-h_t}{\rho_t}
 \right].}
\tag{4.3}
\]

#### Proof

A set whose least active run is `t` must contain `R_t`, avoid every
earlier pivot bank `X_u`, `u<t`, and hit `X_t`.  Conversely these three
conditions make `t` its least active run.  The available ground set outside
`R_t` has size `m+rho_t`; forbidding the earlier pivot banks removes
exactly `H_t` labels.  Choosing the remaining `q-|R_t|` coordinates, and
subtracting the choices which avoid `X_t`, proves (4.2).

The categories are disjoint by definition.  When every `rho_t>=2`, every
nonempty owner fibre has size at least two by Theorem 1.1.  Consequently

\[
 {\sigma(\mathcal D)\over2}
 =|N(\mathcal D)|-|\mathcal D|
 =\sum_t\bigl(|C_t(m)|-|C_t(m-1)|\bigr),
\]

and substituting (4.2) gives (4.3). \(\square\)

Thus even the exact scalar slack has no exponential inclusion--exclusion:
the least-active partition linearizes every strict jump.

### The canonical full-colex identity

Assume every Macaulay aperture satisfies

\[
 \rho_j\ge2.
\tag{4.4}
\]

If the expansion contains the isolated full-shore endpoint
`j=m,c_m=n`, remove it before forming the run DNF.  Its complement is the
complete lower shore and its contribution to both sides of the scalar
identity below is zero; its formal pivot `p_m=n+1` is not a coordinate.

Then every nonzero owner fibre is at least two.  Since the ordinary shadow
of the initial colex segment has size

\[
 \sum_{j=s}^m\binom{c_j}{j-1},
\]

one has the exact scalar identity

\[
 \boxed{
 {\sigma(A)\over2}
 =\sum_{j=s}^m
   \left(\binom{c_j}{j-1}-\binom{c_j}j\right)
 =\sum_{j=s}^m
   \left({j\over\rho_j}-1\right)b_j.}
\tag{4.5}
\]

For the constant-spread reservoir, put

\[
 N_\rho=H_\rho(m)+m+H_d.
\]

### Corollary 4.2 (full nested-gate safe criterion)

The entire colex-complement cut is safe whenever

\[
 \boxed{
 \sum_{j=s}^m\left({j\over\rho_j}-1\right)b_j
 \ge
 \min\left\{
   \sum_{t=0}^T(|X_t|+1)N_{\rho^{(t)}+1},
   \sum_{t=0}^T|X_t|N_{\rho^{(t)}}
 \right\}.}
\tag{4.6}
\]

#### Proof

The common-root trace count gives

\[
 |\mathscr P(R_t)|\le N_{m-|R_t|}=N_{\rho^{(t)}+1},
\]

so (2.4) supplies twice the first term on the right.  Every individual
clause in run `t` has residual rank `rho^(t)` and protected loss at most
`2N_(rho^(t))`, so (2.5) supplies twice the second.  Equation (4.5) is half
the scalar slack.  Thus (4.6) implies `lambda<=sigma`. \(\square\)

## 5. Exact frontier

The multi-run composition problem is now algebraically closed:

* the uppermost active run determines the active root;
* all deeper gates are shielded;
* the literal loss is the exact nested current (2.1); and
* the scalar slack is the disjoint category sum (4.3), with no
  exponential inclusion--exclusion; and
* the whole colex cut has the one-line sufficient criterion (4.6).

What remains is quantitative: prove (4.6) for every localized canonical
profile, or combine it with the singleton erosion theorem when one or more
terminal apertures equal one.  The present theorem does not prove that
last inequality.

## 6. Dependencies

| role | file | SHA-256 |
|---|---|---|
| Macaulay interval/DNF erosion theorem | `MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md` | `77253694d02d6d11c41a21b9875af843ede525d1751bca7d2463ac014b174cec` |
| common-root run theorem | `MATH_THEOREM_COMMON_ROOT_MACAULAY_RUN_EXACT_CURRENT_20260804.md` | `83db1a8e67e359025a03b0d704feb5aad81aaaae49a3e4f5339eb948edbfd189` |
| strict two-run shielding theorem | `MATH_THEOREM_STRICT_MACAULAY_JUMP_TWO_RUN_SHIELDING_CURRENT_20260804.md` | `8dd7fe2074032e5376a5be55b7769437f90e6bc7b95ffd7482024bef1101ed6b` |
