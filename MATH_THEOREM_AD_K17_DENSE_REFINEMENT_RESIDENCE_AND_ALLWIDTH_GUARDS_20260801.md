# K17 dense refinement: canonical contraction, exact residence cuts, and all-width upper guards

Date: 2026-08-01  
Lane: AD  
Status: exact structural theorem and authenticated finite-scope audit.  This
note does **not** assert that the live q1 CEGAR is SAT, construct a K17 word,
or solve the lower compiler.

## 0. Outcome and exact scope

The protected immediate-palette factor is

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

It has seven components, exact owner/lower-q1/upper-q1 palettes, and the
authenticated defects

```text
positive run length 2: 3073
positive run length 3: 2710
upper holes rank 11/12/13: 1502/295/9
upper holes rank 14--17: 0.
```

The current zero-singleton refinement bank is

```text
scratch/k17_dense_refinement_zerozero_bank_20260801.tsv
SHA256 5b4fe2d1a0125ea25f6fbb4b9259a6d2ee2007cd4ba55ac0aa4a6f23aa6bad8f
```

It adds 3,805 cuts to the deterministic 3,807-piece resident segmentation,
giving 7,612 pieces.  The fixed zero/zero bank is q1-UNSAT on the verified
bow-tie core.  Later banks in the cut CEGAR are also only q1 candidates.
There is no selected chronology to which residence or the higher-shadow
conclusions could presently be attached.

The main conclusions are these.

1. An extra cut made **inside an already resident coarse piece** is a pure
   factorization.  If its old factor edge is selected between the two child
   sockets, it contracts literally and changes neither chronology,
   residence nor any interval-OR witness.
2. Only extra cuts whose canonical child edge is not selected are active.
   One active split can expose at most 81 formerly internal upper masks over
   all ranks, and at most `(q+1)^2` at rank `9+q`.
3. Exact residence after ordering is a finite transition-monoid condition.
   At depth three every incumbent bad run yields a sound lazy no-good of
   width at most four.
4. Exact all-width upper coverage is an accumulated-union monoid condition.
   A compressed total/prefix/suffix/internal signature gives a contextual
   replacement theorem, while a witness-avoidance row gives an exact
   order-free guard for old internal witnesses.
5. Q1 feasibility alone implies none of this.  The authenticated factor is
   already an exact q1 counterexample, and the two protected bow-tie C8s
   separately exhibit nonzero upper current and a literal length-three run.

Thus a future q1-SAT bank can be accepted safely by the finite residence and
upper CEGAR below.  There is no theorem that an arbitrary q1-SAT bank must
pass it.

## 1. The exact accumulated-union monoid

Let `P=(P_1,...,P_n)` be a nonempty word of subsets of `[k]`.  Define

\[
\begin{aligned}
 T(P)&=\bigcup_{i=1}^n P_i,\\
 \mathcal P(P)&=\left\{\bigcup_{i=1}^jP_i:1\le j\le n\right\},\\
 \mathcal S(P)&=\left\{\bigcup_{i=j}^nP_i:1\le j\le n\right\},\\
 \mathcal D(P)&=\left\{\bigcup_{i=a}^bP_i:1\le a\le b\le n\right\}.
\end{aligned}                                                     \tag{1.1}
\]

These are sets, not occurrence multisets.  This is the correct object for
coverage.  Write

\[
             \Sigma(P)=(T(P),\mathcal P(P),\mathcal S(P),\mathcal D(P)).
                                                                    \tag{1.2}
\]

### Theorem 1.1 (exact product law)

For two nonempty words `P,Q`,

\[
\begin{aligned}
T(PQ)&=T(P)\cup T(Q),\\
\mathcal P(PQ)&=\mathcal P(P)\cup
 \{T(P)\cup A:A\in\mathcal P(Q)\},\\
\mathcal S(PQ)&=\mathcal S(Q)\cup
 \{A\cup T(Q):A\in\mathcal S(P)\},\\
\mathcal D(PQ)&=\mathcal D(P)\cup\mathcal D(Q)\cup
 \{A\cup B:A\in\mathcal S(P),\ B\in\mathcal P(Q)\}.
                                                               \tag{1.3}
\end{aligned}
\]

Consequently (1.3) defines an associative product on signatures and
\(\Sigma(PQ)=\Sigma(P)\odot\Sigma(Q)\).

