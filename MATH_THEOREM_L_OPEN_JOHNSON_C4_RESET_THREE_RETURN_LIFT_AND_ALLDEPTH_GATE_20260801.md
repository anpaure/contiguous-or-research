# The open Johnson C4 gives the exact central rolling-reset three-return packet, but needs a resident all-depth lift

**Date:** 2026-08-01  
**Lane:** L, occurrence-labelled three-return / compiler interface  
**Status:** exact four-resource and projection theorem; exact common-residual
and topology composition with the opened reset; sharp minimality on the
clean simple-cycle face; exact obstruction for the *bare* consecutive C4.
The formerly open all-depth extension is now closed by the `4d+2`-root
complete-reversal packet in
`MATH_THEOREM_RESET_RETURN_RAIL_COMPLETE_REVERSAL_GUARDED_CYCLE_20260801.md`.
Global planting, opening, exterior windows, the common residual compiler and
regeneration remain open.

## 0. Verdict

The open Johnson-square candidate is the first coupled module which evades
the opposite-seam independent-gain-ear obstruction.

At the central ordered-diamond level it passes exactly:

* the two phases have identical immediate lower and owner palettes;
* after pairing with the two opened-reset phases, their complete typed tail
  and head inventories agree;
* the square's attachment symmetric difference is one return path;
* its predecessor symmetric difference is exactly the two signed parity
  return paths; and
* all three projections come from the same six literal square atoms.

Thus it is an exact **central compatible three-return packet**.  It also
leaves one common residual lower/owner seam pair instead of two
phase-specific debts.

The bare four-root square is not a full rolling-reset compatible lift in the
all-depth sense.
Each open square phase is a consecutive three-edge detour in which one
fresh coordinate has run length two.  Hence no flat strict depth-\(d\)
all-high lift exists for \(d\ge2\).  A resident collar, a longer packet, or
a genuinely nonflat compiler must repair this.  Compiler safety is a joint
packet condition in one fixed cap and does not follow from the central
resource identities.

## 1. The literal square

Let the reset seam endpoints be

\[
                    V_0=A=S\cup\{x\},\qquad
                    V_1=B=S\cup\{y\},                       \tag{1.1}
\]

where \(|S|=r-1\), \(x,y\notin S\), and \(x\ne y\).  Choose

\[
                    f\in S,\qquad
                    g\notin S\cup\{x,y\},                   \tag{1.2}
\]

and set

\[
 V_2=(S\setminus\{f\})\cup\{y,g\},\qquad
 V_3=(S\setminus\{f\})\cup\{x,g\}.                          \tag{1.3}
\]

Then

\[
                         V_0V_1V_2V_3V_0                   \tag{1.4}
\]

is a simple Johnson \(C_4\).  For \(i\) modulo four put

\[
              L_i=V_i\cap V_{i+1},\qquad
              U_i=V_i\cup V_{i+1}.                          \tag{1.5}
\]

The seam resources are

\[
                         L_0=S,\qquad U_0=S\cup\{x,y\}.      \tag{1.6}
\]

The other three pairs are

\[
\begin{array}{c|c|c}
i&L_i&U_i\\ \hline
1&(S\setminus\{f\})\cup\{y\}&S\cup\{y,g\}\\
2&(S\setminus\{f\})\cup\{g\}&
          (S\setminus\{f\})\cup\{x,y,g\}\\
3&(S\setminus\{f\})\cup\{x\}&S\cup\{x,g\}.
\end{array}                                                 \tag{1.7}
\]

They are rainbow on both shores.

Write an ordered atom as

\[
                         (L,U,T,H).                          \tag{1.8}
\]

Delete opposite orientations of the seam and retain

\[
\begin{aligned}
 Q^\rightarrow
   &=\{(L_1,U_1,V_1,V_2),\
        (L_2,U_2,V_2,V_3),\
        (L_3,U_3,V_3,V_0)\},\\
 Q^\leftarrow
   &=\{(L_3,U_3,V_0,V_3),\
        (L_2,U_2,V_3,V_2),\
        (L_1,U_1,V_2,V_1)\}.
\end{aligned}                                               \tag{1.9}
\]

The omitted atoms are respectively

\[
            (L_0,U_0,V_0,V_1),\qquad
            (L_0,U_0,V_1,V_0).                              \tag{1.10}
\]

They share the one physical lower/owner seam pair \(L_0,U_0\); the two
orientations are never selected together.

## 2. Exact resource and projection signature

### Theorem 2.1 (central four-resource identity)

Both sets in (1.9) are ordered-diamond four-resource matchings.  They use
the same lower and owner palettes

\[
                  \{L_1,L_2,L_3\},\qquad
                  \{U_1,U_2,U_3\}.                          \tag{2.1}
\]

