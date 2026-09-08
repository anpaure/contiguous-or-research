# One-copy (3+1) C8 fusion: the two-component parity actuator and its exact upper interface

Date: 2026-08-02  
Status: exact conditional splice theorem, sharp C6 obstruction, and exact
upper-casualty/absorber row.  This note does **not** prove that the required
octagon occurs in every Boolean owner--flag factor, nor that a bounded family
of such octagons can be selected globally.

## 0. Outcome

Start after the one-copy owner--flag problem has been solved up to
connectivity: one literal candidate is selected for every role and owner,
the complete named suffix-target multiset is exact, and the selected literal
turns form a directed cycle cover.

Changing only the successor permutation is the cleanest possible fusion
layer.  The selected candidates, owners, flags, and named suffix payloads do
not move.  The following facts are exact.

1. An alternating `C6` whose three removed turns lie in three different
   components merges those components into one.  If its turns lie in exactly
   two components, it leaves exactly two components.  In particular, a
   single `C6` can never perform a two-to-one fusion.
2. Let an alternating `C8` remove three turns from a component `A`, in their
   cyclic order, and one turn from a component `B`.  With the aligned cyclic
   reconnection, it replaces `A,B` by one component.  With the opposite
   order of the three cuts on `A`, the same reconnection produces three
   components.  Thus the order condition is necessary and sufficient.
3. If the four new turns are literal age-compatible and the four old turns
   avoid every protected successor macroedge, the switch preserves one-copy
   ownership, every named suffix-target multiplicity, literal state balance,
   pins, and residence.  No payload-transparency assumption is needed,
   because no selected candidate is replaced.
4. For strict-upper targets, let `D` be the four deleted seams.  Put

   \[
   Z_F(D)=\{U:\hbox{ every old interval witness of }U
                    \hbox{ crosses }D\}.
   \]

   Let `N_{F'}(D')` be the values supplied by intervals crossing a new seam.
   Among targets covered before the switch, the missing set afterwards is
   exactly

   \[
                         Z_F(D)\setminus N_{F'}(D').       \tag{0.1}
   \]

   This is the sharp absorber row.  With upper rank capped at `r+Q`, the old
   `3+1` interface contains at most

   \[
                              10(Q+1)^2                   \tag{0.2}
   \]

   distinct crossing-union values, while the new four-strand interface
   contains at most `16(Q+1)^2`.  Hence (0.2) bounds the coverage defect of
   one switch.  It is **not** an all-width `O(1)` claim when `Q` grows.
5. A common-exterior Boolean star `C8` preserves the complete immediate-upper
   multiplicity vector automatically.  Combined with the `3+1` order
   condition, it is an exact two-component, owner/suffix/immediate-upper
   neutral fusion atom, subject only to literal turn, protection, and deeper
   upper-interface checks.

Consequently, if clean `C6`s are available hereditarily, an odd number of
components can be fused using hexagons alone.  An even number reduces to two,
and one aligned `3+1` `C8` is the smallest parity-changing finish in a
`C4`-free incidence host.

## 1. Fixed literal section and successor switches

Let `X` be a selected exact owner--flag section.  Every occurrence `v in X`
carries:

* one role and one owner `T(v)`;
* one literal age flag

  \[
                  C(v)=(C_0(v),\ldots,C_d(v));
  \]

* its complete named suffix-target payload; and
* any occurrence-labelled pin or guard data.

Assume all role, owner, and named suffix rows are already exact.  A legal
successor permutation `tau` of `X` satisfies, at every turn `v -> w`,

\[
 C_{i+1}(w)=C_i(v)\setminus C_0(w)
                         \qquad(0\le i<d).             \tag{1.1}
\]

This is the literal age-state recurrence, not merely its type inequality.
The cycles of `tau` are the literal Euler components.

Choose distinct tails `x_0,...,x_(q-1)` and put

\[
                         y_i=\tau(x_i).
\]

Assume that all `y_i` are retained as distinct head occurrences and that the
new turns below are legal.  The forward alternating `C_(2q)` switch is

