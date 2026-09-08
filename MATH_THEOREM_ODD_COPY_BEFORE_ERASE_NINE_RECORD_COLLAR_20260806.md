# Copy-before-erase closes the nine-type odd head collar

**Date:** 2026-08-06  
**Method:** a persistent finite record, the proved root/clock state graph,
and deterministic capacity-two routing; no search or computation  
**Status:** proposed exact closure, pending independent audit of the
three-row record schedule below.  The key correction is that the exterior
tape already determines `a+b`; only the order class inside one fixed sum must
be recorded, and its maximum multiplicity is three.  The operational
root/boundary branch register is therefore left free.

## 1. The logical point

Fix two source connector blocks at a common physical collar,

\[
                         C(a)\mid C(b),
             \qquad (a,b)\in\{0,1,2\}^2.
\tag{1.1}
\]

The previous formulation asked for nine internally disjoint paths inside a
small record register.  That is stronger than the required statement in the
full state graph.  While the record is being written, (1.1) itself is a
persistent nine-valued label.  After the record has been written, the record
is the label.  On teardown the complemented collar is again a persistent
nine-valued label.  Thus information never has to be absent.

This is the ordinary reversible rule

\[
                         \text{copy first, erase second}.
\tag{1.2}
\]

## 2. The record has only three states

Because the full source is central and every connector outside the fixed
collar remains reverse-decodable, the outside tape determines

\[
                              s=a+b.
\tag{2.1}
\]

For fixed `s`, the possible ordered pairs have multiplicities

\[
                       1,2,3,2,1
        \qquad(s=0,1,2,3,4).
\tag{2.2}
\]

The active first scan pair has exactly three selected unordered rows

\[
 \mathcal R=
 \bigl\{\{01,10\},\{02,11\},\{12,21\}\bigr\}.
\tag{2.3}
\]

For each sum `s`, inject its ordered pairs into `mathcal R`; rows may be
reused for different sums.  Call the resulting row `R_(a,b)`.  A work edge
toggles only the endpoint inside its selected row, so this three-valued
record persists through every ordinary shadow-clock lift.  The four
root/boundary states remain available for the pass and local branch exactly
as in the visible-cart theorem.

### Lemma 2.1 (record reachability)

With the source collar (1.1) held fixed, the current first-pair row can be
routed to `R_(a,b)` by a directed finite path avoiding the old linkage.  With
the complemented collar held fixed, it can be routed from `R_(a,b)` to the
required terminal row.

#### Proof

The shadow-clock mass ladder connects clock masses one, two, and three and a
neutral reset chooses the required endpoint of the new row.  The component
router supplies or removes the bounded mass difference.  Hence the three rows
in (2.3) lie in one directed work component.  This routing does not consume
the root/boundary branch register.

Choose one simple route for each ordered pair `(a,b)`.  During a forward
record route the untouched literal collar (1.1) recovers `(a,b)`, so two
global routes cannot meet even if their projections to the first-pair rows
use a common hub.  The protected root/boundary register keeps the
old-linkage-avoidance signature.  The selected first-pair row remains the
first nonquiet clock.  This proves the forward assertion.  The reverse
assertion is identical because the nine complemented collars

\[
                         C^*(a)\mid C^*(b)
\tag{2.4}
\]

are again pairwise distinct.  Once the collar has been replaced by the head,
the outside decoded source supplies `s=a+b`, and the row `R_(a,b)` supplies
the remaining order class.  Thus the record is injective in the only phase in
which the literal collar is absent.  \(\square\)

## 3. Setup, work, and teardown

Put `H=02`.  The exact setup is performed in three stages.

