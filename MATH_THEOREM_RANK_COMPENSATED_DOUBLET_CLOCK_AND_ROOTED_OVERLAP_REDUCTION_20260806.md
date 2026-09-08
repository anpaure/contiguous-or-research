# Rank-compensated doublet clocks and the rooted-overlap reduction

**Date:** 2026-08-06  
**Method:** exact weighted product-residual algebra, competing exponential
clocks, and FIFO overlap-pattern bookkeeping; no computation or search  
**Status:** unconditional compensation and drift identities, and a
proof-safe reduction of the balanced-doublet packing gate.  The correct
clock multiplies an `h`-doublet rate by the inverse survival probability of
its other non-slot resources.  This preserves the exact `2/3` mixture down
to density `Theta(1/d)`, gives pair ratio `O(d^-2)`, and enlarges the
companion parameter only by a factor `O(d)`.  For a macroscopically
separated atomic template, the rooted average-overlap estimate is proved by
slot suppression, far-half entropy, synchronized-chain moments, and a
private-split entry calculation; the same enumeration closes the
three-edge first-two-hit energy needed by the dynamic square drift.
Integral rounding is reduced to signed root self-correction and two
explicit stopped hazard-error transfers, with an analytically charged bad
set.  The pure two-root service compensator and global-rate reconstruction
are closed abstractly, but the incidence-spread/error transfer is not
proved here.  The scalar near-isotropy shortcut is false on slow Johnson
harmonics; the corrected local target is the stopped sector row `(JSEC)`
in the joint-Lyapunov note.  In particular, no fixed-rank nibble theorem is
invoked.

## 1. The weighted balanced-doublet host

Put

\[
 M={k\choose t},\qquad W={k\choose r},\qquad
 \rho={W\over M},\qquad
 L_*={M\over kd},\qquad L=\lceil L_*\rceil,
 \tag{1.1}
\]

and

\[
 \sigma={L_*\over L}={M\over kdL}.
 \tag{1.2}
\]

Use the slot-augmented balanced-doublet host
`B_2 union B_3` from
`MATH_THEOREM_ATOMIC_FIFO_PORTAL_TILE_AND_BALANCED_DOUBLET_REDUCTION_20260806.md`.
An edge in `B_h` contains

\[
 \ell_h=2d\quad\hbox{lower resources},\qquad
 o_h=2h(d+1)\quad\hbox{owner resources},\qquad
 2\quad\hbox{slots}.
 \tag{1.3}
\]

Write

\[
 N_h=\ell_h+o_h=2d+2h(d+1),\qquad R_h=N_h+2.
 \tag{1.4}
\]

Thus `R_2=6d+6` and `R_3=8d+8`.

Give an augmented edge over a base doublet in `D_h` the weight

\[
 \omega_E={\lambda_hM\over2d|D_h|L^2},
 \tag{1.5}
\]

where

\[
 \lambda_3={\rho d\over d+1}-2,
 \qquad
 \lambda_2=3-{\rho d\over d+1}.
 \tag{1.6}
\]

For a resource vertex `v`, put

\[
                         \ell(v)=\sum_{E\ni v}\omega_E.
 \tag{1.7}
\]

The exact fractional-factor calculation gives

\[
 \ell(v)=1\quad(v\hbox{ lower or owner}),
 \qquad
 \ell(v)=\sigma\quad(v\hbox{ a slot}).
 \tag{1.8}
\]

The total base weight of orbit `h` is

\[
 \boxed{\Omega_h:=\sum_{E\in B_h}\omega_E
       ={\lambda_hM\over2d}.}
 \tag{1.9}
\]

Indeed, sum the lower loads from orbit `h`: they equal `lambda_h M`,
while every edge is counted `2d` times.  In particular,

\[
 \Omega_2+\Omega_3={M\over2d}.
 \tag{1.10}
\]

The weighted mean multiplicity is

\[
 \boxed{\bar h:=2\lambda_2+3\lambda_3
             ={\rho d\over d+1}.}
 \tag{1.11}
\]

These two elementary identities are the source of the exact density drift
below.

### 1.1 Choose a macroscopically separated doublet orbit

The local atomic theorem only requires the two headers of a balanced
doublet to have Johnson distance greater than `2d`.  For residual rounding,
choose the fixed template more specifically.  If its headers are `H^1,H^2`
and both contain the port pair `{u,v}`, require

\[
 \alpha k\le |H^1-H^2|=|H^2-H^1|\le\beta k
 \tag{1.12}
\]

for fixed feasible `0<alpha<beta<1/2`.  For example, a sufficiently small
fixed `alpha` works throughout the central range.  The `O(d)` private tail
and continuation labels still fit in the complement of the two headers.

Taking the complete coordinate orbit of this template changes none of
(1.3)--(1.11): coordinate transitivity, edge ranks, and every incidence
double count are identical.  It adds a macroscopic entropy reserve which
is invisible to pair codegrees but essential for the largest overlap
pattern in Section 5.

## 2. The exact rank compensation

Retain every lower and owner resource independently with probability `p`,
and retain every slot independently with probability `p_s`.  Let `U` be
the retained resource set.  For `E in B_h`, define the compensated residual
rate

\[
 \boxed{
 a_E(p,p_s)=
 \omega_Ep^{-(N_h-1)}p_s^{-2}
             1_{\{E\subseteq U\}}.}
 \tag{2.1}
\]

The exponent is `N_h-1`, not `R_h-1`: the two slot survival factors are
compensated separately.  This distinction makes the ceiling in `L` exact.

For a set `Q` of resource vertices, write

\[
 d_a(Q)=\sum_{E\supseteq Q}a_E(p,p_s),
 \qquad
 d_\omega(Q)=\sum_{E\supseteq Q}\omega_E.
 \tag{2.2}
\]

### Theorem 2.1 (exact product-residual identities)

The following identities hold without an asymptotic error.

1. If `v` is a lower or owner resource, then
   \[
   \mathbb E[d_a(v)\mid v\in U]=\ell(v)=1.
   \tag{2.3}
   \]
2. If `s` is a slot, then
   \[
   \mathbb E[d_a(s)\mid s\in U]
       ={p\over p_s}\ell(s)={\sigma p\over p_s}.
   \tag{2.4}
   \]
3. If `Q` consists of `q` lower/owner resources and `s` slots, then
   \[
   \boxed{
   \mathbb E[d_a(Q)\mid Q\subseteq U]
       =p^{1-q}p_s^{-s}d_\omega(Q).}
   \tag{2.5}
   \]
4. The total compensated rate in orbit `h` satisfies
   \[
   \boxed{
   \mathbb E\sum_{E\in B_h}a_E(p,p_s)=p\Omega_h
        ={p\lambda_hM\over2d}.}
   \tag{2.6}
   \]

#### Proof

Condition on a retained lower or owner `v`.  An edge in `B_h` through `v`
has `N_h-1` other non-slot resources and two slots.  Its conditional
survival probability is `p^(N_h-1)p_s^2`, which cancels (2.1).  Summing
gives (2.3).

Condition instead on one retained slot.  The other resources of an edge are
`N_h` non-slots and one slot, so the cancellation leaves the factor

\[
 p^{N_h}p_s\,p^{-(N_h-1)}p_s^{-2}={p\over p_s}.
\]

This proves (2.4).  For general `Q`, the unconditioned resources in an edge
number `N_h-q` on the non-slot shore and `2-s` on the slot shore.  The same
cancellation gives `p^(1-q)p_s^(-s)`, proving (2.5).  Finally, an
unconditioned edge survives with probability `p^N_h p_s^2`; multiplication
by (2.1) leaves `p`.  Sum and use (1.9).  \(\square\)

### Corollary 2.2 (the `2/3` mixture does not drift)

In the product residual, a clock chosen proportionally to the total
compensated rates has

\[
                         \Pr(h=2)=\lambda_2,
 \qquad                  \Pr(h=3)=\lambda_3.
 \tag{2.7}
\]

Consequently its expected resource consumption is

\[
 \boxed{
 2d\quad\hbox{lowers},\qquad
 2\rho d\quad\hbox{owners},\qquad
 2\quad\hbox{slots}.}
 \tag{2.8}
\]

#### Proof

Equation (2.6) has the same common factor `p` for both `h`, so (1.9)--(1.10)
give (2.7).  The owner mean is

\[
 \sum_{h=2}^3\lambda_h,2h(d+1)
       =2(d+1)\bar h=2\rho d
\]

by (1.11).  The other two counts are deterministic for every edge.
\(\square\)

This is the reason for rank compensation.  If one merely restricts the
base weights, the `h=3` orbit acquires an extra factor `p^(2d+2)` relative
to `h=2` and disappears long before the separator scale.  The owner/lower
ledger then fails.

## 3. Exact common-density drift and the slot ceiling

After `n` accepted doublets, the lower density is deterministically

\[
                         p_n=1-{2dn\over M}.
 \tag{3.1}
\]

The slot density is also deterministic:

\[
 \begin{aligned}
 p_{s,n}
   &=1-{2n\over kL}\\
   &=1-\sigma(1-p_n).
 \end{aligned}
 \tag{3.2}
\]

Thus `p_s>=p`, and for `p>=1/d`,

\[
 {p_s\over p}-1
 ={(1-\sigma)(1-p)\over p}
 \le {d\over L}.
 \tag{3.3}
\]

Since `L` is exponential in the central parameter, this is negligible
compared with every inverse power of `d`.

Under the ideal mixture (2.7), the expected owner-density decrement per
accepted edge is

\[
 {2\rho d\over W}={2d\over M},
 \tag{3.4}
\]

exactly the lower-density decrement.  Hence the mean-field trajectory is

\[
 p_{\rm lower}=p_{\rm owner}=p,
 \qquad
 p_{\rm slot}=1-\sigma(1-p).
 \tag{3.5}
\]

No approximation to `rho`, and no replacement of `L` by `L_*`, is used in
this equality.

## 4. Regenerated pair and marked-cluster rows

Assume a base weighted pair row

\[
 d_\omega(v,w)
       \le\delta_0\min\{\ell(v),\ell(w)\}
 \tag{4.1}
\]

for distinct non-slot resources.  The audited doublet host has

\[
                         \delta_0=O(d/k^2)=O(d^{-3})
 \tag{4.2}
\]

in the optimal central range `k=Theta(d^2)`.

Equations (2.3) and (2.5) show that the product-residual relative pair scale
is

\[
                         \delta(p)={\delta_0\over p}.
 \tag{4.3}
\]

At the stopping density `p>=c/d`,

\[
                         \delta(p)=O(d^{-2}).
 \tag{4.4}
\]

This is stronger than the `gamma/d` row sufficient for the fixed-factor
exponential-clock cylinder.

Now let `Sigma(E)` be the unordered marked occurrences carried by a
doublet.  Suppose the complete orbit satisfies, for compatible clusters of
at most three distinct owner carriers,

\[
 \sum_{E:A\subseteq\Sigma(E)}\omega_E
  \le \theta\kappa^{|A|-1}\ell(v(A)).
 \tag{4.5}
\]

For the fresh companion orbit the intended values are

\[
 \theta={1\over r(d+1)},
 \qquad
 \kappa\le {C\over N_*},
 \qquad
 \log N_*=\Theta(d\log d).
 \tag{4.6}
\]

The first is the exact pointed level-two marginal; the second is the
prospective companion-tail atom.

### Proposition 4.1 (the complete doublet orbit has the base cluster row)

For the macroscopically separated complete atomic-doublet orbit, (4.5)
holds through cluster size three with

\[
 \theta={1\over r(d+1)},
 \qquad
 \kappa={C\over N_*}.
 \tag{4.7}
\]

#### Proof

For one occurrence, forget the second member of its unordered port pair.
The resulting pointed level-two occurrence has exact marginal `theta`, so
the more specific unordered occurrence has marginal at most `theta`.

