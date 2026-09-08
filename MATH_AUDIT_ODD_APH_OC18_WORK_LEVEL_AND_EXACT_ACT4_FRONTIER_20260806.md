# Work-level audit of odd APH after OC18: the exact ACT4 frontier

**Date:** 2026-08-06  
**Primary file audited:**
`MATH_THEOREM_ODD_APH_OC18_ORIGIN_APERTURE_AND_MOBILE_CART_REDUCTION_20260806.md`  
**Audited SHA-256:**
`42f3215b10a181d4b365e9be684573fb09e9c9d8604686aacdcad35f9c70b0ea`  
**Directed-lift audit:**
`MATH_AUDIT_ODD_APH_OC18_FIXED_ROW_DIRECTED_LIFT_20260806.md`  
**Method:** literal word matching, theorem-interface audit, and bounded
capacity-two layer arguments; no computation or search  
**Verdict:** **NO-GO for the APH consequence in Section 7 of the primary
file.**  The fixed-row directed lift is valid, and the two-block layer
counts and endpoint reachability are valid.  The work-level origin decoder
and the four-task gather/scatter path bank are not proved.  In fact, the
displayed raw-pair code has a no-op branch on which the old adaptive-origin
collision survives literally.  The proof-safe frontier therefore remains
the anchored-catalyst four-task staging lemma `ACT4` from
`MATH_REDUCTION_ODD_APH_ANCHORED_CATALYST_FOUR_TASK_STAGING_20260806.md`.

This audit does not prove that APH is false.  It isolates the exact bounded
path-bank statement which would repair the OC18 route, and it gives a
three-position single-head endpoint code which removes the no-op capacity
problem without search.

## 1. Dependency status before the work-level audit

The following rows may be cited.

1. After reserving `p_1` and the two fixed collar blocks, a work word of
   length at least eight and imbalance at most three contains an ordinary
   zero-charge atom.
2. The protected four-state register writes the atom type and separates the
   private-gap phase from the raw phase before the atom is changed.
3. One atom head may remain stationary while the other crosses a raw interval.
4. A recorded literal temporary cart crosses the already proved protected
   islands `H`, `H|M`, and `M|H`; a separated temporary/permanent berth
   schedule is also available.
5. The `ACT4` reduction proves the scalar equation, the bound of four tasks,
   staging capacity, bounded collar connectivity, and collar-order
   copy-before-erase.  Conditional on its occurrence-labelled gather/scatter
   row, it implies APH for odd `k >= 45`.
6. Every literal OC18 work edge has the fixed-`p_1` directed lift.  The
   directed-lift audit explicitly does not audit origin-aperture selection or
   the work-level occurrence decoder.

Thus the question left by the dependency chain is not whether the OC18
microedges are directed.  It is whether their projected work paths form a
source-disjoint path bank and whether that bank remembers every adaptive
origin used later.

## 2. The displayed OC18 code has a literal no-op class

For the raw aperture `S=B|B`, table (3.3) in the primary file is

\[
                    2020\longrightarrow2011\longrightarrow2002.
\tag{2.1}
\]

The three displayed vertices are proposed as the three collar-order
codewords.  One of them is

\[
                             2020=B|B=S.             \tag{2.2}
\]

Hence one collar-order class writes no origin marker at all.  The statement
that the physical position of the code carries the adaptive atom address is
then false on that class: the alleged code is just an unchanged raw subword.

### Proposition 2.1 (the padded `ACB/BAC` collision survives)

Let the two length-fourteen balanced work words be

\[
                 w_1=A C B^{12},
          \qquad w_2=B A C B^{11}.                  \tag{2.3}
\]

In each word choose the displayed adjacent `A|C` as the ordinary atom and
choose the two `B` blocks in physical positions four and five as the
aperture.  Tensor both words with the same protected first row, the same
source collar in the order class assigned to (2.2), and the same exterior
records.

Both atoms have the same early state `Q_3`: they are `AB^0C` atoms already
in the raw-transport phase.  The code path for (2.2) is empty.  Their atom
bootstraps are