1. Hold (1.1) fixed and apply Lemma 2.1 to write `R_(a,b)`.
2. While the literal source collar still labels `(a,b)`, use the proved
   component-mass router to prepay, in two disjoint bounded work reservoirs,
   all mass required by both collar conversions.  In particular each
   conversion has collar increment
   \[
                         4-2(a+b)
   \tag{3.1}
   \]
   (the target pair has mass `8-2(a+b)`, so the second increment has the
   same sign).  Return the first clock to the unordered row used by
   `R_(a,b)`.  Now hold both `R_(a,b)` and the exterior component masses
   fixed and route `C(a)|C(b)` together with the setup reservoir to `H|H`
   together with its prepaid state.  This last route has fixed
   work-component mass and is disjoint from the first clock, so the
   unordered row in (2.2) is unchanged (only its endpoint toggles).
3. Keep `R_(a,b)` fixed while the double-head visible-cart construction
   performs the entire marked-corridor complement pass.

The collar is at one common physical address, so after stage 2 the double
head has a genuinely fixed berth.  Its transport theorem therefore has the
occurrence label that the adaptive-berth bootstrap lacks.

Teardown reverses the information order:

1. Return the double head to the fixed berth.
2. Hold `R_(a,b)` fixed and use the separately prepaid teardown reservoir
   to route `H|H` to `C^*(a)|C^*(b)` at fixed work-component mass.
3. Hold the literal target collar fixed, restore both bounded reservoirs
   through the component router, restore the required terminal clock row,
   and then use Lemma 2.1 to retire the record.  The net reservoir change is
   exactly the negative of the collar's source-to-target mass change; the
   global central tape supplies that amount as in the proved component-mass
   theorem.

### Conditional Theorem 3.1 (copy-before-erase collar)

Assume the two prepaid reservoirs in stage 2 are literal banks whose original
source contents are retained in the decoder, and assume their setup,
fixed-mass use, and restoration have occurrence-labelled paths which leave the
three-row record and operational branch register available as stated.  Then
the nine setup--work--teardown paths above are pairwise vertex-disjoint in the
full state graph, retain a source/stage decoder at every nonterminal state,
and avoid the old linkage.  Under those assumptions the finite collar lemma
`DH` holds.

#### Proof

Partition a route into the five information phases

\[
 \begin{array}{c|c}
 \mathrm{phase}&\mathrm{persistent\ type\ label}\\ \hline
 \mathrm{write\ record}&C(a)|C(b),\\
 \mathrm{create\ head}&R_{a,b},\\
 \mathrm{bulk\ work}&R_{a,b}\ \mathrm{and\ the\ fixed\ head\ berth},\\
 \mathrm{retire\ head}&R_{a,b},\\
 \mathrm{erase\ record}&C^*(a)|C^*(b).
 \end{array}
\tag{3.2}
\]

Every row of (3.2) contains an injective encoding of `(a,b)`.  The protected
global pass state and the presence or absence of the fixed double head
separate the rows.  Within a row, use one deterministic simple route.  Its
literal local state determines the microstep once `(a,b)` and the row are
known.  Thus equality of two global states forces equality of `(a,b)`, the
phase, and the microstep.

During bulk work, the fixed berth and `R_(a,b)` meet the hypotheses of the
double-head visible-cart theorem, while the marked corridor and LIFO order
recover the macroscopic cancellation stage.  The shadow clock supplies the
directed lift.  The root/boundary signatures and nonquiet first-pair row avoid
the old linkage, exactly as in Lemma 2.1.  This proves disjointness,
decodability, and avoidance.  \(\square\)

### Audit boundary

The hypotheses about the prepaid reservoirs are not supplied merely by the
scalar component-mass theorem.  That theorem reaches prescribed component
configurations but explicitly does not provide a cross-source
occurrence-labelled routing bank, and an arbitrary work reservoir contains
source information which cannot be overwritten without being recorded.
Thus the copy-before-erase logic reduces `DH` to a bounded persistent-record
and battery-routing lemma; it does not yet prove that lemma.

## 4. Scope

The conditional theorem would close the former nine-type
initializer/retirement premise.  It does not by itself complement the one
connector which overlaps the active
first scan pair.  If that connector is extreme, the work tape retains one
opposite extreme; their joint occurrence-labelled handoff remains the sole
bounded odd residue.  The same copy-before-erase principle may be used in
that handoff, but its directed path must be compatible with first-pair
retirement.
