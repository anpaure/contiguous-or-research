# Heptagonal cap/history product monoid and the regenerative selector gate

**Date:** 2026-08-02  
**Status:** unconditional cap-current, backup, and history-composition
theorems; conditional protected Pascal/pull-ear regeneration.  The
heptagonal central packet supply is taken from
`MATH_THEOREM_HEPTAGONAL_CAP_CIRCULATION_AND_PROSPECTIVE_ABUNDANCE_20260802.md`.
This note does not infer a physical host from that prospective supply.

## 0. Outcome

The raw central circuit menu is not the next bottleneck.

For a selected physical circuit, let `mu^-` and `mu^+` be its old and new
literal immediate-upper cap multiplicities.  On a common free equivariant
cap face the same data may be quotient cap-orbit multiplicities.  Its exact
cap current is

\[
             \delta=\mu^+-\mu^- .                       \tag{0.1}
\]

For an ordered packet, two data are sufficient for every prefix cap test:

\[
 (\Delta,b),\qquad
 \Delta=\hbox{terminal cap current},\qquad
 b=\hbox{least initial duplicate-cap slack}.             \tag{0.2}
\]

They form an exact monoid.  If packet `A` is followed by packet `B`, then

\[
 (\Delta_A,b_A)\star(\Delta_B,b_B)
 =\bigl(\Delta_A+\Delta_B,
        \max\{b_A,b_B-\Delta_A\}\bigr),                 \tag{0.3}
\]

where the maximum is coordinatewise over literal caps (or free cap orbits).
Thus a balanced
packet has `Delta=0`; it is cap-safe from a prepared slack vector `s`
exactly when `s>=b`.

The boundary-history state is another exact relation monoid.  It cannot be
discarded after solving (0.3): cap pairing shifts act on coordinate labels,
and residence depends on their relative phases.  The protected recursive
state must therefore contain

\[
 \boxed{(\text{payload/topology},h;\Delta,b;
         \mathcal R_d^+,\mathcal R_d^-;\mathcal P)},     \tag{0.4}
\]

where `h` is holonomy, the two `mathcal R` are the positive and negative
directed-history relations, and `mathcal P` is the private physical-resource
bank.

The one-aperture pivot is useful here for a precise reason: its **positive**
insertion history is a constant-output reset.  A cap-balanced heptagonal
packet which accepts that output and returns to its input guard can be
sandwiched between two reset copies and exports the same positive-history
state.  Biresidence additionally needs a supplied dual/reversed reset; it
does not follow from the co-oriented pivot alone.  Under that explicit
hypothesis the same sandwich is a literal conditional regenerative macro.
What remains is to plant the duplicate-cap backup and both boundary-history
tickets jointly.

## 1. Exact cap current and backup demand

Let `Omega` be the required **literal physical cap** universe of an
upper-complete factor `F`.  Write

\[
 M_F(O)\ge1,\qquad s_F(O)=M_F(O)-1                       \tag{1.1}
\]

for its cap load and duplicate slack at `O in Omega`.  If every cap orbit
used in an equivariant quotient is free and has one common size, `O` may
instead denote a quotient cap orbit and the equations divide by that common
size.  Shortened cap orbits must be expanded physically or assigned their
orbit-size weights; unweighted quotient arithmetic is then invalid.

For an atomic circuit `e`, let `mu_e^-(O)` and `mu_e^+(O)` count the old and
new selected rows having literal cap `O`, and put

\[
 \delta_e(O)=\mu_e^+(O)-\mu_e^-(O).                     \tag{1.2}
\]

The old and new row counts agree, so

\[
                       \sum_O\delta_e(O)=0.             \tag{1.3}
\]

### Proposition 1.1 (one-atom backup formula)

Applying `e` as one simultaneous circuit preserves cap support iff

\[
                      s_F+\delta_e\ge0                  \tag{1.4}
\]

coordinatewise.  The number of duplicate slack units which its negative
cap current must move is

