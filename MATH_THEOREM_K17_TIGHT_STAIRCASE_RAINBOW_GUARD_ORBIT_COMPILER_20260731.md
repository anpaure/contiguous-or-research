# K17 tight staircase, integrated fragment braid, and guarded compiler

Date: 2026-07-31  
Lane: K, hypothetical complete four-sector carrier  
Status: exact K17 compiler reduction and conditional construction theorems;
no K17 carrier or word is asserted

## 0. Outcome

Put

\[
 W=\binom{17}{9}=24310,
 \qquad L=W+3=24313,
 \qquad
 \Lambda=\sum_{q=1}^{8}\binom{17}{q}=65535.
\tag{0.1}
\]

The existing four-sector middle/upper theorems and the scalar staircase
budget do not yet establish a lower compiler.  Four exact facts sharpen the
missing gate.

1. An arbitrary-start depth-three schedule must pass a rank-chain condition
   in addition to its scalar loss bound.
2. At loss \(7401\), the lower compiler has zero slack: every physical lower
   cell is used and its OR map is a bijection onto the complete lower ideal.
3. For the natural one-pivot schedule this bijection is an explicit
   singleton/pair/tail-triple rainbow identity.  It is necessary and
   sufficient, together with the assumed upper-complete carrier.
4. Connecting the \(U\) shore before integration is unnecessary.  If its
   \(737\) protected fragments are inserted separately into distinct YAX
   junctions, the exact no-new-coordinate edge count is still \(6434\),
   leaving one unfilled palette slot conditional on the literal disjointness
   identity (7.3).  Compiler feasibility depends on the final chronology and
   caps, not on the earlier component partition.

The matching-first alternative is exact inside a fixed matching-closed
guarded bank: after owners and pins, its weighted quotient cuts give a
compiler contained in that bank.  Four-sector symmetry alone supplies
neither the guards nor those cuts, and the linear opening destroys the
natural geometric \(C_{15}\) action.

## 1. Arbitrary-start K17 staircase

Let \(T_0,\ldots,T_{W-1}\) be a hypothetical rank-nine carrier chronology.
Choose three omitted starts and three omitted deadlines.  In the threshold
normal form write

\[
 x_j=\alpha_j+j-1,
 \qquad y_j=\tau_j+j-1,
 \qquad 1\le j\le3,                                  \tag{1.1}
\]

where

\[
 0\le\alpha_1\le\alpha_2\le\alpha_3\le W,
 \qquad
 0\le\tau_1\le\tau_2\le\tau_3\le W,
\]

and legality is \(\tau_j\le\alpha_j\).  Chain alignment and literal middle
replay remain separate requirements.  Put

\[
 \chi=\mathbf1_{\alpha_1<\tau_2}
      +\mathbf1_{\alpha_1<\tau_3}
      +\mathbf1_{\alpha_2<\tau_3}.                    \tag{1.2}
\]

### Lemma 1.1 (exact cell budget)

The complete physical lower-cell atlas has

\[
 |\mathcal C|
 =72936-\operatorname{Loss}(\alpha,\tau),             \tag{1.3}
\]

where

\[
 \operatorname{Loss}(\alpha,\tau)
 =\sum_{j=1}^3\tau_j+3W-\sum_{j=1}^3\alpha_j+\chi.    \tag{1.4}
\]

Consequently the exact scalar gate is

\[
 \operatorname{Loss}\le7401,
 \qquad
 \Omega:=|\mathcal C|-\Lambda
         =7401-\operatorname{Loss}.                   \tag{1.5}
\]

#### Proof

The arbitrary-start P/Q identity gives

\[
 |\mathcal C|=3W+6-\ell(\alpha,\tau).
\]

For three ordered thresholds, the omitted-start boundary correction is
exactly the three crossing indicators in (1.2), which gives (1.4).
Substitute (0.1). \(\square\)

Pins remove one target and one distinct cell each, so they preserve
\(\Omega\).  They may delete candidate incidences and therefore do not
preserve Hall or common-cap feasibility.

### 1.1. Cell-chain spectrum

For \(j=1,2,3\), let \(N_j\) be the number of left endpoints whose atlas
chain has at least \(j\) cells.  Every atlas cell has length at most three,
and

\[
 |\mathcal C|=N_1+N_2+N_3.                           \tag{1.6}
\]

Direct interval counting gives

\[
\begin{aligned}
N_1={}&3+\sum_j(\alpha_j-\tau_j)
       -(\alpha_1-\tau_2)_+
       -(\alpha_2-\tau_3)_+,\\
N_2={}&(\alpha_1-\tau_2)_+
       +(\alpha_2-\tau_3)_+
       -(\alpha_1-\tau_3)_+\\
     &\quad+\mathbf1_{\tau_2\le\alpha_1}
       +\mathbf1_{\tau_3\le\alpha_2},\\
N_3={}&(\alpha_1-\tau_3)_+
       +\mathbf1_{\tau_3\le\alpha_1}.
\end{aligned}                                        \tag{1.7}
\]

The target rank sizes, from rank one through rank eight, are

\[
 17,136,680,2380,6188,12376,19448,24310.              \tag{1.8}
\]

In any lower-complete word, choose one distinct atlas witness for every
lower target.  The chosen cells with one left endpoint have distinct nested
ORs, hence distinct ranks; unused cells may duplicate when \(\Omega>0\).
After forgetting the subset labels, assigning the rank multiplicities in
(1.8) is a bipartite degree-sequence problem with chain degrees at most
three.  Gale--Ryser therefore gives exactly the rank-only dominance tests

\[
 N_1\ge24310,
 \qquad N_1+N_2\ge43758,
 \qquad N_1+N_2+N_3\ge65535.                          \tag{1.9}
\]

These inequalities are sufficient only for the rank-only relaxation, not
for labelled Boolean inclusion or common-cap feasibility.  Under scalar
feasibility, \(N_1+N_2+N_3\ge65535\) and \(N_3\le N_2\).  Hence

