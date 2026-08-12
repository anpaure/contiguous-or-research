# All-slot Bellman clocks: first-crossing deletion and a maximum-density Apéry theorem

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It gives a canonical
minimal-counterexample normalization and an exact eventually periodic normal
form for every finite Bellman table.  It does not prove Gaussian positivity.

Put

\[
 A={\sqrt\pi\over2}
\]

and let

\[
 K(x)=
 \begin{cases}
 1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
 -e^{-(A+x)^2},&x>A.
 \end{cases}                                         \tag{0.1}
\]

Let

\[
 (c_0,c_1,\ldots,c_n),\qquad c_0=0,                 \tag{0.2}
\]

be a finite nonnegative internally superadditive table:

\[
 c_{i+j}\ge c_i+c_j\qquad(i,j\ge0,\ i+j\le n),    \tag{0.3}
\]

and assume `c_n>=A`.  Its unbounded-knapsack Bellman clock is

\[
 V_0=0,\qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j}).       \tag{0.4}
\]

The Bellman functional is

\[
 \Phi(c)=\sum_{m\ge0}K(V_m).                        \tag{0.5}
\]

All series below converge absolutely after their finite compact heads.

## 1. Deletion after the first crossing of the Gaussian threshold

Internal superadditivity gives

\[
 V_m=c_m\qquad(0\le m\le n),                       \tag{1.1}
\]

because the one-part configuration attains `c_m`, while repeated use of
(0.3) bounds every partition of `m` by `c_m`.

### Theorem 1.1 (first-crossing reduction)

Let

\[
 N=\min\{j\in\{1,\ldots,n\}:c_j\ge A\}.            \tag{1.2}
\]

Let `W` be the Bellman clock generated only by the prefix

\[
 (c_0,c_1,\ldots,c_N).                              \tag{1.3}
\]

Then

\[
 W_m=V_m=c_m\quad(0\le m\le N),                    \tag{1.4}
\]

and

\[
 A\le W_m\le V_m\quad(m\ge N).                    \tag{1.5}
\]

Consequently

\[
 \boxed{\Phi(c_0,\ldots,c_N)\le\Phi(c_0,\ldots,c_n).}
                                                               \tag{1.6}
\]

In particular, if a negative finite Bellman table exists, then one exists
whose endpoint is the first threshold crossing:

\[
 c_j<A\quad(1\le j<n),\qquad c_n\ge A.             \tag{1.7}
\]

#### Proof

The prefix still satisfies (0.3), so (1.4) follows from (1.1).  Removing
generators can only decrease a knapsack maximum, hence `W_m<=V_m`.
For `m>=N`, the configuration consisting of one size-`N` generator and a
nonnegative exact fill of the remaining `m-N` slots gives

\[
 W_m\ge c_N+W_{m-N}\ge A.
\]

This proves (1.5).  The kernel `K` is increasing on `[A,infinity)`, so

\[
 K(W_m)\le K(V_m)\qquad(m\ge N).
\]

Together with (1.4), termwise summation proves (1.6).  Also
`W_m>=floor(m/N)c_N`, so the two Gaussian tails are absolutely summable.
The last assertion follows by applying the construction to any negative
table. \(\square\)

This is a deletion statement confined to the monotone tail of `K`.  It is
not denomination-insertion monotonicity; an undominated insertion can lower
the functional.

### Theorem 1.2 (endpoint saturation)

Assume the table is already in first-crossing form (1.7).  Let

\[
 P_n=\max\left\{
   \sum_{i=1}^m c_{j_i}:
   m\ge2,\ 1\le j_i<n,\ \sum_i j_i=n
 \right\},                                           \tag{1.8}
\]

with `P_n=0` if the displayed family is empty.  Replace only the endpoint
by

\[
                         c_n'=\max\{A,P_n\}.          \tag{1.9}
\]

Then the new table is internally superadditive, its Bellman clock `V'`
satisfies

\[
 V_m'=V_m\quad(m<n),
 \qquad A\le V_m'\le V_m\quad(m\ge n),              \tag{1.10}
\]

and consequently

