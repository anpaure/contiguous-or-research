# Fixed-path generalized Pascal braid: exact AA cuts and the first chronology escape

Date: 2026-07-29  
Lane: H  
Status: theorem and solver-free structural obstruction; no full-`q1`
chronology repair is claimed

The frozen parent path is

```text
scratch/k14_common_colour_3opt_best_20260729.json
SHA-256 eeccbd6be6edeba88a5d953a1f543c8f77895bbbec0e6ab0fd4eadb9e05af546
```

The purpose of this note is to separate three different facts which should
not be conflated:

1. the AA projection on the frozen path has an exact coloured-cut
   description;
2. that description already gives a hand proof that hard distinguished-
   coordinate residence is impossible;
3. changing the parent chronology may remove the obstruction, but lower
   support alone does not provide the cross/BB controller required by full
   `q1`.

## 1. Exact AA projection

Let

\[
 P=(T_0,\ldots,T_{N-1}),\qquad N=\binom{14}{7}=3432,
\]

and put \(M=N-1=3431\).  Edge positions are \(0,\ldots,M-1\), and

\[
 \gamma_i=T_i\cap T_{i+1}\in\binom{[14]}6,
 \qquad
 F_X=\{i:\gamma_i=X\}.
\]

Let \(x_i=1\) mean that edge \(T_iT_{i+1}\) is selected in the AA
forest, and let

\[
 C=\{i:x_i=0\}
\]

be its cut set.

### Theorem 1.1 (coloured-cut characterization)

The AA lower-rainbow equations together with the projected A-owner degree
condition are equivalent to

\[
 |C\cap F_X|=|F_X|-1
 \quad\text{for every }X\in\binom{[14]}6,                 \tag{1.1}
\]

\[
 0,M-1\notin C,                                           \tag{1.2}
\]

and

\[
 \{i,i+1\}\nsubseteq C\quad(0\le i<M-1).             \tag{1.3}
\]

Equivalently, one retains exactly one representative of every colour
fibre, the retained positions form a vertex cover of the path on edge
positions, and the two endpoint edges are retained.

Every solution of the complete generalized-Pascal equations (2.1)--(2.6)
projects to such a cut set.  Conversely, (1.1)--(1.3) reconstruct the AA
forest and its aggregate endpoint/interior loads, but do **not** by
themselves imply a physical cross/BB completion at the B owners.

#### Proof

The AA lower equation is

\[
 \sum_{i\in F_X}x_i=1,
\]

which is exactly (1.1).  At an internal A owner \(T_j\), its AA degree is

\[
 d_A(T_j)=x_{j-1}+x_j.
\]

Eliminating the cross and BB lower loads from equations (2.2)--(2.3) gives

\[
 d_A(T_j)=1+Y_{T_j},\qquad Y_{T_j}\in\{0,1\}.
\]

Thus \(d_A(T_j)\ge1\), which is (1.3).  At the two path endpoints the same
condition is exactly (1.2).  The converse on the AA projection is
immediate: (1.2)--(1.3) give degree one or two at every A owner, while
(1.1) gives the exact lower rainbow.  The aggregate loads are then

\[
 C_T=2-d_A(T),\qquad Y_T=d_A(T)-1.
\]

These identities do not impose the B-owner degree ledger, explaining the
last qualification.  ∎

The literal fibre census of the frozen word is

\[
 |F_X|:\qquad 1^{2589},\quad 2^{400},\quad 3^{14}.       \tag{1.4}
\]

It follows that there are exactly

\[
 |C|=400+2\cdot14=428                                   \tag{1.5}
\]

cuts and

\[
 N-3003=429=\operatorname{Cat}_7                       \tag{1.6}
\]

AA components.

## 2. Exact short-component formula

Adjoin the two virtual cuts \(-1\) and \(M=3431\), and write

\[
 -1=c_0<c_1<\cdots<c_{428}<c_{429}=M.
\]

### Theorem 2.1 (gap grading)

The \(j\)-th AA component has exactly

\[
 \ell_j=c_{j+1}-c_j                                      \tag{2.1}
\]

