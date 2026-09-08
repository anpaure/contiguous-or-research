# Pascal event transducers, dual-gap buffers, and a protected compiler braid

Date: 2026-07-29  
Lane: AD  
Status: exact all-depth event-stream theorem; exact finite Catalan-leave
ribbon; exact protected shadow/core/Hall braid criterion; solver-free
validation on the frozen `k=11`, `k=13`, and `k=14` words.  No
all-semilength recursion is claimed.

## 0. Verdict

The odd/even Pascal operations have a very small exact event algebra.  If

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\},
\]

then the facet and union rows

\[
 (\partial T)_i=T_i\cap T_{i+1},\qquad
 (\nabla T)_i=T_i\cup T_{i+1}
\]

have event streams

\[
 (\alpha_i^\partial,\beta_i^\partial)
   =(\alpha_{i+1},\beta_i),
 \qquad
 (\alpha_i^\nabla,\beta_i^\nabla)
   =(\alpha_i,\beta_{i+1}).                         \tag{0.1}
\]

On one-run lifetime/zero-gap pairs they act by

\[
 \partial:(\ell,g)\mapsto(\ell-1,g+1),\qquad
 \nabla:(\ell,g)\mapsto(\ell+1,g-1).               \tag{0.2}
\]

They are inverse up to one chronology shift whenever the corresponding
singleton-return obstruction is absent.  More importantly, they transport
the complete lower and upper flag towers occurrence by occurrence, at all
depths.  Thus they are genuine symbolic Pascal transducers, not layer-count
analogies.

This gives a positive two-level compiler rule.  An odd-to-even lift at child
compiler depth `d` uses parent depth `d` ports on the copied shore and a
shifted parent depth `d+1` package on the facet shore.  An even-to-odd lift
uses parent depth `d` ports on the copied shore and, on a reversed union arm,
a shifted parent depth `d-1` package.  Interior one-cores and their physical
Hall matchings combine exactly because the two new-coordinate target shores
and the two child sectors are disjoint.  Only cross-seam core equations,
promoted collar columns, the empty old part needed for the singleton
new-coordinate target, the final residual Hall check, and the separate
linear endpoint/suffix conditions remain.

There are also two exact local gadgets.

1. Every gap of length `g` in the Catalan leave of the direct `k -> k+2`
   four-sector construction produces one finite mixed ribbon.  The two new
   coordinates have one-run length `g+1` and zero-gap length `2g-1`; all old
   events on that ribbon are explicit.
2. The frozen `k=13` opening is a common-deletion portal.  Its new seam
   preserves one closure colour exactly, and the only lost colour is restored
   literally in the terminal compiler suffix.

The obstruction is sharp at the local level.  A consecutive OR-support-
neutral Pascal triangle creates trace `1,0,1` in the new coordinate, hence a
zero-gap of length one; moreover a crossing fixed-depth upper witness grows
by one edge, so the triangle is not same-depth shadow-neutral.  The frozen
optimal words also have minimum zero-gap one.  The `k=13` source path has 415
internal zero-gaps of length at most two.  Their closed edge spans have exact
minimum transversal size 260, so every pure piece rethreading which becomes
depth-two dual-gap resident needs at least 260 old cuts.  The analogous exact
number for the 532 short gaps of the final `k=14` path is 351.  The actual
six-piece braid has only two cuts on its copied `k=13` shore and is therefore
necessarily one-sided: it preserves lower residence, all needed audited
shadow support, and an artifact-specific literal compiler, but not dual-gap
residence.

Consequently the exact recursive invariant is the pair of event queues plus
protected flag occurrences and the compiler transfer relation.  A scalar
dual-gap lower bound is a clean sufficient invariant, but it is strictly
stronger than the known optimums.

## 1. Event, lifetime, gap, and shadow notation

Let `T=(T_i)` be a cyclic strict Johnson chronology of rank `r` on a finite
ground set `Omega`.  Write

\[
 T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.              \tag{1.1}
\]

For a coordinate `x`, its cyclic membership trace has alternating one-runs
and zero-runs.  Pair every one-run of length `ell` with the immediately
following zero-gap of length `g`.

For `q>=0`, put

\[
 L_q(T)_i=\bigcap_{h=0}^{q}T_{i+h},\qquad
 U_q(T)_i=\bigcup_{h=0}^{q}T_{i+h}.                 \tag{1.2}
\]

The event-prefix identities are unconditional:

\[
 L_q(T)_i=T_i\setminus\{\alpha_i,\ldots,\alpha_{i+q-1}\},
                                                               \tag{1.3}
\]

\[
 U_q(T)_i=T_i\cup\{\beta_i,\ldots,\beta_{i+q-1}\}. \tag{1.4}
\]

Call `T` **biresident through `(d,u)`** when every one-run has length at
least `d+1` and every zero-gap has length at least `u+1`.  Equivalently,

\[
 \beta_i\notin\{\alpha_{i+1},\ldots,\alpha_{i+d}\},
 \qquad
 \alpha_i\notin\{\beta_{i+1},\ldots,\beta_{i+u}\}. \tag{1.5}
\]

For equal depth `d`, define the synchronized recent-event queues

\[
 B_i^+=(\beta_{i-d},\ldots,\beta_{i-1}),\qquad
 B_i^-=(\alpha_{i-d},\ldots,\alpha_{i-1}).           \tag{1.6}
\]

