# Thread A: compound Shadow--Braid portals at the verified H25 carrier

Date: 2026-07-28

Frontier note: the H25 results below remain valid, but the authoritative
outer carrier has subsequently advanced through H24 and H23 to H22.  See
`THREAD_A_H22_NEUTRAL_ROUTER_REMOTE_CIRCUIT_SPLITTER_20260728.md`.

Status: exact compound Hall theorem, exact H25 tight-shore parametrization,
an independently re-audited sequential two-braid Hall-24 certificate, a
strong sufficient portal certificate, and a concrete finite Benders
generator.  A restricted disjoint-pair audit disproves the five-nested-shore
test as a sufficient condition.  No catalogue-wide two-braid no-go is
claimed.

## 0. Outcome

Two seam collars can cooperate: one can be exactly Hall-neutral while
relocating the DM obstruction, and the next can discharge the relocated
shore.  This occurs on the verified H25 carrier via

\[
 \operatorname{FR}(1512,2458,4103),\qquad
 \operatorname{FR}(2664,3491,6201),
\]

with exact deficiencies \(25\to25\to24\).  Both moves preserve the middle
deck, Johnson chronology, depth-three residence, the complete upper support,
and the entire lower-hole vector \((4,19,4,1,0,0,0)\).  Thus the answer is
**yes** when “neutral” means the required deck/residence/shadow-support
ledgers; only the first move is Hall-neutral.  Whether two collars which are
also each Hall-neutral on the same H25 base can cooperate remains open
outside the restricted disjoint branch audited below.

The exact condition is not separate neutrality but the all-shore inequality

\[
 \sigma(A)+n_{B^+}(A)-n_{B^-}(A)\ge1
 \qquad\text{for every target shore }A.              \tag{0.1}
\]

Here \(B^-,B^+\) are the exact old and new boundary-cell banks after
cancelling identical target-neighbourhood signatures, and

\[
                         \sigma(A)=25-|A|+|N_{H25}(A)|.
\]

A pair of three-seam braids has at most 180 old and 180 new full Hall
boundary cells before cancellation, so only shores of old slack at most 180
can obstruct.

The five historical shores

\[
 A_{25}\subset A_{26}\subset A_{27}\subset A_{28}\subset A_{29}
\]

are all tight on H25 and give useful necessary filters.  They are far from
complete: the H25 alternating residual has 9,256 optional SCCs and 5,760
sink SCCs, already giving \(2^{5760}\) tight shores.  Inside that lattice,
5,759 independently adjoinable singleton targets generate a particularly
useful point-portal cube.

A restricted audit found seven commuting, individually Hall-neutral pairs
which improve all five historical shores.  Every one nevertheless remains
Hall-25.  For the clean representative

\[
 \operatorname{FR}(424,1827,3179)
 \quad+\quad
 \operatorname{RF}(3908,4226,5589),                 \tag{0.2}
\]

the shore \(A_{25}\) gains one neighbour, but the tight singleton extension

\[
                         A_{25}\cup\{20654\}
\]

does not.  This is a rigorous obstruction to any descent theorem which
checks only the five nested shores, but it does not conflict with the
child-dependent sequential Hall-24 certificate above.

## 1. Compound braid and seam locality

Let \(X\) be the verified H25 Johnson path.  Delete \(s\) path edges,
orient and reorder the resulting segments, and reconnect them by \(s\)
Johnson edges into one path \(X^\ast\).

### Theorem 1.1 (compound Shadow--Braid theorem)

The reconnection has the following properties.

1. \(X^\ast\) enumerates exactly the same middle deck.
2. At depth \(q\), only windows crossing an old or new seam change; there
   are at most \(sq\) deleted and \(sq\) inserted occurrences per shore.
3. Depth-three residence and the maximal-erosion identities require only
   bounded seam-collar checks.
4. One seam affects at most

   \[
                            9+10+11=30               \tag{1.1}
   \]

   full compiler cells of lengths one, two, and three on either side.

Thus a simultaneous pair of three-cut braids has at most 180 old and 180
new full Hall-boundary cells before signature cancellation.  The theorem
does not require either three-cut move to be a legal intermediate path.

#### Proof