\[
 N_1\ge24310
 \quad\Longrightarrow\quad
 N_1+N_2\ge
 \left\lceil{65535+N_1\over2}\right\rceil
 \ge44923>43758.
\]

Moreover the complement in \([0,W)\) of
\(\bigcup_j[\tau_j,\alpha_j)\) has size

\[
 \tau_1+(\tau_2-\alpha_1)_+
       +(\tau_3-\alpha_2)_+
       +(W-\alpha_3).
\]

Since \(N_1=3+|\bigcup_j[\tau_j,\alpha_j)|\), the sharp additional
condition for rank-only chain feasibility is

\[
 \boxed{
 \tau_1+(\tau_2-\alpha_1)_+
       +(\tau_3-\alpha_2)_+
       +(W-\alpha_3)\le3.}                            \tag{1.10}
\]

It says that the three active threshold intervals
\([\tau_j,\alpha_j)\) leave at most three middle-row indices uncovered.

Scalar equality alone does not imply (1.10).  For example,

\[
 \alpha=(W,W,W),\qquad \tau=(2467,2467,2467)          \tag{1.11}
\]

has loss \(7401\) and \(65535\) cells, but only \(N_1=21846\), fewer than
the \(24310\) rank-eight targets.

## 2. Exact spectral-defect identity

Fix any legal, chain-aligned, middle-exact schedule with loss at most
\(7401\).  Let \(Q=(Q_p)_{p=0}^{L-1}\) be a nonempty word subordinate to
the schedule envelope and exact on every middle row.  For a lower target
\(S\), let

\[
 m_Q(S)=|\{J\in\mathcal C:\bigvee_{p\in J}Q_p=S\}|.   \tag{2.1}
\]

Define

\[
\begin{aligned}
H_Q&=|\{S:1\le|S|\le8,\ m_Q(S)=0\}|,\\
D_Q&=\sum_{1\le|S|\le8}(m_Q(S)-1)_+,\\
R_Q&=|\{J\in\mathcal C:
             |\bigvee_{p\in J}Q_p|\ge9\}|.
\end{aligned}                                        \tag{2.2}
\]

### Theorem 2.1 (tight spectral-defect identity)

\[
                  \boxed{H_Q=D_Q+R_Q-\Omega.}         \tag{2.3}
\]

Hence \(Q\) covers the complete lower ideal if and only if

\[
                         D_Q+R_Q=\Omega.              \tag{2.4}
\]

#### Proof

There are \(\Lambda-H_Q\) distinct lower targets present, with duplicate
excess \(D_Q\).  Thus the number of atlas cells having lower-rank value is
\((\Lambda-H_Q)+D_Q\).  The remaining \(R_Q\) cells have rank at least
nine.  Since \(|\mathcal C|=\Lambda+\Omega\), rearrangement gives (2.3).
\(\square\)

At tight loss \(7401\), \(\Omega=0\).  Therefore \(Q\) covers the complete
lower ideal if and only if

\[
 J\longmapsto\bigvee_{p\in J}Q_p                    \tag{2.5}
\]

is a bijection from \(\mathcal C\) onto all nonempty subsets of \([17]\) of
rank at most eight.  For any such lower-complete \(Q\), every cell is used;
any duplicate, rank-at-least-nine cell, or guard-dead cell is fatal.  Every
target-unit, cell-substochastic fractional matching has every cell load
exactly one.

### 2.1. Moment form

For \(A\subseteq[17]\), put

\[
 Z_A(Q)=|\{J\in\mathcal C:
                 A\subseteq\bigvee_{p\in J}Q_p\}|.   \tag{2.6}
\]

At zero slack, (2.5) is equivalent by Boolean zeta inversion to

\[
 Z_A(Q)=h_{|A|},
 \qquad
 h_a=
 \begin{cases}
 65535,&a=0,\\[1mm]
 \displaystyle\sum_{j=0}^{8-a}\binom{17-a}{j},&1\le a\le8,\\[2mm]
 0,&a\ge9.
 \end{cases}                                        \tag{2.7}
\]

The values for \(a=0,\ldots,8\) are

\[
 65535,26333,9949,3473,1093,299,67,11,1.             \tag{2.8}
\]

Thus each coordinate occurs in exactly \(26333\) cell values and each
fixed coordinate pair occurs in exactly \(9949\).  These are labelled
moment conditions for every \(A\), not merely average rank counts.

## 3. The one-pivot flat-rainbow normal form

Take the carrier-free one-pivot schedule

\[
 \alpha=(W,W,W),\qquad \tau=(0,0,7401).              \tag{3.1}
\]

It has \(\Omega=0\) and

\[
 (N_1,N_2,N_3)=(24313,24312,16910).                  \tag{3.2}
\]

There is one chain of length one, \(7402\) chains of length two, and
\(16910\) chains of length three.  Its complete lower atlas is

\[
\begin{aligned}
\mathcal C={}&\{[p,p]:0\le p\le24312\}\\
&\dot\cup\{[p,p+1]:0\le p\le24311\}\\
&\dot\cup\{[p,p+2]:7401\le p\le24310\}.
\end{aligned}                                        \tag{3.3}
\]

The middle owner intervals have length three before row \(7401\) and
length four afterwards.

### Definition 3.1 (K17-FRS\((T)\))

The chronology \(T\) has a **flat-rainbow section** if there are nonempty
sets \(Q_0,\ldots,Q_{24312}\subseteq[17]\) such that

\[
 Q_i\cup Q_{i+1}\cup Q_{i+2}=T_i
 \quad(0\le i<7401),                                  \tag{3.4}
\]

\[
 Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}=T_i
 \quad(7401\le i<24310),                              \tag{3.5}
\]

and the disjoint multiset union

\[
\begin{aligned}
 &\{Q_p:0\le p\le24312\}\ \dot\cup\\
 &\{Q_p\cup Q_{p+1}:0\le p\le24311\}\ \dot\cup\\
 &\{Q_p\cup Q_{p+1}\cup Q_{p+2}:7401\le p\le24310\}
\end{aligned}                                        \tag{3.6}
\]

