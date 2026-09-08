# PBBS component-signature packets, exact cube correlation, and two-shore traps

Date: 2026-07-30  
Lane: R, pure-mathematics all-`k` compiler lane  
Status: unconditional component-cube theorems and an exact PBBS obstruction
certificate.  No unconditional `B(k)+O(k)` conclusion is claimed.

## 0. Result

Let `M^0,M^1` be two target-saturating matchings in one forced-unit-closed
PBBS interval-candidate face, with the deterministic forced family
`Theta_0` adjoined to both.  Switch independently between the two shores of
each component of `M^0 triangle M^1`.

For a shore-consistent physical conflict `F`, let

* `n(F)` be its number of noncommon edges; and
* `rho(F)` be the number of distinct alternating components containing
  those edges.

Then the fair component cube satisfies the exact, deletion-stable identity

\[
 \Pr(F\subseteq M(Z))=2^{-\rho(F)}
 =2^{n(F)-\rho(F)}\prod_{e\in F}\Pr(e\in M(Z)).       \tag{0.1}
\]

In particular

\[
 \Pr(F\subseteq M(Z))\le 2^{|F|}\prod_{e\in F}x_e.  \tag{0.2}
\]

Thus a two-matching cube has an unconditional all-arity cylinder constant
`C_0=2`; no permanent-minor expansion and no negative association is
needed.  The loss `2^(n-rho)`, rather than arity alone, is exact.

The remaining issue is not correlation but target repair.  We prove an
exact **signature-packet cover theorem**.  A packet consists of a partial
component assignment `sigma`, a target set `H`, and a family of conflicts
all extending `sigma` and all met by `H`.  If packets cover every
shore-consistent run/positive-guard conflict, then one cube point is
repairable after at most

\[
 \left\lfloor
 \sum_S\Pr\!\left(
   \bigvee_{a:S\in H_a}[Z\supseteq\sigma_a]
 \right)
 \right\rfloor                                       \tag{0.3}
\]

target deletions.  A convenient upper bound replaces each probability in
(0.3) by

\[
 \min\left\{1,\sum_{a:S\in H_a}2^{-|\sigma_a|}\right\}. \tag{0.4}
\]

This can be exponentially smaller than summing conflicts individually,
because a single packet may contain every arity and every composition in a
stable bank.

There is, however, no automatic `O(k)` packet bound.  The smallest exact
obstruction is a **two-shore trap**: one alternating component has a
physical conflict on each shore.  Every component choice then contains a
conflict.  Target-disjoint copies force one literal deletion apiece.  In
the actual mandatory-core PBBS graph this is checked entirely by the
candidate sandwiches and the pair-conflict conditions (central cover or
positive guard), plus actual survival in the chosen residual face.  The
isolated four-edge example below survives ordinary degree-one propagation
but not complete failed-literal lookahead, so it is not asserted to survive
every meaning of full closure.  Therefore the corrected exact component
invariant is the minimum cube-point target-repair number below; packet
pressure is a checkable upper certificate.  One must also exclude a
superlinear packing of two-shore traps.  Alternating-component count alone
does not control the compiler.

Finally, component pressure transfers through a Pascal odd/even lift only
under a quantitative component-merger ledger.  If transported child targets
project to parent targets with fibre at most `g`, every child target's
lifted packet load is at most `2^h` times its projected parent load, and the
genuinely new promoted-collar conflicts have packet budget `L`, then

\[
        \Pi_{\rm child}\le\overline\Pi_{\rm child}
        \le g\,2^h\overline\Pi_{\rm parent}+L.                    \tag{0.5}
\]

The proved Pascal envelope/flag identities preserve interior candidates,
but do not bound `h` or `L`; hence they do not yet preserve `B(k)+O(k)`.

## 1. Forced-closed two-matching cube

Let `G=(mathcal S,mathcal I;E)` be a residual bipartite candidate graph.
The left parts `mathcal S` are retained lower targets and the right vertices
`mathcal I` are physical interval columns.  Every matching considered below
saturates `mathcal S`; right vertices need not all be used.  Let

