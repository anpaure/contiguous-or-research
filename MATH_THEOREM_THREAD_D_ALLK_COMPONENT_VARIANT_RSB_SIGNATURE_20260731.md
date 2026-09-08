# Local complement variants: an exact all-dimension RSB signature algebra

Date: 2026-07-31  
Lane: D, complement-bank physicalization  
Status: exact local factorization, exact contextual quotient, and exact
closure theorem; no uniform variant-supply theorem and no `K17` word claim

## 0. Result and scope

Fix an odd dimension

\[
             k=2r+1,\qquad W={k\choose r},
\]

and the depth-two zipper architecture.  Its row has length `W+1`; a row
token has rank `r+1` in the owner bank and rank `r` in the facet bank.  A
literal component split/rethread can be represented exactly by a product of
oriented old-fragment atoms and new-bridge atoms.  The product has the
following interface:

\[
 \boxed{
 \Sigma(V)=
 (\partial V,\rho V,{\mathfrak D}_2V,
  {\mathfrak U}V,\lambda V,{\mathfrak C}V,\kappa V).}
                                                               \tag{0.1}
\]

The seven fields are, respectively,

1. oriented physical sockets and two-token row collars;
2. exact occurrence-resource flux;
3. the exact depth-two residence/inversion monoid;
4. exact accumulated-union transfers for the live upper targets;
5. exact lower-palette flux;
6. the projected maximal-common-cap collar relation; and
7. owner-token, direct-facet, cell, and scalar-slack currents.

All seven operations are associative.  A collection of local variants and
bridges physicalizes the complementary bank if and only if their signature
product has the required root value.  Consequently a catalogue may retain
one witness per reachable signature without losing any solution admitted by
this interface.  Under formal RSB continuations which may test every exposed
resource, automaton state, and cap valuation, no two different signatures
may be identified.

There is an exact prefilter before this quotient.  Every immutable owner-run
defect gives an interval of old component edges which a split/rethread must
touch.  These intervals form an interval hypergraph; its minimum cut-support
problem is integral and is solved by the ordinary greedy interval-stabbing
algorithm.  Hitting the intervals is necessary, not sufficient: new joins
can create new short runs and can fail shadows or the common cap.

For the frozen `K17` OPTIMAL28 complement this proves that an exact catalogue
must contain genuinely internal columns.  The `724` bad runs in `257`
components cannot be changed by socket reassignment.  With the `4108`-owner
bank fixed, all `257` defective components need a nonidentity local option.
On the weaker wholesale-migration face, the already proved scalar ledger
still forces at least `82+24=106` nonidentity components.  The theorem below
does not construct those options.

The signature is local in **arity**, not uniformly finite in dimension.
Residence, ports, collars, and additive current have bounded structural
width.  Exact palette labels, arbitrary-width upper targets, and unrestricted
common-cap target identities form growing banks.  A dimension-uniform
induction therefore needs locally zero-flux variants and either protected
upper witnesses plus a guarded compiler face, or a separate bounded-adhesion
theorem.  Rank-three cap conflicts alone do not give bounded adhesion.

## 1. Component atoms and immutable-run hazards

Let

\[
                   C=(q_1,\ldots,q_s)                 \tag{1.1}
\]

be an oriented owner word in one complementary component.  Its internal
facet word is

\[
            \phi(C)=(q_1\cap q_2,\ldots,q_{s-1}\cap q_s). \tag{1.2}
\]

The two occurrence-labelled component ports are appended when the component
is inserted between its predecessor and successor.  A **split/rethread
support** consists of old adjacencies which are cut, owner occurrences which
are replaced, and new directed bridges.  Cutting (1.1) produces oriented
interval atoms; a rethread is an alternating product

\[
 F_1\,e_1\,F_2\,e_2\cdots e_{t-1}F_t,                \tag{1.3}
\]

where every `F_i` is one old interval in either orientation and every `e_i`
is a declared literal bridge.  Optional replacement atoms are treated as
new one- or multi-occurrence fragments with an exact signed resource ledger.

Fix a coordinate `x`.  Suppose that (1.1) contains the strict internal run

\[
 q_{j-1}(x)=0,\quad
 q_j(x)=\cdots=q_{j+\ell-1}(x)=1,\quad
 q_{j+\ell}(x)=0,                                    \tag{1.4}
\]

where `ell` is two or three.  Its **hazard interval** is the consecutive set
of old adjacencies

