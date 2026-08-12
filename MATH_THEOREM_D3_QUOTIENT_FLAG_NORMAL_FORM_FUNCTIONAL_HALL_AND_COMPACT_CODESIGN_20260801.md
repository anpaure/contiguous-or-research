# Depth-three quotient flags: normal form, functional Hall, and the compact co-design master

**Date:** 2026-08-01  
**Status:** unconditional exact reductions and finite negative calibrations.
The note characterizes the depth-three quotient state graph, isolates its
maximal ordinary-flow subclass, gives an exact co-design formulation smaller
than the current age master, and relates it to the chronology-first
two-matching picture and protected reset banks.  It does **not** prove the
remaining Hall/rainbow theorem.

## 0. Verdict

Let `n=2m+1`, distinguish coordinate `0`, and work modulo cyclic rotation.
Every orbit of depth-three all-high flags has a unique tail-normalized form

\[
                         f=(S,z),
 \tag{0.1}
\]

where

\[
 |S|=m-2,qquad 0,z\notin S,qquad z\ne0.
 \tag{0.2}
\]

It represents the literal flag

\[
                  S+\{0,z\}\supset S+\{0\}\supset S
 \tag{0.3}
\]

with deletion word `(z,0)`.

If a second flag `g` has head-normalized signature `(H,gamma)`, then the
exact state-zero turn law is

\[
 f\longrightarrow g
 \quad\Longleftrightarrow\quad
 S\subset H,quad \gamma\in S,quad z\notin H.
 \tag{0.4}
\]

Its owner is

\[
                         H\cup\{0,z\}.                         \tag{0.5}
\]

For fixed `g` and fixed owner extension `z`, its possible predecessors are
exactly

\[
                  (H-\{\beta\},z),
                  \qquad \beta\in H-\{\gamma\}.               \tag{0.6}
\]

Thus an owner attachment makes the remaining problem an ordinary bipartite
Hall problem.  The difficulty is selecting the flags and the attachment in
correlation.

For `k=17,m=8`, the exact unrestricted quotient co-design master has only

\[
 80,080\text{ flag options},\qquad
 4,324,320\text{ turn options}.                               \tag{0.7}
\]

The deterministic first lower factor fails unrestricted Hall with matching
`1010/1430`.  Adding the deterministic first upper containment bijection and
restricting to its functional core gives only `537/1430`.  Neither factor is
within bounded portal distance of feasibility.  Lower flags, representative
alignments, and the upper matching must be co-designed globally.

## 1. Unique normalized flag-orbit coordinates

Let a literal flag be

\[
                    q\supset q-\{a\}
                      \supset q-\{a,b\},                      \tag{1.1}
\]

with `a,b` distinct.  The middle action is free, so the complete flagged
object also has a free rotation orbit.  Rotate uniquely so that `b=0`, and
put

\[
                     z=a-b,qquad S=q-\{a,b\}                  \tag{1.2}
\]

in the rotated coordinates.  This gives (0.1)--(0.3).  Conversely every
pair satisfying (0.2) gives one flag orbit, so the representation is
bijective.

The complete option set is therefore

\[
 {cal F}={(S,z):z\in\mathbb Z_n-\{0\},
                  S\in\tbinom{\mathbb Z_n-\{0,z\}}{m-2}\}.    \tag{1.3}
\]

It has size

\[
 |{cal F}|=(n-1)\binom{n-2}{m-2}.                            \tag{1.4}
\]

For one fixed root necklace `[Q]`, there are exactly `m(m-1)` options:
choose one of the `m` translates of `[Q]` containing zero and then choose
`z` among its other `m-1` elements.  Algebraically,

\[
 {|{cal F}|\over \binom nm/n}=m(m-1).                        \tag{1.5}
\]

The resources offered by `f=(S,z)` are

\[
 \operatorname{root}(f)=[S+\{0,z\}],\quad
 P(f)=[S+\{0\}],\quad T(f)=[S].                              \tag{1.6}
\]

Choosing one option per root orbit and covering every rank-`(m-1)` orbit by
some `P(f)` and every rank-`(m-2)` orbit by some `T(f)` is necessary and
sufficient for exact named high-target marking after cyclic lift.  Periodic
lower orbits merely create stabilizer-many offers, of which one per named
target is marked.

