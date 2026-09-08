# Protected C8 splices and the K17 four-incidence plateau floor

Date: 2026-07-31  
Lane: R  
Status: exact local splice theorem and exact scoped obstruction.  No K17 word
or all-dimensional existence theorem is claimed.

## 0. Verdict

There is a genuine zero-defect component-merging atom beyond incidence
hexagons.

* A clean alternating incidence `C8` can merge four factor components into
  one while preserving the lower-q1 palette automatically.
* Its complete immediate-upper multiplicity vector is unchanged precisely in
  the three forms described in Theorem 3.1.  A clean four-component merger
  can occur only in the common-exterior class.
* If the four removed incidences avoid a selected occurrence-labelled
  all-depth witness bank and the four new joins pass the exact cyclic
  residence boundary test, the switch preserves that entire literal bank and
  residence.  This is a true zero-defect splice theorem, not an aggregate
  load estimate.

However, it cannot be applied verbatim to the frozen K17 Stage2 service
selection.  In the fixed-service degree-two face, the authenticated
max-retention optimum contains only `13596` of `13600` optional protected
incidences.  Therefore the face containing all fixed service incidences and
the whole selected literal protection bank is empty.  Every alternating
circuit whose endpoint remains in the fixed-service face and which installs
`a` currently absent protected incidences must delete at least `a` other
protected incidences when started at an optimum.  C8 and longer circuits can
transport the four-incidence debt inside that face but cannot annihilate it
without changing the provider selection or changing witness representatives.

This is a counterexample to **fixed-bank** monotone protected transport.  It
is not a counterexample to targetwise all-depth coverage: alternate witnesses
or new seam witnesses may replace the four damaged literal incidences.

## 1. Balanced two-extension factors and an alternating circuit

Put

\[
 q=r-1,
 \qquad {\cal L}=\binom{[k]}q,
 \qquad {\cal M}=\binom{[k]}{q+1},
\]

and let `I=I(k,q)` be their inclusion graph.  Let `F` be a simple spanning
degree-two factor of `I`.  Contracting each `C in L` gives a Johnson 2-factor
on `M`, with one edge labelled by every lower colour `C`.  If the two selected
owners containing `C` are `X_C,Y_C`, its immediate-upper value is

\[
                         \sigma_F(C)=X_C\cup Y_C.       \tag{1.1}
\]

Consider a simple `F`-alternating circuit

\[
 C_0,T_0,C_1,T_1,\ldots,C_{\ell-1},T_{\ell-1},C_0,
                                                               \tag{1.2}
\]

where indices are cyclic, `T_i=C_i union C_{i+1}`, the selected half is
`C_i T_i`, and the unselected half is `T_i C_{i+1}`.  Let `R_i` be the
other selected owner incident with `C_i`.  Toggling (1.2) changes

\[
 \{C_iT_i:0\le i<\ell\}
 \quad\hbox{to}\quad
 \{C_iT_{i-1}:0\le i<\ell\}.                            \tag{1.3}
\]

### Lemma 1.1 (exact ledger of a circuit switch)

The switch (1.3) has the following exact effects.

1. Every vertex of `L` and `M` retains degree two.  Hence the lower-q1
   palette remains exact, with exactly the same labelled colours.
2. The immediate-upper multiplicity change is

   \[
   \Delta m(U)=
   \#\{i:R_i\cup T_{i-1}=U\}
   -\#\{i:R_i\cup T_i=U\}.                              \tag{1.4}
   \]
3. If the selected incidences `C_iT_i` lie in `ell` distinct factor
   components, the switch replaces those `ell` components by one component.
   In particular the component change is `1-ell`.

#### Proof

At every circuit vertex one selected incidence is removed and one is added,
which proves the degree and lower-colour statement.  Before the switch the
two selected owners at row `C_i` are `R_i,T_i`; afterwards they are
`R_i,T_{i-1}`.  This proves (1.4).

For the last assertion, deleting `C_iT_i` from each of `ell` distinct cycles
gives `ell` paths with endpoints `C_i,T_i`.  The new incidences
`T_iC_{i+1}` concatenate these paths cyclically into one cycle.  \(\square\)

