# Clean facet geodesics give paired backups with literal polynomial source halos

**Date:** 2026-08-13  
**Method:** a fresh geodesic on the lower shore, complementation, monotone
coordinate words, and a stopped random-greedy halo packing; no computation
or finite search  
**Status:** unconditional local paired backup and local source-halo theorem.
For the inverse-fan profile with `d^2=O(R)`, polynomially many such halos
pack in the application-relevant order with sub-half exposure and therefore
extend to a simple middle-levels two-factor.  The order is load-bearing at
depth two: those `O(d)` packages are selected before the `O(dR)` long-path
bank.  The theorem does not make the unprotected completion resident,
connect the completed factor, select the deep payload atlas, or supply the
typed terminal router.

## 1. Why the old whiskers are not a resident block

Work on a ground set of size

\[
                             n=2R-1.
\tag{1.1}
\]

Let `S` have rank `R-q`, put `Z=[n]\setminus S`, and write

\[
                             q=s+1.
\tag{1.2}
\]

In the complement-paired whiskered package of
`MATH_THEOREM_COMPLEMENT_PAIRED_BACKUP_AND_PAYLOAD_UPPER_BRIDGE_20260806.md`,
the lower vertices on the upper-witness side are

\[
                 L_-,L_0,\ldots,L_{s-1},L_+.
\tag{1.3}
\]

The whisker coordinate `c` is absent from `L_-` and `L_+` and present in
every internal `L_i`.  Consequently its word on the complementary owner
path is

\[
                             1\,0^s\,1.
\tag{1.4}
\]

Thus the complementary intersection path has an internally trapped zero
gap of length

\[
                             s=q-1.
\tag{1.5}
\]

For `q<=d` this gap is shorter than `d+1`.  No arm attached outside the
path can lengthen a gap which is already bounded at both ends inside the
path.  Therefore the old whiskered package is a correct graph-level paired
backup, but its complementary path is not itself a valid fixed block for a
depth-`d` resident-halo argument.

## 2. The clean facet-geodesic package

Assume

\[
                             1\le q\le R-1.
\tag{2.1}
\]

Choose a rank-`(R-1)` set `L_0\subset Z`.  Then

\[
                             I=Z\setminus L_0
\tag{2.2}
\]

has rank `q`.  Choose a rank-`q` set `D\subset L_0`, and order

\[
 D=(d_1,\ldots,d_q),\qquad I=(i_1,\ldots,i_q).
\tag{2.3}
\]

Put

\[
 L_j=(L_0-\{d_1,\ldots,d_j\})
          \cup\{i_1,\ldots,i_j\},
 \qquad 0\le j\le q,
\tag{2.4}
\]

and, for `1<=j<=q`,

\[
                             A_j=L_{j-1}\cup L_j.
\tag{2.5}
\]

Every `L_j` has rank `R-1`, every `A_j` has rank `R`, and

\[
 L_0-A_1-L_1-A_2-\cdots-A_q-L_q
\tag{2.6}
\]

is an incidence path.  Complement it and write

\[
 W_j=[n]\setminus L_j,\qquad
 F_j=[n]\setminus A_j.
\tag{2.7}
\]

Then

\[
 W_0-F_1-W_1-F_2-\cdots-F_q-W_q
\tag{2.8}
\]

is a second incidence path.

### Theorem 2.1 (clean paired backup)

The two paths `(2.6)` and `(2.8)` are simple and resource-disjoint, and

\[
                 \bigcup_{j=1}^{q}A_j=Z,
 \qquad          \bigcap_{j=0}^{q}W_j=S.
\tag{2.9}
\]

Moreover every coordinate word on either owner path has at most one state
transition.  In particular neither owner path contains an internally
bounded nonconstant positive run or zero gap.

#### Proof

The sequence `(L_j)` is a fresh Johnson geodesic: each `d_j` is deleted
once and each `i_j` is inserted once.  Hence all `L_j`, all intervening
owners `A_j`, and their complements are simple.

Since `A_1` contains all of `L_0`, while each `i_j` belongs to `A_j`,

\[
 \bigcup_j A_j=L_0\cup I=Z.
\]

De Morgan's law gives

\[
 \bigcap_j W_j=[n]\setminus\bigcup_jL_j
               =[n]\setminus Z=S.
\]

Every original resource in `(2.6)` is a subset of `Z`.  Every
complementary resource of the same rank contains the nonempty set `S`.
Thus no resource occurs in both paths.