\[
                    w_1\longrightarrow HH B^{12},
       \qquad       w_2\longrightarrow B HH B^{11}. \tag{2.4}
\]

Move the first cart one raw block to the right.  Its macro endpoint is

\[
                         B HH B^{11},                \tag{2.5}
\]

which is exactly the second bootstrap checkpoint.  The aperture at physical
positions four and five is `B|B` in both copies of (2.5), and all protected
records agree.  Thus the two full states, not merely their work projections,
are equal.

#### Proof

Equations (2.4)--(2.5) are the literal source-internal bootstrap and one
double-head block interchange.  The selected apertures are disjoint from
both atom supports and remain unchanged.  Equality of the displayed work
words and of every tensored record gives equality of the full states.
\(\square\)

This proposition audits the displayed code choice, not every possible
replacement code.  A deterministic atom/aperture selector which is intended
to exclude (2.3), or a different three-code family avoiding (2.2), must be
stated and proved.  Neither occurs in the primary file.

The same issue is present in the other raw rows: each three-vertex row in
(3.2)--(3.4) contains its raw source as one of the three proposed codewords.

## 3. Connectivity does not give the missing source-indexed code bank

The primary file correctly proves that

\[
                       V_4-\{0202\}
\]

is connected.  It then assigns the `M`-containing aperture modes "any three
simple paths" in the corresponding connected layer.  This proves individual
reachability only.

Suppose two different aperture sources `S,S'` have the same mass, the same
early atom state, and the same collar-order class.  Their source collars and
registers are then identical.  If the two chosen simple aperture paths meet,
the unchanged exterior does not distinguish them: the aperture is precisely
the datum being erased.  Consequently the full paths meet as well.  The
required finite assertion is a source-indexed path bank whose paths are
disjoint for every fixed literal outside record, not merely connectivity of
the layer.

The raw tables partially address this point: their different source rows are
disjoint.  They do not address the no-op endpoint, and no analogous table or
decoder is supplied for the `M`-containing aperture modes.  Therefore
Theorem 4.1's phrase "the unique bounded origin code" assumes both endpoint
recognizability and path-bank disjointness which have not been established.

## 4. Atom, aperture, and residual tasks are not jointly selected

Section 5 of the primary file removes the zero-charge atom and then states
that the residual extreme bank is disjoint from the origin code.  That does
not follow from zero charge of the atom, because Lemma 2.1 may choose aperture
blocks outside the atom.

### Proposition 4.1 (legal aperture/residual overlap)

Consider the imbalance-one work word

\[
                            A C A B^{11}.             \tag{4.1}
\]

Choose the first `A|C` as the zero-charge atom.  Its gap has length zero.
The next two nonhead blocks `A|B` form a legal mass-two aperture.  After the
atom is removed from the cancellation input, however, the remaining word is

\[
                              A B^{11},               \tag{4.2}
\]

and its unique residual extreme is exactly the `A` used by the aperture.

#### Proof

The aperture mass is two, strictly between zero and eight.  Removing the
opposite pair `A|C` leaves signed imbalance one, represented by the displayed
`A`; all other blocks are neutral.  Thus the supports coincide. \(\square\)

A different joint selection may avoid this example.  What is missing is a
theorem that makes that joint selection while preserving the residual bound
and the aperture hypotheses.  Simply deleting the aperture from the
cancellation word is not harmless: unlike the atom, an aperture need not
have zero signed charge, so the bound `t <= 3` and the collar balance equation
must then be recomputed.

There is also a gap in the written proof of the origin-aperture lemma.  The
claim that changing to the other edge of a singleton run gives opposite
outer signs unless the whole reduced word has one minority letter is not
valid as stated.  For example, in

\[
                             A A C A A C C             \tag{4.3}
\]

the two edges incident with the singleton first `C` both have outer letters
`A,A`, although `C` is not a unique minority letter.  This does not disprove
existence of some aperture; it shows that the displayed case split is not a
proof of the selector needed by Section 5.

## 5. A mobile cart is not by itself a task-origin record

