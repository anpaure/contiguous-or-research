# Lane L: labelled high-separator rigidity and the pull-clock ray gate

Date: 2026-08-01  
Status: exact labelled cross-rectangle theorem, exact fixed-neighbour
retiming theorem, minimal literal obstruction, and a private-ray
serialization lemma.  No all-dimensional private-ray supply or common-cap
compiler theorem is claimed.

## 0. Outcome

The transition-transparent row isolated in item2528L is false for the raw
core/high two-edge fusion catalogue.

* Two labelled age arcs form a cross rectangle exactly when all differences
  between their live source cells lie in both newborn letters.
* For the raw `g_(0,r-1)` / `g_(0,r-2)` pair this forces the complete ordered
  active flags to agree literally.  At a coatom occurrence both owners
  therefore share the same rank-`(r-1)` target `Q`.  The switch is a genuine
  topology connector inside the `Q`-fibre, but its q1 payload is zero; it
  cannot carry `e_(Q')-e_Q` for `Q'!=Q`.
* More generally, on any transition between distinct rank-`r` owners with a
  singleton terminal age cell, the coatom is forced to be the owner
  intersection.  A fixed directed owner edge has no retimable coatom mark.
* Changing owner edges does not create a clean lower unit either.  Every
  degree-preserving Johnson rethread obeys an exact lower/upper point-current
  cocycle.  Exact return of the immediate-upper deck forbids a primitive
  lower root.  The support-minimal escape is a two-edge octahedron carrying
  one lower unit and one opposite upper unit.
* A nontrivial same-neighbour retiming does exist on a different face: the
  middle newborn letter may exchange equal numbers of elements inside the
  next letter and inside each predecessor age cell.  For a singleton
  terminal cell, the useful choices form a clique on
  `S=Z_(d-1) intersect Y_0`.  Every nontrivial such fibre is necessarily an
  owner **stutter**: the middle and next owners are equal.  Its exterior
  flag interface is returned, but the middle occurrence is stateful; it is
  not a retiming on a nonloop Johnson edge.
* Every nontrivial stutter retiming changes exactly `d` nested proper-subset
  OR cells ending at the retimed letter.  The owner chronology and complete
  immediate-upper deck are unchanged literally; the only exported object
  is a lower/compiler ray.  If that entire ray is private to one fixed
  compiler matching, the retiming is a genuine primitive augmentation.
  A list of private arcs serializes with no upper debt and no loss of already
  matched targets when its full state collars are ordered-compatible; ray
  disjointness alone does not certify this.
* Two fully inverse sites with identical contexts cancel the physical q1
  cell as well as the shorter cells.  They give a useful zero-current basis
  swap, not a primitive occurrence transfer.  Any primitive twin statement
  must leave the longest cell open and record its q1 collateral explicitly.

On the canonical raw `K=1` high rotor the same-neighbour fibre is a singleton
for every `d>=2`.  Thus an all-depth positive theorem must use a multi-state
nonraw cascade and must plant private rays relative to one common matching.
The smallest raw cross-rectangle obstruction already occurs at
`(d,r)=(1,4)`.

## 1. Literal age recurrence and exact cross rectangles

A labelled age state is an ordered disjoint tuple

\[
 X=(X_0,\ldots,X_d).
\]

For a successor `Y`, write `B=Y_0` for its newborn/source letter.  The exact
owner-changing recurrence is

\[
                         Y_{i+1}=X_i\setminus B
                         \qquad(0\le i<d).             \tag{1.1}
\]

Mere containment is not enough.

Consider two literal arcs

\[
                  X\xrightarrow{B}Y,\qquad
                  X'\xrightarrow{B'}Y'.               \tag{1.2}
\]

### Theorem 1.1 (exact labelled cross-rectangle criterion)

Both crossed arcs

