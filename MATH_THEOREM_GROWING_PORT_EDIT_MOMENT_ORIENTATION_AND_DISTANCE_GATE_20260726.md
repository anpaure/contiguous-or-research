# Growing port factors: edit-moment rounding, cube orientation, and the extensive-distance gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let

\[
 n=2s+1,\qquad C_s=\operatorname {Cat}_s,\qquad
 W_s=nC_s=\binom{2s+1}{s},
\]

and let `F,G` be two arbitrary anchored exact `D_s` port factors with the
same prescribed root ports.  They need not be coordinate relabellings.

The earlier maximum-component estimate

\[
 V_H(F,G)\le 2b(F,G)L_H(F,G)
\]

has the following strictly sharper form.  If `K` runs over the rooted
ownership components and

\[
 e_{q,P}={1\over2}\|z^G_{q,P}-z^F_{q,P}\|_1,
\]

define the **edit-size moment**

\[
 \boxed{
 \Xi_H(F,G)=
 {1\over C_s\Omega_H}
 \sum_{q\le H}w_q\sum_K |K|\sum_{P\in K}e_{q,P},
 \qquad \Omega_H=\sum_{q\le H}w_q.}
 \tag{0.1}
\]

When `Omega_H=0`, set `Xi_H=0`.  Then

\[
 \boxed{V_H(F,G)\le 2C_s\Omega_H\Xi_H(F,G).}
 \tag{0.2}
\]

Consequently some literal component-side child satisfies

\[
 \boxed{
 \mathcal Q_H(F_*)
 \le \mathfrak M_H(F,G)
       +{1\over2}C_s\Omega_H\Xi_H(F,G),}
 \tag{0.3}
\]

where `mathfrak M_H` is the exact floor-corrected midpoint energy.  At
`H=ceil(A sqrt(s))`, standard weights satisfy `Omega_H<=H`, and therefore

\[
 {C_s\Omega_H\Xi_H/2\over W_s}
 \le \left({A\over4}+o_A(1)\right){\Xi_H\over\sqrt s}.
 \tag{0.4}
\]

Thus the clean growing-seed theorem is

\[
 \boxed{
 \mathfrak M_H(F,G)=o(W_s),\qquad
 \Xi_H(F,G)=o(\sqrt s)
 \quad\Longrightarrow\quad
 \min_{\text{component children}}\mathcal Q_H=o(W_s).}
 \tag{0.5}
\]

This is the useful non-relabeling variance theorem which survives
component expansion.  It charges a large component only when that
component actually contains edited rows at the observed profiles.

There are two exact obstructions which show that neither hypothesis in
(0.5) is automatic.

1. **Orientation obstruction.**  Every ownership cube has the same
   unsigned component data at all of its vertices.  Fair resampling from a
   vertex has drift equal to the cube-average energy minus the energy of
   that vertex, and these drifts average to zero over all cube vertices.
   Hence no theorem using only unsigned component sizes, edit moments,
   support sizes, or absolute Gram data can orient a strict descent.
   Midpoint counterbias (or a directed comparator inequality) is
   indispensable.
2. **Extensive-distance obstruction.**  If the second seed is at row
   distance `r` from the canonical MSW port factor, every component child
   remains in that same radius-`r` row ball.  The audited invariant-packet
   theorem then gives

   \[
   \boxed{\vartheta(H,\beta)\ge J_s-r}
   \tag{0.6}
   \]

   for every child and every balanced quota containing depth one, where

   \[
   {J_s\over C_s}\longrightarrow
   \delta_{\rm inv}:={107897\over19784704}>0.
   \tag{0.7}
   \]

   Thus a switch construction escaping the canonical packet basin must
   change at least

   \[
   \boxed{
   r\ge J_s-o(C_s/\sqrt s)
    =(\delta_{\rm inv}-o(1))C_s}
   \tag{0.8}
   \]

   rows.  Merely calling a factor a growing `D_s` factor does not meet this
   requirement.

The exact surviving construction is therefore an **extensive but
edit-dispersed** pair: positive-density row distance, a low full-profile
midpoint, and `Xi_H=o(sqrt(s))`.  The statements and constants below
include all cyclic starts and hence all carrier/collar windows.

## 1. Rooted ownership components and complete row profiles

For a middle token `X`, let `rho_F(X),rho_G(X)` be its root owners in the
two factors.  Contract the common port edge labelled by each root `P`.
The resulting rooted owner multigraph has an edge

\[
                       \{\rho_F(X),\rho_G(X)\}.
 \tag{1.1}
\]