Conditional on one level-two owner in a constituent macro, every prescribed
companion copy fixes one tail from the prospective orbit.  After at most one
earlier companion has been exposed, at least `N_*` legal disjoint tails
remain.  There are at most `2h-1=O(1)` companion roles.  Hence each further
prescribed same-half occurrence costs at most `C/N_*`.  An occurrence in
the other macro half additionally fixes a header at distance `Theta(k)`;
its atom is `exp[-Omega(k)]`, which is smaller than `C/N_*`.  Sequentially
expose at most two companions.  This gives (4.5).  \(\square\)

Applying (2.5) to the distinct owner
carriers gives the regenerated product row

\[
 \boxed{
 \mathbb E d_a(A)
  \le \theta\left({\kappa\over p}\right)^{|A|-1}\ell(v(A))}
 \tag{4.8}
\]

after conditioning on the carriers being retained.

Thus the root factor does not grow.  Only the merger parameter changes to

\[
                         \kappa_p={\kappa\over p}
                         \le {d\over c}\kappa.
 \tag{4.9}
\]

This is still `exp[-Omega(d log d)]`.  The shared-mark partition expansion
only needs that exponential scale: multiplication of `kappa` by a
polynomial in `d` leaves

\[
 d^{O(1)}{a\kappa_p\over\theta}=o(d^{-C})
 \tag{4.10}
\]

for every fixed `C`.  Therefore product thinning does **not** create a
dimension-dependent root loss.  Requiring the pristine complete-orbit
value of `kappa` after thinning would be unnecessarily strong.

## 5. The exact rooted intersection polynomial

Maximum `j`-codegrees are a convenient sufficient condition for residual
concentration, but they may be stronger than this template needs.  The
exact second moment is an average over actual FIFO intersection patterns.

Fix a non-slot root `v`.  For edges `E,F` through `v`, put

\[
 m_N(E,F;v)
 =|((E\cap F)-\{v\})\cap(\mathcal L\mathbin{\dot\cup}\mathcal R)|,
 \tag{5.1}
\]

and

\[
 m_S(E,F;v)
 =|(E\cap F)\cap([k]\times[L])|.
 \tag{5.2}
\]

Define

\[
 \boxed{
 \Psi_v(p,p_s)
 ={1\over\ell(v)^2}
 \sum_{E,F\ni v}\omega_E\omega_F
 \left(p^{-m_N(E,F;v)}p_s^{-m_S(E,F;v)}-1\right).}
 \tag{5.3}
\]

Here the diagonal `E=F` is included.

### Theorem 5.1 (exact compensated variance)

Let

\[
 Y_v=\sum_{E\ni v}
 \omega_Ep^{-(N_{h(E)}-1)}p_s^{-2}
 1_{\{E\subseteq U\}}.
 \tag{5.4}
\]

Conditional on `v in U`,

\[
 \boxed{
 \mathbb E Y_v=\ell(v),
 \qquad
 {\operatorname{Var}(Y_v)\over\ell(v)^2}
       =\Psi_v(p,p_s).}
 \tag{5.5}
\]

#### Proof

The mean is (2.3).  For a pair `E,F`, the product of the two compensated
weights cancels the survival probabilities of all resources counted twice
except that every common unconditioned non-slot contributes `p^-1` and
every common slot contributes `p_s^-1`.  Subtracting the product of the
means gives exactly the summand in (5.3).  Summing over ordered pairs proves
(5.5).  \(\square\)

There is an equivalent codegree-energy formula which is often more useful
than an intersection-pattern list.  Put

\[
 z_N=p^{-1}-1,
 \qquad
 z_S=p_s^{-1}-1.
 \tag{5.6}
\]

For `i,j>=0`, not both zero, define the rooted collision energy

\[
 \mathcal E_{v;i,j}
 ={1\over\ell(v)^2}
 \sum_{\substack{Q_N\subseteq\mathcal L\dot\cup\mathcal R,\ |Q_N|=i\\
                  Q_S\subseteq[k]\times[L],\ |Q_S|=j\\
                  v\notin Q_N}}
 d_\omega(\{v\}\cup Q_N\cup Q_S)^2.
 \tag{5.7}
\]

Incompatible tuples have codegree zero, so the sum may range over all
tuples of the displayed types.

### Corollary 5.2 (exact collision-energy expansion)

One has

\[
 \boxed{
 \Psi_v(p,p_s)
   =\sum_{\substack{i,j\ge0\\i+j\ge1}}
       z_N^iz_S^j\mathcal E_{v;i,j}.}
 \tag{5.8}
\]

#### Proof

Use the two-variable binomial identity

\[
 p^{-m_N}p_s^{-m_S}-1
 =\sum_{\substack{i,j\ge0\\i+j\ge1}}
   {m_N\choose i}{m_S\choose j}z_N^iz_S^j.
 \tag{5.9}
\]

After summing over ordered pairs `E,F`, choose the `i` common non-slot
vertices and `j` common slots outside the root.  For each resulting tuple
`Q`, the sum of `omega_E omega_F` over the two edges containing it is
exactly `d_omega(Q)^2`.  This gives (5.8).  \(\square\)

Thus the minimal static input is not a maximum `Delta_j`.  It is the single
weighted inequality

\[
 \boxed{
 \sup_v\sup_{c/d\le p\le1}
 \sum_{i+j\ge1}
 (p^{-1}-1)^i(p_s^{-1}-1)^j
                  \mathcal E_{v;i,j}=O(1/d).}
 \tag{CEnergy}
\]

Only `j<=2` occurs because a doublet has two slots.  Formula `(CEnergy)`
automatically discounts a large worst-case codegree if it occurs on only a
small number of FIFO role patterns.

### Proposition 5.3 (the first overlap and every slot overlap are closed)

Assume the audited weighted pair rows

\[
 \max_{w\ne v}{d_\omega(v,w)\over\ell(v)}
       \le\delta_0=O(d/k^2)
 \tag{5.10}
\]

for non-slot `w`, and

\[
 \max_s{d_\omega(v,s)\over\ell(v)}
       \le\delta_S=O(1/(kL))
 \tag{5.11}
\]

for slots `s`.  Uniformly for `p>=c/d`,

\[
 z_N\mathcal E_{v;1,0}=O(1/d),
 \tag{5.12}
\]

and

\[
 \sum_{\substack{i\ge0,\ 1\le j\le2}}
 z_N^iz_S^j\mathcal E_{v;i,j}=o(d^{-C})
 \tag{5.13}
\]

for every fixed `C`.  Consequently `(RO)` is equivalent to proving only

\[
 \boxed{
 \sup_v\sup_{c/d\le p\le1}
 \sum_{i\ge2}(p^{-1}-1)^i\mathcal E_{v;i,0}=O(1/d).}
 \tag{RO+}
\]

#### Proof

Double counting the other non-slot roles in an edge gives

\[
 \sum_{w\ne v}d_\omega(v,w)
 \le (R_{\max}-1)\ell(v).
 \tag{5.14}
\]

Hence

\[
 \mathcal E_{v;1,0}
 \le \delta_0(R_{\max}-1)=O(d^2/k^2)=O(d^{-2}).
 \tag{5.15}
\]

Since `z_N<=d/c`, this proves (5.12).

If a tuple `Q` contains a slot `s`, then

\[
 d_\omega(Q)^2
 \le d_\omega(v,s)d_\omega(Q)
 \le\delta_S\ell(v)d_\omega(Q).
 \tag{5.16}
\]

For fixed `i,j`, another incidence double count gives

\[
 \sum_{Q_N,Q_S}d_\omega(\{v\}\cup Q_N\cup Q_S)
 \le\ell(v){R_{\max}-1\choose i}{2\choose j}.
 \tag{5.17}
\]

Therefore the left side of (5.13) is at most

\[
 \delta_S(1+z_N)^{R_{\max}-1}
             ((1+z_S)^2-1).
 \tag{5.18}
\]

At `p>=c/d`, this is

\[
 {1\over kL}\exp[O(d\log d)].
 \tag{5.19}
\]

In the central regime `log L=Theta(k)=Theta(d^2)`, so (5.19) is smaller
than every inverse power of `d`.  Equations (5.12)--(5.13) leave exactly
`(RO+)`.  \(\square\)

For the stopped pair martingale one needs the sharper average hidden by the
maximum pair bound.

### Proposition 5.4 (sharp first collision energy)

For every non-slot root `v`,

\[
 \boxed{
                         \mathcal E_{v;1,0}=O(k^{-2})
                         =O(d^{-4}).}
 \tag{FE}
\]

#### Proof

First take a same-shore partner.  For Johnson distance `ell`, let

\[
 N_\ell={t\choose\ell}{k-t\choose\ell}
 \quad\hbox{or}\quad
 N_\ell={r\choose\ell}{k-r\choose\ell}
 \tag{5.20}
\]

be its stabilizer orbit, and let `c_bar_ell` be the weighted mean number of
other roles at that distance in an edge through `v`.  Transitivity gives

\[
 \sum_{w:\operatorname{dist}(v,w)=\ell}
 {d_\omega(v,w)^2\over\ell(v)^2}
                         ={\bar c_\ell^2\over N_\ell}.
 \tag{5.21}
\]

The atomic track table has `c_bar_ell=O_h(1)`.  On one lower or owner track
there are at most two roles at a fixed distance.  For two distinct owner
tracks, if the root has level `j`, every partner level `l>=j` has distance
`d-j`, while the levels `l<j` have distinct larger distances.  The first
group has `d-j` roles but the root occupies level `j` with weighted
frequency `Theta(1/d)` in the complete orbit, so its contribution to
`c_bar_(d-j)` is `O(1)`.  There are only three copies.  The last-two fan has
constant size.  Terminal roles and the two possible `h`-types change only
the constant.

For `1<=ell<=O(d)`, the distance orbits are increasing in the central
range, and

\[
                         \sum_{\ell\ge1}{1\over N_\ell}
                         =O(k^{-2}).
 \tag{5.22}
\]

This proves `(FE)` on each same shore.  A lower/owner pair has orbit at
least `{k-t choose d}` or `{r choose d}`, so its squared contribution is
exponentially smaller by the same maximum-times-total calculation.
Cross-half pairs are `exp[-Omega(k)]` by macroscopic separation.  Summing
the three cases proves the proposition.  \(\square\)

When `p_s=p`, (5.3) reduces to

\[
 {1\over\ell(v)^2}\sum_{E,F\ni v}\omega_E\omega_F
 \left(p^{-|((E\cap F)-\{v\})|}-1\right).
 \tag{5.23}
\]

By (3.3), replacing `p_s` by `p` changes the desired separator-scale bound
by `o(d^-C)` for every fixed `C`.

The precise static target is

\[
 \boxed{
 \sup_{v}\sup_{c/d\le p\le1}
                         \Psi_v(p,p_s(p))=O(1/d).}
 \tag{RO}
\]

Analogous polynomials rooted at a pair and at a marked cluster of size at
most three are needed only for those tests, not for every arbitrary
`j`-tuple.

### 5.5 Why pair codegree alone does not prove `(RO)`

Expanding (5.23) gives factorial intersection moments.  A power hierarchy

\[
 d_\omega(Q)/\ell(v)
       \le(Cd/k^2)^{|Q|-1}
 \tag{5.24}
\]

would imply `(RO)` exactly as in the fresh lower-path calculation.  The
audited doublet theorem proves only the first step of (5.24).  Retaining one
pair from a larger intersection gives the same pair bound, not another
power, and is insufficient after multiplication by `p^-j`.

The first pattern which shows why an incremental proof must be amortized is
the last-two-owner fan.  In one `h`-macro its `2h<=6` penultimate and
terminal owners are

\[
 C_*+z_1,\ldots,C_*+z_{2h},
 \qquad |C_*|=r-1,
 \tag{5.25}
\]

with distinct `z_a`.  Already three members display the issue.  After
fixing the first owner, the ordered pair of two others has orbit size

\[
                         r(k-r)_2.
 \tag{5.26}
\]

The second owner fixes a deletion and an insertion, but once their
intersection `C_*` is known the third fixes only one further insertion.
Thus a false term-by-term assertion that every new owner costs two fresh
coordinates would fail.  Nevertheless, in the central range