Then biresidence is exactly

\[
 \alpha_i\notin B_i^+,\qquad \beta_i\notin B_i^-.  \tag{1.7}
\]

The lower and upper envelopes are

\[
 P_i^{(d)}=T_i\setminus B_i^+
   =\bigcap_{a=0}^{d}T_{i-a},                         \tag{1.8}
\]

\[
 Q_i^{(d)}=T_i\cup B_i^-
   =\bigcup_{a=0}^{d}T_{i-a}.                         \tag{1.9}
\]

Their exact updates are

\[
 P_{i+1}^{(d)}=P_i^{(d)}-\{\alpha_i\}+\{\beta_{i-d}\},
                                                               \tag{1.10}
\]

\[
 Q_{i+1}^{(d)}=Q_i^{(d)}-\{\alpha_{i-d}\}+\{\beta_i\}.
                                                               \tag{1.11}
\]

Thus a biresident carrier already contains two synchronized Johnson
chronologies: its erosion and dilation rows.  These two queues, not just the
one-run queue, are the finite seam state required by a dual-resident
recursion.

## 2. The facet/union Pascal ladder

### Theorem 2.1 (exact bidirectional Pascal transducer)

Define

\[
 (\partial T)_i=T_i\cap T_{i+1},\qquad
 (\nabla T)_i=T_i\cup T_{i+1}.                       \tag{2.1}
\]

1. If `T` has no one-run of length one, `partial T` is a strict Johnson
   chronology and

   \[
   (\alpha_i^\partial,\beta_i^\partial)
      =(\alpha_{i+1},\beta_i).                       \tag{2.2}
   \]

   Each run pair transforms as

   \[
   (\ell,g)\mapsto(\ell-1,g+1).                     \tag{2.3}
   \]

2. If `T` has no zero-gap of length one, `nabla T` is a strict Johnson
   chronology and

   \[
   (\alpha_i^\nabla,\beta_i^\nabla)
      =(\alpha_i,\beta_{i+1}).                       \tag{2.4}
   \]

   Each run pair transforms as

   \[
   (\ell,g)\mapsto(\ell+1,g-1).                     \tag{2.5}
   \]

3. At every depth,

   \[
   L_q(\partial T)_i=L_{q+1}(T)_i,                  \tag{2.6}
   \]

   and, for `q>=1`,

   \[
   U_q(\partial T)_i=U_{q-1}(T)_{i+1}.              \tag{2.7}
   \]

   Dually,

   \[
   U_q(\nabla T)_i=U_{q+1}(T)_i,                    \tag{2.8}
   \]

   and, for `q>=1`,

   \[
   L_q(\nabla T)_i=L_{q-1}(T)_{i+1}.                \tag{2.9}
   \]

4. Under the respective singleton exclusions,

   \[
   \nabla\partial T=\operatorname{shift}(T),\qquad
   \partial\nabla T=\operatorname{shift}(T).        \tag{2.10}
   \]

#### Proof

Put `I_i=T_i cap T_(i+1)`.  In the common state `T_(i+1)`,

\[
 I_i=T_{i+1}\setminus\{\beta_i\},\qquad
 I_{i+1}=T_{i+1}\setminus\{\alpha_{i+1}\}.         \tag{2.11}
\]

The two missing coordinates are distinct precisely when the coordinate
inserted at `i` is not deleted at `i+1`, that is, when there is no singleton
one-run.  This proves (2.2).  On a binary trace, replacing `t_i` by
`t_i t_(i+1)` erodes each one-run at its right end and enlarges the following
zero-gap at its left end, proving (2.3).

Similarly, with `V_i=T_i union T_(i+1)`,

\[
 V_i=T_{i+1}\cup\{\alpha_i\},\qquad
 V_{i+1}=T_{i+1}\cup\{\beta_{i+1}\}.               \tag{2.12}
\]

The two added coordinates are distinct precisely when there is no singleton
zero-gap.  This proves (2.4), and the trace `t_i or t_(i+1)` proves (2.5).

Equation (2.6) is associativity of intersection.  Under the first singleton
exclusion, adjacent facets satisfy

\[
 I_{j-1}\cup I_j=T_j.                               \tag{2.13}
\]

Taking the union of `I_i,...,I_(i+q)` therefore gives the union of
`T_(i+1),...,T_(i+q)`, proving (2.7).  Equations (2.8)--(2.9) are the dual
argument using

\[
 V_{j-1}\cap V_j=T_j.                               \tag{2.14}
\]

Equations (2.13)--(2.14) are exactly (2.10).  \(\square\)

### Corollary 2.2 (sharp buffer law)

The facet row alone is biresident through `(d,u)` exactly when

\[
 \min\ell(T)\ge d+2,\qquad \min g(T)\ge u.         \tag{2.15}
\]

The union row alone is biresident through `(d,u)` exactly when

\[
 \min\ell(T)\ge d,\qquad \min g(T)\ge u+2.         \tag{2.16}
\]

If one construction uses both `T` and `partial T`, its bulk is biresident
through `(d,u)` exactly when

\[
 \min\ell(T)\ge d+2,\qquad \min g(T)\ge u+1.       \tag{2.17}
\]

If it uses both `T` and `nabla T`, the corresponding condition is