is exactly

\[
                 \{S\subseteq[17]:1\le|S|\le8\}.    \tag{3.7}
\]

### Theorem 3.2 (exact K17 compiler normal form)

If \(T\) is upper-complete by consecutive chronology blocks, then
K17-FRS\((T)\) is necessary and sufficient for a universal nonempty word
which realizes \(T_i\) on the prescribed owner intervals of schedule
(3.1).  Consequently it proves
\(\nu(17)=24313\) when combined with the known lower bound.

#### Proof

Equations (3.4)--(3.5) are exactly middle replay.  Equation (3.3) is the
complete lower-cell atlas, so (3.6)--(3.7) are exactly lower completeness by
Theorem 2.1.  Chain alignment makes the union of the physical intervals of
any consecutive middle-row block an interval; hence every assumed upper
witness transfers to \(Q\).  Conversely, every lower witness of a universal
word must avoid containing a whole rank-nine owner interval and therefore
lies in (3.3).  Zero slack forces the bijection (3.6). \(\square\)

Immediate consequences of K17-FRS are:

- all letters \(Q_p\) are distinct lower targets;
- every singleton target occurs as one singleton letter;
- adjacent letters are incomparable;
- for every tail triple, each endpoint contributes a bit absent from the
  opposite adjacent pair; and
- exactly \(24310\) of the \(24313\) maximal same-start cells have rank
  eight; precisely three start chains have a lower-rank top.

The last item is the **top-port condition**.  Any construction intending to
reuse a four-sector carrier's particular rank-eight edge occurrences as
ports must place them on physical terminal cells.  Abstract palette equality
or lower-q1 rainbowness without occurrence-level top-port alignment is
insufficient.  The condition is necessary but is not, by itself, a lower
compiler.

## 4. Four-sector ledgers

Write the new coordinates as \(x,y\).  The complete lower target ideal
splits by \(S\cap\{x,y\}\) as

\[
 (n_{00},n_{10},n_{01},n_{11})
 =(22818,16384,16384,9949).                           \tag{4.1}
\]

At rank \(q\), the split is

\[
\left(
 \binom{15}{q},
 \binom{15}{q-1},
 \binom{15}{q-1},
 \binom{15}{q-2}
 \right).                                            \tag{4.2}
\]

Here and below \(\binom{15}{j}=0\) outside \(0\le j\le15\).

In particular, rank eight has signature vector

\[
 (6435,6435,6435,5005),                              \tag{4.3}
\]

the pair-complement of the four owner-sector sizes
\((5005,6435,6435,6435)\).  After a jointly legal pinning of the complete
rank-eight deck, the residual signature demands are

\[
 (16383,9949,9949,4944),                             \tag{4.4}
\]

of total \(41225\).  Pin contraction preserves \(\Omega\).  At zero slack,
the residual instance is again square and every residual cell must be used.

For a zero-slack flat-rainbow section, the exact \((x,y)\)-signature counts
of cell values are necessarily (4.1).  More generally, the labelled moment
conditions (2.7) are stronger than all four signature totals.

## 5. Guarded orbit-flow theorem

Fix any chain-aligned, middle-exact legal schedule of loss at most \(7401\),
a common-cap-safe partial pin matching \(M_0\), and rebuild the residual
candidate graph after all pin caps.  Call a residual bank \(H\)
**matching-closed guarded** when every target-saturating matching contained
in \(H\) simultaneously preserves every position, middle, protected-pin,
and selected-lower trace.  Permanent witness positions or exclusion of the
complete minimal conflict clutter certify this property; pairwise edge
compatibility alone does not in general certify it.

Assume a finite group \(\Gamma\) preserves \(H\).  Let
\(\mathcal L_\alpha\) and \(\mathcal C_\beta\) be its target and cell
orbits.

### Theorem 5.1 (K17 guarded orbit compiler inside a fixed bank)

The bank \(H\) contains a target-saturating residual matching, and every such
matching is a literal common cap, if and only if the weighted quotient cuts

\[
 \boxed{
 \sum_{\alpha\in A}|\mathcal L_\alpha|
 \le
 \sum_{\beta\in N_H(A)}|\mathcal C_\beta|
 \quad(A\text{ a target-orbit set})}                 \tag{5.1}
\]

hold.  Together with the fixed middle-exact schedule and the hypothetical
upper-complete carrier, this gives a universal word of length \(24313\).
The equivalence is only for matchings contained in \(H\), not for an
unrestricted compiler outside this bank.

#### Proof

Every nonempty orbit block is biregular.  A capacitated flow with target
orbit supplies \(|\mathcal L_\alpha|\) and cell-orbit capacities
\(|\mathcal C_\beta|\) exists exactly under (5.1).  Distribute its block
mass uniformly over physical edges.  This gives a fractional matching;
bipartite integrality gives an integral matching.  The complete guard system
makes every such matching a common cap.  The maximal-cap word realizes the
middle and pinned rows, and chain alignment transfers all upper witnesses.
\(\square\)

At \(\Omega=0\), total target and cell mass are equal.  Hence every
cell-orbit inequality in the quotient flow is an equality.  On the full
target cut, no physical cell may become guard-dead.  For \(\Omega>0\), the
full-cut guard-deletion budget is only \(\Omega\); proper target cuts still
require (5.1) and do not follow from this scalar budget.

### 5.1. Sector-complete compression

If every residual target orbit of one new-bit signature has the same
cell-orbit neighbourhood \(B_R\), call the quotient
**sector-complete**.  Put

\[
 n_R^{\rm res}
 =n_R-|\operatorname{dom}(M_0)\cap\mathcal L_R|.
\]

Then (5.1) reduces exactly to the fifteen nonempty signature cuts

\[
 \sum_{R\in A}n_R^{\rm res}
 \le
 \sum_{\beta\in\bigcup_{R\in A}B_R}|\mathcal C_\beta|
 \qquad
 (\varnothing\ne A\subseteq\{00,10,01,11\}).         \tag{5.2}
\]