\[
 {1\over r(k-r)_2}=O(d^{-6})
       =O\left((d/k^2)^2\right),
 \tag{5.27}
\]

and there are only `O(1)` terminal-role assignments because `h<=3`.
Hence this smallest near-redundant pattern pays the desired two powers
after joint, rather than sequential, exposure.  Consecutive states on one
FIFO track pay one deletion/insertion pair per gap and have only `O(d)`
relative placements.  Entry into a private queue-tail track pays an
unordered tail orbit of size `exp[Theta(d log d)]`.  Entry into the second,
Johnson-separated macro pays at least the header-distance orbit.  These
facts make `(RO)` plausible, but a complete enumeration of mixed lower,
owner, terminal-fan, and slot patterns has not yet been written.

This is a materially smaller task than proving an arbitrary full
`j`-codegree hierarchy: only the weighted sum of patterns occurring in
(5.3), and its pair/cluster-rooted analogues, is required.

The complete fan energy is in fact closed.  For `1<=s<=2h-1`, fixing an
unordered `s`-set of further fan owners after the root has stabilizer orbit
of order

\[
                         r{k-r\choose s}.
 \tag{TF1}
\]

There are only `{2h-1 choose s}=O_h(1)` such role sets in an edge.  The same
maximum-times-total calculation as in Proposition 5.3 gives

\[
 \sum_{\substack{Q\text{ consists of }s\text{ further}\\
                  \text{last-two fan owners}}}
 {d_\omega(\{v\}\cup Q)^2\over\ell(v)^2}
 \le {C_h\over r{k-r\choose s}}.
 \tag{TF2}
\]

At `p>=c/d` and `k=Theta(d^2)`, its fugacity-weighted sum is

\[
 \sum_{s=1}^{2h-1}O(d^s k^{-(s+1)})=O(d^{-3}).
 \tag{TF3}
\]

For four or more fan owners the maximum hierarchy (5.24) can indeed lose a
power of `d`; `(TF2)`--`(TF3)` show exactly why the squared average required
by `(RO+)` still gains.  Thus neither the penultimate nor terminal fan is
part of the remaining static gap.

### Proposition 5.6 (rigid same-doublet overlaps are negligible)

Use the macroscopically separated template (1.12).  Conditional on any
fixed non-slot resource in one constituent macro and on all of that macro's
header data, the other header has at least

\[
 \binom{t-O(d)}{\ell_0-O(d)}
 \binom{k-t-O(d)}{\ell_0-O(d)}
                         =\exp[\Theta(k)]
 \tag{5.28}
\]

possible images, where `ell_0=|H^1-H^2|`.  Hence the number
`D_base(v)` of physical base doublets through a fixed non-slot root obeys

\[
                         D_{\rm base}(v)\ge\exp(c k).
 \tag{5.29}
\]

The contribution to `Psi_v` from pairs of augmented edges lying over the
same physical base doublet, including pairs with different slot indices,
is

\[
 O\left({p^{-(R_{\max}-1)}\over D_{\rm base}(v)}\right)
                         =\exp[-\Omega(k)].
 \tag{5.30}
\]

uniformly for `p>=c/d`.

#### Proof

After deleting the common port pair and `O(d)` private labels, build the
second header by choosing its removed and added sides at the fixed linear
distance `ell_0`.  This gives (5.28); every such header has at least one
legal atomic completion.  A root which fixes less than the complete first
header only increases the count, proving (5.26).

Aggregate the `L^2` augmented weights over each physical base doublet.
The aggregate weights are uniform, so the sum of their squares divided by
the squared root load is `1/D_base(v)`, up to the two fixed orbit-mixture
constants.  Two augmented edges over the same base share at most
`R_max-1` resources outside the root, giving the first bound in (5.30).
Finally,

\[
 (R_{\max}-1)\log(1/p)=O(d\log d)=o(k),
 \tag{5.31}
\]

which proves the last equality.  \(\square\)

This proposition closes the apparently dangerous case in which two
different slot copies share all non-slot resources.  With only a minimally
separated header at distance `2d+1`, (5.29) would have only
`exp[O(d log d)]` scale and the constants in (5.30) would require a new
audit.  Macroscopic separation removes that unnecessary boundary.

### Proposition 5.7 (cross-half overlap is exponentially negligible)

Classify the roles of a fixed root `v` in two doublet edges `E,F`.  Relative
to either root role, every same-shore resource in the opposite macro half
has Johnson distance

\[
                         \ell_0+O(d)=\Theta(k)
 \tag{5.32}
\]

from `v`.  Consequently the normalized codegree of `v` with any specified
opposite-half resource is at most

\[
 \delta_{\rm far}
 \le {O(d)\over
   {t\choose\ell_0+O(d)}{k-t\choose\ell_0+O(d)}}
   +{O(d)\over
   {r\choose\ell_0+O(d)}{k-r\choose\ell_0+O(d)}}
 =\exp[-\Omega(k)].
 \tag{5.33}
\]

Mixed lower/owner pairs have an even smaller containment-orbit bound.
The total contribution to `(RO+)` from intersection tuples containing any
opposite-half resource is `exp[-Omega(k)]`.

#### Proof

Every resource in one atomic macro differs from its header state by only
`O(d)` coordinate exchanges.  The triangle inequality in the Johnson
metric and (1.12) give (5.32).  The stabilizer of `v` is transitive on each
distance orbit, whose sizes are the two binomial products in (5.33).  A
doublet has only `O(d)` resource roles, proving the pointwise bound.  There
are only `O(d^2)` choices for the two root roles.

If an intersection tuple `Q` contains such a resource `w`, then

\[
 d_\omega(\{v\}\cup Q)^2
 \le d_\omega(v,w)d_\omega(\{v\}\cup Q)
 \le\delta_{\rm far}\ell(v)d_\omega(\{v\}\cup Q).
 \tag{5.34}
\]

Sum the last codegree over every remaining role subset as in (5.17).  Even
after inserting every fugacity, the result is at most

\[
 O(d^2)\delta_{\rm far}p^{-(R_{\max}-1)}
 =\exp[-\Omega(k)+O(d\log d)]
 =\exp[-\Omega(k)].
 \tag{5.35}
\]

This proves the claim.  \(\square\)

After Proposition 5.7, `(RO+)` is a one-macro problem.  The macroscopic
partner half and the sharp slot mechanism no longer enter its unresolved
intersection sum.

### 5.8 A synchronized FIFO track has the required overlap moment

The pure same-track part of the enumeration can be closed exactly.  Let
two independent paths in

\[
 \mathcal Z_n(X,B)
 ={X\choose j}\times{B\choose j},\qquad0\le j\le n,
 \tag{5.36}
\]

have the same two endpoints.  Each path is given by one ordering of `X`
and one independent ordering of `B`.  Let `Z` be the number of common
internal states of the two paths.

### Lemma 5.8 (synchronized-chain overlap)

For every fixed `C_0` and `0<=z<=C_0n`,

\[
 \boxed{
                         \mathbb E(1+z)^Z=1+O_{C_0}(1/n).}
 \tag{5.37}
\]

#### Proof

Fix common internal levels

\[
 0<j_1<\cdots<j_q<n
 \tag{5.38}
\]

and let `g_1,...,g_(q+1)` be the positive successive gaps, whose sum is
`n`.  Conditional on the first ordering of `X`, a second ordering has the
same prefix sets at all these levels with probability

\[
                         {\prod_ag_a!\over n!}.
 \tag{5.39}
\]

The `B` ordering is independent, so the probability for the synchronized
state is the square of (5.39).

For `m>=1`, put

\[
 S_{n,m}=
 \sum_{\substack{g_1+\cdots+g_m=n\\g_a\ge1}}
       \left({\prod_ag_a!\over n!}\right)^2.
 \tag{5.40}
\]

We claim

\[
                         S_{n,m}\le
 {4^{m-1}\over(n)_{m-1}^2}.
 \tag{5.41}
\]

This follows by induction on `m`.  Split off `g_1=a` and apply the induction
hypothesis to the remaining composition.  With `N=n-m+1`, the required
last estimate reduces to

\[
 \sum_{a=1}^{N}a!^2(N-a+1)!^2\le4N!^2.
 \tag{5.42}
\]

The two endpoint terms total `2N!^2`; after division by `N!^2`, the
interior terms are bounded by the convergent two-sided inverse-binomial
tail and total less than two.  This proves (5.42), and hence (5.41).

Expanding `(1+z)^Z` by its common-level subsets and using (5.40)--(5.41)
gives

\[
 \mathbb E(1+z)^Z
 \le\sum_{q=0}^{n-1}{(4z)^q\over(n)_q^2}.
 \tag{5.43}
\]

For `q<=n/2`, the terms after `q=0` are bounded by a geometric series with
first term `O_C(1/n)`.  For `q>n/2`, the ratio of successive displayed
terms is monotone, so their maximum is at an endpoint of that interval.
The `q=n/2` term is exponentially small, while Stirling's bound makes the
`q=n-1` term at most

\[
                         (C_1/n)^{n-1}.
 \tag{5.44}
\]

Thus the whole tail is `o(1/n)`, proving (5.37).  \(\square\)

At the separator scale take `z=p^-1-1=O(d)` and `n=d+O(1)`.  Lemma 5.8
therefore gives exactly `1+O(1/d)` for two lower tracks or two owner tracks
once their endpoints and coordinate banks have been fixed.  A
one-coordinate Boolean chain would give only one power of (5.39), which is
not enough; the synchronized deletion/insertion product is the decisive
FIFO gain.

Lemma 5.8 does not by itself close `(RO+)`: common endpoint fibres, entry
into another copy, and partial overlaps between different tracks must still
be weighted by their tail/header orbit probabilities.  It does close the
entire internal-order contribution after those entry data are fixed.

The remaining entry cost is supplied by the private deletion/tail bank.
We first record its one-coordinate estimate.

### Lemma 5.9 (one-coordinate chain after a private split)

Let two independent Boolean maximal chains on an `n`-set have the same
endpoints, and let `Z_1` be their number of common internal states.  Then

\[
 \mathbb E(1+z)^{Z_1}
 \le\sum_{q=0}^{n-1}{(4z)^q\over(n)_q}.
 \tag{OC1}
\]

If `0<=n<=d`, `0<=z<=C_0d`, and `K>=c_0d^2`, then, for `n>=1`,

\[
 \boxed{
 {1\over{K\choose n}}\mathbb E(1+z)^{Z_1}
       \le\left({C_1\over d}\right)^n.}
 \tag{OC2}
\]

#### Proof

For prescribed common levels with positive composition gaps, one ordering
pays `prod g_a!/n!`, with no square.  The induction used in Lemma 5.8 now
gives

\[
 \sum_{g_1+\cdots+g_m=n}{\prod_ag_a!\over n!}
       \le {4^{m-1}\over(n)_{m-1}}.
 \tag{OC3}
\]

Indeed the induction reduces to
`sum_(a=1)^N a!(N-a+1)!<=4N!`.  Expanding by common-level subsets proves
`(OC1)`.

The terms in `(OC1)` have monotone successive ratio
`4z/(n-q)`.  Hence their maximum is at an endpoint, and

\[
 \mathbb E(1+z)^{Z_1}
 \le n\max\left\{1,{(4C_0d)^{n-1}\over n!}\right\}.
 \tag{OC4}
\]

Use `{K choose n}>=(K/n)^n` and `n!>=(n/e)^n`.  If the first term in the
maximum dominates, the product in `(OC2)` is at most `(C/d)^n`.  If the
second dominates, it is at most

\[
 n\left({n\over K}\right)^n
       {(4C_0d)^{n-1}\over n!}
 \le\left({C_1\over d}\right)^n,
\]

after enlarging `C_1`; here `n<=d` and `K>=c_0d^2`.  \(\square\)

### Theorem 5.10 (same-half mixed-track entry closure)

For the canonical atomic macro normal form, after removing the last-two fan
class `(TF1)`--`(TF3)`, the total mixed-track contribution to `(RO+)` is
`O(1/d)`.  For every generic same-half entry pair `v,w`,

