# Thread R: exact Pascal-seam common-`Q` gluing and the first resident sectorwise obstruction

Date: 2026-07-28

Status: independent audit of the corrected Shadow--Braid sufficient theorem;
an exact necessary-and-sufficient collar gluing theorem; and a minimal
symbolic counterexample, in a precisely stated two-pin class, to automatic
sectorwise compiler composition.  This note does **not** disprove the
Shadow--Braid sufficient theorem, the existence of a different Pascal braid,
or the conjectural formula.

## 0. Verdict

The corrected fixed-braid theorem in
`THREAD_D_EXACT_SHADOW_BRAID_INDUCTION_AND_CUT_AWARE_OBSTRUCTION_20260728.md`
is valid as a conditional sufficient theorem.  Its decisive clauses really
are independent:

1. the intended middle order and its residence determine a maximal erosion
   envelope;
2. cut-aware occurrence budgets decide which upper and natural lower
   shadow windows still exist in that intended middle order;
3. every selected lower occurrence must still be installed as a physical
   pin; and
4. all central, lower, seam, boundary, and endpoint pins must pass one
   common coordinatewise allowed-position system `Q`, including physical
   nonzeroness.

The Pascal-recursive seam step is therefore not automatic from feasible
sector compilers.  The exact valid step is the collar theorem proved below.
It checks the intersection of the transported sectorwise allowed sets at
every affected central or extra positive requirement.  Neither nonempty
maximal erosion nor separate sectorwise private hits imply that check.

The smallest nonredundant example in the scoped depth-one/two-pin class is
the actual parameter `k=6`, where `d(6)=1`.  It has a resident Johnson
collar

\[
       136,\ 123,\ 124,\ 145,
\]

whose three relevant internal erosion states are

\[
       13,\ 12,\ 14,
\]

and two distinct individually feasible singleton pins

\[
       [1,1]\mapsto3,
       \qquad [2,2]\mapsto2.
\]

After both are imposed, every physical position remains nonempty, but
coordinate `1` has no allowed occurrence in the first central window.  Thus
the common maximal word has first derivative value `23`, not `123`.

This is not the simpler `k=4` collar `12,23,24`: that triple has the internal
singleton run `3` and already fails depth-one residence.  The present
example passes residence and isolates the common-`Q` obstruction.

## 1. Audit of the corrected fixed-braid theorem

Let

\[
 T=(T_0,\ldots,T_{W-1})
\]

be the intended rank-`r` middle order at deadline `d`.  For a physical
position `p` put

\[
 E_p=\bigcap_{\substack{0\le i<W\\i\le p\le i+d}}T_i.
\tag{1.1}
\]

For a pin family `Pi`, containing the central pins

\[
 [i,i+d]\mapsto T_i,
\tag{1.2}
\]

define

\[
 Q_x=\{p:x\in E_p\}\setminus
     \bigcup_{(I,S)\in\Pi:\ x\notin S}I.
\tag{1.3}
\]

This is equivalent to the formulation which starts from the whole physical
line, since the negative parts of the central pins cut it down to (1.1).

### Proposition 1.1 (audit of the common-`Q` criterion)

The pin family is realized by one nonzero word with depth-`d` middle row
`T` if and only if

\[
 Q_x\cap I\ne\varnothing
       \qquad((I,S)\in\Pi,\ x\in S)
\tag{1.4}
\]

and

\[
 \{x:p\in Q_x\}\ne\varnothing
       \qquad(0\le p<W+d).
\tag{1.5}
\]

When they hold, the maximal word

\[
                         A_p=\{x:p\in Q_x\}
\tag{1.6}
\]

realizes every pin.

#### Proof

Every negative pin condition forces the deletion made in (1.3).  Every
positive coordinate of a pin needs a surviving position in its interval,
which is (1.4).  Conversely, (1.3) gives containment in every pin label and
(1.4) gives the reverse inclusion after taking the interval union.  Equation
(1.5) is exactly the nonzero-letter condition.  Applying (1.4) to the
central pins gives

\[
                         \bigcup_{p=i}^{i+d}A_p=T_i.
\]

This proves necessity and sufficiency.  \(\square\)

Three cautions follow.

* `E_p` nonempty for every `p` is necessary but not sufficient.  Other pins
  may make the set in (1.5) empty.
* Even pointwise nonemptiness of the final maximal word is not sufficient.
  A coordinate required by a central or lower pin may lose all of its
  positive positions.  The example in Section 4 has exactly this form.