## 2. The head involution and the exact turn law

Start from the tail-normalized representative (0.3) and rotate by `-z` so
that its first deletion becomes zero.  Its head signature is

\[
 \Gamma(S,z)=(H,\gamma),qquad
 H=\tau^{-z}S\cup\{-z\},qquad \gamma=-z.                    \tag{2.1}
\]

The corresponding head root is `H+{0}` and its deletion word is
`(0,gamma)`.  The map `(S,z)->(H,gamma)` is a bijection on the complete flag
option set.

Let `f=(S,z)` be used as a tail and let `g` have head signature
`(H,gamma)`.  A state-zero turn must replace the first tail deletion `z` by
some entering label `beta`, while the second head deletion `gamma` must
survive in the old bottom `S`.  Hence

\[
                         H=S+\{\beta\},qquad \gamma\in S,     \tag{2.2}
\]

and `z` must lie outside the head root.  This is exactly (0.4).  The two
middle roots and owner are

\[
 p=S+\{0,z\},\qquad q=H+\{0\},\qquad o=H+\{0,z\}.             \tag{2.3}
\]

Conversely (0.4) makes (2.3) a legal Johnson turn and gives the required
survivor.  This proves the characterization.

For a fixed head `(H,gamma)`, choose `z` outside `H+{0}` and then choose the
unique omitted element `beta=H-S`.  Condition `gamma in S` is precisely
`beta!=gamma`, proving (0.6).  There are

\[
                         (m+1)(m-2)                            \tag{2.4}
\]

potential predecessors of every head option in the complete option host.
All `m-2` predecessors with the same `z` have the same owner (0.5).

## 3. Exact compact quotient co-design formulation

Use a binary variable `x_f` for every `f in F`.  For every head option `g`,
every

\[
 z\notin H_g+\{0\},\qquad
 \beta\in H_g-\{\gamma_g\},                                  \tag{3.1}
\]

use a binary turn variable

\[
 y_{g,z,\beta},                                               \tag{3.2}
\]

whose predecessor is

\[
                         f(g,z,\beta)=(H_g-\{\beta\},z).       \tag{3.3}
\]

The exact equations are:

### Root choice

\[
 \sum_{f:\operatorname{root}(f)=R}x_f=1
 \qquad(R\in\tbinom{[n]}m/C_n).                              \tag{3.4}
\]

### High-target offers

\[
 \sum_{f:P(f)=P}x_f\ge1,qquad
 \sum_{f:T(f)=T}x_f\ge1                                     \tag{3.5}
\]

for every rank-`(m-1)` and rank-`(m-2)` target orbit.

### Incoming and outgoing turns

\[
 \sum_{z,\beta}y_{g,z,\beta}=x_g,                            \tag{3.6}
\]

\[
 \sum_{g,z,\beta:f(g,z,\beta)=f}y_{g,z,\beta}=x_f.           \tag{3.7}
\]

### Owner exactness

\[
 \sum_{g,z,\beta:[H_g+\{0,z\}]=O}y_{g,z,\beta}=1
 \qquad(O\in\tbinom{[n]}{m+1}/C_n).                          \tag{3.8}
\]

### Theorem 3.1 (exactness of the compact master)

Equations (3.4)--(3.8) are feasible if and only if there is a
rotation-equivariant depth-three all-high flag table which offers every
named high target and has an owner-exact literal directed cycle cover.

#### Proof

Sections 1--2 prove that every flag orbit and every state-zero turn orbit
occurs exactly once in the variables.  Equations (3.4)--(3.5) are exactly
root choice and target-orbit coverage.  Equations (3.6)--(3.7) give every
selected flag one incoming and one outgoing turn.  Equation (3.8) uses every
owner orbit once.  Rotating all selected quotient turns gives the physical
table and cover.  Conversely, quotient any equivariant physical solution and
read off its unique normalized options.  `square`

For `n=17,m=8`,

\[
 |{cal F}|=16\binom{15}{6}=80,080,                            \tag{3.9}
\]

and (2.4) gives

\[
 80,080\cdot9\cdot6=4,324,320                                \tag{3.10}
\]

turn variables.  This is smaller and structurally simpler than the current
5,068,292-variable age skeleton, but it deliberately handles only the
depth-three all-high/high-target gate.  It omits non-all-high pull types,
upper shadows, connectedness, opening, and the compiler.