\[
 \min\ell(T)\ge d+1,\qquad \min g(T)\ge u+2.       \tag{2.18}
\]

If the same base row must supply all three sectors `T`, `partial T`, and
`nabla T`, the exact combined bulk threshold is

\[
 \min\ell(T)\ge d+2,\qquad \min g(T)\ge u+2.         \tag{2.19}
\]

Thus the facet sector spends one unit of lifetime buffer and the union sector
spends one unit of zero-gap buffer.  Their operator composition is merely a
chronology shift by (2.10), so this is a simultaneous sector requirement,
not cumulative loss under formal composition.  Seam collars can impose
additional conditions.

## 3. Dimension-changing shadow and compiler charts

### Theorem 3.1 (odd-to-even facet chart)

Let `|Omega|=2r-1`, and let `T` be a lower-rainbow exact rank-`r` Johnson
factor.  Its facets `I_i=T_i cap T_(i+1)` enumerate every `(r-1)`-set once.
Adjoin `z` and form the disjoint factor

\[
 A_i=T_i,\qquad B_i=\{z\}\cup I_i.                  \tag{3.1}
\]

The two sectors enumerate every rank-`r` child owner exactly once.  Their
internal shadows are

\[
 L_q(A)_i=L_q(T)_i,\qquad U_q(A)_i=U_q(T)_i,         \tag{3.2}
\]

\[
 L_q(B)_i=\{z\}\cup L_{q+1}(T)_i,                  \tag{3.3}
\]

and, for `q>=1`,

\[
 U_q(B)_i=\{z\}\cup U_{q-1}(T)_{i+1}.              \tag{3.4}
\]

Consequently, at every fixed depth `q`, the no-`z` and `z` child target
decks are exactly the adjacent two parent depths displayed in
(3.2)--(3.4), provided the witnessing windows have their expected ranks.

At compiler depth `d`, the maximal child envelopes are

\[
 P_d(A)_i=P_d(T)_i,\qquad
 P_d(B)_i=\{z\}\cup P_{d+1}(T)_{i+1}.               \tag{3.5}
\]

Here and below `P_d(T)_i` means the backward envelope `P_i^(d)` of
(1.8).  The shift in the second formula is essential: the `B_i` envelope
uses the parent states `T_(i-d),...,T_(i+1)`.

Suppose the parent carries

* a depth-`d` one-core and physical Hall matching for every required no-`z`
  low target, and
* a depth-`d+1` one-core and physical Hall matching for every old part of a
  required `z`-target, including one auxiliary empty old target assigned to
  a column with empty core.

Then, on the unbraided interiors, keep the first core on `A` and use the
shifted core `{z} union C_(i+1)` at `B_i`.  The two one-core equations remain exact, and the two
Hall matchings combine into one child matching because their target sets and
position sets are disjoint.  The auxiliary empty target becomes the child
singleton `{z}`.

#### Proof

The owner count is Pascal's identity, while the facet deck is exact by the
lower rainbow.  Equations (3.2)--(3.4) are Theorem 2.1.  Equation (3.5)
follows by intersecting `B_(i-d),...,B_i`:

\[
 \bigcap_{a=0}^{d}B_{i-a}
 =\{z\}\cup\bigcap_{h=i-d}^{i+1}T_h
 =\{z\}\cup P_{d+1}(T)_{i+1}.
\]

For a core port, the exact incidence condition is

\[
 C_i\subseteq S\subseteq P_i.                       \tag{3.6}
\]

On `A`, neither the core, target, nor envelope contains `z`.  On `B`, all
three contain `z`, so (3.6) reduces to the old depth-`d+1` incidence after
deleting `z`.  The core union equation also reduces after deleting the
coordinate which is present in both adjacent `B` cores.  The two physical
column sets are disjoint, so the two injections combine.  For the singleton
`{z}`, condition (3.6) forces the old core to be empty.  \(\square\)

This theorem is an interior theorem.  A cross seam between `A` and `B`
still needs its actual core equation, and every matching edge invalidated by
collar promotion belongs to the residual Hall problem of Theorem 6.1 below.

### Theorem 3.2 (even-to-odd union chart)

Let `T_a,...,T_b`, with `a<b`, be one interval selected by the direct
common-colour Pascal construction, put `U_i=T_i union T_(i+1)`, and let
`L=b-a+1>=2`.  Assume on the relevant union arm that there is no singleton
zero-gap, so `beta_i != alpha_(i-1)` and consecutive reversed-`U` states are
distinct.
Assume `d>=1` whenever the depth-`d-1` compiler package is invoked.
The child cycle

\[
 zT_a,\ldots,zT_b,U_{b-1},\ldots,U_a               \tag{3.7}
\]

has event word

\[
 (\alpha_i,\beta_i)\quad(a\le i<b),                 \tag{3.8}
\]

\[
 (z,\alpha_{b-1}),                                   \tag{3.9}
\]

\[
 (\beta_i,\alpha_{i-1})
       \quad(i=b-1,b-2,\ldots,a+1),                 \tag{3.10}
\]

\[
 (\beta_a,z).                                        \tag{3.11}
\]

The new-coordinate trace is

\[
 1^L0^{L-1}.                                         \tag{3.12}
\]

Thus lower residence through depth `d` needs `L>=d+1`, while dual-gap
residence through depth `u` needs the strictly stronger `L>=u+2`.