Put `C=L_0\setminus D`.  On the complementary owner sequence
`W_0,\ldots,W_q`, the coordinate words are

\[
\begin{array}{c|c}
x\in S&1^{q+1}\\
d_t\in D&0^t1^{q+1-t}\\
i_t\in I&1^t0^{q+1-t}\\
x\in C&0^{q+1}.
\end{array}
\tag{2.10}
\]

On `A_1,\ldots,A_q`, the `d_t` words are prefixes, the `i_t` words are
suffixes, and the remaining words are constant.  Hence every word on
either path is constant, `0^*1^*`, or `1^*0^*`.  This proves the final
claim. \(\square\)

The case `q=2` is included.  Thus the separate small-stratum exception in
the whiskered formulation is not intrinsic; it arose only because that
formulation was indexed by upper excess `s=q-1>=2`.

## 3. A literal monotone source halo

Let the required source depth be `d`, assume `q<=d`, and put

\[
                             \ell=d+1.
\tag{3.1}
\]

First collar the complementary intersection path `(W_0,\ldots,W_q)`.
Recall `C=L_0\setminus D`, so

\[
 |S|=R-q,\qquad |C|=R-q-1.
\tag{3.2}
\]

Assume

\[
                         R-q-1\ge2\ell.
\tag{3.3}
\]

Choose disjoint ordered sets

\[
 D^-,D^+\subset S,qquad |D^-|=|D^+|=\ell,
\tag{3.4}
\]

and disjoint ordered sets

\[
 I^-,I^+\subset C,qquad |I^-|=|I^+|=\ell.
\tag{3.5}
\]

From `W_0`, take an outward fresh geodesic which successively exchanges
the ordered `D^-` bank for the ordered `I^-` bank.  From `W_q`, take the
analogous outward geodesic using `D^+,I^+`.  Orient the first arm toward
`W_0`, traverse `W_0,\ldots,W_q`, and orient the second arm away from
`W_q`.

### Theorem 3.1 (flag-convex source halo)

The resulting owner path has the following properties.

1. Every coordinate word is constant, `0^*1^*`, or `1^*0^*`.
   Therefore the halo has no internally bounded nonconstant positive run
   and no internally bounded nonconstant zero gap.
2. The central `q+1` owners still have intersection `S`.
3. If, on the complete owner trace containing this protected path, one
   defines the maximal candidate antecedent
   
   \[
                       P_t=\bigcap_{a=0}^{d}T_{t-a},
   \tag{3.6}
   \]
   
   then the protected source interval
   
   \[
                       P_{i+q},P_{i+q+1},\ldots,P_{i+d}
   \tag{3.7}
   \]
   
   has width `d-q+1` and exact union `S`, where
   `T_i,\ldots,T_{i+q}=W_0,\ldots,W_q`.

The identity in item 3 is independent of every exterior completion beyond
the two length-`d+1` arms.

#### Proof

A coordinate in `D^-` has word `0^*1^*` on the whole collared path,
because it is inserted on the left arm and, by disjointness, is never
deleted on the right arm.  A coordinate in `D^+` has the dual word
`1^*0^*`.  Coordinates in `I^-` and `I^+` have the opposite two monotone
words.  Equation `(2.10)` gives the same property for the central active
coordinates, and all remaining coordinates are constant.  This proves
item 1; item 2 is Theorem 2.1.

For every `q<=h<=d`, the owner window defining `P_(i+h)` contains all of
`T_i,\ldots,T_(i+q)`.  Hence

\[
                 \bigcup_{h=q}^{d}P_{i+h}\subseteq S.
\tag{3.8}
\]

Conversely, let `x\in S`.  If `x\notin D^+`, then `x` is present from
`T_i` through the entire right arm, so `x\in P_(i+d)`.  If `x\in D^+`,
then `x\notin D^-` and it is present through the entire left arm and
through `T_(i+q)`, so `x\in P_(i+q)`.  The arms have length `d+1`, hence
both displayed windows are internal to the protected halo.  This proves
the reverse inclusion in `(3.8)` and item 3. \(\square\)

Thus the large target `S` never has to occur as one literal source letter.
The short owner intersection, together with its monotone halo, already
materializes the required source cell.  This is exactly what fails in the
partition collar `W_S`: there the attempted common bank has rank `q<d`
and cannot be split into `d` nonempty letters.