\[
                         \Gamma_{v,w}(p)=O(1)
 \tag{MT}
\]

uniformly for `p>=c/d`.

#### Proof

Fix the roles of `v,w` in the two compared macro completions.  One macro
has one lower track and at most three owner tracks.  In the fresh normal
form they share one insertion order, while their private coordinate banks
are respectively the lower-deletion bank `A` and the queue-tail banks
`X_c`.

Designate the track pair containing the root data as the **free track**.
All of its further common states require agreement of the shared insertion
order and of its private order.  Its complete overlap moment, including
variable endpoint fibres, is `1+O(1/d)` by the fresh-path overlap theorem;
when the endpoint banks have already been exposed this is also Lemma 5.8.
Only one track is charged this shared insertion-order randomness.

Consider any additional track and one of its common states at level `a` for
which the current common data do not already determine its private split.
On the forward side of that state, `n=d-a` private labels form the suffix of
`A` or `X_c` visible in the state.  Conditional on all earlier exposed
common data, coordinate symmetry leaves at least

\[
                         {K\choose n},\qquad K\ge c_0d^2,
 \tag{MT1}
\]

possible private suffix splits; disjointness from the other constant number
of `O(d)` banks only changes `K` by `O(d)`.  Two independently weighted
macro completions can have another common state on this side only after
choosing the same split.  Conditional on that split, drop the shared
insertion-order requirement and retain only the private ordering.  This
enlarges the event to the one-coordinate chain of Lemma 5.9.  The total
forward-side factor beyond one is therefore at most `(C/d)^n`.

The backward side is identical.  Its `a` private labels lie outside the
current state and are chosen from a pool of size `Theta(d^2)`; matching
their unordered block and then their private order costs at most
`(C/d)^a`.  If a side has length zero, it contributes one.  Thus the whole
additional track contributes

\[
                         1+O(1/d)
 \tag{MT2}
\]

to the closure moment.  This argument also covers a track having only one
common state: then there is no further ordering factor.  A terminal private
singleton is either paid by the `n=1` case or belongs to the already closed
last-two fan.

Expose additional generic tracks sequentially.  Their private banks are disjoint,
so each new exposure removes only `O(d)` labels from the next
`Theta(d^2)` pool.  There are at most three additional tracks, and their
factors multiply to `O(1)`.  If the two compared completions assign `v,w`
to different role pairs, apply the same argument to each fixed assignment.
The numerator of `Gamma_(v,w)` is bilinear in the assignment masses, so
the generic assignment classes give the same constant times the square of
their total mass; level choices with a short side are already summed in
`(OC2)`, not paid again.

It remains to audit entries for which `v,w` themselves determine the
private split.

* If one is lower and the other is an owner, the complete-orbit conditional
  atom is at most
  \[
  {Cd\over{k-t\choose d}}=\exp[-\Theta(d\log d)].
  \tag{MT3}
  \]
  After the split is fixed, all private one-coordinate tracks together
  have moment at most `exp[O(d)]` by `(OC1)`; there are only constantly many
  tracks.  Thus the complete contribution of this class is
  `exp[-Theta(d log d)]`.
* Suppose two different owner tracks have an aligned entry whose private
  visible parts have size `q`.  The case `q=1` is the last-two fan.  For
  `q>=2`, the distance-orbit atom is at most
  \[
  {Cd(q!)^2\over(r)_q(k-r)_q}.
  \tag{MT4}
  \]
  The determined side has one-coordinate moment at most
  `(Ced/q)^q`, while the other side is either generic and paid by `(OC2)`
  or has a still larger distance orbit.  Including the `O(d)` possible
  level roles, the sum is at most
  \[
  Cd^2\left({Cq\over d^3}\right)^q=O(d^{-4}).
  \tag{MT5}
  \]
  Unequal levels add insertion-coordinate differences and only enlarge the
  stabilizer orbit for a fixed amount of remaining private-chain freedom.

The exceptional bounds remain `o(1/d)` after the outer fugacity `p^-1`.
For the generic class, `(MT)` and Proposition 5.3 give

\[
 {p^{-1}\over\ell(v)^2}
 \sum_wd_\omega(v,w)^2\Gamma_{v,w}(p)=O(1/d).
 \tag{MT6}
\]

Together with the already closed fan, this proves the theorem.  \(\square\)

### 5.11 Pair-rooted closure completes the static overlap row

For distinct non-slot resources `v,w` with positive codegree, put

\[
 \Gamma_{v,w}(p)
 ={1\over d_\omega(v,w)^2}
 \sum_{E,F\supseteq\{v,w\}}\omega_E\omega_F
 p^{-|((E\cap F)-\{v,w\})\cap
              (\mathcal L\dot\cup\mathcal R)|}.
 \tag{5.45}
\]

Slot intersections have already been removed by Proposition 5.3.  For a
pair `E,F` with `m>=1` common non-slots outside `v`, choose any one of them
as `w`.  Since

\[
                         p^{-m}-1\le m p^{-m},
 \tag{5.46}
\]

one obtains the exact sufficient bound

\[
 \Psi_v(p,p_s)
 \le o(d^{-C})+{p^{-1}\over\ell(v)^2}
       \sum_{w\ne v}d_\omega(v,w)^2\Gamma_{v,w}(p).
 \tag{5.47}
\]

Consequently `(RO)` follows from the **average pair-closure row**

\[
 \boxed{
 \sum_{w\ne v}d_\omega(v,w)^2\Gamma_{v,w}(p)
 \le C\sum_{w\ne v}d_\omega(v,w)^2}
 \tag{PC}
\]

uniformly for `p>=c/d`, after the exponentially negligible rigid and
cross-half classes are removed.  Proposition 5.3 then turns (5.47) into
`O(1/d)`.  Theorem 5.10 proves `(PC)` for the remaining same-half classes.

This is weaker than a maximum higher-codegree hierarchy and weaker even
than a uniform bound on every `Gamma_(v,w)`: a rare rigid pair may have a
large closure moment if its squared pair codegree is correspondingly tiny.
Lemma 5.8 proves the internal synchronized-order part of `Gamma=O(1)`.
The fan calculation `(TF1)`--`(TF3)` proves it for the last-two-owner
closure, and Lemma 5.9 plus the entry audit of Theorem 5.10 proves the
mixed-track part.  Thus `(RO)` is unconditional for the chosen
macroscopically separated atomic template.

There is no remaining single-track term.  Fix one lower track, or one of
the at most three owner tracks, in each of the two compared macro edges.
Projection of the complete macro orbit onto that track is the complete
labelled fresh Johnson-path orbit; every projected path has the same number
of private completions.  Therefore the normalized overlap polynomial for
all intersections confined to this track pair is exactly the fresh-path
polynomial.  The all-order fresh-path theorem gives

\[
 \left(1+{Cd\over k^2}(p^{-1}-1)\right)^{d+O(1)}-1
                         =O(1/d).
 \tag{5.48}
\]

There are only `O_h(1)` choices of lower/owner track pair.  Thus (5.48)
closes their union.  The phrase "a second track first becomes common" in
`(PC)` describes the last class closed by Theorem 5.10.

The dynamic square calculation below needs one finite three-edge
corollary.  It is useful to record it before introducing the process.  Fix
`p_*=c/d`.  For a pair root `Q={v,w}` and `E,F` containing `Q`, put

\[
 m(E,F;Q)=|((E\cap F)-Q)\cap(\mathcal L\dot\cup\mathcal R)|,
 \qquad
 j(G;E,F)=|G\cap(E\cup F)\cap(\mathcal L\dot\cup\mathcal R)|,
 \tag{FE3.1}
\]

and, for `j>=2`,

\[
 K_{p_*}(j)=\int_{p_*}^1p^{2-j}\,dp.
 \tag{FE3.2}
\]

Terms with `j<2` are zero.  Define the first-two-hit energy

\[
 \mathcal F_3(p_*)=
 \sum_{Q}\sum_{E,F\supseteq Q}\sum_G
 \omega_E\omega_F\omega_Gp_*^{-m(E,F;Q)}
 {j(G;E,F)\choose2}K_{p_*}(j(G;E,F)).
 \tag{FE3.3}
\]

As elsewhere, the displayed formula is the non-slot part; inserting the
separate slot fugacity gives an exponentially smaller addition.

### Proposition 5.12 (first-two-hit closure)

For the macroscopically separated complete atomic orbit,

\[
 \boxed{
                         \mathcal F_3(p_*)
 \le \left({C\over d}+o(d^{-C_0})\right)\mathcal S_2(p_*),}
 \tag{FE3}
\]

for every fixed `C_0`, where `S_2` is defined in (SM6) below.  Thus the multi-hit correction in
the aggregate pair-energy drift has one spare factor `1/d`.

#### Proof

Expand the binomial coefficient in (FE3.3) by choosing the first two
distinct hit resources `x,y` of `G` in `E union F`.  There are `O(d^2)`
role pairs.  The complete-orbit pair row charges the event
`{x,y} subseteq G` by

\[
                         d_\omega(x,y)=O(d^{-3}),
 \tag{FE3.4}
\]

so the total first-entry cost is `O(1/d)`.

It remains to sum further intersections of `G` with `E union F`, after
`x,y` and their roles have been fixed.  For `z=p_*^{-1}-1=O(d)`,

\[
 K_{p_*}(j)\le C(1+z)^{j-2}
 \qquad(j\ge2).
 \tag{FE3.5}
\]

Expose the track containing the first anchor as the free track.  Further
states on it have the synchronized-chain moment of Lemma 5.8.  On the
first entry into any track of either `E` or `F` not yet exposed, the
private visible block is chosen from a `Theta(d^2)` pool; Lemma 5.9 and
the forward/backward split argument `(MT1)`--`(MT2)` give a factor
`1+O(1/d)`.  There are at most eight fixed lower/owner tracks in
`E union F`, so these factors remain bounded.  This exposure permits fewer
choices than the two-completion calculation in Theorem 5.10 only by
deleting `O(d)` labels from each pool, which leaves every pool at
`Theta(d^2)`.

If the two anchors already determine a private split, the lower/owner
class pays `(MT3)`, the owner/owner class with visible size at least two
pays `(MT4)`--`(MT5)`, and visible size one is the fan `(TF1)`--`(TF3)`.
Rigid same-base and cross-half entries are exponentially small by
Propositions 5.6--5.7.  Hence the conditional sum after the first two
anchors is `O(1)`.  Multiplying by (FE3.4), summing the `O(d^2)` anchor
roles, and then summing the already weighted pair `E,F` gives
`(C/d)S_2(p_*)`.  The slot classes use (5.16)--(5.19) and give the stated
remainder.  \(\square\)

### Corollary 5.13 (separator-constant gain)

The proof of `(RO)` in fact gives the quantitative form

\[
 \boxed{
 \sup_v\Psi_v(p,p_s(p))
 \le {C\over p d^2}+o(d^{-C_0})
 \qquad(c/d\le p\le1),}
 \tag{ROc}
\]

for every fixed `C_0`.  In particular, at `p=c/d` the root variance scale
is `O(1/(cd))`.

#### Proof

The single-track term (5.48), which is the largest class, is

\[
 \left(1+{Cd\over k^2}(p^{-1}-1)\right)^{d+O(1)}-1
                         =O(1/(pd^2))
 \tag{FE3.6}
\]

because `k=Theta(d^2)`.  Proposition 5.4 makes the first and mixed-entry
terms `O(1/(pd^4))`; `(TF2)` gives the same or smaller scale for the fan.
Rigid, cross-half, and slot classes are smaller than every inverse power.
Summing the constant number of track/role classes proves `(ROc)`.
\(\square\)

## 6. The rank-compensated exponential-clock process

Set

\[
 p_i=1-{2di\over M},
 \qquad
 p_{s,i}=1-\sigma(1-p_i).
 \tag{6.1}
\]

At step `i`, for every doublet edge whose resources are unused, use the rate