* A natural lower shadow occurrence is negative-inert only when installed
  alone.  After all other pins are imposed, every positive coordinate of
  that natural pin still has to pass (1.4).

### Proposition 1.2 (audit of cut-aware occurrence accounting)

Fix a decorated braid `Gamma`.  Let `C_Gamma` contain every old edge,
vertex, or index disruption.  For a signed target `S`, let
`O^epsilon(S)` be its old occurrence family with full supports, and let
`N_Gamma^epsilon(S)` be the final windows of value `S` crossing at least one
new seam.  Then the final number of occurrences is exactly

\[
 m_Gamma^\epsilon(S)=
 \#\{P\in O^\epsilon(S):
                \operatorname{supp}(P)\cap C_Gamma=\varnothing\}
 +\#N_Gamma^\epsilon(S).
\tag{1.7}
\]

A window crossing several seams is counted once.  On the lower side only
depths `1<=q<=d` can be credited to maximal-envelope cells.  Thus the budget

\[
                         \beta_Gamma^\epsilon(S)
                         =m_Gamma^\epsilon(S)-1
\tag{1.8}
\]

is an exact support test.  It is not a physical compiler test.

#### Proof

Every final window either lies wholly inside one retained oriented source
piece or crosses at least one new seam.  In the first case reversal changes
neither its union nor its intersection, and the old occurrence survives
exactly when its complete support avoids the disruption.  The two classes
are disjoint and exhaustive, proving (1.7).  The lower depth restriction is
the physical row identity `(d-q,i+q)`; a longer intersection has no such
short cell.  \(\square\)

Consequently the corrected Shadow--Braid theorem is logically sound:
upper support is settled by (1.7), protected lower support supplies only a
candidate physical pin, and Proposition 1.1 settles all pins together.  The
all-`k` induction theorem remains conditional because it assumes the
existence of decorated child braids passing these tests; Pascal's deck
identities do not construct them.

## 2. Exact common-`Q` collar gluing

We now isolate the precise seam step which *can* be iterated.

Start with oriented source pieces carrying feasible local pin systems.
Transport their positions, labels, and named private-hit witnesses into a
proposed final order.  Add all new seam, endpoint, spill, and boundary pins,
and recompute the final middle envelope (1.1).  Let `Q_x` be the global
allowed sets (1.3).

Let `K` be any physical collar with the following property:

* outside `K`, the final envelope membership and every negative pin
  incidence agree with the transported feasible source systems; and
* every transported positive requirement whose old named witness may have
  changed is declared affected.

The minimal such collar consists of the changed erosion positions, the
supports of changed extra pins, and any positions of old private-hit
witnesses invalidated by the transport.  Enlarging `K` is harmless.

Let `R_K` be the set of affected positive requirements.  It contains:

1. every central pair `([i,i+d],x)` with `x in T_i` whose interval meets
   `K` and whose old named hit is not certified outside `K`; and
2. every extra pair `(I,x)` with `x in S` for a pin `(I,S)` whose old named
   hit is not certified outside `K`, including every new pin.

### Theorem 2.1 (exact collar gluing criterion)

Assume all unaffected source requirements retain their named witnesses
outside `K`.  The transported pieces and new seam data admit one common
nonzero physical compiler if and only if

\[
 Q_x\cap I\ne\varnothing
                    \qquad((I,x)\in R_K)
\tag{2.1}
\]

and

\[
 \{x:p\in Q_x\}\ne\varnothing
                    \qquad(p\in K).
\tag{2.2}
\]

Equivalently, every affected central private hit, every affected lower or
boundary private hit, and every affected nonzero letter must be checked
against the **intersection** of all transported and new allowed-position
systems.  Separate sectorwise checks are insufficient.

#### Proof

Necessity is Proposition 1.1.  Conversely, every unaffected positive
requirement has its certified old witness outside `K`; by the definition of
`K`, that position remains in the final `Q_x`.  Every affected positive
requirement is supplied by (2.1).  Source nonzeroness persists outside `K`,
and (2.2) supplies it inside `K`.  Thus (1.4)--(1.5) hold globally, and
Proposition 1.1 gives the common maximal word.  \(\square\)

This statement is an exact `if and only if`, not a sufficient scalar
surrogate.  It also handles an interval crossing several seams: the
requirement appears once with its whole physical interval.

### Corollary 2.2 (complete cut-aware seam step)