For \(M_0=\varnothing\), the distinct pair demands are

\[
 39202,32767,32768,26333,                             \tag{5.3}
\]

and the distinct triple demands are

\[
 55586,49151,42717;                                   \tag{5.4}
\]

the all-signature demand is \(65535\).  These cuts are sufficient only
under the stated sector-complete guarded support.  Sector cardinalities by
themselves do not imply it.

### 5.2. Natural \(C_{15}\) bulk census

Let \(C_{15}\) rotate the old coordinates and fix \(x,y\).  The free target
orbit counts and nonfree physical masses are

\[
\begin{array}{c|rrrr}
 &00&10&01&11\\ \hline
\text{free orbit count}&1520&1091&1091&662\\
\text{nonfree target mass}&18&19&19&19.
\end{array}                                          \tag{5.5}
\]

#### Proof

A nonconstant binary word of length fifteen has orbit size \(3,5\), or
\(15\).  In every signature, the allowed old ranks contain one size-three
orbit of old weight five and three size-five orbits, one of old weight three
and two of old weight six.  This accounts for mass \(18\).  The three
signatures containing a new coordinate also contain the fixed empty old
set, adding one.  Subtracting these masses from (4.1) and dividing by
fifteen gives (5.5). \(\square\)

Thus there are \(4364\) free target orbits and \(75\) exceptional targets
in \(19\) short orbits.  Conditional on a full, unpinned bank whose
\(65535\) cells decompose into \(4369\) free cell orbits, it is enough to
absorb the \(75\) exceptional targets into five *complete* cell orbits by
guarded weighted flow and then match the residual \(4364\times4364\) free
quotient.  Under sector-complete support the latter uses the free-orbit
demand vector

\[
                    (1520,1091,1091,662).             \tag{5.6}
\]

This is a concrete additional bank invariant, not a consequence of the
target census or the four-sector construction.  With pins, all orbit masses
and the exceptional flow must be recomputed.

### Lemma 5.2 (linear opening destroys geometric \(C_{15}\))

For the one-pivot schedule, any permutation of physical positions preserving
the complete interval-cell atlas is the identity or reversal.  Hence an
odd-order \(C_{15}\) coordinate rotation cannot act nontrivially on this
linear atlas.

#### Proof

All owner intervals have length three or four.  Therefore every singleton
and every adjacent pair is a lower cell.  The two-element cells are exactly
the edges of the path on positions \(0,\ldots,24312\).  Any atlas-preserving
position permutation is a path automorphism, hence identity or reversal.
An odd-order subgroup of this two-element automorphism group is trivial.
\(\square\)

Accordingly, (5.5)--(5.6) can be used only after an explicit boundary
absorber restores a free bulk action, or through an accidental automorphism
of the guarded incidence graph not induced by physical positions.

## 6. Matching-first shift alternative

Suppose an exceptional guarded absorber has been fixed and a perfect
matching of the remaining free \(C_{15}\) target and cell orbit nodes has
been chosen.  In paired orbit block \(a\), let \(D_a\subseteq C_{15}\) be
the allowed differences.  Choosing one shift \(\Delta_a\in D_a\) produces a
physical perfect matching and eliminates all same-cell conflicts before the
common-cap analysis.

After every pin and unary conflict is contracted, assume a permanent owner
orientation eliminates empty-position conflicts.  The remaining depth-three
conflicts have arities \(2,3,4\).  Let
\(\widetilde D_j(a,\delta)\) count the shift-consistent arity-\(j\) events
which prescribe an alternative to retained value \((a,\delta)\).

### Theorem 6.1 (C15 shift-pressure compiler)

If \(|D_a|\ge M>1\) and, for some \(1<c<M\),

\[
 \prod_{j=2}^{4}
 \left(1-(c/M)^j\right)^{\widetilde D_j(a,\delta)}
 \ge {1\over c}                                      \tag{6.1}
\]

for every retained shift value, then some shift matching is a literal
common-cap compiler.

For the full natural domain \(M=15\), taking \(c=2\) gives the explicit
additive sufficient test

\[
 {4\over221}\widetilde D_2
 +{8\over3367}\widetilde D_3
 +{16\over50609}\widetilde D_4
 \le\log2.                                           \tag{6.2}
\]

If \(\widetilde D_j\le D^{j-1}\), (6.2) passes for \(D\le9\); it does not
certify \(D=10\).  This failure is not a no-go.

#### Proof

Orbit shifts preserve the already chosen physical perfect matching.  A
shift-consistent arity-\(j\) event has probability at most \(M^{-j}\).
Give it lopsided-LLL charge \((c/M)^j\).  Atomic events are adjacent only
when they prescribe different values of a shared shift variable, so (6.1)
is the candidate-opposition product condition.  Inequality (6.2) is
\(-\log(1-u)\le u/(1-u)\) with \(u=(2/15)^j\). \(\square\)

After fixing the exceptional absorber, recompute the complete residual
conflict clutter.  A conflict with no residual variable rejects the
absorber; one residual variable forbids a shift value; and conflicts with
two or more residual variables remain in the corresponding
\(\widetilde D_j\).  Only after unary deletion may the value \(M\) be
quoted.  Without a permanent owner, empty-position conflicts can have arity
up to six at depth three, so the \(j=5,6\) terms must also be included and
neither the displayed \(j\le4\) test nor the \(D\le9\) calibration applies.

## 7. The integrated 737-fragment braid

Let \({\cal U}\) be the authenticated partition of the \(5005\) no-new-
coordinate owners into \(f=737\) protected paths.  It has \(5005-f=4268\)
internal Johnson edges with distinct old rank-eight colours.  Assume its
internal interval bank is upper-complete and its internal short-run data are
carried with each oriented fragment.

### Lemma 7.1 (provenance erasure)