Thus a clean `C8` changes component count by `-3` and reverses component
parity.  The formula also applies to longer clean circuits; no locality or
hexagon decomposition is being assumed.

## 2. Classification of incidence C8 geometry

Every simple incidence `C8` has one of the following two forms, after cyclic
reindexing.

**Star form.**  There are `S` of rank `q-1` and four distinct petals
`a_0,a_1,a_2,a_3` outside `S` such that

\[
 C_i=S+a_i,
 \qquad T_i=S+a_i+a_{i+1}.                              \tag{2.1}
\]

**Octahedral-square form.**  There are `S` of rank `q-2` and four distinct
petals such that

\[
 C_i=S+a_i+a_{i+1},
 \qquad T_i=S+a_i+a_{i+1}+a_{i+2}.                     \tag{2.2}
\]

These are the standard two shapes: opposite lower vertices have Johnson
distance one in (2.1) and distance two in (2.2).  Conversely both displays
give a simple incidence `C8`.

For completeness, one can obtain the classification directly.  The lower
vertices form a simple Johnson four-cycle with four distinct successive
unions.  If opposite lower vertices have distance one, common-neighbour
classification and distinctness of the upper unions force one common
rank-`q-1` core.  If they have distance two, their two differences each have
size two and the two intermediate common neighbours must use opposite
choices, giving (2.2).

## 3. Exact immediate-upper-neutral C8 classification

### Theorem 3.1 (all load-neutral alternating C8s)

Let (2.1) or (2.2) be `F`-alternating with selected half `C_iT_i`, and let
`R_i` be the other selected owner at `C_i`.  Then the complete immediate-
upper multiplicity vector is unchanged by the toggle if and only if one of
the following holds.

1. **Star/common exterior:** there is one
   `e notin S union {a_0,a_1,a_2,a_3}` such that

   \[
                         R_i=S+a_i+e\quad(0\le i<4).     \tag{3.1}
   \]

2. **Star/antipodal closure:**

   \[
                         R_i=S+a_i+a_{i+2}\quad(0\le i<4). \tag{3.2}
   \]

3. **Octahedral/common exterior:** there is one
   `e notin S union {a_0,a_1,a_2,a_3}` such that

   \[
                         R_i=S+a_i+a_{i+1}+e\quad(0\le i<4). \tag{3.3}
   \]

Moreover, in the antipodal case `R_i=R_{i+2}`.  Consequently the toggled
incidences with indices `i` and `i+2` already lie in the same old factor
component.  A load-neutral C8 which is clean on four components must
therefore be of one of the two common-exterior types (3.1) or (3.3).

#### Proof

In the star form write `R_i=S+a_i+x_i`.  Alternation and simplicity forbid
`x_i=a_{i-1}` and `x_i=a_{i+1}`.  Thus `x_i` is either the antipodal petal
`a_{i+2}` or a point exterior to the four-petal support.  Formula (1.4) gives

\[
 U_i=S+a_i+a_{i+1}+x_i,
 \qquad
 U'_i=S+a_{i-1}+a_i+x_i.                                \tag{3.4}
\]

Fix an exterior point `e` and let `I_e={i:x_i=e}`.  Targets containing `e`
cannot equal a target from an antipodal row or from a row using a different
exterior point.  Within the `e`-class, the old targets are indexed by the
cycle edges `{a_i,a_{i+1}}` for `i in I_e`, while the new targets are indexed
by those edges for `i-1`, `i in I_e`.  All four cycle edges are distinct.
Equality of the two multisets therefore says

\[
                         I_e=I_e-1\pmod 4.              \tag{3.5}
\]

The only shift-invariant subsets of a four-cycle are the empty set and the
whole set.  Hence any exterior point which occurs occurs in all four rows;
this is (3.1).  If no exterior point occurs, every row is forced to use its
antipodal petal, giving (3.2).  Directly, (3.4) then shows that the four old
and four new targets are the same four triples, cyclically permuted.