\[
 a_E(i)=\omega_Ep_i^{-(N_{h(E)}-1)}p_{s,i}^{-2}.
 \tag{6.2}
\]

Accept the first exponential clock, consume the whole balanced doublet,
and repeat until `p_i<=c/d`.  Every exposure is automatically
doublet-closed.  Opposite-orientation coins are left unexposed until after
the unordered packing.

For a live non-slot `v`, define its compensated load

\[
 Y_v(i)=\sum_{E\ni v,\ E\text{ available}}a_E(i),
 \tag{6.3}
\]

and define `Y_Q(i)` and `Y_A(i)` analogously for resource tuples and marked
clusters.

### Proposition 6.1 (exact main-term drift cancellation)

Suppose at one state that

\[
 Y_w(i)=1+o(1)\quad\hbox{on the non-slot resources relevant to the test},
 \qquad
 X(i):=\sum_Ea_E(i)=(1+o(1)){p_iM\over2d}.
 \tag{6.4}
\]

For one summand `a_E(i)` of a live root load, the deterministic increase
caused by replacing `p_i` with `p_(i+1)` has main term

\[
 (N_{h(E)}-1){2d\over Mp_i}a_E(i).
 \tag{6.5}
\]

Its expected collision loss has main term

\[
 {a_E(i)\over X(i)}
       \sum_{w\in E-\{v\}}Y_w(i)
 =(1+o(1))(N_{h(E)}-1){2d\over Mp_i}a_E(i),
 \tag{6.6}
\]

apart from the two-slot ceiling correction and multiple-intersection
inclusion--exclusion terms.  Hence (6.5) and (6.6) cancel separately for
each edge rank `h`.

#### Proof

The logarithmic derivative of `p^(-(N_h-1))` is
`-(N_h-1)dp/p`, and `p_i-p_(i+1)=2d/M`, which gives (6.5).
An accepted edge kills the summand precisely when it meets one of its other
resources.  Summing the clock rates over each possible meeting resource
gives the numerator in (6.6); intersections in two or more resources are
the stated inclusion--exclusion correction.  Substitute (6.4).  The slot
factor has its own deterministic density (3.2), so its two terms cancel
with `Y_s=sigma p/p_s`; the difference from replacing them by non-slot
terms is bounded by (3.3).  \(\square\)

The proposition is an identity of leading terms, not a concentration
theorem.  It shows exactly what must be controlled: rooted overlap patterns
price the multiple-intersection correction and the predictable quadratic
variation.

The same cancellation has a useful rank-rooted form.  If `Q` consists of
`q` live non-slot resources, put

\[
                         H_Q(i)=p_i^{q-1}Y_Q(i).
 \tag{6.7}
\]

### Proposition 6.2 (the compensated `q`-root process)

For a summand belonging to an `h`-doublet,

\[
 p^{q-1}a_E=\omega_Ep^{-(N_h-q)}p_s^{-2}.
 \tag{6.8}
\]

Consequently its deterministic one-step relative increase has main term

\[
 (N_h-q){2d\over Mp}+2\sigma{2d\over Mp_s}.
 \tag{6.9}
\]

On a state satisfying the ideal rows in (6.4), its collision loss through
the `N_h-q` non-slot resources outside `Q` and its two slots has the same
main term.  Thus `H_Q`, rather than `Y_Q`, is the approximately drift-free
quantity.  In particular,

\[
                         H_v=Y_v,
 \qquad                  H_{v,w}=pY_{v,w}.
 \tag{6.10}
\]

#### Proof

Equation (6.8) is immediate from (6.2).  Its logarithmic derivative gives
the first term in (6.9); since `p_s` decreases by `sigma 2d/M` per step,
the two slot factors give the second.  An edge through `Q` has exactly
`N_h-q` other non-slots.  Their ideal hit loads divided by
`X=pM/(2d)` give the first term of (6.9).  Each slot has ideal load
`sigma p/p_s`, so its load divided by `X` is `sigma 2d/(Mp_s)`; there are
two.  Multiple hits, deviations of the current loads and total rate, and
the distinction between a raw and a `Q`-avoiding transition are precisely
the drift-error terms which a stopped tracking lemma must bound.  \(\square\)

There is also an exact way to reconstruct the global rate from local lower
loads.  Write

\[
 Y_v^{(h)}(i)=\sum_{\substack{E\ni v,\ E\in B_h\\E\ {\rm available}}}a_E(i),
 \qquad
 X_h(i)=\sum_{\substack{E\in B_h\\E\ {\rm available}}}a_E(i).
 \tag{6.11}
\]

### Proposition 6.3 (aggregate root tracking prevents a global stall)

At every raw state after `i` accepted doublets,

\[
 \boxed{
 2dX_h(i)=\sum_{v\in\mathcal L_i}Y_v^{(h)}(i),
 \qquad |\mathcal L_i|=p_iM.}
 \tag{6.12}
\]

Consequently, if up to `p_i>=p_*=c/d`

\[
 \mathcal R_h:=
 \sum_{v\in\mathcal L}
  \sup_{j<\tau_v\wedge T}
       |Y_v^{(h)}(j)-\lambda_h|^2
                         \le {C_LM\over d},
 \tag{6.13}
\]

then uniformly over those states

\[
 \left|X_h(i)-{\lambda_hp_iM\over2d}\right|
 \le {\sqrt{p_iM\mathcal R_h}\over2d}
 \le \sqrt{C_L/c}\,{p_iM\over2d}.
 \tag{6.14}
\]

In particular, orbit-resolved stopped root estimates
`E R_h=O(M/d)` imply, after choosing the absolute separator constant `c`
large enough and applying Markov's inequality, a positive-probability event
on which the total rate never vanishes and every orbit with
`lambda_h` bounded below retains a fixed positive share of its ideal rate.

#### Proof

Every available `h`-edge contains exactly `2d` live lowers, so double
counting its rate proves the first identity in (6.12).  Every accepted
doublet consumes exactly `2d` lowers, proving the second.  Subtract
`lambda_h` from every summand in (6.12) and apply Cauchy--Schwarz over the
`p_iM` live lower vertices.  Since `p_id>=c`, this gives (6.14).
For the probabilistic statement, stop provisionally at the first violation
of the desired global lower bound.  On the event (6.13) holds with a
sufficiently large fixed Markov constant, (6.14) contradicts such a first
violation.  This is the usual stopped bootstrap and does not assume global
positivity beyond the stopping time.  \(\square\)

## 7. Analytical bad roots and the stopped cylinder

A uniform degree statement over all `M=exp[Theta(d^2)]` resources is neither
needed nor supported by the elementary second moment.  The proved row
`(RO)` has fixed-root variance scale `O(1/d)`, which is enough for an
aggregate charged bad set but not for a union bound over the entire layer.

For a non-slot carrier `v`, define its **local bad time** to be the first
pre-hit state at which any required test fails, for example

\[
 Y_v\notin[c_0,C_0],
 \tag{7.1}
\]

or

\[
 {Y_{v,w}\over\min(Y_v,Y_w)}>{\gamma\over d},
 \tag{7.2}
\]

or, for a tested marked cluster `A` rooted at `v`,

\[
 {Y_A\over Y_v}>
 C_1\theta\left({\kappa\over p_i}\right)^{|A|-1}.
 \tag{7.3}
\]

This stopping is analytical: it does not delete `v`, suppress clocks, or
alter the process.  A marked occurrence is retained only if its carrier is
served before its local bad time.  After the run, delete every selected
doublet touching an analytically bad marked/root occurrence.  Because the
selected doublets form a matching, this costs at most one doublet per
charged occurrence.

For the pair row, one need not maximize (7.2) over all never-selected
partners.  Run the raw clock unchanged and, afterward, form a graph on the
selected doublets.  Join two of them if their two tested carriers violated
(7.2) at any time while both were live and before the earlier carrier was
hit.  Mark a selected doublet if one of its finitely many compatible
clusters of size at most three violated (7.3) while its root was live.
Delete every marked doublet and both endpoints of every bad relation.

For a fixed proposed cylinder, any raw history on which one of its required
rows fails has continuation payoff zero: if the roots are later selected,
the post-run rule deletes at least one of them.  At every history with
nonzero payoff the raw cause-rate bounds apply.  The first-hit induction is
therefore a **killed-event induction** on the raw filtration; it does not
condition the next clock on future quarantine survival.  It is enough to
prove the averaged cleanup estimate

\[
 \mathbb E(B_0+B_1)=O(M/d^2),
 \tag{SR}
\]

where `B_0` is the number of individually bad selected doublets and `B_1`
the number of bad selected relations.  Deleting all indicated endpoints
then loses `O(M/d)` lower resources in expectation.  A little-oh estimate
would give separator slack but is not required.  The squared
selected-pair average in `(SR)` is aligned with `(PC)`; no union bound over
all potential partners occurs.

The exact dynamic scale behind `(SR)` is most cleanly stated before
conditioning on selection.  This avoids a Palm-size-bias issue.  Let
`beta_v` be the individual degree/cluster bad time of `v`, let `tau_v` be
its first raw hit, and put

\[
 \tau^g_{v,w}=\tau_v\wedge\tau_w\wedge\beta_v\wedge\beta_w,
 \qquad
 Z^g_{v,w}=\sup_{t<\tau^g_{v,w}}
 \left({Y_{v,w}(t)\over\min\{Y_v(t),Y_w(t)\}}\right)^2.
 \tag{SM1}
\]

The superscript is essential.  Once either load is individually bad, its
eventual selected block is charged to `B_0`; no relation estimate should
divide by that bad load.  The aggregate stopped square-energy target is

\[
 \boxed{
 \mathbb E\sum_{\{v,w\}\in\mathcal P}Z^g_{v,w}
                         =O(M/d^2),}
 \tag{ASE}
\]

where `P` is the set of compatible owner-carrier pairs which could occur
in distinct selected blocks.  The corresponding individual target is

\[
 \boxed{
 \mathbb E\sum_v1_{\{\beta_v<\tau_v\}}=O(M/d).}
 \tag{AIB}
\]

### Proposition 7.1 (two first-hit hazards give separator cleanup)

Suppose `(ASE)` and `(AIB)` hold and, after every allowed raw history, the
rate which first-hits a live owner carrier `v` in one of its marked roles is
at most

\[
                         \eta_mY_v,
 \qquad                  \eta_m\le {C_m\over d}.
 \tag{SM2}
\]

For relation threshold `delta=gamma/d`,

\[
                         \mathbb E(B_0+B_1)=O(M/d^2).
 \tag{SM3}
\]

#### Proof

If `v` becomes individually bad before its first hit, then, conditional on
its entire pre-hit path, the probability that its first hit is in a marked
role is at most `eta_m` by competing risks.  Therefore

\[
                         \mathbb E B_0
 \le \eta_m\mathbb E\sum_v1_{\{\beta_v<\tau_v\}}
                         =O(M/d^2).
 \tag{SM4}
\]

Now fix an unordered compatible pair `{v,w}`.  A bad selected relation
requires `Z^g_(v,w)>delta^2` and two distinct marked first-hit causes.  At
the first hit of `{v,w}`, an edge containing both carriers creates one
selected block and contributes zero.  The useful marked cause-rate is at
most `eta_m(Y_v+Y_w)`, while the union hit-rate is
`Y_v+Y_w-Y_(v,w)>=max{Y_v,Y_w}`.  Thus the first useful marked cause has
conditional probability at most `2eta_m`.  After it occurs, the other
carrier is still live, and its later marked first-hit probability before
its individual bad time is at most `eta_m`.  If that bad time comes first,
the eventual block is already charged to `B_0`.  Applying the adaptive
first-hit lemma twice, after stopping at the first threshold crossing,
gives

\[
 \Pr(\{v,w\}\hbox{ is a bad selected relation})
 \le 2\eta_m^2\Pr(Z^g_{v,w}>\delta^2)
 \le {2\eta_m^2\over\delta^2}\mathbb EZ^g_{v,w}.
 \tag{SM5}
\]

Sum over `P` and use `(ASE)`.  Since
`eta_m^2 delta^-2=O(1)`, this gives `E B_1=O(M/d^2)` and proves (SM3).
\(\square\)