\[
 H(x,j,\ell)=
 \{q_{j-1}q_j,q_jq_{j+1},\ldots,
                q_{j+\ell-1}q_{j+\ell}\}.            \tag{1.5}
\]

An occurrence replacement at either endpoint of an edge in (1.5) counts as
touching that edge.

### Lemma 1.1 (immutable-run support theorem)

If a split/rethread support is disjoint from `H(x,j,ell)`, then the output
facet word still has a strict internal positive `x`-run of length
`ell-1`.  Hence an internally depth-two-legal facet variant must touch every
hazard interval, unless the entire component is removed from the facet bank.

#### Proof

If no edge of (1.5) is cut or rewritten, the whole literal collar

\[
                         0\,1^\ell\,0
\]

lies in one unchanged interval atom.  Reversing that atom preserves the
collar.  On taking consecutive intersections, its two zero boundary edges
remain zero and its `ell-1` internal edges are one.  Thus the facet word
contains `0 1^(ell-1) 0`, of length one or two.  This is a forbidden strict
internal run for exact depth-two inversion. \(\square\)

### Corollary 1.2 (integral hazard core)

For one linear component, the minimum number of old-edge cuts meeting all
hazard intervals equals the maximum number of pairwise edge-disjoint hazard
intervals.  Its linear relaxation is integral.

#### Proof

The sets (1.5) are intervals in the old edge order.  The interval--point
incidence matrix has the consecutive-ones property and is totally
unimodular.  Equivalently, repeatedly choosing the right endpoint of the
leftmost-ending unhit interval gives both a transversal and a disjoint-
interval certificate of the same size. \(\square\)

The corollary is only a support normal form.  Every valid support contains
an inclusion-minimal hazard transversal, but auxiliary cuts can be required
by palette, shadow, or cap constraints.  It is therefore unsafe to enumerate
only minimum transversals.  The exact enumeration is: select a hazard core,
allow the declared auxiliary support class, and quotient all resulting atom
products by (0.1).

## 2. The seven exact local fields

### 2.1 Ports and exact resources

The port field `partial V` contains the two oriented socket occurrences,
their rank-`r` physical labels, the first two and last two output row tokens,
and the bank mode of each endpoint.  A bridge atom records its literal owner
and both labels

\[
                    X\cap Y,\qquad X\cup Y.           \tag{2.1}
\]

The resource field is a signed occurrence-labelled multiset

\[
\rho V=(\Delta{\cal O},\Delta{\cal E},
          \Delta{\cal M},\Delta{\cal S},
          \Delta{\cal J},\Delta{\cal T}_{low}).       \tag{2.2}
\]

Here `O` contains middle-owner occurrences, `E` old/new edge occurrences,
`M` macro or optional-component occurrences, `S` socket occurrences, `J`
physical lower-cell occurrences, and `T_low` lower-target assignment
identities once assignments are sealed inside a block.  Addition is signed
multiset addition.  Protected marked-packet identifiers may not occur
negatively.  The root requires the exact desired occurrence deck, not merely
the correct cardinalities.  If the lower assignment is deferred rather than
sealed, its `J,T_low` variables remain exposed in the cap relation below.

### 2.2 The exact depth-two monoid

For a binary word `b`, store its initial and terminal positive-run lengths,
capped at three, its all-one flag, and whether it has a strict internal
positive run of length one or two.  Concatenate by joining the two boundary
arms, closing an arm when the other word begins or ends with zero, and then
truncating again at three.  This is the syntactic run monoid
`R_2` for the language with no short strict internal positive run.

Take its product over the `k` coordinates.  Append the literal-window
monitor which stores the first and last two row tokens and rejects an empty
adjacent-pair boundary intersection or an empty internal three-token
intersection.  Call the product

\[
                         {\mathfrak D}_2(V).          \tag{2.3}
\]

It is associative.  A complete row is accepted exactly when its maximal
three-window envelopes are all nonempty and reproduce every row token.
Indeed, nonemptiness is precisely the pair/triple monitor, while a
coordinate is reproduced at every row containing it exactly when each of
its strict internal runs has length at least three.  Boundary runs may be
short.  Once (2.3) accepts, the adjacent-OR derivative has every strict
internal run of length at least four, so no separate `D3` residence field is
needed for this flat depth-two interface.

The same definition with arm lengths capped at `d+1` gives the
dimension-independent formula for a depth-`d` run monoid.  Its structural
width per coordinate is constant for fixed `d`; the coordinate-labelled
product still grows with `k`.