## 4. The upper-witness path has the same halo

The owner path `A_1,\ldots,A_q` in `(2.6)` is saturated at its two ends by
the endpoint lower vertices `L_0,L_q`.  Continuing through `L_0` forces
the first outward exchange to delete `i_1`; continuing through `L_q`
forces the first outward exchange to delete `d_q`.

Assume

\[
                         R-q-1\ge2d,qquad R-q\ge2(d+1).
\tag{4.1}
\]

Choose disjoint `(d)`-sets `K^-,K^+\subset C` and disjoint
`(d+1)`-sets `J^-,J^+\subset S`.  Use outward deletion banks

\[
                         \{i_1\}\cup K^-,qquad
                         \{d_q\}\cup K^+
\tag{4.2}
\]

and insertion banks `J^-,J^+`, putting the forced exchanges through
`L_0,L_q` first.

### Corollary 4.1 (paired flag-convex halo)

Both incidence paths in the clean paired package admit length-`d+1`
halos which preserve every central owner, lower facet, and the upper union
`Z`, and on which every coordinate word is monotone.  The two halos are
mutually owner/lower-resource disjoint.  The only flags not closed inside
one halo are clipped at its two far ports.

#### Proof

The two deletion banks in `(4.2)` are disjoint.  The inserted banks are
disjoint and consist of coordinates absent from every central `A_j`.
The same coordinate-word check as in Theorem 3.1 applies.  The forced
first exchanges use exactly the already protected endpoint facets
`L_0,L_q`, so no central incidence is changed.  Every owner of the
intersection halo has at least `R-q-(d+1)` coordinates in `S`, whereas
every owner of the upper-witness halo has at most `d+1` coordinates in
`S`.  Under `(4.3)` the first number is larger than the second; the same
rank-one comparison separates their lower facets.  Thus the two halos do
not meet. \(\square\)

For `q<=d`, all inequalities in Sections 3--4 hold once

\[
                             R\ge3d+3.
\tag{4.3}
\]

## 5. Polynomially many halos pack

The following is the simultaneous form needed by the low-spine inverse
fan.  Use the all-occurrence exposures

\[
 \alpha(P)=\max_x|\{U\in V(P)\cap{[n]\choose R}:x\subset U\}|,
\tag{5.1}
\]

\[
 \beta(P)=\max_U|\{x\in V(P)\cap{[n]\choose R-1}:x\subset U\}|.
\tag{5.2}
\]

### Theorem 5.1 (ordered polynomial source-halo packing)

Suppose

\[
 d^2=O(R),\qquad d=o(R),
\tag{5.3}
\]

and, for `2<=q<=d`, a multiset `mathcal D_q` of targets of rank `R-q`
satisfies

\[
                         |\mathcal D_q|\le C_0dq
\tag{5.4}
\]

for an absolute constant `C_0`.  Let `P_end` be a fixed endpoint bank of
size and exposure `O(d)`.  Then:

1. the depth-two targets admit mutually resource-disjoint clean packages
   and all four halos while avoiding `P_end`; call their union `H_2`;
2. after this choice, let `P_0` be any protected path forest containing
   `P_end union H_2` with
   
   \[
                |V(P_0)|=O(dR),\qquad
                \alpha(P_0),\beta(P_0)=O(d);
   \tag{5.5}
   \]
   
   (in the PBBS application, the long low-spine bridges are selected in
   this intermediate step); and
3. all targets of depths `3<=q<=d` then admit mutually
   resource-disjoint clean paired packages and four halos avoiding `P_0`.

The resulting total bank `P` is a path forest and

\[
                         \alpha(P),\beta(P)<R/3.
\tag{5.6}
\]

The total protected incidence size is

\[
 O\!\left(d\sum_{q=2}^{d}|\mathcal D_q|\right)
                         =O(d^4)=O(R^2).
\tag{5.7}
\]

Consequently the polynomial protected-factor theorem extends `P` to a
simple spanning middle-levels two-factor.  In every such extension, each
target retains its paired proper-upper witness.  On the maximal candidate
word of either orientation of the completed factor, `(3.7)` is a literal
protected interval of value `S`.  If the completed owner trace is
`d`-resident, this candidate word is its valid maximal antecedent, so the
interval is an actual compiler cell.

#### Proof

### Step 1: depth two

