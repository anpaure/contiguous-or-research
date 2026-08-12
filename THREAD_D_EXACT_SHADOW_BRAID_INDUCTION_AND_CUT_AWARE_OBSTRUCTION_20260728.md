# Thread D: exact Shadow--Braid induction and the cut-aware compatibility obstruction

Date: 2026-07-28

Status: exact conditional induction theorem, exact fixed-braid equivalence,
the first fully audited obstruction in the current catalogue to the strict
native priority lift, and an exact restricted `k=15` atlas isolated-collar
no-go.  No unconditional all-`k` induction is claimed.

## 0. Verdict

The Pascal and diamond constructions have one exact common form.

* A **shadow** is a middle-layer ordering `T` whose consecutive
  intersections/unions carry the lower/upper flag tower.
* A **braid** cuts source shadows into oriented pieces and reconnects them
  into one child ordering.
* A **compiler** is one physical word `A`, not four sectorwise words or a
  collection of independent row matchings.

For a fixed child braid, the optimal formula

\[
                         \nu(k)=B(k)
\]

follows if and only if the following four data are simultaneously present
inside the flat-middle Shadow--Braid normal form.

1. The braided ordering is a permutation of the child middle layer.
2. It is resident at the exact monotone-deadline depth.
3. Every upper target has a surviving internal or new seam-crossing
   consecutive-union witness.
4. Every lower target, every central cell, and every lower seam/boundary pin
   are realized by one coordinatewise compatible physical word.

The word “simultaneously” is the induction gate.  Pascal decomposition gives
the correct child **deck**, but it does not choose cuts, a `U` selector,
ports, or the common compiler.

For a strict Johnson braid, the last two requirements admit an exact lower
normal form.  The maximal depth-`d` erosion is a rank-`(r-d)` Johnson
controller on its flat interior.  A common compiler exists exactly when the
maximal allowed positions on every controller run retain the forced
endpoints, have gaps at most `d+1`, hit every positive lower pin, and leave
no physical position empty.  In addition, its coordinate incidences obey
`p_x=t_x-d i_x`.  Pascal sectors transport this controller only away from
completion and seam collars; each seam creates `d` genuinely mixed
controller states.

On the frozen Hall-29 `k=15` carrier, the independent-collar version of this
program is now closed for the **1,602 atlas-derived UNIT pins**.  Of their
1,601 flat instances, 1,318 admit one isolated rank-preserving
single-controller-state edit; the resulting one-middle-state replacement
digraph is acyclic.  Hence no nonempty pairwise `8`-separated family of
those isolated edits preserves the middle deck.  This is not a no-go for
raw UNIT pairs outside the retained atlas, overlapping collars, or
multi-state edits.  Any surviving atlas-UNIT construction must introduce a
closed interacting deck circuit.

The correct cut statistic is not a target's raw multiplicity.  For a braid
`Gamma` and a signed target `S`, the exact protected-occurrence budget is

\[
 \beta_\Gamma^\pm(S)=
 \#\{P\in\mathcal O^\pm(S):
          \operatorname{supp}(P)\cap C_\Gamma=\varnothing\}
 +\#\mathcal N_\Gamma^\pm(S)-1.
\tag{0.1}
\]

Here `C_Gamma` is the actual disruption set and `N_Gamma` is the set of
final windows crossing at least one new seam.  A multi-seam window is counted
once.  On the lower side both the old and new occurrence families are
restricted to depths `1<=q<=d`; a longer seam-crossing intersection has no
physical cell `(d-q,i+q)` and earns no lower credit.  Every upper target
requires `beta>=0`.  A lower target with negative budget is legal only when
the **same** physical compiler gives it another cell.

This makes scalar load `>=2` insufficient as a survival certificate.  In
the exact strict inherited-edge `11 -> 13` first-priority `U` selector, one
empty-signature upper target has
four old provider intervals, but the selector deletion set hits all four.
Its raw load is four and its exact budget is `-1`; ordinary cross-sector
seams and the lower compiler cannot repair it.  This is the first fully
audited failure in the current catalogue of the natural same-parity
Shadow--Braid rule.  It is not a no-go for adaptive, off-spine, or
same-signature `UU`-rethreaded `11 -> 13` braids.

## 1. The flat-middle Shadow--Braid normal form

Put

\[
 r=\left\lceil\frac{k}{2}\right\rceil,
 \qquad W=\binom kr,
 \qquad
 \Lambda=\sum_{s=1}^{r-1}\binom ks.
\tag{1.1}
\]

Let `d=d(k)` be the least nonnegative integer satisfying

\[
 \Lambda\le dW+\binom{d+1}{2},
 \qquad B(k)=W+d.
\tag{1.2}
\]

For a nonzero set word

\[
 A=(A_0,\ldots,A_{n-1}),
\]

write

\[
 (DA)_i=A_i\cup A_{i+1},
 \qquad
 (D^tA)_i=\bigcup_{j=0}^{t}A_{i+j}.
\tag{1.3}
\]

The monotone-deadline lower bound gives `nu(k)>=B(k)`.  We now isolate the
exact equality certificate.

Let

\[
 T=(T_0,\ldots,T_{W-1})
\tag{1.4}
\]

be an ordering of the rank-`r` layer.  At the proposed length `W+d`, define
its maximal central envelope by

\[
 E_p(T)=
 \bigcap_{\substack{0\le i<W\\i\le p\le i+d}}T_i,
 \qquad 0\le p<W+d,
\tag{1.5}
\]

Call `T` **depth-`d` resident** when

\[
                    T_i=\bigcup_{p=i}^{i+d}E_p(T)
                    \qquad(0\le i<W).
\tag{1.6}
\]

This is the exact coordinatewise residence condition for any chronology:
every internal one-run has length at least `d+1`, with the corresponding
one-sided endpoint convention.  Equation (1.6), rather than an average run
length, is authoritative.

### 1.1 One physical pin system

A physical row cell is a pair

\[
                         c=(t,i),
 \qquad 0\le t\le d,\qquad0\le i<W+d-t,
\]

with physical interval

\[
                         I_c=[i,i+t].
\tag{1.7}
\]

A pin system `Pi` assigns a label \(S_c\subseteq[k]\) to selected cells.  It
always contains the central pins

\[
                         (d,i)\longmapsto T_i
                         \qquad(0\le i<W).
\tag{1.8}
\]

For coordinate `x`, define its allowed physical positions

\[
 Q_x(\Pi)=[0,W+d-1]\setminus
 \bigcup_{c:\,x\notin S_c}I_c.
\tag{1.9}
\]

### Proposition 1.1 (exact simultaneous compiler criterion)

The pins `Pi` are realized by a nonzero physical word if and only if

\[
 Q_x(\Pi)\cap I_c\ne\varnothing
 \qquad(c\in\Pi, x\in S_c),
\tag{1.10}
\]

and

\[
 \{x:p\in Q_x(\Pi)\}\ne\varnothing
 \qquad(0\le p<W+d).
\tag{1.11}
\]

When these conditions hold, the coordinatewise maximal word

\[
                         A_p=\{x:p\in Q_x(\Pi)\}
\tag{1.12}
\]

realizes every pin.

#### Proof

If `x notin S_c`, then `x` must be absent throughout `I_c`, giving the
forbidden union in (1.9).  If `x in S_c`, it must occur somewhere in
`I_c`, giving (1.10).  These conditions are necessary.  Conversely,
(1.12) excludes every negative coordinate from every pin and (1.10) gives
every positive coordinate a private hit.  Hence the union on `I_c` is
exactly `S_c`.  Condition (1.11) makes every source letter nonzero.
\(\square\)

This is the missing common quantifier.  Separate Hall matchings for lower
ranks or Pascal sectors need not have the same allowed sets `Q_x` and do not
imply Proposition 1.1.  Likewise, rankwise hypersimplex completion settles
marginals but not the common physical intervals in (1.9).

### Theorem 1.2 (Shadow--Braid sufficiency)

Assume:

1. `T` enumerates every rank-`r` set exactly once;
2. `Pi` contains (1.8), assigns every target of rank below `r` injectively
   to a cell of depth `<d`, and satisfies (1.10)--(1.11); and