In the octahedral form write `R_i=C_i+x_i`.  The two petals absent from
`C_i` give exactly the two circuit neighbours `T_{i-1},T_i`; alternation
therefore forces every `x_i` to be exterior to the four-petal support.  Now

\[
 U_i=S+x_i+a_i+a_{i+1}+a_{i+2},
 \qquad
 U'_i=S+x_i+a_{i-1}+a_i+a_{i+1}.                        \tag{3.6}
\]

For each fixed exterior `e`, equality again shifts the index set `I_e` by
one, so (3.5) forces one common exterior point in all four rows.  This is
(3.3).

Finally (3.2) gives `R_i=R_{i+2}`.  The selected path

\[
 C_i-R_i-C_{i+2}
\]

joins the two toggled incidences through the old factor, excluding four-
component cleanliness.  \(\square\)

### Corollary 3.2 (a genuine plateau atom)

A star C8 is the binary sum of the two incidence hexagons on petals
`(a_0,a_1,a_2)` and `(a_0,a_2,a_3)`; their two diagonal incidences cancel.
For a common-exterior alternating C8 those diagonal incidences are absent,
so neither constituent hexagon need be alternating in the current factor.
Thus the C8 is an intrinsically legal compound move even though its binary
hexagon decomposition need not admit a legal intermediate state.

This is the smallest explicit mechanism by which algebraic hexagon
generation can fail to describe nonnegative plateau transport.

### Theorem 3.3 (common-exterior polygon family)

The positive construction is not special to length eight.  Let
`ell>=3`, let `S` have rank `q-1`, and choose pairwise-distinct petals
`a_0,...,a_(ell-1)` and one further point `e`.  Put

\[
 C_i=S+a_i,\qquad T_i=S+a_i+a_{i+1},\qquad R_i=S+a_i+e. \tag{3.7}
\]

If the incidence `C_(2 ell)` through the `C_i,T_i` is `F`-alternating with
selected half `C_iT_i`, then its toggle preserves the complete immediate-
upper multiplicity vector.  If the selected incidences lie in `ell`
distinct factor components, it merges all `ell` into one.

#### Proof

The old and new upper values in row `C_i` are respectively

\[
 S+e+a_i+a_{i+1},\qquad S+e+a_{i-1}+a_i.
\]

The second is the old value in row `i-1`, so the whole load vector is
permuted.  Lemma 1.1 gives the topology.  \(\square\)

Thus common-exterior star polygons give an explicit scalable family of
adjacent-palette-neutral longer switches.  Their existence with PBBS
protected sockets is a separate geometric question.

## 4. Literal all-depth and residence protection

Choose, for every target `Z` required from the factor, an occurrence-
labelled witness span `W_Z`, meaning a contiguous incidence path in `F`
whose contracted owner interval has the required union or intersection.
Let

\[
                         P=\bigcup_Z E(W_Z)              \tag{4.1}
\]

be its literal incidence support.

Cut a clean alternating circuit once in each touched component.  The four
old cycles become paths.  Give those paths the orientations forced by the
new cyclic splice, and let `w_0,...,w_3` be their owner-coordinate words.

For a coordinate `x` and an oriented word `w`, write `p_x(w),s_x(w)` for
the positive prefix and suffix lengths and let `a_x(w)` record that the
whole word is one.  Values may be capped at `h+1` when only positive runs of
length at most `h` are forbidden.

### Lemma 4.1 (exact cyclic boundary-run test)

Assume every `w_i` is internally free of forbidden positive runs.  In the
cyclic concatenation `w_0w_1w_2w_3`, every new positive run for coordinate
`x` is obtained as follows.  Take two consecutive non-all-one fragments in
the cyclic order, with the intervening (possibly empty) block `B` of
all-one fragments.  Its length is