\[
                  X\xrightarrow{B'}Y',\qquad
                  X'\xrightarrow{B}Y                 \tag{1.3}
\]

are literal if and only if

\[
             X_i\mathbin\triangle X'_i\subseteq B\cap B'
                         \qquad(0\le i<d).             \tag{1.4}
\]

No equality of tail types is needed for (1.4), although the applications
below have equal types.

#### Proof

The first crossed arc is literal exactly when

\[
 Y'_{i+1}=X_i\setminus B'.                            \tag{1.5}
\]

The old second arc gives `Y'_(i+1)=X'_i setminus B'`, so (1.5) is equivalent
to

\[
                         X_i\triangle X'_i\subseteq B'.
\]

The other crossed arc gives the same condition with `B`.  Taking both is
exactly (1.4).  \(\square\)

The criterion is occurrence-labelled.  It is stronger than equality of age
types and stronger than the biregular fractional lift.

## 2. The raw `K=1` high class is a fixed-coatom connector

Let

\[
 F=(F_0,\ldots,F_{d-1})
\]

be an ordered active flag and put `Q=dotunion_(i<d)F_i`.  Let `D,D'` be
terminal blocks of the same size, disjoint from `Q`, and fix a permanent
label `p in F_0` for the high copy.

The core-free raw arc has tail and newborn letter

\[
 X=(F_0,\ldots,F_{d-1},D),\qquad B=D,                \tag{2.1}
\]

and the `K=1` raw arc has

\[
 X'=(F_0,\ldots,F_{d-1},D'),\qquad B'=D'\cup\{p\}.  \tag{2.2}
\]

The displayed `F_0` in (2.2) already contains `p`; deleting `p` from its
first survivor produces the canonical `g_(0,r-2)` head.

### Theorem 2.1 (raw core/high labelled rigidity)

For arbitrary equal-type raw core/high tails, the outgoing-head swap is
literal if and only if their ordered active flags agree cell by cell:

\[
                         X_i=X'_i\qquad(0\le i<d).     \tag{2.3}
\]

Consequently, after fixing `F`, every two terminal owner extensions
`Q dotunion D` and `Q dotunion D'` admit the raw cross rectangle.  At
terminal size one this is a complete topology connector bank among the
rank-`r` owners above `Q`, but every connector preserves the same coatom
`Q`.

#### Proof

For the core arc, `B=D=X_d`, which is disjoint from every `X_i`, `i<d`.
If (1.4) holds, then `X_i-X'_i` is contained in `D`, hence is empty.  Equal
tail block sizes force `X_i=X'_i`.  Conversely, if all active cells agree,
their symmetric differences vanish and Theorem 1.1 applies.  The union of
the active cells is `Q`, independent of the terminal owner extension.
\(\square\)

### Corollary 2.2 (no primitive q1 root in the raw fusion graph)

At a coatom occurrence `|D|=|D'|=1`, every raw core/high cross rectangle has
signed coatom payload zero.  Hence the returned-provider transfer digraph
induced by this catalogue has no edge `Q->Q'` with `Q!=Q'`; it decomposes by
`Q`, and in fact by the full ordered flag `F`.

Thus the strong-connectivity hypothesis of item2528L's returned unit-root
theorem fails maximally on the raw catalogue.  A hole in one `Q`-fibre
cannot be filled from surplus in another by these switches.

### Smallest canonical obstruction

Take `d=1,r=4` and

\[
 X=(123\mid4),\qquad Y=(4\mid123),                  \tag{2.4}
\]

\[
 X'=(124\mid3),\qquad p=1,\qquad Y'=(13\mid24).     \tag{2.5}
\]

Both old arcs obey (1.1), and both tails have type `(3,1)`.  But

\[
 123\triangle124=\{3,4\}\not\subseteq4\cap13,
\]

so neither crossed arc is literal.  Their coatoms are `123` and `124`.
This is the first canonical parameter range because `r-2>d` requires
`r>=d+3`.