There are `O(d)` depth-two tasks.  Select all their central packages first.
For one fixed target, the smallest relevant resource orbit has size
`R+1`; fewer than `O(d)=o(R)` resources have been used when the next
central package is selected.  Hence greedy stabilizer avoidance works,
including repeated occurrences of the same target.

Now add the four arms of every selected package.  At any intermediate
owner, the permitted deletion and insertion banks have size `R-O(d)`.
The complete depth-two bank has only `O(d)` components, and one fresh
geodesic contributes at most two units to any exposure row.  Thus its
eventual exposure is `O(d)`.  Greedily choose each next facet and owner:
only `O(d)` facets below the current owner and `O(d)` owners above the
chosen facet are already forbidden.  This gives `Omega(R^2)` legal fresh
ordered exchanges at every step.  It constructs `H_2`, with

\[
 |V(H_2)|=O(d^2)=O(R),\qquad
 \alpha(H_2),\beta(H_2)=O(d).
\tag{5.8}
\]

This is why the order in the theorem is necessary.  A general
`O(dR)` bank can occupy all `R+1` rank-`R` resources inside one depth-two
upper target while still having `o(R)` exposure.

### Step 2: the central packages at depths at least three

Process depths increasingly.  For a target at depth `q`, choose the fresh
facet geodesic uniformly from its stabilizer orbit and reject choices
meeting the already selected bank.  At a fixed role the four kinds of
central resources are uniform on

\[
 {Z\choose R},\quad {Z\choose R-1},\quad
 \{S\cup Q:|Q|=q\},\quad
 \{S\cup Q:|Q|=q-1\}.
\tag{5.9}
\]

The smallest of these orbits has size

\[
                         {R+q-1\choose q-1}.
\tag{5.10}
\]

At `q=3` this is `Theta(R^2)`, whereas the initial bank has
`O(dR)=O(R^(3/2))` resources.  Only the central packages are selected in
this step; their arms are postponed to Step 3.  Before depth `q` their
total resource bank has size

\[
 O\!\left(\sum_{t<q}t|\mathcal D_t|\right)
                         =O(dq^3).
\tag{5.11}
\]

For `q=3`, `(5.11)=O(d)`; for every larger `q`, the denominator `(5.10)`
grows by another factor `Omega(R/q)`.  A union bound over the `O(q)` roles
therefore gives rejection probability `o(1)` uniformly.  Conditioning on
avoidance changes every one-role probability by `1+o(1)`.

For a fixed opposite-shore star, one role in `(5.9)` hits that star only
if it contains one prescribed `(q-1)`-set on the small side of the
target partition.  Consequently its probability is at most

\[
                         {q\over {R+q-1\choose q-1}}.
\tag{5.12}
\]

One clean paired package contributes at most four units to any exposure
row: a fresh geodesic meets a fixed star in at most two consecutive
resources, and there are two complementary paths.  Equations `(5.4)` and
`(5.12)` make the sum of the conditional means `o(1)`.  The exponential
supermartingale estimate for adaptively exposed bounded indicators gives

\[
 \Pr\bigl(\text{one central exposure increment}\ge R/100\bigr)
                         \le\exp\{-\Omega(R\log R)\}.
\tag{5.13}
\]

A union bound over the fewer than `2^(2R)` rows fixes mutually disjoint
central packages whose added exposure is below `R/100` on both shores.

### Step 3: all remaining halos

Condition on those central packages.  Expose every arm as a fresh
geodesic, choosing uniformly among the resource-legal exchanges, and stop
if either total exposure first reaches `R/10`.  Before stopping, fewer
than `R/10` facets below the current owner are used and fewer than `R/10`
owners above a proposed facet are used.  Since every permitted coordinate
bank has size `R-O(d)`, every ordinary step has `Omega(R^2)` legal ordered
exchanges.  At the first step of an upper-witness halo the endpoint facet
is prescribed, but at least `Omega(R)` new owners above it remain.  Thus
conditioning on avoidance multiplies the probability of any specified
deletion or insertion label by only an absolute factor.

We record the elementary conditional shell estimate used below.  Let

\[
 U_j=U_0-D_j+I_j
\tag{5.14}
\]

be a fresh arm, and let `x` have rank `R-1`.  Put

\[
 a=|U_0\setminus x|=|x\setminus U_0|+1.
\]

