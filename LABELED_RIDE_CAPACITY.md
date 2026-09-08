# Labeled capacities for windmill rides

## 1. Outcome

This note audits and develops the labeled-capacity proposal in Section 8b of
`fable_general_case/FABLE_GENERAL_CASE_WORK.md`.

There are two rigorous conclusions.

First, a generic per-entry target capacity strong enough to sum ride by ride
does **not** exist.  In an `h`-rank slab, one entry achieving one prescribed
coordinate can participate in as many as

\[
                         h(2a+1)                    \tag{1.1}
\]

distinct targets.  A literal contiguous portal gadget attains

\[
                h(2a+1)-{h(h+1)\over2}=\Theta(ah), \tag{1.2}
\]

and realizes all those targets with only `O(a)` word positions.  For
`h=Theta(a)`, one capped position therefore multiplexes `Theta(a^2)` targets.
This also essentially saturates the fan-capped theorem: at each right
endpoint the targets form one chain of size at most `h`, and there are
`Theta(a)` right endpoints.

Second, the “fresh head/fresh tail” observation does have an exact global
form.  It produces a bipartite compatibility graph `Gamma` on ride
transitions.  If a chosen disjoint ride decomposition has `R` rides and
`Q=M-R` internal ride transitions, then every realization satisfies

\[
              \boxed{D\ge M-2R-\nu(\Gamma).}        \tag{1.3}
\]

Equivalently, if the Hall deficiency of `Gamma` is `Delta=Q-nu(Gamma)`, then

\[
                              D\ge\Delta-R.          \tag{1.4}
\]

Thus a uniform `Delta=Omega(a^2)` theorem would prove the desired quadratic
defect whenever `R=O(a)`.

However, a completely explicit pair of legal, delay-`a`, factorable A-turn
rides matches `a-1` fresh tail requirements from the first ride to `a-1`
fresh head requirements in the second.  The nominal linear defect of one
ride is exported into and absorbed by the next ride.  Hence summing the
two-chain lower bound independently over rides is invalid.  The remaining
problem is now precise:

> Prove a quadratic Hall deficiency in the global head-tail graph, or prove
> a contamination/separation theorem preventing the portal arms of
> `Theta(a)` ride levels from being shared.

Caps and local achievements alone cannot do either.

## 2. Setting and the cap lemma

Work in the product lattice

\[
                         P_a=[0,2a]^3
\]

with coordinatewise maximum as join and middle rank `3a`.  Select one
middle witness

\[
                  I_i=[\ell_i,r_i],\qquad 1\le i\le M,
\]

for each middle target `T_i`, in increasing endpoint order.  Write

\[
 \ell_i=i+\alpha_i,\qquad r_i=i+\beta_i,
 \qquad 0\le\alpha_i\le\beta_i\le D,
 \qquad N=M+D.
\]

Both offset sequences are nondecreasing.

Lemma G from the Fable handoff is correct.  At most `D` physical positions
are contained in no selected interval.  At every other position,

\[
 G_p:=\bigwedge_{i:p\in I_i}T_i,
 \qquad A_p\le G_p.                                \tag{2.1}
\]

The first assertion follows from the telescoping hole count

\[
 \alpha_1+\sum_i\max(0,\alpha_{i+1}-\beta_i)
       +(D-\beta_M)\le D.
\]

The second is coordinatewise: every entry of a join witness for `T_i` is
at most `T_i`.

For a target `U`, say that position `p` **achieves coordinate `c`** when

\[
                         A_p(c)=U(c).
\]

Every witness for `U` contains an achievement for each of the three
coordinates.  An entry can achieve several coordinates of one target and
can be reused by many different target intervals.

## 3. Uniform capacity of a fixed label set

For `1<=h<=3a`, put

\[
 \mathcal F_h=\{U\in P_a:3a-h\le\rho(U)\le3a-1\}.
\]

Fix an entry value `b` and a nonempty coordinate subset `C`.  Let

\[
 \operatorname{Ach}_C(b)=
 \{U\in\mathcal F_h:b\le U,\ U(c)=b(c)\text{ for every }c\in C\}.
\]

### Lemma 1 (label-set capacity)

Uniformly in `b`,

\[
 |\operatorname{Ach}_C(b)|\le
 \begin{cases}
   h(2a+1),&|C|=1,\\
   h,&|C|=2,\\
   1,&|C|=3.
 \end{cases}                                      \tag{3.1}
\]