## 4. Functional attachment: the maximal ordinary-flow face

Let

\[
 \vartheta:\binom{[n]}m/C_n\longrightarrow
             \binom{[n]}{m+1}/C_n                             \tag{4.1}
\]

be a bijection with `R subset vartheta(R)` in the quotient containment
poset.  The upper half of any necklace SCD supplies such a bijection.

For a selected head option `g` rooted at `R`, put

\[
 Z_\vartheta(g)={z\notin H_g+\{0\}:
                    [H_g+\{0,z\}]=\vartheta(R)}.              \tag{4.2}
\]

This set is nonempty because the quotient cover can be aligned to the
head-normalized representative `H_g+{0}`.

Let `X={f:x_f=1}`.  Define the functional predecessor graph

\[
 B_\vartheta(X)=(X^-,X^+;E_\vartheta)                         \tag{4.3}
\]

by joining

\[
 (H_g-\{\beta\},z)\longrightarrow g
 \tag{4.4}
\]

whenever `z in Z_vartheta(g)`, `beta in H_g-{gamma_g}`, and the predecessor
belongs to `X`.

### Theorem 4.1 (functional quotient Hall criterion)

For fixed `X,vartheta`, an owner-exact equivariant cycle cover using the
attachment `vartheta` exists if and only if `B_vartheta(X)` has a perfect
matching.  Equivalently, for every `Y subseteq X`,

\[
 \left|
 \{(H_g-\{\beta\},z)\in X:
      g\in Y, z\in Z_\vartheta(g),\
      \beta\in H_g-\{\gamma_g\}\}
 \right|\ge |Y|.                                             \tag{4.5}
\]

#### Proof

Every edge entering `g` has owner orbit `vartheta(root(g))`.  Since one
head option is selected per root orbit and `vartheta` is bijective, every
owner orbit is then used exactly once.  What remains is precisely a perfect
matching between the selected tail and head options.  Hall gives (4.5).
`square`

Thus fixing an upper containment matching removes the three-index owner
coupling and exposes a totally unimodular bipartite core.  The hard step is
choosing `X` and `vartheta` so that (3.5) and (4.5) hold together.

There is a smaller exact cut system before the punctured-facet choices are
examined.  Put

\[
                         \ell_z=|\{(S,z)\in X\}|.              \tag{4.5a}
\]

First ask only for one alignment `z in Z_vartheta(g)` at every head, with
exactly `ell_z` heads assigned label `z`.  This is a capacitated bipartite
flow from heads to the `n-1` nonzero labels.

### Theorem 4.2 (alignment-flux cut compression)

Such an alignment exists if and only if, for every label set
`A subseteq Z_n-{0}`,

\[
 |\{g\in X:Z_\vartheta(g)\subseteq A\}|
       \le \sum_{z\in A}\ell_z.                              \tag{4.5b}
\]

Its exact deficiency is

\[
 \delta_{\rm flux}(X,\vartheta)
 =\max_A\left(
 |\{g:Z_\vartheta(g)\subseteq A\}|-
 \sum_{z\in A}\ell_z
 \right)_+.                                                  \tag{4.5c}
\]

#### Proof

Join head `g` to every label in `Z_vartheta(g)`, give every head demand one,
and give label `z` capacity `ell_z`.  Max-flow/min-cut is exact.  The usual
capacitated Hall inequalities are

\[
 |Y|\le\sum_{z\in N(Y)}\ell_z.
\]

If this fails, take `A=N(Y)`; every member of `Y` has its complete list
inside `A`.  Conversely, for a fixed `A`, take all heads whose lists lie
inside `A`.  This gives (4.5b), and the same min-cut calculation gives
(4.5c).  `square`

The cut family has only `2^(n-1)` members, rather than one cut for every
subset of the Catalan-sized head shore.  It also gives an exact Benders face
for **variable** owner attachment.  Introduce a head--owner matching
variable `a_(g,O)`, and let `Z(g,O)` be the physical alignment list for that
incidence.  In addition to one attachment per head and owner, impose

\[
 \sum_{g,O:Z(g,O)\subseteq A}a_{g,O}
       \le\sum_{z\in A}\ell_z
 \qquad(A\subseteq\mathbb Z_n-\{0\}).                        \tag{4.5d}
\]

