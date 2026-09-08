# The coherent three-label birail has an indispensable cubic Markov move

> **Physical-scope correction, 2026-08-01.**  The `C6`/`C8` toric
> calculations and whole-chain source-signature identities below remain
> valid.  The literal Klein four-block realization of the `C8` (phase
> vectors `0110` and `1001`) is **not** a simple-owner or strict-lower-
> rainbow physical packet.  The independent replay
> `scratch/audit_c8_fourblock_physical_owner_palette_nogo_20260801.py`
> proves `32d+92` central owner occurrences but only `8d+24` distinct
> owners, together with the analogous lower-q1 multiplicities.  Uniform
> block-private tags do not repair this while preserving the connected
> cancellation relation.  References below to a strict-rainbow twisted-cube
> lift are therefore conditional on a nonliteral quotient weave.  The
> abstract chordless-`C8` Markov result is unaffected.

Date: 2026-08-01  
Status: exact local theorem for the nested lower-provider quotient of one
three-slot mixed-coatom family, plus the source-signature four-packet
comparison subject to the correction above.
Compiler defect, exterior witnesses, global host existence, and simultaneous
planting in a Pascal child are outside scope.

## 0. Result

For the three authenticated active pairs

\[
 \{I_{ab},I_{bc}\},\qquad
 \{I_{bc},I_{ca}\},\qquad
 \{I_{ca},I_{ab}\},
\]

the smallest occurrence-labelled state which retains the whole multi-depth
provider chains is a \(3\times3\) zero-one matrix with zero diagonal.  The
row and column margins are all one.  Its allowed bipartite support is

\[
                         K_{3,3}-\{11,22,33\}=C_6.
\]

Consequently its toric ideal is principal:

\[
 x_{12}x_{23}x_{31}-x_{21}x_{32}x_{13}.             \tag{0.1}
\]

The alternating \(C_6\) is the unique primitive Markov move.  There is no
legal \(2\times2\) move.  The cubic is indispensable already for \(d=2\),
and the same whole-chain cubic is sufficient for every \(d\ge2\).

This cubic statement is exact for the common lower-chain/provider ledger.
The all-\(d\), same-flag physical triangle repeats three cross-packet lower-
\(q1\) socket colours, so it is not a strict \(q1\)-rainbow packet bank.
For \(d=2,3\), distinct-filler three-packet variants are genuinely
rainbow-compatible and retain the cubic.  The authenticated uniform
strict-rainbow family for every \(d\ge2\) is instead the four-packet twisted
cube; its honest support is \(C_8\) and its indispensable move is quartic.

At \(d=3\), treating the two depths independently produces four formal
states, two of which have no physical mixed-coatom phase.  In depth-expanded
orientation coordinates, the same cubic has degree \(3(d-1)\); this growth
is exactly removed by the honest whole-chain token quotient.  Thus the
answer depends on the coordinate system:

* depthwise squares are not a physical Markov basis;
* the smallest balanced three-row birail needs, and has, one cubic
  whole-chain toggle in its lower-provider quotient.

No claim is made that arbitrary prepared families have cubic Markov bases.
For a general allowed occurrence graph, chordless even cycles are required;
quadrics suffice exactly on the chordal-bipartite face, provided every such
cycle has a literal physical lift.

## 1. Input from the mixed-coatom provider theorem

Put

\[
             1=I_{ab},\qquad 2=I_{bc},\qquad 3=I_{ca}.
\]

For \(2\le q\le d\), the exact filler flags are

\[
 P_q=\{f_1,\ldots,f_{d+1-q}\},\qquad
 S_q=\{f_q,\ldots,f_d\}.                              \tag{1.1}
\]

The three authenticated connector rows have active pairs

\[
                       \{2,3\},\quad\{1,2\},\quad\{3,1\}.       \tag{1.2}
\]

The provider theorem authenticates these row types separately.  In Sections
1--5, **lower-chain prepared family** means that one occurrence of each type
has been indexed over the same core, filler order and chain addresses and
that only its nested lower occurrence/provider ledger is being quotiented.
This does not assert cross-slot lower-\(q1\) palette disjointness.  Even
disjoint exterior halos do not remove an internal socket collision.
Establishing a simultaneously strict-rainbow planting in an arbitrary child
is a separate theorem.

For an oriented pair \(i\to j\), every depth uses the same orientation:

\[
 i\cup P_q\longleftrightarrow c_q^L,\qquad
 j\cup S_q\longleftrightarrow c_q^R.                  \tag{1.3}
\]

Reversing the physical phase replaces \(i\to j\) by \(j\to i\) at every
depth simultaneously.  The provider-switch theorem proves that these are
the only changed local supports and that the displayed cells are their
unique providers inside the prepared bank.

We impose one exact balancing condition: across the three prepared slots,
each active label occurs once on the prefix rail and once on the suffix
rail.  This is the fixed-margin condition needed to preserve the separate
active-label rail ledgers.  An isolated row toggle does not preserve these
separate margins.

## 2. The smallest honest state matrix

For \(i\ne j\), let

\[
 x_{ij}=1
\]

mean that the prepared slot \(\{i,j\}\) is oriented \(i\to j\), hence
uses (1.3) at **all** depths.  Put \(x_{ii}=0\).  The exact constraints are

\[
\begin{aligned}
 x_{ij}+x_{ji}&=1 &&(1\le i<j\le3),\\
 \sum_{j\ne i}x_{ij}&=1 &&(i=1,2,3),\\
 \sum_{i\ne j}x_{ij}&=1 &&(j=1,2,3).                 \tag{2.1}
\end{aligned}
\]

The first line chooses one phase in each physical slot.  The second and
third lines are the prefix- and suffix-label margins.  In this unit-margin
fibre the slot equations are redundant, but retaining them records the
physical occurrence labels and is useful for larger multiplicities.

This is the smallest exact quotient for the stated prepared family:

1. fixed cores, filler flags and cell addresses are deterministic and may be
   suppressed;
2. every admissible oriented slot has a distinct depth-two target/provider
   incidence, so none of the six off-diagonal variables can be identified;
3. one variable \(x_{ij}\) determines the complete depth vector by (1.3).

Thus the compression loses no in-scope lower-support or local-provider
information.  It is not asserted to preserve compiler defect or exterior
last-witness data.

Equivalently, use physical-slot columns \(e_{12},e_{23},e_{31}\), and let
\(y_{i,e}=1\) when label \(i\) occupies the prefix chain of slot \(e\).
The literal table is

\[
\begin{array}{c|ccc}
 &e_{12}&e_{23}&e_{31}\\ \hline
1& *&0&*\\
2& *&*&0\\
3& 0&*&*
\end{array}.                                                   \tag{2.2}
\]

The suffix label is the other endpoint of \(e\).  Relabelling an allowed
cell \(y_{i,\{i,j\}}\) as \(x_{ij}\) gives the oriented matrix above.  This
slot form makes clear that the margins are physical occurrence margins, not
an ad hoc algebraic restriction.

### Structural zeros

There are exactly three structural zeros in the whole-chain table:

\[
                            x_{11}=x_{22}=x_{33}=0.             \tag{2.3}
\]

In the slot representation these are \(y_{1,e_{23}},y_{2,e_{31}},
y_{3,e_{12}}\): a label cannot occupy a slot to which it does not belong.
All six off-diagonal orientations are locally authenticated.

If the table is unfolded by depth, rank-\(q\) targets may use only the two
rank-\(q\) cells \(c_q^L,c_q^R\); every cross-depth target-to-cell entry is
also a structural zero.  The equal-phase equations across depths are not
additional cell zeros.  They are diagonal coherence constraints on whole
physical phases.

## 3. Exact Markov basis

For completeness, retain every depth margin and the slot margin in the
design column.  The column of \(x_{ij}\) is

\[
 a^{(d)}_{ij}=e_{\{i,j\}}^S+
       \sum_{q=2}^d\bigl(e_{q,i}^L+e_{q,j}^R\bigr).    \tag{3.1}
\]

Deleting repeated depth-margin rows contracts (3.1) to
\(e_i^L+e_j^R+e_{\{i,j\}}^S\) and does not change its integer kernel.
Let \(z=(z_{ij})_{i\ne j}\) lie in the integer kernel.  The slot rows give

\[
                         z_{ji}=-z_{ij}.                       \tag{3.2}
\]

Write \(a=z_{12}\), \(b=z_{23}\), and \(c=z_{31}\).  The three left-margin
equations at any one depth give

\[
                     a-c=0,qquad -a+b=0,qquad -b+c=0.         \tag{3.3}
\]

Hence \(a=b=c\), and

