# Lane L: recycled coatom providers and the unit-root gate

Date: 2026-08-01  
Status: exact static matching theorem, exact one-class min--max theorem,
exact age-type fusion theorem, and sharp scoped counterexamples.  No
one-copy rotor colouring, physical compiler, or new bound on `nu(k)` is
claimed.

## 0. Verdict

The fractional monotone-rotor/pull-clock circulation does contain a
genuinely useful globally shared provider class, but only after three
different projections are kept separate.

1. **Static named providers.**  On every unpunctured rank, and in particular
   on the coatom rank `r-1`, the fractional support contains an integral
   owner--target matching.  In the central regime this rebuilds the entire
   lower-q1 deck with distinct rank-`r` owners.  Thus the protected
   word-slack cut from item2526L disappears completely if q1 provider marks
   may be released and rematched independently of chronology.
2. **Unlabelled age topology.**  One copy of the adjacent high class
   `g_(0,r-2)` connects all raw rotation components of one core-free class
   `g_(0,r-1)` at age-type level.  The separator class is a genuine quotient
   fusion catalyst; a blanket type-level lower bound against one extra high
   class would be false.
3. **Physical one-copy correlation.**  Neither result selects one balanced
   trace per owner.  The exact reusable resource is not a class name or a
   fractional amount of high mass.  It is a literal separator-returning
   catalogue of **unit provider roots** `e_v-e_u` whose directed transfer
   graph passes the provider cuts.  Under that hypothesis one shared
   separator is reusable through arbitrarily many components with no
   terminal separator boundary.  Without unit-root saturation, even a
   complete transfer graph and an exact fractional all-target solution can
   leave linearly many integral holes.

Consequently the weakest positive next theorem is transition-transparent
coatom retiming, or equivalently a literal returned-separator unit-root
network coupled to the one-copy chronology.  The already proved fractional
rank distribution supplies the static matching but does not prove this
correlation row.

## 1. Consumable occurrences versus a returned separator

Let `P` be a finite named palette.  After the connector packet let

\[
 m:P\longrightarrow\mathbb Z_{\ge0},\qquad
 D=\{t:m(t)=0\},\qquad s(t)=(m(t)-1)_+ .                 \tag{1.1}
\]

A private unit transport `u->v` deletes one provider of `u` and creates one
provider of `v`.  Give the transports integral capacities `c(u,v)`.  As in
item2526L, the capacities include every persistent physical resource of the
macro.

Now add a family `G` of **consumable separator occurrences**.  An occurrence
`g` may be deposited initially at one target in its menu `E_g subseteq P`,
and may be used at most once.  Menus and transports are assumed independent
and serial-safe: after a provider reaches an intermediate target, it may be
passed on, and no resource outside the displayed capacities is consumed.
Put

\[
 \gamma(B)=|\{g\in G:E_g\cap B\ne\varnothing\}|.         \tag{1.2}
\]

### Theorem 1.1 (exact one-class occurrence cut)

The minimum number of terminal holes is

\[
 \boxed{
 H^*=\max_{B\subseteq P}
 \bigl(|D\cap B|-s(B)-c(P\setminus B,B)-\gamma(B)\bigr)_+.}
                                                               \tag{1.3}
\]

Thus a shared provider *class* contributes only through its number of
literal occurrence tokens that can enter each cut.  Giving many tokens one
common type name does not make one token count more than once.

#### Proof

Build a network with source `sigma`, sink `tau`, target nodes `P`, and one
node for every `g in G`.  Add

\[
\begin{array}{c|c}
 \sigma\to u&s(u)\\
 u\to v&c(u,v)\\
 \sigma\to g&1\\
 g\to t&+\infty\quad(t\in E_g)\\
 t\to\tau&1\quad(t\in D).
\end{array}                                                   \tag{1.4}
\]

An integral flow path either starts at an old surplus or at one consumable
separator token and ends at one old hole.  Execute it from source to sink.
Every initially covered intermediate receives the travelling provider before
passing one on, so it never becomes uncovered; an initially empty
intermediate receives and passes the unit and remains an old hole.  Conversely
trace each newly filled initial hole backward through any terminal-improving
serialization to an initial surplus or consumed token.  Discard cycles and
lineages ending at already covered targets.  The remaining source-rooted
provider lineages project to a flow of exactly the number of newly filled
old holes.