For an integral head--owner matching, (4.5d) is necessary and sufficient
for an alignment assignment with the tail-label histogram.  The cuts can be
separated by one max-flow computation.  They do not yet include the
facet/predecessor Hall cuts.

If one additionally chooses one physical alignment

\[
                         \zeta(g)\in Z_\vartheta(g),            \tag{4.6}
\]

then the graph splits by the label `z`.  Put

\[
 L_z=\{(S,z)\in X\},\qquad
 R_z=\{g\in X:\zeta(g)=z\}.                                  \tag{4.7}
\]

A necessary balance condition is `|L_z|=|R_z|` for every `z`, and the sharp
remaining cuts are

\[
 \left|
 \{(H_g-\{\beta\},z)\in L_z:
          g\in Y,\ \beta\in H_g-\{\gamma_g\}\}
 \right|\ge |Y|
 \quad(Y\subseteq R_z).                                      \tag{4.8}
\]

Each block (4.8) is a punctured containment graph: its left vertices are
rank-`(m-2)` sets in `[n]-{0,z}`, while a right record `(H,gamma)` may use
only the facets of `H` which retain `gamma`.  This is the sharp local object
for a Hall/expansion proof.

### Corollary 4.3 (block-regular sufficient face)

Suppose (4.6) is chosen so `|L_z|=|R_z|` for every `z`, and every induced
punctured containment graph in (4.8) is positive biregular.  Then
`B_vartheta(X)` has a perfect matching and the quotient chronology is owner
exact.

Indeed, edge counting in a biregular bipartite graph with equal shore sizes
gives equal positive degrees, so every block has a perfect matching.  More
generally it is enough that every block have the normalized matching
property

\[
                         {|N(Y)|\over|L_z|}
                         \ge {|Y|\over|R_z|}.                  \tag{4.9}
\]

The complete option host has this face **fractionally**.  Give each head
record `(H,gamma)` weight `1/(m+1)` at each external label `z`.  For fixed
`z`, the total head mass equals

\[
 {1\over m+1}\binom{2m-1}{m-1}(m-1)
 =\binom{2m-1}{m-2}=|L_z|,                                   \tag{4.10}
\]

and every left set `S` sees `(m+1)(m-2)` candidate marked heads, hence
fractional degree `m-2`.  Thus there is no fractional balance or regularity
separator in the prospective complete host.  Rounding this colouring while
also choosing one option per root orbit and exact target offers is the
integral design problem.

There is a concrete integral sufficient condition for that colouring.  Fix
`gamma`, and put

\[
 V_\gamma=\mathbb Z_n-\{0,\gamma\},qquad |V_\gamma|=2m-1.
 \tag{4.11}
\]

A head record `(H,gamma)` is the same as an `(m-2)`-set

\[
                         A=H-\{\gamma\}\subset V_\gamma.       \tag{4.12}
\]

Suppose there is a proper colouring

\[
 c_\gamma:J(2m-1,m-2)\longrightarrow V_\gamma               \tag{4.13}
\]

from the natural complement lists,

\[
                         c_\gamma(A)\notin A.                  \tag{4.14}
\]

Attach `(H,gamma)` at label `z=c_gamma(A)`.  Fix a left set `S` containing
`gamma`, and write `B=S-{gamma}`.  The upper neighbours

\[
                         A=B+\{\beta\},
                         \qquad\beta\in V_\gamma-B            \tag{4.15}
\]

form a clique of size `m+2` in the Johnson graph.  Properness gives `m+2`
different colours.  Every colour lies in `V_gamma-B`, and (4.14) forbids
the colour `beta` on its own vertex.  Hence the colours in (4.15) are
exactly a derangement of `V_gamma-B`.  For every external `z`, precisely
one `beta` therefore contributes the marked head `(S+beta,gamma)` to the
`z`-block.  Summing over the `m-2` choices `gamma in S` gives left degree
exactly `m-2`, proving the block-regular face.

This reduces prospective integral regularization to the following natural
list-colouring question:

> Colour every `(m-2)`-set of a `(2m-1)`-set by an element outside it, with
> adjacent Johnson vertices receiving different colours.