\[
 \ker_{\mathbb Z}A=
 \mathbb Z\bigl(e_{12}+e_{23}+e_{31}
                 -e_{21}-e_{32}-e_{13}\bigr).         \tag{3.4}
\]

The generator is primitive.  A rank-one primitive integer kernel has the
singleton Markov basis consisting of its generator and reverse: along every
nonnegative fibre, consecutive feasible lattice points differ by that
primitive vector.  Equivalently, the allowed support graph is one chordless
\(C_6\), whose alternating circuit is (3.4).  This proves (0.1).

There is no supported \(2\times2\): any two chosen row labels and two chosen
column labels are subsets of a three-element set, so they intersect; the
corresponding diagonal cell is one of (2.2).  Therefore no quadratic
interchange exists.

The unit-margin fibre contains exactly

\[
 X^+=
 \begin{pmatrix}0&1&0\\0&0&1\\1&0&0\end{pmatrix},
 \qquad
 X^-=
 \begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}.            \tag{3.5}
\]

Any Markov basis for this fibre must connect these two states, so the cubic
is also indispensable without invoking the universal toric statement.

## 4. The cases \(d=2\) and \(d=3\)

### 4.1 Depth \(d=2\)

There is one lower depth and

\[
                         P_2=\{f_1\},\qquad S_2=\{f_2\}.       \tag{4.1}
\]

Each nonzero entry \(x_{ij}\) means that \(i\cup P_2\) uses the left cell
and \(j\cup S_2\) uses the right cell.  The two states are exactly (3.5),
and the unique move is the cubic (3.4).  Three independent row toggles are
not allowed by the fixed prefix/suffix margins.

### 4.2 Depth \(d=3\)

Now

\[
\begin{array}{c|c|c}
q&P_q&S_q\\ \hline
2&\{f_1,f_2\}&\{f_2,f_3\}\\
3&\{f_1\}&\{f_3\}.
\end{array}                                                    \tag{4.2}
\]

The depth-expanded abstract product has four formal states

\[
 (X^+,X^+),\ (X^+,X^-),\ (X^-,X^+),\ (X^-,X^-).              \tag{4.3}
\]

The provider-switch theorem permits only the diagonal two:

\[
                         (X^+,X^+),\qquad(X^-,X^-).            \tag{4.4}
\]

The mixed states in (4.3) would require opposite physical phases at depths
two and three of the same coatom block.  No such chronology exists.
Therefore a depth-two cubic followed independently by a depth-three cubic
is not a physical path.

If one nevertheless uses variables \(x_{ij}^{(q)}\) at every depth, the
primitive coherent move is

\[
 \widetilde g_d=\sum_{q=2}^d
 \bigl(e_{q,12}+e_{q,23}+e_{q,31}
      -e_{q,21}-e_{q,32}-e_{q,13}\bigr),              \tag{4.5}
\]

of binomial degree \(3(d-1)\) in those orientation variables; for \(d=3\)
the degree is six.  The chain-token map
\(x_{ij}\mapsto(x_{ij}^{(q)})_{q=2}^d\) is an exact bijection onto the
coherent states, and
contracts (4.5) to the cubic (3.4).

If each depth orientation atom is further split into its two literal
target-to-provider incidences, the same circuit has degree \(6(d-1)\).
These are repeated-coordinate embeddings of one circuit, not new Markov
moves or new structural zeros.

## 5. All-depth pattern and general structural-zero criterion

The flags and cell addresses change with \(d\), but the oriented-slot graph
does not.  Therefore (3.4) is the exact whole-chain Markov basis for every
\(d\ge2\).  A bounded higher-degree move is both necessary and sufficient:
the bound is three, not two.

The same conclusion extends exactly to any occurrence-labelled prepared
family made from these three row types.  Let

\[
 E=E_{12}\sqcup E_{23}\sqcup E_{31}
\]

be its set of prepared slots.  Use variables \(y_{i,e}\), with

\[
 y_{i,e}=0\quad\Longleftrightarrow\quad i\notin e,\qquad
 \sum_{i\in e}y_{i,e}=1,\qquad
 \sum_{e\ni i}y_{i,e}=r_i.                            \tag{5.1}
\]

These are all the structural zeros and margins in the local quotient.
Indeed, if \(\deg_E(i)\) is the number of slots containing \(i\), then the
suffix count of label \(i\) is automatically