\[
 \beta(e)=\sum_O(-\delta_e(O))_+
         ={1\over2}\|\delta_e\|_1.                     \tag{1.5}
\]

In particular `beta(e)=0` iff the old and new literal cap multisets agree.

#### Proof

The final cap load is

\[
 M_{F^e}=M_F-\mu_e^-+\mu_e^+=1+s_F+\delta_e.
\]

This proves (1.4).  Equation (1.3) makes the total positive and negative
parts of `delta_e` equal, proving (1.5). \(\square\)

The phrase “one backup” means one unit of duplicate load at the named cap
orbit, not a separately constructed packet.  If `delta_e(O)=-q`, then the
old load at `O` must be at least `q+1`; one baseline occurrence remains and
`q` duplicate units are transported away.

### Proposition 1.2 (exact prefix-backup monoid)

For an ordered packet word

\[
                         P=e_1e_2\cdots e_t,             \tag{1.6}
\]

put

\[
 \Delta_P=\sum_{j=1}^t\delta_{e_j},\qquad
 b_P(O)=\max_{0\le p\le t}
       \left(-\sum_{j=1}^p\delta_{e_j}(O)\right)_+ .    \tag{1.7}
\]

Every prefix of `P` is cap-safe from initial slack `s` iff `s>=b_P`.
Moreover concatenation obeys (0.3).

#### Proof

After prefix `p`, the slack is

\[
              s+\sum_{j=1}^p\delta_{e_j}.
\]

Nonnegativity for every prefix is exactly `s>=b_P`.  A prefix of `AB` is
either a prefix of `A`, or all of `A` followed by a prefix of `B`.  The two
corresponding requirements are `b_A` and `b_B-Delta_A`; taking their
coordinatewise maximum gives (0.3). \(\square\)

Thus `(Delta,b)` is a Markov-sufficient cap state.  A **balanced private
backup packet** is a word with

\[
                         \Delta_P=0,\qquad b_P\le s_F,   \tag{1.8}
\]

whose rows and designated backup occurrences avoid every protected
resource.  It returns the complete cap-load vector exactly and can be
reused by the recurrence.  A weaker recurrence may allow a prescribed
permutation of `s_F`, but that permutation must be part of the state.

## 2. How much cap slack exists, and what this does not prove

There is an exact scalar reserve in the odd Middle-Levels owner layer.

### Theorem 2.1 (global duplicate-cap reserve)

Let `k=2r-1`, let

\[
                         W={2r-1\choose r},              \tag{2.1}
\]

and let `F` be a degree-two factor on all rank-`r` owners which is complete
on the rank-`(r+1)` cap palette.  Then

\[
 \sum_{U}\bigl(M_F(U)-1\bigr)
   =W-{2r-1\choose r+1}
   ={2W\over r+1}.                                      \tag{2.2}
\]

Every cap has load at most `r+1`, so at least

\[
                         {2W\over r(r+1)}               \tag{2.3}
\]

cap targets have positive duplicate slack.

#### Proof

A degree-two factor on `W` vertices has `W` edges, hence total cap load
`W`.  The ratio

\[
 { {2r-1\choose r+1} \over {2r-1\choose r} }
 ={r-1\over r+1}
\]

gives (2.2).  For a fixed cap `U`, all selected edges with union `U` lie
in the complete graph on the `r+1` owners `U-{u}`.  Their selected degree
is at most two at each owner, so there are at most `r+1` such edges and at
most `r` slack units.  Dividing (2.2) by `r` proves (2.3). \(\square\)

For an equivariant action, the same statements divide by the orbit size
only on a common free owner/edge/cap face.  With shortened cap orbits one
must retain orbit-size weights or expand physically.  At `k=17,r=9` every
nonempty proper `Z_17` subset orbit is free, and the physical slack is

\[
                 24310-19448=4862,                      \tag{2.4}
\]

and the `Z_17` quotient slack is `286`.  Hence at least `ceil(286/9)=32`
quotient cap orbits must have positive slack; the authenticated 2,754
factor has `160`.