For comparison, replacing `X'` by `(123|5)` gives a positive rectangle:
the owners `1234` and `1235` share the complete active flag and coatom
`123`.

## 3. A fixed owner edge fixes its coatom

The preceding rigidity is not peculiar to raw rotors.

### Theorem 3.1 (owner-edge coatom law)

Let `X->Y` be a literal transition between distinct rank-`r` owners `T,T'`,
and assume `X_d={alpha}`.  Then

\[
                T'=T-\{\alpha\}+\{\beta\},\qquad
                Q_X:=T-\{\alpha\}=T\cap T'.          \tag{3.1}
\]

In particular, the directed owner edge `(T,T')` uniquely fixes the q1
coatom.  No post-hoc mark retiming can change it while keeping that edge.

#### Proof

Every element of `Q_X=dotunion_(i<d)X_i` is either refreshed into `Y_0` or
survives into `Y_(i+1)` by (1.1).  Hence `Q_X subseteq T'`.  Since `T,T'`
are distinct `r`-sets, their intersection has size at most `r-1`, while it
contains the `r-1` elements of `Q_X`.  Equality follows, and the displayed
Johnson exchange is forced.  \(\square\)

Thus on any connected owner-simple chronology with more than one owner,
the complete q1 edge-colour sequence is determined by the owner sequence.
The static owner--coatom matching of item2528L cannot simply be attached to
a frozen chronology.

There is also a sharp static exchange floor.  The containment graph between
rank-`r` owners and rank-`(r-1)` coatoms has no `C4`: two distinct owners
share at most one coatom.  Its smallest alternating cycle is the `C6`

\[
 S+a\;--\;S+a+b\;--\;S+b\;--\;S+b+c\;--\;
 S+c\;--\;S+c+a\;--\;S+a,                            \tag{3.2}
\]

where `|S|=r-2` and `a,b,c` are distinct.  Hence a nontrivial closed
owner--coatom matching exchange needs at least three owner rows.  This is
only the static incidence floor; literal chronology, upper colours and cap
guards can require more.

### Theorem 3.2 (unavoidable paired upper current)

For a rank-`s` named palette define

\[
 \partial_s e_A=\chi_A\in\mathbb Z^{[k]}.             \tag{3.3}
\]

Let `F,F'` be directed Johnson-edge multisets satisfying, separately at
every rank-`r` owner `T`,

\[
 d_F^+(T)=d_{F'}^+(T),\qquad d_F^-(T)=d_{F'}^-(T).   \tag{3.4}
\]

Let `Delta L` and `Delta U` be the signed changes in their rank-`r-1`
intersection and rank-`r+1` union occurrence vectors.  Then

\[
              \boxed{\partial_{r-1}\Delta L+
                     \partial_{r+1}\Delta U=0.}       \tag{3.5}
\]

Consequently exact return of the immediate-upper occurrence vector forbids

\[
                         \Delta L=e_V-e_Q             \tag{3.6}
\]

for distinct coatoms `Q,V`.

#### Proof

Every Johnson edge `A->B` satisfies the coordinate identity

\[
             \chi_A+\chi_B=\chi_{A\cap B}+\chi_{A\cup B}.       \tag{3.7}
\]

Sum over `F` and `F'`.  Their owner-side sums agree by the degree
hypothesis, proving (3.5).  If `Delta U=0`, then
`partial_(r-1) Delta L=0`, whereas the image of (3.6) is
`chi_V-chi_Q!=0`.  \(\square\)

Without the degree-return hypothesis the right side is the owner boundary
`partial_r(Delta d^+ + Delta d^-)`; open endpoints must therefore be carried
as part of the state.  Thus a returned separator supported entirely on such
nonloop Johnson edges, whose upper state is also returned, cannot carry a
clean primitive intersection-colour root.  Strong connectivity within that
face after forgetting the upper-current coordinate is unsound.  The stutter
ray of Sections 4--6 is outside this face: its q1 cell is a proper source
interval, not the intersection colour of a nonloop owner edge.

