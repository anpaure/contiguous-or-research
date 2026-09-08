# Facet prime-slope frames: a local `q`-amplifier and the global frame-packing gate

Date: 2026-08-02  
Status: unconditional local owner/target-simple construction and exact
conditional amplification theorem.  The global packing of sufficiently many
frames is isolated but not proved.  No handoff or research-index file is
changed by this note.

## 0. Outcome

Put

\[
 q=d+2,\qquad c=r-q+1=r-d-1,
 \qquad W=\binom{k}{r},                                  \tag{0.1}
\]

and assume `c>=1`.  One primitive facet absorber has a `q`-set of private
tags `V`, a `c`-core `C`, owner block

\[
                 \{C\cup(V-\{v\}):v\in V\},             \tag{0.2}
\]

and high targets `C union J`, where `J` runs through the `q` cyclic
`j`-intervals of an order on `V`, for every `2<=j<=q-2`.

The post-labeling obstruction in the companion facet note shows that
`Theta(k)` arbitrary owner-disjoint blocks over one common interval pool can
be unlabelable.  The result here gives the matching positive local scale.

Choose a prime `p>3` with

\[
                         p\le q-2,\qquad s=q-p\ge2.      \tag{0.3}
\]

On one common `p`-set, the nonzero slopes of `F_p`, modulo sign, give

\[
                         m={p-1\over2}                  \tag{0.4}
\]

pairwise owner- and target-simple facet absorbers.  Every high interval
which uses a private tag is automatically private to its block.  Every
remaining interval is a proper arithmetic progression in `F_p`; the
translation-invariant second moment

\[
             |S|\sum_{x\in S}x^2-\left(\sum_{x\in S}x\right)^2 \tag{0.5}
\]

recovers the progression slope up to sign.  Thus different slope classes
cannot collide.

Bertrand's theorem supplies `p=Theta(q)` satisfying (0.3) for all
sufficiently large `q`, and the complete frame uses at most

\[
                         c+q+{q^2\over8}                \tag{0.6}
\]

coordinate names.  This is below `k` in the canonical middle-level regime.
Hence one legal frame amplifies one common core into `Theta(q)` exact
primitive modules.

The remaining global statement is now precise:

> pack `Omega(W/q^3)` mutually resource-disjoint prime-slope frames.

Their union would contain `Omega(W/q^2)` pairwise owner- and target-simple
primitive facet absorbers, closing the current factor-`q` gap under this one
explicit spread hypothesis.  This note does not prove the frame packing.

## 1. The prime-slope frame

Fix a prime `p>3` and `s=q-p>=2`.  Choose disjoint coordinate sets

\[
 |C|=c,\qquad I=\mathbb F_p,
 \qquad X_{[a]}\quad([a]\in\mathbb F_p^*/\{\pm1\}),     \tag{1.1}
\]

where every private set `X_[a]` has size `s`, and all the `X_[a]` are
pairwise disjoint and disjoint from `C union I`.  There are
`m=(p-1)/2` sign classes.

For each class choose one representative `a` and put

\[
 V_a=I\ \dot\cup\ X_a,\qquad
 Z_a=C\ \dot\cup\ V_a.                                 \tag{1.2}
\]

Then `|V_a|=q`, `|Z_a|=c+q=r+1`, and the corresponding owner block is

\[
                         B_a=\{Z_a-\{v\}:v\in V_a\}.     \tag{1.3}
\]

Start from the directed arithmetic-progression cycle

\[
                         0,a,2a,\ldots,(p-1)a            \tag{1.4}
\]

on `I`.  It has `p` cyclic gaps.  Put two distinguished private tags
`w_a,h_a in X_a` into two nonadjacent gaps.  Here nonadjacent means that the
two gaps share no endpoint in the cycle (1.4).  Insert the other `s-2`
private tags arbitrarily, allowing several tags in one gap.  Call the
resulting oriented cyclic order on `V_a` `sigma_a`.