This scalar theorem does **not** plant a heptagon.  The debit cap orbits of
all candidates rooted at one required defect can avoid the slack support,
and their acceptable boundary histories can be concentrated on a different
subfamily.  The needed assertion is a correlated intersection theorem, not
another count of total cap excess.

## 3. Holonomy makes the correlation unavoidable

For a quotient circuit with row increments `a_i`, let

\[
                         h=\sum_i a_i\pmod m.            \tag{3.1}
\]

The developed moving graph has `gcd(m,h)` components.  Cap multiset
equality is equivalent to matching the old and new quotient cap entries by
a row permutation and phase shifts.

For the natural successor matching with retained labels `z_i`, cap equality
forces

\[
                         z_i=\rho^{a_i}z_{i+1}.          \tag{3.2}
\]

Around the heptagon this gives `z_0=rho^h z_0`.  Under a free coordinate
action, a coprime nonzero `h` is therefore impossible on this fixed-label
face.  A topology-useful developed packet must instead have a nontrivial
cap permutation, use duplicate slack according to Section 1, or close its
cap current only in a larger compound return.

The fixed-`z` phasewise `C14` atlas has `Delta=0` but `h=0`.  Its
`Theta(k^7)` rooted count closes central local supply only.  The twisted
seven-run expression

\[
 {r-1\choose6}{k-r-1\choose6}(7!)^2\,\Omega(k)^7        \tag{3.3}
\]

counts prospective coprime-voltage geodesic sockets.  It does not by itself
give cap closure, free developed resources, host exposure, or an accepting
history.

For the authenticated `k=17` 2,754 packet, `h=5`.  Four of seven cap orbits
are transported.  Its cap current has three negative entries, at

\[
                         13783,27447,28075,              \tag{3.4}
\]

and three positive entries, at

\[
                         13727,28331,43755.              \tag{3.5}
\]

Every negative orbit has incumbent load two.  Hence `beta=3` and (1.4)
passes exactly.  This is a certificate of three available slack units, not
a theorem that three independent backup macros have been planted.

## 4. Boundary histories and the product transition

Fix residence depth `d`.  Let `mathscr H_d` be the finite state space of
**endpoint-realizable joint sockets**: it stores the newest `d` insertion
labels and the dual deletion history, with the appropriate frame/coset
field, and retains the requirement that recent insertions are present while
recent deletions are absent at the common endpoint.  A directed physical path or bounded
retained-path packet `P` induces a partial relation

\[
                         \mathcal R_P\subseteq
                    \mathscr H_d\times\mathscr H_d.     \tag{4.1}
\]

It contains both polarities.  Relations compose under concatenation, and a
closed chronology is bi-resident exactly when the composed relation has a
consistent fixed point.  For the seven retained paths of a heptagonal
rethread, this is equivalently the two-polarity transfer tuple in the
boundary-history theorem.

Cap pairing phase shifts act diagonally on every coordinate label in
`mathscr H_d`.  Consequently cap multiset closure does not imply history
closure: different row shifts realizing the same cap pairing can give
different deletion/insertion collisions at a join.  The relative shifts,
or the resulting relation (4.1), are load-bearing state.

### Theorem 4.1 (exact cap/history product state)

Associate to every protected atomic packet `e` the cap descriptor
`(delta_e,(-delta_e)_+)` and its phase-correct history relation
`mathcal R_e`.  Then an ordered word `P=e_1...e_t` is prefix-cap-safe and
history-compatible from `(s,H)` to `(s',H')` iff

\[
 s\ge b_P,\qquad s'=s+\Delta_P,                         \tag{4.2}
\]

and there are histories

\[
 H=H_0,H_1,\ldots,H_t=H'
 \quad\hbox{with}\quad
 (H_{j-1},H_j)\in\mathcal R_{e_j}.                      \tag{4.3}
\]

Thus the product of the cap monoid (0.3) and phase-correct relation
composition is exact.  Feasibility of either projection separately is not
sufficient.