The marked-hazard row `(SM2)` is the sum over the pointed root rows: in the
complete factor it is exactly `1/(d+1)`, and the stopped cluster test only
needs to preserve it within a fixed factor.  The two factors in `(SM5)` are
the selection probabilities of the two endpoints.  This is why the
unselected aggregate energy `(ASE)`, rather than a conditional law of a
"uniform selected root", is the proof-safe target.

Static `(PC)` gives exactly the correct budget for `(ASE)`.  For owner
carriers define, with `D_(v,w)=d_omega(v,w)`,

\[
 \mathcal S_2(p)=
 \sum_v\sum_{w\ne v}D_{v,w}^2\Gamma_{v,w}(p).
 \tag{SM6}
\]

By `(PC)` and Proposition 5.4,

\[
 \boxed{\mathcal S_2(p)=O(M/d^4)}
 \qquad(c/d\le p\le1).
 \tag{SM7}
\]

In an independent product residual, `H_(v,w)=pY_(v,w)` satisfies the exact
identity

\[
 \mathbb E[H_{v,w}^2\mid v,w\hbox{ live}]
                         =D_{v,w}^2\Gamma_{v,w}(p),
 \tag{SM8}
\]

up to the already negligible slot terms.  Thus `(SM7)` is not merely
dimensionally suggestive: it is the exact terminal product-residual second
moment which the raw greedy dynamics must transfer to a stopped maximal
bound.

### Lemma 7.2 (generic stopped maximal transfer)

Let `H_alpha(t)` be finitely many square-integrable stopped processes with
Doob decompositions

\[
                         H_\alpha(t)=H_\alpha(0)
                                      +M_\alpha(t)+A_\alpha(t),
 \tag{SM9}
\]

where `M_alpha(0)=A_alpha(0)=0`, `M_alpha` is a martingale, and `A_alpha`
is predictable.  If

\[
 \sum_\alpha H_\alpha(0)^2
 +\sum_\alpha\mathbb E\langle M_\alpha\rangle_T
 +\sum_\alpha\mathbb E\sup_{t\le T}|A_\alpha(t)|^2
                         \le C\mathcal S,
 \tag{SM10}
\]

then