Finally, fix one point `beta in C`.  In block `a`, use

* `beta` as the deleted core point `b` of the primitive `P` source;
* `w_a` as the unique `P` tag; and
* `h_a` as the tag of the designated primitive `H` source.

Anchoring the cyclic order at `w_a` makes this a literal labeling of the
standard facet absorber.  The two tags are distinct because `s>=2`.

## 2. The modular second-moment invariant

For a nonempty set `S subseteq F_p` of size `j`, define

\[
                 \Phi(S)=j\sum_{x\in S}x^2
                         -\left(\sum_{x\in S}x\right)^2
                         \in\mathbb F_p.                 \tag{2.1}
\]

### Lemma 2.1 (translation invariance)

For every `z in F_p`,

\[
                         \Phi(S+z)=\Phi(S).              \tag{2.2}
\]

#### Proof

Write `A=sum_(x in S)x` and `B=sum_(x in S)x^2`.  Then

\[
\begin{aligned}
 \Phi(S+z)
 &=j(B+2zA+jz^2)-(A+jz)^2\\
 &=jB-A^2=\Phi(S).
\end{aligned}
\]

All calculations take place in `F_p`.  \(\square\)

### Lemma 2.2 (the moment recovers a proper progression step)

Let

\[
 S=\{x,x+a,\ldots,x+(j-1)a\}\subseteq\mathbb F_p,
 \qquad 2\le j\le p-2,                                  \tag{2.3}
\]

with `a!=0`.  Then

\[
                         \Phi(S)
 =a^2{j^2(j^2-1)\over12}.                               \tag{2.4}
\]

The coefficient multiplying `a^2` is nonzero in `F_p`.  Consequently, if
the same set `S` is also a length-`j` progression of nonzero step `b`, then

\[
                         b=\pm a.                        \tag{2.5}
\]

#### Proof

By Lemma 2.1 take `x=0`.  The integer identities

\[
 \sum_{t=0}^{j-1}t={j(j-1)\over2},\qquad
 \sum_{t=0}^{j-1}t^2={j(j-1)(2j-1)\over6}               \tag{2.6}
\]

give

\[
\begin{aligned}
 j\sum_{t=0}^{j-1}(ta)^2
 -\left(\sum_{t=0}^{j-1}ta\right)^2
 &=a^2\left[
 {j^2(j-1)(2j-1)\over6}
 -{j^2(j-1)^2\over4}\right]\\
 &=a^2{j^2(j-1)(j+1)\over12},
\end{aligned}
\]

which is (2.4).

Because `p>3`, the denominator `12` is invertible in `F_p`.  In the range
`2<=j<=p-2`, none of `j`, `j-1`, or `j+1` is zero modulo `p`.  Hence the
coefficient is nonzero.  Applying (2.4) with steps `a,b` gives `a^2=b^2`,
and the field identity `(a-b)(a+b)=0` proves (2.5).  \(\square\)

The exclusions at the two ends are necessary for this invariant: a
one-point set has no step, while a `(p-1)`-set is the complement of one
point and can be an interval in every slope order.  The high deck starts at
size two, and the gap placement in Section 1 excludes an `I`-only interval
of size `p-1`.

## 3. Why the inserted gaps give only proper progressions

### Lemma 3.1 (range of an `I`-only interval)

Every cyclic interval of `sigma_a` which is contained wholly in `I` and has
size at least two has size at most `p-2`.  It is therefore a progression of
the form (2.3) in step `a` within the range of Lemma 2.2.

#### Proof

Deleting the private tags from `sigma_a` recovers (1.4).  Hence any
`I`-only interval lies inside one run of consecutive entries of (1.4)
between occupied gaps and is an arithmetic progression of step `a`.

Index the gaps cyclically by `0,1,...,p-1`, with gap `i` following the
`i`th entry of (1.4).  If the two occupied gaps have cyclic gap-distance
`e`, nonadjacency says

\[
                         2\le e\le p-2.
\]