Two construction histories with the same final ordered rank-nine chronology
\(T\), P/Q schedule, baseline positional caps, and pin map give identical
lower Hall and common-cap systems.  In particular, those systems are
independent of whether the \(U\) owners were first connected or remained in
\(737\) pieces until integration.

#### Proof

The cell atlas is determined by the starts and deadlines.  Its envelope,
candidate incidences, and minimal cap-conflict clutter are determined by the
final owner intervals \(T_i\) and the pins.  None of these definitions
contains an intermediate component label.  The same final data therefore
give the same compiler instance. \(\square\)

This does not say that arbitrary fragment insertions work.  Their final
seams can change the Johnson palette, upper witnesses, coordinate runs,
envelopes, and caps; those changes are visible through \(T\).

### 7.1. Exact no-new-coordinate ledger

The YAX macro backbone has \(1430-1=1429\) junctions whose lower colour has
signature \(00\).  Insert each of \(f\) whole \(U\)-fragments into a
distinct such junction.  Each insertion deletes one old junction and adds
two \(U\)--exterior seams.  Hence the final path has

\[
 (1429-f)+(5005-f)+2f=6434                         \tag{7.1}
\]

edges of signature \(00\), independently of \(f\).  At \(f=737\), these
are

\[
 692\text{ retained YAX seams}
 +4268\text{ internal }U\text{ edges}
 +1474\text{ cross seams}.                          \tag{7.2}
\]

For comparison, first connecting \(U\) and then inserting it once gives
\(1428+5004+2=6434\).  Thus prior connectedness changes no q1 slot count.

The count is not yet a colour theorem.  The exact local ledger required of
an integrated braid is the disjoint palette identity

\[
 \binom{[15]}8
 =C_U\ \dot\cup\ C_{\rm YAX}\ \dot\cup\ C_{\rm cross}
  \ \dot\cup\ \{c_\star\},                         \tag{7.3}
\]

with sizes \(4268,692,1474,1\).  Only under this identity is \(c_\star\) the
unique missing colour.  Equivalently, the \(2167\) old colours
unused internally by \(U\) must be used bijectively by the \(692+1474\)
retained/cross seams, except for the unique boundary colour \(c_\star\).
The other three signature decks must pass their own exact local ledgers.

### 7.2. Collar charge is orphan-cell charge

For a schedule with atlas \({\cal C}\) and surplus \(\Omega\), reserve a
set \(K\subseteq{\cal C}\) of collar cells.  Suppose a target- and
cell-injective collar pin family \(\Pi_K\) assigns
\(p=|\Pi_K|\) distinct lower targets to cells of \(K\).  After contracting
those targets and reserving all of \(K\), the
exact residual scalar surplus is

\[
 \boxed{\Omega_{\rm res}=\Omega-(|K|-p).}            \tag{7.4}
\]

Thus the charge is the number of orphan reserved cells, not the number of
seams.  In particular, at one-pivot zero slack every reserved cell must
simultaneously discharge a distinct lower target.

If a collar instead quarantines every lower cell crossing physical cuts
\(B\subseteq\{1,\ldots,24312\}\), put \(\kappa(B)=|K|\).  In the one-pivot
atlas (3.3), with a cut \(b\) lying between positions \(b-1,b\),

\[
 \kappa(B)=|B|+
 \left|\left\{p\in[7401,24310]:
       \{p+1,p+2\}\cap B\ne\varnothing\right\}\right|. \tag{7.5}
\]

Consequently one cut costs between one and three lower cells, and every
nonempty pure quarantine is impossible at one-pivot zero slack.  If an
implementation assigns separate entry and exit physical cuts to all
\(737\) insertions, then \(|B|\le1474\) and the crude bounds are

\[
 \kappa(B)\le4422,
 \qquad
 \#\{\text{crossing windows of lengths }2,3,4\}\le8844. \tag{7.6}
\]

The length-four windows in the second count are owner windows, not lower
cells.  More importantly, row interfaces need not be quarantined physical
cuts at all: a collar has zero orphan charge only when every reserved cell
is paired with a distinct jointly safe lower target.

### 7.3. Physical rank-eight slot basis

Let \(\Pi_8=\{(S,J_S):|S|=8\}\) assign each rank-eight target to one
distinct physical atlas cell.  Its \(24309\) path-edge colours come from the
four local ledgers, and \(c_\star\) uses one separately proved non-edge top
port.  This port is a boundary cell only if the construction proves that
placement.  The q1 ledger does not itself construct \(\Pi_8\): a
**physical** slot basis additionally requires an occurrence-to-cell map,
distinct cells, and joint cap safety.

Require \(K\) to be disjoint from the cells of \(\Pi_8\), and put
\(\Pi_{\rm all}=\Pi_8\dot\cup\Pi_K\).  Require this union to be injective
on both targets and cells.  Let \(\Gamma_p\) be the envelope after every
baseline positional and pre-existing cap, equal to the unpinned \(E_p\) when
there are no such caps.  Define

\[
 \Gamma_p^{\Pi_{\rm all}}
 =\Gamma_p\cap
   \bigcap_{(S,J)\in\Pi_{\rm all}:\,p\in J}S.       \tag{7.7}
\]

Call \(\Pi_{\rm all}\) **collar-absorbed** when

\[
 \Gamma_p^{\Pi_{\rm all}}\ne\varnothing
       \quad\text{for every }p,                     \tag{7.8}
\]

\[
 \bigvee_{p\in I_i}\Gamma_p^{\Pi_{\rm all}}=T_i
       \quad\text{for every owner row }i,           \tag{7.9}
\]

and

\[
 \bigvee_{p\in J}\Gamma_p^{\Pi_{\rm all}}=S
       \quad\text{for every }(S,J)\in\Pi_{\rm all}. \tag{7.10}
\]

Separate per-junction cap checks do not imply (7.8)--(7.10) when collars
overlap.

### Theorem 7.2 (integrated braid and local-ledger compiler GO)

Suppose the fragment-integrated chronology satisfies all of the following.