\[
 \tau'(x_i)=y_{i+1}\quad(i\bmod q),\qquad
 \tau'(v)=\tau(v)\quad(v\notin\{x_i\}).               \tag{1.2}
\]

In the bipartite tail--head graph, (1.2) toggles one alternating cycle.  It
is performed atomically; a decomposition into smaller signed circuits need
not have legal intermediate states.

### Lemma 1.1 (fixed-section invariance)

If every new turn in (1.2) is literal and none of the deleted turns is a
protected successor macroedge, then `tau'` is another legal one-copy
owner--flag cycle cover.  It preserves, coefficientwise,

1. every role and owner row;
2. every named suffix-target row at every marked rank;
3. every age-type multiplicity and marked first moment;
4. every candidate-local guard or payload row; and
5. every protected turn outside the switch.

#### Proof

The switch changes only the bijection from selected tail occurrences to the
same selected head occurrences.  Thus every occurrence remains selected
once and all of its local resource columns are unchanged.  Equation (1.2)
is a permutation, so every occurrence still has indegree and outdegree one.
The assumed legality of the new turns gives (1.1), and pin avoidance leaves
all protected macroedges intact.  \(\square\)

This is stronger than a payload-neutral replacement theorem: there is no
payload comparison because the payload-bearing vertices themselves do not
move.

The fixed-section hypothesis is essential.  In the coloured-Euler arc
selector of the TPC note, a tail/head switch may replace the
payload-bearing trace arcs themselves; Lemma 1.1 then applies only after a
literal payload-transparent lift has been exhibited.  Here the intended
face is the OFHT cycle-hypergraph model, where resources are carried by the
selected candidates and the successor variables are a separate layer.

## 2. Exact cut-permutation topology

Delete the old turns `x_i -> y_i`.  Starting at `y_i` and following retained
old turns, one reaches a unique next cut tail `x_(s(i))`.  The resulting
permutation `s` of the cut indices records both the old touched components
and the cyclic order of their cuts: its cycles are exactly those old
components.

Let

\[
                         h=(0\ 1\ \cdots\ q-1).        \tag{2.1}
\]

After (1.2), a traversal from `x_i` first goes to `y_(h(i))` and then along
the retained old strand to `x_(s(h(i)))`.

### Theorem 2.1 (cut-permutation formula)

The number of new components meeting the switched turns is

\[
                              c(sh),                    \tag{2.2}
\]

where `c(pi)` denotes the number of cycles of a permutation `pi`.  In
particular,

\[
              c(sh)-c(s)\equiv q-1\pmod2.              \tag{2.3}
\]

#### Proof

The preceding traversal shows that `sh` is exactly the first-return
permutation on the cut tails in the new factor, proving (2.2).  Since
`sgn(pi)=(-1)^(q-c(pi))` and `sgn(h)=(-1)^(q-1)`, comparison of `s` and
`sh` gives (2.3).  \(\square\)

### Corollary 2.2 (sharp C6 obstruction)

For `q=3`, if the removed turns lie in two old components, then the switch
leaves exactly two components.

#### Proof

After relabelling, `s=(0 1)(2)` and `h=(0 1 2)`.  Hence `sh` has one fixed
point and one transposition.  Equivalently, (2.3) forbids the odd change
`2 -> 1`.  \(\square\)

If the three removed turns lie in three components, `s` is the identity and
`sh=h`; the `C6` merges all three into one.

### Lemma 2.3 (why the Boolean host has no smaller switch)

The rank-`(r-1)`/rank-`r` Boolean incidence graph has no simple `C4`.
Consequently its smallest possible alternating two-component parity actuator
has length eight.

#### Proof

Two distinct rank-`(r-1)` sets have at most one common rank-`r` superset:
if they are Johnson adjacent, that superset is their union, and otherwise
there is none.  A `C4` would give them two common upper neighbours.  Thus
the first circuit length is six; Corollary 2.2 shows that length six cannot
fuse two components, while the `C8` below can.  \(\square\)