Their typed tail and head differences are

\[
\begin{aligned}
 \chi_T(Q^\rightarrow)-\chi_T(Q^\leftarrow)
       &=e_{V_1}-e_{V_0},\\
 \chi_H(Q^\rightarrow)-\chi_H(Q^\leftarrow)
       &=e_{V_0}-e_{V_1}.                                  \tag{2.2}
\end{aligned}
\]

The head--owner attachment symmetric difference is the one alternating
path

\[
 V_0^+ -U_3-V_3^+-U_2-V_2^+-U_1-V_1^+,                    \tag{2.3}
\]

up to reversal.  The tail--head predecessor symmetric difference is the
disjoint union

\[
 V_1^- -V_2^+-V_3^- -V_0^+                                \tag{2.4}
\]

and

\[
 V_0^- -V_3^+-V_2^- -V_1^+.                               \tag{2.5}
\]

Thus it exports exactly one attachment endpoint pair and the two oppositely
signed predecessor endpoint pairs on \(V_0,V_1\).

#### Proof

Formula (1.7) proves the lower/owner claim.  The tail sets are
\(\{V_1,V_2,V_3\}\) and \(\{V_0,V_2,V_3\}\), while the head sets are
\(\{V_0,V_2,V_3\}\) and \(\{V_1,V_2,V_3\}\), giving (2.2).

In the attachment projection, \(Q^\rightarrow\) gives

\[
             (V_2,U_1),(V_3,U_2),(V_0,U_3),
\]

and \(Q^\leftarrow\) gives

\[
             (V_1,U_1),(V_2,U_2),(V_3,U_3).
\]

Alternating them gives (2.3).  In the predecessor projection the two
matchings are

\[
 V_1^-V_2^+,\ V_2^-V_3^+,\ V_3^-V_0^+
\]

and

\[
 V_0^-V_3^+,\ V_3^-V_2^+,\ V_2^-V_1^+.
\]

Their two components are (2.4)--(2.5). \(\square\)

There is also a lower--tail alternating path between \(V_0,V_1\).  It is
irrelevant when immediate lower correctness is only a palette condition,
because (2.1) is exact.  A host which freezes occurrence-labelled
lower--tail assignments must include that path in its packet state; it is
part of the all-depth gate, not an automatically zero projection.

## 3. Composition with the opened reset

Identify \(V_0=T_0\) and \(V_1=T_{N-1}\).  Pair the forward reset path with
\(Q^\rightarrow\) and the reverse reset path with \(Q^\leftarrow\).

### Theorem 3.1 (central compatible three-return lift)

Assume the private square resources

\[
 V_2,V_3,\quad L_1,L_2,L_3,\quad U_1,U_2,U_3               \tag{3.1}
\]

are disjoint from the reset interior and the fixed exterior, except for the
declared endpoint incidences.  Then:

1. the square tail/head differences (2.2) cancel the opened reset's tail
   and head differences;
2. (2.3) closes the reset attachment path and (2.4)--(2.5) close its two
   predecessor parity paths;
3. the two combined phases consume identical complete sets of immediate
   lower, owner, typed-tail and typed-head resources;
4. the omitted seam tasks \(L_0,U_0\) are the same common residual tasks in
   both phases; and
5. every projected return is the projection of the literal atoms (1.9).

Hence the open \(C_4\) instantiates the central resource and atomic-lift
part of the rolling-reset compatible three-return criterion.

#### Proof

The opened reset's forward phase omits typed tail \(V_1\) and head \(V_0\);
its reverse phase omits tail \(V_0\) and head \(V_1\).  Equation (2.2)
supplies exactly the complementary resources.  The reset endpoint paths
and (2.3)--(2.5) have the same endpoints, so their unions are alternating
cycles.  Equations (2.1) and (1.10) give the common immediate palettes and
common residual seam tasks.  All projections were read from the same
ordered atoms in Theorem 2.1. \(\square\)

At physical-topology level, a directed reset path from \(V_0\) to \(V_1\)
followed by

\[
                         V_1\to V_2\to V_3\to V_0           \tag{3.2}
\]

is one directed cycle.  The reverse phase is its reverse.  If the reset
packet is meant to remain attached to a larger path rather than close as an
isolated cycle, a separate common opening/connector is still required.

## 4. Minimality on the clean orientation-flip face

### Theorem 4.1 (support-four minimum in the simple-cycle class)

Among open orientation flips of one simple Johnson cycle whose retained
edges are owner- and lower-rainbow and whose predecessor difference has two
signed parity paths, the \(C_4\) is minimum.

#### Proof