On every internal `zT` arm, the shadow and compiler package is parent depth
`d`.  On every internal reversed-`U` arm, the exact forward child-shadow
identities are

\[
 L_q^{\rm rev\,U}(U_i)=L_{q-1}(T)_{i-q+1}\quad(q\ge1),\qquad
 U_q^{\rm rev\,U}(U_i)=U_{q+1}(T)_{i-q}\quad(q\ge0). \tag{3.13a}
\]

Thus lower data use a shifted parent depth `q-1`, while upper depth `q` uses
shifted parent depth `q+1`.  At child state `U_i`, whose preceding states on
the reversed arm are `U_(i+1),...,U_(i+d)`, the exact backward compiler
identity is

\[
 P_d(zT)_i=\{z\}\cup P_d(T)_i,\qquad
 P^{\rm rev\,U}_d(U_i)
   =L_d(\nabla T)_i
   =L_{d-1}(T)_{i+1}
   =P_{d-1}(T)_{i+d}.                                \tag{3.13}
\]

Hence a protected depth-`d` package for the `z`-targets and a protected
depth-`d-1` package for the no-`z` targets combine on the two interiors, with
the two turn collars checked directly from (3.8)--(3.11).

#### Proof

The forward events are inherited.  Since

\[
 U_{b-1}=T_b\cup\{\alpha_{b-1}\},
\]

the first turn is (3.9).  On the reverse arm,

\[
 U_i=T_i\cup\{\beta_i\},\qquad
 U_{i-1}=T_i\cup\{\alpha_{i-1}\},
\]

which gives (3.10); the last turn gives (3.11).  Equation (3.12) follows
immediately.  Equation (3.13a) is (2.9) and (2.8) applied at the first
forward-union index `i-q`.  The last three equalities in (3.13) are (2.9),
with the final one simply rewriting the forward interval
`T_(i+1),...,T_(i+d)` as a backward envelope.  \(\square\)

## 4. The Catalan-leave mixed ribbon

Use the four-sector semilength-raising construction with

\[
 A_i=C_i\cup\{x,y\},\quad X_i=T_i\cup\{x\},\quad
 Y_i=T_i\cup\{y\},\quad U_i=T_i\cup T_{i+1}.        \tag{4.1}
\]

Here `C_i=T_i cap T_(i+1)` is the parent facet.

Let `j,k` be consecutive leave positions on one parent component and put
`g=k-j` in the cyclic orientation.

### Theorem 4.1 (exact finite ribbon and dual-gap rule)

The mixed child segment between the two leave vertices is exactly

\[
 A_j,
 Y_{j+1},\ldots,Y_k,
 U_{k-1},\ldots,U_{j+1},
 X_{j+1},\ldots,X_k,
 A_k.                                                \tag{4.2}
\]

For `g>=2`, its directed event types are

\[
\begin{array}{c|c}
\text{transition}&(\text{deleted},\text{inserted})\\ \hline
A_j\to Y_{j+1}&(x,\beta_j)\\
Y_i\to Y_{i+1}&(\alpha_i,\beta_i)\\
Y_k\to U_{k-1}&(y,\alpha_{k-1})\\
U_i\to U_{i-1}&(\beta_i,\alpha_{i-1})\\
U_{j+1}\to X_{j+1}&(\beta_{j+1},x)\\
X_i\to X_{i+1}&(\alpha_i,\beta_i)\\
X_k\to A_k&(\alpha_k,y).
\end{array}                                          \tag{4.3}
\]

For `g=1`, the empty `U` arm is replaced by the direct event

\[
 Y_{j+1}\to X_{j+1}:(y,x).                          \tag{4.4}
\]

Across all mixed components, both new coordinates have one-run multiset

\[
 \{g+1:g\text{ is a leave gap}\}                   \tag{4.5}
\]

and zero-gap multiset

\[
 \{2g-1:g\text{ is a leave gap}\}.                 \tag{4.6}
\]

These are marginal multisets, not the same pairing for the two labels.  If
the cyclic leave gaps in order on one parent/mixed component are `g_a`, then
their exact paired run/gap histograms are

\[
 H_y=\sum_a e_{(g_a+1,\,2g_a-1)},\qquad
 H_x=\sum_a e_{(g_a+1,\,2g_{a+1}-1)}.               \tag{4.6a}
\]

The all-`A` cycles from the cap-two factor are constant one in both new
coordinates.  Therefore `x,y` are biresident through `(d,u)` if and only if
every leave gap satisfies

\[
 g\ge d,\qquad
 g\ge\left\lceil\frac{u+2}{2}\right\rceil.         \tag{4.7}
\]

The event list (4.3) determines every lower and upper window at every depth
by (1.3)--(1.4).  In particular, it is one finite multi-depth ribbon, not a
separate gadget for each shadow rank.

#### Proof

Following the degree-two edge rules from `A_j` gives the `Y` arm, the
descending selected-union arm, and the `X` arm in exactly the order (4.2).
Taking set differences gives (4.3)--(4.4).  On the displayed segment, `y`
is present on `A_j,Y_(j+1),...,Y_k` and absent on the following `g-1` union
states and `g` `X` states.  The corresponding statement for `x` is the
reflection across the segment boundary.  This proves (4.5)--(4.7).
\(\square\)