\[
                         M^0,M^1\subseteq E                         \tag{1.1}
\]

be two such matchings in the same face after exact unit closure.  All
structurally forced candidates form a compatible deterministic family
`Theta_0`.  We adjoin `Theta_0` to every selected matching before physical
run/guard conflicts are tested.  Thus a contracted conflict with a forced
anchor is always used in its lifted form and its target set includes that
anchor target.  Put

\[
 \mathcal T=\mathcal S\cup
 \{S:(S,I)\in\Theta_0\};                              \tag{1.1b}
\]

these are all target parts which may be deleted and appended.  Exact
closure has already removed the forced targets and columns from the
residual graph, so the two displayed pieces are disjoint as matching data.

Here “unit closure” means closure under presently forced candidates and
their deterministic deletions/contractions, as in item 1997.  It does not
mean complete failed-literal or global-consistency closure; whenever the
latter stronger closure is intended, survival is stated separately.

Put

\[
                         \mathcal E_0=\Theta_0\cup(M^0\cap M^1).   \tag{1.1a}
\]

Delete the common residual edges from `M^0 union M^1`.  Its nontrivial connected
components are alternating paths and even cycles; call their set
`mathcal K`.  For `z in {0,1}^mathcal K`, put

\[
 M(z)=\mathcal E_0\cup
 \bigcup_{K\in\mathcal K}(M^{z_K}\cap E(K)).          \tag{1.2}
\]

Every `M(z)` is again a matching saturating all retained targets.  This is
because each target of a nontrivial component has one incident edge of
each shore, while the selected shore is a matching on the right side.

For an edge `e in (M^0 triangle M^1)`, write `kappa(e)` for its component
and `epsilon(e) in {0,1}` for its shore.  Common edges have neither datum.
A set `F subseteq Theta_0 union M^0 union M^1` is **shore-consistent** when

\[
 \epsilon(e)=\epsilon(f)
 \quad\hbox{whenever }\kappa(e)=\kappa(f).            \tag{1.3}
\]

Its signature is the partial bit assignment

\[
 \sigma_F(K)=\epsilon(e)
 \quad(e\in F,\ \kappa(e)=K),                         \tag{1.4}
\]

and

\[
 n(F)=|F\setminus\mathcal E_0|,
 \qquad \rho(F)=|\operatorname{dom}\sigma_F|.         \tag{1.5}
\]

## 2. Exact component-rank cylinder law

### Theorem 2.1 (exact cube probability)

Under the uniform product law on the component bits:

1. a non-shore-consistent `F` has probability zero;
2. a shore-consistent `F` satisfies

   \[
   \Pr(F\subseteq M(Z))=2^{-\rho(F)};                 \tag{2.1}
   \]

3. if `x_e=Pr(e in M(Z))`, then

   \[
   \Pr(F\subseteq M(Z))
   =2^{n(F)-\rho(F)}\prod_{e\in F}x_e;                \tag{2.2}
   \]

4. after conditioning arbitrary component bits, the same statements hold
   on the unconditioned components, with inconsistent events deleted and
   the conditioned coordinates removed from `sigma_F`;
5. after deleting common target/column data and restricting both shores,
   the new alternating components refine the surviving old components, so
   the identity holds anew and `n(F)-rho(F)` cannot increase for a retained
   event.  The same applies after first conditioning shore bits and deleting
   their used endpoints.

Consequently every physical conflict, of every arity, obeys

\[
 \Pr(F\subseteq M(Z))\le2^{|F|}\prod_{e\in F}x_e.    \tag{2.3}
\]

#### Proof

The event `F subseteq M(Z)` is impossible exactly when `F` asks for both
shores of one component.  Otherwise it asks for one prescribed fair bit on
each of the `rho(F)` components in its signature and asks nothing of all
other component bits.  This proves (2.1).  A common edge has marginal one
and a noncommon edge has marginal one half, so the product of edge
marginals is `2^(-n(F))`; (2.2) follows.  Conditioning fixes or kills each
requested bit and leaves the remaining bits independent and fair.  Common
vertex/edge deletion can only split an alternating path or cycle, never
join two of its components.  Thus the surviving noncommon edges of `F`
meet at least as many component blocks, while `n(F)` is unchanged.  After
a shore is conditioned, deleting its endpoints has the same refinement
effect on all still-free components.  Finally
`n(F)-rho(F)<=n(F)<=|F|`, proving (2.3).  QED.