Its connected components are denoted by `K`.

The common root port `P` is owned by row `P` on both shores.  Hence every
full bipartite ownership component contains exactly the same root-label
set on its two shores.  In particular, choosing either whole shore of
each component preserves one row at every root as well as the complete
`X/Y` ledgers.  This is the rooted-component theorem proved in
`MATH_THEOREM_GROWING_PORT_FACTOR_SPARSE_COMPONENT_VARIANCE_20260726.md`;
only its canonical root pairing is used here.

Fix any depth window and any common ambient carrier system.  For each root
`P`, let

\[
 z^F_{q,P},z^G_{q,P}
 \tag{1.2}
\]

be the **complete physical** depth-`q` row histograms.  Thus they are
formed after summing the row/start-resolved carrier push-forwards

\[
 \Phi_\omega(e_S)=e_{O_\omega\cup\iota_\omega(S)}.
 \tag{1.3}
\]

No marked boundary column is substituted for (1.2).  Every interval
crossing either port collar is one of its coordinates.  In a standalone
port factor these are the incidence vectors of all cyclic intervals of
the specified length.

Put

\[
 d_{q,P}=z^G_{q,P}-z^F_{q,P},\qquad
 \delta_{q,K}=\sum_{P\in K}d_{q,P}.
 \tag{1.4}
\]

For nonnegative weights `w_q`, the fair component variance is

\[
 V_H(F,G)=\sum_{q\le H}w_q\sum_K\|\delta_{q,K}\|_2^2.
 \tag{1.5}
\]

## 2. The edit-moment variance theorem

### Theorem 2.1 (exact edit-size moment)

With (0.1), one has the exact upper bound (0.2).

#### Proof

Fix `q,K`.  At any physical target, each shore contains at most `|K|`
rows.  Therefore

\[
 \|\delta_{q,K}\|_\infty\le |K|.
 \tag{2.1}
\]

Also, by (1.4) and the triangle inequality,

\[
 \|\delta_{q,K}\|_1
 \le\sum_{P\in K}\|d_{q,P}\|_1
 =2\sum_{P\in K}e_{q,P}.
 \tag{2.2}
\]

Consequently

\[
 \|\delta_{q,K}\|_2^2
 \le\|\delta_{q,K}\|_\infty
       \|\delta_{q,K}\|_1
 \le2|K|\sum_{P\in K}e_{q,P}.
 \tag{2.3}
\]

Multiply by `w_q`, sum over `q,K`, and use (0.1).  This gives

\[
 V_H(F,G)
 \le2\sum_{q\le H}w_q\sum_K|K|\sum_{P\in K}e_{q,P}
 =2C_s\Omega_H\Xi_H(F,G).
\]

\(\square\)

The maximum-component theorem follows because `|K|<=b` in (2.3), but
(0.2) can be much smaller: a giant component containing no changed
observed row has zero charge.

### Corollary 2.2 (variable consecutive edits)

Suppose the two cyclic rows at root `P` agree outside a cyclic block of
`k_P` positions.  Then

\[
 e_{q,P}\le2(k_P-1)_+
 \tag{2.4}
\]

at every proper cyclic interval length, including intervals crossing the
two block boundaries.  Hence

\[
 \boxed{
 \Xi_H(F,G)\le
 {2\over C_s}\sum_K|K|
                  \sum_{P\in K}(k_P-1)_+.}
 \tag{2.5}
\]

If `k_P<=k` on every edited row and

\[
 \chi(F,G)={1\over C_s}\sum_K|K|^2,
 \tag{2.6}
\]

then

\[
 \boxed{\Xi_H(F,G)\le2(k-1)\chi(F,G).}
 \tag{2.7}
\]

#### Proof

A cyclic window can change only if one of its two boundary cuts is
strictly inside the edited block.  There are `k_P-1` internal cuts and,
for a fixed length, each can occur as either boundary of one window.
Thus at most `2(k_P-1)` old windows change, which is (2.4).  Substitute
this in (0.1).  The bound is independent of `q`, so the weights cancel.
Summing `|K|` once for each `P in K` proves (2.7).  \(\square\)

The use of the size-biased moment `chi`, rather than `max |K|`, is sharp
for this estimate: large unedited components contribute nothing to
`Xi_H`, while a component of size `u` in which all rows are edited is
charged proportionally to `u^2`.

## 3. Floor-corrected rounding and exact Gaussian accounting

Let `f^F,f^G` be the centered complete load vectors in the weighted
window, and let `B_H` be the factor-independent integer-floor baseline.
Set