The two complementary `I`-runs consequently have sizes `e` and `p-e`, so
both have size at most `p-2`.  Inserting further private tags can only split
runs and decrease this maximum.  \(\square\)

Equivalently, the two nonadjacent occupied gaps break the `p`-cycle into at
least two nonempty `I`-runs, neither of which is all of `I` minus a single
point.  This is exactly the endpoint condition required in Lemma 2.2.

## 4. Exact owner and target simplicity

### Theorem 4.1 (prime-slope frame theorem)

The `m=(p-1)/2` labeled facet absorbers constructed in Section 1 have
pairwise distinct owners and pairwise distinct emitted named targets at
every rank `c,c+1,...,r-1`.

#### Proof

**Owners.**  An owner in block `a` is `C union (V_a-{v})`.  Since
`|X_a|=s>=2`, it contains at least `s-1>=1` coordinates of `X_a`.  It
contains no coordinate of `X_b` for a different slope class `[b]`.
Therefore an owner from block `a` cannot equal an owner from block `b`.
Owners inside one block are distinct facets of `Z_a`.

**High targets which meet a private set.**  At rank `c+j`, `2<=j<=q-2`,
a target in block `a` is

\[
                         C\cup J,                        \tag{4.1}
\]

where `J` is a cyclic `j`-interval of `sigma_a`.  If `J` meets `X_a`, the
target contains a coordinate which belongs to no other `X_b`, and hence it
cannot equal a target from another block.

**High targets contained in `C union I`.**  Otherwise `J subseteq I`.
Lemma 3.1 makes it a progression of some length `2<=j<=p-2` and step `a`.
If a target from block `b` were equal, its interval also could not meet
`X_b`, because all private sets are disjoint from `C union I`.  Equality
after removing the common core `C` would therefore make the same `j`-set a
progression of steps `a` and `b`.  Lemma 2.2 gives `b=\pm a`, so `[a]=[b]`.
Thus two different slope blocks cannot collide.  Within one block, distinct
cyclic intervals of one fixed proper length give distinct target sets, as
in the standard facet-absorber construction.

**Rank `c`.**  The unique low target in block `a` is

\[
                         (C-\{\beta\})+\{w_a\}.          \tag{4.2}
\]

The tags `w_a` lie in pairwise disjoint private sets, so these targets are
distinct.

**Rank `c+1`.**  The unique target is

\[
                         C+\{h_a\}.                      \tag{4.3}
\]

Again the private tags distinguish the blocks.  The two low targets are
legal because `w_a!=h_a`; targets at different ranks are different resource
species.  This proves every row.  \(\square\)

The theorem simultaneously chooses the owner blocks and all cyclic orders.
It is not a post-labeling argument for an arbitrary owner matching.

## 5. Prime choice and the canonical coordinate budget

### Lemma 5.1 (a linear-size prime choice)

For every sufficiently large `q`, there is a prime `p>3` satisfying

\[
                         {q\over3}-1<p<{2q\over3},       \tag{5.1}
\]

and hence (0.3), with

\[
                         m={p-1\over2}=\Theta(q).        \tag{5.2}
\]

#### Proof

Put `n=floor(q/3)`.  For large `q`, `n>3`.  Bertrand's theorem gives a prime
`p` with `n<p<2n`.  Therefore `p>q/3-1` and `p<2q/3`.  In particular
`q-p>q/3>=2` eventually, so `p<=q-2` and (0.3) holds.  Equation (5.2) is
immediate.  \(\square\)

This is the only external number-theoretic input.  Any comparable prime-gap
statement would suffice.

### Lemma 5.2 (frame coordinate budget)

One complete frame uses

\[
                         c+p+ms                          \tag{5.3}
\]

distinct coordinate names.  Moreover,

\[
                         p+ms
 \le q+{q^2\over8}.                                     \tag{5.4}
\]

For the canonical middle-level parameters this is at most `k-c` for all
sufficiently large `k`, so the frame embeds in `[k]`.