#### Proof

A prefix of `PQ` either ends in `P`, or consists of all of `P` followed by a
prefix of `Q`.  The suffix statement is dual.  A contiguous interval is
inside `P`, inside `Q`, or is a suffix of `P` followed by a prefix of `Q`.
These cases are exhaustive and give (1.3).  Associativity follows because
both bracketings equal the signature of the same concatenated word.  QED

If every letter has rank nine in a 17-set, each prefix or suffix chain has
at most nine distinct masks: its cardinality starts at nine and can increase
at most eight times.  Therefore the cross-deck in the last line of (1.3)
has size at most

\[
                              9^2=81.                    \tag{1.4}
\]

At rank `9+q`, there is at most one member of a nested chain of each size
`9,...,9+q`; hence the rank-`9+q` part has size at most

\[
                             (q+1)^2.                    \tag{1.5}
\]

Both are worst-case upper bounds; collisions only reduce them.

## 2. Exact residence transition monoid

Fix depth `d`.  For one coordinate use the state set

\[
             Q_d=\{0,1,\ldots,d,\mathsf L,\bot\}.        \tag{2.1}
\]

State zero means that no positive run is open, state `j` means that the
current positive run has length `j`, `L` means length at least `d+1`, and
`bottom` means that a bounded run of forbidden length has already closed.
Reading a one sends

\[
0\mapsto1,\quad j\mapsto j+1\ (j<d),\quad
d\mapsto\mathsf L,\quad\mathsf L\mapsto\mathsf L,        \tag{2.2}
\]

and reading a zero sends `0,L` to zero and every `1,...,d` to `bottom`.
The bottom state is absorbing.

For a word `P`, let `R_x(P):Q_d->Q_d` be the transition map induced by the
binary trace of coordinate `x`, and put

\[
                         R(P)=(R_x(P))_{x\in[k]}.          \tag{2.3}
\]

### Theorem 2.1 (exact product and acceptance)

For every `P,Q`,

\[
                    R_x(PQ)=R_x(Q)\circ R_x(P).           \tag{2.4}
\]

With a specified left collar, a linear word has no forbidden run exactly
when the transition from the collar's incoming state avoids `bottom`; a
short final positive run remains open for the right collar.  If both ends
are declared boundary-clipped, discard the maximal initial positive prefix,
start in state zero at the first zero, and allow the final open state.  This
is exactly the absence of an internal factor `0 1^j 0`, `1<=j<=d`.
An all-one trace has no first zero and is explicitly accepted in this
both-clipped convention.

For a cyclic word, an all-one coordinate is accepted.  Otherwise choose one
actual zero, begin immediately after it in state zero, scan one complete
lap, and append that chosen closing zero.  The cycle is resident exactly
when this scan avoids `bottom` for every coordinate.  Equivalently, its
cyclic transition has a fixed state other than `bottom`.

#### Proof

Equation (2.4) is ordinary composition of deterministic word transitions.
A transition to `bottom` occurs exactly when a zero closes an open positive
run of length in `1,...,d`.  Starting from an explicit collar state gives
the first claim.  When both linear ends are clipped, removing the maximal
positive prefix ensures that only runs bounded by two actual zeros are
tested, while the final open run is deliberately not closed.  In the cyclic
case a zero gives a canonical break at which the open run state is zero,
and the appended closing zero tests the final cyclic run.  The only case
with no zero is the allowed all-one trace.  QED

This formulation is exact even through arbitrarily many all-one pieces.  A
pairwise endpoint-age test which forgets the transported state is not an
exact substitute.

### Corollary 2.2 (bounded residence no-good)

Assume every fixed join has first been contracted into a piece and every
resulting fixed piece is internally depth-`d` resident.  In a selected piece
chronology, let

\[
                            0\,1^j\,0,qquad1\le j\le d,  \tag{2.5}
\]

be a literal bad coordinate run.  Let `E` be the selected seam variables
among the `j+1` adjacencies of this substring.  Then

\[
                         \sum_{e\in E}y_e\le |E|-1        \tag{2.6}
\]

is a valid incumbent-violated lazy cut, and

\[
                              |E|\le d+1.                 \tag{2.7}
\]

At K17, `d=3`, so every such row has width at most four.