\[
 \mathcal Q_H(F)=\|f^F\|_H^2-B_H,
 \qquad
 \mathfrak M_H(F,G)
 =\left\|{f^F+f^G\over2}\right\|_H^2-B_H.
 \tag{3.1}
\]

### Theorem 3.1 (non-relabeling edit-moment rounding)

Some integral component child satisfies (0.3).

#### Proof

The audited two-seed identity gives

\[
 \mathbb E\mathcal Q_H(F_\varepsilon)
 =\mathfrak M_H(F,G)+{1\over4}V_H(F,G).
 \tag{3.2}
\]

No heat identity is reproved here.  Apply Theorem 2.1 to (3.2), and choose
one outcome no larger than its expectation.  \(\square\)

For `H=ceil(A sqrt(s))` and the standard weights `w_q=1/c_q`, one has
`Omega_H<=H`.  Since `W_s=(2s+1)C_s`, division of (0.3)'s rounding term by
`W_s` gives

\[
 {C_s\Omega_H\Xi_H/2\over W_s}
 \le {\lceil A\sqrt s\rceil\over2(2s+1)}\Xi_H
 =\left({A\over4}+o_A(1)\right){\Xi_H\over\sqrt s}.
 \tag{3.3}
\]

This proves (0.4)--(0.5), including the constant `A/4`.

## 4. Antipodal cube orientation

Fix an ownership overlay with components `K=1,...,J`.  Orient the two
shores once and let `delta_K` be the corresponding stacked component
effect.  Write

\[
 a={f^F+f^G\over2},\qquad
 f^\varepsilon=a+{1\over2}\sum_K\varepsilon_K\delta_K,
 \qquad\varepsilon\in\{\pm1\}^J.
 \tag{4.1}
\]

### Theorem 4.1 (same cube, zero average fair drift)

For every `epsilon`, the direct overlay of the antipodal factors
`F_epsilon,F_(-epsilon)` has exactly the original components.  Its
component effects are the original effects with independently reversed
orientations.  In particular it has the same

* component sizes;
* rowwise edit distances and `Xi_H`;
* component norms and variance `V_H`;
* absolute Gram entries and Gram spectrum; and
* carrier support sizes.

Fairly choosing every component shore in this antipodal overlay produces
the uniform distribution on the same `2^J` cube.  If

\[
 \overline{\mathcal Q}
 =2^{-J}\sum_\eta\mathcal Q_H(F_\eta),
 \qquad
 \Delta(\varepsilon)
 =\overline{\mathcal Q}-\mathcal Q_H(F_\varepsilon),
 \tag{4.2}
\]

then

\[
 \boxed{2^{-J}\sum_\varepsilon\Delta(\varepsilon)=0.}
 \tag{4.3}
\]

More explicitly, with

\[
 D_\varepsilon=\sum_K\varepsilon_K\delta_K,
 \qquad V=\sum_K\|\delta_K\|_H^2,
\]

one has

\[
 \boxed{
 \Delta(\varepsilon)
 ={V\over4}-{\|D_\varepsilon\|_H^2\over4}
                -\langle a,D_\varepsilon\rangle_H.}
 \tag{4.4}
\]

#### Proof

Inside an original component `K`, the two antipodal factors choose
opposite original shores.  Those shores own exactly the same token set,
and their original bipartite overlay is connected.  No token belongs to
two different original components.  Hence the antipodal overlay has
exactly the same component partition.

Reversing the two shores of component `K` multiplies its signed effect by
`-1`, but changes none of the listed unsigned data.  On the Gram matrix it
acts by conjugation with a diagonal sign matrix, preserving its spectrum
and the absolute values of its entries.  Independent fair shore choices
now choose each sign vector `eta` with probability `2^{-J}`, irrespective
of the starting `epsilon`.  This proves the first assertion and (4.2).
Summing (4.2) over all vertices gives (4.3).

Finally, fair-sign averaging in (4.1) gives

\[
 \overline{\mathcal Q}=\|a\|_H^2-B_H+{V\over4}.
\]

Subtract

\[
 \mathcal Q_H(F_\varepsilon)
 =\|a\|_H^2-B_H+\langle a,D_\varepsilon\rangle_H
                    +{1\over4}\|D_\varepsilon\|_H^2
\]

to obtain (4.4).  \(\square\)

### Corollary 4.2 (unsigned heat cannot orient itself)

If the cube energy is nonconstant, some vertices have positive fair drift
and some have negative fair drift.  No condition depending only on the
unsigned data listed in Theorem 4.1 can force a strict fair descent from
every vertex of that cube.