\[
                           \deg_E(i)-r_i.                     \tag{5.2}
\]

At every depth \(q\), literal decoding gives

\[
\begin{aligned}
 \mu_q(i\cup P_q)&=r_i,\\
 \mu_q(i\cup S_q)&=\deg_E(i)-r_i.                     \tag{5.3}
\end{aligned}
\]

Thus one fixed row-margin system fixes both rails at every depth.

The allowed bipartite graph has only three label vertices.  Its chordless
cycles are exactly:

1. a \(C_4\) using two distinct slots of one common pair type \(E_{ij}\);
   its move is quadratic; or
2. a \(C_6\) using one slot from each of \(E_{12},E_{23},E_{31}\); its move
   is cubic.

No longer simple cycle exists because a bipartite simple cycle would need
more than three distinct label vertices.  Alternating-cycle decomposition
therefore proves:

> **Prepared-family Markov theorem.**  All supported quadrics and cubics
> above form a Markov basis for every nonnegative fixed-margin fibre of
> (5.1).  Degree at most three is uniform in \(d\).  After deleting
> invariant or zero-margin columns, quadrics suffice exactly when at least
> one of the three pair types is absent.  If all three types occur, each
> selected one-of-each \(C_6\) has a unit-margin fibre with its two
> alternating matchings, so its cubic obstruction is genuine.

The one-copy-per-type fibre of Sections 2--4 is the smallest case and has
no quadrics at all.

More generally, let \(G=(L,R;E)\) be the allowed graph of prepared
whole-chain tokens, with fixed endpoint margins.  The ordinary
transportation proof gives:

* alternating even cycles of \(G\) connect every nonnegative fixed-margin
  fibre;
* all simple even-cycle moves form an exact Markov basis;
* \(2\times2\) moves suffice for all margins if and only if \(G\) is chordal
  bipartite.

In particular, every induced cycle of length greater than four has a
unit-margin fibre consisting of its two alternating perfect matchings and
no supported square, so its higher-degree circuit cannot be omitted from a
square-only universal claim.

For the present family, \(G=C_6\), so the first higher-degree circuit is
already forced.  This abstract statement becomes a physical statement only
when each whole-chain cycle is supplied as one coherent prepared packet and
the family is closed under its application.  Those hypotheses hold locally
for the two stated phases; no global-host closure is inferred.

## 6. Strict-rainbow correction: the twisted cube is \(C_8\)

The all-\(d\) same-flag triangle from Sections 1--5 has a literal
owner-disjoint realization, but its three slots repeat exactly the socket
colours

\[
 K\mathord\infty cxF,\qquad
 K\mathord\infty cyF,\qquad
 K\mathord\infty czF.
\]

It therefore cannot be inserted unchanged in a strict lower-\(q1\)-rainbow
bank.  The four-packet twisted-cube theorem supplies the first authenticated
uniform correction.  Its Markov matrix can also be computed exactly.

For \(t=d+1-q\), write its four two-target cancellation channels as

\[
\begin{array}{c|c|c}
\text{channel}&\text{distinguished target}&\text{partner}\\ \hline
\alpha=h_{01}&E_{100}(A_t)&E_{000}(A_t)\\
\beta =h_{02}&E_{110}(B_t)&E_{010}(B_t)\\
\gamma=h_{13}&E_{101}(B_t)&E_{001}(B_t)\\
\delta=h_{23}&E_{111}(A_t)&E_{011}(A_t).
\end{array}                                                   \tag{6.1}
\]

The pairings are exactly those in the twisted-cube identity:

\[
\begin{aligned}
p_0&:\{\alpha,\beta\},&
p_1&:\{\alpha,\gamma\},\\
p_2&:\{\beta,\delta\},&
p_3&:\{\gamma,\delta\}.                              \tag{6.2}
\end{aligned}
\]

Let \(y_{i,h}=1\) when packet slot \(p_i\), on channel \(h\), carries the
distinguished target throughout the whole depth chain.  The honest support
matrix is

\[
\begin{array}{c|cccc}
 &\alpha&\beta&\gamma&\delta\\ \hline
p_0&*&*&0&0\\
p_1&*&0&*&0\\
p_2&0&*&0&*\\
p_3&0&0&*&*
\end{array}.                                                   \tag{6.3}
\]