vertices.  Consequently its number of depth-three distinguished-coordinate
residence defects is exactly

\[
 D(C)=\#\{j:c_{j+1}-c_j\in\{2,3\}\}.                   \tag{2.2}
\]

Hard distinguished-coordinate residence is equivalent to all successive
cuts in \(C\cup\{-1,M\}\) being at distance at least four.

#### Proof

After a cut at edge \(c_j\), the next component begins at vertex
\(c_j+1\) and ends at vertex \(c_{j+1}\); this gives (2.1), including the
two boundary components.  Condition (1.3) already gives \(\ell_j\ge2\).
A distinguished-coordinate run is precisely one AA component, so a run is
too short for depth three exactly when \(\ell_j=2\) or \(3\).  ∎

There is an equivalent finite logical form.  Let \(K_i\) mean that position
\(i\) is the retained representative of its fibre.  Besides exactly one
\(K_i\) in every fibre, the owner-degree clauses are

\[
 K_i\lor K_{i+1},                                        \tag{2.3}
\]

with endpoint units.  Hard residence adds

\[
 K_i\lor K_j\qquad(|i-j|=2\text{ or }3),                \tag{2.4}
\]

and the four additional boundary units.  Since cut positions cannot be
adjacent, every violated clause in (2.4) is one and only one short
component.  After choosing the survivor of each of the fourteen ternary
fibres, this is a Boolean Min-2SAT instance on the 400 double fibres.  This
is the exact nonlocal content hidden by the scalar short-run count.

## 3. A general interval bound

For an interval \(I\) of edge positions, define

\[
 \delta(I)=|I|-|\{\gamma_i:i\in I\}|.                  \tag{3.1}
\]

### Lemma 3.1 (interval excess)

Every feasible AA cut set has at least \(\delta(I)\) cuts in \(I\).  The
number of short gaps whose two endpoints lie in \(I\) is at least

\[
 \phi(I)=\max\left\{0,
 \left\lceil\frac{4(\delta(I)-1)-(|I|-1)}2\right\rceil
 \right\}.                                               \tag{3.2}
\]

#### Proof

At most one occurrence of each colour can be retained, proving the first
claim.  If \(t\) cuts in \(I\) have \(s\) successive gaps of length two or
three, their span is at least

\[
 2s+4(t-1-s)=4(t-1)-2s.
\]

It is at most \(|I|-1\).  Use \(t\ge\delta(I)\) and rearrange.  ∎

This bound is useful locally but cannot see the long fibre implications
which dominate the frozen instance.

## 4. Four hand-verifiable forced defects

All positions below are zero-based edge positions, and the displayed lists
are the complete fibres of the indicated decimal rank-six masks.

### Proposition 4.1 (solver-free lower bound)

Every AA projection on the frozen path satisfies

\[
 \boxed{D(C)\ge4}.                                       \tag{4.1}
\]

#### Proof

There are four fibre-disjoint implication gadgets.

1. The consecutive double-double word is

   \[
   F_{14374}=\{708,709\},\qquad
   F_{12390}=\{710,711\}.
   \]

   Each fibre supplies one cut.  The choice \(709,710\) is forbidden by
   (1.3), and every other pair has distance two or three.

2. The consecutive triple is

   \[
   F_{10318}=\{1940,1941,1942\}.
   \]

   It supplies two cuts.  Nonadjacency forces them to be \(1940,1942\),
   at distance two.

3. The two-fibre implication is

   \[
   F_{5149}=\{2219,2220\},\qquad
   F_{5273}=\{2221,2521,2522\}.
   \]

   The adjacent pair \(2521,2522\) cannot both be cuts, so the ternary
   fibre forces a cut at \(2221\).  The double fibre forces a cut at
   \(2219\) or \(2220\).  The latter is adjacent to \(2221\), so the cut
   is \(2219\), giving a gap of two.