#### Proof

Equation (4.2) is Proposition 1.2.  Equation (4.3) is the definition of
relational composition and is exact because the retained history state is
Markov-sufficient at each boundary.  Both conditions use the same selected
packet word, so their conjunction is necessary and sufficient. \(\square\)

### Corollary 4.2 (endpoint-realizable connector abundance)

Suppose a cap `U` of size `n` and two internally biresident collars have
been supplied.  Let `H_I,H_D` be the recent insertion/deletion collars at
the left endpoint and `F_D,F_I` the future deletion/insertion collars at the
right endpoint.  A connector

\[
                  U-\alpha\longrightarrow U-\beta     \tag{4.4}
\]

with `alpha!=beta` realizes those literal endpoints and is biresident iff

\[
 H_I\cup F_D\subseteq U,\qquad
 (H_D\cup F_I)\cap U=\varnothing,                      \tag{4.5}
\]

the old positive and negative cross-collar inequalities hold, and

\[
 \alpha,\beta\in W_U:=U-(H_I\cup F_D),\qquad
 \alpha\ne\beta.                                      \tag{4.6}
\]

When the first two conditions hold, the exact number of oriented choices is

\[
                         |W_U|(|W_U|-1),                \tag{4.7}
\]

and it is at least `(n-2d)(n-2d-1)` when `n>=2d+1`.

#### Proof

Recent insertions and future deletions must be present in the respective
endpoints, while recent deletions and future insertions must be absent.
The two endpoints omit exactly `alpha` and `beta`; the connector event then
forces both missing labels outside the positive collars.  This is exactly
(4.5)--(4.6).  Any ordered pair of distinct elements of `W_U` works, giving
(4.7). \(\square\)

Thus a supplied central cap and endpoint-realizable aligned collars have
`Theta(k^2)` raw connectors in the central regime.  This closes the final
two-label choice, not endpoint-owner privacy, the lower colour, or the
task-to-cap/history alignment which is missing in Section 7.

## 5. Integration with the one-aperture Pascal reset

Let `Pi^+` be the protected one-aperture pivot.  On the positive history it
has a triangular input guard `G^+` and constant output

\[
                  H_*^+=(\mu,\rho_{d-1},\ldots,\rho_1). \tag{5.1}
\]

The co-oriented pivot does not determine the future-deletion state at its
exit, so its negative-history output is not automatically a reset.  Assume
separately that a literal reversed/dual module `Pi^-` supplies an input
guard `G^-` and constant output `H_*^-`.  Write `Pi` for the resulting
protected bi-history reset.  Its actual entrance domain is the subset
G_joint of endpoint-realizable joint sockets whose positive and negative
projections lie in G^+ and G^-, respectively.  It is not the unrestricted
Cartesian product.  Assume the constant output H_* belongs to that same
joint state space.  In symbols,

\[
 G_{\rm joint}=\{(H^+,H^-)\in\mathscr H_d:
                   H^+\in G^+,\ H^-\in G^-\}.         \tag{5.2}
\]

### Theorem 5.1 (balanced reset sandwich)

Assume the two copies of the **bi-history reset** `Pi` are literal, private,
and cap-neutral on the complete upper-cap universe claimed by the recursive
class.  Its positive half is the
one-aperture pivot and its negative half is the separately supplied
dual/reversed reset above.  Let `P` be a protected heptagonal/pull-ear packet
such that

\[
 \Delta_P=0,\qquad b_P\le s_F,                           \tag{5.3}
\]

and

\[
       \mathcal R_P(H_*)\cap G_{\rm joint}\ne\varnothing. \tag{5.4}
\]

Then the chronological macro

\[
                         \Pi\;P\;\Pi                    \tag{5.5}
\]

returns the cap slack and exports the same constant history state `H_*`.
If its port square, payload, protected resources, and topology opening also
return, it is a regenerative protected Pascal/pull-ear macro.

#### Proof