Oriented segments retain every internal path edge and every internal
union/intersection window.  The new endpoint tests are exactly the \(s\)
reconnecting edges, and the state multiset is unchanged.  A new short run
must meet a new seam.  At depth three a middle seam changes only the three
controller states \(P_c,P_{c+1},P_{c+2}\).  A depth-\(e\) compiler cell has
full predicate interval \(P_{a-3},\ldots,P_{a+e+3}\), giving \(e+9\)
possible starts.  Summing \(9,10,11\) proves (1.1). \(\square\)

## 2. Exact two-collar Hall theorem

Represent every compiler cell by its exact target-neighbourhood shore,
retaining multiplicity.  Cancel the common shore multiset of the H25 and
final graphs.  Let \(B^-\) and \(B^+\) be the residual old and new banks,
and define

\[
 n_F(A)=|\{c\in F:N(c)\cap A\ne\varnothing\}|.       \tag{2.1}
\]

### Theorem 2.1 (exact compound Hall current)

The compound braid has deficiency at most 24 if and only if (0.1) holds.
If \(b=|B^-|\), it is enough to check shores with

\[
                         \sigma(A)\le b.             \tag{2.2}
\]

For two base braids \(Q,R\), define

\[
\begin{aligned}
 I_Q(A)&=|N_Q(A)|-|N_0(A)|,\\
 \Xi_{Q,R}(A)
 &=|N_{QR}(A)|-|N_Q(A)|-|N_R(A)|+|N_0(A)|.
\end{aligned}                                       \tag{2.3}
\]

Then the exact pair condition is

\[
 \sigma(A)+I_Q(A)+I_R(A)+\Xi_{Q,R}(A)\ge1
 \qquad(A\subseteq L).                              \tag{2.4}
\]

Currents may be added only when the interaction term is known to vanish,
as for commuting braids with disjoint exact Hall collars.  For sequential
braids one may instead use the always-valid telescoping currents

\[
 d_1(A)=|N_1(A)|-|N_0(A)|,\qquad
 d_2(A)=|N_2(A)|-|N_1(A)|.                          \tag{2.5}
\]

#### Proof

After signature cancellation,

\[
 |N_{\rm final}(A)|-|N_0(A)|=n_{B^+}(A)-n_{B^-}(A).
\]

Substitute this identity into the bipartite deficiency formula.  If
\(\sigma(A)\ge b+1\), the loss is at most \(b\), so (0.1) is automatic.
Equations (2.3)--(2.5) are algebraic expansion and telescoping of the same
neighbourhood difference. \(\square\)

### Matching form

Fix a maximum H25 matching \(M\), let \(M_0\) be its part surviving in the
final graph, and put

\[
                         r=|M|-|M_0|.
\]

If \(\alpha\) is the maximum number of vertex-disjoint
\(M_0\)-augmenting paths in the final alternating network, then

\[
                         \delta_{\rm final}=25+r-\alpha.          \tag{2.6}
\]

Hence a pair descends precisely when

\[
                         \alpha\ge r+1.                            \tag{2.7}
\]

For two individually Hall-neutral collars, each separate alternating
network has only enough flow to rematch its destroyed old edges.  Joint
descent requires one additional portal unit in the combined network.

## 3. Exact H25 slack and tight-shore lattice

The verified H25 graph has 16,383 targets, 19,311 cells, matching size
16,358, and deficiency 25.  Its lower-hole vector is

\[
                         (4,19,4,1,0,0,0),
\]

every upper layer \(q=1,\ldots,7\) is complete, and its seven zero-candidate
targets are

\[
 2575,5801,13616,13620,17738,21641,29776.
\]

Let \(U\) be the 25 left vertices unmatched by a fixed maximum matching
\(M\).  For a left set \(A\), define

\[
 e_M(A)=|\{r\in N(A):
       r\text{ is unmatched on the right or }M(r)\notin A\}|.     \tag{3.1}
\]

### Theorem 3.1 (residual slack identity)

For every \(A\subseteq L\),

\[
 \boxed{\sigma(A)=|U\setminus A|+e_M(A).}             \tag{3.2}
\]

In particular \(A\) is tight, meaning \(|A|-|N(A)|=25\), if and only if:

1. \(U\subseteq A\);
2. \(A\) is closed under alternating successors; and
3. no vertex of \(A\) has an edge to an unmatched right vertex.

#### Proof

The matched vertices in \(A\setminus U\) supply
\(|A\setminus U|\) distinct baseline neighbours.  Every remaining
neighbour is counted exactly once by \(e_M(A)\).  Hence

\[
 |N(A)|=|A\setminus U|+e_M(A),
\]

which gives (3.2).  Equality \(\sigma(A)=0\) is equivalent to the three
displayed closure conditions. \(\square\)

On left vertices, draw \(x\to y\) when a nonmatching edge from \(x\) reaches
a right vertex matched to \(y\), and mark \(x\) bad when it reaches an
unmatched right vertex.  After SCC condensation:

* the forward closure of \(U\) is forced;
* the reverse closure of the bad SCCs is forbidden; and
* any successor-closed subset of the remaining SCCs is optional.

The exact H25 census is

\[
\begin{array}{c|r|r}
\text{class}&\text{SCCs}&\text{left vertices}\\ \hline
\text{forced}&1279&1320\\
\text{forbidden}&2130&5754\\
\text{optional}&9256&9309.
\end{array}                                           \tag{3.3}
\]

There are 12,665 SCCs.  The optional DAG has 15,219 arcs, height eight,
2,214 sources, and 5,760 sinks.  The minimal tight shore is \(A_{25}\).
The maximal tight shore has 10,629 targets and 10,604 neighbours.  Every
subset of the sink SCCs is successor-closed, so H25 has at least
\(2^{5760}\) distinct tight shores.

There is a much larger explicit sublattice.  Put

\[
 F=A_{25},\qquad C=N(F),
\]

and let \(X\) be the set of 5,759 targets \(x\notin F\) for which
\(F\cup\{x\}\) is tight.  For every \(x\in X\), tightness gives

\[
                         N(x)\setminus C=\{p(x)\}                 \tag{3.4}
\]

for a unique cell \(p(x)\).  The map \(p:X\to R\setminus C\) is injective:
if \(p(x)=p(y)\) for distinct \(x,y\), then

\[
 |F\cup\{x,y\}|-|N(F\cup\{x,y\})|\ge 26,
\]

contrary to the verified H25 deficiency.  Consequently every \(S\subseteq
X\) obeys

\[
 |N(F\cup S)|=|C|+|S|=|F\cup S|-25.                \tag{3.5}
\]

Thus the shores \(F\cup S\) form an explicit Boolean cube of
\(2^{5759}\) tight shores.  This rules out literal enumeration as a useful
all-shore certificate and motivates the rank oracle below.

### Theorem 3.2 (one-cut separator for all tight shores)

For any fixed signed compound bank \(B^-,B^+\), the minimum Hall current

\[
 \mu(B^-,B^+)=
 \min_{A:\,|A|-|N_G(A)|=25}
       \bigl(n_{B^+}(A)-n_{B^-}(A)\bigr)             \tag{3.6}
\]

is the value of one integral source--sink minimum cut on the optional-SCC
condensation with one auxiliary node per nonconstant gained cell.  Hence
the compound opens every old tight shore if and only if \(\mu\ge1\), and a
failed cut reconstructs a literal blocking shore.

#### Proof

Let \(x_C\) indicate selection of optional SCC \(C\).  Successor closure is
the implication \(x_C\le x_D\) for every condensation arc \(C\to D\).
An old cell is either forced active, forced inactive, or has activity one
optional-SCC indicator: if it is matched by \(M\) to \(y\), every other
neighbour \(x\) has the alternating successor arc \(x\to y\), while \(y\)
itself hits the cell, so its activity is exactly the indicator of the SCC
of \(y\).  A gained cell is likewise constant, or has
activity

\[
                         \bigvee_{C\in K(c)}x_C,
\]

where \(K(c)\) is the set of optional target SCCs met by its exact shore.
Move the lost-cell indicators to rewards.  For each nonconstant gained
cell add a node \(y_c\) of weight \(-1\) and implications \(C\to y_c\) for
all \(C\in K(c)\).  In a maximum-weight closed set, \(y_c\) is selected
exactly when at least one predecessor is selected.  Thus maximum closure,
equivalently one integral minimum cut, computes the negative of (3.6) up
to the forced constant.  The selected SCCs give the shore by Theorem 3.1.
\(\square\)