Coverage alone forces `Delta U=0` only on an exact old upper deck with the
same number of inserted and deleted edges and preservation of every upper
target, or locally when every deleted upper occurrence is a protected unique
witness.  Mere upper completeness in the presence of multiplicity slack is
not enough.

### Proposition 3.3 (support-minimal octahedral pair)

The obstruction is sharp.  Let `W` be an `(r-1)`-set, take `x in W`, and
take distinct `a,b,t` outside `W`.  Put

\[
\begin{aligned}
 A&=(W-\{x\})+\{a,b\},& B&=W+\{t\},\\
 C&=W+\{a\},& D&=W+\{b\}.
\end{aligned}                                                   \tag{3.8}
\]

Replacing `A->C,B->D` by `A->D,B->C` gives

\[
\begin{aligned}
 \Delta L&=e_{(W-x)+b}-e_{(W-x)+a},\\
 \Delta U&=e_{W+t+a}-e_{W+t+b}.
\end{aligned}                                                   \tag{3.9}
\]

The point currents in (3.9) are opposite.  One edge cannot preserve owner
degrees, so support two is minimal.  Conversely, after possibly transposing
the source and head shores (time reversal) and swapping the two diagonals,
every nondegenerate two-edge Johnson rectangle whose lower payload reduces
to one primitive root has this star/top-neighbour form and carries the
opposite upper root.  This is an owner-edge/palette statement only: the
rectangle still needs a literal age decoration, residence and compiler
guards.

## 4. Exact fixed-neighbour pull-clock fibre

The raw cross catalogue is rigid, but there is one exact local mechanism
which can change a coatom without changing either neighbouring state.

Fix literal transitions

\[
                  Z\xrightarrow{B}X\xrightarrow{C}Y,
                  \qquad B=X_0,\ C=Y_0.              \tag{4.1}
\]

### Theorem 4.1 (same-neighbour, same-type retiming)

An alternative middle state `tilde X` with the same type and the same two
neighbours exists exactly when its newborn block `tilde B=tilde X_0`
satisfies

\[
\begin{aligned}
 |\widetilde B|&=|B|,\\
 |\widetilde B\cap Z_i|&=|B\cap Z_i| &&(0\le i<d),\\
 \widetilde B\triangle B&\subseteq C.               \tag{4.2}
\end{aligned}
\]

The other cells are then forced by

\[
                  \widetilde X_{i+1}=Z_i\setminus\widetilde B.
                                                               \tag{4.3}
\]

The owner of the middle state is also unchanged if and only if

\[
          \widetilde B\triangle B
             \subseteq Z_0\dot\cup\cdots\dot\cup Z_{d-1}.     \tag{4.4}
\]

#### Proof

The incoming recurrence forces (4.3).  Equality of the middle types is
equivalent to the first two rows of (4.2).  The outgoing row at age one is
`B setminus C=tilde B setminus C`, which is equivalent to the last row of
(4.2).  For later ages, (4.3) and the same containment give

\[
 (Z_i\setminus B)\setminus C
   =(Z_i\setminus\widetilde B)\setminus C.
\]

This proves necessity and sufficiency.  A changed label outside the first
`d` predecessor cells belongs to the middle owner exactly when it belongs
to the newborn block; a changed label inside those cells remains in the
owner either as newborn or survivor.  This proves (4.4).  \(\square\)

Put

\[
                         S=Z_{d-1}\cap C.             \tag{4.5}
\]

On the owner-preserving subfibre which changes no earlier age cell, (4.2)
reduces to choosing a fixed-size subset `K=B intersect S`.  If `X_d` is a
singleton and the fibre is nontrivial, then the terminal element lies in
`S`, and the possible states are indexed by

\[
                         z\in S,\qquad Q_z=T-\{z\}.    \tag{4.6}
\]