3. every target of rank above `r` is the union of a consecutive block of
   `T`.

Then the word (1.12) has length `B(k)`, covers every nonempty subset of
`[k]`, and

\[
                         \boxed{\nu(k)=B(k).}
\tag{1.13}
\]

#### Proof

The central pins give `D^dA=T`.  The lower pins cover the whole lower ideal,
and `T` covers the middle layer.

Every interval of `A` having length at least `d+1` is the union of the
consecutive central windows which it contains.  Explicitly,

\[
 \bigcup_{p=i}^{i+d+q}A_p
 =\bigcup_{j=0}^{q}T_{i+j}.
\tag{1.14}
\]

Thus condition 3 covers the upper ideal.  The construction has length
`W+d`; the monotone-deadline lower bound proves equality.  \(\square\)

Conversely, any length-`B(k)` word whose depth-`d` row is a permutation of
the middle layer produces such a `T` and a pin system by choosing one actual
witness cell for each lower target.  Hence Theorem 1.2 is an equivalence
inside the flat-middle normal form.  Bare equality `nu(k)=B(k)` need not
produce this normal form when the arithmetic slack is positive.

## 2. Cut-aware shadows and minimal seam data

Let source chronologies be cut into oriented pieces and concatenated into a
candidate child order `T^+`.  A source occurrence of target `S` is recorded
with its full support: every source vertex, transition, or selected index
needed to retain it.  For upper targets let

\[
 \mathcal O^+(S)
\tag{2.1}
\]

contain the old union occurrences over all relevant window lengths.  For
protected natural lower pins let `O^-(S)` contain only intersection windows
of `q+1` middle vertices with `1<=q<=d^+`; longer intersections do not map
to lower physical rows through `(d^+-q,i+q)`.  Let `C_Gamma` be the full
disruption set of a decorated braid `Gamma`.

Every final window is uniquely of one of two kinds:

* it lies wholly inside one oriented old piece and corresponds to an old
  occurrence avoiding `C_Gamma`; or
* it crosses at least one new seam and belongs to `N_Gamma`.

For lower occurrences, `N_Gamma^-(S)` is subject to the same
`1<=q<=d^+` restriction as `O^-(S)`.  In particular, a long intersection
cannot make `beta_Gamma^-(S)` nonnegative without an available physical
row.

Therefore (0.1) is an identity, not an estimate.  Reversal does not change
the intersection or union of an internal window.

For a protected target family `P`, the source-only safe-cut complex is

\[
 \mathcal K_{\mathcal P}^{\pm}
 =\left\{C:
   \forall S\in\mathcal P\ \exists P\in\mathcal O^\pm(S),\quad
       \operatorname{supp}(P)\cap C=\varnothing\right\}.
\tag{2.2}
\]

New seam replacements are credited only after the seam order is fixed.
Residence is different: its short-run intervals form a clutter which the
cut set must hit.  Thus a legal choice must lie in the protected-occurrence
complex while simultaneously transversing the residence clutter.  Neither
raw multiplicity nor a minimum load controls this intersection.

### Lemma 2.1 (exact rank of a seam)

Let consecutive child middle sets `M,N` have common rank `R`, and put

\[
                         s=R-|M\cap N|.
\tag{2.3}
\]

If `T^+=D^{d^+}A`, then

\[
                         (DT^+)_i=M\cup N,
\tag{2.4}
\]

of rank `R+s`.  In the maximal central envelope `E(T^+)`, the corresponding
first lower cell is

\[
                         (D^{d^+-1}E)_{i+1}=M\cap N,
\tag{2.5}
\]

of rank `R-s`.

#### Proof

Equation (2.4) is the definition of `D`.  Formula (2.5) is the intersection
of the two adjacent central constraints in the maximal envelope.  The rank
claims follow from equal rank of `M,N`.  \(\square\)

Thus Johnson adjacency (`s=1`) supplies the expected immediate lower and
upper seam ranks, but it is neither necessary nor sufficient for braid
legality.  A rank-`s` two-vertex seam window automatically supplies its
upper union at offset `s`; when `s>1`, it does not by itself supply an upper
target at offset one.
Its lower intersection occurs only in the maximal envelope.  The refined
physical word (1.12) may shrink it, so it can be credited to the lower ideal
only when it is included as a pin and passes Proposition 1.1.  Longer
seam-collar and multi-seam windows must be evaluated by their own actual
unions and ranks; Lemma 2.1 does not grade them.

### Lemma 2.2 (exact braid residence test)

Assume every coordinate run wholly inside one oriented piece has legal
length.  The concatenation is depth-`d^+` resident if and only if every
internal maximal run formed from a terminal piece-run, zero or more all-one
pieces, and an initial piece-run has total length at least `d^++1`.

#### Proof

Every final internal run is either wholly inside one piece or is uniquely a
concatenation of the displayed boundary runs.  Apply the coordinatewise
form of (1.6).  \(\square\)

In a natural first-shadow strand, an internal parent run of length `ell`
becomes a run of length `ell-1`.  An internal run with
`2<=ell<=d^++1` therefore creates a hazard interval supported on its native
collar.  That interval must be cut, rethreaded, or exposed at a port whose
boundary run merges to legal length.  Endpoint runs are governed by the
one-sided convention and are not automatic failures.  For an already
depth-`d^+` resident parent at unchanged deadline, the new hazards are
exactly its internal runs of length `d^++1`.

## 3. The exact Shadow--Braid induction theorem

Fix a Pascal child deck `D^+` and a decorated braid `Gamma` of that deck.
Let `T^+` be its final order, let `d^+=d(k^+)`, and let all old occurrence
families be recorded with full supports.

For bookkeeping, permit a partition of the lower ideal into two families:

\[
                         \mathcal L^-=\mathcal P^-\sqcup\mathcal R^-.
\tag{3.1}
\]

Targets in `P^-` are intended to use surviving natural shadow occurrences;
targets in `R^-` are carried by spill, endpoint, seam, or deeper compiler
cells.

### Theorem 3.1 (fixed-braid equivalence)

The braid `Gamma` supports a length-`B(k^+)` Shadow--Braid word if and only
if there exists a partition (3.1) and associated pin choices for which all
of the following hold.

**SB0: exact deck.**  `T^+` contains every child middle set exactly once.

**SB1: exact residence.**  `T^+` satisfies (1.6) at depth `d^+`;
equivalently its internal piece runs and every seam-composed run pass
Lemma 2.2.

**SB2: cut-aware upper support.**  For every child target `S` above the
middle rank,

\[
                         \beta_\Gamma^+(S)\ge0.
\tag{3.2}
\]

Occurrences are allowed at any window length giving the correct final rank.
For the two-vertex seam window, a non-Johnson seam is credited at the offset
dictated by Lemma 2.1; every longer collar window is credited only at its
directly audited union and rank.

**SB3: protected lower support.**  For every `S in P^-`,

\[
                         \beta_\Gamma^-(S)\ge0,
\tag{3.3}
\]

and one final occurrence--either a surviving old window or a new
seam-crossing window counted in `N_Gamma`--is selected as the physical pin
for `S`.
Specifically, a protected depth-`q` intersection

\[
 S=\bigcap_{h=0}^{q}T^+_{i+h},
 \qquad1\le q\le d^+,
\]

uses the maximal-envelope cell `(d^+-q,i+q)`; it is credited only when that
cell is pinned to `S` in the refined word.
Every target in `R^-`, including every deficit removed from the protected
family because its budget would be negative, is
assigned injectively to an actual lower row cell.  A seam intersection is a
lower resource only when its pin is included.  No physical cell may receive
two different labels.

**SB4: one common compiler.**  The lower pins from SB3, all central pins,
all seam pins, and all endpoint/boundary pins form one system `Pi^+`
satisfying (1.10)--(1.11).

When these conditions hold,

\[
                         \boxed{\nu(k^+)=B(k^+).}
\tag{3.4}
\]

#### Proof

SB4 and Proposition 1.1 give one nonzero physical word `A^+` with
`D^(d^+)A^+=T^+` and every lower target.  SB0 covers the middle layer.

By the exact window partition preceding Lemma 2.1, SB2 says precisely that
every upper target has a final consecutive-union occurrence in `T^+`.
Equation (1.14) lifts it to an interval of `A^+`.  Theorem 1.2 now proves
(3.4).