A proposed Pascal splice of already valid pieces gives a valid fixed-braid
Shadow--Braid certificate if and only if all of the following hold.

1. The final middle order is the exact intended deck.
2. The final order passes the direct residence/run test.
3. Every upper target has nonnegative cut-aware budget (1.8).
4. Every protected lower target has nonnegative budget, one surviving or
   new occurrence is selected at a physical depth `1<=q<=d`, and all other
   lower targets are assigned injectively to actual short cells.
5. The resulting full pin system passes (2.1)--(2.2).

#### Proof

Items 1--4 are exactly the deck, residence, and old/new window partition.
Item 5 is Proposition 1.1 in the localized form of Theorem 2.1.  The usual
identity

\[
 \bigcup_{p=i}^{i+d+q}A_p
       =\bigcup_{j=0}^{q}T_{i+j}
\]

then lifts every upper occurrence to the same physical word.  \(\square\)

Corollary 2.2 proves the seam step *conditional on the collar certificate*.
It does not prove that every parent package has a collar satisfying it.

## 3. Exact seam costs

Suppose `J` old transition slots are cut and the resulting blocks are joined
through `J` new seams.

### Lemma 3.1 (controller and occurrence collar bounds)

At deadline `d`, the old and new erosion collars together contain at most

\[
                              2dJ
\tag{3.1}
\]

physical positions, before overlaps and endpoint truncation.  At flag depth
`q`, at most `qJ` old windows meet deleted edges and at most `qJ` final
windows cross inserted seams.  Hence the old/new depth-`q` occurrence
symmetric difference has size at most

\[
                              2qJ.
\tag{3.2}
\]

If `M` changed noncentral pins are all short cells, their physical intervals
add at most `dM` positions to a crude union bound for `K`.

#### Proof

A seam between middle positions `a,a+1` is seen by exactly the mixed
erosion positions `a+1,...,a+d`, subject to endpoint truncation.  Apply this
to the old and new seam sets.  A fixed transition edge lies in at most `q`
windows of `q+1` consecutive vertices, proving (3.2).  A noncentral short
cell has depth `<d` and therefore interval length at most `d`.  \(\square\)

The bounds are bookkeeping bounds only.  They do not imply that the lost
targets have suitable new occurrences, nor that the global `Q` intersection
has the needed private hits.  Overlapping collars must be audited as their
union, and multi-seam windows are counted once in (1.7).

## 4. A resident sectorwise-compiler obstruction at `k=6`

We give the local data in set notation on `[6]`.  For `k=6`,

\[
 r=3,\qquad W={6\choose3}=20,
 \qquad \Lambda={6\choose1}+{6\choose2}=21,
\]

and hence

\[
                         d(6)=1
\tag{4.1}
\]

because `W+1=21`.

Consider the rank-three Johnson path segment

\[
 T_{-1}=136,\qquad T_0=123,\qquad
 T_1=124,\qquad T_2=145.
\tag{4.2}
\]

All three transitions are Johnson.  At deadline one the maximal erosion on
the five physical positions of this linear segment is

\[
 P_0=136,
 \quad P_1=T_{-1}\cap T_0=13,
 \quad P_2=T_0\cap T_1=12,
 \quad P_3=T_1\cap T_2=14,
 \quad P_4=145.
\tag{4.3}
\]

Every set in (4.3) is nonempty.  The displayed path is depth-one resident:
coordinates `3`, `2`, and `4` have respectively the two-vertex runs
`T_{-1},T_0`, `T_0,T_1`, and `T_1,T_2`; coordinate `1` spans the segment;
and the singleton runs of `6` and `5` meet the two linear endpoints.

Add two distinct lower pins

\[
 c_L=([1,1],3),
 \qquad
 c_R=([2,2],2).
\tag{4.4}
\]

The system containing only `c_L` is feasible.  Its maximal letters on the
collar are

\[
                         136,\ 3,\ 12,\ 14,\ 145,
\tag{4.5}
\]

so all four displayed central unions are unchanged.  The system containing
only `c_R` is also feasible.  Its maximal letters are

\[
                         136,\ 13,\ 2,\ 14,\ 145,
\tag{4.6}
\]

and all four central unions are again unchanged.  Every displayed letter is
nonempty in both systems.

After both pins are imposed, the common maximal letters are

\[
                         136,\ 3,\ 2,\ 14,\ 145.
\tag{4.7}
\]

They still realize both extra pins and are pointwise nonempty.  However,