Thus one repeated last-age/next-letter block exposes a clique of primitive
coatom transfers while fixing both neighbours, the owner, and the age type.
There is one further forced fact.  Since `z in S subseteq C`, the next
newborn block refreshes the terminal element, while every other owner
element is refreshed or survives.  Therefore

\[
                              T(Y)=T(X).              \tag{4.7}
\]

Every nontrivial fibre (4.6) is thus an equality/stutter separator.  It is
the exact positive local pull-clock mechanism missing from the raw cross
rectangles, but it cannot be inserted as a nonloop edge in an owner-simple
chronology without an auxiliary sidecar, puncture, or multi-state cascade.

### Corollary 4.2 (canonical `K=1` raw local rigidity)

Write the mobile blocks of a raw high rotor as `A_0,...,A_d` and its
permanent label as `p`.  For `d>=2`, three consecutive states are

\[
\begin{aligned}
 Z&=(p+A_1,A_2,\ldots,A_d,A_0),\\
 X&=(p+A_0,A_1,\ldots,A_d),\\
 Y&=(p+A_d,A_0,\ldots,A_{d-1}).                     \tag{4.8}
\end{aligned}
\]

The only possible change in (4.2) would replace `p` by an element of
`A_d`.  The `Z_0=p+A_1` intersection count forbids removing `p`, while the
`Z_(d-1)=A_d` count forbids inserting an element of `A_d`.  Hence
`tilde X=X`: there is no nontrivial one-state transition-transparent
retiming for any `d>=2`.

At `d=1` there is one exceptional fibre:

\[
 (p+A_0\mid A_1)\longmapsto
 (q+A_0\mid p+(A_1-\{q\}))\qquad(q\in A_1),          \tag{4.9}
\]

with predecessor and successor both `(p+A_1|A_0)`.  If `A_1={q}`, this
transfers the coatom from `T-{q}` to `T-{p}`.  Section 5 shows why even this
exception is not lower/compiler transparent by itself, although its
complete upper deck is fixed.

## 5. The exact exported lower/compiler ray

Use word positions so that `Z` is the state at time `t-1`, `B` is emitted
at `t`, and `C` at `t+1`.  Suppose the singleton terminal is retimed from
`z` to `z'` through the fibre (4.6).  Then `z,z' in Z_(d-1) intersect C`.
Both last occurred at time `t-d`, neither occurs at
`t-d+1,...,t-1`, the old `B` contains `z'` but not `z`, and the new `B`
contains `z` but not `z'`.

### Theorem 5.1 (prefix-ray law)

The only contiguous-OR occurrences changed by the retiming are the `d`
intervals

\[
                         [t-\ell+1,t]\qquad(1\le\ell\le d).     \tag{5.1}
\]

For each `ell` there is a context mask `H_ell`, containing neither `z` nor
`z'`, such that the old and new values are