Old-coordinate traces on the `X/Y` arms are inherited.  On a descending
`U` arm they are governed by (3.10), while on the `A`-only cap-two cycles
their order is the chosen nonparent order.  Thus (4.7) closes only the two
new labels.  The exact old-label event word and the compiler port transfer
remain part of the root signature.

## 5. One OR-support triangle and its sharp obstruction

Put

\[
 Q_{i-1}=T_i\setminus\{\beta_{i-1}\},\qquad
 Q_i=T_i\setminus\{\alpha_i\},                       \tag{5.1}
\]

and

\[
 P=\{z\}\cup Q_{i-1},\qquad R=\{z\}\cup Q_i,
 \qquad V=T_i.                                       \tag{5.2}
\]

### Theorem 5.1 (OR-support-neutral triangle)

Assume `alpha_i != beta_(i-1)`, equivalently that the displayed parent turn
is not a singleton one-run.  Then the direct facet edge and its two-side
subdivision are strict and have events

\[
 P\to R:(\alpha_i,\beta_{i-1}),                     \tag{5.3}
\]

\[
 P\to V:(z,\beta_{i-1}),\qquad
 V\to R:(\alpha_i,z),                               \tag{5.4}
\]

and satisfy

\[
 P\cup R=P\cup V=V\cup R=\{z\}\cup T_i.           \tag{5.5}
\]

Replacing `P,R` by `P,V,R` preserves the OR value of every old contiguous
interval: an interval crossing `P|R` is represented by the corresponding
interval through `P,V,R`.  Its edge length, however, increases by one.  Thus
the move preserves arbitrary-length upper support, but it does **not**
preserve a fixed-depth row `U_q`: a crossing `q`-edge witness becomes a
`q+1`-edge witness.  Dually, a lower intersection spanning both old
endpoints changes from `S` to `S\setminus\{z\}` and also gains one edge.

However, the new-coordinate trace on the triangle is

\[
                         1,0,1.                      \tag{5.6}
\]

Hence the raw consecutive subdivision creates a zero-gap of length one and
is incompatible with every positive dual-gap requirement.  It also inserts
the additional middle owner `V`; a deck-exact exchange must remove or route
that owner elsewhere.

#### Proof

Under the stated inequality, equations (5.3)--(5.5) are direct set
differences and unions.  Any old
interval crossing `P|R` becomes the corresponding interval through
`P,V,R`; inserting `V subseteq P union R` does not change its union.  For a
lower intersection, every old coordinate common to `P,R` lies in `T_i`,
while `z` does not, giving the stated deletion.  Equation (5.6) is immediate.
\(\square\)

This is the smallest exact explanation for why topological Pascal
Hamiltonization is cheap but simultaneous fixed-depth shadows and dual-gap
residence are not.  A valid owner-exact braid must route the added owner and
stretch the two alternate triangle sides nonlocally; the collar ledger must
account for the depth shift.

## 6. Protected shadow/core/Hall braid theorem

Consider a decorated chronology cut at `s` old seams, with the retained
pieces possibly reversed and rejoined at `s` new strict Johnson seams.  Fix
compiler depth `d`, dual-gap depth `u`, and protected shadow depth `H`.
An event comparison **crosses** a seam when its closed event-index interval
contains that seam.

### Theorem 6.1 (finite protected braid)

The new chronology retains biresidence through `(d,u)`, all declared lower
and upper targets through depth `H`, and a cyclic compiler-ready core and
target-occurrence matching if the following exact conditions hold.

1. Every new seam is Johnson-legal.
2. Every old one-run of length at most `d`, and every old zero-gap of length
   at most `u`, has a deleted seam in its closed event span.
3. Every new no-return comparison (1.5) whose event interval crosses a new
   seam passes.
4. For every `q<=H`, every target whose old protected occurrences all cross
   deleted seams has a named expected-rank occurrence in a new `q`-collar.
5. Let `R` be the changed depth-`d` erosion halo, enlarged by one unchanged
   envelope column at every outer boundary.  Transport the old one-core
   outside `R`; at every position of `R`, including the added unchanged
   boundary columns, set the new core equal to the full recomputed envelope.
   This is the canonical seam promotion.
6. Discard every old matching edge assigned to a position of `R`, even if it
   happens to remain valid after promotion, and retain every transported
   matching edge outside `R`.  Let `D` be exactly the targets formerly
   matched into `R`.  Let `K^+` be all new positions not occupied by the
   retained matching, not merely the geometrical collar.  The actual
   post-promotion core/envelope incidence graph contains a matching

   \[
                         D\hookrightarrow K^+.       \tag{6.1}
   \]

#### Proof

A retained binary run or gap whose closed span avoids all cuts remains
inside one transported piece; reversal preserves its length.  Every new
short run or gap crosses a new seam and is exactly one of the comparisons in
item 3.  This proves residence.

A `q+1`-vertex window changes only when it crosses an old or new seam.
Transported protected occurrences give every unaffected target, and item 4
gives precisely the lost ones.