#### Proof

The sets in (1.1) are disjoint, giving (5.3).  Since `m=(p-1)/2` and
`s=q-p`,

\[
 p+ms=p+{(p-1)(q-p)\over2}
       \le q+{p(q-p)\over2}
       \le q+{q^2\over8},                               \tag{5.5}
\]

where the last inequality is the maximum of `x(q-x)`.

Now `k-c=(k-r)+q-1`.  Put `a=k-r`; in the middle-level regime
`a>=r-1`.  The corrected pull-clock estimate gives
`q=d+2<=ceil(sqrt(r))+2`, and hence `q^2<=8(a-1)` for all sufficiently
large `r`.  Consequently

\[
 q+{q^2\over8}\le q+a-1=k-c,                            \tag{5.6}
\]

proving the claim.  \(\square\)

The asymptotically sharper relation `q^2/r -> pi/4` leaves a large constant
margin, but is not needed for (5.6).

## 6. The exact factor-`q` amplification

Call the complete data

\[
             {\cal F}=(C,\beta,I,(X_a,\sigma_a,w_a,h_a)_{[a]}) \tag{6.1}
\]

a prime-slope frame.  Its resource deck is the union of all rank-`r` owners
and all named targets emitted by its `m` modules.  By Theorem 4.1, its exact
per-rank deck sizes are

\[
\begin{array}{c|c}
\text{resource rank}&\text{number in one frame}\\ \hline
r&mq\\
c&m\\
c+1&m\\
c+j,\quad 2\le j\le q-2&mq.
\end{array}                                                   \tag{6.2}
\]

Thus the deck has `m(q^2-2q+2)` resources in total.  Two frames are
resource-disjoint if their rank-`r` owner decks are disjoint and their
target decks are disjoint separately at every target rank.  This does not
require the coordinate supports of the two frames to be disjoint.

### Corollary 6.1 (frame-packing amplification)

Suppose the canonical owner/target atlas contains `F` pairwise
resource-disjoint prime-slope frames.  Then it contains

\[
                         F{p-1\over2}                   \tag{6.3}
\]

pairwise owner- and target-simple primitive facet absorbers.  In particular,
if

\[
                         F\ge\gamma {W\over q^3}        \tag{6.4}
\]

for a fixed `gamma>0`, then the number of modules is

\[
                         \Omega\left({W\over q^2}\right). \tag{6.5}
\]

Any smaller prescribed number can be obtained by discarding surplus
modules.

#### Proof

Theorem 4.1 gives `(p-1)/2` mutually resource-disjoint modules inside each
frame.  Resource-disjointness between frames lets us take their union.
Lemma 5.1 gives `(p-1)/2=Omega(q)`, so (6.4) implies (6.5).  Removing modules
cannot create a collision.  \(\square\)

Thus the exact remaining global theorem is:

> **Prime-slope frame-packing theorem.**  For the canonical primitive
> inventory, the facet owner/target atlas contains `Omega(W/q^3)` mutually
> resource-disjoint prime-slope frames, with protected/preused resources
> deleted in advance.

This is a matching problem on frames whose hyperedges already contain
`Theta(q)` complete primitive modules.  It is strictly more structured than
the false operation of labeling an arbitrary owner matching after the fact.
Proving it would close the factor-`q` gap from the current
`Theta(W/q^3)` individual-module scale to `Theta(W/q^2)` modules.

## 7. Independent checks and boundary

The second-moment proof was checked independently in two ways.

1. Expanding (2.1) after translation cancels the linear and quadratic
   translation terms exactly, giving Lemma 2.1.
2. Exhaustive enumeration for every prime `5<=p<=43`, every
   `2<=j<=p-2`, and all slope classes found that no `j`-set is a cyclic
   arithmetic-progression interval for two slopes not related by sign.  It
   also confirms algebraically that

   \[
        j\sum_{t=0}^{j-1}t^2-\left(\sum_{t=0}^{j-1}t\right)^2
        ={j^2(j^2-1)\over12}.
   \]