The first pivot sends every allowed input to `H_*`.  By (5.4), `P` sends
`H_*` to some state in `G_joint`, so the second pivot is legal and resets that
state to `H_*`.  Equations (5.3) and Proposition 1.2 preserve every cap at
every prefix and return the initial slack vector.  The remaining rows are
explicit hypotheses because neither cap nor history composition controls
them. \(\square\)

One physical reset module may serve simultaneously as the terminal reset of
one recursive node and the initial reset of the next.  This can keep the
number of *live* boundary interfaces bounded.  It does not prove the
one-star source consolidation required by the conditional `B+1` bridge, it
does not make two separately inserted pivot cells into one letter, and it
does not manufacture the missing dual reset.

## 6. Exact selector gate and the conditional greedy consequence

For a prepared defect anchor `t`, let `A_t(s,H_*)` be the set of complete
occurrence-labelled heptagonal or compound tickets which simultaneously:

1. preserve the declared owner/facet/lower payload and private port bank;
2. have the required topology/holonomy;
3. satisfy `Delta=0`, `b<=s`, or belong to a declared bounded compound
   whose terminal descriptor does;
4. satisfy the phase-correct history return (5.4); and
5. carry every protected deeper-upper, source, and compiler resource that
   the chosen recursive class declares.

This is the correct candidate list.  The raw `Theta(k^7)` fixed-`z` atlas is
only its central projection.

### Proposition 6.1 (complete-ticket greedy lemma)

Suppose `H` prepared anchors are to be served.  Assume every live anchor
has at least `L` complete tickets in `A_t(s,H_*)`, and one selected complete
ticket conflicts with at most `Delta` tickets at any other anchor.  If

\[
                         L>(H-1)\Delta,                  \tag{6.1}
\]

then pairwise-compatible complete tickets exist for all anchors.

#### Proof

Choose anchors in any order.  Before the `j`th choice, at most
`(j-1)Delta` of its tickets have been deleted, which is less than `L`.
Choose any survivor. \(\square\)

The heptagonal theorem supplies `L=Theta(k^7)` and `Delta=O(k^6)` only for
central named tokens.  If the same estimates held after conditioning on
balanced backups and boundary histories, with `O(d)` extra resources per
ticket, then `Delta=O(dk^6)` and (6.1) would serve every fixed `H`, more
generally every `H` with `Hd=o(k)`.  This conditional implication is exact.
The full-ticket estimates are the missing theorem.

## 7. Sharp remaining lemma

The next all-`k` target is not another central `C14` enumeration.  It is:

> **Balanced backup-history planting.**  In the prospective protected
> Pascal/pull-ear host, expose for each required anchor a positive-density
> subfamily of topology-useful heptagonal or bounded compound packets whose
> cap descriptors admit a common balanced backup bank and whose
> phase-correct two-polarity history relations accept the prepared pivot
> reset.  The complete occurrence/resource load must remain one power of
> `k` below the rooted list size.

Equivalently, prove the complete-ticket hypotheses of Proposition 6.1, or
construct a bounded cap/history return directly in the lifted product
state of Theorem 4.1.

Three marginal facts do not suffice:

1. total cap slack (Theorem 2.1) does not force it onto candidate debit
   cap orbits;
2. cap exactness does not fix the relative phase at history joins; and
3. prospective seven-run/geodesic abundance does not expose the retained
   paths in one incumbent host.

Upper ranks beyond the immediate cap row, source-envelope binding,
one-star consolidation, exterior opening, and the terminal common-cap
compiler remain separate accepting coordinates.  No `B+1`, `B+O(1)`, or
exact formula follows until this correlated planting lemma and those rows
are proved.

Finally, the history interface is uniform in form but not constant-size as
the residence depth grows.  It carries `d` recent labels in each polarity,
and the known no-section theorem prevents recovering depth `d+1` from a
depth-`d` state without one new oldest label or a certified reset with its
larger entrance guard.  The product monoid closes composition at each
declared depth; it is not a bounded-state all-depth existence theorem.