Conversely, suppose a flat-middle physical word exists for this decorated
braid.  Choose one actual lower witness for every target and place it in
`P^-` if it is one of the recorded surviving shadow occurrences, otherwise
in `R^-`.  Its actual pins satisfy Proposition 1.1.  Every upper witness is
a consecutive union of `T^+`, and the old/new window partition gives SB2.
Thus SB0--SB4 hold.  \(\square\)

This is the exact fixed-braid certificate theorem.  It is noncircular: every
hypothesis is a finite deck, run, occurrence-support, or coordinatewise pin
certificate.  It does not prove parent-class closure or assert that an
arbitrary parent package admits such a braid.

The hypotheses are fail-closed in the following precise sense.

* Omitting SB0 loses a middle target.
* SB1 is the exact braid-level obstruction to realizing the central pins.
  Logically it follows from a successful full SB4 and is listed separately
  so residence can be rejected before solving the compiler; a shortest
  formal statement may merge SB1 into SB4.
* An upper deficit in SB2 has no compiler escape.
* A protected lower deficit must be moved from `P^-` to the actual compiler
  family `R^-`; counting it as a surviving shadow is invalid.
* Sectorwise versions of SB4 do not imply one physical word.

### 3.2 Equivalent erosion-controller form of SB4

There is a sharper form when the final middle braid `T^+` is a Johnson path.
Put `R=ceil(k^+/2)`, `W=binom(k^+,R)`, `d=d^+`, and define the maximal
erosion controller

\[
 P_j=\bigcap_{i=\max(0,j-d)}^{\min(j,W-1)}T^+_i,
 \qquad 0\le j<W+d.
\tag{3.5}
\]

By erosion--Johnson duality, SB1 implies that every fully interior `P_j`
has rank `R-d` and consecutive interior states are Johnson-adjacent.  More
exactly,

\[
 |P_j|=
 \begin{cases}
 R-j,&0\le j<d,\\
 R-d,&d\le j\le W-1,\\
 R-(W+d-1-j),&W\le j<W+d.
 \end{cases}
\tag{3.5a}
\]

Thus “rank-`(R-d)` controller” always means its flat interior together with
the displayed one-sided collars.  If

\[
 T^+_{i+1}=T^+_i-\{\alpha_i\}+\{\beta_i\},
\]

then the exact port identities are

\[
 P_j\setminus P_{j+1}=\{\alpha_j\}
 \qquad(0\le j\le W-2),
\tag{3.6a}
\]

and

\[
 P_j\setminus P_{j-1}=\{\beta_{j-d-1}\}
 \qquad(d+1\le j\le W+d-1).
\tag{3.6b}
\]

Both apply simultaneously for `d+1<=j<=W-2`.

Let `Pi_0` be the lower, seam, and endpoint pins in SB3--SB4, with the
central pins removed.  For each coordinate `x`, choose a set `H_x` of
positions on the `x`-runs of `P`, and put

\[
                         A_j=\{x:j\in H_x\}.
\tag{3.7}
\]

### Theorem 3.2 (exact controller-pinning criterion)

For a fixed Johnson braid satisfying SB0--SB1, SB4 holds if and only if
there are sets \(H_x\subseteq\{j:x\in P_j\}\) satisfying all three
conditions below.

**CP1: exact carrier coverage.**  For every coordinate `x`,

\[
 \{i:x\in T^+_i\}
 =\bigcup_{j\in H_x}
   \bigl([j-d,j]\cap[0,W-1]\bigr).
\tag{3.8}
\]

Equivalently, on every internal maximal `x`-run `[u,v]` of `P`, both
`u,v` are forced into `H_x` and consecutive selected positions have gap at
most `d+1`.  The boundary cases are exactly the one-sided version of
(3.8).  On a run meeting only the left boundary, the last controller
endpoint is forced, the first selected position is at most `d`, and all
selected gaps are at most `d+1`.  On a run meeting only the right boundary,
the first controller endpoint is forced, the last selected position is at
least `W-1`, and the same gap bound holds.  A spanning run forces neither
controller endpoint; it requires first selected position at most `d`, last
selected position at least `W-1`, and every gap at most `d+1`.  Under SB0 a
spanning coordinate run cannot occur.

**CP2: all extra pins.**  For every `(c,S_c) in Pi_0`,

\[
 \begin{array}{ll}
 H_x\cap I_c=\varnothing,&x\notin S_c,\\
 H_x\cap I_c\ne\varnothing,&x\in S_c.
 \end{array}
\tag{3.9}
\]

**CP3: physical nonzeroness.**  For every source position `j`, some
coordinate satisfies \(j\in H_x\).

Under these conditions (3.7) is the common compiler.  In particular,
(3.6a)--(3.6b) force the applicable incoming and outgoing controller
coordinates into `A_j`; the only remaining central freedom consists of
extra pins placed inside long controller runs with gaps at most `d+1`.

#### Proof

The containment \(A_j\subseteq P_j\) is forced by the central cells.  A pin
at physical position `j` covers precisely the carrier indices
\([j-d,j]\cap[0,W-1]\), so (3.8) is equivalent coordinate by coordinate to
`D^dA=T^+`.  The internal endpoint-and-gap description is the interval
covering form of this equality; (3.6a)--(3.6b) give its forced ports.  Conditions
(3.9) say exactly that the union of `A` over every extra pin interval is its
assigned label.  CP3 makes every letter nonzero.  Thus CP1--CP3 imply SB4.
Conversely, take \(H_x=\{j:x\in A_j\}\) from any SB4 compiler.  The same
three coordinatewise observations give CP1--CP3.  \(\square\)

The existential pin choice has a deterministic maximal form.  Define

\[
 \widehat H_x=
 \{j:x\in P_j\}\setminus
 \bigcup_{\substack{(c,S_c)\in\Pi_0\\x\notin S_c}} I_c.
\tag{3.10}
\]

A feasible family \(H_x\) exists if and only if the maximal family
\(\widehat H_x\) satisfies the coverage equality (3.8), hits every positive
pin,

\[
                 \widehat H_x\cap I_c\ne\varnothing
                 \qquad(x\in S_c),
\tag{3.11}
\]

and leaves every physical position in at least one \(\widehat H_x\).  Indeed,
every feasible \(H_x\) is contained in \(\widehat H_x\).  Conversely, adding an
allowed controller position cannot create an unwanted carrier occurrence:
\(x\in P_j\) already implies that `x` belongs to every \(T_i^+\) whose
central window contains `j`.  Coverage, positive hits, and nonzeroness are
therefore monotone under enlargement.  Thus the maximal word

\[
                         \widehat A_j=\{x:j\in\widehat H_x\}
\tag{3.12}
\]

is the canonical controller compiler whenever one exists.  A natural
maximal-erosion pin introduces no new negative deletion, but it still needs
the positive-hit test (3.11) after all other pins have been imposed.

The upper and protected lower shadow towers can also be read directly on
the controller.  For `0<=q<=d` and `0<=i<=W-1-q`,

\[
 \bigcap_{h=0}^{q}T^+_{i+h}
 =\bigcup_{j=i+q}^{i+d}P_j
 =(D^{d-q}P)_{i+q},
\tag{3.12a}
\]

while for `q>=0` and `0<=i<=W-1-q`,

\[
 \bigcup_{h=0}^{q}T^+_{i+h}
 =\bigcup_{j=i}^{i+d+q}P_j.
\tag{3.12b}
\]

Thus SB2 is exactly the completeness of the appropriate longer consecutive
controller unions.  Formula (3.12a) explains why a natural lower pin is
negative-inert: every controller state in its physical cell is already a
subset of the target.  Its positive coordinates can nevertheless be erased
by other pins, which is why (3.11) remains necessary.

Indeed, (3.12b) follows by expanding
\(T_i^+=\bigcup_{j=i}^{i+d}P_j\).  For (3.12a), inspect one coordinate run:
it covers all carrier positions `i,...,i+q` exactly when its eroded run
meets the controller interval `i+q,...,i+d`.  The same statement, with the
one-sided truncation, holds at either endpoint.

### Lemma 3.3 (global controller-incidence cut)

