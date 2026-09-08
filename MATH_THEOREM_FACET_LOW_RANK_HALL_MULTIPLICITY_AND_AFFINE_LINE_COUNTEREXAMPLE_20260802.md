# Facet low ranks: exact conditional Hall, sharp multiplicity, and affine-line counterexamples

Date: 2026-08-02  
Status: exact low-label criterion, robust sufficient multiplicity theorem,
and explicit owner/high-simple counterexamples.  This note is conditional on
an already selected owner/high-simple facet-module packing.  It makes no
claim about constructing that high packing.

## 0. Outcome

Fix `q>=4` and `c>=1`.  For every selected module `i`, let

\[
 |C_i|=c,\qquad |V_i|=q,\qquad C_i\cap V_i=\varnothing,       \tag{0.1}
\]

and let `sigma_i` be its oriented cyclic order on `V_i`.  Assume all
rank-`r` owners and all high targets at ranks
`c+2,...,r-1` are already globally distinct, where `r=c+q-1`.  Explicitly,
writing `sigma_i=(v_(i,0),...,v_(i,q-1))` with indices modulo `q`, these
resources are

\[
 O_{i,v}=C_i\cup(V_i-\{v\}),\qquad
 T_{i,u,j}=C_i\cup\{v_{i,u},\ldots,v_{i,u+j-1}\}
 \quad(2\le j\le q-2).
\]

The remaining low labels are

\[
 H_i=C_i\cup\{h_i\},\qquad
 P_i=(C_i-\{b_i\})\cup\{w_i\},                              \tag{0.2}
\]

where `b_i in C_i` and `w_i,h_i in V_i` with `w_i!=h_i`.

There is an exact two-stage Hall theorem.  First choose distinct `H_i`.
After those choices, ordinary Hall on the remaining `P` menus is necessary
and sufficient.  In particular, put

\[
\begin{aligned}
 \Delta_H&=\max_Y\#\{i:Y=C_i\cup\{h\}\text{ for some }h\in V_i\},\\
 \Delta_P&=\max_X\#\{i:X=(C_i-\{b\})\cup\{w\}
                         \text{ for some }b\in C_i,w\in V_i\}.
\end{aligned}                                                  \tag{0.3}
\]

The clean multiplicity conditions

\[
                         \Delta_H\le q,qquad
                         \Delta_P\le c(q-1)                   \tag{0.4}
\]

guarantee a complete low labeling.  The first threshold is sharp even
inside the owner/high-simple facet class.

High simplicity does not imply (0.4).  It gives only

\[
 \Delta_H\le\left\lfloor{k-c-1\over2}\right\rfloor,
 \qquad
 \Delta_P\le\left\lfloor{1\over2}\binom{k-c}{2}\right\rfloor. \tag{0.5}
\]

Canonically these bounds have orders `r` and `r^2`, whereas the sufficient
thresholds have orders `q=Theta(sqrt(r))` and
`cq=Theta(r^(3/2))`.

There are two exact counterexamples.

1. For every prime-power `q>=4`, all affine lines of `F_q^2`, placed over
   one common core, give `q(q+1)` owner/high-simple modules but only `q^2`
   possible rank-`(c+1)` targets.  Every such target has multiplicity
   exactly `q+1`.
2. At `q=4`, twelve explicitly listed edge-disjoint four-cycles on eleven
   common tags already give the same failure.  This is minimal by tag-union
   size and module count among common-core `q=4` systems.

Thus scalar ledger feasibility plus owner/high simplicity does **not** make
the two low rows automatic.

## 1. Candidate systems

Let `M` be the selected module index set.  Define the rank-`(c+1)` menu

\[
                         {\cal H}_i
 =\{C_i\cup\{h\}:h\in V_i\}.                                \tag{1.1}
\]

For a fixed choice `h in V_i`, define the compatible rank-`c` menu

\[
 {\cal P}_i(h)
 =\{(C_i-\{b\})\cup\{w\}:b\in C_i,
                              w\in V_i-\{h\}\}.               \tag{1.2}
\]

It is also convenient to use the unrestricted menu

\[
 {\cal P}_i^*
 =\{(C_i-\{b\})\cup\{w\}:b\in C_i,
                              w\in V_i\}.                      \tag{1.3}
\]

### Lemma 1.1 (menu sizes and unique recovery)

For every module `i`,

\[
 |{\cal H}_i|=q,\qquad |{\cal P}_i(h)|=c(q-1),
 \qquad |{\cal P}_i^*|=cq.                                   \tag{1.4}
\]

Moreover, a member of `mathcal H_i` uniquely determines `h`, and a member
of `mathcal P_i^*` uniquely determines its ordered pair `(b,w)`.

#### Proof