For two sequential collars, Theorems 2.1 and 3.1 give the concrete exact
condition

\[
 |U\setminus A|+e_M(A)+d_1(A)+d_2(A)\ge1
 \qquad(A\subseteq L).                              \tag{3.7}
\]

This is the promised all-low-slack statement.  Theorem 3.2 separates all
old tight shores at once, but that test alone is not sufficient: a
positive-slack shore can receive enough negative current to become the new
blocker.  A final maximum matching, equivalently the exact core/exterior
decomposition in Theorem 5.2, remains necessary.

## 4. The five inherited nested shores

On H25 the five inherited shores and their neighbourhoods are nested:

\[
\begin{array}{c|rrrrr}
 &A_{25}&A_{26}&A_{27}&A_{28}&A_{29}\\ \hline
|A_i|&1320&1480&1484&1489&1524\\
|N(A_i)|&1295&1455&1459&1464&1499.
\end{array}                                           \tag{4.1}
\]

All five have gap 25.  Successive left and right layer sizes agree:

\[
                         160,\ 4,\ 5,\ 35.            \tag{4.2}
\]

As a cross-check, with rows \(H29,H28,H27,H26,H25\) and columns
\(A_{29},A_{28},A_{27},A_{26},A_{25}\), the audited gap matrix is

\[
\begin{pmatrix}
29&28&27&26&25\\
28&28&27&26&25\\
27&27&27&26&25\\
26&26&26&26&25\\
25&25&25&25&25
\end{pmatrix}.                                       \tag{4.3}
\]

For a cell shore \(\Gamma\), let

\[
 \tau(\Gamma)=\min\{j\in\{0,1,2,3,4\}:
                    \Gamma\cap A_{25+j}\ne\varnothing\},
\]

with \(\tau=\infty\) if there is no hit.  Put

\[
 c_t(Q)=
 |\{\Gamma\in B_Q^+:\tau(\Gamma)=t\}|
 -
 |\{\Gamma\in B_Q^-:\tau(\Gamma)=t\}|.              \tag{4.4}
\]

Then

\[
 \Delta_Q(A_{25+j})=\sum_{t\le j}c_t(Q).             \tag{4.5}
\]

Thus a disjoint additive pair must satisfy the five necessary prefix
conditions

\[
 \sum_{Q\in\{Q_1,Q_2\}}\sum_{t\le j}c_t(Q)\ge1
 \qquad(0\le j\le4).                                \tag{4.6}
\]

These five inequalities are not sufficient because the optional SCCs
generate thousands of additional tight shores.

## 5. A strong positive two-collar portal certificate

Let \(F=A_{25}\) be the minimal tight shore and let \(A^{\max}\) be the
maximal tight shore from Section 3.

### Theorem 5.1 (domination plus universal portal)

Suppose the combined old and new boundary banks have equal size and admit a
bijection

\[
                         \phi:B^-\longrightarrow B^+
\]

such that

\[
                         N(c)\subseteq N(\phi(c))
                         \qquad(c\in B^-).            \tag{5.1}
\]

Assume that for one pair \(c_\ast,\phi(c_\ast)\),

\[
 N(c_\ast)\cap A^{\max}=\varnothing,
 \qquad
 N(\phi(c_\ast))\cap F\ne\varnothing.                \tag{5.2}
\]

Then every shore satisfies (0.1), and the compound braid has deficiency at
most 24.

#### Proof

The inclusion matching (5.1) implies that no shore loses a boundary
neighbour.  Hence every shore of positive old slack satisfies (0.1).
Every tight shore contains \(F\) and is contained in \(A^{\max}\).
Condition (5.2) therefore changes the distinguished paired cell from a
nonneighbour to a neighbour for every tight shore, giving strict current
one. \(\square\)

The bijection may pair an old cell from the first collar with a new cell
from the second.  Thus two collars can satisfy this theorem even when
neither collar has a domination certificate separately.  This is an
explicit algebraic mechanism for neutral-collar cooperation.