Assume `d>=1` and that `T^+` is depth-`d` resident.  For a coordinate `x`,
let

\[
 t_x=\#\{i:x\in T_i^+\},\qquad
 p_x=\#\{j:x\in P_j\},
\]

let `i_x` be the number of internal maximal `x`-runs in the linear carrier
`T^+`, and put

\[
 b_x=\mathbf 1_{\{x\in\bigcap_{i=0}^{W-1}T_i^+\}}.
\]

Then the general linear identity is

\[
                 \boxed{p_x=t_x-d i_x+d b_x.}
\tag{3.13}
\]

Under SB0, `b_x=0` and every coordinate has

\[
 p_x=t_x-d i_x,
 \qquad
 t_x={k^+-1\choose R-1},
 \qquad
 \boxed{p_x\equiv {k^+-1\choose R-1}\pmod d}.
\tag{3.14}
\]

#### Proof

Residence ensures that every internal carrier run `[a,b]` has length at
least `d+1`; it becomes the controller run `[a+d,b]` and
loses exactly `d` incidences.  A run meeting exactly one linear boundary
retains its incidence count because the erosion window is clipped there.  A
single run meeting both boundaries is the spanning run, and its controller
version gains the `d` endpoint-collar incidences.  This proves (3.13).  SB0
rules out the spanning run because the exact middle deck contains sets both
with and without `x`; its exact middle-layer degree then gives (3.14).
\(\square\)

This is a braid condition, not a pin condition.  When controller pieces are
spliced directly, every coordinate total must land in the residue class
(3.14), in addition to every local collar having the right rank.  A proposed
controller which fails this cut cannot be the erosion of an exact middle
deck, regardless of how the extra physical pins are chosen.  If `P` is
recomputed from an already exact resident `T^+`, the identity is of course
automatic; its force is as an early consistency test in controller-first
assembly.  The run-count proof itself does not use Johnson adjacency, so
(3.13)--(3.14) remain necessary for a resident non-Johnson seam-relaxed
braid even when `P` is no longer a constant-rank Johnson controller.

Theorem 3.2 permits a strict Johnson braid to be specified one level lower:
give its rank-`(R-d)` interior controller with its one-sided collars, verify
that it agrees with the maximal erosion (3.5), that its consecutive
`(d+1)`-window unions give the exact middle permutation `T^+`, and solve
only the coordinate pins.  This does **not** extend to a
non-Johnson seam-relaxed braid: its maximal erosion can change rank and need
not be a Johnson controller, so Theorem 3.1 and Proposition 1.1 remain the
authoritative general form.

### 3.3 What a Pascal sector braid preserves

The controller is inherited only on sector interiors.  If a final seam lies
between middle positions `a` and `a+1`, then precisely the controller
vertices

\[
                         P_{a+1},\ldots,P_{a+d}
\tag{3.15}
\]

have erosion windows crossing that seam; near a linear endpoint, some lie
in the one-sided collars of (3.5a).  Thus a seam creates `d` mixed
controller vertices and `d+1` incident controller transitions.  Reversal
does not remove this collar, and collars of nearby seams must be audited as
their union rather than counted independently.

For an isolated oriented seam with a full flat collar
`d<=a<=W-d-2`, write

\[
 \ldots,L_{-1},L_0\mid R_0,R_1,\ldots,
\]

The same `d` mixed states, listed in the opposite order if necessary, are

\[
 C_h=\left(\bigcap_{s=0}^{h-1}L_{-s}\right)
     \cap
     \left(\bigcap_{t=0}^{d-h}R_t\right),
 \qquad 1\le h\le d.
\tag{3.16}
\]

In the final index order,

\[
                         C_h=P_{a+d+1-h}.
\tag{3.17}
\]

Assume each piece is Johnson, every coordinate run wholly inside a piece is
already depth-`d` legal, the two inherited outer controller states are
legal, and the carrier seam \(L_0\mid R_0\) is Johnson.  Every `C_h` must
have rank `R-d`, and every
transition from the inherited left controller through the `C_h` sequence to
the inherited right controller must be a nontrivial Johnson step.  The rank
condition alone is insufficient: it does not exclude a repeated controller
state, as Example 3.4 shows.  Together, the rank and transition conditions
are necessary and sufficient for the seam-run test in Lemma 2.2: a new
short run makes the corresponding affected controller edge repeat or change
rank, and the converse follows by reading that failure back as a short run.
For short pieces or overlapping collars, (3.16) must be replaced by every
actual crossing `(d+1)`-vertex intersection and its incident transitions.
For a seam within `d` positions of a linear endpoint, use the collar ranks
in (3.5a) and the direct one-sided run test; unequal-rank endpoint-collar
transitions are not Johnson edges.

Consequently, a Pascal braid preserves a global controller exactly only if:

1. each uncut sector interior supplies the required depth flag in its actual
   orientation;
2. every carrier seam is Johnson; at a full flat collar every actual mixed
   state in (3.15) has rank `R-d` and every incident controller transition
   is a nontrivial Johnson step, while an endpoint collar passes (3.5a) and
   the direct one-sided run test;
3. the stitched controller agrees with the maximal erosion (3.5), and its
   `(d+1)`-window unions reproduce the prescribed middle deck; and
4. every coordinate count passes the global identity (3.13), hence the
   residue cut (3.14); and
5. the forced ports and extra pins solve CP1--CP3 after all sectors and
   collars are combined.

These are finite seam-collar and run-pinning tests.  Merely concatenating
the parent controllers or their sectorwise physical words does not imply
them: a seam can merge two coordinate runs, split one run and create new
forced endpoints, or place a forced port inside the forbidden interval of a
lower pin.

### Example 3.4 (smallest local controller-collar obstruction)

The failure already occurs at deadline `d=1` and middle rank two (the local
`k^+=4` odd-to-even deck, where `W=6`, `Lambda=4`, and `d(4)=1`).  Let an
`A` piece end with

\[
             T_{a-1}=\{1,2\},\qquad T_a=\{2,3\},
\]

and let the following `B` piece begin with

\[
                         T_{a+1}=\{2,z\}.
\]

Both displayed middle transitions are Johnson.  Within the separate `A`
piece, coordinate `3` is a legal one-sided endpoint run.  After joining the
pieces it is an internal run of length one, so depth-one residence fails.
Equivalently, the two controller states incident with the seam are

\[
 T_{a-1}\cap T_a=\{2\}
 \qquad\text{and}\qquad
 T_a\cap T_{a+1}=\{2\},
\]

so the purported rank-one controller repeats a vertex rather than making a
Johnson step.  No smaller collar example exists: `d=0` has no mixed erosion
state, while at `d=1` three consecutive middle vertices are the minimum
needed to turn a piece endpoint into an internal run.  This is a local
no-go for **direct** controller preservation, not an obstruction to choosing
a different seam in the full Pascal deck.

### Corollary 3.5 (compressed strict Shadow--Braid equivalence)

A fixed decorated Pascal braid whose final middle transitions are Johnson
supports a length-`B(k^+)` word if and only if the following data exist.

1. Its middle order is the exact child deck.
2. Its controller agrees with the maximal erosion (3.5), has the ranks
   (3.5a), satisfies the one-sided endpoint run conditions, and every consecutive
   flat-interior transition is a nontrivial Johnson step (including through
   every seam collar), and it reconstructs the middle order by consecutive
   `(d+1)`-unions.  For a controller assembled before `T^+`,
   (3.13)--(3.14) are mandatory global consistency cuts.
3. Every upper target passes the cut-aware budget SB2, equivalently the
   corresponding longer controller union in (3.12b) survives or is newly
   created.
4. The lower targets admit the injective physical-cell partition and pin
   assignment of SB3.
5. For those pins, the maximal allowed run sets \(\widehat H_x\) pass carrier
   coverage, all positive hits, and nonzeroness.

#### Proof

Item 2 is SB1 in controller form.  In the reverse direction, an internal
carrier run of length at most `d` makes the erosion transition at its exit
either have the wrong rank or repeat/fail a Johnson step, so the displayed
controller conditions exclude every residence violation.  Items 1, 3, and
4 are SB0, SB2, and SB3.  By Theorem 3.2 and its maximal closure
(3.10)--(3.12), item 5 is exactly SB4.  Theorem 3.1 proves both directions.
\(\square\)