### Theorem 2.4 (the aligned `3+1` C8 fusion)

Let `q=4`.  Suppose the old turns with indices `0,1,2` lie on one component
`A` in that cyclic order, and the turn with index `3` lies on a different
component `B`.  Then (1.2) replaces `A,B` by one component.

If the cyclic order on `A` is instead `0,2,1`, the switched support has
three components meeting these turns.

#### Proof

In the aligned case

\[
 s=(0\ 1\ 2)(3),\qquad h=(0\ 1\ 2\ 3),
\]

and

\[
                         sh=(0\ 2\ 3\ 1),
\]

which is one cycle.  In the opposite case

\[
 s=(0\ 2\ 1)(3),\qquad sh=(0)(1)(2\ 3),
\]

which has three cycles.  These are the only two cyclic orders of three
labelled cuts, so the order condition is exact.  \(\square\)

Thus a `C8` need not touch four different components.  Its `3+1` incidence
pattern is precisely the smallest alternating circuit which can fuse two
components when the host has no usable `C4`.

## 3. Literal residence is automatic after a literal switch

Put

\[
                         T_t=\bigcup_{i=0}^d C_i(t)
\]

along a legal cyclic component.  For a coordinate `a`, its membership word
`1[a in T_t]` is the owner-residence word.

### Lemma 3.1 (age recurrence implies residence)

Under (1.1), every maximal positive run which is not the whole cyclic
component has length at least `d+1`.  If the residence convention also
tests an all-one cyclic run, it suffices additionally that the component
length be at least `d+1`.

#### Proof

At the first position of a positive run, `a` must lie in the fresh class
`C_0`.  At every subsequent turn, (1.1) either advances its current age by
one or refreshes it into the new `C_0`.  It cannot leave the owner until
`d+1` positions after its most recent refresh.  Hence a finite maximal run
has length at least `d+1`.  The only excluded case has no first position,
namely an all-one cyclic run.  \(\square\)

### Corollary 3.2 (literal two-component fusion)

Under the hypotheses of Lemma 1.1 and the aligned order of Theorem 2.4, the
`C8` produces one literal Euler component on `A union B`, preserves every
owner and named suffix target exactly, and preserves depth-`d` residence.

No separate endpoint-run test is needed here.  Such a test is necessary for
an incidence-only switch whose new turns have not been lifted to literal age
flags; literal compatibility (1.1) already contains it.

### Proposition 3.3 (the inherited age-slack obstruction)

Let `m_c` be the fixed integer age-type multiplicities, let

\[
 D_i=M_i-M_{i+1},\qquad S=\sum_{i=0}^{d-1}D_i,
\]

and let `kappa` be the number of nonempty rotation-orbit blocks met by the
selected occurrences.  Every successor-only switch leaves `m_c`, every
`D_i`, and `S` unchanged.  Consequently a terminal chronology with `C`
components is possible only if

\[
                              \kappa-C\le S,                    \tag{3.1}
\]

or equivalently `C>=kappa-S`.  In particular, one component requires

\[
                              \kappa-1\le S.                    \tag{3.2}
\]

In particular, on the zero-slack rotation face, a literal `3+1` `C8` cannot
fuse components belonging to different rotation-orbit blocks.

#### Proof

The switch does not change the occurrence multiset, so all displayed
quantities are fixed.  A zero-slack transition stays within one rotation
orbit, while the number of positive-slack transition copies is at most `S`.
Connecting `kappa` contracted orbit blocks into `C` weak components requires
at least `kappa-C` such copies.  This is the integral component-budget row
of the first-moment identity.  \(\square\)

Thus the octagon is a topology actuator only after the age template has
enough off-rotation slack.  Literal availability of its four new turns
automatically respects the fixed slack ledger, but does not certify the
global inequalities (3.1)--(3.2); fractional stationarity alone proves
neither.

## 4. Exact strict-upper casualty and absorber row

The owner and suffix rows are vertex-local, but strict-upper targets are
unions of intervals in the owner order and can change at the four seams.
This section gives the exact interface without claiming automatic
transparency.