\[
 Q_1\cap[1,2]=\varnothing,
 \qquad
 A_1\cup A_2=23\ne123=T_0.
\tag{4.8}
\]

Thus the two sectorwise positive witnesses for coordinate `1` cross:
`c_L` leaves only position `2` available in the central window for `T_0`,
while `c_R` leaves only position `1`; their common `Q_1` leaves neither.

At the intended middle-row level the seam `123|124` is Johnson and has the
perfectly valid windows

\[
                         123\cap124=12,
 \qquad
                         123\cup124=1234.
\tag{4.9}
\]

Hence a cut-aware ledger may correctly credit these intended lower/upper
windows.  That fact does not repair (4.8).  In particular, if the natural
lower value `12` is selected as the seam pin, its positive coordinate `1`
is incompatible with `c_R` at the same physical erosion position `2`.
This is exactly why lower occurrence survival and common-`Q` installation
are separate clauses of the corrected theorem.

### Proposition 4.1 (scoped minimality)

Among local obstructions with all of the following properties,
the example above has the smallest actual dimension:

1. the actual deadline is `d(k)=1`;
2. one rank-`r` Johnson seam is used;
3. two **distinct** nonempty singleton lower-target pins occupy the two
   physical positions of one central window;
4. each one-pin system separately realizes the intended adjacent central
   rows with nonzero letters;
5. the two-pin maximal word is still pointwise nonempty but loses a central
   positive coordinate.

#### Proof

No such obstruction exists at `d=0`, since a central window has one physical
position and there is no lower short-row pin to compose.

At `d=1`, let `a` be the central coordinate lost after the two pins are
combined.  Both pin labels omit `a`.  The two physical erosion positions of
that central window are subsets of its rank-`r` label.  If `r=2`, the only
nonempty subset left after omitting `a` is the other singleton `{b}` at
either position.  Thus the two nonempty pin labels are equal, contrary to
the required distinctness.  Hence `r>=3`.

For actual middle rank `r=ceil(k/2)`, the dimensions below six with
`r>=3` consist only of `k=5`, but

\[
 W_5=10,
 \qquad \Lambda_5=5+10=15,
 \qquad 10+1<15,
\]

so `d(5)=2`, not one.  At `k=6`, (4.1) holds and (4.2)--(4.8) realize every
listed property.  \(\square\)

The scope of Proposition 4.1 is deliberate.  If duplicate pin labels are
allowed, or if more pins, a larger deadline, non-Johnson seams, or a failure
of pointwise nonzeroness is permitted, smaller symbolic obstructions exist.
It is not a minimum counterexample to the all-`k` conjecture.

## 5. Separation from the elementary nonresidence obstruction

At `k=4`, deadline one, the three rank-two states

\[
                         12,\ 23,\ 24
\tag{5.1}
\]

have Johnson transitions.  Nevertheless coordinate `3` occurs only in the
middle state, giving an internal one-run of length one.  The chronology
therefore fails residence before lower pins or common `Q` are considered.
Equivalently, the two incident erosion states both equal `{2}`, so the
controller repeats a vertex.

By contrast, (4.2) passes the complete depth-one run test and has three
nonempty erosion states.  Its failure (4.8) occurs only after two separately
feasible lower pin systems are intersected.  Therefore:

\[
 \boxed{
 \text{Johnson seam}\not\Rightarrow\text{residence},
 \qquad
 \text{residence + sectorwise compilers}
      \not\Rightarrow\text{common compiler}.}
\tag{5.2}
\]

These are two different gates and neither may be used as a substitute for
the other in a Pascal recurrence.

## 6. Exact surviving all-`k` gate

The corrected sufficient theorem survives the audit.  The recursive
existence claim does not follow from parent packages unless one proves the
following additional statement at every lift:

> Choose the child sector cuts, orientations, selectors, seams, protected
> occurrences, and injective lower cells so that the direct residence test
> and every cut-aware budget pass, and so that the affected collar
> requirements (2.1)--(2.2) hold for the intersection of **all** transported
> and new allowed-position systems.

This is exactly the Pascal-recursive seam gate.  Theorem 2.1 proves its
logical sufficiency and necessity once a decorated braid is specified.
Section 4 proves that it cannot be replaced by separate sector compilers,
even with a resident Johnson collar, nonempty erosion, pointwise nonempty
combined letters, and valid intended seam shadows.

No unconditional construction of such collars for every `k` is supplied
here.  No counterexample to a globally repinned or off-spine child braid is
proved.