This is the shortest nonduplicative fixed-braid statement in the strict
Johnson class.  The incidence identity is automatic when `P` is recomputed
from an exact resident `T^+`; it becomes an independent rejection test only
in the controller-first Pascal assembly.  No analogous compression removes
the cut-aware upper ledger or the common lower-pin quantifier.

## 4. Odd-to-even Pascal specialization

Let the parent ground set have size `2r-1`, and adjoin `z`.  The even child
middle rank is `r`.  Let `P_A` enumerate the parent rank-`r` layer.  Let
`P_B` be a possibly different parent chronology and let `Q_B` be its
completed first-shadow ordering, enumerating the parent rank-`r-1` layer.
The exact child deck is

\[
 \boxed{
 \binom{[2r-1]\cup\{z\}}r
 =\{P_A(i)\}_i\ \sqcup\
   \{\{z\}\cup Q_B(j)\}_j.}
\tag{4.1}
\]

The two sources may be different parent packages.  On uncut interiors,

\[
\begin{array}{c|cc}
\text{shore}&\text{lower intersection of }q+1\text{ vertices}
            &\text{upper union of }q+1\text{ vertices}\\ \hline
A&L_{P_A}^{(q)}&U_{P_A}^{(q)}\\
B&\{z\}+L_{Q_B}^{(q)}&\{z\}+U_{Q_B}^{(q)}.
\end{array}
\tag{4.2}
\]

At the child deadline `d^+`, Theorem 3.2 restricts on the same interiors to

\[
 \begin{array}{c|c}
 A&(P^+|A)_j=(L_{P_A}^{(d^+)})_j\\
 B&(P^+|B)_j=\{z\}\cup(L_{Q_B}^{(d^+)})_j.
 \end{array}
\tag{4.2a}
\]

For the displayed forward completion, away from its collar the indexed
identity is

\[
 (L_{Q_B}^{(q)})_j=(L_{P_B}^{(q+1)})_{j-1}\qquad(j\ge1),
\tag{4.3a}
\]

with the corresponding shifted identity after reversal.  Thus the `B`
lower shore consumes one more parent lower level and loses one residence
unit.  Completion, orientation, and endpoint collars must be audited
directly.

Hence the `A` controller interior is transported only if the parent stores
depth `d^+`, while the `B` controller interior requires depth `d^++1` in
`P_B`.  Neither statement fills the `d^+` mixed controller vertices around
each `A/B` seam.  Those collars, and the global CP1--CP3 pin sets, remain
fresh child data.

Every mixed `A/B` window contains an `A` vertex without `z` and a `B`
vertex with `z`.  Consequently

\[
 \text{mixed intersection omits }z,
 \qquad
 \text{mixed union contains }z.
\tag{4.3}
\]

Hence mixed seams provide no replacement for:

* a protected `z`-containing lower `B` target; or
* a no-`z` upper `A` target.

The former may still be moved into the common lower compiler.  The latter
has no such escape and must have nonnegative upper budget.

### Corollary 4.1 (exact odd-to-even Shadow--Braid lift)

Choose any segmentation, orientation, and braid of the deck (4.1).  It
proves `nu(2r)=B(2r)` exactly when SB0--SB4 hold at the even deadline.

In particular, no fixed number of pieces and no Johnson-only condition is
part of the exact fixed-braid criterion.  The successful six-piece construction is one
finite realization: its two `B`-ear cuts create two unique upper losses and
its two `A` cuts expose their repair endpoints.  A different braid is legal
if and only if it passes the same budgets, residence, and compiler.

The structural residence obstruction is immediate.  If an uncut parent
one-run has length `d(2r)+1`, its first-shadow image has length `d(2r)` and
violates SB1.  Thus, when the deadline does not drop, the chosen `B` cuts
must form a transversal of all such eroded-run hazard intervals.  Parent
optimality alone supplies no such transversal.

## 5. Same-parity diamond specialization

Let the parent have size `2r-1` and adjoin `x,y`.  Suppose
`P` enumerates rank `r`, `Q=widehat L_P^(1)` enumerates rank `r-1`, and the
support of `U_P^(1)` covers every rank-`r+1` parent set.  Choose one
occurrence of each such upper value, with its actual index and order, to form
`U_*`.  The child middle deck is

\[
\boxed{
 \binom{[2r+1]}{r+1}
 = (\{x,y\}+Q)
 \sqcup(\{x\}+P)
 \sqcup(\{y\}+P)
 \sqcup U_* .}
\tag{5.1}
\]

Call the four sectors `A,X,Y,U`.  On uncut native interiors their direct
flag values are

\[
\begin{array}{c|cc}
\text{sector}&\text{lower }(q+1)\text{-window}
             &\text{upper }(q+1)\text{-window}\\ \hline
A&\{x,y\}+L_Q^{(q)}&\{x,y\}+U_Q^{(q)}\\
X&\{x\}+L_P^{(q)}&\{x\}+U_P^{(q)}\\
Y&\{y\}+L_P^{(q)}&\{y\}+U_P^{(q)}\\
U&L_{U_*}^{(q)}&U_{U_*}^{(q)}.
\end{array}
\tag{5.2}
\]

The corresponding depth-`d^+` controller restrictions are

\[
\begin{array}{c|c}
A&\{x,y\}\cup L_Q^{(d^+)}\\
X&\{x\}\cup L_P^{(d^+)}\\
Y&\{y\}\cup L_P^{(d^+)}\\
U&L_{U_*}^{(d^+)}.
\end{array}
\tag{5.2a}
\]

On the uncompleted chronological `A` interior, the exact relation is
`(L_Q^(q))_j=(L_P^(q+1))_(j-1)` for the forward completion and is shifted
accordingly under reversal.  No analogous inheritance is valid for an
arbitrary thinned `U_*`: its deeper flags depend on the actual selected
index sequence.

Thus the `A` controller consumes parent depth `d^++1`, the `X/Y`
controllers consume depth `d^+`, and the `U` controller is not transported
from the parent at all.  Even when these four interiors have the right rank,
the mixed collars (3.15) and the common run-pinning problem CP1--CP3 are not
sectorwise consequences.

For the native cyclic sector order `U,Y,A,X`, the adjacent seam signatures
are

\[
\begin{array}{c|cccc}
\text{seam}&UY&YA&AX&XU\\ \hline
\text{intersection tags}&\varnothing&\{y\}&\{x\}&\varnothing\\
\text{union tags}&\{y\}&\{x,y\}&\{x,y\}&\{x\}.
\end{array}
\tag{5.3}
\]

Therefore ordinary cross-sector seams cannot replace:

* a both-new lower `A` occurrence; or
* an empty-signature upper `U` occurrence.

The first target family may use SB4 if compatible lower cells exist.  The
second is chronology-only and must survive the `U` selector and cuts.

### 5.1 Exact native protected systems

In the Catalan `A` forest, retaining one native edge of each required
first-lower colour makes every retained edge the unique internal occurrence
of its colour.  The deletion set is a base of the first-shadow partition
matroid.  Thus it has no further **internally protected** cut extension;
additional `A` cuts must be paid for by SB4 or by same-signature rethreading.

For `U`, let `I_Z` be the native occurrence-index fibre of immediate upper
value `Z`.  A one-representative selector deletes `|I_Z|-1` indices in each
fibre.  Before later braid cuts or rethreading, a deeper empty-signature
upper target survives the selector through a native provider exactly when
the provider's required consecutive `U`-index interval avoids those
deletions.  Later seam replacements are separate entries in
`N_Gamma^+`.  Old upper multiplicity without interval supports proves
nothing.

### Corollary 5.1 (exact diamond Shadow--Braid lift)

Choose an occurrence-labelled `U_*`, a segmentation, and a braid of (5.1).
It proves `nu(2r+1)=B(2r+1)` exactly when SB0--SB4 hold at the new deadline.

The Pascal identities prove only SB0 before ordering.  They do not imply
SB1, the protected budgets in SB2--SB3, or the common physical compiler SB4.
This is the exact sense in which the diamond recursion is conditional rather
than an unconditional induction.