The eight displayed zeros are all the structural zeros.  Each packet phase
carries a distinguished member on exactly one of its two channels, so the
packet-row sums are one.  Exact coefficientwise cancellation splits each
two-target channel between its two incident packets, so the channel-column
sums are one.  Conversely, these margins force exact lower-counter
preservation at every depth.

The two states are

\[
Y^-=
\begin{pmatrix}
1&0&0&0\\
0&0&1&0\\
0&1&0&0\\
0&0&0&1
\end{pmatrix},
\qquad
Y^+=
\begin{pmatrix}
0&1&0&0\\
1&0&0&0\\
0&0&0&1\\
0&0&1&0
\end{pmatrix},                                               \tag{6.4}
\]

with columns \((\alpha,\beta,\gamma,\delta)\).  The support cycle is

\[
                  p_0-\alpha-p_1-\gamma-p_3-\delta-p_2-\beta-p_0.
\]

Hence its integer kernel is rank one, generated by

\[
\begin{aligned}
g_8={}&e_{0\beta}+e_{1\alpha}+e_{2\delta}+e_{3\gamma}\\
     &-e_{0\alpha}-e_{1\gamma}-e_{2\beta}-e_{3\delta}. \tag{6.5}
\end{aligned}
\]

The toric ideal is the principal quartic

\[
 y_{0\beta}y_{1\alpha}y_{2\delta}y_{3\gamma}
 -
 y_{0\alpha}y_{1\gamma}y_{2\beta}y_{3\delta}.          \tag{6.6}
\]

Because (6.3) is chordless \(C_8\), no \(2\times2\) move exists and the
quartic is indispensable for this family.  Equivalently, if \(s_i\) is the
phase of packet \(p_i\), the four channels force

\[
                s_0=s_1,\quad s_0=s_2,\quad
                s_1=s_3,\quad s_2=s_3,                 \tag{6.7}
\]

so only the all-old and all-new phase vectors preserve the counters.

This proof is uniform in \(d\).  Even when \(A_t=B_t\) for the short base
depths, the eight cube triples in (6.1) remain distinct, so no channel
merges and no chord appears.  The whole-chain degree is four; separate
depth-token coordinates give degree \(4(d-1)\), and literal paired-provider
coordinates give degree \(8(d-1)\).

At \(d=2,3\), the distinct-filler three-packet constructions

\[
 (x,y),(y,z),(z,x)
\quad\text{and}\quad
 (x,m,y),(y,m,z),(z,m,x)
\]

are already owner- and \(q1\)-palette-disjoint and have the cubic \(C_6\)
matrix.  Thus the quartic is a uniform all-\(d\) construction, not a
dimensionwise minimality theorem.  For \(d\ge4\), a cubic is excluded only
on the normalized common-base face; arbitrary-core cubic existence remains
open.

## 7. Corrected CBC implication and the split-letter terminal

The audit of the Baggett--Yan reduction asked for physical
square-completeness.  The present calculation gives the exact weaker
replacement for the three-label lower-chain family.

### Theorem 7.1 (closed whole-chain cycle completeness)

Let \({\cal C}\) be a class of physical chronologies and let

\[
                 \phi:{\cal C}\longrightarrow{\cal F}_G(b)
\]

record an occurrence-labelled three-label whole-chain table of the form
(5.1).  Assume:

1. for every current \(T\in{\cal C}\), every supported \(C_4\) or \(C_6\)
   move applicable to \(\phi(T)\) has a literal compound lift at \(T\);
2. the lift preserves all physical rows declared in the definition of
   \({\cal C}\), and its result lies again in \({\cal C}\); and
3. the occurrence labels and whole depth chains used by \(\phi\) are the
   ones transported by that literal lift.

Then the physical orbit of any \(T_0\in{\cal C}\) projects onto the entire
fixed-margin fibre \({\cal F}_G(b)\).

#### Proof

Section 5 proves that the supported \(C_4\) and \(C_6\) circuits connect
every nonempty fibre of this three-label support.  Follow such an abstract
path from \(\phi(T_0)\).  Hypothesis 1 lifts its first circuit; Hypothesis 2
keeps the result in the class, so induction lifts the whole path.
Hypothesis 3 ensures that the projected endpoint is the requested table.
\(\square\)

Thus **closed whole-chain alternating-cycle completeness**, of degree at
most three, replaces square-completeness in the lower-chain CBC statement.
It is strictly weaker than requiring every square of a full rectangular
matrix fibre.  It is also still a physical closure hypothesis: the abstract
Markov theorem does not establish any of its three assumptions.