For only the five certified nested shores, the weaker version of (5.2)
replaces \(A^{\max}\) by \(A_{29}\).  It is not safe for the full H25
tight-shore lattice.

### Theorem 5.2 (exact core/exterior split)

Let \(G'\) be any final compound graph, put \(F=A_{25}\),
\(C'=N_{G'}(F)\), \(L_0=L\setminus F\), and set

\[
                         K=|L|-24=16359.              \tag{5.3}
\]

Then \(G'\) has deficiency at most 24 if and only if there are an integer

\[
 1296=K-|L_0|\le a\le\min\{1320,|C'|\}              \tag{5.4}
\]

and a set \(C_1\subseteq C'\), \(|C_1|=a\), such that

1. \(G'[F,C_1]\) has a matching saturating \(C_1\); and
2. \(G'[L_0,R\setminus C_1]\) has a matching of size at least \(K-a\).

#### Proof

Given a matching of size at least \(K\), discard edges until its size is
\(K\).  Let \(C_1\) be the right endpoints of its edges from \(F\), and put
\(a=|C_1|\).  At most all \(|L_0|=15063\) exterior targets are matched, so
\(a\ge K-|L_0|=1296\); the two restrictions of the matching have the stated
properties.  Conversely, the two asserted matchings use disjoint left
sets and disjoint right sets, so their union has size at least
\(a+(K-a)=K\). \(\square\)

This is an exact DM-portal allocation theorem, not merely a rankwise
necessary condition.  It permits a larger core gain to trade against a
small exterior leave, as happens in the positive pair of Section 6.

### Theorem 5.3 (exact one-new-neighbour DM-portal criterion)

Let \(G'\) be the final graph of any compatible compound braid, not
necessarily a disjoint composition.  Put

\[
 F=A_{25},\quad C=N_G(F),\quad C'=N_{G'}(F),\quad
 L_0=L\setminus F.
\]

Suppose

\[
                         |C'|=|C|+1=1296.            \tag{5.5}
\]

Then \(G'\) has deficiency exactly 24 if and only if both of the following
finite rank conditions hold:

1. \(G'[F,C']\) has a matching saturating all 1,296 vertices of \(C'\);
2. \(G'[L_0,R\setminus C']\) has a matching saturating all 15,063 vertices
   of \(L_0\).

#### Proof

If the two matchings exist, their left and right vertex sets are disjoint,
so their union has size

\[
                         1296+15063=16359.
\]

It leaves 24 of the 16,383 targets unmatched.  On the other hand \(F\)
itself has final gap \(1320-1296=24\), so the deficiency is exactly 24.

Conversely, a matching witnessing deficiency 24 has size 16,359.  It can
match at most all 15,063 vertices of \(L_0\), hence it matches at least
1,296 vertices of \(F\).  Every neighbour of \(F\) lies in the 1,296-set
\(C'\), so it matches exactly 1,296 vertices of \(F\), saturates \(C'\),
and matches every vertex of \(L_0\) into \(R\setminus C'\).  Restriction
gives the two asserted matchings. \(\square\)

Equivalently, once the core rank is 1,296, every all-shore inequality
containing \(F\) collapses to Hall's condition in the external graph
\(G'[L_0,R\setminus C']\).  Indeed, for \(B\subseteq L_0\),

\[
 |F\cup B|-|N_{G'}(F\cup B)|
 =24+|B|-|N_{G'}(B)\setminus C'|.                  \tag{5.6}
\]

Thus a single external maximum-matching computation checks the entire
\(2^{5759}\)-shore cube from (3.5), all its unions, and every other shore
containing \(F\).  This is the sharp finite DM-portal test in the common
case where a neutral pair gives \(F\) exactly one new neighbour.

## 6. Exact positive sequential portal certificate

Let \(G_0\) be H25, and define \(G_1,G_2\) successively by

\[
 G_0\xrightarrow{\operatorname{FR}(1512,2458,4103)}G_1
 \xrightarrow{\operatorname{FR}(2664,3491,6201)}G_2.             \tag{6.1}
\]

### Theorem 6.1 (two-braid DM-portal escape)

The two moves in (6.1) are literal resident Johnson segment braids and
satisfy

\[
 \nu(G_0)=16358,\qquad \nu(G_1)=16358,\qquad \nu(G_2)=16359.     \tag{6.2}
\]

Consequently \(G_2\) has deficiency 24 and satisfies the compound Hall
inequality

\[
 \sigma_{G_0}(A)+|N_{G_2}(A)|-|N_{G_0}(A)|\ge1
 \qquad(A\subseteq L) .                              \tag{6.3}
\]

At both steps the middle deck is exact, every adjacent pair is Johnson,
depth-three residence is exact, maximal erosion is nonempty and dilates
back to the middle path, every upper support through \(q=7\) remains
complete, and the lower-hole vector remains

\[
                         (4,19,4,1,0,0,0).            \tag{6.4}
\]

The seven zero-candidate targets also remain unchanged.

#### Proof and independent audit

The canonical files are

```text
scratch/k15_segment_braid_hall25.json
scratch/k15_segment_braid_hall25_portal.json
scratch/k15_segment_braid_hall24.json
```

with file SHA-256 values, respectively,

```text
67a84c71f570dbdb8cdad5912b9bed333c4122e9237fed38d56690ad5bd0c473
83678f3fb928402b3e01f3de0553be0f1a60b30a50ee51d7979b8517abd99701
49eb1060ccbe86f056295f0b96fe409f275737b8b759f5b7ca0ee2fa7ca0416e
```

The independent verifier `scratch/audit_k15_segment_braid_descent.py`
reconstructs each segment permutation, every Johnson edge, residence and
erosion, all lower and upper supports through depth seven, the 19,311-cell
compiler graph, and a fresh maximum matching.  Applied to (6.1), it returns
`PASS`, deficiencies \((25,25,24)\), changed exact cell-shore counts
\((18,40)\), and contracted boundary-rank changes

\[
                         15\to15,\qquad20\to21.       \tag{6.5}
\]

The reproducing invocation is

```sh
python3 scratch/audit_k15_segment_braid_descent.py \
  --base scratch/k15_segment_braid_hall25.json \
  --step scratch/k15_segment_braid_hall25_portal.json \
  --step scratch/k15_segment_braid_hall24.json
```

The matching counts give (6.2).  Equation (6.3) is then exactly Theorem
2.1.  The remaining claims are the verifier's direct finite checks.  This
is a certificate proof: the verifier does not import the production
enumerator. \(\square\)

The exact DM-shore gap matrix, with rows \(G_0,G_1,G_2\) and columns the
canonical maximum shores extracted from \(G_0,G_1,G_2\), is

\[
\begin{pmatrix}
25&24&23\\
22&25&24\\
21&24&24
\end{pmatrix}.                                       \tag{6.6}
\]

Running the verifier from H29 through the full descent and then (6.1) gives
an additional exact check on the five inherited shores: every one of
\(A_{25},\ldots,A_{29}\) has gap

\[
                         25\longrightarrow22\longrightarrow21. \tag{6.7}
\]

Equivalently, the two sequential current vectors on this chain are
\((3,3,3,3,3)\) and \((1,1,1,1,1)\).  Thus even strict improvement of every
historical nested shore by the first braid does not imply global descent;
the replacement DM shore in (6.6) is decisive.

Thus the first braid does much more than open the old minimal shore: it
reduces that shore's gap from 25 to 22, while a different shore rises from
24 to 25.  The second braid lowers this relocated obstruction and leaves no
shore above 24.  This is the exact nonmonotone DM-portal mechanism.  The
transported segment ranges overlap and the second braid is specified in the
child ordering, so it must be materialized on \(G_1\); adding two
independently computed base-H25 bank signatures would not prove the result.

This is only a Hall/support advance.  The final lower holes still violate
the necessary prefix corridor \(h_1\le2\), \(h_2\le h_1+3\le5\), and Hall
deficiency remains 24.  No exact length-6438 compiler is claimed.

## 7. Concrete failure of the five-shore screen

Among 9,233 resident/all-upper-safe H25 descriptions, 6,433 are identity
reversals.  The remaining 2,800 descriptions represent 2,115 distinct
paths.  Requiring the lower-\(q=1\) hole count to remain four leaves 874
descriptions, all representing distinct paths.  Hence the preliminary
commuting-pair pool has at most

\[
                         \binom{874}{2}=381501        \tag{7.1}
\]

candidates before interval, shadow, and signature pruning.

The following two moves have disjoint moved intervals, commute, and are
individually Hall-neutral:

\[
 Q=\operatorname{FR}(424,1827,3179),\qquad
 R=\operatorname{RF}(3908,4226,5589).                \tag{7.2}
\]

Each move and their composition is a Johnson path, is depth-three resident,
has complete upper support, preserves the full lower-hole vector

\[
                         (4,19,4,1,0,0,0),
\]

keeps the same seven zero targets, and has matching size 16,358.

Their five-chain currents are

\[
 (1,0,0,0,0)+(0,1,1,1,1)=(1,1,1,1,1),              \tag{7.3}
\]

so every inequality (4.6) passes.  Nevertheless, put

\[
                         A_x=A_{25}\cup\{20654\}.
\]

This is another tight shore.  Before the pair,

\[
 |N(A_{25})|=1295,\qquad |N(A_x)|=1296.
\]

After the pair,

\[
 |N(A_{25})|=1296,\qquad |N(A_x)|=1296.              \tag{7.4}
\]

Thus \(A_x\) remains gap 25.  Target 20654 has one old external portal cell,
at depth two and start 3179, with envelope 20654 and mandatory mask 20518.
The pair replaces it by the depth-two cell at start 1776, whose mandatory
mask is 20516, but that new cell is already a neighbour of the new
\(A_{25}\).  The singleton extension therefore gains no new neighbour.

The failure is exactly the second rank obstruction in Theorem 5.3.  For
this pair the core graph \(G'[F,C']\) has rank \(1296/1296\), whereas the
external graph \(G'[L_0,R\setminus C']\) has rank

\[
                         15062/15063.                \tag{7.5}
\]

Its sole unmatched external target is 20654.  Thus the pair creates the
new core neighbour required by the nested shores, but consumes the unique
external portal of precisely the target which remains exposed.

There are 5,759 certified tight singleton extensions
\(A_{25}\cup\{x\}\), of which 5,535 have rank-seven \(x\) and 224 have
rank-six \(x\).  Define

\[
\begin{aligned}
 \gamma_Q&=\Delta_Q(A_{25}),\\
 \rho_Q(x)&=\Delta_Q(A_{25}\cup\{x\})-\gamma_Q.
\end{aligned}                                        \tag{7.6}
\]

For a disjoint additive pair, every singleton extension imposes the cheap
necessary screen

\[
 \gamma_Q+\gamma_R+\rho_Q(x)+\rho_R(x)\ge1.           \tag{7.7}
\]

Equation (7.4) is exactly the failure of (7.7) at \(x=20654\).

Six further disjoint pairs pass (4.6) but remain Hall-25:

\[
\begin{array}{ll}
\operatorname{RF}(3884,4135,4533)+\operatorname{FF}(658,670,3639),\\
\operatorname{RF}(3884,4135,4533)+\operatorname{FR}(1676,2595,3642),\\
\operatorname{RF}(4922,6057,6113)+\operatorname{FF}(658,670,3639),\\
\operatorname{RF}(4922,6057,6113)+\operatorname{FR}(1676,2595,3642),\\
\operatorname{RF}(4922,6057,6113)+\operatorname{FR}(674,4396,4476),\\
\operatorname{RF}(4922,6057,6113)+\operatorname{RF}(1856,2714,4699).
\end{array}                                          \tag{7.8}
\]

The restricted screen is exhaustive under the following additional
hypotheses: both candidates are generated directly from H25, have disjoint
collars, preserve lower \(q=1\), and have nonnegative current on every shore
in (4.1).  Call a pair *chain-complementary* when its exact combined
five-current vector is \((1,1,1,1,1)\).  Before imposing individual
Hall-neutrality, exactly eight disjoint chain-complementary pairs occur.
One contains \(\operatorname{RF}(123,1679,4480)\), whose child has
deficiency 27; removing it leaves exactly the seven individually Hall-25
pairs in (7.2) and (7.8).

For every one of the seven, \(\Delta(A_{25})=1\), the core rank is
\(1296/1296\), and the external rank is \(15062/15063\).  Hence all seven
fail Theorem 5.3 and remain Hall-25.  The representative and the first two
pairs in (7.8) preserve the full lower-hole vector; the last four have five,
rather than four, depth-three lower holes.  Thus this is a rigorous no-go
for the restricted disjoint, lower-\(q=1\)-safe, individually Hall-neutral,
chain-nonnegative architecture, not for overlapping collars, simultaneous
six-cut braids, nonmonotone intermediates, or pairs which temporarily lose
a nested shore.

## 8. Proof-safe finite pair generator

The following rule is exact and terminates.

1. Start with the 874 nontrivial, lower-\(q=1\)-safe descendants generated
   directly from H25 in Section 7.  Store for each its exact at-most-90-cell
   old and new banks,
   its five currents \(\Delta(A_{25+j})\), its core gain
   \(\gamma=\Delta(A_{25})\), and the sparse singleton vector \(\rho\) in
   (7.6).
2. For the commuting branch, retain pairs whose moved intervals and exact
   boundary-start sets are disjoint and whose reconnections commute.  More
   than ten positions of separation is a sufficient, not necessary,
   collar-disjointness test.  This branch begins with at most 381,501
   unordered pairs.
3. Signature-cancel the old and final exact cell-shore multisets to obtain
   \(B^-,B^+\).  Reject a pair unless it passes every prefix inequality
   (4.6), has total \(\gamma\ge1\), and passes all 5,759 singleton
   inequalities (7.7).
4. Run the exact maximum-closure cut of Theorem 3.2.  If \(\mu<1\), record
   the returned literal tight shore as a Benders row and reject the pair.
5. Attempt the polynomial domination matching (5.1)--(5.2).  A success is a
   theorem-level Hall-24 certificate without an all-cut computation.
6. When total \(\gamma=1\), form \(C'=N_{G'}(A_{25})\) directly from the
   compound banks and run the two rank tests of Theorem 5.3.  These tests
   are necessary and sufficient, so no further shore enumeration is
   needed.
7. In every other case run the exact incremental matching test (2.6).
   Accept exactly when the final matching has size at least 16,359.
8. On failure, output a final residual DM shore \(A\) and add its exact
   inequality (0.1) as a Benders cut for every remaining pair.

For arbitrary sequential two-braid words, the second braid must instead be
re-enumerated on each first child: a braid changes segment coordinates, so
two H25 bank signatures cannot simply be added.  At each child one must
recheck the Johnson endpoints, residence, every upper layer, and the full
cell catalogue before applying Steps 3--8.  Alternatively one may enumerate
simultaneous reconnections of at most six path edges, which does not require
a legal intermediate.  Both extensions are finite, and Theorem 5.3 remains
an exact final-state oracle whenever \(|N_{G'}(A_{25})|=1296\); otherwise
the final matching test remains exact.

There are finitely many pairs and finitely many target subsets.  Therefore
the process terminates.  A positive output contains the final path and a
matching of size 16,359.  If every pair is eliminated, the accumulated
shores and per-pair inequalities form a rigorous catalogue-wide
obstruction.

The present exact boundary is:

* a cooperative pair is algebraically possible;
* the five nested shores do not certify it;
* the explicit sequential pair (6.1) proves Hall \(25\to25\to24\) while
  preserving every required support ledger audited here;
* every pair in the restricted disjoint, individually neutral,
  chain-nonnegative branch fails the exact external-rank portal test;
* this Hall-24 endpoint still has lower holes \((4,19,4,1,0,0,0)\), seven
  zero targets, and no common-word certificate, so it does not solve the
  finite formula.

The H25 graph and the positive certificate in Section 6 are independently
reproducible from the frozen artifacts and verifier named there.  The SCC
census in Section 3 agrees with
`THREAD_D_H25_MULTI_COLLAR_CROSS_STRATUM_CIRCULATION_20260728.md`; the
5,759-singleton and restricted seven-pair counts are exact in-lane finite
audits.  This lane did not freeze a separate standalone output for those
three censuses.  The structural theorems do not depend on that omission;
portable independent reproduction of those numerical counts does.