1. It is one Johnson Hamilton path on the \(24310\) owners, and its four
   local rank-eight ledgers include (7.3).  This is a provenance check;
   clause 4 is the separate physical occurrence-to-cell requirement.
2. It has a legal, chain-aligned, middle-exact schedule with
   \(\operatorname{Loss}+|K|-|\Pi_K|\le7401\).
3. Every upper target has a final consecutive witness; fragment-internal
   upper witnesses may be used unchanged because every fragment remains one
   contiguous oriented block.
4. The complete target- and cell-injective family
   \(\Pi_{\rm all}=\Pi_8\dot\cup\Pi_K\) is collar-absorbed.
5. After contracting these balanced pins, a matching-closed guarded
   residual bank satisfies physical Hall, or satisfies (5.1) for a group
   preserving the *final* bank.

Then maximal-cap materialization gives a universal word of length \(24313\).
No connectedness hypothesis on the pre-insertion \(U\) bank is needed.

#### Proof

The first four clauses give one final owner chronology, exact middle replay,
all upper witnesses, and a jointly legal complete rank-eight preassignment.
By (7.4), the residual full cut has nonnegative capacity.  The last clause
and Theorem 5.1 give an integral residual common-cap matching.  Equations
(7.8)--(7.10) and matching-closed guarding make the maximal word reproduce
the owners and every pinned/residual lower target.  Chain alignment transfers
the upper witnesses. \(\square\)

At \(\Omega=0\), immediately after contracting \(\Pi_8\) and before any
additional collar reservation, there remain exactly

\[
 65535-24310=41225                                 \tag{7.11}
\]

residual targets and cells.  Any further unpaired discarded cell makes the
full Hall cut deficient.

### 7.4. The staircase is final-order local, not seam-additive

Let \(\rho_j(T)\) be the latest start of an interior coordinate run of
length at most \(j\), with value zero when none exists.  Internally safe
fragments reduce the run audit to runs touching new interfaces, but the
interfaces must be composed in their actual order: a short fragment can
make one run cross two or three successive seams.  The exact summary
\(\Sigma_3\) records fragment length and, for every coordinate, capped
initial/terminal positive-run lengths, the all-one flag, and the relative
internal maxima \(\rho_1,\rho_2,\rho_3\).  These records compose
associatively and give the exact final frontier.  The internal maxima may be
omitted only for internally depth-three-safe fragments.

The literal one-pivot schedule passes its run test exactly when

\[
 \rho_1=\rho_2=0,
 \qquad \rho_3\le7401.                              \tag{7.12}
\]

A run/scalar-feasible zero-slack tail-start schedule satisfying the
rank-only dominance condition exists exactly when

\[
 \rho_1\le3,
 \qquad \rho_1+\rho_2+\rho_3\le7401.               \tag{7.13}
\]

Without the rank-only condition, scalar zero slack needs only
\(\rho_1+\rho_2+\rho_3\le7401\).  In the arbitrary-start form, put
\(\delta_j=W-\alpha_j\) and require legality
\(\tau\le\alpha\), \(\tau\ge\rho^\delta(T)\), and
\(\operatorname{Loss}\le7401\), with equality for zero slack; add chain
alignment and (1.10) when rank-chain feasibility is claimed.  Envelope
nonemptiness remains necessary for a literal word.  Thus \(1474\) safe
seams can cost zero, while one late singleton run can exceed the whole
budget.  The budget is automatic under the stronger local-to-global
certificate that every oriented fragment is internally depth-three safe and
the composed seam state creates no interior run of length at most three.
This gives a loss-zero run/scalar schedule; four-local envelope nonemptiness
is still required.  Johnson legality or pairwise endpoint checks alone do
not give this certificate.

## 8. The balanced cap-two plus two-factor core

The proposed balanced core can be stated without ambiguity by recording its
fixed degree deficit.  Let \(P_0\) consist of \(1430\) vertex-disjoint
nontrivial paths spanning all \(5005\) \(U\)-owners and exactly \(1430\)
owners in each of \(A,X,Y\), with the remaining \(15015\) owners treated as
isolated components.  Assume it is a simple spanning linear forest and its
unused owner degrees are

\[
 (D_A,D_X,D_Y,D_U)=(11440,10725,10725,0).           \tag{8.1}
\]

Assume also that its used q1 colours are all \(6435\) colours of signature
\(00\), plus \(715\) colours of each of signatures \(10,01\).  The residual
selection

\[
 5005\ AA,\qquad 5005\ XX+715\ AX,\qquad
 5005\ YY+715\ AY                                  \tag{8.2}
\]

then has endpoint contribution

\[
 A:2(5005)+715+715=11440,\quad
 X:2(5005)+715=10725,\quad
 Y:10725,                                           \tag{8.3}
\]

has the correct remaining q1 *slot counts*.  Require additionally the
literal complement-rainbow palette identity

\[
 5005\text{ of signature }11,qquad
 5720\text{ of signature }10,qquad
 5720\text{ of signature }01.                       \tag{8.4}
\]

Equivalently, \(P_0\) contributes degree vector

\[
 (1430,2145,2145,10010)                            \tag{8.5}
\]

and colour vector \((6435,715,715,0)\), while the residual blocks are
required to contribute the disjoint complement
\((0,5720,5720,5005)\).  Thus (8.1), rather than the raw edge totals alone,
is the exact sector-degree audit, while (8.4) is a separate rainbow
hypothesis.  The literal degree condition is vertexwise:

\[
             \deg_R(v)=2-\deg_{P_0}(v).             \tag{8.6}
\]

The \(AA\) block is the cap-two factor, while the \(XX/AX\) and \(YY/AY\)
blocks are the two lower-rainbow factor problems.  Regard the \(1430\)
nontrivial paths and the \(15015\) untouched \(A/X/Y\) owners as a spanning
linear forest with \(16445\) components.  After contracting these components,
a degree-correct residual selection is 2-regular.  Its union with \(P_0\) is
one Hamilton cycle if and only if this contracted residual graph is
connected (with loops and parallel edges carrying their usual multigraph
degrees).  The block counts alone do not imply that monodromy.  Opening one
edge then gives a Hamilton path, and its omitted colour must be assigned to
a separately proved non-edge physical top port.