This is not an obstruction to (0.5).  A low midpoint plus a small edit
moment proves that the cube **contains** a low-energy vertex.  It is an
obstruction to replacing the midpoint hypothesis by an unsigned variance
or expansion statement.

## 5. The row-ball hull theorem

For exact factors with the same number of rows, put

\[
 d(F,G)=|F\setminus G|=|G\setminus F|.
 \tag{5.1}
\]

### Theorem 5.1 (the entire switch cube stays in the endpoint row ball)

If `d(F,G)=r`, every ownership-component child `H` of `F,G` satisfies

\[
                         \boxed{d(H,F)\le r.}
 \tag{5.2}
\]

#### Proof

Every row `E in F cap G` is an isolated ownership component.  Indeed each
token of `E` is owned by `E` on both shores, and exact ownership forbids
an edge from either copy of `E` to a different row.  Thus every child
contains all common rows.  All nontrivial component shores consist only of
rows in `F setminus G` and `G setminus F`.  Relative to `F`, a child can
remove at most the `r` rows of `F setminus G`, proving (5.2).  \(\square\)

This elementary fact is stronger than a variance estimate: it controls
every vertex of the cube simultaneously and is independent of component
sizes.

### Theorem 5.2 (extensive distance is necessary from the canonical basin)

Let `F_s^MSW` be the canonical port factor, and let `G` be any exact
factor with `d(F_s^MSW,G)=r`.  For every component child `H` and every
balanced quota system containing depth one,

\[
                         \boxed{\vartheta(H,\beta)\ge J_s-r.}
 \tag{5.3}
\]

Consequently any such cube containing a factor with
`vartheta=o(C_s/sqrt(s))` must satisfy (0.8).

#### Proof

The audited invariant-packet theorem gives, for every exact factor `H`,

\[
 \vartheta(H,\beta)+d(H,\mathcal Q_{\tau,s})\ge J_s,
 \tag{5.4}
\]

where `mathcal Q_(tau,s)` is the complete native MSW one-transposition
cube.  The canonical factor belongs to this cube.  Hence Theorem 5.1 gives

\[
 d(H,\mathcal Q_{\tau,s})
 \le d(H,F_s^{\rm MSW})\le r.
\]

Substitution in (5.4) proves (5.3).  Since
`J_s/C_s -> delta_inv`, the bound
`vartheta=o(C_s/sqrt(s))` forces

\[
 r\ge J_s-o(C_s/\sqrt s)
   =(\delta_{\rm inv}-o(1))C_s.
\]

\(\square\)

## 6. A genuinely non-relabelled growing example with tiny `Xi` and no escape

The sparse obstruction is not vacuous.  Fix any suffix
`B_s in D_(s-4)`.  In the fourteen roots `PB_s`, `P in D_4`, replace the
canonical first slab by the audited noncanonical `D_4` factor and leave
every other row canonical.  The closed-slab context theorem gives an exact
anchored `D_s` port factor `G_s^(B_s)`.  It differs from the canonical
factor in at most fourteen rows.

This factor is not a coordinate relabelling of the canonical factor.  The
canonical first-insertion histogram is

\[
 h_F(2j)=C_{j-1}C_{s-j}>0,\qquad h_F(2j-1)=0.
 \tag{6.1}
\]

The fixed right-suffix slab changes it by

\[
 4(e_3-e_2)-e_4-e_6+2e_7.                            \tag{6.2}
\]

Thus coordinates `3` and `7`, previously unused, acquire counts `4` and
`2`.  The decreased even counts remain positive:

\[
 C_{s-1}-4\ge1,\qquad C_{s-2}-1\ge1,
 \qquad2C_{s-3}-1\ge1                               \tag{6.3}
\]

for every `s>=4`.  Hence the number of zero entries in the first-insertion
histogram drops from `s` to `s-2`.  Coordinate relabelling merely permutes
this histogram and preserves its number of zero entries, proving the
claim.

The nontrivial overlay is confined to those fourteen roots.  In the full
right-concatenated coordinate word the changed local `a` positions and
changed local `b` positions form two bounded blocks, not necessarily one
contiguous block.  The proof of Corollary 2.2 applied to the internal cuts
of both blocks gives a uniform `O(1)` bound for every `e_(q,P)`.  Hence the
definition (0.1) gives

\[
                         \Xi_H=O(C_s^{-1})             \tag{6.4}
\]

uniformly in `H` (the implicit constant is absolute).  Nevertheless every
cube child satisfies