The map `h -> C_i union {h}` is injective because `V_i` is disjoint from
`C_i`.  If

\[
                         X=(C_i-\{b\})\cup\{w\},              \tag{1.5}
\]

then

\[
                         C_i-X=\{b\},\qquad X-C_i=\{w\}.      \tag{1.6}
\]

Thus `(b,w)` is recovered from `X`, and all displayed menu sizes follow.
\(\square\)

## 2. Exact Hall and Rado form

### Theorem 2.1 (exact conditional low-label theorem)

A complete low labeling exists if and only if there are choices
`h_i in V_i`, `i in M`, such that

1. the targets `C_i union {h_i}` are pairwise distinct; and
2. for every `J subseteq M`,

   \[
    \left|\bigcup_{i\in J}{\cal P}_i(h_i)\right|\ge |J|.      \tag{2.1}
   \]

#### Proof

Every complete labeling supplies the choices in item 1.  Its distinct
rank-`c` targets are representatives from the menus in (1.2), so Hall's
necessary inequalities give (2.1).

Conversely, item 1 fixes globally distinct rank-`(c+1)` targets.  Condition
(2.1) is precisely Hall's theorem for the family
`(mathcal P_i(h_i))_(i in M)`, so it supplies distinct representatives
`P_i`.  Lemma 1.1 uniquely recovers `(b_i,w_i)` from `P_i`; membership in
`mathcal P_i(h_i)` gives `w_i!=h_i`.  The two target ranks are different
resource species, so no cross-rank collision is relevant.  \(\square\)

The same statement has the standard Rado form.  If admissible targets at
either low rank must additionally be independent in a matroid, replace the
cardinality of each union by its matroid rank.  For a fixed first-stage
choice `(h_i)`, Rado's theorem makes those rank inequalities necessary and
sufficient.  Ordinary global distinctness is the free-matroid, hence Hall,
special case.  A forbidden or preused bank is handled exactly by deleting
its elements from the menus before applying the theorem.

### Corollary 2.2 (robust multiplicity criterion)

With `Delta_H,Delta_P` as in (0.3), condition (0.4) implies a complete low
labeling.

#### Proof

For `J subseteq M`, count incidences between `J` and its rank-`(c+1)`
candidate union.  Lemma 1.1 and the definition of `Delta_H` give

\[
 q|J|=\sum_Y\#\{i\in J:Y\in{\cal H}_i\}
       \le\Delta_H\left|\bigcup_{i\in J}{\cal H}_i\right|
       \le q\left|\bigcup_{i\in J}{\cal H}_i\right|.         \tag{2.2}
\]

Thus the `mathcal H_i` satisfy Hall, and we may choose distinct targets,
equivalently tags `h_i`.

Now every restricted menu has size `c(q-1)`.  Since
`mathcal P_i(h_i) subseteq mathcal P_i^*`, every rank-`c` target occurs in
at most `Delta_P` restricted menus.  Hence, for every `J`,

\[
 c(q-1)|J|
 \le\Delta_P\left|\bigcup_{i\in J}{\cal P}_i(h_i)\right|
 \le c(q-1)\left|\bigcup_{i\in J}{\cal P}_i(h_i)\right|.      \tag{2.3}
\]

This is (2.1), so Theorem 2.1 finishes the labeling.  \(\square\)

The two numerical thresholds in the proof are the exact left degrees of
the relevant candidate systems.  Section 4 shows that increasing the first
one from `q` to `q+1` is impossible even with owner/high simplicity.

## 3. What high simplicity actually controls

Only the rank-`(c+2)` part of high simplicity is needed for the following
bounds.

### Proposition 3.1 (automatic low-menu multiplicity bounds)

Every owner/high-simple module packing satisfies (0.5).

#### Proof

Fix a rank-`(c+1)` target `Y`.  For every module counted by `mu_H(Y)`, there
is a unique tag `h` with `Y=C_i union {h}`.  Let `x^-` and `x^+` be the two
cyclic neighbours of `h` in `sigma_i`.  They are distinct because `q>=4`.
That module emits the two rank-`(c+2)` targets

\[
                         Y\cup\{x^-\},\qquad Y\cup\{x^+\}.    \tag{3.1}
\]

All `2mu_H(Y)` targets in (3.1) are globally distinct by high simplicity.
There are only `k-(c+1)` rank-`(c+2)` supersets of `Y`, proving the first
bound in (0.5).

Now fix a rank-`c` target `X`.  In every module counted by `mu_P(X)`, Lemma
1.1 gives unique tags `b,w` such that

\[
                         X=(C_i-\{b\})\cup\{w\}.              \tag{3.2}
\]

If `x^-` and `x^+` are the cyclic neighbours of `w`, the module emits