For a cut whose target nodes on the sink side are `B`, a separator node can
stay on the source side exactly when its menu misses `B`; otherwise its unit
source arc is cut.  The remaining cut terms are `s(B)`,
`c(P-B,B)`, and the old-hole sink arcs outside `B`.  Subtracting the minimum
cut from `|D|` gives (1.3).  Network integrality completes the proof.
\(\square\)

A **returned separator** is different.  It is a catalyst, not a positive
source term: every macro starts and ends with the same literal separator
state and changes only the named provider load.  Suppose a single returned
separator enables a serial-regenerative digraph `R` of unit moves
`u->v`, each with payload `e_v-e_u`.  The same separator may be used again
after every macro; all other local resources are restored or are separately
time-expanded.

### Theorem 1.2 (returned unit-root catalyst)

With the preceding literal return and regeneration hypotheses,

\[
 \boxed{
 H^*=\max_{\substack{B\subseteq P\\
                     \delta_R^-(B)=\varnothing}}
       \bigl(|D\cap B|-s(B)\bigr)_+
     =\max_{\delta_R^-(B)=\varnothing}(|B|-m(B))_+.}   \tag{1.5}
\]

In particular, if `R` is strongly connected and `m(P)>=|P|`, one globally
recycled separator closes every provider hole with zero terminal boundary,
regardless of the number of connector components.

#### Proof

Apply Theorem 1.1 with no consumable tokens and infinite capacity on every
arc of `R`.  A finite cut must have no `R`-arc entering `B`; these and only
these cuts remain in (1.3).  The identity

\[
 |B|-m(B)=|D\cap B|-\sum_{u\in B}(m(u)-1)_+
\]

gives the second form.  Integrally decompose the resulting flow into paths
from old surpluses to old holes.  Execute each path in forward order.  At an
intermediate vertex the arriving unit is present before the outgoing unit is
moved, and the separator has returned before the next step.  If `R` is
strongly connected, the only nonempty in-closed set is `P`, whose displayed
deficit is nonpositive by the total-load hypothesis.  \(\square\)

Equation (1.5) is the precise weakest cut theorem in this regenerative
model.  If a macro moves two provider units at once, consumes a separator,
or fails to restore another socket, it is not an arc of `R` and the theorem
does not apply.

## 2. The pull-clock coatom mass rounds statically

Fix

\[
 k\ge r>d\ge1,\qquad W=\binom{k}{r},\qquad
 N=\binom{k}{r-1}\le W.                               \tag{2.1}
\]

Let `mu` be the normalized literal same-owner marked trace circulation from
the monotone-rotor theorem, with owner mass one in every rank-`r` owner.
Assume the rank-`r-1` Ferrers puncture is zero:

\[
 b_{r-1}=0,qquad q_{r-1}=N/W.                       \tag{2.2}
\]

The first condition is automatic on the usual face `d<r-1`.  For an owner
`T` and coatom target `Q`, let `X(T,Q)` be the `mu`-mass of marked
rank-`r-1` occurrences whose owner is `T` and whose literal prefix is `Q`.
Only containments `Q subset T` have positive mass.

### Theorem 2.1 (static coatom recycling)

The support graph

\[
 \mathcal E=\{(T,Q):X(T,Q)>0\}
\]

has a matching saturating every rank-`r-1` target `Q`.  Hence all `N`
coatom targets have distinct supported rank-`r` owners.  In the odd central
case the matching is perfect; in the even central case it leaves exactly
`W-N` owners unmarked.

#### Proof

The target-load calculation of the fractional rotor theorem gives

\[
 \sum_T X(T,Q)={Wq_{r-1}\over N}=1                 \tag{2.3}
\]

for every `Q`.  One owner occurrence offers at most one target of a fixed
rank, and owner mass is one, so in fact

\[
 \sum_QX(T,Q)=q_{r-1}=N/W\le1                     \tag{2.4}
\]

for every `T`.  If `S` is any family of coatom targets and
`N_X(S)` its neighbourhood in the positive support, then