\[
 s_x(w_i)+\sum_{j\in B}|w_j|+p_x(w_{i'}).                \tag{4.2}
\]

If all four fragments are all-one, the only run is the whole cycle.  Hence
the splice preserves minimum positive run `h+1` if and only if every
positive value in (4.2) is at least `h+1` (with the all-one cycle treated as
one full-length run).

#### Proof

Any run not wholly internal to one fragment starts in the suffix of the
last non-all-one fragment before it, traverses exactly the consecutive
all-one fragments, and ends in the prefix of the next non-all-one fragment.
These pieces are disjoint and exhaustive, giving (4.2).  \(\square\)

The same statement for an arbitrary finite residence automaton is obtained
by storing the exact transition monoid element of each oriented fragment and
multiplying the four elements in splice order, including cyclic closure.

### Theorem 4.2 (zero-defect common-exterior C8 splice)

Suppose an alternating C8 in `F` satisfies all of the following.

1. It is clean: its four removed incidences lie in four distinct factor
   components.
2. It has one of the common-exterior forms (3.1) or (3.3).
3. Its removed incidence set is disjoint from the selected literal bank `P`
   in (4.1).
4. Its four oriented cut paths pass Lemma 4.1, or equivalently the complete
   product residence DFA accepts their cyclic splice.

Then the toggle replaces four components by one, preserves the exact lower-
q1 palette, preserves the complete immediate-upper multiplicity vector,
retains every selected all-depth witness literally, and preserves the stated
residence condition.

#### Proof

Lemma 1.1 gives the degree, lower-colour and topology conclusions.  Theorem
3.1 gives equality of the entire immediate-upper load vector, not only
surjectivity.  A witness path avoiding every removed incidence remains a
contiguous path of retained incidences after the splice; reversal of a
whole old strand does not change its union or intersection.  Thus every
`W_Z` survives.  The only new residence runs can cross one or more of the
four joins, and Lemma 4.1 is necessary and sufficient for their safety.
\(\square\)

The theorem extends verbatim to a clean alternating `C_(2 ell)` if one uses
the exact load ledger (1.4), a protected cut-free witness bank, and the
`ell`-fragment residence monoid.  The special contribution of Theorem 3.1
is that for `ell=4` immediate-upper load neutrality has a closed set-theoretic
classification.

### Corollary 4.3 (edge-disjoint witness reserve)

The witness-disjointness hypothesis in Theorem 4.2 is automatic for a C8 if
every required deeper target has five pairwise edge-disjoint old witness
spans.  More generally, `ell+1` pairwise edge-disjoint spans per target
suffice for the witness-survival part of a `C_(2 ell)` switch.  The
residence-DFA hypothesis remains separate.

#### Proof

The switch removes only `ell` incidences.  Those incidences cannot meet all
members of a family of `ell+1` pairwise edge-disjoint spans.  Choose one
survivor for each target and apply Theorem 4.2 (or its polygon extension).
\(\square\)

PBBS presently supplies at least one canonical witness with controlled
load, not this edge-disjoint reserve.  In particular targets of load one
show why the corollary cannot be silently inferred from all-depth support.
The reserve is also only for one switch.  A switch bank needs a reserve
larger than the union of all future deleted incidences, or an explicit
make-before-break reselection after each switch.

## 5. Exact fragment-braid CSP atom

Theorem 4.2 maps without relaxation to the fragment-braid formulation.

* The four removed incidences are four occurrence-labelled cuts.
* The four opposite C8 incidences are the four new seam half-incidences.
* At every lower-colour row one old owner is replaced by one new owner, so
  the lower palette row is an identity row, not a Hall demand.
* The common-exterior classification gives zero immediate-upper signature.
* The blocker vector of a deeper target is zero whenever its selected span
  avoids the four cuts.  More generally its exact row is

  \[
  \mathbf 1\{\hbox{all old spans meet the cuts}\}
  \le
  \mathbf 1\{\hbox{some new suffix--fragment--prefix span realizes it}\}.
                                                               \tag{5.1}
  \]
* The run row is exactly the four-fold monoid product in Lemma 4.1.
* Cleanliness is a four-component hyperedge.  Selecting a sequence in which
  every hyperedge meets four current components reduces the component count
  by three per atom.

Consequently, if a PBBS factor has `c` components and `c` is even, one clean
protected C8 changes it to `c-3`, an odd number.  Protected clean C6 atoms
can then reduce by two.  For example `c=146` has the exact topological
ledger

\[
                   146\xrightarrow{C8}143
                   \xrightarrow{71\ C6\text{s}}1.       \tag{5.2}
\]

Equation (5.2) is only topology.  The missing PBBS theorem is the existence
of the common-exterior C8 socket and the subsequent C6 loose tree with the
literal blocker and residence rows simultaneously zero.

There is an important source-factor caveat.  In the initial canonical PBBS
factor, the audited fixed-matching C8 catalogue reduces to a restricted
directed-C4 catalogue attached to one `(q-1)`-core; that classification does
not supply a clean common-exterior socket.  Therefore Theorem 4.2 does not
assert that such a socket is already present while one canonical PBBS
matching is held fixed.  A usable socket may instead have to be a mixed-half
alternating C8 of the full degree-two incidence factor, or be created after
an earlier protected rethread/long circuit.  This is consistent with
Corollary 3.2: binary hexagon generation does not make either constituent
hexagon legally toggleable at the starting state.

## 6. The frozen K17 Stage2 obstruction

We now use only the authenticated finite facts supplied for the current K17
source/service choice.

The Stage2 cut-and-service operation serves all `1838` previously missing
deep targets, but cutting the `3336` source edges destroys the last old
witness of exactly `3489` targets, split by upper rank as

\[
                  (1864,1221,386,18).                    \tag{6.1}
\]

Thus targetwise provider injection is not a protected factor theorem.

More sharply, let `A` be the `3676` fixed service incidences and `P` the
`13600` optional incidences in the selected protected-span bank.  In the
degree-two face

\[
             {\cal F}_A=\{H:\ H\text{ is a spanning degree-two factor},
                                  \ A\subseteq H\},       \tag{6.2}

\]

the exact max-retention result is

\[
                    \max_{H\in{\cal F}_A}|H\cap P|=13596. \tag{6.3}

One optimum loses the four incidences

\[
 (7847,7843),\quad(79406,71214),\quad
 (96540,80156),\quad(109506,109250),                     \tag{6.4}

\]

affecting provider rows `814,1024,1325,1352`.  The individual optimum has
`6796` fully retained protected physical edges and four partially retained
ones.  The optimization is incidencewise and explicitly has no bundle
guarantee.

There is also a short, solver-free cut certificate for nonexistence of the
full bank.  Put

\[
 U_* = \{73379,109258\}
\]

and

\[
\begin{split}
 L_* = \{&7843,43722,69283,71331,72867,73251,73347,73377,\\
         &73378,101066,107210,108746,109130,109194,109250,109256\}.
                                                               \tag{6.5}
\end{split}
\]

After prescribing `A union P`, the two upper owners in `U_*` have total
residual demand four, every lower row in `L_*` has residual capacity zero,
and the only full-inclusion-graph neighbours of `U_*` outside `L_*` are

\[
                     72355\quad\hbox{and}\quad76490.    \tag{6.6}
\]

Indeed the nine lower neighbours of `73379` are the eight listed members of
`L_*` plus `72355`, and the nine lower neighbours of `109258` are the other
eight listed members plus `76490`.  Thus the residual cut has capacity two
against demand four.  There are exactly twenty protected incidences in

\[
                        P\cap E(U\setminus U_*,L_*).
\]

By the first state containing all fixed
service incidences, at least two members of this twenty-edge set must already
be absent; they may have been released earlier or simultaneously.  No fixed
pair is individually forced.  This argument is independent of circuit
length.  The separate exact optimization (6.3) strengthens this
hand-checkable floor from two to four for the frozen bank.

### Theorem 6.1 (four-incidence protected-face floor)

Inside the fixed service face (6.2):

1. no degree-two factor contains the whole literal bank `P`;
2. no C8, longer alternating circuit, or sequence of alternating circuits
   can start and end in (6.2) while ending with every incidence of `P`;
3. if `H` is an optimum in (6.3), and a circuit switch adds `a` incidences
   of `P\setminus H` while deleting `b` incidences of `P\cap H`, then

   \[
                              b\ge a.                    \tag{6.7}
   \]

Hence every fixed-service circuit move from an optimum is debt-transporting
rather than strictly debt-annihilating at the four-incidence plateau.

#### Proof

The first statement is exactly (6.3).  Every alternating-circuit endpoint
is again a degree-two factor.  If the sequence retains `A`, its endpoint
belongs to (6.2), so the first statement proves the second.  Finally the new
defect is

\[
 |P\setminus H'|=4-a+b.
\]

Equation (6.3) says this is at least four, proving (6.7).  \(\square\)

### Lemma 6.2 (why four suggests C8 but does not close it)

The incidence graph has no four-cycles.  Suppose two degree-two factors
have symmetric difference consisting of exactly four additions and four
deletions.  Their balanced red/blue symmetric difference is then one
alternating C8.

#### Proof

The symmetric difference decomposes into edge-disjoint alternating even
circuits.  Every circuit has at least six edges.  A decomposition of eight
edges cannot contain two such circuits, and a single circuit must therefore
use all eight.  \(\square\)

Thus a radius-four incidence repair, if it existed after relaxing the fixed
face, would have exactly the C8 form.  But (6.3) proves that within the
frozen face a C8 can only move the four missing incidences to four other
locations.  The numerical coincidence is a boundary normal form, not a
completion certificate.

The maximum-retention factor makes the distinction from target protection
especially stark.  It contains all fixed service incidences and all `1838`
new service targets (the four affected service rows have alternate literal
Johnson intervals), yet it has `6499` holes among targets covered by the old
factor, with rank profile

\[
                         (4066,2036,388,9).             \tag{6.8}
\]

Thus an arbitrary balanced `b`-flow can be incidence-optimal while being
far from all-target protected transport.

## 7. Precise remaining theorem

The fixed Stage2 selection must be broadened in at least one of two ways.

1. **Provider exchange:** change some of the `1838` service seams so that the
   new fixed-service face intersects the full chosen protection face.
2. **Witness exchange:** retain the service seams but replace damaged literal
   spans by alternate old spans or by new suffix--fragment--prefix spans.

For one proposed C8 or longer circuit with removed set `R` and inserted set
`N`, targetwise all-depth preservation is exactly

\[
 \forall Z:\quad
 \bigl(\exists W\in{\cal W}_F(Z):E(W)\cap R=\varnothing\bigr)
 \ \lor\ 
 \bigl(\exists W'\in{\cal W}_{F\triangle(R\cup N)}(Z)\bigr). \tag{7.1}
\]

Together with (1.4), Lemma 4.1, and clean component incidence, (7.1) is the
exact protected alternating-circuit column for the fragment-braid CSP.

A zero-defect K17 completion would follow from a sequence of such columns
which:

* merges all components;
* preserves the exact lower palette;
* satisfies (7.1) for every upper target after each compound bank handoff;
* passes the product residence DFA; and
* is compatible with the final staircase/common-cap compiler.

Neither the Stage2 `1838`-provider injection nor arbitrary degree-two
`b`-flow proves this.  Conversely, the four-incidence floor proves no
targetwise impossibility after provider/witness exchange.  No assertion
`nu(17)=B(17)` is made here.

## 8. Audit boundary

The purely mathematical claims independently checked in this note are:

1. the general circuit ledger (1.4) and clean topology formula;
2. both incidence-C8 shapes;
3. the three and only three immediate-upper-load-neutral C8 forms;
4. exclusion of the antipodal star from a clean four-component merge;
5. the exact cyclic residence boundary formula;
6. literal survival of every cut-disjoint witness span;
7. the four-incidence debt inequality (6.7);
8. the explicit two-owner Hoffman cut (6.5)--(6.6); and
9. the C4-free radius-four/C8 normal form.

The finite equalities (6.1)--(6.4) are used at exactly their authenticated
scope.  In particular, (6.3) concerns individual incidences in one fixed
service face.  It neither certifies bundled target survival nor rules out a
different provider bank.  This scope restriction is essential.