\[
                 X\cup\{b,x^-\},\qquad X\cup\{b,x^+\}.       \tag{3.3}
\]

The two added points in each set are distinct and outside `X`.  Again all
`2mu_P(X)` targets in (3.3) are distinct by high simplicity.  The number of
rank-`(c+2)` supersets of `X` is `binom(k-c,2)`, proving the second bound.
\(\square\)

In the canonical regime, `k-c=Theta(r)`, `c=Theta(r)`, and
`q=Theta(sqrt(r))`.  Proposition 3.1 therefore misses both sufficient
thresholds in (0.4) by a polynomial factor.  This mismatch alone would not
disprove automatic low labeling; the next two sections do.

## 4. Infinite sharp family from affine lines

### Theorem 4.1 (affine-line low-target obstruction)

Let `q>=4` be a prime power, let `U=F_q^2`, and let `mathcal L` be the set of
all affine lines in `U`.  Fix a `c`-set `C` disjoint from `U`.  For every
`L in mathcal L`, choose an arbitrary oriented cyclic order `sigma_L` on
`L` and form the module `(C,L,sigma_L)`.

These `q(q+1)` modules are owner-simple and high-target-simple, but they
have no globally distinct rank-`(c+1)` labeling.  Moreover,

\[
                         \Delta_H=\Delta_P=q+1.              \tag{4.1}
\]

#### Proof

The affine plane has `q^2` points, `q(q+1)` lines, `q` points on every
line, at most one common point between distinct lines, and `q+1` lines
through every point.

An owner from line `L` has the form `C union (L-{x})`.  If owners from
distinct lines `L,L'` were equal, then `L` and `L'` would share the common
`(q-1)`-set left after the deletions.  Since `q-1>=3`, this contradicts the
at-most-one intersection property.  Owners inside one module are plainly
distinct.

At high rank `c+j`, `2<=j<=q-2`, equality of two targets would, after
removing the common core, give a common `j`-set contained in both lines.
This is impossible for distinct lines because `j>=2`.  Within one line,
the proper cyclic `j`-intervals have distinct starting points and are
distinct sets.  Thus the packing is high-target-simple.

The rank-`(c+1)` menu of line `L` is

\[
                         {\cal H}_L=\{C\cup\{x\}:x\in L\}.    \tag{4.2}
\]

The union of all these menus has only `q^2` targets, one per point of `U`,
whereas there are `q(q+1)>q^2` modules.  Hall fails on the whole line set.
Finally, each point lies on exactly `q+1` lines, so every target in (4.2)
has multiplicity `q+1`.  With the common core fixed, an unrestricted
rank-`c` candidate is uniquely indexed by a pair `(b,x) in C times U` and
occurs precisely in the lines through `x`.  Its multiplicity is also
`q+1`, proving (4.1).  In particular, when `c>=2`,
`Delta_P=q+1<=c(q-1)`: only the first condition in (0.4) fails.  \(\square\)

The construction uses `c+q^2` coordinate names and therefore embeds
whenever `k-c>=q^2`.  Its role is local: any independent primitive/buffer
ledger still has to admit the chosen number of modules.

## 5. A smallest common-core `q=4` obstruction

The affine-plane family is uniform and infinite.  The following smaller
instance freezes an explicit first obstruction in the common-core
four-cycle class.

Take

\[
 q=4,qquad c=5,qquad r=8,qquad k=16,                       \tag{5.1}
\]

fix a five-set `C`, and put `U={0,1,...,10}` on the other eleven
coordinates.  Use the following oriented four-cycles; their vertex sets are
the `V_i`:

\[
\begin{array}{rrrr}
(1,7,10,8),&(0,5,9,8),&(2,8,3,10),&(4,6,5,10),\\
(0,6,1,10),&(0,2,5,3),&(2,3,9,7),&(1,4,7,5),\\
(0,1,9,4),&(1,2,4,3),&(0,7,6,9),&(3,6,8,7).
\end{array}                                                   \tag{5.2}
\]

### Proposition 5.1 (exact twelve-on-eleven counterexample)

The twelve modules in (5.2) are owner-simple and high-target-simple, but
their rank-`6` menus have no system of distinct representatives.  Their
rank-`6` multiplicities, in point order `0,1,...,10`, are

\[
                         (5,5,4,5,4,4,4,5,4,4,4),             \tag{5.3}
\]

so `Delta_H=5=q+1`.

#### Proof

Expanding the consecutive edges in (5.2) gives every edge of `K_11` except

\[
 \{45,58,84\}\ \dot\cup\ \{26,6\,10,10\,9,92\},             \tag{5.4}
\]