#### Proof

Fix one of the `h` possible target ranks.  If one coordinate is prescribed,
the other two must have a prescribed sum.  There are at most `2a+1`
bounded nonnegative solutions.  If two coordinates are prescribed, the
rank determines the third coordinate uniquely.  If all three are
prescribed, the target itself is fixed.  Summing over the slab ranks proves
(3.1).  Lower bounds `U>=b` and coordinate upper bounds can only reduce the
count.  \(\square\)

The first line is the relevant danger.  It is quadratic when `h=Theta(a)`;
the fact that `b<=G_p` does not improve it, because an entry may be sparse in
the two coordinates it is not being asked to achieve.

The displayed bounds are uniform but not constant-sharp.  For `1<=h<=a`,
the exact maximum with one prescribed coordinate is

\[
 h(2a+1)-\left\lfloor{h^2\over4}\right\rfloor,       \tag{3.2}
\]

obtained by centering `h` consecutive coefficients of the triangular
two-coordinate rank distribution.  With two prescribed coordinates the
exact uniform maximum is `min(h,2a+1)`.  These refinements do not change the
quadratic-capacity obstruction used below.

## 4. A sharp contiguous portal counterexample

The quadratic single-label capacity is real.  Consider the word

\[
 \begin{aligned}
 &(0,2a,0),(0,2a-1,0),\ldots,(0,1,0),\\
 &\hspace{38mm}p=(a,0,0),\\
 &(0,0,1),(0,0,2),\ldots,(0,0,2a).
 \end{aligned}                                    \tag{4.1}
\]

For every `0<=y,z<=2a`, the interval beginning at `(0,y,0)` (or at `p`
when `y=0`) and ending at `(0,0,z)` (or at `p` when `z=0`) has join

\[
                             (a,y,z).               \tag{4.2}
\]

Thus one portal position `p` achieves the `x` coordinate of all
`(2a+1)^2` targets in this two-dimensional face.
The same entry is legal under every cap `G_p>=(a,0,0)`, including a mixed
ride cap whose frozen `x` component is `a`; large cross-coordinate caps are
not needed at the portal itself.

Restrict to the slab targets of ranks `3a-q`, `1<=q<=h<=a`.  They satisfy

\[
                             y+z=2a-q.
\]

For a fixed `q` there are `2a-q+1` choices.  Hence the one portal is reused
by exactly

\[
 \sum_{q=1}^h(2a-q+1)
 =h(2a+1)-{h(h+1)\over2}                           \tag{4.3}
\]

distinct near-middle targets.  The entire family is realized by a word of
only `4a+1` positions.

At a fixed right-arm endpoint `z`, moving the left endpoint outward makes
the joins `(a,y,z)` into one inclusion chain.  The slab contributes at most
`h` members of that chain.  Summing over the `Theta(a)` right endpoints is
exactly the `Theta(ah)` behavior in (4.3).  Therefore this gadget is also a
sharp model for why the fan cap cannot be improved by assigning a uniform
small capacity to the shared portal entry.

Consequences:

* one free position from Lemma G is not one unit of labeled capacity;
* even `O(a)` free portals can carry `Theta(a^3)` coordinate-target
  incidences;
* contiguity by itself does not prevent the multiplexing; and
* a successful theorem must couple several ride levels or several endpoint
  fans, rather than count achievements independently.

## 5. Fresh achievements on a directed ride

Now suppose a selected middle subsequence is partitioned into disjoint
consecutive **rides**.  On one ride a coordinate `c` is constant and the two
cross coordinates are strictly monotone in opposite directions.  Shared
boundary points can be assigned to either neighbouring ride; this changes
all counts by at most `O(R)`.

Consider an internal transition `i -> i+1` of a ride.  Let `u_i` be the
cross coordinate which increases and `d_i` the one which decreases:

\[
 T_{i+1}(u_i)>T_i(u_i),\qquad
 T_{i+1}(d_i)<T_i(d_i).                            \tag{5.1}
\]

The value `T_(i+1)(u_i)` must be achieved somewhere in `I_(i+1)`.  It
cannot be achieved in `I_i`, because every entry there has `u_i` coordinate
at most `T_i(u_i)`.  Hence there is a **tail achievement** in