4. The long implication chain is

   \[
   \begin{aligned}
   F_{7697}&=\{179,1775\},&
   F_{3858}&=\{181,1838\},\\
   F_{16128}&=\{1364,1365,1773\},&
   F_{3792}&=\{1836,2723\},\\
   F_{2761}&=\{2725,2726\}.&&
   \end{aligned}
   \]

   Suppose this gadget created no short gap.  The last double fibre forces
   a cut at \(2725\) or \(2726\), so the preceding double fibre cannot cut
   at \(2723\) and must cut at \(1836\).  Hence the second fibre cannot cut
   at \(1838\) and must cut at \(181\).  Hence the first fibre cannot cut
   at \(179\) and must cut at \(1775\).  The ternary fibre must cut at
   \(1773\), because its adjacent positions \(1364,1365\) cannot both be
   cuts.  The cuts \(1773,1775\) give the final contradiction.

Each gadget therefore supplies a pair of cuts at distance two or three.
No third cut can lie strictly between such a pair without being adjacent
to one endpoint, so the pair is consecutive in the global cut order.  The
four gadgets use disjoint fibre-position sets, hence give four distinct
terms in (2.2).  ∎

The triple gadget alone proves hard residence infeasible, without invoking
either upper-`q1` family or a solver.

## 5. Where the trusted bound 17 lives

On the 842 positions belonging to non-singleton fibres, join two positions
when either they are in the same fibre or their path distance is at most
three.  Fibre choices and every term of (2.2) factor over the connected
components of this graph.  The literal component-size census is

\[
 45\cdot2,\ 2\cdot4,\ 3\cdot6,\ 1\cdot7,\ 2\cdot8,
 \ 2\cdot10,\ 1\cdot11,\ 3\cdot12,\ 1\cdot25,\ 1\cdot611.
                                                               \tag{5.1}
\]

Thus there are 61 independent components.  The four gadgets of Proposition
4.1 lie in four of the 60 small components.  The frozen 17-defect witness

```text
scratch/k15_generalized_pascal_braid_20260729/minz_base.json
SHA-256 dd2a8eeda0aa996fed43a9bb92eb823cfa57d0d00f1f3e9492dcc4235f115363
```

has exactly four defects in the 60 small components and thirteen in the
single 611-position component.  Proposition 4.1 and this witness therefore
certify that the combined small-component minimum is exactly four.

The trusted CP-SAT log originally proved minimum 17 for the complete
lower/degree system without exporting a solver-independent UNSAT core.  At
the time of this note, the precise missing combinatorial statement was:

> **Former missing giant-component lemma.**  Every admissible survivor choice in
> the 611-position, 300-fibre component creates at least thirteen short
> gaps.

This lemma is now proved, by fifteen weighted implication cores and a parity
exclusion of equality, in

```text
THREAD_H_K14_GIANT_WEIGHTED_CORE_PARITY_THEOREM_20260729.md
```

Together with Proposition 4.1 it gives a solver-free proof of 17 for the AA
projection.  Lemma 3.1 alone detects the first two local gadgets; the other
two proofs already use implications transported along colour fibres.

## 6. Quantitative cost of editing the path

The 17 short gaps of the displayed optimum have the following pairwise
disjoint cut endpoints:

\[
\begin{split}
 &(179,181),(547,549),(708,711),(842,844),(853,856),\\
 &(1179,1181),(1260,1262),(1429,1432),(1697,1700),\\
 &(1822,1824),(1881,1883),(1940,1942),(2207,2209),\\
 &(2219,2221),(2735,2737),(2774,2776),(3351,3353).
\end{split}                                               \tag{6.1}
\]

### Theorem 6.1 (edit-versus-global-rerouting inequality)