The factor `2^(n-rho)` is sometimes one and sometimes exponential in the
arity.  Thus it is incorrect to treat the noncommon edge indicators as
negatively associated.  What survives exactly is component-rank, not edge-
rank.

## 3. Signature-packet target cover

Let `mathcal C_triangle` be the complete shore-consistent physical conflict
family in `Theta_0 union M^0 union M^1`, including every hybrid conflict
which occurs in neither endpoint and every forced-anchor conflict in lifted
form.  For a
conflict `F`, let `T(F)` be its set of target parts.

A **signature packet** is a triple

\[
                         a=(\sigma_a,H_a,\mathcal C_a)               \tag{3.1}
\]

such that

1. `sigma_a` is a partial assignment of component bits;
2. `H_a subseteq mathcal T` is a finite target set;
3. `mathcal C_a subseteq mathcal C_triangle`;
4. `sigma_a subseteq sigma_F` and `H_a cap T(F) ne emptyset` for every
   `F in mathcal C_a`.

A packet family is complete when the `mathcal C_a` cover
`mathcal C_triangle`.  Define its exact pressure

\[
 \Pi(\mathcal P)=
 \sum_{S\in\mathcal T}
 \Pr\left(
   \bigvee_{a:\,S\in H_a}[Z\supseteq\sigma_a]
 \right).                                             \tag{3.2}
\]

The probability is an ordinary Boolean-cylinder union probability; no
independence between packets is asserted.  The union bound gives

\[
 \Pi(\mathcal P)\le
 \sum_S\min\left\{1,
   \sum_{a:\,S\in H_a}2^{-|\sigma_a|}
 \right\}.                                             \tag{3.3}
\]

### Theorem 3.1 (packet-cover completion)

Suppose the middle chronology is upper-complete and recursive closure has
omitted `O_cl`.  For every complete signature-packet family,

\[
 \boxed{
 \nu(k)\le B(k)+|O_{cl}|+\lfloor\Pi(\mathcal P)\rfloor.}           \tag{3.4}
\]

In particular `|O_cl|+Pi(mathcal P)=O(k)` proves `B(k)+O(k)`.

#### Proof

For a component assignment `z`, activate packet `a` when
`z supseteq sigma_a` and delete

\[
                         D(z)=\bigcup_{a:\,z\supseteq\sigma_a}H_a. \tag{3.5}
\]

If a conflict `F` occurs in `M(z)`, choose a packet containing it.
Occurrence means `z supseteq sigma_F`, and
`sigma_a subseteq sigma_F`; hence that packet is active.  Its target set
meets `T(F)`, so `D(z)` deletes a target part of `F`.  Therefore `D(z)`
hits every occurring minimal conflict.  Physical compatibility is downward
closed, so the surviving target selector is compatible.

For each target `S`, the probability that `S in D(Z)` is exactly the
summand in (3.2).  Hence `E|D(Z)|=Pi(mathcal P)`, and some integral cube
point has `|D(z)|<=floor(Pi(mathcal P))`.  Append all targets in `O_cl`
and `D(z)` literally.  Upper completeness supplies the upper half, proving
(3.4).  QED.

### Corollary 3.2 (stable-bank collapse)

Fix one residual anchor edge `a=(S,I)`.  Every run/guard conflict in any
collection which contains `a` and whose component signature extends the
shore bit of `a` lies in the single packet

\[
                         (\{\kappa(a)=\epsilon(a)\},\{S\},\mathcal C_a).
                                                               \tag{3.6}
\]

Its exact target cost is at most `1/2`.  If the two shore edges at target
`S` both anchor such collections, their union costs at most one, not the
number of arities, compositions, or labels in those collections.  A common
anchor costs one.