It has explicit solutions at the first two ranks.  For `m=3`, it is a
derangement colouring of `J(5,1)=K_5`.  For `m=4`, identify `V_gamma` with
`Z_7` and colour

\[
                         c_\gamma(\{a,b\})={a+b\over2}\pmod7;  \tag{4.16}
\]

this is a proper edge-colouring of `K_7` and never uses an endpoint colour.

The face has a sharp infinite obstruction.

### Theorem 4.4 (Steiner divisibility obstruction)

For every odd `m>=5`, the natural complement-list colouring (4.13)--(4.14)
does not exist.

#### Proof

Put `v=2m-1` and `k=m-2`.  For a colour `x`, let

\[
                         {\cal F}_x=\{A:c(A)=x\}.              \tag{4.17}
\]

Every member of `F_x` lies in `V-{x}`.  Properness says that two members of
`F_x` cannot share a `(k-1)`-set, so `F_x` is a `(k-1)`-packing and

\[
                         k|{\cal F}_x|
                         \le\binom{v-1}{k-1}.                  \tag{4.18}
\]

Summing over all `v` colours gives

\[
 \binom vk=\sum_x|{\cal F}_x|
 \le {v\over k}\binom{v-1}{k-1}
 =\binom vk.                                                  \tag{4.19}
\]

Equality is forced everywhere.  Hence every `F_x` is a Steiner system

\[
                         S(k-1,k,v-1).                         \tag{4.20}
\]

In such a system, the number of blocks through a fixed `(k-2)`-set is

\[
 {v-1-(k-2)\over k-(k-2)}={m+2\over2}.                       \tag{4.21}
\]

This must be an integer, forcing `m` even.  `square`

More generally, all divisibility conditions for (4.20) are necessary.  With
`j=k-i`, they read

\[
                         j\mid\binom{m+j}{j-1}
                         \qquad(1\le j\le m-2).                \tag{4.21a}
\]

At the target value `m=8`, the block-count condition `j=m-2=6` already
fails:

\[
                         |{\cal F}_x|
                         ={\binom{14}{5}\over6}
                         ={1001\over3}\notin\mathbb Z.         \tag{4.21b}
\]

Hence the complement-list/block-regular sufficient face is impossible for
`k=17` itself.  Any successful `k=17` punctured-containment Hall solution
must be nonregular (or leave this face entirely).

Thus block regularity is at best a sporadic even-`m` sufficient face, not a
uniform all-`m` route; even `m` is only a first divisibility gate.  At `m=5` it
would require the nonexistent Steiner triple
system `S(2,3,8)`; an exact H100 CNF replay returns `UNSAT`.  At `m=6` the
same finite model returns `SAT`, consistent with the divisibility condition
but not a proof for all even `m`.

The `m=6` positive instance also has a conceptual construction.

### Lemma 4.5 (Steiner lift)

If a Steiner system `S(k,k+1,v)` exists, then `J(v,k)` has a proper natural
complement-list colouring.

#### Proof

For a `k`-set `A`, let `B(A)` be its unique containing block and colour

\[
                         c(A)=B(A)-A.                          \tag{4.22}
\]

The colour is outside `A`.  If adjacent `A,A'` had the same colour `x`, the
`k`-set `(A intersect A')+{x}` would lie in the two distinct blocks
`A+{x}` and `A'+{x}`, contradicting the Steiner property.  `square`

For `m=4`, the Fano system `S(2,3,7)` supplies such a colouring.  For
`m=6`, the Witt system `S(4,5,11)` does so, proving the positive finite face
without a solver.  These sporadic designs do not remove the odd-`m`
obstruction or provide the needed all-parameter theorem.

Even when the colouring exists, it regularizes the complete option host;
one still needs an invariant one-per-root transversal satisfying (3.5).

## 5. Chronology-first form: two incidence matchings and future departures

Let `M=binom([n],m)` and `O=binom([n],m+1)`.  An owner-exact directed root
factor is equivalently a pair of incidence perfect matchings

\[
 A:M\longrightarrow O,qquad B:O\longrightarrow M.            \tag{5.1}
\]

Their composition

\[
                         \sigma=B\circ A                       \tag{5.2}
\]

is the root permutation.  Owner exactness is automatic.  Write

\[
 a(p)=p-\sigma(p)                                             \tag{5.3}
\]