## 6. The first fully audited cut-aware obstruction in the current catalogue

Use `scratch/sigma_sat_k11_allcentral_cap2.certificate.json`, with audited
SHA-256
`a23b8d6847dba4350cca8dc8b9da89519e77067e58c866422713115887aaf397`.
If `middle_cycle` is its stored cyclic rank-six carrier, root it by

\[
 T_i=(\mathtt{middle\_cycle})_{i+2\pmod{462}}.
\tag{6.0}
\]

Put

\[
 \widehat C_0=T_{461}\cap T_0,
 \qquad
 \widehat C_{i+1}=T_i\cap T_{i+1}\quad(0\le i\le460).
\tag{6.0a}
\]

This exact rooted carrier gives the first fully audited failure in the
current catalogue of the strict native first-priority `k -> k+2` rule.  All
array and interval indices in this section are zero-based.

### Theorem 6.1 (strict native `U` braid: load four, budget minus one)

Freeze the inherited-edge `U` braid: deleting an unselected `U` index
breaks its native run, and no new same-signature `UU` edge is inserted
between separated retained runs.

For the first-occurrence `U` selector, let

\[
 Z=\{1,2,4,5,6,8,9,11\}.
\tag{6.1}
\]

The complete list of old `T` intervals with union `Z` is

\[
 [13,16],\quad[14,16],\quad[321,323],\quad[393,395].
\tag{6.2}
\]

Their selected-index patterns are respectively

\[
             (1,0,1),\quad(0,1),\quad(0,1),\quad(0,1).
\tag{6.3}
\]

Thus no inherited provider lies wholly inside a retained native `U` run.
Every cross-sector window contains `x` or `y`, so it cannot have union `Z`;
and the frozen braid has no new `UU` seam.  Consequently, for this strict
braid,

\[
 \text{raw load}(Z)=4,
 \qquad
 \beta_\Gamma^+(Z)=0+0-1=-1.
\tag{6.4}
\]

The strict first-priority native braid violates SB2 and no endpoint or lower
compiler can repair it.

#### Proof

The interval list (6.2) is exhaustive among inherited native-index
providers in the frozen carrier.  Each pattern in (6.3) crosses a deleted
index, so no provider is wholly inside a retained native `U` run.  The
cross-sector signature assertion follows from (5.3), while the frozen
no-rethreading convention gives `N_Gamma^+(Z)=0`.  Upper witnesses depend
only on consecutive unions of `T^+`, by (1.14), and are unaffected by the
choice of lower word below `T^+`.  \(\square\)

The scope is essential.  The first pattern `(1,0,1)` retains
\(V_{13},V_{15}\), and direct union gives \(V_{13}\cup V_{15}=Z\).  A
newly inserted same-signature \(V_{13}\mid V_{15}\) Johnson seam therefore
repairs this particular
upper target.  Such a seam must be entered in `N_Gamma^+(Z)` and then pass
the residence, lower-pin, and global compiler tests; Theorem 6.1 does not
exclude it.

The strict last-occurrence inherited-edge selector likewise fails: the target

\[
 Z'=\{2,3,4,5,6,7,8,11\}
\]