Theorem 4.1 of the primary file claims transport of the temporary `H|H`
through named block alphabets.  Section 5 then says that, for each remote
increment, the cart shuttles the remote block to the collar and returns the
target block to its labelled address.  These are different statements.

Even with a literal cart beside a local window, an unmarked interchange has
the old location collision

\[
              Y|X|HH\leadsto X|Y|HH,                 \tag{5.1}
\]

because the endpoint is also the initial local checkpoint for a source in
which `X,Y` already occur in the latter order.  A fixed cart makes every
strict microstate locally visible; it does not record the original address
of `X` after the macro interchange.  The marked-corridor theorem repairs
this only when the crossed interval is actually rewritten as a decodable
trail, or when another literal origin marker remains at the task address.

No such trail or task-origin marker is specified in Section 5.  In
particular:

1. The fixed-berth visible-cart theorem cannot be invoked as written: its
   protected fixed berth is precisely what APH is trying to create.
2. Replacing that berth by an adaptive OC18 code requires the work-level
   source-disjoint decoder rejected in Sections 2--3 above.
3. The protected-island theorem covers the recorded islands `H`, `H|M`, and
   `M|H`; an arbitrary two-block OC18 codeword is not one of its stated
   hypotheses.
4. The primary file neither performs a complete marked tagging pass before
   the four increments nor gives an enlarged-alphabet trail theorem for the
   resulting residual and `G_1` tasks.

Thus Section 5 is an endpoint schedule, not a proof of `ACT4`'s
occurrence-labelled gather/scatter row.

## 6. A constructive endpoint repair: a three-position single-head code

The two-block no-op is not a capacity obstruction.  Enlarge an OC18
two-block aperture of mass two, four, or six by one raw nonhead block.  Its
new mass is an even `J` with `2 <= J <= 10`.  Whenever that third block has
been selected disjointly, the resulting three-block aperture has a simple
self-locating endpoint family for the three collar-order classes.

For each even `J` with `2 <= J <= 10`, choose the following raw ordered pair
`F_J` of mass `J-2`:

\[
\begin{array}{c|ccccc}
J&2&4&6&8&10\\ \hline
F_J&A|A&A|B&A|C&B|C&C|C.
\end{array}                                         \tag{6.1}
\]

Write `F_J=F_1|F_2` and put

\[
 O_{J,0}=H|F_1|F_2,\qquad
 O_{J,1}=F_1|H|F_2,\qquad
 O_{J,2}=F_1|F_2|H.                                 \tag{6.2}
\]

### Proposition 6.1 (three-position code capacity)

The three words in (6.2) have total mass `J`, are pairwise distinct, contain
exactly one aligned `H`, and are outside the raw three-block alphabet.  The
position of that `H` records one of the three collar-order classes.

Every three-block aperture source of the same mass is individually reachable
from each word in (6.2) inside the six-coordinate capacity-two layer.

#### Proof

The head has mass two and (6.1) has mass `J-2`, proving the mass statement.
The fillers contain no `H`, so the three insertion positions are distinct
and each word has exactly one head.  A word containing `H=02` is not raw.

Because (6.2) is neither the all-zero nor the all-two state, its fixed-mass
layer is nonextreme.  The prefix-discrepancy algorithm connects every two
states in a nonextreme capacity-two layer on a path: move a unit from the
first prefix excess to the next prefix deficit.  This gives the individual
reachability assertion. \(\square\)

At a macro checkpoint separated from the temporary cart, (6.2) visibly
distinguishes an isolated origin head from the mobile adjacent pair `H|H`.
It also makes the collar-order endpoint capacity literal rather than
algorithmic.  What Proposition 6.1 deliberately does **not** prove is a
mutually source-disjoint family of paths from all allowed aperture sources
to these endpoints.  That finite routing/decoder row is the remaining local
work, not scalar connectivity.

## 7. The authoritative exact remaining statement

The proof-safe named frontier is still `ACT4`.  For the OC18 architecture it
can be sharpened to the following statement.

### Origin-coded anchored-catalyst four-task lemma `OC-ACT4`

Start at a decoded fixed-`p_1` work checkpoint with:

1. a raw work word, a named two-block source collar, and four named staging
   slots;
2. one deterministically selected zero-charge atom with its early literal
   atom/phase record;
3. a bounded origin aperture selected jointly with the cancellation so that
   it is disjoint from the atom, the collar, the staging slots, and every one
   of the at most four labelled task occurrences;
4. a temporary `H|H` still at that atom; and
5. the collar order still literal.

There are pairwise source-disjoint directed work paths, using no theorem
whose premise is a source-independent fixed head, which do all of the
following.

**Origin write.**  Before both temporary heads leave, write a persistent
origin word.  Its literal state and physical occurrence, together with the
early register, injectively recover the atom address, aperture source and
geometry, private/raw phase, and collar-order class.  The complete writing
paths, not only their endpoints, are source indexed and mutually disjoint.

**Four-task escort.**  Move the temporary cart and gather the at most four
labelled source task blocks into their named staging slots.  At every macro
and strict state a literal trail or a stationary task-origin record recovers
the task index, its original address, direction, crossed interval, and local
microstep.  The decoder remains valid across previously written `M` blocks,
the `G_1` task, and the complete origin word, each of which is restored when
crossed.

**Bounded conversion and scatter.**  Apply the already proved fixed-mass
path on the collar plus at most four staging slots, writing the collar-order
record `R_j` and all task targets.  Scatter every target to its own source
address under the same decoder.

**Retirement.**  Return the temporary cart to the recorded atom, restore the
aperture source, reverse the atom bootstrap, and erase the early atom record
only after `R_j` is literal.  Then use the proved order-copy schedule to turn
`R_j` into the source-independent permanent `H|H`.

Every nonzero work edge must lie after `p_1`, so the already audited fixed-row
generator supplies its directed lift.

The unresolved local catalog in `OC-ACT4` is bounded:

* two-block OC18 writes live only in `V_2,V_4,V_6`, of respective sizes
  `10,19,10`; the three-block repair lives in one six-coordinate layer;
* the collar conversion uses at most six two-coordinate blocks, hence twelve
  work coordinates; and
* one escort step uses one task block, one crossed block, and the two cart
  blocks.  Arbitrary distance is iteration of that same local step with a
  literal trail decoder, not a growing finite search.

This is the exact bounded occurrence-labelled pre-head path statement.  It
does not assume a fixed head and therefore breaks the dependency cycle if
proved.

## 8. Conditional composition and exact scope

### Theorem 8.1 (`OC-ACT4` implies APH)

If `OC-ACT4` holds on every `ACT4` input, then odd APH holds for every odd
`k >= 45` covered by the four-slot staging reduction.

#### Proof

The `ACT4` reduction supplies a zero-charge atom, at most four labelled
tasks, the scalar collar identity, and four staging slots.  Apply
`OC-ACT4`.  Its retirement endpoint is a raw restored temporary support, all
task targets at their labelled addresses, the collar-order copy protected,
and a literal source-independent permanent cart.  These are exactly the
inputs required by the already proved fixed-head marked/LIFO continuation,
connector beta, and monotone post-beta accumulator.  No fixed-head theorem is
used before the permanent cart appears. \(\square\)

The primary OC18 file aims at the lower threshold where the reserved-collar
work word has length at least fourteen (equivalently `k >= 33` under
`|w|=m-3`, `k=2m-1`).  This audit does not certify that threshold: the joint
atom/aperture/task selector needed for it is missing.  The only currently
proved asymptotic implication is therefore

\[
        \boxed{\text{`ACT4` or `OC-ACT4`}\Longrightarrow
               \text{odd APH for }k\ge45.}           \tag{8.1}
\]

Without that occurrence-labelled path bank, the proof-safe status is

\[
 \boxed{
 \begin{array}{l}
 \text{odd post-beta terminal: closed},\\
 \text{early atom record and raw anchored transport: closed},\\
 \text{OC18 fixed-row directed lift: closed},\\
 \text{OC18 work-level origin/task decoder: open},\\
 \text{odd APH and the full odd package: open exactly at `ACT4`.}
 \end{array}}
\]