### 2.3 Exact upper accumulated-union transfers

For an upper target `S`, use the deterministic automaton

\[
 {\cal A}_S=\{\bot,\checkmark\}\cup 2^S.              \tag{2.4}
\]

The accepting state is absorbing.  From a nonaccepting state, a token
`z` not contained in `S` resets to `bot`; a token contained in `S` starts or
extends the current accumulated union, and enters `checkmark` exactly when
that union is `S`.  The block transfer

\[
                   \tau_{S,V}:{\cal A}_S\to{\cal A}_S \tag{2.5}
\]

recognizes whether some interval ending in or before `V` has union `S`.
For the live target bank `H`, put

\[
                 {\mathfrak U}(V)=(\tau_{S,V})_{S\in H}. \tag{2.6}
\]

Composition is ordinary function composition.  Thus (2.6) is exact for
arbitrary interval width; fixed-width witness rows are not a substitute.
When a sealed baseline already covers `S`, its coordinate may be deleted
only if a protected occurrence-labelled witness remains sealed.

Equivalently, one may store total, prefix-OR chain, suffix-OR chain, and
internal union deck.  The cross term for `UV` is every suffix of `U` union
every prefix of `V`.  The automaton form is usually smaller once `H` has
been separated lazily.

### 2.4 Lower-palette flux

For every rank-`r` lower colour `c`, define

\[
 \lambda_V(c)=
 \#\{\hbox{new direct or bridge occurrences of }c\}
 -\#\{\hbox{deleted old occurrences of }c\}.          \tag{2.7}
\]

This is an integer vector, not a support size.  The fixed marked packet plus
all selected complement variants retain the lower palette exactly if and
only if the root flux is zero and every final occurrence multiplicity is
one.  A **palette-private** option has `lambda_V=0` locally.  Palette-private
options remove this entire growing bank from the intercomponent state;
merely having equal numbers of deleted and inserted colours does not.

### 2.5 Exact common-cap collar relation

Let `Phi_V` be the complete Boolean formula for the rows, maximal envelopes,
short prepins, selected singleton/pair lower cells, and common physical cap
inside `V`.  Expose:

* the two row tokens on each side;
* cap letters at positions within distance two of either boundary;
* every singleton/pair cell crossing a boundary;
* every live target-, cell-, and fixed-pin identity meeting those positions;
* every global target-use or cell-use variable not assigned to a predetermined
  disjoint block (even when its chosen cell is internal); and
* any owner/schedule bit shared with the exterior.

The exact collar relation is

\[
       {\mathfrak C}(V)=
       \pi_{\partial V}(\operatorname{Sol}\Phi_V).    \tag{2.8}
\]

The second target-use bullet is necessary for exact injectivity: an internal
target variable may be projected away only after its target and cell belong
to a fixed block partition, or after their occurrence identities have been
charged in (2.2).  For a bridge relation `C_e`,

\[
 {\mathfrak C}(UV)=
 \pi_{\partial(UV)}
  ({\mathfrak C}(U)\Join {\mathfrak C}_e
                         \Join {\mathfrak C}(V)).     \tag{2.9}
\]

Natural join followed by existential projection is associative.  If a
slot-preserving option changes row indices `I`, only envelope positions
`I+{0,1,2}` and replay rows `I+{-2,-1,0,1,2}` can change.  Hence its literal
row collar has bounded width.  The relation (2.8), however, can still have
many target-labelled valuations.  The fact that inclusion-minimal cap
conflicts have rank at most three does not bound this relation's adhesion.

### 2.6 Owner, facet, and slack current

Let `ell` be the row-token length, `a` the number of direct rank-`r+1`
owner-token occurrences, `f` the number of direct rank-`r` facet-token
occurrences, and `c_aux` the number of short cells spent without discharging
a distinct residual lower target.  The additive current is

\[
                    \kappa=(\ell,a,f,c_{aux}).        \tag{2.10}
\]

The palette/resource rows make the `f` accepted occurrences distinct.  A
partial product may still be rejected for a duplicate, so distinctness is
not inferred from the scalar `f`.

There are `2W+5` singleton/adjacent-pair cells and

\[
               L_r=\sum_{j=1}^r{k\choose j}          \tag{2.11}
\]

lower targets.  Therefore the exact scalar slack is