#### Proof

Every displayed conflict contains the anchor target `S` and requires the
anchor shore bit.  Apply one packet, then (3.2).  Complementary shore
cylinders at the same target have union probability one.  QED.

This disposes of raw exponential stable-bank multiplicity for a fixed
anchor target.  It does **not** bound the number of anchor targets.  In
particular there are `Theta(k^2)` rank-two target parts, and omitting all of
them is incompatible with an additive `O(k)` theorem.

## 4. Exact repair invariant and the two-shore trap

For a cube point `z`, let `mathcal C(z)` be its occurring conflict
hypergraph on target parts and put

\[
 \tau(z)=\min\{|D|:D\subseteq\mathcal T,
                    D\cap T(F)\ne\varnothing
                    \text{ for every }F\in\mathcal C(z)\}.         \tag{4.1}
\]

Define the exact existential repair number and its cube average by

\[
 \tau_\triangle=\min_z\tau(z),\qquad
 \mathcal A_\triangle=2^{-|\mathcal K|}\sum_z\tau(z).              \tag{4.2}
\]

Every complete packet family satisfies

\[
 \tau_\triangle\le\mathcal A_\triangle\le\Pi(\mathcal P).        \tag{4.3}
\]

The exact two-matching existential invariant is `tau_triangle`; the average
`mathcal A_triangle` and packet pressure are successively weaker checkable
upper certificates.  In particular

\[
 \nu(k)\le B(k)+|O_{cl}|+\tau_\triangle.                            \tag{4.3a}
\]

### Definition 4.1 (two-shore trap)

Let `K in mathcal K`.  A two-shore trap on `K` is a pair of physical
conflicts `F^0,F^1` such that

\[
 \operatorname{dom}\sigma_{F^b}\subseteq\{K\},
 \qquad \sigma_{F^b}(K)=b\quad(b=0,1).               \tag{4.4}
\]

Common edges may occur in either conflict.  A family of traps is
target-disjoint when the sets

\[
                         T(F_i^0)\cup T(F_i^1)                      \tag{4.5}
\]

are pairwise disjoint.

### Theorem 4.2 (trap-packing lower bound)

If the overlay contains `t` target-disjoint two-shore traps, then for every
cube point

\[
                         \tau(z)\ge t,                              \tag{4.6}
\]

and consequently

\[
 \tau_\triangle\ge t,\qquad
 \mathcal A_\triangle\ge t,
 \qquad \Pi(\mathcal P)\ge t.                                    \tag{4.7}
\]

for every complete packet family.

#### Proof

For trap `i`, the conflict `F_i^(z_(K_i))` occurs: it asks only for the
chosen shore of `K_i` and common edges.  The selected conflicts for
different traps have disjoint target sets by (4.5), so every target hitting
set contains at least one target for each trap.  This proves (4.6), and
taking the minimum and averaging prove the first two inequalities in
(4.7).  Inequality (4.3) proves the third.  QED.

Because the mandatory-core PBBS conflict hypergraph has girth two, the
smallest trap has two size-two conflicts.  Its alternating component may
be a four-edge path or a four-cycle, with two selected target edges on each
shore.  The exact PBBS certificate is finite and symbolic:

1. all four shore edges pass
   `F(I) subseteq S subseteq P(I)`;
2. each shore pair satisfies one of the exact pair-conflict conditions
   (central cover, first positive guard, or second positive guard);
3. both shore partial matchings extend in the same closed residual face.

Ordinary degree-one/forced-candidate propagation need not remove this
pattern; complete failed-literal lookahead may remove it, as Proposition
4.3 illustrates.  Every two-shore trap attaining the minimum possible two
edges on each shore has precisely this form after common deterministic
edges are contracted.  Hence excluding
superlinear target-disjoint trap packings is a necessary part of any
component-cube `B(k)+O(k)` theorem.  Counting components, checking every
single shore separately, or bounding conflict arity does not exclude it.

### Proposition 4.3 (smallest abstract residual core)