A cycle of length two is the two opposite orientations of one Johnson edge:
it repeats the unique lower and owner resources and is the forbidden closed
doubleton.  Opening a triangle leaves a two-edge detour between adjacent
endpoints.  The common-neighbour dichotomy says every such detour repeats
either the endpoint intersection or endpoint union.  The next simple cycle
has length four, and (1.7) realizes both rainbows. \(\square\)

This is not a claim that every conceivable non-Cartesian support-three
packet is impossible.  The minimum is exact for the clean simple-cycle
orientation-flip architecture.

## 5. The exact all-depth obstruction

The forward square path (3.2), read from \(V_1\) to \(V_0\), inserts the
private coordinate \(g\) on its first turn and deletes it on its third.
The reverse square path has the same run.

### Theorem 5.1 (no consecutive flat depth-\(d\) lift)

For every \(d\ge2\), the phases (1.9) cannot be consecutive strict
depth-\(d\) all-high chronology segments with the private square roots
unchanged.

#### Proof

The positive owner run of \(g\) on the square path consists exactly of
\(V_2,V_3\), hence has length two.  Under the repository's strict
depth-\(d\) convention, every internal positive run has length at least
\(d+1\).  Equivalently, at the first square transition the shifted flag would
have to append the freshly inserted \(g\), while a legal strict shift
appends a member of the old bottom block.  This is impossible for
\(d\ge2\). \(\square\)

Consequently Theorem 3.1 is a central/projection closure, not yet the full
literal all-depth lift required by the reset theorem.  A positive completion
must provide one of:

1. a collar which extends the \(g\)-run and supplies compatible flags in
   both orientations;
2. a longer coupled open module with the same central boundary; or
3. a nonflat compiler actuator which compensates the short run.

The collar must also prove equality of every selected suffix-target
multiset and rail histogram.  Immediate palette equality (2.1) does not
imply these rows.

## 6. Upper and boundary guards

The two completed **owner cycles** are reversals of the same undirected
cycle.  Therefore their cyclic owner-level interval-union decks and
coordinate run multisets agree.  This observation does not by itself prove
source-word or linear-boundary transparency.

For an all-depth physical module one must additionally verify:

1. complete occurrence-labelled flags in both phases and equality of every
   marked lower suffix deck;
2. a full prefix/suffix union signature, or another proved boundary
   dominance certificate, so crossing intervals in an arbitrary exterior
   retain their upper witnesses;
3. equality/dominance of every internal source interval union at the guarded
   widths;
4. a common topology boundary and common residual component quotient; and
5. one common provider for the residual seam tasks \(L_0,U_0\), unless those
   tasks are deliberately left to a later common transversal.

The owner-level reversal proves only the cyclic central part of item 2.

## 7. Compiler and private-sink requirements

Treat the square as **one correlated packet**, not as three independently
chosen return corridors.  This removes the three-menu selection problem but
does not remove occurrence hazards.

Fix a deletion-only compiler cap \(\theta\).  If installing the selected
phase has complete hazard set \(D_\varepsilon\), its exact compiler
condition is

\[
                         D_\varepsilon\in I(M_\theta^*).     \tag{7.1}
\]

For one fixed compiler matching which supports a deferred choice of either
phase, the stronger sufficient condition is

\[
 D_\rightarrow\cup D_\leftarrow\in I(M_\theta^*).           \tag{7.2}
\]

With an allowed deletion \(F\), replace the left side by its union with
\(F\).  Equivalently, all hazard cells in that union must have
vertex-disjoint alternating relocation paths to distinct unmatched compiler
sinks.  A source-private relocation block for the complete square packet is
a transparent sufficient certificate.

Separate tests on the three projected return paths are insufficient.  The
same \(U_{2,3}\) obstruction can occur internally if three packet hazards
are the only providers of one compiler target.  If the phase change alters
incidences rather than only deleting cells, (7.1)--(7.2) do not apply; one
must instead prove a common contracted compiler minor or a literal paired
relocation module.

Compiler relocation paths are distinct from the attachment and predecessor
paths in Theorem 2.1.

## 8. Exact surviving target

The open Johnson square closes the previously missing **central correlated
three-return** row.  The remaining physical theorem is now:

\[
 \boxed{\text{resident/flag-compatible collared open }C_4}
 \;+\;
 \boxed{\text{all-depth boundary and residual-seam guards}}
 \;+\;
 \boxed{\text{joint fixed-cap private-sink certificate}}.
\]

The complete-reversal return rail now supplies the resident all-depth packet,
all cyclic internal OR decks, every derivative inventory, and internal
compiler transport.  It does not supply a global root-palette host, a common
opening/join, exterior cross-window transparency, one common residual
compiler, or same-parity regeneration.  No
\(\nu(k)\le B(k)+O(1)\) conclusion is inferred.