Here each `y_e` is an occurrence-specific directed atom fixing both physical
sockets and the intervening oriented piece traces.  If a master exposes only
quotient, colour, or unoriented-edge atoms, (2.6) must also contain the
orientation and piece-activation literals which fix the displayed physical
substring.  In a variable-cut master it is guarded by the current cut/piece
activation assumptions.

#### Proof

The run is not internal to one fixed piece.  If all selected seams appearing
among its `j+1` literal adjacencies remain selected, every adjacency in
(2.5)—the others being fixed internal edges—remains, and the same bad run
survives.  Hence at least one listed seam must change.  There are at most
`j+1<=d+1` of them.  QED

If a bad run lies wholly inside one fixed piece, there is no seam cut: the
piece bank itself must be split or rethreaded.

## 3. Pure refinement and canonical contraction

Let `C_0` be a bank of already internally resident coarse pieces.  Split
some coarse pieces further at a set `F` of old internal factor gaps.  For
`g in F`, call the old factor adjacency between its two new child sockets
the **canonical edge** `e_g`.

The adjective “already resident” is essential.  It does not apply to the
original 3,807 residence cuts: restoring one of those old adjacencies may
restore the very short run which forced the cut.

### Theorem 3.1 (canonical-contraction normal form)

Let `M` be any selected socket matching on the refined bank.  If `e_g` is
selected, its two child sockets are unavailable to every other seam, and
the two oriented child words concatenate to the original coarse word or its
reversal.  Contracting `e_g` therefore preserves:

* the literal owner chronology and component topology;
* the exact residence transition product `R`;
* the complete all-width signature `Sigma`;
* the lower and immediate-upper label on every other adjacency; and
* every chronology-functorial source/compiler certificate not naming the
  split as an indivisible protected atom.

Contract all such edges.  The exact active refinement support is

\[
                       A(M)=\{g\in F:e_g\notin M\}.       \tag{3.1}
\]

Every residence or upper-deck effect of the extra refinement factors through
the chronology on this contracted active quotient.

#### Proof

The selected canonical edge has degree one at each new socket, so no other
selected seam can meet either socket.  Traversing one child, the old factor
edge and the other child yields exactly the old coarse owner sequence in one
of its two orientations.  Equations (1.3) and (2.4) show that both signatures
are the products of the child signatures and hence equal the old signature.
The other statements depend only on the unchanged literal chronology.
Contractions at different selected canonical edges commute.  QED

### Corollary 3.2 (exact cross-deck charge)

For an active split `P=L R`, the old internal witnesses not internal to one
child are exactly

\[
       X_g=\{A\cup B:A\in\mathcal S(L),\ B\in\mathcal P(R)\}.  \tag{3.2}
\]

Thus at most `81|A(M)|` distinct upper-mask liabilities are exposed by the
extra active splits, before overlaps and gains are accounted for.  At rank
`9+q` the corresponding bound is `(q+1)^2|A(M)|`.

These are liability bounds, not claims that the masks become holes: a new
seam or another old occurrence may redeliver them.

## 4. The exact cut hit/avoid invariant

Work on one old factor component.  For an upper target `U`, let `W(U)` be
the family of all old literal witness intervals with union `U`.  For a cut
set `C`, write `int(I)` for the old gaps strictly internal to interval `I`.

### Theorem 4.1 (internal-deck cut criterion)

After cutting at `C`, target `U` occurs in the union of the internal decks
of the resulting pieces if and only if

\[
                \exists I\in W(U)\quad int(I)\cap C=\varnothing. \tag{4.1}
\]

Consequently, if (4.1) holds for every required upper target, every
permutation and reversal of the pieces retains the complete upper deck
internally.  For rank seventeen it suffices instead that the final chronology
is one spanning path/cycle, since its total owner union is `[17]`.

#### Proof

An old interval remains internal to one cut piece exactly when no selected
cut lies among its internal gaps.  This proves both directions of (4.1).
Internal intervals survive every permutation and reversal.  The last claim
uses the whole spanning chronology as the rank-seventeen interval.  QED

Together with the exact residence requirement “hit at least one of the
`j+1` collar gaps of every old run `1^j`, `j<=d`”, (4.1) is an exact
**hit/avoid bi-transversal**:

* hit every short-run collar;
* avoid all gaps of at least one witness interval for every guarded target.

With variables `c_g` for cuts and `w_I` for guarded witnesses, its direct
linearization is