For a strict \(q1\)-rainbow all-\(d\) class based on the currently
authenticated twisted cube, the analogous degree bound is four, not three.

### Theorem 7.2 (terminal split certificate replaces defect factorization)

Suppose a reachable physical chronology \(T\) has an actual source word
\(W\), a complete matching \(M\) saturating the entire declared old
strict-lower target bank \(L\), and \(H\) insertion cuts, pairwise separated
so that no compiler-band cell crosses two cuts.  Fix a set \(R\subseteq L\)
of old chain targets whose \(M\)-edges will be released, and let \(U\) be
the genuinely new target bank.
At cut \(s\), insert a nonempty pivot \(X_s\).  Assume:

1. \(X_s\) is contained in the union of the two adjacent old source letters,
   so every old interval OR transports unchanged;
2. the cut is rank-saturated: the length-\((h+1)\) hull of every lost
   width-\(h\) crossing cell is a legal rank-\(m\) middle owner;
3. after releasing the \(M\)-edges of \(R\), the singleton and two ray
   cells at the \(H\) cuts admit a literal matching saturating
   \(R\sqcup U\), with no target or cell collision;
4. the inserted chronology satisfies the required owner, \(q1\), residence,
   upper, topology and deadline rows; and
5. the displayed expanded word is legal in one common cap.

Then the transported edges of \(M\) after deleting its \(R\)-incident
edges, together with the ray assignments, form a complete literal lower
matching.  No compiler-defect function
\(\lambda(\phi(T))\), and no assertion that compiler defect factors through
the birail matrix, is needed.  The length cost is exactly \(H\).

#### Proof

At one cut, the only old width-band cells which fail to transport are the
maximal crossing cells.  Rank saturation makes their values middle-rank, so
no strict-lower edge of \(M\) uses them.  Every edge of \(M\) therefore
transports injectively with the same OR.  Release the transported edges
incident with \(R\).  The new cells outside the transport image are
precisely the singleton and two rays, and Hypothesis 3 assigns
\(R\sqcup U\) to them.  Those assignments are cell-disjoint from the
remaining transported matching and saturate exactly the omitted plus new
target rows.  Hypothesis 5 supplies one literal common-\(Q\) witness, while
Hypothesis 4 supplies the noncompiler physical rows.  For separated cuts
the same argument composes cut by cut.
\(\square\)

Consequently the compiler quotient in the original CBC implication may be
replaced by the following terminal existential clause:

> some state in the closed whole-chain cycle orbit has a rank-saturated
> \(H\)-split source whose literal side-cell graph and common cap pass
> Theorem 7.2.

For \(H=1\), when the reachable chronology has baseline length \(B\), this
is an exact \(B+1\) terminal theorem.

There is a stronger terminal face tailored exactly to the two mixed-coatom
chains; it leaves the flat derivative ansatz.

### Theorem 7.3 (one split letter carries both coatom rays)

Let the actual old source word contain the local subword

\[
 \{f_{d-1}\},\ldots,\{f_2\},X,
 \{f_{d-1}\},\ldots,\{f_2\},
\]

and put

\[
\begin{aligned}
 Z&=A\cup\{f_1\},\\
 T&=B\cup\{f_d\},\\
 X&=Z\cup T.                                           \tag{7.1}
\end{aligned}
\]

Replace the one actual old letter \(X\) by the consecutive nonempty letters
\(Z,T\).  Then:

1. every old interval OR survives under full-block contraction;
2. the left-exclusive ray contains every \(A\cup P_q\);
3. the right-exclusive ray contains every \(B\cup S_q\), for
   \(2\le q\le d\); and
4. physical length increases by exactly one.

Hence, if transported old matching/witness cells remain deadline-admissible
and the resulting owner, \(q1\), residence, upper, topology and common-cap
rows are valid, the terminal compiler is literal and complete.  Compiler
defect need not be a function of the birail matrix, and the
rank-saturation hypothesis of Theorem 7.2 is unnecessary on this
block-split face.

#### Proof