Outside the erosion halo, both envelope and core transport unchanged.  On an
edge with two promoted halo endpoints, both cores are the full envelopes, so
the one-core union equation holds directly.  At an outer
promoted/unpromoted boundary the envelope pair is an unchanged old pair.
Replacing one old core by its larger full envelope cannot destroy the exact
old union equality: the new union contains the old full envelope union and
is contained in the same full envelope union.  Thus item 5 gives one global
core.  Every retained matching edge lies outside `R`, where its incidence
transports unchanged.  The retained edges and (6.1) have disjoint target and
position sets because `K^+` excludes occupied positions, so together they
saturate the complete target family.  This is precisely a cyclic
compiler-ready decoration.
\(\square\)

The theorem does **not** by itself open that decoration into a linear literal
word.  For that conclusion one must additionally exhibit a safe opening and
check the actual endpoint core/envelope equations and the `d` terminal suffix
columns required by the fixed-core linearization theorem.  Those conditions
are artifact data, not consequences of the collar ledger.

The exact collar bounds are

\[
 |K_{q,\rm old}|,|K_{q,\rm new}|\le sq,              \tag{6.2}
\]

\[
 |K_{\rm erosion}|\le sd,\qquad
 |R|\le s(d+2),\qquad |D|\le |R|,                    \tag{6.3}
\]

with at most `s(d+3)` core adjacencies incident with promoted positions.
Overlaps only decrease these bounds.  The theorem composes: after one braid,
its two event queues, protected occurrences, endpoint core masks, and
matched-port relation are the input decoration for the next braid.

This is a sufficient theorem, not an assertion that every successful braid
has an assignment avoiding promotion.  Condition (6.1), against positions
left free by the retained matching, is the exact residual Hall gate for
extending that specified partial matching with this canonical promoted core.
Failure of (6.1) does not exclude a global rematching which also moves targets
outside `R`.

### Theorem 6.2 (short-gap cut lower bound)

Let `Z_<=u(T)` be the number of internal or cyclic zero-gaps of length at
most `u`, summed over all `k` coordinates.  Every cut/reverse/rejoin braid
which becomes dual-gap resident through depth `u` uses at least

\[
 s\ge\left\lceil\frac{Z_{\le u}(T)}k\right\rceil    \tag{6.4}
\]

old cuts.  The analogous bound with short one-runs holds for ordinary
residence.

#### Proof

Every old short gap whose closed span contains no cut survives wholly inside
one retained piece, possibly reversed.  It therefore remains short.  For a
fixed coordinate the closed spans of distinct zero-gaps are edge-disjoint,
so one cut lies in at most one such span per coordinate, hence in at most `k`
spans total.  \(\square\)

### Theorem 6.3 (exact linear short-gap transversal)

Let `T_0,...,T_(N-1)` be a linear Johnson path.  For every coordinate and
every maximal internal zero-gap occupying states `a,...,b-1`, associate its
closed edge span

\[
                         [a-1,b-1].                  \tag{6.5}
\]

Let `F_<=u` be the family of these intervals for gaps of length at most `u`.
Every pure cut/reverse/rejoin braid which is dual-gap resident through depth
`u` must cut a hitting set of `F_<=u`.  Consequently it uses at least

\[
 \tau(F_{\le u})                                      \tag{6.6}
\]

old cuts.  Because these are intervals on one edge line, `tau` is computed
exactly by repeatedly choosing the smallest right endpoint among the
remaining intervals and deleting every interval containing it.

#### Proof

If no old cut lies in `[a-1,b-1]`, both boundary one-states and the entire
zero-gap remain in one retained piece.  Reversal preserves its length, so a
short gap survives.  Hence the cuts hit every interval.  For interval
families, let `r` be the smallest right endpoint.  Any hitting set contains
some point `p` in an interval ending at `r`.  Every interval hit by `p` has
left endpoint at most `p<=r` and right endpoint at least `r`, by the
minimality of `r`; replacing `p` by `r` therefore preserves all those hits.
Thus an optimum contains `r`; induction proves the earliest-finish
greedy algorithm optimal.  \(\square\)

This is an exact necessary cut count for the inherited short gaps.  It is
not sufficient for residence: new joins may create additional short gaps.

## 7. A reusable endpoint portal

### Theorem 7.1 (common-deletion portal with suffix restitution)

Let two oriented closure edges be

\[
 u\to a:(p,q),\qquad b\to v:(r,s),                  \tag{7.1}
\]

and suppose the proposed join is

\[
 u\to v:(p,t).                                       \tag{7.2}
\]

Opening the two closures and inserting `u->v` preserves the first lower
colour exactly:

\[
 u\cap a=u\setminus\{p\}=u\cap v.                  \tag{7.3}
\]

The orientation is important: deleting the two closures leaves paths
`a...u` and `v...b`, which the new edge joins as `a...u->v...b`.  At lower
depth one, among the three displayed seam occurrences only the second
closure colour `b cap v` can disappear; it may of course retain another
occurrence elsewhere.  At every fixed depth `q`, all other changes lie in
the `q`-collars of the three affected seams.

Put `L=b cap v` and assume `L` is nonempty.  If the preceding `d` source
letters are fixed, appending `L` realizes `L` literally and gives terminal
depth-`d` value `b` if and only if

\[
       (\text{OR of the preceding `d` letters})\cup L=b.           \tag{7.4}
\]

The appended letter affects no earlier depth-`d` window.

#### Proof

Equation (7.3) follows from the common deletion token.  Every window outside
the three collars is unchanged.  The appended source letter belongs to only
the new terminal length-`d+1` window, so (7.4) is necessary and sufficient
for its terminal depth-`d` value while realizing `L` literally.  \(\square\)