Let the residual graph have two target parts `S_1,S_2`, two interval
columns `I_0,I_1`, and all four candidate edges.  Declare exactly the two
diagonals

\[
 \begin{aligned}
 F^0&=\{(S_1,I_0),(S_2,I_1)\},\\
 F^1&=\{(S_1,I_1),(S_2,I_0)\}
 \end{aligned}                                                        \tag{4.8}
\]

to be physical conflicts.  Then both target parts and both columns have
two choices, ordinary degree-one/forced-candidate propagation fixes or
forbids no candidate, and the two
target-saturating matchings are `F^0,F^1`.  Their component cube has

\[
                         \tau(0)=\tau(1)=1.                         \tag{4.9}
\]

This is the smallest counterexample, with no fixed common conflict, to any
claim that a nontrivial two-matching cube automatically contains a
compatible selector.

#### Proof

The candidate graph is one alternating four-cycle.  Its only two perfect
matchings are the two diagonals, and each is declared conflicting.  Each
target row retains two graph candidates, so ordinary degree-one/forced
unit propagation alone has no move.  One
target deletion hits the selected diagonal, while zero deletions do not;
this proves (4.9).  Conflict girth two shows that no physical residual core
with fewer selected candidates can have this shore-changing property in
the absence of a fixed common conflict.  QED.

For an actual PBBS occurrence, (4.8) is not a free declaration: all four
candidate sandwiches and both instances of the exact pair-conflict normal
form must be checked, and both diagonals must extend in the residual face.
Thus Proposition 4.3 is an abstract sharp counterexample and Definition
4.1 is the fail-closed PBBS certificate once a trap is present in the
overlay.  Complete failed-literal or arc-consistency lookahead rejects the
isolated core (4.8), because neither candidate belongs to a compatible full
transversal of that core.  The proposition therefore does not assert that
this isolated rectangle, or any such rectangle, survives a stronger PBBS
closure.

### Proposition 4.4 (dead reciprocal rectangle certificate)

Let `S!=R` be residual strict-lower targets and `I!=J` residual columns.
Assume all four candidates `(S,I),(S,J),(R,I),(R,J)` survive.  Put
`E_x={p:x in P_p}` and let `D_x^0` be the fixed negative background from
the forced family.  Suppose some
coordinate `x` and middle index `t` satisfy `x in T_t minus (S union R)`
and, with

\[
 U=(E_x\cap[t,t+d])\setminus D_x^0,
\]

one has

\[
 U\subseteq I\cup J,qquad U\nsubseteq I,qquad U\nsubseteq J.      \tag{4.10}
\]

Then both diagonal pairs in (4.8) are the residual parts of contracted
central-run conflicts.  For each diagonal, choose an inclusion-minimal
subfamily of deterministic negative-background candidates which completes
the cover, and adjoin it to obtain a lifted physical conflict.  If these
two lifted conflicts are the two shores of one alternating component in
the chosen overlay, they form a two-shore trap.  Consequently `N` such
rectangles whose **full lifted conflict target sets** are pairwise disjoint
force `tau_triangle>=N`.

#### Proof

Every one of the four labels omits `x`.  On either diagonal, the two
selected intervals together with `D_x^0` delete `x` throughout the
derivative window `[t,t+d]`, although neither residual selected interval
does so by itself.  Delete redundant fixed-background candidates until the
full cover is inclusion-minimal.  The exact run normal form gives the
claimed lifted conflicts.  The trap and packing conclusions are Theorem
4.2.  QED.

The four candidate sandwiches themselves are equivalent to

\[
 F(I)\cup F(J)\subseteq S\cap R,qquad
 S\cup R\subseteq P(I)\cap P(J).                    \tag{4.11}
\]

Thus (4.10)--(4.11), plus residual survival and extendability of both
diagonals, are a finite symbolic PBBS obstruction certificate.  Existing
all-depth support and ordinary Hall do not exclude a packing of these
certificates.

## 5. Return-free flat hulls have no external links

The component cube is built from the interval-link graph: two interval
columns are linked when one retained target has candidates on both.  The
mandatory cores impose a strong deletion-stable restriction on this graph.