### Corollary 8.1 (common-cap criterion for the balanced core)

The balanced core gives a length-\(24313\) compiler provided that one joint
choice of the cap-two block, both lower-rainbow blocks, one-cycle monodromy,
and the opened edge satisfies all five clauses of Theorem 7.2 for the
resulting final chronology.

This criterion cannot be checked separately in the three factor blocks.
Their biregularity concerns owner degrees and q1 colours; residual compiler
Hall concerns \(41225\) labelled targets versus overlapping P/Q cells after
all rank-eight pins have jointly capped the word.  A generic product of the
cap-two and PBBS factors therefore supplies no automatic common cap.  It
does supply the correct q1 slot basis once (8.1)--(8.4), one-cycle
monodromy, and the physical top-port realization are proved.

If, after those joint pins, the *final* guarded residual bank is
sector-complete, its singleton signature demands are

\[
 (16383,9949,9949,4944).                            \tag{8.7}
\]

The distinct two-signature cuts have demands

\[
 26332,21327,19898,14893,                            \tag{8.8}
\]

the distinct three-signature cuts have demands

\[
 36281,31276,24842,                                  \tag{8.9}
\]

and the full cut has demand \(41225\).  Weighted cell-orbit capacities on
the right of these fifteen cuts give the explicit common-cap criterion in
the sector-complete case.  Without identical guarded neighbourhoods within
each signature, all physical Hall cuts remain necessary.

The currently available lower-rainbow 2-factor verifies the q1 layer but
has \(4413\) upper-q1 holes and a large short-run frontier.  It therefore
fails the carrier hypotheses of Theorem 7.2 before compilation.  Everything
below is conditioned on a future upper-aware, resident residual factor.

### Theorem 8.2 (pair-choice-conditioned maximal-cap criterion)

Let \(G\) be the union of the fixed path bank and the allowed Johnson edges
in the five residual blocks.  For each owner \(v\), let

\[
 {\cal A}_v=
 \{a\subseteq\delta_G(v): |a|=2,
        \ \delta_{P_0}(v)\subseteq a\},
\]

and introduce binary pair variables \(y_{v,a}\).  Fix \(x_e=1\) on every
retained path-bank edge.  Impose one-hot choice at every owner and endpoint
consistency on every residual edge \(e=vw\):

\[
 \sum_{a\in{\cal A}_v}y_{v,a}=1\quad(v\in V(G)),
 \qquad
 x_e=\sum_{a\in{\cal A}_v:\,a\ni e}y_{v,a}
     =\sum_{a\in{\cal A}_w:\,a\ni e}y_{w,a}
       \quad(e=vw\in E(G)\setminus E(P_0)).         \tag{8.11}
\]

Together with the fixed bank, impose the literal vertex degrees (8.6), one
selected edge of each rank-eight colour, every required upper-edge colour,
and connected contracted monodromy.  Fix an opened edge, orientation, and a
legal schedule for any pair assignment \(y\) passing the full upper and
residence audits.  These choices determine the ordered chronology, baseline
envelopes \(\Gamma_p(y)\), with the standard owner subordination

\[
 \Gamma_p(y)\subseteq\bigcap_{i:\,p\in I_i}T_i.
\]

The complete unary provider domain for a lower target \(S\) is

\[
 {\cal P}^{\max}_y(S)=
 \left\{J\in{\cal C}:
   \Gamma_p(y)\cap S\ne\varnothing\ (p\in J),\quad
   S\subseteq\bigvee_{p\in J}\Gamma_p(y)
 \right\}.                                         \tag{8.11a}
\]

Use \({\cal P}_y(S)={\cal P}^{\max}_y(S)\) for a global criterion.  A
narrower physical slot architecture is also allowed, including restriction
of rank-eight \(S\) to selected-pair or opened-port occurrences, but then
the theorem is necessary and sufficient only among compilers respecting
that declared architecture.  Every preassigned pin must either remain as a
fixed provider variable or already be intersected into \(\Gamma(y)\) and
removed with its target and cell.

There is a literal lower common-cap compiler respecting these provider
domains for this fixed \(y\), opening, orientation, and schedule if and only
if binary provider variables \(z_{S,J}\),
\(J\in{\cal P}_y(S)\), satisfy

\[
 \sum_{J\in{\cal P}_y(S)}z_{S,J}=1
       \quad\text{for every lower target }S,         \tag{8.12}
\]

\[
 \sum_{S:J\in{\cal P}_y(S)}z_{S,J}\le1
       \quad\text{for every atlas cell }J,           \tag{8.13}
\]

and, with

\[
 C_p(y,z)=\Gamma_p(y)\cap
  \bigcap_{S,J:\,z_{S,J}=1,\ p\in J}S,             \tag{8.14}
\]

where an empty target-cap intersection is \([17]\).

the exact cap equations

\[
 C_p(y,z)\ne\varnothing,                            \tag{8.15}
\]

\[
 \bigvee_{p\in I_i}C_p(y,z)=T_i,                    \tag{8.16}
\]

\[
 z_{S,J}=1\quad\Longrightarrow\quad
 \bigvee_{p\in J}C_p(y,z)=S.                        \tag{8.17}
\]

Equations (8.15), (8.16), and (8.17) range over every position, owner row,
and provider variable respectively.

#### Proof

Necessity follows by choosing one witness cell for each lower target in a
literal word.  Distinct targets cannot use the same cell value.  Intersecting
all owner, positional, and chosen target caps gives (8.14); maximalization
cannot delete a witnessed bit and cannot add a bit outside any selected
target or owner, so (8.15)--(8.17) follow.  Conversely, the nonempty word
\(Q_p=C_p(y,z)\) reproduces every owner and every chosen lower target by
(8.16)--(8.17).  The assumed chain alignment transfers the already audited
upper witnesses. \(\square\)