The suffix statement is only about this terminal cell.  The portal does not
by itself preserve deeper shadows, residence, other compiler pins, global
universality, or Hall; those are the finite collar and residual conditions
of Theorem 6.1.

## 8. Frozen `k=11 -> 13` audit and a local-event obstruction

The cyclic quotient lifetime histograms are

```text
k=11: 4^13 5^12 6^5 7^4 8^2 9 10^2 11 12 14
k=13: 4^33 5^23 6^16 7^17 8^9 9^10 10^8 11 12
      13^8 14^2 15 16^2 18
```

and the zero-gap histograms are

```text
k=11: 1^4 2^5 3^10 4^4 5^6 6^2 7^2 8^4 10 12^2 14^2
k=13: 1^9 2^23 3^17 4^13 5^21 6^7 7^8 8^8 9^5 10^3
      11^4 12 13^3 14 15 16 18^2 20 22 23^2 28
```

Both factors have minimum lifetime four and minimum gap one.  Thus they pass
the depth-three lower residence used by their literal compilers but fail
full positive dual-gap residence.  In the frozen audit their expected-rank
upper target supports at depths `q=2,3` nevertheless remain complete; dual
gap is not a necessary condition for those finite support statements.

There is a sharper obstruction to a small row-local `k=11 -> 13` event
inheritance.  For an oriented quotient factor, let `H(ell,g)` count a one-run
of length `ell` paired with its following zero-gap `g`.  Reversal preserves
`ell` but pairs it with the formerly preceding gap.

Since

\[
 \operatorname{Cat}_6=132=3\operatorname{Cat}_5+6,  \tag{8.1}
\]

compare the child with three independently oriented intact `k=11` sheets
plus six inserted quotient run-pairs.  The allowed symmetries here are cyclic
phase, coordinate relabelling, independent parent-sheet orientation, and
independent orientation of the two child components.  Phase and coordinate
relabelling do not change `(ell,g)`.  Minimizing over the number `t` of
reversed parent sheets and the two child orientations gives the exact `L^1`
table

\[
\begin{array}{c|rrrr}
t&(0,0)&(0,1)&(1,0)&(1,1)\\ \hline
0&170&174&162&168\\
1&158&162&146&154\\
2&156&162&146&154\\
3&168&172&160&166.
\end{array}                                          \tag{8.2}
\]

### Proposition 8.1 (three-sheet local-event no-go)

In this restricted model at least 70 of the 126 retained parent run-pair
**labels** fail to coincide with child labels as a multiset.  Equivalently,
the two multisets have intersection size at most 56.

#### Proof

The minimum distance in (8.2) is 146.  If `M` of the 126 source multiset
entries are outside a maximum source-child multiset intersection, then the
child has `M+6` unmatched entries because its total is 132.  Hence

\[
 146\le2M+6,
\]

so `M>=70`.  Equivalently the maximum multiset intersection is

\[
 \frac{126+132-146}{2}=56.                           \tag{8.3}
\]

This is a multiset `(ell,g)` obstruction, not identification of 70 physical
`(alpha,beta)` events or a cut bound.  It excludes only three intact oriented
sheets plus six inserted run-pairs.  Complement, facet/union transforms,
sheet fragmentation, the nonuniform four-sector lift, a four-sheet/delete
scheme, and global alternating correction are outside its scope.

The canonical one-core Hall graphs imported from the hash-bound port artifact
pass separately:

```text
k=11: 231/231
k=13: 1092/1092.
```

They do not inject.  Each of the eleven old singleton targets has six
candidate columns at `k=11`, giving 66 old incidences, while every singleton
has degree one at `k=13`.  Under a literal old-coordinate/column injection,
at most eleven old incidences survive, so at least `11*(6-1)=55` disappear.
The two new singleton rows bring the child total to 13, a net drop of 53 from
the old total.  This is scoped to the canonical cores and literal injection;
it is not a Hall deficiency, since the rebuilt child graph passes.  Event
histograms alone therefore cannot carry compiler ownership.

The frozen `k=13` splice is the positive finite portal:

\[
 2515\to2395:(7,3),\qquad2167\to2391:(5,8)
\]

are replaced by

\[
 2515\to2391:(7,2).                                  \tag{8.4}
\]

The first old and new edges share lower colour 2387.  The second displayed
closure occurrence has colour 2135 and is removed.  In `answers/k13.word`,
2135 occurs once, as the final source letter, and in none of its first three
OR derivatives; moreover

\[
 48\vee2161\vee2147\vee2135=2167.                  \tag{8.5}
\]

Thus Theorem 7.1 is realized literally.  Its suffix legality remains an
endpoint fact of this artifact, not a generic selector rule.

## 9. Frozen `k=13 -> 14` validation

The odd-to-even child is exactly a six-piece braid of the copied `k=13`
carrier and its facet chart, after the audited relabelling and invariant
recovery.  Its oriented piece lengths are

\[
 419, 3, 270, 966, 1027, 747,                  \tag{9.1}
\]

and its five new events are

\[
 (0,13),(13,3),(12,13),(13,2),(11,13)               \tag{9.2}
\]

at positions

\[
 418,421,691,1657,2684.                              \tag{9.3}
\]