Call an index interval `H=[u,v]` a **flat hull** when every `P_p`, `p in H`,
has the same interior erosion rank and consecutive states are distinct
Johnson neighbours.  Call it **return-free** when, for every coordinate
`x`, the set

\[
                         \{p\in H:x\in P_p\}                         \tag{5.1}
\]

is an interval (possibly empty).  Thus no erosion coordinate disappears
and later reappears inside `H`.

### Theorem 5.1 (return-free link rigidity)

Let `I=[a,b]` and `J=[c,e]` be two interval columns contained in one
return-free flat hull.  If one target `S` is a retained candidate on both
columns, then

\[
                         I=J.                                      \tag{5.2}
\]

The conclusion survives arbitrary target, column, and candidate deletion.

#### Proof

Common candidacy gives

\[
 F(I)\cup F(J)\subseteq S\subseteq P(I)\cap P(J).                  \tag{5.3}
\]

Suppose first that `a<c`.  Flatness and strict residence make
`P_a,P_(a+1)` distinct equal-rank Johnson neighbours, so choose

\[
                         x\in P_a\setminus P_{a+1}.                 \tag{5.4}
\]

Then `x in F_a subseteq F(I) subseteq P(J)`.  Hence `x in P_q` for
some `q in J`, where `q>=c>a`, although `x notin P_(a+1)`.  The set
in (5.1) is therefore not an interval, contrary to return-freeness.
Interchanging `I,J` excludes `c<a`, so `a=c`.

Now suppose `b<e`.  Choose

\[
                         y\in P_e\setminus P_{e-1},                 \tag{5.5}
\]

again using flatness.  Then `y in F_e subseteq F(J) subseteq P(I)`,
so `y in P_p` for some `p<=b<e`, while `y notin P_(e-1)`.  This is a
second return, contradicting (5.1).  Symmetry excludes `e<b`; hence
`b=e`.  Deleting graph data cannot create a common candidate, so the
statement is deletion-stable.  QED.

### Corollary 5.2 (return/ramp necessity for switching)

The interval-link graph induced by columns contained in one return-free
flat hull has no edge between distinct columns.  Therefore every
nontrivial alternating component, external guard bridge, or two-shore trap
which changes an interval column must either

1. leave that hull;
2. meet an erosion ramp; or
3. certify a coordinate return in the convex hull of its two alternative
   columns.

In particular no two-shore trap is supported wholly inside a return-free
flat hull.

This is an actual PBBS obstruction to a purely local external-bridge
supply.  It does not bound the number or congestion of return certificates
in the full PBBS chronology; such a bound is still needed for a global
positive or negative theorem.

## 6. A run-specific fixed obstruction

There is a second, simpler certificate which is useful when the two
matchings have common edges.  Let `x` be a coordinate, and suppose
`F_1,...,F_t subseteq M^0 cap M^1` are central-run conflicts whose target
sets are pairwise disjoint.  Then every cube point contains all `F_i`, so

\[
                         \tau(z)\ge t.                              \tag{6.1}
\]

For example, if `t` pairwise target-disjoint families of common negative
candidate intervals minimally cover `t` central `d+1` windows, they give
such a certificate.  This is the exact **common-run packing number**.

The mandatory run-boundary theorem rules out unary members of this packing
but does not bound its size.  Therefore choosing two matchings with a large
common edge set is not harmless: a component cube randomizes no common-run
conflict.  A positive PBBS overlay theorem must bound both the common-run
packing number and the two-shore trap packing number by `O(k)`, or provide a
stronger packet cover which hits them with `O(k)` shared targets.

## 7. Pascal transfer with a merger ledger

For a packet family write

\[
 \overline\Pi(\mathcal P)=
 \sum_S\min\left\{1,
   \sum_{a:S\in H_a}2^{-|\sigma_a|}\right\}.                         \tag{7.1a}
\]