This criterion is finite and exact, not a generic Hall relaxation.  It has
a compact Boolean form.  For every bit \(b\), introduce a survival literal

\[
 r_{p,b}\ \longleftrightarrow\
 [b\in\Gamma_p(y)]\ \wedge\!
 \bigwedge_{S,J:\,p\in J,\ b\notin S}\neg z_{S,J}.  \tag{8.18}
\]

Then (8.15) is \(\bigvee_b r_{p,b}\), (8.16) requires
\(\bigvee_{p\in I_i}r_{p,b}\) for each \(b\in T_i\), and (8.17) requires

\[
 z_{S,J}\Longrightarrow
 \bigvee_{p\in J}r_{p,b}\qquad(b\in S).             \tag{8.19}
\]

Tseitin expansion gives an equisatisfiable CNF for fixed \(y\); a joint
\(y,z\) encoding additionally uses activation implications
\(z_{S,J}\Rightarrow[J\in{\cal P}_y(S)]\) and encodes the induced chronology
and envelopes.  At one-pivot zero slack, after the \(24310\) rank-eight
providers are fixed injectively on distinct cells, incorporated into the
baseline caps, and contracted with no orphan reservation,
(8.12)--(8.13) reduce to an exact \(41225\)-by-\(41225\) residual matching
with the same cap clauses.  Ordinary Hall becomes sufficient only after
restricting this system to a matching-closed guarded bank.

The \(7401\) staircase is likewise not automatic from (8.2).  If the fixed
paths are internally depth-three safe, carry \(\Sigma_3\) through the
selected factor connectors.  Opening a cycle edge creates no new interior
short run; it only makes every run crossing that edge a boundary run.  Full
composed depth-three safety gives \(\rho=0\) and hence a loss-zero run/scalar
schedule.  In the Johnson Hamilton setting, every intersection of at most
four consecutive owners has rank at least six, so envelope nonemptiness is
then automatic.  If the *full composed cyclic trace*, rather than merely
each connector checked pairwise, avoids \(010\) and \(0110\), then
\(\rho_1=\rho_2=0\); the exact remaining one-pivot gate is
\(\rho_3\le7401\).

There are \(16445\) contracted components and \(16445\) residual edges.
After opening one residual edge, the path retains \(16444\) inter-component
connectors.  If each were charged as a distinct aligned pure-quarantine cut,
then already

\[
 \kappa(B)\ge16444>7401,                            \tag{8.20}
\]

while the crude upper bounds would be \(49332\) lower cells and \(98664\)
windows of lengths two through four.  Thus even a loss-zero schedule cannot
pay one orphan cell per connector.  Almost every residual join must be
transparent or balanced by a distinct jointly legal lower-target pin.

## 9. Sharp implication boundary

Even a symmetric marginal perfect matching, permanent owners, and
depth-three interval geometry do not imply a common cap.  For
example, take one four-position rank-nine middle row containing a fragile
bit \(a\), a permanent owner \(o\), four private bits, and three padding
bits.  Join four singleton cells completely to four distinct targets
\(\{o,x_i\}\).  Every incidence is individually legal and the marginal
graph is \(K_{4,4}\), but every perfect matching caps all four positions by
targets omitting \(a\), so the middle row fails.  This is an abstract
compiler obstruction, not a PBBS-specific no-go.

This abstract example refutes inference from those coarse compiler
properties.  It is not a counterexample satisfying every hypothesis of a
complete K17 four-sector carrier.  The exact proved boundary is the
following.

1. **Exact terminal condition:** K17-FRS\((T)\) is necessary and sufficient
   for the fixed one-pivot schedule.  More generally, once a middle-exact
   word \(Q\) is supplied, \(D_Q+R_Q=\Omega\) is equivalent to lower
   completeness.  These are terminal identities, not noncircular carrier
   invariants.
2. **Necessary first shell:** the complete physical rank-eight top-port
   basis is necessary at zero slack.  It is not sufficient for the lower
   ranks.
3. **Noncircular sufficient route:** a post-opening matching-closed guarded
   bank satisfying physical Hall or the exact quotient cuts (5.1), with the
   \(75\)-target short-orbit absorber handled literally if the natural
   \(C_{15}\) bulk is used.
4. **Alternative sufficient route:** a quotient perfect matching and the
   full opposing profile (6.1) after owners, absorber contraction, and unary
   deletion.

The currently proved four-sector ownership, upper-completeness, q1, and
\(\Delta=7401\) statements do not establish clauses 1, 3, or 4.  PBBS
canonical witness load is an upper bound on collisions, not a lower guarded
degree or an orbit-flow certificate.  No logical no-go is claimed for a
hypothetical stronger four-sector construction.

## 10. Sources and scope

The proof uses the exact arbitrary-start P/Q identity, maximal-common-cap
theorem, guarded-Hall/orbit-flow theorem, and matching-supported atomic LLL
from:

- `MATH_THEOREM_ODD_EVEN_REROOT_PINNED_COMMON_CAP_COMPILER_20260731.md`;
- `MATH_AUDIT_MONOTONE_DEADLINE_RUN_STAIRCASE_ARBITRARY_STARTS_20260731.md`;
- `MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`;
- `MATH_THEOREM_UNIFORM_COMMON_CAP_ORBIT_FLOW_AND_PRODUCT_LLL_BARRIER_20260731.md`;
- `MATH_THEOREM_K_COMMON_CAP_ATOMIC_PRESSURE_AND_CUT_DUAL_20260731.md`;
- `MATH_THEOREM_AD_K17_K15_FOUR_SECTOR_FACTOR_AND_RETHREAD_GATES_20260731.md`;
- `MATH_THEOREM_A_K17_UYAX_ARBITRARY_START_STAIRCASE_20260731.md`; and
- `MATH_THEOREM_R_K17_PBBS_GUARDED_ENDPOINT_LADDER_AND_ALTERNATING_SPLICE_20260731.md`.

No finite search and no K16 collar work is used.  The four-sector carrier is
hypothetical throughout.