\[
                         \boxed{\Phi(c')\le\Phi(c)}. \tag{1.11}
\]

Thus a negative table may additionally be assumed to have the saturated
endpoint (1.9).  If `P_n>=A`, the endpoint generator is inert: every use
of it can be replaced by a configuration of smaller denominations having
the same capacity and value at least `c_n'=P_n`.  If `P_n<A`, one may
normalize the endpoint exactly to `c_n'=A`.

The inert case cannot simply be discarded while retaining the
first-crossing normalization: after deleting denomination `n`, all
remaining displayed generator values can be below `A`, even though their
Bellman clock eventually crosses `A`.  Re-extending that shorter clock to
its first crossing merely reinstalls an inert threshold endpoint.  Thus
Theorem 1.2 does not by itself imply that a minimal first-crossing
certificate has `c_n=A`.

#### Proof

For `n=1`, (1.9) simply replaces `c_1` by `A`, and every assertion follows
directly.  Assume `n>=2` below.

Every lower-index partition of `n` has value at most `P_n`, so (1.9)
preserves all superadditivity inequalities whose right side is `c_n`.
All lower inequalities are unchanged.  Also
`P_n>=c_{n-1}+c_1>=c_{n-1}`, so monotonicity at the endpoint is preserved.
Repeated use of the original superadditivity inequalities gives
`c_n>=P_n`; together with `c_n>=A`, this proves `c_n'<=c_n`.

Lowering one generator can only lower the Bellman clock, and capacities
below `n` do not use that generator.  For `m>=n`, one endpoint generator
followed by nonnegative size-one fill gives `V_m'>=c_n'>=A`.  Hence both
clocks lie in the increasing tail of `K`, proving (1.10)--(1.11)
termwise.  When `P_n>=A`, choose an attaining partition in (1.8) and
replace each endpoint generator independently; this proves inertness.
\(\square\)

## 2. Critical density and the reduced residue graph

For an arbitrary finite nonnegative generator table, put

\[
 \lambda=\max_{1\le j\le n}{c_j\over j}>0,
 \qquad
 S=\{j:c_j=j\lambda\},
 \qquad
 g=\gcd S,                                          \tag{2.1}
\]

and define the reduced weights

\[
 d_j=c_j-j\lambda\le0.                              \tag{2.2}
\]

The indices in `S` are the critical, maximum-density denominations.  They
have zero reduced weight and are all divisible by `g`; every other
denomination has strictly negative reduced weight.

Consider the directed graph on `Z/gZ` having, for every `j` not in `S`,
an edge

\[
 r\longmapsto r+j\pmod g
\]

of weight `d_j`.  For `r in Z/gZ`, let `beta_r` be the maximum weight of a
walk from zero to `r`; set `beta_0=0`.

### Lemma 2.1 (finite Apéry witnesses)

Every `beta_r` is finite and is attained by a simple walk.  Hence one may
choose an attaining walk `P_r` with at most `g-1` edges and ordinary
capacity

\[
 \ell_r:=\sum_{j\text{ used by }P_r}j\le(g-1)n.     \tag{2.3}
\]

#### Proof

If `g>1`, denomination one is noncritical and the graph is reachable from
zero; if `g=1`, there is only the zero residue.  Every noncritical edge has
strictly negative weight.  Removing the segment between two repeated
vertices therefore strictly increases the weight.  A maximizing walk is
simple and has at most `g-1` edges.  There are only finitely many simple
walks, so a maximum is attained, and (2.3) follows. \(\square\)

## 3. A conductor bound for the critical semigroup

Let

\[
 S'=\{j/g:j\in S\},\qquad
 a=\min S',\qquad N_*=\max S'.                     \tag{3.1}
\]

Then `gcd(S')=1`, `a<=n/g`, and `N_*<=n/g`.

### Lemma 3.1 (elementary conductor bound)

Every integer

\[
 k\ge (a-1)N_*                                     \tag{3.2}
\]

is a nonnegative integer combination of elements of `S'`.  Equivalently,
every multiple of `g` at least

\[
 C_*:=g(a-1)N_*\le(a-1)n                           \tag{3.3}
\]

belongs to the semigroup generated by `S`.

#### Proof

Use the elements of `S'` as directed steps on `Z/aZ`.  Since their gcd is
one, every residue is reachable from zero.  A shortest residue walk is
simple, hence uses at most `a-1` steps and has an ordinary sum at most
`(a-1)N_*`.  For each residue choose such a represented sum `h_r`.
If `k>=max_r h_r` and `k` has residue `r`, then

\[
 k=h_r+qa\qquad(q\ge0),
\]

and `a` itself lies in `S'`.  This proves (3.2), and scaling by `g` proves
(3.3). \(\square\)

## 4. The all-slot maximum-density Apéry theorem

### Theorem 4.1 (eventual exact cosets)

For every residue `r in Z/gZ`,

\[
 \boxed{
 V_m=\lambda m+\beta_r
 \quad\text{whenever}\quad
 m\equiv r\pmod g,
 \quad m\ge\ell_r+C_*.
 }                                                     \tag{4.1}
\]

In particular the formula holds for every

\[
 \boxed{m\ge n(n-1).}                               \tag{4.2}
\]

Thus every finite Bellman clock is eventually a union of `g` shifted
arithmetic clocks of common period

\[
 P=g\lambda.                                        \tag{4.3}
\]

#### Proof

Every exact-fill configuration of capacity `m` is a residue walk from zero
to `m mod g`, and

\[
 \sum c_j=\lambda m+\sum d_j.                       \tag{4.4}
\]

Critical steps have zero reduced weight and are residue loops.  Deleting
them leaves a walk in the graph of Section 2, so (4.4) is at most
`lambda m+beta_r`.

Conversely, take the attaining path `P_r`.  If
`m>=ell_r+C_*` and `m=ell_r mod g`, Lemma 3.1 writes `m-ell_r` as a sum of
critical denominations.  Appending those zero-reduced-weight steps to
`P_r` gives an exact-fill configuration of capacity `m` and value
`lambda m+beta_r`.  This proves (4.1).

By (2.3) and (3.3), a sufficient threshold is

\[
 (g-1)n+(a-1)n=(g+a-2)n.                            \tag{4.5}
\]

Since `a<=n/g` and `1<=g<=n`,

\[
 g+a\le g+{n\over g}\le n+1.
\]

Substitution in (4.5) proves (4.2). \(\square\)

The bound (4.2) is uniform and deliberately coarse.  The exact residue
thresholds `ell_r+C_*` are usually much smaller; for example, when the
unique critical denomination is the endpoint `n`, the critical conductor
is zero and only the simple residue paths remain.

### Corollary 4.2 (finite head plus shifted Gaussian lattices)

Put

\[
 s_r=\lambda r+\beta_r,
 \qquad P=g\lambda,
 \qquad
 Q_r=\max\left\{0,\left\lceil{n(n-1)-r\over g}\right\rceil\right\}.
                                                               \tag{4.6}
\]

Then the Bellman functional has the exact decomposition

\[
 \boxed{
 \Phi(c)=
 \sum_{r=0}^{g-1}
 \left(
   \sum_{0\le q<Q_r}K(V_{qg+r})
   +\sum_{q\ge Q_r}K(qP+s_r)
 \right).
 }                                                     \tag{4.7}
\]

All nonperiodicity is therefore confined to the capacities
`m<n(n-1)`.  Each eventual shift `s_r` has a certificate using at most
`g-1` subcritical denominations, followed only by critical padding.

#### Proof

For `m=qg+r>=n(n-1)`, Theorem 4.1 gives

\[
 V_{qg+r}=q(g\lambda)+(\lambda r+\beta_r)=qP+s_r.
\]

Splitting each residue row before `Q_r` proves (4.7). \(\square\)

## 5. Minimal-counterexample form and exact scope

Combining Theorems 1.1, 1.2, and 4.1 gives the following proof-safe
statement.

### Corollary 5.1 (canonical finite counterexample certificate)

If the universal Bellman inequality fails, it fails for a table satisfying
(1.7) and the endpoint saturation (1.9).  For that table, choose its
critical density data `(lambda,S,g)`.
Its entire negative certificate consists of

1. the finite Bellman head at capacities `m<n(n-1)`;
2. at most `g` shifted arithmetic Gaussian tails of common period
   `P=g lambda`;
3. simple Apéry witnesses of at most `g-1` subcritical steps per residue;
4. critical-semigroup padding with the explicit conductor bound (3.3).

There is no infinite or unstructured Bellman recursion left.

A denomination `j` which can already be matched at capacity `j` by the
other denominations is inert: replacing each use of `j` by that matching
configuration leaves every `V_m` unchanged.  Thus an active-support-minimal
certificate may additionally be assumed to contain no such dominated
generator.  This is exact deletion, not a claim that inserting an
undominated generator has a favorable sign.

The theorem does **not** bound the grid size `n` by an absolute constant,
does not sign the finite head in (4.7), and does not prove the universal
Rayleigh coagulation or Gaussian Bellman inequality.  Its gain over the
one-period residue relaxation is that the eventual cosets and every carry
are derived from the exact Bellman clock, while all remaining transients
are explicitly finite.