The distinguished coordinate therefore has one-runs `3,966,747` and
internal zero-gaps `270,1027`.  The length-three ear is exactly the
depth-two threshold.  Its unique forward depth-two erosion window starts at
middle position 419; the same window is the backward envelope ending at
controller position 421, and the actual source letter there is the singleton

\[
                         \{13\}=8192.                \tag{9.4}
\]

The facet transform sends every source lifetime `ell` to `ell-1`; in the
recovered uncut facet factor the 429 physical source runs of length four
become 429 runs of length three.  Three are cut by the displayed `B`-piece
boundaries, so 426 remain wholly internal to the three retained `B` pieces;
the final six-piece path has 427 internal old-coordinate one-runs of length
three after its cross seams are included.  This is the exact event
explanation for the successful compiler-depth drop `3 -> 2`.

All piece-internal flags are governed by Theorem 3.1.  The only targets with
no witness wholly inside one of the six pieces are

```text
lower q2: 2374,2404,2852
lower q3: 2596
upper q2: 10718
upper q3: none.
```

Their listed seam windows in the frozen audit supply the missing
occurrences.  The literal word `answers/k14.word` covers all 16,383 nonempty
masks.

The braid is not dual-gap resident.  Among its internal old-coordinate
zero-gaps there are exactly

\[
 117\text{ of length }1,\qquad415\text{ of length }2. \tag{9.5}
\]

The coarse coordinate-count form of Theorem 6.2 forces at least

\[
 \left\lceil\frac{117+415}{14}\right\rceil=38      \tag{9.6}
\]

cuts in any pure piece rethreading which makes this path depth-two
dual-gap resident.  The copied `k=13` source path already has 415 internal
gaps of length at most two, forcing

\[
 \left\lceil\frac{415}{13}\right\rceil=32.          \tag{9.7}
\]

Theorem 6.3 gives the exact inherited-gap hitting numbers.  Greedy
earliest-right-end interval stabbing on all closed short-gap edge spans gives

\[
 \tau_{k=13}=260,\qquad \tau_{k=14}=351.             \tag{9.8}
\]

Thus every pure piece rethreading which removes all inherited depth-two
short gaps uses at least 260 old cuts for the `k=13` path and at least 351 for
the `k=14` path.  These are necessary, not sufficient, because new joins may
create new short gaps.  The actual `A` shore is cut into only three pieces,
so the six-piece construction cannot possibly be such a dual-gap router.
This is consistent with the exact upper ledger: there are 117
rank-deficient upper-`q=2` windows, yet every rank-nine target is covered by
other expected-rank windows.

Thus `k=13 -> 14` validates the facet transducer, protected shadow seams, and
an artifact-specific literal compiler.  It simultaneously refutes any claim
that the same braid preserves full dual-gap residence.

## 10. Reproduction and precise remaining gate

The new solver-free audit is

```text
scratch/audit_ad_pascal_event_stream_braid_20260729.py
scratch/ad_pascal_event_stream_braid_20260729.audit.json
```

Their SHA-256 values are

```text
748faa01190d57b27ebe44ff0bb3006a83510657df83cdba5e4d8a814ee4c032  scratch/audit_ad_pascal_event_stream_braid_20260729.py
6904894bf1a013d2b0d625acd4715b13d4ae137ea780d54baed21f60a0c3ef38  scratch/ad_pascal_event_stream_braid_20260729.audit.json
```

It checks, without removable assertions and identically under `python` and
`python -O`:

* all frozen input hashes;
* the `k=11` and `k=13` cyclic event/run-pair tables in both orientations;
* the complete 16-entry distance table (8.2);
* the facet event and run/gap identities, its tower identities for every
  physical `k=13` position at `q=0,...,12`, and the corresponding union
  identities and inverse shift on the strict `k=13` facet rows;
* algebraic four-sector ribbon fixtures at gaps `1,2,5` (not membership in a
  particular Catalan leave selection or a complete ribbon histogram);
* the common-deletion portal and terminal restitution;
* all five `k=14` seam events, the seam-exclusive target lists, the
  singleton ear, the coarse cut bounds, and the exact interval-transversal
  bounds `260,351`; and
* literal interval coverage of all nonempty masks at `k=11,13,14`.

The remaining theorem is not a marginal balance statement.  At each new
dimension one must choose the Pascal pieces and seams so that, simultaneously,

1. both event queues pass on every collar;
2. every required lower and upper target has a protected internal or named
   collar occurrence;
3. the two shifted parent compiler packages exist, including the auxiliary
   empty-core port for the new singleton;
4. every cross-seam core equation holds; and
5. the residual physical Hall graph matches all targets displaced from
   invalidated or promoted columns, using only positions left free by retained
   matches.

Theorems 2.1--7.1 prove that this signature composes and that its local
verification is finite for fixed depths.  Their all-depth identities are
proved algebraically; the regression checks both towers only through `q=12`.
The theorems do not prove that an accepting signature exists in every
dimension.  The frozen
`k=11 -> 13` run-pair distance and the exact `k=13 -> 14` short-gap
transversals show that any successful all-depth recursion must include a
genuinely nonlocal event refresh, not merely the known local Pascal triangles
or a bounded number of intact inherited-sheet insertions.

No SAT/CP solver, exhaustive carrier search, web access, or heavy local job
was used in this work; the regression is a solver-free identity and frozen-
artifact audit.