\[
 w_I\le1-c_g\quad(g\in int(I)),\qquad
 \sum_{I\in W(U)}w_I\ge1.                               \tag{4.2}
\]

Let `C_0` be the fixed coarse residence-cut bank.  For witness families
defined on the original factor, the exact refined guard is

\[
              int(I)\cap\bigl(C_0\cup A(M)\bigr)=\varnothing. \tag{4.2a}
\]

Equivalently, first restrict `W(U)` to witnesses already internal to one
coarse `C_0`-piece; only then may `c_g` in (4.2) be replaced by the active
extra-split indicator `1_{e_g\notin M}`.  Omitting `C_0` would incorrectly
revive a witness crossing an original residence cut.  These rows guarantee
preservation of old witnesses; they are not necessary for coverage because
new seams can create new ones.

### Theorem 4.2 (retained-witness residual for an arbitrary rethread)

Let `F` be an old rank-nine owner 2-factor and let `F'` be any final graph of
maximum degree two on the same owners.  Put

\[
                          A=E(F)\setminus E(F').          \tag{4.3}
\]

Thus a cut old edge which is canonically restored is not active.  Let
`W_F(U)` be all cyclic `F`-intervals with union `U`, and define

\[
 Z_F(A)=\{U:\text{every }I\in W_F(U)\text{ contains an edge of }A\}.
                                                                  \tag{4.4}
\]

The universal quantifier is vacuous when `W_F(U)` is empty, so intrinsic
old holes belong to `Z_F(A)`.  Every target outside `Z_F(A)` occurs as a
literal interval of `F'`.

#### Proof

Choose an old witness interval `I` containing no active edge.  Every internal
old edge of `I` is retained in `F'`.  These edges form a path.  Since `F'`
has maximum degree two, no internal owner of that path can leave it; hence
the same owner segment occurs consecutively in `F'`, possibly reversed.
Its union is still `U`.  QED

This is exact for the **old-witness channel**: `Z_F(A)` is precisely the set
not certified by retained old intervals.  New seams may still cover its
members.

### Corollary 4.3 (81-Lipschitz residual bound)

For the authenticated protected factor, over ranks 11--17,

\[
                         |Z_F(A)|\le1806+81|A|,           \tag{4.5}
\]

where `1806=1502+295+9` is the intrinsic old hole count.  Layer by layer the
corresponding bounds are

\[
\begin{array}{c|rrrrrr}
\text{rank}&11&12&13&14&15&16\\ \hline
|Z_F(A)|\text{ bound}&1502+9|A|&295+16|A|&9+25|A|&36|A|&49|A|&64|A|.
\end{array}                                                     \tag{4.6}
\]

Each row is capped, of course, by the size of its Boolean layer.  Rank
seventeen is automatic once `F'` is one spanning chronology.

#### Proof

For each nonintrinsic `U` in `Z_F(A)`, choose one old witness and then one
active edge of that witness.  The target belongs to the suffix-prefix
cross-deck (3.2) of the chosen edge.  Take a union bound and apply (1.4) or
(1.5).  QED

An exact Benders form uses a variable `z_U` meaning “send `U` to the new
accumulated-union channel”.  For every inclusion-minimal edge hitting set
`H` of `W_F(U)`, impose

\[
                         z_U\ \vee\ \bigvee_{e\in H}r_e,  \tag{4.7}
\]

where the exact linkage is

\[
                       r_e=1\quad\Longleftrightarrow\quad e\in E(F'). \tag{4.8}
\]

If `W_F(U)` is empty, the empty hitting set forces `z_U=1`.  With (4.8), if
`z_U=0`, all rows (4.7) are equivalent to the existence of one wholly
retained old witness.  Only targets with `z_U=1` need the more expensive
new-witness DFA/portal channel.

## 5. Context-transparent noncanonical repair

The hit/avoid condition is deliberately order-free and can be too strong.
The following packet theorem is the exact local alternative.

### Theorem 5.1 (compressed contextual upper dominance)

Let an old fragment `P` be replaced by `Q`.  Suppose

\[
\begin{aligned}
T(Q)&=T(P),\\
\mathcal P(Q)&\supseteq\mathcal P(P),\\
\mathcal S(Q)&\supseteq\mathcal S(P),\\
\mathcal D(Q)&\supseteq\mathcal D(P).                  \tag{5.1}
\end{aligned}
\]

Then for arbitrary exterior words `L,R`,

\[
                         \mathcal D(LQR)\supseteq
                         \mathcal D(LPR).                \tag{5.2}
\]

#### Proof

An old interval is wholly exterior, internal to `P`, enters `P` from the
left and ends there, starts in `P` and exits right, or crosses all of `P`.
These cases use respectively no packet datum, `D(P)`, `P(P)`, `S(P)`, or
`T(P)`.  The four rows of (5.1) supply a new interval with the same union in
every case.  QED

Pointwise equality of first/last arrival times is unnecessary.  Inclusion
of the compressed prefix and suffix OR decks is enough.

### Theorem 5.2 (residence-and-upper transparent repair)

In addition to (5.1), suppose

\[
                             R(Q)=R(P).                  \tag{5.3}

\]

Suppose also that the replacement has the declared boundary owners and its
internal/seam q1 resource ledger is accepted by the global q1 selector.
Then replacing `P` by `Q` in any context preserves every old upper witness
and preserves the positive owner-run depth-`d` DFA in both directions.  Any
family of pairwise-disjoint replacements satisfying these hypotheses
composes.  This statement alone does not preserve signed/source `D^3`
residence, clipped source collars, or compiler state; those require their
own typed components in the packet signature.

#### Proof

Upper preservation is Theorem 5.1.  Equality (5.3), followed and preceded
by the same exterior transition products, gives the same final state for
every coordinate and every incoming age state.  Hence residence acceptance
is identical in every context.  Apply the one-fragment statement
successively to disjoint fragments.  QED

For a fixed context, equality in (5.3) may be weakened to acceptance of the
actual product.  The equality is the reusable packet condition.

## 6. Proof-producing post-q1 CEGAR

The preceding theorems give a complete finite integration which does not
duplicate the live q1 solve.

1. Obtain a q1-SAT seam selection on a fixed cut bank.
2. Contract every selected canonical extra-cut edge by Theorem 3.1.
3. Materialize the selected oriented component words.  Reject any internally
   nonresident fixed piece upstream.
4. Run the exact residence product.  Each bad run emits (2.6), of width at
   most four at K17.
5. Run the accumulated-union/first-arrival oracle on each cyclic component
   or on the selected opened path.  For a missing target `U`, restrict the
   current chronology to owners contained in `U`.  Its connected components
   all have proper union.  Any future solution on the same fixed pieces
   which covers `U` must select a catalogue seam whose two physical endpoint
   owners both lie in `U` and belong to two distinct such components.  Its
   immediate upper label need not equal `U`.  Therefore the disjunction of
   all such currently false occurrence-labelled seam atoms is a valid lazy
   portal clause on that fixed piece bank.  In a joint cut-choice master,
   prepend the negations of the complete current cut/piece activation
   assumptions.  For a selected opening, also prepend the negation of the
   unique root atom if one atom fixes it, or the disjunction of negations of
   the complete opening assignment otherwise.
6. Repeat until an incumbent passes, or until a proof-producing q1/chronology
   master proves the exact fixed-bank face UNSAT.

The portal clause in step 5 is exact as a necessary cut: without a new
cross-component adjacency, every future induced component is contained in
one old proper-union component.  It is not a promise that one chosen portal
alone suffices; degree, colour, topology and residence remain in the master.

This finite loop is complete because the fixed seam/root catalogue has only
finitely many assignments and every rejected incumbent is excluded.  It is
not a polynomial-time or existence theorem.

For a literal depth-three source antecedent, the identity

\[
       \bigcup_{i=a}^{b}T_i=\bigcup_{j=a}^{b+3}E_j       \tag{6.1}
\]

makes the owner accumulated-union oracle exact for nonwrapping strict-upper
witnesses after the opening is fixed.  Short source intervals, lower pins,
suffix corrections and the terminal common-cap compiler remain separate.

## 7. Authenticated K17 quantitative boundary

The exact deterministic 3,807-cut resident segmentation has internal-path
hole vector, at ranks 10 through 17,

\[
              (2423,3116,1297,249,12,0,0,0).             \tag{7.1}
\]

This is authenticated in

```text
scratch/k17_3807_endpoint_master_20260801/
  k17_3807_endpoint_master_v2.audit.json
SHA256 92f135639e5549236cbf43781f2b7277b21ce9b232fdde0bc7ab2e8295e803e9
```

Relative to the uncut protected factor, residence cutting exposes an
additional

\[
                  1614, 1002, 240, 12                 \tag{7.2}
\]

holes at ranks 11,12,13,14, respectively.  The full higher internal debt of
the resident coarse pieces is

\[
                  3116+1297+249+12=4674.                \tag{7.3}
\]

Ranks 15--17 already have internal witnesses and can be protected by the
avoidance rows (4.2).  The 1,502/295/9 intrinsic rank-11/12/13 holes and all
other targets not guarded internally require seam-created or packet-created
witnesses.

The complete protected C6 audit gives an independent warning that rank-ten
safety does not imply deeper safety.  Among the 405 component-merging,
q1-safe C6s, one move can create up to

\[
                         3, 3, 1                       \tag{7.4}

\]

new holes at ranks 11,12,13.  This is read directly from

```text
scratch/k17_protected_c6_local_calculus_20260801.tsv
SHA256 f2c948de733a5286f4d21c3ba3cd2507831e2b061ca59f7fe82ace5c11b55d67
```

and the authenticated replay summary is

```text
scratch/audit_k17_protected_c6_local_calculus_20260801.out
SHA256 7efac1586e378b271e3a433d958494e98c0a28b4e792b9fdc9c15238661b0535
```

The independent full reconstruction gives the same `3/3/1` maxima:

```text
scratch/threadD_k17_q3_fusion_independent_replay_20260801/audit.json
SHA256 1cc0ad6aaa69315c294551c3de33476581534c5d59d441167b0ce0abc0a59997
```

For the zero/zero bow tie, the only protected two-colour role-changing C8
has an exact bounded coordinate-3 run of length three.  The only resident
alternative changes named upper current by

\[
                         +[116862]-[117086].              \tag{7.5}

\]

The exact two-key audit is

```text
scratch/threadD_k17_zerozero_bowtie_q4_20260801/two_keys.audit.tsv
SHA256 b8e55eb3a6fb9a25243d347ad13553c1d5022fcc0ba5177bc63deb251c4264b5
```

These are literal counterexamples to importing a q1-only cut or circuit
without the state carried in Sections 1--2.

There is a simple but overly strong order-free residence alternative: for
every allowed seam, require every ending/starting positive run to be long,
and every continuing suffix-plus-prefix run to have length at least `d+1`,
using the actual piece length rather than `infinity` for an all-one trace.
Then every ordering is resident.  The authenticated zero/zero replay shows
why this cannot replace the transition product here:

```text
conservative seam triples                         9488
zero deleted-lower colours                        5065
zero tail pieces / zero head pieces          5346 / 5346
piece TC / CH projection rank                2240 / 2240
common-orientation zero pieces                     6011
```

The same bank has no zero in any of those rows under the exact relaxed
two-block predicate.  Thus conservative pruning destroys most of the live
q1 supply, whereas the width-four lazy run cuts retain it.  The current
literal replay is

```text
scratch/k17_dense_refinement_zerozero_literal_audit_20260801.out
SHA256 2a5966273d09664752457a007ab1fc4a6625ee5006f7487ac17f9dbfcfa7f2e1
```

## 8. Sharp remaining boundary

Proved:

* pure extra refinement is exactly contractible when its canonical edge is
  selected;
* the active support and its complete old cross-deck liability are explicit;
* residence has width-at-most-four proof-producing incumbent cuts at K17;
* old higher witnesses have an exact cut hit/avoid invariant;
* noncanonical packets have an exact context-transparent sufficient test;
* arbitrary fixed-bank q1 solutions can be checked and separated by a finite
  exact residence/higher-shadow CEGAR.

Not proved:

* that any live dense q1 bank is SAT;
* that a q1-SAT bank admits an accepting residence/higher ordering;
* a bounded active-support theorem for the iterated bow-tie CEGAR;
* creation of all 4,674 coarse-piece higher witnesses;
* one-component opening/voltage, lower pins, source suffixes, or the terminal
  common-cap compiler.

The mathematically correct next integration is therefore to leave the live
q1 solver untouched, replay its first SAT incumbent through the canonical
contraction, add only the width-at-most-four run cuts and missing-target
portal cuts, and retain explicit witness guards for ranks already complete.