These finite checks are audits, not dependencies of Theorem 4.1.

### 7.1 Exact comparison with the pointed-flag contraction

Write one module order as `sigma=(v_0,...,v_(q-1))`, with indices modulo
`q`.  Its pointed flag starting at `u` is the nested chain

\[
 {\mathfrak f}_u=
 \left(C\cup\{v_u,\ldots,v_{u+j-1}\}\right)_{j=2}^{q-2}
 < C\cup(V-\{v_{u-1}\}).                              \tag{7.1}
\]

The `q` flags in

\[
                         E(C,V,\sigma)
 =\{{\mathfrak f}_u:u\in\mathbb Z/q\mathbb Z\}         \tag{7.2}
\]

partition the module's high-target and owner deck: a cyclic interval has a
unique starting point, and the last entry of `f_u` is the owner which omits
`v_(u-1)`.  Thus a module is exactly one `q`-edge of the
pointed-flag hypergraph.  The `m` module edges in a prime-slope frame form a
matching under the stronger resource-sharing conflict relation, by Theorem
4.1.  The two low ranks are not vertices of this contraction; their
disjointness is supplied separately by `w_a,h_a`.

For completeness, the degree and maximum pair codegree of the unlabelled
pointed-flag hypergraph follow directly from (7.1).  A fixed flag is
completed by choosing and ordering the two tags inside its bottom
`(c+2)`-set, then choosing the omitted predecessor outside its rank-`r`
owner.  Hence

\[
 D=2\binom{c+2}{2}(k-r)=(c+2)(c+1)(k-r).              \tag{7.3}
\]

For two compatible flags at adjacent starts, their bottom sets intersect
in `C` plus their one common tag.  Choosing that tag gives `c+1`
completions, after which both chains determine the whole cyclic order.  At
nonadjacent starts the two bottom tag pairs are disjoint, so their
intersection determines `C` and there is at most one completion.  Therefore

\[
                         \Delta_2=c+1,qquad
 {q^2\Delta_2\over D}={q^2\over(c+2)(k-r)}\longrightarrow0.    \tag{7.4}
\]

This favorable local ratio does **not** prove the frame-packing statement
in Section 6.  It controls completions of one unrestricted module edge.
A frame is a correlated matching of `m=Theta(q)` such edges with a common
`(C,I)`, arithmetic-progression slopes, disjoint private sets, and fixed low
labels.  Moreover, distinct pointed-flag vertices may still share one of
their constituent named resources, which is an additional conflict
relation.  A global proof therefore still needs either degree/codegree and
robustness estimates for whole frame patterns, or a growing-uniformity
conflict-free nibble which preserves these correlations and the low ranks.
No such implication is asserted here.

The scope is deliberately local.  The theorem does not prove the global
frame packing, reserve `d` short buffers for each primitive, place other
rotor packages, fuse cycle components, or supply upper shadows, residence,
protected pins, and the compiler cap.  It proves that the known common-core
collision is sharp in order and that a correlated prime-slope choice gains
the missing local factor `Theta(q)` without any owner or named-target loss.

## 8. Dependencies

The facet absorber and its exact target deck are in
`MATH_THEOREM_OFHT_EXACT_CYCLE_HYPERGRAPH_FUNCTIONAL_HALL_AND_POINTED_FACE_20260801.md`
and
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`.
The star-decomposition reduction, exact labeling loads/codegrees,
common-core overload cut, and independent-label LLL obstruction are in
`MATH_THEOREM_FACET_ABSORBER_MIXED_STAR_DECOMPOSITION_AND_TARGET_COLLISION_GATE_20260802.md`.
The corrected primitive-and-buffer ledger, including the genuine
`Theta(W/q^2)` feasibility ceiling, is in
`MATH_THEOREM_FACET_MODULE_LEDGER_AND_WEIGHTED_JOINT_GREEDY_SPREAD_20260802.md`.