An interval avoiding \(X\) is unchanged.  An interval containing \(X\)
is mapped to the interval containing both \(Z,T\), whose union is \(X\).
Thus all old ORs transport injectively.  The successive left-exclusive
intervals ending at \(Z\) add \(f_2,f_3,\ldots,f_{d-1}\), giving exactly
\(A\cup P_q\) in reverse \(q\)-order.  The successive right-exclusive
intervals beginning at \(T\) add
\(f_{d-1},f_{d-2},\ldots,f_2\), giving exactly \(B\cup S_q\).
The block has two letters in place of one. \(\square\)

The fixed-cut criterion is exact: the two desired chains must be cumulative
unions on the two physical rays, and their bases must union to one actual
old source letter \(X\).  Nesting or envelope containment alone is
insufficient.

The authenticated canonical \(0110\) maximal-erosion source does not supply
this host.  No native envelope contains the merged active roles together
with both extreme fillers, and the existing filler trace is one-sided
rather than mirrored.  The exact finite replay finds no terminal
two-chain split in any of the three connector rows or either phase for
\(3\le d\le20\) (the \(d=2\) old-phase degeneracy does not survive in the
terminal phase).  Thus Theorem 7.3 answers the factorization question
positively but conditionally: the remaining local gate is one phase-common
merged host, or two one-sided hosts, planted in the protected child.

The monotone inserted-pivot alternative of Theorem 7.2 does not make its
terminal gate automatic.  For the canonical complementary coatom chains,
all internal crossed joins equal one rank-middle owner, so the lower
compiler is exact but owner simplicity fails for \(h\ge3\).  The canonical
shortest rotating-hole source has the opposite failure: its crossed joins
have rank \(m-1\).  Its surviving physical lemma is a **pivot-rich source
theorem** producing distinct legal middle owners, endpoint Johnson
adjacency, and the full \(q1\)/residence/upper interface.  The block-split
alternative of Theorem 7.3 avoids those lost-crossing joins but needs the
new merged actual-letter host just identified.

In particular, whole-chain cycle completeness alone neither locates such a
terminal state nor proves that the property depends only on \(\phi(T)\).
The split theorems remove factorization after a literal terminal certificate
is found; they do not remove the terminal existence problem.

## 8. Exact boundary of the theorem

Proved here:

1. the occurrence-resolved whole-chain state matrix for the prepared
   three-slot family;
2. all its local structural zeros;
3. its exact rank-one integer kernel and indispensable cubic Markov basis;
4. the symbolic \(d=2,3\) fibres; and
5. the dimension-independent degree-three lower-chain pattern; and
6. the exact degree-four strict-rainbow twisted-cube pattern;
7. the corrected degree-three whole-chain CBC reachability implication; and
8. the exact conditional replacement of compiler factorization by either a
   rank-saturated split-terminal certificate or the sharper actual-letter
   two-coatom-ray split.

Not proved here:

1. existence of three mutually compatible prepared occurrences with
   disjoint or hereditarily commuting halos inside an arbitrary Pascal
   child;
2. preservation of exterior all-depth witnesses under a sequence of such
   packets;
3. compiler/common-cap feasibility or defect monotonicity;
4. rooted topology, global owner chronology, or regeneration.

The adjacent-order reflection breaker is not represented in the
common-order three-slot matrix.  Enlarging the packet menu can add cells and
cycles and therefore changes the Markov-basis problem.

Thus this theorem resolves the local Markov-basis question but not CBC(C),
an all-\(k\) upper bound, or literal contiguous-OR completion.

## 9. Exhaustive finite audit

The dependency-free audit

~~~text
python3 scratch/audit_r_coherent_birail_multidepth_markov_basis_20260801.py
~~~

enumerates all \(2^6=64\) binary \(C_6\) tables.  Their exact margin
signatures form 63 fibres: 62 singleton fibres and one two-state fibre, the
two states (3.5).  Their difference is exactly (3.4).  It also checks every
candidate \(2\times2\) support and finds none.

As an independent scope check, the same replay enumerates all \(2^8=256\)
binary tables on the rainbow \(C_8\): 254 singleton fibres and one two-state
fibre, with generator (6.5), and again no supported square.  It verifies
that the depth-three ambient product has four sign states but only two
diagonally coherent states.

Expected status:

~~~text
PASS_R_COHERENT_BIRAIL_MULTIDEPTH_MARKOV_BASIS
~~~

Canonical audit payload SHA-256:

~~~text
57f11efab00a9343eb0989510fa5800edd5a076101a09bb7bace07c2b38d9e66
~~~