\[
 \mathcal Q_i:=I_{i+1}\setminus I_i
   \subseteq [r_i+1,r_{i+1}].                      \tag{5.2}
\]

Similarly `T_i(d_i)` must be achieved at a **head achievement** in

\[
 \mathcal H_i:=I_i\setminus I_{i+1}
   \subseteq [\ell_i,\ell_{i+1}-1].                \tag{5.3}
\]

The regions `\mathcal H_i` are pairwise disjoint as `i` varies, and the
regions `\mathcal Q_i` are pairwise disjoint.  Therefore chosen head
achievement positions are all distinct, chosen tail achievement positions
are all distinct, and the only possible saving is to make one physical
position serve one head and one tail simultaneously.

This statement uses actual set differences, so fresh achievements are
covered positions.  The at-most-`D` free positions in Lemma G cannot serve
these middle fresh demands.

## 6. The exact head-tail compatibility graph

Let `E_R` be the set of transitions internal to the chosen ride
decomposition.  If the rides partition all `M` middle targets and their
number is `R`, then

\[
                             Q:=|E_R|=M-R.           \tag{6.1}
\]

Make a bipartite graph `Gamma` with a head copy and a tail copy of `E_R`.
Join head transition `i` to tail transition `k` when there is a position

\[
               p\in\mathcal H_i\cap\mathcal Q_k    \tag{6.2}
\]

at which the two labels are cap-compatible.  Explicitly:

* if `d_i != u_k`, require
  \[
  T_i(d_i)\le G_p(d_i),\qquad
  T_{k+1}(u_k)\le G_p(u_k);
  \]
* if `d_i=u_k`, require those two requested values to be equal and at most
  `G_p(d_i)`.

These conditions are exactly the existence of some product-lattice entry
`b<=G_p` achieving both labels: when the coordinates differ, set the third
coordinate to zero.

### Theorem 2 (fresh-demand matching bound)

Every word realizing the selected middle witnesses satisfies

\[
                            N\ge2Q-\nu(\Gamma),      \tag{6.3}
\]

and therefore

\[
             \boxed{D\ge M-2R-\nu(\Gamma).}         \tag{6.4}
\]

#### Proof

Choose one head and one tail achievement for every transition in `E_R`.
The `Q` head positions are distinct by (5.3), and the `Q` tail positions are
distinct by (5.2).  Whenever a head and a tail use the same physical
position, their transitions form an edge of `Gamma`.  No transition can
participate in two such identifications, so the shared positions form a
matching.  There are at most `nu(Gamma)` of them.  The union of the two
position families therefore has size at least `2Q-nu(Gamma)` and lies in a
word of length `N`.  Substitute `Q=M-R` and `N=M+D`.  \(\square\)

Let

\[
 \Delta(\Gamma)=Q-\nu(\Gamma)
 =\max_{S\subseteq E_R}(|S|-|N_\Gamma(S)|)          \tag{6.5}
\]

be its Hall deficiency.  Equation (6.4) becomes

\[
                              D\ge\Delta(\Gamma)-R. \tag{6.6}
\]

This is the exact labeled gate promised in the handoff.  In a windmill with
`R=O(a)`, a uniform quadratic Hall deficiency would immediately force
`D=Omega(a^2)`.

## 7. Why independent per-ride defects cannot be summed

The compatibility graph can match fresh requirements across a turn.  The
following legal factorable example makes the sharing explicit.

Take the middle sequence

\[
 \begin{aligned}
 X_j&=(a,j,2a-j),&&0\le j\le a,\\
 Y_s&=(a-s,a,a+s),&&1\le s\le a,
 \end{aligned}                                    \tag{7.1}
\]

in the displayed order.  The first ride fixes `x=a`, increases `y`, and
decreases `z`; the second fixes `y=a`, decreases `x`, and increases `z`.
They form an A turn at `(a,a,a)`.

Index the `M=2a+1` targets consecutively and prescribe fixed-delay witnesses

\[
                         I_i=[i,i+a].               \tag{7.2}
\]

The word length is `M+a`.  This central row is factorable.  For every
coordinate threshold, the `x` superlevel set is a prefix, the `y` superlevel
set is a suffix, and the `z` superlevel set is a union of a prefix and a
suffix.  Hence no threshold incidence word has a strictly internal 1-run;
the fixed-delay run criterion is satisfied.  Therefore the coordinatewise
maximal factor