\[
              s_{low}=2W+5-L_r+f-c_{aux}.             \tag{2.12}
\]

On an accepted duplicate-free zipper,
`ell=a+f=W+1`, and hence

\[
              s_{low}=3W+6-L_r-a-c_{aux}.             \tag{2.13}
\]

Thus a slot-preserving migration which increases `a` by one spends exactly
one scalar unit.  Equations (2.12)--(2.13) are only capacity rows; they do
not imply lower Hall or common-cap feasibility.

## 3. Atomic factorization and the context-minimal quotient

Let `A_C` be a declared finite set of oriented interval atoms, replacement
atoms, and legal bridge atoms for component `C`.  A word in `A_C` is
resource-complete when every required old occurrence is used exactly once
or is cancelled by a declared replacement, every bridge socket is paired,
and no protected marked occurrence is deleted.

### Theorem 3.1 (exact atom factorization)

The map from an atom to (0.1), with multiplication defined by signed-resource
addition, port gluing, run-monoid multiplication, upper-transfer composition,
palette addition, cap natural join/projection, and current addition, is a
monoid homomorphism.  Every declared split/rethread variant has the product
signature of its factorization (1.3).  Conversely, every resource-complete
compatible atom product spells one literal declared variant with that
signature.

#### Proof

Resources, palette flux, and current are literal sums.  Ports enforce exactly
the declared adjacent atom endpoints.  The depth-two record is defined by
literal concatenation followed by a syntactic quotient.  Deterministic word
automata compose by function composition.  Formula conjunction along common
boundary variables is natural join, and hiding sealed variables is
projection.  Each operation is associative and agrees with literal
concatenation, proving the forward statement.  Reading a compatible product
from left to right supplies the fragment order, orientations, bridges, and
replacement occurrences, proving the converse. \(\square\)

It follows that an exact dynamic programme may merge two partial products
as soon as their signatures and used-resource sets agree.  Retaining one
literal witness for each reachable final signature gives a complete
component catalogue.  This is the smallest catalogue relative to the
declared interface in the following precise sense.

### Theorem 3.2 (formal-context separation)

Suppose two resource-compatible variants have different signatures in
(0.1).  Then some formal RSB continuation using only the exposed interface
accepts one and rejects the other.  Consequently no proof valid against all
such continuations may identify them.

#### Proof

A different port, literal row collar, or named resource is separated by a
continuation demanding that socket, collar, or resource.  A different
run-monoid state is separated by at
most a bounded zero/one collar closing the unequal arm or exposing the bad
flag.  Distinct deterministic upper transfers differ on an input state; a
prefix realizing that state and an accepting suffix separate them.  A
different palette flux is separated by the root multiplicity-one row.  Two
different cap relations have a boundary valuation in their symmetric
difference; pinning that valuation separates them.  A different additive
current is separated by the exact root total. \(\square\)

This is a Myhill--Nerode statement for the formal interface, not a claim that
every separating continuation occurs in a particular Pascal construction.
A smaller physical quotient is possible only after proving a restriction on
the allowed future contexts.

## 4. Exact assembly theorem

Contract the fixed marked packet to one distinguished object.  Choose one
variant per complement component and connect their occurrence-labelled
sockets by legal owner columns.  Let the resulting directed socket circuit
be cut at the distinguished packet, producing the literal complement path.

### Theorem 4.1 (component-variant RSB closure)

Within the declared atom and bridge atlas, the selected variants physicalize
the depth-two row while retaining the fixed marked packet if and only if all
of the following hold simultaneously.

1. **Resources and ports.**  The signed occurrence ledger gives the exact
   owner/macro/socket deck, and the directed socket columns form the required
   path or circuit.
2. **Residence/inversion.**  The root product of
   \({\mathfrak D}_2\) is accepting.
3. **Upper service.**  Starting from \(\bot\), every required upper-target
   transfer in `U` reaches `checkmark` (or has a still sealed protected
   witness).
4. **Lower palette.**  The root flux is zero and every lower colour has final
   multiplicity one.
5. **Common cap.**  The natural join of all local, bridge, prepin, and
   residual-target relations contains an accepting root valuation.
6. **Current.**  The row length, owner count, direct-facet count, cell use,
   and (2.12) agree with the prescribed global totals.

#### Proof