has exhaustive inherited providers `[1,3],[105,107],[105,108]` with
patterns `(0,1),(1,0),(1,0,1)`.  Here
\(V_{105}\cup V_{107}=Z'\), so the same
`UU`-rethreading caveat applies.  These facts refute the two canonical
priority rules without nonnative `UU` edges, not every adaptive selector or
braid.

### 6.2 Independent residence failure

For the first-occurrence `A` selector, the completed-spine vertices

\[
 \widehat C_{253},\widehat C_{254},\widehat C_{255},
 \widehat C_{256},\widehat C_{257}
\]

have coordinate-one pattern

\[
                         0,1,1,1,0.
\tag{6.5}
\]

All four intervening colour representatives are retained, so the selected
`A` strand has an internal run of length three.  Since `d(13)=3`, SB1
requires length at least four.  At the certificate's stored alternative
root, an analogous coordinate-two run at indices `233,...,237` has four
singleton edge colours; hence **every** native exact-colour selector at that
root retains the bad run.  Changing the root or adding off-spine edges is
outside this obstruction.

### 6.3 The strict first-`A` selector also fails the common compiler

Assume that every both-new first-lower colour is retained at exactly one
native `AA` gap and that no extra `AA` rethreading is allowed.  The strict
first-`A` selector misses the seven old triples

\[
\begin{gathered}
 a=\{1,7,8\},\quad b=\{1,6,9\},\quad c=\{3,9,10\},\\
 d=\{1,5,11\},\quad e=\{2,8,11\},\quad
 f=\{3,8,11\},\quad g=\{8,9,11\}.
\end{gathered}
\tag{6.6}
\]

In the strict native forest, any linear compiler repair forces these seven
triples into the two old rank-five endpoint cores.  Indeed, a direct boundary
placement is endpoint-contained.  If a missing triple is instead placed in
an interior `D^2` cell, that cell shrinks the unique retained both-new
rank-five `AA` colour containing it.  The displaced colour has no second
interior native occurrence and, by assumption, no rethreaded `AA`
occurrence; hence that colour must be boundary-supported.  The missing
triple is again contained in one endpoint core.  No two rank-five cores can
contain all seven triples.

Indeed, put `c` in a red core.  Each of `a,d,e` is disjoint from `c`, so all
three must be blue.
Since `b` is disjoint from `e`, it is red, and

\[
                         b\cup c=\{1,3,6,9,10\}
\]

fills the red five-set.  Hence `g` is blue; since `b` is disjoint from `f`,
`f` is blue.  But

\[
 a\cup d\cup e\cup f\cup g
 =\{1,2,3,5,7,8,9,11\}
\]

has size eight.  This contradicts a rank-five blue endpoint core.  Thus the
strict first-`A` braid violates SB4 even though its crude scalar boundary
count has slack.

This obstruction is architecture-specific: extra `AA` rethreading, repeated
selected colours, or a different global selector may change the charge.
The independently constructed exact `k=13` factor lies outside the failed
native priority braid.

## 7. Odd-to-even calibration and seam minimality

Odd-to-even does not contain the same native `U`-priority obstruction.
Exact six-piece braids close `11 -> 12` and `13 -> 14`.  The latter
nevertheless shows why seam repair must be target-specific.

In the frozen `k=14` alternating schema, isolate the three-vertex `B` ear
`B[966..968]` by cuts after `B[965]` and `B[968]`.  This destroys the two
unique first-upper targets

\[
 15204=8192\mathbin{\mathrm{OR}}7012,
 \qquad
 10702=8192\mathbin{\mathrm{OR}}2510.
\tag{7.1}
\]

An `A/B` seam restoring the mask `8192 OR S` must expose the rank-seven `A`
endpoint `S`.  The two required endpoints occur at

\[
                         A[419]=2510,
 \qquad
                         A[1445]=7012.
\tag{7.2}
\]

Their incident cut sets `{418,419}` and `{1444,1445}` are disjoint, so one
`A` cut cannot restore both.  The certified cuts after `418,1445`, together
with the two `B` cuts, yield six pieces, and the seams

\[
                         15200\longrightarrow7012,
 \qquad
                         2510\longrightarrow8654
\tag{7.3}
\]

restore the two upper targets.  The exact residence, all-depth upper, and
common compiler audits then pass.

Thus, after freezing both shores, this `B` ear, and the audited
`B-A-B-A-B` predecessor family, two `A` cuts are necessary.  This is not a
global three-cut or nonalternating no-go.  It proves the relevant principle:
a seam count or total excess is not a repair certificate; each lost
protected target needs an actual compatible port.

The smaller strict `7 -> 8` and `9 -> 10` intersection templates fail for a
different reason: the deadline does not drop, and first-shadow erosion
creates many internal residence failures.  Those finite audits do not rule
out every possible braid, but they instantiate the hazard-transversal
condition following Lemma 2.2.

### 7.1 The isolated atlas-UNIT cone at `k=15`

Now freeze the authoritative Hall-29 `k=15` chronology

\[
 T_0,\ldots,T_{W-1}\in{[15]\choose8},
 \qquad W=6435,
\]

and its depth-three erosion controller

\[
 P_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i.
\tag{7.4}
\]

Let `U_atlas` be the 1,602 UNIT pairs `(p,x)` extracted from the
singleton-positive-defect records in the retained Hall residual atlas.  This
is an atlas-defined family, not the set of all raw unique-omission pairs in
the chronology.  The unique pair `(0,4)` lies outside the flat rank-five
controller model.  The unrestricted raw UNIT replacement graph is not
acyclic, so none of the potential conclusions below may be exported beyond
`U_atlas`.

For a flat atlas pair, an **isolated UNIT edit** changes one controller state
only:

\[
                         P'_p=P_p-\{y\}+\{x\}.
\tag{7.5}
\]

It is locally legal when the two incident controller edges remain Johnson,
all four affected controller-window unions have rank eight, and all affected
middle edges remain Johnson.  By the UNIT condition, exactly one of the four
old middle states containing `P_p` omits `x`; call its index `q`.
These are deliberately necessary local tests only: they do not certify that
the edited controller is the new maximal erosion, or that the residence,
common compiler, lower pins, and upper shadows survive.

### Lemma 7.1 (one-state deck derivative)

Every locally legal edit (7.5) changes precisely one middle value,

\[
                         T_q\longmapsto T_{q'},
                         \qquad q'\ne q,
\tag{7.6}
\]

and fixes the other three affected middle states.

#### Proof

Adding `x` changes only the unique union that omitted it.  In that union,
rank eight forces `y` to disappear; in each of the other three, losing `y`
would lower the rank to seven.  Thus exactly one union changes.  Since the
old middle chronology is the exact rank-eight deck, its new rank-eight value
is `T_(q')` for a unique `q'`, and nontriviality gives `q'!=q`.
\(\square\)

The exhaustive census in
`MATH_K15_UNIT_PIN_ISOLATED_CONTROLLER_CYCLE_NOGO_20260728.md` is

\[
\begin{array}{c|r}
\text{atlas UNIT pairs}&1602\\
\text{boundary pair outside the model}&1\\
\text{flat pairs with one locally legal deletion}&1318\\
\text{flat pairs with no locally legal deletion}&283\\
\text{replacement arcs }q\to q'&1318\\
\text{incident deck indices}&2295.
\end{array}
\tag{7.7}
\]

Every admissible pair has exactly one admissible deletion.  The directed
graph `G_iso` formed by the 1,318 arcs on its 2,295 incident vertices is
acyclic; Kahn elimination removes all 2,295 vertices.

### Theorem 7.2 (independent atlas collars cannot close the deck)

There is no nonempty family of locally legal isolated edits (7.5), drawn
from `U_atlas`, whose linear controller positions satisfy

\[
                         |p-p'|\ge8
\tag{7.8}
\]

and whose simultaneous application preserves the exact middle-deck
multiset.

#### Proof

At separation eight, the affected controller states, four-window blocks,
middle-edge tests, and depth-three physical collars are independent.  The
source intervals `[p-3,p]` are disjoint, so the changed source indices `q`
are distinct.  Exact deck preservation requires the target multiset
`{q'}` to equal the source set `{q}`.  Hence every selected source has one
selected predecessor and successor, and the chosen arcs contain a directed
cycle.  This contradicts acyclicity of `G_iso`.  \(\square\)

A stronger algebraic certificate underlying the theorem is obtained as
follows.  Let `e_q` be the standard basis of `Z^W` and assign an arc the
deck-displacement vector

\[
                         \delta_{q,q'}=e_{q'}-e_q.
\tag{7.9}
\]

A topological ordering of `G_iso` gives an integer height `h` on its
incident vertices; extend it arbitrarily to the other deck indices.  Then

\[
                         \langle h,\delta_{q,q'}\rangle>0
\tag{7.10}
\]

on every isolated atlas arc.  Thus the nonnegative isolated-edit cone lies
strictly on one side of the deck-conservation lattice `delta=0`; its only
balanced element is zero.  This height separation is the acyclicity
certificate used in Theorem 7.2; it is stronger than the theorem's scoped
claim about physically realizable pairwise `8`-separated families.

There is a sharper test for edits which are individually among these 1,318
arcs but are applied jointly.  Put

\[
 \Phi_i(P')=\bigcup_{j=i}^{i+3}P'_j
\]

and, whenever every `Phi_i(P')` has rank eight, define its total deck
displacement by writing `iota(S)` for the unique index with
`S=T_(iota(S))` and setting

\[
\Delta(P')=
 \sum_{i=0}^{W-1}\bigl(e_{\iota(\Phi_i(P'))}-e_i\bigr).
\]

Then `Delta(P')=0` if and only if the reconstructed values form the exact
middle deck as a multiset.

For a nonempty family `F` of individually admissible atlas edits at
pairwise-distinct controller positions, define `P^F` by applying the unique
prescribed replacement at each selected position and leaving every other
controller state fixed.  Let

\[
 \Omega(F)=\Delta(P^F)-\sum_{e\in F}\delta_e
\tag{7.10a}
\]

be the exact interaction correction.  If `P^F` preserves the deck, then

\[
 \Omega(F)=-\sum_{e\in F}\delta_e,
 \qquad
 \langle h,\Omega(F)\rangle<0.
\tag{7.10b}
\]

If no four-controller window contains the support positions of two selected
edit operations, then every middle union changes independently and
`Omega(F)=0`; exact deck preservation
is impossible even if larger adjacency or physical collars overlap.  Thus a
useful compound family of individually admissible one-state edits must place
at least two edited positions in one four-controller window and create
genuinely negative `h`-interaction.  Jointly legal edits which are
individually inadmissible, and direct multi-state moves, lie outside this
derivative formula and remain open.  In particular, choosing two different
certified operations at the same controller position is not a family `F` in
this definition; it requires one jointly specified replacement state.

Only 14 of the 24 pins in the displayed optimistic Hall-29 witness admit an
isolated edit.  The witness itself contains positions as close as distance
two, so `14/24` is a separate local-admissibility fact, not an application of
the separation theorem.  It rules out reading the witness as 24 individually
legal collars, but not an interacting realization.  Its 24 forced source
indices `q(p,x)` are distinct, so any same-position realization of that
fixed witness changes at least 24 indexed middle states; an exact repaired
deck would therefore induce a permutation with support at least 24.  The ten
nonadmissible pins require compound interaction or a move outside the
isolated atlas model.

### 7.2 The closed interacting deck-circuit gate

For simultaneous edits, isolated derivatives cannot simply be added when
their four-window collars overlap.  Join two edited controller positions in
the conservative **physical interaction graph** whenever their linear
distance is less than eight.  For the distinct-position family `F` of
certified one-coordinate edits, actual nonlinear deck interaction requires
a shared four-controller window, as (7.10a)--(7.10b) show.  A jointly
specified multi-coordinate replacement at one controller position is also
nonlinear, but lies outside that derivative formula.

For a connected edit cluster `C`, recompute all affected middle states
jointly.  If they have rank eight, write

\[
 T_i^C=T_{\tau_C(i)}
\]

and define its exact deck displacement

\[
 \Delta(C)=
 \sum_{i\in A(C)}\bigl(e_{\tau_C(i)}-e_i\bigr),
\tag{7.11}
\]

where `A(C)` is the set of middle indices actually changed by the cluster.
For mutually separated clusters, the final middle multiset is the original
deck if and only if

\[
                         \sum_C\Delta(C)=0.
\tag{7.12}
\]

When (7.12) holds, the map `i -> tau_C(i)` over all changed indices is a
permutation and decomposes into closed directed cycles.  If every component
were a singleton isolated atlas edit, (7.10) would make the left side of
(7.12) have positive `h`-weight.  Therefore any successful construction in
this restricted atlas-UNIT lane must contain at least one **nonisolated
component**, meaning a component which is not a singleton certified
one-coordinate `G_iso` edit.  This includes overlapping one-state edits, a
joint multi-coordinate replacement at one position, or a direct
multi-controller-state move.  Moves outside the atlas, non-UNIT moves,
chronology reordering, and a new carrier are separate escapes and are not
excluded.

More sharply, every cycle of the changed-label permutation contains at
least one effective transition outside `G_iso`; otherwise it would be a
directed cycle in the acyclic graph.  If such a permutation cycle contains
an isolated atlas arc, the sum of its `h`-increments is zero, so at least one
of its nonisolated transitions has negative `h`-increment.  This is the
cyclewise form of the same obstruction.

Fix, for example, the zero extension of `h` off the 2,295 incident
vertices.  Taking the `h`-inner product in (7.12) gives

\[
                         \sum_C\langle h,\Delta(C)\rangle=0.
\tag{7.12a}
\]

Every singleton isolated atlas component contributes strictly positively by
(7.10).  Hence every nontrivial closed solution must contain a nonisolated
component with `h`-drift at most zero.  This is an exact first screening cut
for the multi-state circuit catalogue; it is not a claim that every such
nonpositive component can be physically lifted.

This gives the precise next search object for continuing the retained Hall
service plan.  A **closed interacting deck-circuit system** is a nonempty
family of clusters which does not decompose entirely into singleton
certified `G_iso` edits and which passes all of the following ledgers
simultaneously.  It may use auxiliary UNIT or non-UNIT controller changes;
those are not ruled out by Theorem 7.2.  A primitive system may consist of
one zero-displacement cluster, but separate nonisolated clusters are also
allowed to cancel through (7.12).

1. The jointly edited controller is a legal path, equals the maximal erosion
   of the reconstructed middle chronology, and passes every overlapping
   residence collar.
2. Every reconstructed middle value has rank eight, the middle edges are
   Johnson, and the deck displacement is exactly zero as in (7.12).
3. For every coordinate, the controller-incidence change obeys

   \[
                         \Delta p_x=-3\,\Delta i_x,
   \tag{7.13}
   \]

   hence `Delta p_x` is divisible by three.
4. Every designated UNIT demand `(p,x)` first satisfies `x in P'_p`.
   Together with all fixed, reserved, old, seam, and endpoint pins and all
   injective lower-cell assignments, these demands form the full retained
   pin system `Pi_0`, which must pass the one common maximal compiler of
   Theorem 3.2.
5. Its changed chronology retains all cut-aware upper occurrences required
   by SB2.

No such nontrivial circuit system is constructed here.  The theorem removes
only the separated isolated one-coordinate edit lane inside the retained
1,602-pair atlas.  Compound circuits are the remaining route **within that
Hall service plan**; auxiliary UNIT moves, non-UNIT moves, chronology
changes, and new carriers remain open.

## 8. Exact induction statement and surviving gate

### Theorem 8.1 (Shadow--Braid induction)

Suppose a finite set of base dimensions has Shadow--Braid certificates, and
suppose that for every subsequent odd dimension:

1. a decorated diamond braid satisfies SB0--SB4 and produces the next odd
   certificate; and
2. a decorated odd-to-even braid satisfies SB0--SB4 and produces the
   intervening even certificate.

Then

\[
                         \nu(k)=B(k)
\]

in every dimension reached by the induction.

#### Proof

Apply Theorem 3.1 to each braid.  The diamond step propagates the odd
lineage, and the odd-to-even step supplies the adjacent even dimension.
Induction completes the proof.  \(\square\)

This theorem is logically exact but its braid-existence hypothesis is not
presently proved.  Bare equality in the parent dimension is insufficient:
an optimal word need not expose a flat resident middle carrier at all.  Even
a parent Shadow--Braid certificate supplies only the Pascal deck identities
(4.1) or (5.1), not a simultaneous child braid.

Failure of direct extraction from an arbitrary optimal witness occurs
already at `k=4`: the optimal word
`(10,9,5,1,2,4,8)` has length `B(4)=7`, but its first candidate central
union is `10 OR 9=11`, of rank three rather than the middle rank two.  Thus
this optimal witness is not itself a Shadow--Braid base.  This observation
does not claim that `k=4` has no other flat optimum; it only blocks the
unsupported step “take any optimal parent word and lift its middle row.”

The sharp remaining system for this Shadow--Braid route is

\[
\boxed{
 \begin{array}{c}
 C_A\text{ hits every eroded-run residence hazard}\\[1mm]
 C_A\text{ lies in the cut-aware protected-occurrence system}\\[1mm]
 \text{for each empty-signature upper target, an old provider survives}\\
 \quad\text{or a directly audited same-signature witness replaces it}\\[1mm]
 \text{all ports and mixed controller collars pass their exact tests}\\[1mm]
 \text{when }d\ge1,\ \text{every controller coordinate passes (3.13), hence (3.14)}\\[1mm]
 \text{all lower deficits share one compiler satisfying (1.10)--(1.11).}
 \end{array}}
\tag{8.1}
\]

For odd-to-even, delete the empty-signature `U` line and use the two-shore
signature constraints (4.3).  For the diamond lift, ordinary cross-sector
seams cannot help either extreme protected family in (8.1).

In the strict Johnson subroute, the final line of (8.1) is equivalently the
single global controller-pinning system CP1--CP3.  The controller view does
not make the condition sectorwise: every seam still contributes the mixed
collar (3.15).

For the frozen Hall-29 `k=15` atlas, Theorem 7.2 removes the option of
satisfying this gate with a nonempty bank of pairwise `8`-separated isolated
UNIT collars.  Any continuation of this Hall service plan must instead
include a nonisolated closed deck-circuit system of the form
(7.11)--(7.13), possibly with auxiliary or non-UNIT changes, or abandon the
plan/carrier.  This is a restriction of the search space, not a `k=15`
impossibility theorem.  For the displayed 24-pin witness,
the circuit support is at least 24 and ten designated pins require compound
or outside-atlas handling.

Equation (8.1) replaces raw scalar load by cut-aware occurrence survival;
the two conditions are incomparable.  A single uncut occurrence may pass
(8.1), while raw load four can fail when every inherited occurrence is
hit, as in Theorem 6.1.  Aggregate Hall and separate sector compilers still
do not imply its common-word condition.  The system relaxes Johnson-only or
perfect-rainbow shadow requirements: lower holes may use the physical
compiler and non-Johnson seams may be credited at their true rank offsets.
Those relaxations coexist with orthogonal residence and compiler
requirements, so no global logical comparison with a rainbow condition is
claimed.

The remaining mathematical choice within this Shadow--Braid route is now
precise.  One must either prove
that (8.1) always has a solution in a suitably strengthened parent class,
or construct an adaptive/off-spine braid which regenerates the protected
occurrence and compiler interfaces.  The strict inherited-edge native
first-priority recursion is already refuted by Theorem 6.1; arbitrary
same-signature rethreading is not.

## 9. Source audit

The statements used here are drawn from:

* `MATH_PASCAL_FLAG_PACKAGE_AND_CATALAN_LIQUIDITY_20260728.md`;
* `MATH_ODD_EVEN_SIX_PIECE_LIFT_20260728.md`;
* `MATH_ATTACK_H_KPLUS2_DIAMOND_CATALAN_SEAM_RELAXED_INDUCTION_20260728.md`;
* `MATH_ATTACK_H_KPLUS2_LABELLED_ROUTING_PHASE_AND_NATURAL_SELECTOR_COUNTEREXAMPLE_20260728.md`;
* `MATH_LANE_E_FLAT_DEADLINE_COMPILER_EQUIVALENCE_AND_INDUCTION_GATE_20260728.md`;
* `MATH_EROSION_JOHNSON_CONTROLLER_DUALITY_20260728.md`;
* `MATH_INTERSECTION_TABLEAU_AND_NESTED_OWNER_TARGET_20260728.md`;
* `MATH_K13_EXACT_1719_CERTIFICATE_20260728.md`;
* `MATH_K14_EXACT_3434_CERTIFICATE_20260728.md`;
* `MATH_K15_UNIT_PIN_ISOLATED_CONTROLLER_CYCLE_NOGO_20260728.md`;
* `scratch/sigma_sat_k11_allcentral_cap2.certificate.json`;
* `scratch/sigma_sat_k11_allcentral_verify.json`;
* `scratch/audit_k15_unit_pin_isolated_cycle_nogo.py`;
* `THREAD_D_CUT_SPECIFIC_SAFE_COMPLEX_AND_LINK_ZERO_OBSTRUCTION_20260728.md`.