for the departure at `p`; nonstuttering requires `p!=sigma(p)`.

### Theorem 5.1 (depth-three chronology-first equivalence)

The factor `(A,B)` supports the literal all-high depth-three flag at every
root if and only if

\[
                         a(\sigma(p))\in p\cap\sigma(p)         \tag{5.4}
\]

for every root `p`.  The flag is then uniquely

\[
                         (p;a(p),a(\sigma(p))).                 \tag{5.5}
\]

Its two offered high targets are

\[
 P(p)=p\cap\sigma(p),qquad
 T(p)=p\cap\sigma(p)\cap\sigma^2(p).                           \tag{5.6}
\]

Hence exact high-target marking is equivalent to the orbit families
`{P(p)}` and `{T(p)}` covering every required rank-`(m-1)` and rank-`(m-2)`
target.

#### Proof

The first transition deletes `a(p)`.  The second future departure is a
legal second flag deletion exactly when it survived the first transition,
which is (5.4).  Equation (5.5) follows.  Removing the first departure gives
the first intersection in (5.6); removing both consecutive departures gives
the three-root intersection.  Optional marking turns orbit coverage into
exact named coverage as before.  `square`

This formulation clarifies the matroid boundary.  The two incidence factors
in (5.1) are individually bipartite perfect matchings.  The rank-`(m-1)`
colour `P(p)` already couples them through a **surjective ordered Boolean-
diamond factor**: owners, tails, and heads are exact resources, while lower
diamond colours must all occur and may repeat.  This is the same four-
resource correlation which becomes the Catalan ordered-four-transversal
gate on its exact punctured/Pascal sector; the present odd layer has lower-
colour surplus and is not literally the equal-shore Catalan instance.  The
rank-`(m-2)` colour `T(p)` depends on two consecutive values of `sigma` and
is therefore a quadratic window constraint, not a rank function of either
matching alone.

After fixing one incidence matching, selecting one provider for every
`P`-colour with distinct owner and head resources is an intersection of
three partition constraints (target, owner, head), not ordinary two-matroid
intersection.  No Rado reduction is currently justified without fixing one
of those resource maps.  Functional attachment (Section 4) is exactly the
tractable subclass obtained by fixing the owner map; the remaining object is
ordinary bipartite Hall.

## 6. Relation to a protected reset bank

A reset packet specifies a bounded collection of literal transitions and
therefore fixes bounded pieces of both incidence matchings (5.1), together
with their future-departure flags.  In the unrestricted physical middle-
levels graph, the existing protected-factor theorem can extend a fixed
degree-two incidence forest of size `O(d)` into a spanning two-factor.  That
closes the uncoloured owner/root skeleton.

For an equivariant quotient construction the correct protected object is a
whole orbit of every reset transition.  Fixing one quotient turn variable in
(3.2) automatically fixes all of its physical translates and preserves rail
balance.  If a bank `P` of `h` quotient turns is a matching on tail, head,
and owner orbits, then deleting those `h` resources from (3.4)--(3.8) gives
the exact residual co-design problem; any residual solution joins `P` to an
owner-exact factor.

There are two proof-safe sufficient faces.

1. **Functional residual core.**  Attach the remaining head-root orbits
   bijectively to the remaining owners and prove the residual form of (4.5).
2. **Portal residual core.**  Treat the reset turns as prepared odd-cycle
   portals and prove that the residual turn incidence is balanced and
   fractionally perfect.

The target-selector theorem can quarantine a bounded physical flag bank,
but an orbitwise protected bank contains `n h` roots; its compatibility with
the cyclic exact selector must therefore be built directly into (3.5), not
inferred from the `h<=m+1` physical quarantine theorem.

For the authenticated `k=17` two-queue reset this direct coexistence has
already been proved.  Write its roots and owners as

\[
 T_a=K+\{X_a,X_{a+1},X_{a+2},X_{a+3}\},\qquad
 U_a=K+\{X_a,\ldots,X_{a+4}\}.                               \tag{6.1}
\]

Opening the reset between `T_7` and `T_0` retains the seven turns

\[
                         T_a\longrightarrow T_{a+1},
                         \qquad0\le a<7.                       \tag{6.2}
\]

In the two-incidence-matching language these are exactly the protected
edges