which are respectively a triangle and a four-cycle.  Thus the twelve
four-cycles use `48` pairwise distinct edges.  At `q=4`, the only high rank
is `c+2=7`, and its four targets in a module are `C` plus the four cycle
edges.  They are therefore globally distinct.

If two owner blocks shared an owner, their two tag sets would share a
three-set.  Deleting the fourth vertex from a four-cycle leaves a two-edge
path on that three-set.  Two two-edge paths in the same triangle share an
edge, contradicting the edge-disjointness just proved.  Hence the owners
are also globally distinct.

Every possible rank-`6` target is `C union {x}` for some `x in U`.  There
are only eleven such targets for twelve modules, so Hall fails.  Counting
the occurrences of each point in (5.2) gives (5.3).  A rank-`5` candidate
is indexed by `(b,x) in C times U` and has the same point multiplicity, so
`Delta_P=5<=c(q-1)=15`.  Thus only the sharp `Delta_H` condition fails.
\(\square\)

Here concatenation in (5.4) denotes an unordered edge: for example `45`
means `{4,5}` and `6 10` means `{6,10}`.

### Proposition 5.2 (minimality in the common-core four-cycle class)

Let `t` common-core `q=4` modules have high-simple cycles on a tag union of
size `n`.  If their rank-`(c+1)` menus violate Hall on all `t` modules, then
`n>=11` and `t>=12`.  The construction (5.2) attains both bounds.

#### Proof

For a common core, high simplicity at rank `c+2` says exactly that the
four cycle edges of different modules are disjoint.  Hence

\[
                         4t\le\binom n2.                      \tag{5.5}
\]

The union of the low menus has size exactly `n`, so failure on the whole
family requires `t>n`.  For `n<=9`, (5.5) gives `t<=n`.

If `n=10`, then `t>n` and (5.5) force `t=11`.  The eleven cycles would use
`44` of the `45` edges of `K_10`, leaving one edge.  An edge-disjoint union
of cycles has even degree at every vertex.  But `K_10` minus one edge has
odd degree at the eight vertices not incident with the omitted edge, a
contradiction.  Thus `n>=11`, and then `t>n` gives `t>=12`.  Proposition
5.1 supplies equality.  \(\square\)

This is a scoped minimality statement; it does not claim minimality among
systems with varying cores or with `q>4`.

## 6. Scalar-ledger audit and exact boundary

The obstruction is not a shortage of global named resources.  In the
instance (5.1),

\[
\begin{array}{c|c|c}
\text{row}&\text{use}&\text{ambient capacity}\\ \hline
\text{rank-}8\text{ owners}&48&\binom{16}{8}=12870\\
\text{rank-}7\text{ high targets}&48&\binom{16}{7}=11440\\
\text{rank-}6\text{ low targets}&12&\binom{16}{6}=8008\\
\text{rank-}5\text{ low targets}&12&\binom{16}{5}=4368.
\end{array}                                                   \tag{6.1}
\]

With `d=q-2=2`, the separated primitive-coordinate values are

\[
 A_{d+1}=\binom{16}{5}-\binom{16}{4}=2548,
 \qquad
 A_{d-1}=\binom{16}{7}-\binom{16}{6}=3432.                   \tag{6.2}
\]

Thus `t=12<=A_(d+1)`, `(q-1)t=36<=A_(d-1)`, and
`qt=48<=binom(16,7)`.  The separate short-buffer row is `dt=24<=L-H` and
must still be supplied by whatever primitive inventory produced the module
packing.  Conditional on that independent row, every scalar ledger
inequality is slack while the low Hall row fails.

The conclusions of this note are exactly these:

* Theorem 2.1 is a necessary-and-sufficient low-label criterion after an
  owner/high packing has been fixed.
* Corollary 2.2 is a robust sufficient multiplicity certificate.
* High simplicity alone does not supply that certificate and does not make
  the low ranks automatic.
* The affine and twelve-on-eleven examples obstruct only the low labeling;
  they do not refute a high-packing theorem which simultaneously controls
  low menus, such as the private-tag prime-slope frame construction.

No owner/high module packing, buffer reservation, other rotor package,
component fusion, upper shadow, residence, protected interface, or compiler
claim is made here.

## 7. Dependencies

The facet target deck and the independent owner/high packing boundary are
recorded in
`MATH_THEOREM_FACET_MODULE_LEDGER_AND_WEIGHTED_JOINT_GREEDY_SPREAD_20260802.md`.
The local private-tag construction which controls both low ranks by design
is in
`MATH_THEOREM_FACET_PRIME_SLOPE_FRAME_Q_AMPLIFIER_20260802.md`.
The pointed-flag nibble scope audit is in
`MATH_AUDIT_FACET_POINTED_FLAG_GROWING_NIBBLE_AND_CONFLICT_BARRIER_20260802.md`.