\[
 \vartheta(H,\beta)\ge J_s-14
   =(\delta_{\rm inv}-o(1))C_s.                       \tag{6.5}
\]

Thus this sequence consists of literal, non-conjugate, growing `D_s`
factors and has vanishing edit-moment variance, yet it is maximally
unsuitable for coefficient one.  The failed hypothesis is directed
midpoint/bulk movement, not variance.

## 7. A cap-space version which also survives expansion

For completeness, there is a parallel statement for the exact cap
potential.  Let the cap be `p`, let every depth histogram have total mass
`W`, and put

\[
 \bar\mu_q={\mu_q^F+\mu_q^G\over2}.
\]

For a physical target `T`, write

\[
 d_{q,P}(T)=z^G_{q,P}(T)-z^F_{q,P}(T),
 \qquad
 B_{q,T}=\sum_K\left(\sum_{P\in K}d_{q,P}(T)\right)^2,
 \tag{7.1}
\]

and `mathfrak B=sum_(q,T)B_(q,T)`.  Define the midpoint cap excess

\[
 M=\sum_{q,T}(\bar\mu_q(T)-p)_+.
 \tag{7.2}
\]

### Theorem 7.1 (component-imbalance cap rounding)

Some integral component child satisfies

\[
 \boxed{
 \sum_{q\le H}K_p(\mu_q)
 \le M+{1\over4}\sqrt{{2HW\over p}\,\mathfrak B}
          +{\mathfrak B\over8p}.}
 \tag{7.3}
\]

In particular,

\[
 M=o(W),\qquad \mathfrak B=o(pW/H)
 \quad\Longrightarrow\quad
 \sum_{q\le H}K_p(\mu_q)=o(W).                       \tag{7.4}
\]

#### Proof

Under fair component signs, the fluctuation at `(q,T)` has variance
`B_(q,T)/4`.  The audited margin-sensitive cap inequality bounds its
contribution by

\[
 {1\over4}\sqrt{B_{q,T}}
 \quad\text{when }\bar\mu_q(T)>p/2,
 \qquad
 {B_{q,T}\over8p}
 \quad\text{otherwise}.                              \tag{7.5}
\]

At a fixed depth there are at most `2W/p` targets in the first class,
because their midpoint loads have total mass `W`.  Across `H` depths
there are at most `2HW/p` such targets.  Cauchy--Schwarz in (7.5) gives
(7.3).  The two error terms are `o(W)` under (7.4).  \(\square\)

For a standalone `D_s` factor, `p=n` and `W=nC_s`, so the required
imbalance budget at `H=ceil(A sqrt(s))` is

\[
 \mathfrak B=o\left({n^2C_s\over H}\right)
 =o_A(s^{3/2}C_s).                                   \tag{7.6}
\]

This is a signed cancellation condition inside the **actual expanded
components**.  A bound on component size alone is sufficient but not
necessary.

## 8. Exact constructive redirect

The component-expansion and bounded-seed no-gos leave the following
precise positive theorem to prove.

For every fixed `A>0` and all sufficiently large `s`, construct two exact
anchored `D_s` port factors `F_s,G_s` such that, with
`H=ceil(A sqrt(s))`,

\[
 \boxed{
 \begin{aligned}
 &\mathfrak M_H(F_s,G_s)=o(W_s),\\
 &\Xi_H(F_s,G_s)=o(\sqrt s),\\
 &\text{all midpoint and edit quantities are computed on the complete}
       \text{ physical carrier tensor},
 \end{aligned}}
 \tag{8.1}
\]

and audit `Xi_H` on the complete row/start-resolved physical carrier
tensor.  If the construction is intended to escape directly from the
canonical basin by one two-seed cube, it must additionally satisfy the
necessary extensive-distance bound

\[
                         d(F_s^{\rm MSW},G_s)
 \ge(\delta_{\rm inv}-o(1))C_s.                       \tag{8.2}
\]

Theorem 3.1 then gives a literal exact child with
`mathcal Q_H=o(W_s)`.  A cap-based construction may replace the first two
lines of (8.1) by (7.4).

This redirect is stronger and more exact than “find a growing
noncanonical seed.”  It requires simultaneously:

1. enough edited roots to leave the canonical robust basin;
2. an edit-weighted ownership moment below the critical `sqrt(s)` scale;
3. a signed low midpoint, which the antipodal orientation theorem shows
   cannot follow from unsigned expansion; and
4. the full carrier/collar tensor, not a first-insertion marginal.

No pair satisfying (8.1)--(8.2) is constructed here, so no coefficient-one
claim is made.