\[
 |S|=\sum_{Q\in S,T}X(T,Q)
    \le {N\over W}|N_X(S)|\le |N_X(S)|.             \tag{2.5}
\]

Hall's theorem gives the required integral matching, using only supported
pairs.  For `k=2m+1,r=m+1`, one has `N=W`; for `k=2m,r=m`, one has
`N/W=m/(m+1)` and `W-N=W/(m+1)`.  \(\square\)

The same proof works **separately** at every unpunctured rank `s` for which
`binom(k,s)<=W`: put `N_s=binom(k,s)` and
`q_s=N_s/W`.  It does not choose one common nested flag simultaneously at
several ranks.

### Corollary 2.2 (what happens to the protected word-slack cut)

In the `C` disjoint-tag `PH` bank of item2526L, the lower bound

\[
 h\ge C(d-1)-B_{\rm out}                              \tag{2.6}
\]

assumes that old q1 provider identities remain protected and every recreated
colour is charged to a bounded outside-closure bank.  If coatom marks may be
released after source reassembly and reattached according to Theorem 2.1
without changing the selected transitions or consuming another resource,
then discard all old q1 provider identities and use the matching.  Every q1
target is present, every provider-closure cut is nonnegative, and the static
q1 debt is zero.  The bounded-`B_out` premise of (2.6) then no longer
applies: Theorem 2.1 supplies a new global matching outside that protected
retained-source accounting.

This corollary is deliberately conditional on **transition-transparent
retiming**.  In the literal pull clock the coatom is `Q=T-C_d`; changing it
generally changes the labelled state and its legal predecessor/successor.
Theorem 2.1 does not preserve state balance, topology, residence, upper
witnesses, or a compiler cap.

## 3. One adjacent high class fuses the core-free quotient

There is also a positive result before labels are installed.  Fix

\[
                         d\ge1,\qquad r\ge d+3.       \tag{3.1}
\]

One `g_(0,r-1)` package contains one occurrence of every positive
composition

\[
 x=(x_0,\ldots,x_d),\qquad \sum_i x_i=r,             \tag{3.2}
\]

and its raw successor rotates `x`.  One `g_(0,r-2)` package has mobile
composition `y` of `r-1` and permanent core one; its age type is

\[
                         y+e_0.                       \tag{3.3}
\]

Thus it gives a second occurrence of every type `x` with `x_0>=2`, in a
different rotor package.  The two bank sizes are

\[
 |\mathcal A_r|=\binom{r-1}{d},\qquad
 |\mathcal A_{r-1}|=\binom{r-2}{d}.                  \tag{3.4a}
\]

Every common type occurs once in each bank.  Writing
`iota(y)=(1+y_0,y_1,...,y_d)`, the second raw arc is

\[
 \iota(y)\longrightarrow\iota(Ry)
   =(1+y_d,y_0,\ldots,y_{d-1}).                      \tag{3.4b}
\]

Its first shifted row is `y_0<=1+y_0` and all later rows are equality.
One full canonical package is used; minimality is not claimed.

### Theorem 3.1 (single high-class quotient catalyst)

At age-type level, the disjoint union of one raw `g_(0,r-1)` cycle cover and
one raw `g_(0,r-2)` cycle cover can be rethreaded into one successor cycle by
two-edge switches.  Every occurrence, and hence every occurrence-attached
rank mark, is retained.

#### Proof

Contract the raw rotation cycles in both packages.  Join a necklace `[x]`
of positive compositions of `r` to a necklace `[y]` of positive
compositions of `r-1` whenever, after cyclic choice of representatives,