Let `U_Q` be the required targets of ranks `r+1,...,r+Q`.  For `U in U_Q`,
let `W_F(U)` be the set of all occurrence-labelled cyclic owner intervals
of the old factor whose union is `U`.  Let `D` be the four deleted turns and
define

\[
 Z_F(D)=\{U\in U_Q: W\cap D\ne\varnothing
                         \hbox{ for every }W\in W_F(U)\}.       \tag{4.1}
\]

Let `D'` be the four new turns and define the new cross-seam deck

\[
 N_{F'}(D')=\{U\in U_Q:\hbox{ some }F'\hbox{-interval of union }U
                                   \hbox{ meets }D'\}.          \tag{4.2}
\]

For a target `U`, write \(m_F^{\times}(U;D)\) for the number of its old
occurrence-labelled interval witnesses which meet `D`, and define
\(m_{F'}^{\times}(U;D')\) similarly.  The complete signed multiplicity
interface is

\[
 m_{F'}(U)-m_F(U)
      =m_{F'}^{\times}(U;D')-m_F^{\times}(U;D).                \tag{4.2a}
\]

Indeed, intervals avoiding the old cuts and intervals avoiding the new
seams are the same internal strand intervals, occurrence for occurrence.
Thus exact upper multiplicity is equivalent to equality of the two
cross-seam multisets.  Formula (4.2a) is exact but has no length-independent
`l_1` bound when strands have long prefix/suffix plateaux.

### Theorem 4.1 (exact upper-interface identity)

Assume every target in `U_Q` is covered in `F`.  After any legal successor
switch on `D`, the targets missing from `F'` are exactly

\[
                            Z_F(D)\setminus N_{F'}(D').         \tag{4.3}
\]

#### Proof

Every old witness avoiding `D` lies wholly in one retained strand and is
still a contiguous interval with the same owner word in `F'`.  Hence only a
target in `Z_F(D)` can disappear.  Conversely, an interval of `F'` which
does not meet `D'` lies wholly in one retained strand and was already an old
witness avoiding `D`.  Therefore a target in `Z_F(D)` is restored precisely
when it occurs in the new cross-seam deck (4.2).  \(\square\)

Equation (4.3) is both the sharp defect formula and the sharp absorber
condition.  A separately certified owner/suffix/pin-neutral absorber repairs
the upper-coverage row exactly when it covers
`Z_F(D)\setminus N_(F')(D')`.  Zero-defect switching is the special case
`Z_F(D) subseteq N_(F')(D')`; protecting one cut-avoiding witness per target
is the stronger sufficient condition `Z_F(D)=emptyset`.  The identity does
not by itself construct such an absorber or authorize extra owner copies.

### Lemma 4.2 (compressed four-strand bound)

For a nonempty owner-word strand `W`, its distinct prefix unions and suffix
unions of rank at most `r+Q` each number at most `Q+1`.

If a cyclic word is cut into `m` strands, the set of distinct rank-at-most
`r+Q` union values of intervals crossing at least one cut has size at most

\[
                              m^2(Q+1)^2.                       \tag{4.4}
\]

#### Proof

The prefix unions form a nested chain starting at rank `r`; every strict
change raises rank by at least one.  This proves the `Q+1` bound, and the
suffix case is identical.

A crossing interval is determined by its ordered first and last strands,
one suffix value of the first, one prefix value of the last, and the fixed
total unions of the intervening whole strands.  There are `m^2` ordered
strand pairs and at most `(Q+1)^2` choices for each.  Invalid or duplicate
choices only lower the count.  \(\square\)

### Corollary 4.3 (one `3+1` C8 defect bound)

The three cuts on `A` produce three old strands and the cut on `B` produces
one.  Therefore

\[
 |Z_F(D)|\le (3^2+1^2)(Q+1)^2=10(Q+1)^2,             \tag{4.5}
\]

and the new four-strand cross-seam deck has size at most

\[
                         4^2(Q+1)^2=16(Q+1)^2.         \tag{4.6}
\]

In particular the terminal upper-coverage defect of one switch is at most
the right side of (4.5).

These bounds count distinct coverage values.  They do not bound the full
signed multiplicity change of all interval occurrences: long prefix/suffix
plateaux can have large occurrence multiplicity.  Immediate-upper
multiplicity has the exact neutral Boolean face below.

## 5. Common-exterior Boolean star C8

Let `S` have rank `r-2`, and choose distinct petals
`a_0,a_1,a_2,a_3` outside `S` and a further exterior point `e`.  Indices are
cyclic.  Put

\[
 \begin{aligned}
 C_i&=S\cup\{a_i\},\\
 T_i&=S\cup\{a_{i-1},a_i\},\\
 R_i&=S\cup\{a_i,e\}.
 \end{aligned}                                                \tag{5.1}
\]

Suppose a rank-`(r-1)`/rank-`r` incidence factor contains the selected
incidences `C_iT_i` and `C_iR_i`.  The four opposite incidences
`C_iT_(i+1)` are precisely the other half of a Boolean star `C8`.

### Theorem 5.1 (Boolean `3+1` neutral fusion)

Toggle

\[
                         C_iT_i\longmapsto C_iT_{i+1}.          \tag{5.2}
\]

Then:

1. every rank-`(r-1)` lower row and every rank-`r` owner keeps degree two;
2. the complete immediate-upper multiplicity vector is unchanged;
3. every deeper named suffix flag rooted at a `C_i` is unchanged; and
4. if the four removed incidences have the aligned `3+1` component order of
   Theorem 2.4, the switch fuses those two components into one.

If, in addition, (5.2) lifts to four legal literal turns and avoids the
protected bank, the fused component is owner-simple, suffix-exact, and
resident.  Its deeper upper defect is exactly (4.3) and obeys (4.5).

#### Proof

Every circuit vertex loses one selected incidence and gains one, proving
the degree rows.  At `C_i`, the old and new immediate-upper values are

\[
 \begin{aligned}
 R_i\cup T_i&=S\cup\{e,a_{i-1},a_i\},\\
 R_i\cup T_{i+1}&=S\cup\{e,a_i,a_{i+1}\}.
 \end{aligned}                                                \tag{5.3}
\]

Thus the four new values are the four old values shifted cyclically, with
identical multiplicities.  The rooted flags do not move.  The topology is
Theorem 2.4, and the literal/residence and deeper-upper conclusions are
Corollaries 3.2 and 4.3.  \(\square\)

The star `C8` is the binary sum of two Boolean incidence hexagons sharing a
diagonal.  The diagonal need not be selectable in the current nonnegative
factor, so (5.2) is an atomic octagon, not a justified sequence of two
hexagon switches.

The octahedral-square common-exterior `C8` has the same conclusion after
the corresponding cyclic relabelling.  The star form (5.1) is singled out
because it gives the simplest explicit four-petal Boolean socket.

The same common-exterior construction with three petals is an
immediate-upper-neutral `C6`.  It fuses three distinct components to one,
but Corollary 2.2 shows that its `2+1` use cannot fuse two components.

## 6. Component count, defect, and the final absorber condition

Consider a serial-safe schedule in which every switch is replayed on the
current literal factor.  Let

* `n_6` be the number of clean `C6` three-to-one fusions;
* `n_8^(31)` the number of aligned `3+1` two-to-one `C8` fusions; and
* `n_8^(4)` the number of clean four-to-one `C8` fusions.

If no switch creates an undeclared split, then the component count is

\[
 c_{\rm final}=c_{\rm initial}-2n_6-n_8^{(31)}-3n_8^{(4)}.     \tag{6.1}
\]

At the same time Proposition 3.3 forces

\[
                       c_{\rm final}\ge\max\{1,\kappa-S\}.     \tag{6.1a}
\]

Thus any proposed packet count violating (6.1a) cannot be realized as the
advertised serial-safe literal schedule.

In particular, hexagons alone preserve component parity.  Subject to
hereditary availability, `(c-1)/2` clean hexagons fuse an odd `c` to one;
for even `c`, `(c-2)/2` clean hexagons leave two and one aligned `3+1`
octagon finishes.

### Theorem 6.1 (one-octagon bounded-interface fusion)

Assume:

1. all preliminary `C6` fusions are literal and protected-safe, preserve the
   immediate-upper multiplicity vector, and are strict-upper
   coverage-transparent;
2. they leave two components;
3. one final common-exterior `3+1` `C8` satisfies Theorem 5.1; and
4. a separately certified owner/suffix/pin/residence/immediate-upper-neutral
   absorber operation covers the exact residual set

   \[
                    A=Z_F(D)\setminus N_{F'}(D').              \tag{6.2}
   \]

Then the terminal factor has one literal Euler component, exact owners,
exact named suffix-target multiplicities, exact immediate-upper
multiplicities, residence, and complete strict-upper coverage through rank
`r+Q`.  The absorber demand satisfies

\[
                              |A|\le10(Q+1)^2.                  \tag{6.3}
\]

#### Proof

The preliminary switches give two components without changing any declared
resource row.  Theorems 5.1 and 2.4 fuse them.  Lemma 1.1 and Corollary 3.2
give owner, suffix, pin, and residence preservation; (5.3) gives exact
immediate-upper multiplicity.  Theorem 4.1 identifies (6.2) as the complete
remaining upper casualty set, and the absorber covers it.  Bound (6.3) is
Corollary 4.3.  \(\square\)

If `Q` is bounded, (6.3) is a bounded absorber interface.  If `Q` grows
with `k` or `d`, the theorem gives the displayed polynomial bound only.  No
`O(1)` additive conclusion follows without a separately bounded upper
horizon, a cut-avoiding witness bank, or a stronger deck-coboundary theorem.

## 7. Exact remaining supply theorem

This note closes the local logic but not the global existence row.  The
remaining Boolean-specific statement is:

> after correlated one-copy owner--flag rounding and clean `C6` reduction,
> the last two components contain an aligned, protected-safe,
> common-exterior `3+1` star `C8` whose four opposite turns are literal and
> whose casualty set (6.2) has a separately certified neutral absorber.

Failure can now be certified in one of four explicit places:

1. no aligned `3+1` alternating `C8` exists across the two components;
2. every such octagon hits a protected successor macroedge;
3. an opposite incidence has no literal age-compatible lift; or
4. the upper casualty set (6.2) has no absorber.

The first obstruction is topological, the second is pinned-resource, the
third is chronological/residence, and the fourth is the bounded upper
interface.  None is implied by fractional pull-clock stationarity or by the
fixed-multiplicity transportation theorem.

## 8. Dependencies and scope reconciliation

The fixed-section owner/suffix formulation is the cycle-hypergraph face of
`MATH_THEOREM_OFHT_EXACT_CYCLE_HYPERGRAPH_FUNCTIONAL_HALL_AND_POINTED_FACE_20260801.md`
and the chronology-first fixed-flag face of
`MATH_THEOREM_CHRONOLOGY_FIRST_OWNER_FLAG_HALL_AND_PROTECTED_EXCHANGE_20260801.md`.
The invariant age budget (3.1)--(3.2) is the component row in
`MATH_THEOREM_INTEGRAL_AGE_CIRCULATION_NORMALITY_AND_LATTICE_OBSTRUCTIONS_20260801.md`.
The common-exterior load identity extends the four-component `C8` calculus
of
`MATH_THEOREM_R_PROTECTED_C8_SPLICE_AND_K17_FOUR_INCIDENCE_FLOOR_20260731.md`
to the aligned two-component `3+1` topology.  The upper casualty set is the
occurrence-labelled cut residual used in the later all-width guard notes.

Nothing here supplies the preceding one-copy integral section.  The modular
and route-cost obstructions in
`MATH_THEOREM_THREAD_D_TPC_ONE_COPY_COLOURED_EULER_ROUNDING_20260801.md`
therefore remain prior gates.