Then `x\subset U_j` is possible only at `j=a`; it requires all `a`
members of `U_0\setminus x` to be deleted and all `a-1` members of
`x\setminus U_0` to be inserted.  Hence, unless the first deletion is
one prescribed endpoint event,

\[
 \Pr(\exists j\ge1:x\subset U_j\mid\text{past})
             \le {C^a(a!)^2\over R^{2a-1}}.
\tag{5.15}
\]

For a fixed rank-`R` owner `Y`, put `a=|U_0\setminus Y|`.  Exclude the
prescribed endpoint facet when the first arm exchange reuses a central
facet; that resource was already counted in the central path and adds no
new `beta` load.  A **new** edge facet of the arm lies below `Y` only at
steps `a` or `a+1`.  If `a>=1`, the same counting gives conditional
probability at most

\[
                         {C^a(a!)^2\over R^{2a-1}}.
\tag{5.16}
\]

For a forced first endpoint exchange and `a=1`, a later new hit requires
the random first insertion to be the unique label in `Y-U_0`, and hence
has probability `O(1/R)`.  If `a=0`, only the endpoint facet can be
forced.  These estimates follow
by revealing the distinct event labels in order: at every reveal there
are at least `cR` legal choices, and the displayed containment requires
the stated prescribed deletion and insertion sets.  This proof remains
valid under the stopped avoidance process.

For an ordinary arm, `(5.15)` is `O(1/R)` when `x\subset U` and
`O(1/R^3)` otherwise.  A forced first endpoint exchange can add one owner
containing `x` deterministically, but only when its central endpoint
already contains `x`; hence the complete deterministic contribution of
all such steps is at most the central endpoint exposure `R/100+O(d)`.
If the forced first deletion is one of at least two labels required by
`x`, the remaining probability is `O(1/R^2)`.  The remaining conditional
means therefore sum to `O(1)`, because the central endpoint exposure is
`R/100+O(d)` and there are `O(d^3)=O(R^(3/2))` arms.

For a fixed rank-`R` row `U`, at most one arm starts at `U`.  Reused
endpoint facets contribute no new load.  An arm from another endpoint at
Johnson distance one adds a **new** facet below `U` with probability
`O(1/R)` by `(5.16)`; every more distant endpoint costs `O(1/R^3)`.
Hence the corresponding stopped conditional mean is

\[
                         O(d^3/R)=O(d).
\tag{5.17}
\]

A fresh arm meets one fixed exposure row in at most two consecutive
resources.  The conditional exponential-moment bound for these bounded
increments gives

\[
 \Pr\bigl(\text{one random added halo load}\ge R/100\bigr)
       \le \exp\{-\Omega(R\log(R/d))\}
       =\exp\{-\Omega(R\log R)\}.
\tag{5.18}
\]

Again union bound over all rows shows that the stopped process never
stops and that every halo can be selected resource-disjointly.  Combining
`(5.5)`, `(5.8)`, `(5.13)`, and `(5.18)`, including the deterministic
forced-endpoint charge just bounded, gives `(5.6)`.  The path count
and `(5.4)` give `(5.7)`.

The protected-factor theorem supplies the simple factor extension.  Every
window used in `(3.7)` lies strictly inside its protected halo, so the
extension cannot alter the local source identity or the central upper
witness.  Global validity of the maximal candidate word is exactly the
separate residence premise stated in the conclusion. \(\square\)

## 6. Exact consequence and remaining boundary

The clean package closes three problems at once for the shallow
inverse-fan leave:

1. it replaces the whiskered complementary path's trapped short zero gap
   by a fresh monotone path;
2. it includes the formerly exceptional depth-two stratum; and
3. it supplies a literal source cell of width `d-q+1` inside a protected
   full halo for every polynomially many lost target occurrences.

The theorem does **not** imply that the arbitrary edges used by the simple
factor completion are resident.  It proves only that every protected
block is internally flag-convex and that its designated source cell is
immune to the completion outside the halo.  A complete PBBS proof still
requires:

1. resident joining or rethreading of the unprotected completion;
2. the remote atlas and pinned-envelope Hall theorem for depths `q>d`;
3. preservation/opening of upper witnesses outside the paired named bank;
4. topology/fusion in the same occurrence state; and
5. the typed terminal suffix router.

The structural conclusion is

\[
 \boxed{
 \text{near-middle targets need no }d\text{-letter target collar:}
 \quad
 \text{a clean facet geodesic plus two monotone arms is a literal source
 halo}.}
\]