\[
 \boxed{
 \mathbb E\sum_\alpha\sup_{t\le T}|H_\alpha(t)|^2
                         \le C'\mathcal S.}
 \tag{SM11}
\]

#### Proof

Use `|x+y+z|^2<=3(x^2+y^2+z^2)`, sum over `alpha`, and apply Doob's
`L^2` inequality followed by
`E M_alpha(T)^2=E <M_alpha>_T`.  One may take `C'=12C`.  \(\square\)

Apply the lemma to the hit-killed pair processes

\[
 H_{v,w}(i)=p_iY_{v,w}(i)
 1_{\{i<\tau_v\wedge\tau_w\wedge\beta_v\wedge\beta_w\}}.
 \tag{SM12}
\]

Thus the pair process is killed, rather than frozen, at its first hit or
individual bad time.  Its maximum is exactly its good pre-hit maximum.
The killed convention uses no conditioning on future avoidance; an
analytical bad transition only adds an extra nonpositive term to the
future-potential drift below.

Because `Y_v,Y_w>=c_0` before `tau^g_(v,w)` and
`p_i>=p_*=c/d`,

\[
 \sum_{\{v,w\}\in\mathcal P}Z^g_{v,w}
 \le {p_*^{-2}\over c_0^2}
       \sum_{\{v,w\}\in\mathcal P}
       \sup_{i<\tau^g_{v,w}}H_{v,w}(i)^2.
 \tag{SM13}
\]

Consequently `(ASE)` follows from the single dynamic estimate

\[
 \boxed{
 \sum_{v,w}\mathbb E\langle M_{v,w}\rangle_T
 +\sum_{v,w}\mathbb E\sup_{i\le T}|A_{v,w}(i)|^2
                         =O(\mathcal S_2(p_*)),}
 \tag{DPAIR}
\]

because `sum D_(v,w)^2<=S_2(p_*)`, (SM7), (SM11), and
`p_*^-2=O(d^2)` give (ASE).  This freezes the exact pair-tracking target:
the predictable drift and quadratic variation of `pY_(v,w)` may spend only
a constant multiple of the static pair-rooted second-moment budget.

For reference, this target has a completely explicit one-step form.  At a
good pre-transition state set

\[
 \xi_{E,i}=p_i a_E(i),\qquad
 r_{E,i}=\left({p_i\over p_{i+1}}\right)^{N_{h(E)}-2}
          \left({p_{s,i}\over p_{s,i+1}}\right)^2.
 \tag{SM14}
\]

For a proposed selected edge `G`, let `chi_Q(G)` indicate that `G` misses
both roots and the resulting state is still before both individual bad
times.  The good-killed increment is exactly

\[
 \Delta_{v,w}(G;i)=
 \chi_Q(G)\sum_{\substack{E\supseteq\{v,w\}\\E\cap G=\varnothing}}
       r_{E,i}\xi_{E,i}
       -\sum_{E\supseteq\{v,w\}}\xi_{E,i}
 \tag{SM15}
\]

Since `G` is chosen with probability `a_G(i)/X(i)`, put

\[
 \mu_{v,w}(i)={1\over X(i)}\sum_Ga_G(i)\Delta_{v,w}(G;i),
 \qquad
 V_{v,w}(i)={1\over X(i)}\sum_Ga_G(i)\Delta_{v,w}(G;i)^2.
 \tag{SM16}
\]

The Doob decomposition has drift increments `mu_(v,w)(i)` and conditional
quadratic variation at most `V_(v,w)(i)`.  Therefore the two concrete rows

\[
 \sum_{v,w}\mathbb E\sum_{i<T}V_{v,w}(i)=O(\mathcal S_2(p_*)),
 \qquad
 \sum_{v,w}\mathbb E
   \sup_{j\le T}\left|\sum_{i<j}\mu_{v,w}(i)\right|^2
                         =O(\mathcal S_2(p_*))
 \tag{QPAIR}
\]

imply `(DPAIR)` verbatim.  Equations `(SM14)`--`(SM16)` also locate the
remaining difficulty: `(PC)` prices the intersection patterns inside the
square in `(SM15)`, while control of `1/X(i)` and of the accumulated drift
uses the actual greedy history.  The static product law alone does not
establish `(QPAIR)`.

Estimating `V_(v,w)(i)` separately at every step would introduce a false
`log d` accumulation.  The correct object is a future-overlap potential.
For `Q={v,w}` and available `E,F` containing `Q`, set

\[
 \begin{aligned}
 m_N(E,F;Q)&=|((E\cap F)-Q)\cap
                    (\mathcal L\dot\cup\mathcal R)|,\\
 m_S(E,F)&=|(E\cap F)\cap([k]\times[L])|,\\
 u_N(E,F;Q)&=|((E\cup F)-Q)\cap
                    (\mathcal L\dot\cup\mathcal R)|,\\
 u_S(E,F)&=|(E\cup F)\cap([k]\times[L])|.
 \end{aligned}
 \tag{FP1}
\]

Define

\[
 \mathcal P_i=
 \sum_{Q\ {\rm good\ and\ live}}\sum_{E,F\supseteq Q}
 \xi_{E,i}\xi_{F,i}
 \left({p_i\over p_*}\right)^{m_N(E,F;Q)}
 \left({p_{s,i}\over p_{s,*}}\right)^{m_S(E,F)}.
 \tag{FP2}
\]

### Proposition 7.3 (exact future-overlap drift)

At time zero and at every later state,

\[
 \boxed{
 \mathcal P_0\le\left(1+o(d^{-C_0})\right)\mathcal S_2(p_*),
 \qquad
 \sum_QH_Q(i)^2\le\mathcal P_i.}
 \tag{FP3}
\]

Here `C_0` is arbitrary; the negligible discrepancy is exactly the slot
part suppressed in Proposition 5.3.  If `S_2` is restricted to `P` and its
slot part is included, the first inequality is an equality.

Put `rho_i=p_(i+1)/p_i`, `rho_(s,i)=p_(s,i+1)/p_(s,i)`, and

\[
 R_i(E,F;Q)=\rho_i^{-u_N(E,F;Q)}
             \rho_{s,i}^{-u_S(E,F)},
 \qquad
 q_i(E,F;Q)=1-\rho_i^{u_N(E,F;Q)+2}
                 \rho_{s,i}^{u_S(E,F)}.
 \tag{FP4}
\]

For a resource set `U`, let
`Lambda_i(U)=sum_(G:G cap U ne empty)a_G(i)`.  If
`c_i(Q,E,F)` denotes the summand of (FP2), then the exact conditional drift
for the raw hit-killed potential, and an upper bound for the good-killed
potential, is

\[
 \boxed{
 \begin{aligned}
 \mathbb E(\mathcal P_{i+1}-\mathcal P_i\mid\mathcal F_i)
  \le{}&(\rho_i^2-1)\mathcal P_i\\
    &+\sum_{Q,E,F}c_i(Q,E,F)R_i(E,F;Q)
       \left(q_i(E,F;Q)-{\Lambda_i(E\cup F)\over X(i)}\right).
 \end{aligned}}
 \tag{FP5}
\]

#### Proof

The first identity in (FP3) is (SM8) summed over pair roots at `p_*`; the
second holds because both future-fugacity factors in (FP2) are at least
one.  In the raw hit-killed process, if the selected edge is `G`, a
cross-term indexed by `Q,E,F` survives precisely when `G` misses
`E union F`.  In the good-killed process it may additionally disappear
when an individual test fails, which only lowers the next potential.  Its
two rate factors scale by `r_Er_F`.  The elementary counts

\[
 (N_E-2)+(N_F-2)=u_N+m_N,
 \qquad                         4=u_S+m_S
 \tag{FP6}
\]

show that rate scaling times the change in the future-fugacity weight is
exactly `R_i`.  The chance that `G` misses `E union F` is
`1-Lambda_i(E union F)/X(i)`.  Finally,

\[
 R_i\left(1-{\Lambda_i(E\cup F)\over X(i)}\right)-1
 =(\rho_i^2-1)+R_i
   \left(q_i-{\Lambda_i(E\cup F)\over X(i)}\right),
 \tag{FP7}
\]

because `R_i(1-q_i)=rho_i^2`.  Summation proves (FP5).  \(\square\)

Formula (FP5) separates the useful two-root killing drift from one hazard
defect.  Put

\[
 \alpha_N(i)=X(i)(1-\rho_i),
 \qquad
 \alpha_S(i)=X(i)(1-\rho_{s,i}).
 \tag{FP8}
\]

The union bound for the product expression in `q_i`, followed by the first
Bonferroni lower bound for the actual hit rate, gives the exact inequality

\[
 \begin{aligned}
 X(i)q_i-\Lambda_i(E\cup F)
 \le{}&\sum_{x\in(E\cup F)\cap(\mathcal L\dot\cup\mathcal R)}
                   (\alpha_N(i)-Y_x(i))\\
 &+\sum_{s\in(E\cup F)\cap([k]\times[L])}
                   (\alpha_S(i)-Y_s(i))
   +\sum_{\{x,y\}\subseteq E\cup F}Y_{x,y}(i).
 \end{aligned}
 \tag{FP9}
\]

The last line is precisely the dynamic three-edge first-two-hit term.
Under product thinning, summing it over time against the coefficients in
(FP5) produces the kernel `K_(p_*)(j)` in (FE3.2): after the `E,F` future
weight is inserted, a deleting edge meeting `E union F` in `j` non-slot
resources contributes `p^(2-j)dp`.  Proposition 5.12 therefore proves that
the **static** cumulative multi-hit budget is only
`O(S_2(p_*)/d)`.

The two first-order lines of (FP9) have an exact signed decomposition.  For
a resource type `T`, define its potential-incidence weight

\[
 g_x(i)=\sum_{\substack{Q,E,F\\x\in E\cup F}}c_i(Q,E,F)R_i(E,F;Q),
 \qquad
 \bar g_T={1\over|T_i|}\sum_{x\in T_i}g_x,
 \qquad
 \bar Y_T={1\over|T_i|}\sum_{x\in T_i}Y_x.
 \tag{FP12}
\]

Then

\[
 \boxed{
 \sum_{x\in T_i}(\alpha_T-Y_x)g_x
 =(\alpha_T-\bar Y_T)\sum_{x\in T_i}g_x
  -\sum_{x\in T_i}(Y_x-\bar Y_T)(g_x-\bar g_T).}
 \tag{FP13}
\]

For live lowers the parallel term vanishes identically, because

\[
 \bar Y_{\mathcal L}={2dX\over p_iM}
                         =X(1-\rho_i)=\alpha_N.
 \tag{FP14}
\]

It also vanishes identically for live slots:

\[
 \bar Y_{\mathcal S}={2X\over p_{s,i}kL}
 =X(1-\rho_{s,i})=\alpha_S,
 \tag{FP15}
\]

where `sigma 2d/M=2/(kL)`.  On the owner shore the parallel term is exactly
the orbit-mixture/owner-ledger error, since

\[
 \bar Y_{\mathcal R}
 ={2(d+1)(2X_2+3X_3)\over|\mathcal R_i|}.
 \tag{FP16}
\]

Thus no unsigned sum of all root deviations is required.  Only the
orthogonal covariance in (FP13) remains.  With

\[
 \mathcal R_T(i)=\sum_{x\in T_i}(Y_x-\bar Y_T)^2,
 \qquad
 \mathcal I_T(i)=\sum_{x\in T_i}(g_x-\bar g_T)^2,
 \tag{FP17}
\]

Young's inequality gives, for every `a>0`,

\[
 -\sum_{x\in T_i}(Y_x-\bar Y_T)(g_x-\bar g_T)
 \le {a\over2}\mathcal R_T(i)+{1\over2a}\mathcal I_T(i).
 \tag{FP18}
\]

There is a stronger size-biased form.  On the good interval put

\[
 b_x={g_x\over Y_x},qquad
 \bar b_T={1\over|T_i|}\sum_{x\in T_i}b_x,qquad
 \mathcal J_T(i)=\sum_{x\in T_i}(b_x-\bar b_T)^2.
 \tag{FP18a}
\]

When `alpha_T=bar Y_T`, as holds exactly for lowers and slots,

\[
 \boxed{
 \sum_{x\in T_i}(\alpha_T-Y_x)g_x
 =-\bar b_T\mathcal R_T
  -\sum_{x\in T_i}(b_x-\bar b_T)Y_x(Y_x-\bar Y_T).}
 \tag{FP18b}
\]

Thus incidence size-bias makes root variance helpful.  If
`c_0<=Y_x<=C_0`, Cauchy--Schwarz and Young give

\[
 \sum_{x\in T_i}(\alpha_T-Y_x)g_x
 \le- {\bar b_T\over2}\mathcal R_T
       +{C_0^2\over2\bar b_T}\mathcal J_T,
 \tag{FP18c}
\]

with the right side interpreted as zero when `bar b_T=0` (then every
`g_x=0`).  For owners, add the parallel ledger term
`(alpha_N-bar Y_R)sum_xg_x` from (FP13).

The matching root energy has the needed opposite sign.  For an orbit
component `h`, put

\[
 \mathcal R_h^{\rm root}(i)=
 \sum_{v\in\mathcal L_i}(Y_v^{(h)}(i)-\lambda_h)^2.
 \tag{FP19}
\]

The part of its one-step drift caused solely by removal of the `2d` lower
roots in the selected edge is exactly

\[
 -{1\over X(i)}\sum_{v\in\mathcal L_i}
       Y_v(i)(Y_v^{(h)}(i)-\lambda_h)^2.
 \tag{FP20}
\]

Before the individual lower-load stop this is at most
`-c_0 R_h^(root)/X`.  Deterministic rescaling and collisions of unhit roots
have the main cancellation of Proposition 6.2; their square injection is
the summed rooted-overlap budget.  Equations (FP18)--(FP20) identify the
joint Lyapunov route: add a suitable multiple of the orbit-resolved root
energy to `P_i`, absorb the `R_T` part of (FP18) by (FP20), and charge the
incidence-spread part `I_T` by the same first-entry enumeration as `(FE3)`.

Precisely, after separately charging the owner parallel term in (FP16), a
natural gradient/Dirichlet target is

\[
 \boxed{
 \mathbb E\sum_{i<T}{1\over X(i)}
 \sum_T{\mathcal J_T(i)\over\bar b_T(i)}
                         =O(\mathcal S_2(p_*)),}
 \tag{GDIR}
\]

together with root-noise injection `O(M/d)`.  The complete orbit has
`J_T(0)=0` by transitivity.  Expanding `J_T` produces two pair-potential
terms sharing their first incidence resource `x`; after that common entry
is exposed, the remaining overlap is exactly the `(FE3)` private-split
geometry.  Proving that this dynamic Dirichlet creation is paid by the
first-two-entry energy is the remaining incidence-spread step; it is
strictly weaker than uniform control of every root.  The coarser covariance
demand follows from `(GDIR)` and (FP18c), so it need not be assumed
separately.

This yields a sharper dynamic target than a stepwise variance sum.  It is
enough to prove the cumulative positive-defect transfer

\[
 \mathbb E\sum_{i<T}{1\over X(i)}
 \sum_{Q,E,F}c_iR_i
       [X(i)q_i-\Lambda_i(E\cup F)]_+
                         =O(\mathcal S_2(p_*)),
 \tag{FDEF}
\]

with the multi-hit part charged to `(FE3)` and the first two lines of
(FP9) charged to the orbit-resolved root self-correction.  Then (FP5)
telescopes and gives

\[
                         \mathbb E\sum_QH_Q(T)^2
                         =O(\mathcal S_2(p_*)).
 \tag{FP10}
\]

Finally, there is an exact aggregate square identity

\[
 \mathbb E(S_{i+1}-S_i\mid\mathcal F_i)
 =2\sum_QH_Q(i)\mu_Q(i)+\sum_QV_Q(i),
 \qquad S_i=\sum_QH_Q(i)^2.
 \tag{FP11}
\]

Hence `(FP10)` upgrades to the quadratic-variation half of `(QPAIR)` once

\[
 \mathbb E\sum_{i<T}
   \left[-\sum_QH_Q(i)\mu_Q(i)\right]_+
                         =O(\mathcal S_2(p_*))
 \tag{FDRIFT1}
\]

is proved.  The remaining drift half is exactly

\[
 \sum_Q\mathbb E\sup_{j\le T}
       \left|\sum_{i<j}\mu_Q(i)\right|^2
                         =O(\mathcal S_2(p_*)).
 \tag{FDRIFT2}
\]

The negative term `(rho_i^2-1)P_i` in (FP5) is the two-root service
compensator which should pay `(FDRIFT1)`--`(FDRIFT2)`; root-load
self-correction controls its error.  Thus the stopped pair problem is now
reduced to `(FDEF)` and the two drift rows, with the entire raw overlap
cost prepaid by `(PC)` and `(FE3)`.  No `Theta(log d)` envelope is present.

The service-compensator part of those drift rows can in fact be discharged
abstractly.

### Lemma 7.4 (killed-hazard Hardy inequality)

Let `tau` be a discrete stopping time.  Suppose that, conditionally on
`tau>i`, the chance of stopping at the next transition is at least
`c_h h_i`, where `h_i` is deterministic, `0<=h_i<=h_0`, and `c_h,h_0`
are fixed.  For every predictable real process `Z_i`,

\[
 \boxed{
 \mathbb E\sup_{j\le\tau}
       \left|\sum_{i<j}h_iZ_i\right|^2
 \le C(c_h,h_0)\mathbb E\sum_{i<\tau}h_iZ_i^2.}
 \tag{KH}
\]

#### Proof

Expand the square.  For `i<j`, put `H_(i,j)=sum_(i<=s<j)h_s` and use

\[
 2|Z_iZ_j|\le e^{aH_{i,j}}Z_i^2+e^{-aH_{i,j}}Z_j^2
 \tag{KH1}
\]

with `0<a<c_h`.  Conditional survival from `i` through `j` is at most
`exp(-c_h H_(i,j))`.  Hence the first term in (KH1), after expectation,
has kernel `exp(-(c_h-a)H_(i,j))`; its sum against `h_j` is bounded by a
constant depending only on `c_h-a` and `h_0`.  The second term has the
backward deterministic kernel `exp(-aH_(i,j))`, whose sum against `h_i`
is bounded depending only on `a,h_0`.  The diagonal uses
`h_i^2<=h_0h_i`.  This proves the bound for every fixed partial sum.
For the maximum, partition the deterministic cumulative `h`-axis into
unit intervals.  Cauchy--Schwarz bounds the square of the contribution
inside one interval by a constant times `sum h_iZ_i^2` there, while
conditional survival to the `m`-th later interval is at most `e^{-c_hm}`.
Applying Cauchy--Schwarz to the interval contributions with weights
`e^{am}`, `0<a<c_h`, and summing the geometric tail proves the same bound
for the largest partial sum.  \(\square\)

Take

\[
                         h_i=1-\rho_i^2.
 \tag{KH2}
\]

Before `tau^g_(v,w)`, the pair-hit probability at the next transition is

\[
 {Y_v+Y_w-Y_{v,w}\over X}
 \ge {\max\{Y_v,Y_w\}\over X}\ge {c_0\over X}.
 \tag{KH3}
\]

On the provisional global bootstrap interval,
`X<=C_Xp_iM/(2d)`, so (KH3) is at least a fixed multiple of (KH2).
Stopping at an individual bad time can only increase this kill hazard.
Lemma 7.4 is therefore applicable to every good pair.

There is an exact one-root drift decomposition.  Put

\[
 q_i(E)=1-\rho_i^{N_{h(E)}}\rho_{s,i}^2,
 \qquad
 \varepsilon_Q(i)=
 \sum_{E\supseteq Q}\xi_{E,i}r_{E,i}
       \left(q_i(E)-{\Lambda_i(E)\over X(i)}\right).
 \tag{KH4}
\]

Then (SM15)--(SM16) give

\[
 \boxed{
 \mu_Q(i)=-h_iH_Q(i)+\varepsilon_Q(i)-\zeta_Q(i),
 \qquad                         \zeta_Q(i)\ge0.}
 \tag{KH5}
\]

Here `zeta_Q` is zero for the raw hit-killed process and is the conditional
loss caused by an analytical bad transition for the good-killed process.
Indeed `r_E(1-q_i(E))=rho_i^2`, exactly as in (FP7), and deleting the
nonnegative post-transition load on a bad transition subtracts `zeta_Q`.
From (FP5) and
`(FDEF)`,

\[
 \mathbb E\sum_{i<T}h_i\sum_QH_Q(i)^2
 \le \mathbb E\sum_{i<T}h_i\mathcal P_i
                         =O(\mathcal S_2(p_*)).
 \tag{KH6}
\]

The equality sign in the last display denotes equality of scale: summing
(FP5) bounds the middle expression by the initial potential plus the
positive defect budget.

Consequently Lemma 7.4 proves the squared-drift bound for the service term
`-h_iH_Q`.  The extra `zeta_Q` is another killing compensator: the
post-transition load before killing is at most `(1+o(1))H_Q`, and its
predictable bad-kill probability is paid by the simultaneous drop of the
nonnegative potential.  The same proof of Lemma 7.4, with this predictable
kill hazard added to `h_i`, controls its squared accumulated drift and
quadratic variation.  Both `(FDRIFT1)` and the remaining part of `(FDRIFT2)` follow
from the single residual error-energy row

\[
 \boxed{
 \sum_Q\mathbb E\sum_{i<\tau^g_Q}
             {\varepsilon_Q(i)^2\over h_i}
                         =O(\mathcal S_2(p_*)).}
 \tag{FERR}
\]

For `(FDRIFT2)`, apply Lemma 7.4 to
`Z_i=varepsilon_Q(i)/h_i`.  For `(FDRIFT1)`, use Cauchy--Schwarz between
`sum h_iH_Q^2` and `sum varepsilon_Q^2/h_i`, then sum over `Q` and take
expectations.  Thus the pair dynamic theorem is reduced further to
`(FDEF)`, `(GDIR)`, and `(FERR)`; the pure two-root service drift is closed.

The error row itself is a Dirichlet form of the same hazard defect.  Put

\[
                         \mathcal H_i(E)=
 q_i(E)-{\Lambda_i(E)\over X(i)}.
 \tag{KH7}
\]

Expanding the square in (KH4) gives the exact identity

\[
 \sum_Q{\varepsilon_Q(i)^2\over h_i}
 ={1\over h_i}\sum_Q\sum_{E,F\supseteq Q}
    \xi_{E,i}\xi_{F,i}r_{E,i}r_{F,i}
                  \mathcal H_i(E)\mathcal H_i(F).
 \tag{KH8}
\]

The current-to-future factor in `c_iR_i` dominates `r_Er_F` up to
`1+o(1)`: the missing factor is
`rho_i^{-m_N}rho_(s,i)^{-m_S}`, whereas the future weight is at least one,
and one step has `d(1-rho_i)=o(1)`.  Hence `2ab<=a^2+b^2` shows that
`(FERR)` follows from

\[
 \boxed{
 \mathbb E\sum_{i<T}{1\over h_i}
 \sum_{Q,E,F}c_i(Q,E,F)R_i(E,F;Q)
       \bigl(\mathcal H_i(E)^2+\mathcal H_i(F)^2\bigr)
                         =O(\mathcal S_2(p_*)).}
 \tag{HDIR}
\]

Bonferroni expands each `mathcal H_i(E)` into its signed root-incidence deviation
and its first-two-hit correction.  Thus `(HDIR)` and `(GDIR)` are the two
quadratic faces of one gradient/Dirichlet calculation: the former controls
the hazard error along an edge and the latter the nonuniformity of the
future-potential derivative across resources.  Their static injections are
respectively `(ROc)` and `(FE3)`.  A joint stopped Lyapunov proving these
two dynamic transfers is the remaining local analytic step.

The same calculation covers the marked clusters needed for `(AIB)` without
a new rank loss.  If `A` has `m<=3` distinct owner carriers, use

\[
                         H_A(i)=p_i^{m-1}Y_A(i)
 \tag{MCL1}
\]

and kill it at the first carrier hit or cluster-bad time.  A summand then
has exponent `N_h-m`.  In the square potential, future fugacity cancels all
shared resources outside `A`; ideal survival of the full union leaves the
factor `rho_i^m`, rather than `rho_i^2`.  Hence the useful service drift is
`rho_i^m-1`, a fixed multiple of `1-rho_i`, and Lemma 7.4 applies.  The
initial potential is the marked-cluster-rooted analogue of (SM8), bounded
by the base row `(4.7)` times its cluster-rooted FIFO overlap moment.  The
first-two-hit and Dirichlet expansions have the same finite track-entry
types as `(FE3)`, but their normalization is by the smaller cluster mass
and must be replayed explicitly.  That replay is supplied by Propositions
6.2 and 7.1 of
`MATH_THEOREM_JOINT_ROOT_PAIR_LYAPUNOV_AND_MARKED_CLUSTER_NORMALIZATION_20260806.md`.
Thus size-two and size-three cluster tracking has the same remaining
dynamic incidence transfer; it does not require a maximum arbitrary
higher-codegree hierarchy.

The individual degree part is parallel, but here the stopping convention is
slightly stronger than for pairs.  Apply Lemma 7.2 to `Y_v-1` stopped only
at the root hit or the provisional global bootstrap stop, not at the
individual bad time; do the same for
`Y_v^(h)-lambda_h` on lower roots.  The sufficient aggregate input is

\[
 \sum_v\mathbb E\langle M_v\rangle_T
 +\sum_v\mathbb E\sup_{i\le T}|A_v(i)|^2=O(M/d).
 \tag{DROOT}
\]

Then a fixed-width failure of (7.1) has total expectation `O(M/d)` by
Markov, giving its part of `(AIB)`.  Because the root process was not
frozen at that failure, the orbit-resolved versions, with the same right
side, also imply the global continuation conclusion of Proposition 6.3
after choosing the fixed separator constant `c` large enough.  The
marked-cluster part is the finite check and transfer described after
`(MCL1)`, summed only over occurrences which can be charged to a selected
block.  No maximum over all abstract owner tuples is needed.

The first-hit proof for regenerative exponential clocks applies verbatim to
the event

\[
 \{\hbox{the prescribed roots are served before their local bad times}\}.
 \tag{7.4}
\]

If a root becomes bad first, the continuation payoff for that branch is
zero.  Thus there is no additive `Pr(Bad)` term in the cylinder.  On good
branches, (7.2)--(7.3) give

\[
 \Pr(\Pi=\pi,\ \hbox{all tested roots good})
 \le C^{|\pi|}\theta^{|\pi|}
       (d\kappa)^{m-|\pi|}
 \tag{7.5}
\]

through order `O(d)`, for an absolute `C`, provided `gamma` is sufficiently
small for the tested order window.  The factor `d` in the merger parameter
is harmless by Section 4.

If `(SR)` holds and the process reaches `p=c/d` with probability bounded
away from zero, then the terminal live lower set already has size `cM/d`.
Every quarantined doublet releases `2d` lowers, so `(SR)` makes the expected
additional loss `O(M/d)`.  Markov's inequality, with a sufficiently large
fixed constant depending only on the reach probability, gives an outcome
in which terminal live resources and cleanup together cost `O(M/d)`.
Conditioning the output law on this constant-probability event costs only
an absolute factor in an unconditional root cylinder.  Since
retained-root selection is a subevent of (7.4), (7.5) survives such
unconditional conditioning with a fixed root factor.

There is one scope caveat.  Conditioning on a small-cleanup event of
constant **unconditional** probability preserves the unconditional
cylinder up to a fixed factor, but it need not preserve a cylinder after
an arbitrary stopped prefix: the cleanup success probability conditional
on that prefix could be small.  The raw post-quarantine law itself has the
stopped killed-event cylinder.  To obtain simultaneously a deterministic
`O(M/d)` leave and the fully hereditary stopped law, the dynamic lemma must
either give a cleanup bound with uniformly positive conditional probability
after every allowed doublet-closed separator prefix, or show that the
downstream argument only needs the unconditioned expected cleanup.  This
quantifier is included in the remaining lemma below.

Fair opposite orientations may then be exposed independently per retained
doublet.  The balanced-doublet orientation theorem contributes only its
fixed `sqrt(2)` factor, and the filtration remains doublet-closed.

## 8. The exact remaining dynamic lemma

The preceding identities reduce integral packing to the following
template-specific statement.

> **Rank-compensated atomic-doublet tracking lemma.**  For the fixed
> canonical atomic templates defining `B_2,B_3`, the process (6.1)--(6.2)
> reaches `p=c/d` with probability bounded away from zero.  Its global
> live rate remains positive, its orbit mixture remains within a
> sufficiently small fixed error of
> `(lambda_2,lambda_3)`, its individually bad selected blocks and bad
> selected relations satisfy `(SR)` by proving `(SM2)`, `(AIB)`, and
> `(ASE)`.  It is enough for the last row to establish the Doob-budget
> transfer `(DPAIR)` from the static value `(SM7)`.  The future-potential
> and killed-hazard arguments reduce that transfer to `(FDEF)`, `(GDIR)`,
> and `(HDIR)`; the pure two-root service term is already closed.
> Orbit-resolved
> `(DROOT)` gives both `(AIB)` and, via Proposition 6.3, global
> continuation, while the marked-cluster analogues finish `(AIB)`.  These cleanup
> estimates must either hold with a uniformly
> positive conditional success probability after every allowed
> doublet-closed separator prefix, or be shown sufficient in expectation
> for the downstream stopped construction.  The proof may use the
> rooted overlap inequality `(RO)` and its pair/marked-cluster analogues,
> but no maximum full-codegree hypothesis beyond those weighted pattern
> sums.

The static FIFO overlap input to this lemma is now supplied by Section 5:
first and slot overlaps, rigid bases, cross-half resources, terminal fans,
single tracks, and mixed-track entries together prove `(RO)`.  What remains
is best checked in two separate rows.

1. **Local stopped transfer:** prove the Johnson-sector stopped row
   `(JSEC)` from the joint-Lyapunov note for the pair-, root-, and marked
   families.  The pristine Eberlein tail is closed there, so its exact
   remaining form is the adaptive resolvent/switching perturbation
   `(JRES)`--`(JSW)`.  It is the corrected common operator form of `(GDIR)` and the
   first-order part of `(HDIR)`; the centered root potential then gives
   orbit-resolved `(DROOT)`.  The static injections are `(ROc)`, `(PC)`,
   `(FE3)`, and their now-audited marked analogues; Lemma 7.4 prevents a
   logarithmic service loss.
   Proposition 7.1 then gives cleanup without a selection-biased
   conditional root law.
2. **Global bootstrap:** use the orbit-resolved lower-root part of
   `(DROOT)` in the exact identity (6.12).  Proposition 6.3 then keeps the
   total live rate positive and the compensated `2/3` orbit mixture usable
   until `p=c/d`, for a sufficiently large absolute `c`.

Thus no independent all-resource positivity theorem is needed once the
lower-root maximal budget is proved.  This algebraic bootstrap should still
be kept distinct from pair tracking: global positivity alone gives no
stopped pair maximal inequality, and `(DPAIR)` alone says nothing about a
stall.

The static pair-codegree theorem alone proves neither row.  Conversely, a
uniform statement for every resource is unnecessary and would demand an
invalid union bound.

## 9. Black-box boundary and queue state

Vu's higher-codegree theorem does not replace the remaining lemma.  In its
relevant parametrization, a leave `tilde O(n/x)` requires consecutive
codegree drops satisfying

\[
 x^3\le D_j/D_{j+1}
 \tag{9.1}
\]

and a final exponent condition.  A pair ratio by itself corresponds to
stopping the hierarchy at `s=2`; the final condition then contains the
growing rank and does not permit `x=Theta(d)`.  Even a consecutive drop of
order `d` gives only `x=O(d^(1/3))`.  The rooted pattern polynomial is the
bespoke replacement because it weights rare near-redundant FIFO clusters by
their actual number of placements instead of a worst-case `Delta_j`.

Every accepted edge is already a literal balanced pair of atomic portals,
so owner disjointness, the sharp slot cap, and doublet-closed exposure are
automatic.  The process never fixes the terminal `Sym(h)` assignment of a
selected macro.  Hence all terminal permutation switches remain available
after cleanup.  This exports local terminal-permutation joinability.

It does **not** prove that the macro component graph is connected.  A
connected component graph, or an `O(M/d)` separator connector bank which
joins its components, remains an additional global queue row.  Terminal
permutations merge all components once that graphic connectivity premise is
met, without changing any lower, owner, slot, or marked resource.

## 10. Proof-safe conclusion

The balanced-doublet gate is now reduced more sharply than a generic
growing-rank nibble request.

* The correct state-dependent rate is (2.1), with a separate slot-density
  factor.
* In the product residual, the `2/3` mixture and lower/owner density
  equality regenerate exactly.
* At density `1/d`, the pair ratio has room of one full power of `d` and
  the companion merger parameter remains exponentially small.
* Product-residual variance is exactly the rooted FIFO intersection
  polynomial (5.3).
* Dynamic exceptional roots should be charged analytically and removed
  after the run; no impossible all-resource union bound is required.

What is not proved is the adaptive part `(JRES)`--`(JSW)` of the joint
stopped Johnson-sector transfer `(JSEC)`, or the prefix-uniform cleanup
quantifier.  Accordingly this note does not claim
the `O(M/d)` integral matching, the final hereditary unordered cylinder, or
global component connectivity.