\[
                         T_a\longrightarrow U_a,qquad
                         U_a\longrightarrow T_{a+1}.           \tag{6.3}
\]

Their departure sequence is `a(T_a)=X_a`, so the survivor test is

\[
 X_{a+1}\in T_a\cap T_{a+1}.                                 \tag{6.4}
\]

The chronology-first target colours are precisely

\[
 \begin{aligned}
 P(T_a)&=T_a\cap T_{a+1}
       =K+\{X_{a+1},X_{a+2},X_{a+3}\},\\
 T(T_a)&=T_a\cap T_{a+1}\cap T_{a+2}
       =K+\{X_{a+2},X_{a+3}\}.
 \end{aligned}                                                \tag{6.5}
\]

Thus the reset is not merely compatible with (5.4)--(5.6); it is a literal
protected path fragment in both incidence factors with its q1 and q2 colours
already priced.  Exact quotient replay proves that its lower chain edges and
its seven head--owner columns extend to the corresponding global containment
matchings.  What remains open is the common predecessor/target completion,
not either marginal extension.

Most importantly, the first `k=17` factors have Hall deficiencies `420` and
`893` below.  A bounded reset/portal bank cannot repair either frozen factor.
The reset must be planted inside a globally co-designed `X,vartheta`, not
added after the deterministic quotient SCD is frozen.

## 7. Exact `k=17` calibrations

The first lower quotient chain factor has

```text
G0 edges=3836 zeroL=246 zeroR=124 matching=1010
matched_colors=818 color_collisions=192
```

so its unrestricted matching deficiency is `1430-1010=420` before owner
rainbow.

The functional calibration computes an independent rank-eight-to-rank-nine
quotient containment bijection, retains every physical alignment of that
owner orbit at each head flag, and then builds (4.3).  H100 reports

```text
PASS_FUNCTIONAL_UPPER_AUDIT roots=1430 upper_matching=1430
alignments=1433 max_align=2 edges=1454
zeroL=824 zeroR=722 matching=537 alignment_balance_matching=1235
flux_cut mask=95586 demand=996 capacity=801 deficiency=195
alignment_hist 1:1427 2:3
```

Thus the independent first upper factor leaves functional deficiency
`1430-537=893`.  The fact that `1427/1430` head flags have only one physical
alignment also shows that representative freedom cannot repair this fixed
upper matching locally.  Even the earlier alignment-flux row fails by195:
the sharp compressed cut uses labels
`{1,5,6,8,10,12,13,14,16}`, contains all allowed alignments of996 heads,
and has tail capacity only801.  This independently authenticates Theorem
4.2 on a nontrivial exact instance.

Artifacts:

```text
MATH_AUDIT_K17_CYCLIC_SCD_D3_FIRST_FACTOR_STATE_HALL_20260801.md
scratch/build_audit_k17_quotient_scd_d3_state_graph_20260801.cpp
scratch/k17_quotient_scd_d3_first_factor_20260801.audit.txt

scratch/audit_k17_quotient_scd_d3_functional_upper_20260801.cpp
scratch/k17_quotient_scd_d3_functional_upper_20260801.audit.txt
```

## 8. Sharpened missing theorem

The smallest positive theorem which closes this gate is:

> **Functional quotient chain-factor theorem (`d=3`).**  Choose one flag
> option per root necklace satisfying (3.5), and choose a quotient
> root-to-owner containment bijection `vartheta`, so that the punctured
> containment Hall inequalities (4.5) hold.

This theorem is strictly weaker than solving the unrestricted rainbow
master: owner exactness then follows from the functional attachment and
ordinary bipartite integrality.  A still stronger but more structured target
chooses alignments `zeta` and proves every block (4.8) has a perfect
matching.

Chronology-first, the same statement asks for two incidence perfect
matchings whose permutation obeys the survivor condition (5.4) and covers
both intersection decks (5.6).  The first deck is the surplus ordered-
diamond correlation whose exact punctured sector is the open Catalan
ordered-four-transversal problem; the second is a two-step refinement.  Thus
there is no hidden ordinary Rado theorem left after fixing only one incidence
factor.

The protected reset bank is compatible with either formulation, but only as
part of the joint construction.  The calibrated deterministic factors are
too deficient for bounded post-hoc absorption.