\[
 G_p=\bigwedge_{i:p\in I_i}T_i                    \tag{7.3}
\]

satisfies

\[
                   \bigvee_{p=i}^{i+a}G_p=T_i
                   \qquad(1\le i\le M).
\]

For the `X_j -> X_(j+1)` transition, put `i=j+1`.  Its new tail position is

\[
                         p=i+a+1.
\]

For `0<=j<=a-2`, this same physical position is the removed head position
of the transition beginning at `Y_(j+1)`.  The selected windows containing
`p` run from `X_(j+1)` through `Y_(j+1)`, and their meet has

\[
 G_p(y)=j+1,qquad G_p(x)=a-j-1.                   \tag{7.4}
\]

Thus the single maximal-factor entry `G_p` simultaneously achieves

```text
the fresh y=j+1 tail label from the X ride,
the fresh x=a-j-1 head label from the Y ride.
```

This supplies `a-1` pairwise disjoint matching edges across the ride turn.
Almost the whole nominal boundary loss of one ride is absorbed by the next.
A three-direction windmill may plausibly continue the same mechanism around
successive A turns, but the displayed two-ride construction does not prove
that global continuation.

Therefore the fresh middle-label statement “one ride needs a linear number
of distinct head and tail positions” is not additive.  Its arm positions are
precisely positions which the next ride can reuse.  This does not yet refute
an additive theorem that also uses the complete family of below-middle
targets; those witnesses were not constructed in this example.

## 8. Relation to below-middle target realization

The portal gadget and Theorem 2 expose two different kinds of multiplexing.

1. **Within a ride level.**  A fixed-coordinate portal supplies one label to
   `Theta(a^2)` slab targets; two monotone arms supply the other labels.
   This is the actual two-chain box mechanism behind the local linear cost.

2. **Across rides.**  A fresh arm position for one ride can be the opposite
   fresh arm position for the next ride.  The cap is the mixed meet of the
   two endpoint-monotone portions, exactly as predicted in Section 8b of the
   Fable handoff.

Consequently none of the following proposed ledgers is valid:

```text
one target-coordinate achievement = one unit of position capacity;
one capped position = O(a) below-target capacity;
one local two-chain defect per ride, summed over rides.
```

The first two are refuted by (4.1)--(4.3); the third is refuted by
(7.1)--(7.4).

The fan-capped theorem remains fully compatible with both examples.  It
limits distinct target joins at one endpoint to a chain height, but it does
not prevent one portal or one arm entry from being reused across many
endpoints.

## 9. Precise remaining theorem alternatives

There are now two mathematically sharp routes.

### Route A: global Hall deficiency

For every all-long-max windmill witness system with `R=O(a)`, prove

\[
 \max_{S\subseteq E_R}
       (|S|-|N_\Gamma(S)|)\ge\delta a^2            \tag{9.1}
\]

for an absolute `delta>0`.  Theorem 2 then gives `D=Omega(a^2)`.

The A-turn example shows that `S` cannot be chosen ride by ride.  It must
detect a global failure after the head-tail requirements have been routed
through several successive turns.

### Route B: portal-arm contamination

Suppose `Theta(a)` distinct ride levels each attempt to use a local portal
gadget like (4.1).  Prove that their two monotone arms cannot be shared with
subquadratic total length.  A contiguous interval using an `x=c` portal is
contaminated by every included portal with larger `x` value.  Thus multiple
levels require either duplication, a laminar separation of their witness
families, or additional transition entries.  A theorem quantifying this
separation by `Omega(a^2)` would close the same route even when `Gamma` has a
near-perfect matching.

This is genuinely stronger than Lemma G: `D` free entries may themselves be
highly multiplexed portals.

## 10. Final status

Proved here:

* the exact label-set capacity bounds (3.1);
* a contiguous construction attaining quadratic one-label multiplexing;
* the exact fresh-demand matching inequality (6.4)/(6.6); and
* an explicit legal factorable A-turn showing linear ride defects can be
  shared across rides.

Not proved:

* a universal quadratic Hall deficiency;
* a global portal-arm contamination theorem; or
* `D=Omega(a^2)` for every all-long-max order.

The labeled-capacity proposal therefore does not yet kill the windmill
branch, but it is no longer vague.  Its exact obstruction is the matching
deficiency (9.1), with portal-arm contamination as the alternative global
mechanism.