Thus `Pi(mathcal P)<=overline Pi(mathcal P)` by (3.3).  Consider a parent
component cube and a child cube obtained after a Pascal
transport.  Assume the transported child targets have a projection `pi`
to parent targets with fibres of size at most `g`.  Assume also that for
every transported child target `S'`, its total lifted packet-incidence
weight obeys

\[
 \sum_{\widehat a:S'\in H_{\widehat a}}
       2^{-|\widehat\sigma_a|}
 \le 2^h
 \sum_{a:\pi(S')\in H_a}2^{-|\sigma_a|}.             \tag{7.1}
\]

For example, (7.1) holds when each relevant parent packet has at most one
lift in each target channel and every lifted signature loses at most `h`
component bits.

Assume every child conflict not covered by these lifted packets is covered
by a new packet family whose union-bound pressure is at most `L`.

### Theorem 7.1 (bounded-merger Pascal transfer)

Under the displayed hypotheses,

\[
 \Pi_{\rm child}\le\overline\Pi_{\rm child}
 \le g\,2^h\overline\Pi_{\rm parent}+L.                          \tag{7.2}
\]

Thus constant `g`, `h=O(1)`, `overline Pi_parent=O(k)`, and `L=O(k)`
preserve an additive `O(k)` compiler bound.

#### Proof

Insert (7.1) into the capped union bound (3.3).  The elementary inequality

\[
                         \min(1,2^hu)\le2^h\min(1,u)                \tag{7.4}
\]

gives at most `2^h` times the parent capped load for each child target.
There are at most `g` child targets above each parent target, so the lifted
total is at most `g 2^h overline Pi_parent`.  Add the pressure `L` of the
new packets.  QED.

If the child overlay starts as a component-faithful, channelwise-unique
lift with target projection fibre at most `g`, and then performs `h` binary
component mergers (equivalently, if every lifted signature loses at most
`h` component bits), (7.1) holds: one binary merger reduces the number of
component blocks met by any signature by at most one.
Splitting a parent component only increases signature rank and cannot hurt
(7.2).

The known binary Pascal facet/union transducers have constant target-channel
multiplicity on unbraided interiors and preserve envelope candidates and
mandatory event ports there.  This transports the **incidence** part of an
interior packet.  It does not prove that promoted
collars merge only `O(1)` alternating components, nor does it packet-cover
new mixed-shore run/guard conflicts with `L=O(k)`.  In the `e=d-1` scalar
phase branch, even the number of Pascal runs may grow with `W`; no bounded
`h` follows.  Hence current odd/even identities do not preserve the
component-pressure hypothesis unconditionally.

## 8. Proved and unproved boundary

Proved:

1. exact deletion-stable component-rank cylinder probabilities, with
   universal `C_0=2` for every conflict arity;
2. an exact signature-packet target-cover theorem which groups exponentially
   many conflicts before paying a target;
3. the minimum repair number `tau_triangle` as the exact component-cube
   alteration invariant, with average repair and packet pressure as upper
   certificates;
4. a smallest two-shore trap and a target-disjoint trap-packing lower bound;
5. deletion-stable return-free link rigidity and the resulting necessity
   of a return/ramp certificate for every nonlocal switch;
6. the common-run packing lower bound; and
7. a quantitative Pascal transfer theorem with explicit component-merger
   loss and new-collar packet pressure.

Not proved:

1. no construction yet supplies two fully closed PBBS matchings whose
   minimum repair number, average repair, or complete packet pressure is
   `O(k)`;
2. unit closure alone does not exclude two-shore traps or common-run
   packings;
3. no theorem bounds the number of active rank-two stable anchors by
   `O(k)` or gives them a shared target packet cover; and
4. the existing odd/even Pascal braid does not bound the component-merger
   ledger or the promoted-collar packet pressure.

Therefore no unconditional `B(k)+O(k)` follows.  The exact positive gate is
now sharper than generic capped pressure: construct one fully closed PBBS
overlay with a complete signature-packet cover of pressure `O(k)` (or prove
directly `tau_triangle=O(k)`) and with no superlinear two-shore/common-
run trap packing; for even dimensions, retain bounded merger loss and
`O(k)` new-collar packet pressure.