\[
                         x=y+e_j                     \tag{3.4c}

for some coordinate `j`.  This bipartite quotient is connected.  Indeed,
two `r`-compositions adjacent through the same `y` differ by moving one unit
between two coordinates while all parts stay positive.  These unit transfers
connect all positive compositions of fixed sum, and quotienting by cyclic
rotation preserves connectedness.  Every `(r-1)`-necklace `[y]` is adjacent
to `[y+e_0]`, so the entire bipartite quotient, not merely its `r`-shore
two-section, is connected.

An edge (3.4c) is witnessed by two occurrences of the same age type: rotate
the core-free occurrence so that the added unit is at coordinate zero, and
use the corresponding permanent-core occurrence (3.3).  Since the two tails
have identical type, each accepts both old heads.  Cross their outgoing
arcs.  If their current cycles are distinct, this merges the two cycles.

Root a spanning tree of the connected bipartite quotient and process its
edges outward from the root.  At each step the parent occurrence is in the
already fused root-subtree cycle and the child occurrence is in a new raw
cycle, so the crossing merges them.  A parent witness may be reused: after
an earlier crossing its current head is still legal from every occurrence
of the same source type, and crossing it with a new child again merges two
distinct current cycles.  The last state is therefore one cycle.  Only
successor arcs changed, so all occurrence-attached marks remain.
Exactly `|\mathcal A_r/<R>|+|\mathcal A_{r-1}/<R>|-1` switches are used.
\(\square\)

This theorem is unlabelled.  Equal age types need not be equal ordered
partitions of a named owner, and the crossed labelled arcs need not satisfy
the exact survivor recurrence/equalities.  It therefore removes the
raw-word/deep-fibre
topology obstruction for this two-package inventory but does not supply a
literal owner, q1, upper, or compiler lift.  It also does not assert that one
separator package fuses arbitrarily many repeated core-free packages.

There is a separate terminal-provider capacity which quotient fusion does
not evade.  One copy of `g_(0,b)` has `binom(b,d)` occurrences, and exactly

\[
                         \binom{b-1}{d-1}             \tag{3.5}
\]

of them offer a rank-`r-1` coatom: in the positive mobile composition the
last part must be one.  Thus `z` copies contribute at most
`z binom(b-1,d-1)` terminal coatom providers.  Against the protected `PH`
bank, even a perfectly recycled class obeys the literal counting bound

\[
 h\ge C(d-1)-B_{\rm other}-z\binom{b-1}{d-1}.        \tag{3.6}
\]

Here `B_other` counts terminal old-q1 provider incidences disjoint from the
`z` package occurrences.  Consequently a fixed multiplicity of the
quotient catalyst need not close a
growing protected bank.  Theorem 2.1 avoids this count only by releasing and
rematching the complete global coatom supply, not by counting one package
twice.

## 4. Why fractional supply is not the physical theorem

The returned-catalyst theorem needs primitive unit roots in the named-load
lattice.  Fractional rank marginals do not imply that saturation.

### Theorem 4.1 (complete bundled-root graph with linear integral debt)

For every `q>=2` and `n>=1` there is a provider system on `qn` targets with
one globally returned separator class such that

* its macro support digraph is complete and hence strongly connected;
* its fractional relaxation reaches the all-one target vector exactly; but
* every integral serialization leaves at least `(q-1)n` targets uncovered.

#### Construction and proof

Initially give `n` targets load `q` and the other `(q-1)n` targets load zero.
For every ordered pair allow the separator-returning bundled move

\[
                         q(e_v-e_u).                 \tag{4.1}
\]

Partition the holes into `q-1` private destinations for every initially
loaded target.  Giving each of those `q-1` moves weight `1/q` removes
`q-1` units from the source and puts one at each destination.  The
fractional terminal vector is all ones.

Every integral move preserves every load modulo `q`.  Since total load is
`qn`, at most `n` targets can be nonzero in any integral state.  Therefore
at least `(q-1)n` targets remain absent; the initial state attains the bound.
\(\square\)

Thus it is unsound to replace a bundled signed payload by `q` unit arcs in
the min-cut.  The exact missing hypothesis in Theorem 1.2 is saturation by
the primitive roots `e_v-e_u` together with positive serializability, not
merely strong support or real-cone feasibility.

Theorem 4.1 is an abstract signed-provider catalogue.  It is not asserted to
embed in the Boolean pull-clock; the following route obstruction is the
separate literal calibration.

There is a second correlation failure even with unit provider tokens.  For
`P={x_1,...,x_n,y_1,...,y_n}`, give one global clock two integral phases and
two tokens for every `i`.  In phase zero both tokens have singleton menu
`{x_i}`; in phase one both have menu `{y_i}`.  With no old load or
transports, the two phase cut functions are

\[
 \gamma_0(B)=2|\{i:x_i\in B\}|,\qquad
 \gamma_1(B)=2|\{i:y_i\in B\}|.                     \tag{4.2}
\]

Their half--half average is `\bar\gamma(B)=|B|` for every `B`, so every
averaged provider cut passes and every target has fractional load one.  But
either integral phase misses exactly `n` targets.  Equivalently,

\[
 \min_{\omega\in\{0,1\}}\max_{B\subseteq P}
       (|B|-\gamma_\omega(B))_+=n,
 \qquad
 \max_B(|B|-\bar\gamma(B))_+=0.                    \tag{4.3}
\]

Thus even unit occurrences cannot be inserted into (1.3) by averaging over
a shared clock phase.  Their menus must be independently selectable, or the
phase variable must remain inside the min--max.

There is also a literal Boolean route obstruction.  For every even `k>=4`,
take `(r,d)=(2,1)` and give pair-owner `{u,v}` the two traces `u->v` and
`v->u`.  Weight each direction by `1/2` and mark mass `1/(k-1)` at its
singleton tail.  This is owner-perfect and stationary, and every singleton
coatom target has total marked load one.  Theorem 2.1 therefore gives a
static supported provider matching.  But every integral one-copy selector
orients `K_k`; all `k` state divergences are odd because `k-1` is odd.  A
circuit needs at least `k/2` added route arcs, and an open trail at least
`k/2-1`.  These bounds are sharp by adding a perfect matching, or a matching
on all but two vertices, before applying the Euler orientation theorem.

This infinite family is a literal distribution-only no-go, but for `k>4`
it is not the central Ferrers slice.  It does not refute a future
central-rank transition-transparent coatom theorem.

Finally, even exact balance and exact high-provider marginals need not have
a common integral point in an arbitrary catalogue.  Take states `a,b,c,d`,
targets `p,q`, and two owners with options

\[
\begin{array}{c|cc}
1&a\to b\ (p)&c\to d\ (q)\\
2&b\to a\ (p)&d\to c\ (q).
\end{array}                                                   \tag{4.4}
\]

Half of all four columns is balanced, owner-perfect, and gives loads
`p=q=1`.  An integral balanced owner-perfect choice is either the first
reverse pair, of payload `2p`, or the second, of payload `2q`.  One named
target is missing.  `C` disjoint copies force `C` holes.  This abstract
gadget is not claimed to be a Boolean pull-clock embedding; it isolates the
non-TU intersection of owner, state-incidence, and provider rows.

## 5. Exact surviving one-class theorem

Combining the positive statements gives the following proof-safe target.

### Corollary 5.1 (zero-boundary one-class closure)

Suppose a selected one-copy chronology is already exact outside the coatom
provider row.  Assume either:

1. coatom marks are transition-transparent and their supported owner graph
   contains the fractional matrix `X` of Theorem 2.1; or
2. one literal separator is returned after every macro and its serial-safe
   named payloads contain the unit roots of a digraph `R` satisfying all
   closed-set inequalities in (1.5).

Then the complete coatom provider row can be restored integrally.  In case
1 this is Hall matching; in case 2 it is integral flow and serial path
execution.  No separator occurrence is left at an internal merge, so the
terminal separator boundary is zero.  With allowed terminal debt `H`, the
exact condition is (1.3) or (1.5) with right-hand slack `H`.

The hypotheses are strictly stronger than the monotone-rotor fractional
circulation.  That circulation proves the static matrix `X`, and Theorem
3.1 proves a quotient catalyst, but neither identifies labelled unit-root
macros on the same selected chronology.  Other ranks, common nested-flag
choice, Hamilton topology, residence, upper/deep witnesses, and compiler
cap remain open.

## 6. Relation to earlier items

* Item2513L supplies the fractional circulation and the core-free rotation
  rigidity.
* Item2517R supplies the aggregate two-buffer semigroup decomposition.
* Items2520L and2526L show that the two scalar buffers do not imply physical
  fusion or bounded provider boundary.
* Theorem 2.1 above shows that a released coatom provider class is stronger
  than those two scalar buffers and eliminates the static q1 cut exactly.
* Theorems 1.2 and4.1 identify the remaining dichotomy: primitive returned
  provider roots give a zero-boundary network theorem; bundled or
  transition-coupled high mass can retain linear integral debt.