Necessity follows by restricting any literal physicalization to each atom
and bridge.  For sufficiency, Item 1 spells one literal row with the fixed
marked packet.  Item 2 is exactly maximal-envelope nonemptiness and `D2`
replay.  Item 3 is exact arbitrary-width interval-union coverage.  Item 4
gives the literal lower-q1 partition.  Item 5 supplies one physical cap and
one injective lower assignment rather than incompatible marginal solutions.
Item 6 supplies the exact length and scalar ledger.  These are precisely the
carrier, residence, upper-shadow, lower-palette, and compiler fields of the
depth-two RSB interface. \(\square\)

The theorem is an iff reduction, not an existence theorem.  In particular,
separate feasibility of the socket circuit, upper automata, lower palette,
and cap matching does not imply their joint feasibility.

## 5. What is bounded and what necessarily grows

The word "finite-state" has three different meanings here and they must not
be conflated.

| field | bounded structural datum for bounded support | growing datum unless an extra theorem is used |
|---|---|---|
| ports | two sockets and two row tokens per side | the `k`-bit socket labels |
| residence | constant run state per coordinate for fixed depth; five-row changed collar | the product over all `k` named coordinates |
| resources | `O(h)` occurrence identifiers for support `h` | the global owner/macro deck |
| lower palette | no live state for a palette-private (`lambda=0`) option | all rank-`r` colour identities for nonzero flux |
| upper shadows | one deterministic transfer per live target; bounded-depth cut debt is `O(cq)` | the unrestricted upper bank, or the polynomially growing prefix/suffix union bank |
| common cap | `O(h)` changed positions and rank-three local conflicts | the exact target-labelled boundary relation; rank three is not bounded adhesion |
| current | a constant number of additive integers | their range grows with `W` |

Two exact compressions are available.

* If a complete baseline fixed-window tower is modified at `c` physical
  seams, only `cq` old depth-`q` windows meet cuts.  Carrying the endangered
  occurrence-labelled witnesses is exact for that fixed depth.
* For arbitrary-width unions, every prefix or suffix union chain has at most
  `k-r+1` distinct values.  A `c`-fragment braid therefore has at most
  `O(c^2(k-r+1)^2)` cross-fragment union values in addition to its baseline
  holes.

Neither gives a dimension-independent target alphabet.  Likewise, the
common-cap relation becomes bounded-width only on a guarded face with
permanent bits and protected hosts, or after proving a bounded-adhesion
decomposition.  Ordinary Hall, marginal feasibility, and the rank-three
conflict bound do not provide such a decomposition.

Hence the smallest noncircular all-dimension regenerative hypothesis for
this lane is:

> Every required hazard core has a resource-disjoint local atom product
> whose palette flux is zero, whose protected upper-witness delta is confined
> to a declared bounded live bank, and whose common-cap collar lies in a
> Pascal-preserved guarded relation; the remaining additive currents admit
> one accepting socket circuit.

This hypothesis is closed under Theorem 4.1.  Its uniform supply is open.

## 6. Consequence for the frozen `K17` complement

The authenticated fixed complement contains `724` bad owner runs in `257`
components.  Lemma 1.1 explains why component order, reversal, and residual
owner pairing cannot help: those operations do not hit the hazard intervals.
It also gives the correct first catalogue layer—interval-transversal cores,
not endpoint sockets.

If the marked bank stays exactly at `4108` direct owner tokens, every one of
the `257` components must have a nonidentity option whose atom support hits
all of its hazards.  If whole length-three-only components may migrate into
an enlarged owner bank, the `82` length-two components still need genuine
variants.  The owner/slack current (2.13), applied to the `175` remaining
components, forces variants in at least `24` more, giving the exact relaxed
floor `106` already audited for OPTIMAL28.

The smallest proof-safe next catalogue is therefore stratified as follows.

1. Compute every inclusion-minimal interval-transversal core in a defective
   component (or fix one core and permit a stated auxiliary-cut radius).
2. Factor all supported rethreads into oriented interval and bridge atoms.
3. Reject products immediately by resources, palette flux, and `D_2`.
4. Quotient survivors by the exact signature (0.1).
5. Install upper transfers only for the currently endangered ranks/targets,
   retaining literal witnesses for every omitted target.
6. Send the surviving signatures, not literal permutations, to the directed
   socket and common-cap master.

This is a complete construction method for any frozen finite support class.
It does not show that the K17 atlas contains `106`, let alone `257`, jointly
compatible variants.  Direct radius-two occurrence changes remain one
possible source of replacement atoms, not part of this theorem.