\[
             H_\ell\cup\{z'\}\qquad\longrightarrow\qquad
             H_\ell\cup\{z\}.                       \tag{5.2}
\]

Every interval containing `t+1` is unchanged because `C` contains both
labels.  Every interval reaching time `t-d` is unchanged because the common
old occurrence contains both labels.

#### Proof

Intervals avoiding `t` do not see the changed letter.  An interval which
contains `t+1` also contains `C`, hence both exchanged labels.  An interval
ending at `t` contains the common previous occurrence at `t-d` exactly when
its length is at least `d+1`.  The remaining lengths are precisely (5.1),
and the age definition excludes both labels from their earlier context.
This gives (5.2).  \(\square\)

The negative and positive supports in (5.2) are disjoint.  The longest
changed values are the two coatoms `Q_z=T-{z}` and `Q_(z')=T-{z'}`; every
shorter value is a proper subset of the same fixed owner `T`.  Thus the
signed payload has negative and positive mass exactly `d`, entirely in the
lower/source deck.  The owner sequence and every immediate-upper or wider
owner-union witness are unchanged literally.  If `t-d` and `t+1` lie inside
the replaced source, its complete prefix- and suffix-union boundary
signatures are unchanged as well.

The `d` physical interval cells are exactly the compiler cells whose target
values change.  A fixed compiler matching survives automatically only if it
avoids all of them or is explicitly rerouted.  A scalar count of unused
cells is not enough.

## 6. The concrete bounded-state interface: private-ray serialization

The ray law gives a genuine primitive augmenter, but its hypothesis is
occurrence-labelled rather than scalar.

### Definition 6.1 (private retiming site)

Fix one lower target--cell matching `M`.  A retiming site
`Q_z->Q_(z')` from Theorem 4.1 is private at a given step when:

1. its `d-1` shorter ray cells are unused by `M`;
2. its length-`d` cell is unused at that step;
3. every other protected assignment of `M` lies outside the complete ray;
4. `Q_z` has a retained matched provider outside that length-`d` cell; and
5. the source-position envelope and every external pin have the same state
   before and after the retiming.

The conditions refer to one literal occurrence and the current matching.  A
scalar count of unused cells elsewhere does not imply them.

### Theorem 6.2 (one-site private-ray augmentation)

If `Q_(z')` is unmatched and `Q_z->Q_(z')` is private, retime the stutter
site and assign its new length-`d` cell to `Q_(z')`.  The matching rank rises
by one.  Both exterior age states, the owner stutter, the complete owner
chronology, every immediate-upper and wider owner-union occurrence, every
old edge of `M`, and all declared position/pin guards are preserved.

#### Proof

Theorem 4.1 returns both exterior states, the type and the owner.  Theorem
5.1 confines all changed cells to the declared lower ray and proves literal
upper return.  Privacy leaves every old edge of `M` intact, including a
retained provider of `Q_z`.  The new longest cell has value `Q_(z')` and is
unused, so adjoining that incidence augments `M`.  \(\square\)

### Theorem 6.3 (time-expanded private-ray serialization)

Let `Q_0,Q_1,...,Q_h` be distinct target states and let `P_i`,
`0<=i<h`, be retiming sites whose old and new length-`d` values are
`Q_i,Q_(i+1)`.  Assume:

* every shorter ray cell of every `P_i` is unused by `M`;
* the complete physical ray-cell sets are pairwise disjoint;
* all other edges of `M` avoid the union of the rays;
* `M` matches `Q_0` outside the rays, matches `Q_i` to the longest cell of
  `P_i` for `1<=i<h`, and misses `Q_h`;
* the longest cell of `P_0` is unused; and
* the ordered list is **serially compatible**: after toggling every proper
  prefix `P_0,...,P_(i-1)`, site `P_i` remains the same literal
  fixed-neighbour fibre with the same ray and every exterior/pin guard
  required in Definition 6.1.

Pairwise disjoint full state-support collars are a simple sufficient
condition for the last row.  Ray-cell disjointness alone is not: adjacent
age sites also need the crossed literal transition of Theorem 1.1.

Toggle `P_0,P_1,...,P_(h-1)` in order.  After toggling `P_i`, move the
matching edge for `Q_(i+1)` from the longest cell of `P_(i+1)` to the newly
changed cell of `P_i` (when `i+1<h`), thereby freeing the next site.  At the
last site, assign its new cell to `Q_h`.  The final matching has rank
`|M|+1`; all old targets remain matched, and no upper or compiler debt is
left.

#### Proof

Inductively, immediately before step `i` the longest cell of `P_i` is free,
while `Q_i` is matched outside that cell.  Serial compatibility makes the
retiming literal, and its shorter changed cells carry no matching edge.  Its
new longest cell has value `Q_(i+1)`.  If `i+1<h`, transfer the existing
`Q_(i+1)` edge from `P_(i+1)` to this new cell.  This is a rank-preserving
matching relocation and frees the next site; it does not use Theorem 6.2's
unmatched-target hypothesis.  At the last step `Q_h` is unmatched, so
Theorem 6.2 augments the matching.  Theorem 5.1 and the serial guard give
literal upper return throughout.  \(\square\)

The exterior separator state is returned at each step, but the marked
middle occurrence is stateful and consumed.  Hence this is a capacity-one,
occurrence-token path, not an infinitely reusable catalyst.  Strong
connectivity of an occurrence-labelled, time-expanded private-ray network
is sufficient to route a primitive when the required path of distinct sites
is present.  Strong connectivity after projection to target names is not
sufficient.

### Proposition 6.4 (full inverse twins are zero-current)

If a second site performs the inverse retiming with the identical ordered
contexts `(H_1,...,H_d)`, then the two physical changes cancel at every
length, including the length-`d` coatom row:

\[
                  \Delta_{\rm lower}=0,\qquad
                  \Delta_{q1}=0.                    \tag{6.1}
\]

Literal `K_(2,2)` compiler rectangles at every length can return a declared
cap matching, but the packet is a zero-current basis exchange, not a
primitive occurrence transfer.  To leave a primitive root open, a twin must
leave the longest row open as well and carry the second q1 root as explicit
collateral.

### Proposition 6.5 (a fully returned stutter has zero payload)

At one fixed retiming site write `V_\ell(z)` for the value of its
length-`ell` cell in fibre state `z`.  For any sequence
`z_0,z_1,...,z_h` of legal retimings, the complete signed physical payload
telescopes to

\[
       \sum_{\ell=1}^d
          \bigl(e_{V_\ell(z_h)}-e_{V_\ell(z_0)}\bigr).           \tag{6.2}
\]

In particular, returning the marked middle state, `z_h=z_0`, returns zero
payload at every depth.  Therefore one stutter occurrence cannot be an
infinitely reusable nonzero unit-root catalyst: either its state remains
changed, a second occurrence token is consumed, or an external collateral
root is exported.  This is an occurrence-vector statement; a compiler basis
can still undergo a zero-current exchange unless its return is imposed
separately.  The smallest labelled obstruction is already a two-state fibre
at `d=1`.

#### Proof

At every depth, consecutive changes at the same physical cell cancel
pairwise, leaving only its final value minus its initial value.  Summing over
the `d` ray cells gives (6.2).  \(\square\)

The raw `K=1` high rotor has no nontrivial private site for `d>=2`.  Hence
Theorems 6.2--6.3 close the local transition/compiler semantics but not the
dimension-uniform supply theorem.  A regenerative proof must construct
enough returned stutter fibres in a nonraw cascade and make their rays
private to one common matching.

## 7. Relation to the larger coatom packets

The mixed-screen coatom tensor is a useful calibration.  It already gives a
larger reversible path replacement with equal owner sets, immediate
palettes, prefix/suffix OR signatures, complete internal OR support and
residence.  Thus upper-transparent nonraw cascades exist.  However its exact
native compiler-return graph is empty and has deficiency `2(d-1)`; exterior
return cells remain necessary.  Therefore upper transparency does not by
itself return the compiler state.

The present theorem identifies the smaller obstruction underneath that
phenomenon.  The raw high/core topology connector is trapped in one ordered
`Q`-flag.  Escaping to a primitive q1 root requires a repeated-letter
pull-clock fibre, which exports the literal `d`-cell lower/compiler ray.  The
exact live construction target is now:

> plant an occurrence-labelled path bank of returned stutter interfaces
> whose shorter rays are private and whose longest cells form the
> serially compatible alternating matching chain of Theorem 6.3, or build a
> multi-state packet with the same time-expanded capacity and returned cap
> state.

Neither the fractional high-separator distribution nor the static coatom
matching proves that stateful bank.  No additive-constant conclusion is
claimed.