Let a same-endpoint Hamilton path \(P'\) delete \(s\) old path edges and
add \(s\) new ones.  Let \(L\) be the set of lower colours occurring on
the deleted or added seams, so \(|L|\le2s\).  Compare any AA survivor
choice on \(P'\) with the displayed 17-defect survivor choice on \(P\), and
let \(u\) be the number of colours \(X\notin L\) whose surviving retained
old occurrence changes.  Then

\[
 \boxed{D(P')\ge17-4s-u}.                               \tag{6.2}
\]

In particular, hard residence requires

\[
 4s+u\ge17.                                              \tag{6.3}
\]

#### Proof

An old cut endpoint from (6.1) can cease to be an old cut in only three
ways.  It can be one of the \(s\) deleted old edges.  Its colour can lie in
\(L\), in which case at most one old cut per such colour is promoted to the
new survivor.  Or its unchanged colour fibre can be globally rerouted, in
one of the \(u\) counted cases.  Thus at most

\[
 s+|L|+u\le3s+u
\]

of the 34 pairwise distinct endpoints disappear as cuts.  This destroys at
most \(3s+u\) of the 17 old short intervals.  If both endpoint cuts remain,
the corresponding old short segment remains contiguous unless a deleted
old path edge lies inside it.  The intervals in (6.1) are disjoint, so the
\(s\) deleted edges destroy at most \(s\) further intervals.  Every
surviving interval is still a two- or three-vertex AA component of \(P'\),
which proves (6.2).  ∎

Consequences of (6.3) are exact:

\[
\begin{array}{c|c}
s&\text{necessary global reroutings outside changed colours}\\ \hline
2&u\ge9\\
3&u\ge5\\
4&u\ge1\\
u=0&s\ge5.
\end{array}                                               \tag{6.4}
\]

Thus a repair confined to the colour fibres touched by its deleted or added
seams must replace at least five old path edges.  A two- or three-seam
repair can only work through a genuinely global alternating survivor
cascade.

## 7. The smallest chronology neighbourhood

A nontrivial Hamilton path on the same vertex deck with the same two
endpoints cannot differ in one edge.  If it differs in exactly two old and
two new edges, it is a 2-opt interval reversal.  Hence \(s=2\) is the
absolute smallest same-port chronology neighbourhood.

It is nonempty and can alter a local obstruction.  Cutting positions
\(1941,2671\) and reversing the intervening block replaces lower seam
labels

\[
 (10318,8271)\longmapsto(8271,12366).                   \tag{7.1}
\]

Both new seams are Johnson edges, the endpoints and middle deck are fixed,
and all 3003 rank-six colours remain present.  The multiplicity of 10318
drops from three to two, destroying the consecutive-triple certificate;
12366 rises from one to two.  This is only a support-level escape, not a
full-`q1` factor.  Literally, the deleted endpoint pairs are
\((10319,14414)\) and \((8783,12367)\), while the added pairs are
\((10319,8783)\) and \((14414,12367)\); their intersections are the four
labels displayed in (7.1).

There is nevertheless a stronger unconditional lower bound for an actual
hard-resident escape.  If every old edge of either gadget 1 or gadget 2 in
Proposition 4.1 survives, those edges remain a contiguous subpath (possibly
reversed).  Extra new occurrences of either gadget colour do not help:
exactly one occurrence may be selected globally, while two adjacent old
occurrences cannot both be cuts.  Thus each old double still has exactly
one local cut; similarly, the old consecutive triple must still have the
local cut--selected--cut pattern.  Therefore a successful path must delete
an edge from each gadget.  For a 2-opt cutting position
\(i\in\{708,709,710,711\}\) and
\(j\in\{1940,1941,1942\}\), the two half-symmetric-difference distances of
the proposed seams are

\[
\begin{array}{c|ccc}
 &1940&1941&1942\\ \hline
708&(3,3)&(2,2)&(2,2)\\
709&(3,2)&(3,1)&(2,2)\\
710&(2,3)&(2,2)&(1,3)\\
711&(3,3)&(3,2)&(2,3).
\end{array}                                               \tag{7.2}
\]

A Johnson 2-opt requires \((1,1)\), which never occurs.  Hence

\[
 \boxed{|E(P)\setminus E(P')|\ge3,
 \qquad |E(P)\triangle E(P')|\ge6}                      \tag{7.3}
\]

for every same-endpoint hard-resident replacement.

The threshold in (7.3) is sharp only for escaping these two local
certificates.  A legal three-cut rethreading is obtained by cutting

\[
 (709,835,1942)
\]

and changing

\[
 A|B|C|D\longmapsto A|\overleftarrow B|
 \overleftarrow C|D.                                    \tag{7.4}
\]

It deletes seam labels \(14374,14854,10318\), adds
\(14854,14406,10766\), is Johnson throughout, retains the same endpoints,
and preserves the complete rank-six support.  It breaks gadgets 1 and 2,
but gadgets 3 and 4 remain; it is therefore not a hard-resident solution.
The literal changed seams are

\[
\begin{array}{c|c|c}
\text{kind}&\text{rank-seven endpoints}&\text{intersection}\\ \hline
\text{deleted}&14886,14438&14374\\
\text{deleted}&14855,14862&14854\\
\text{deleted}&14414,10830&10318\\
\text{added}&14886,14855&14854\\
\text{added}&14438,14414&14406\\
\text{added}&14862,10830&10766.
\end{array}                                               \tag{7.5}
\]

The correct conclusion is consequently three-tiered:

* two changed edges are enough to leave the single-triple fibre trap;
* at least three are necessary to leave the two principal local traps
  simultaneously;
* at least five are necessary for a repair local to its changed colour
  fibres to eliminate all seventeen defects of the known optimum.

No statement here proves that three or five changed edges suffice for hard
residence.

## 8. Full-q1 boundary

Full `q1` only restricts the AA family further.  Therefore every full-`q1`
solution on the frozen path obeys Theorems 1.1, 2.1, Proposition 4.1, and in
particular cannot be hard resident.  Combining the trusted lower/degree
optimum with the currently reported full-`q1` incumbent gives the present
finite bracket

\[
 17\le \min D_{\mathrm{full}\ q1}\le29,                 \tag{8.1}
\]

where the lower endpoint is solver-certified for the larger lower/degree
feasible set and the upper endpoint is the independently replayed s15106
incumbent, not an optimum proved in this note.

After changing the chronology one must still choose the singleton/pair
controllers at all A owners so that the B-owner degree ledger and both
upper channels hold simultaneously.  Preserving rank-six support, as in
(7.1) or (7.4), proves none of those conditions.

The smallest exact replacement gate is therefore:

> Find a same-endpoint path edit with \(s\ge3\), necessarily with
> \(4s+u\ge17\), whose new coloured-cut instance has a distance-four exact
> transversal and whose selected endpoint/interior controllers admit the
> common B-owner degree ledger and both upper-`q1` covers.

The giant-component lemma is the remaining fixed-path structural problem;
the displayed replacement gate is the first variable-path/full-`q1`
problem.  Neither is proved here.

## 9. Adversarial scope audit

1. Proposition 4.1 is independent of CP-SAT and of both upper channels.
2. In the original version of this note, 17 was not reproved
   combinatorially and the missing content was isolated as the 611-position
   lemma.  The follow-up weighted-core theorem cited in Section 5 now proves
   that lemma and hence the exact value 17.
3. The three-cut certificate preserves the middle deck and lower support,
   not an AA selection, full `q1`, old-coordinate residence, or deeper
   shadows.
4. Inequality (6.2) is relative to the displayed optimum and explicitly
   charges every survivor change outside the seam-colour set through \(u\);
   it does not rule out a global alternating cascade.
5. Accordingly, (7.3) is a necessary hard-residence bound, while \(s=5\)
   is only a necessary bound for the narrower seam-local repair class.

## 10. Later sharp support-radius correction

Item 5 above is superseded by the audited four-closure theorem in

```text
MATH_CODE_AUDIT_AD_PASCAL_LIVE305_AND_EDIT5_CEGAR_20260729.md.
```

Four disjoint durable old-edge closures force four deletions for every
hard-resident exact-lower AA chronology, including when new seams add further
occurrences of their colours.  The complete 900-case four-cut route audit
then shows that every Johnson-compatible assembly restores all four deleted
edges.  Consequently the unconditional frozen-parent bound is now

\[
 |E(P)\setminus E(P')|\ge5,
 \qquad |E(P)\triangle E(P')|\ge10,
\]

under exact one-per-rank-six colour, AA degree one or two at every vertex,
and minimum AA-component size four.  No edit-five positive solution is
claimed.
