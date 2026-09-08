# Thread A: the three-seam Shadow--Braid exchange and Hall descent

Date: 2026-07-28

Status: unconditional braid, shadow-locality, and matching-augmentation
theorems, together with one exact finite descent from Hall deficiency 29 to
28.  No theorem yet guarantees another descent from every positive
deficiency state.

## 0. Outcome

The segment braid is a genuinely different primitive from local UNIT
controller surgery.  It permutes whole path segments, so middle ownership
and deck exactness are automatic.  Every internal intersection and union
window is transported unchanged; only windows meeting three old or three
new seams enter the shadow ledger.

For the frozen \(k=15\) carrier, the audited enumeration contains

\[
                         12\,013
\]

resident indexed move descriptions, of which

\[
                          9\,243
\]

preserve every upper rank-\((8+q)\) support layer for \(1\le q\le7\).
Both totals include \(6\,433\) length-one reversal identities.  After
removing them there are \(5\,580\) nontrivial resident descriptions,
\(2\,810\) nontrivial resident/all-upper-safe descriptions, and \(2\,105\)
distinct nontrivial safe paths.  The enumeration is exhaustive for the
four implemented interior single-braid orientation classes, not for
endpoint braids or compositions.
The move

\[
                         \operatorname{RF}(471,2327,5456)       \tag{0.1}
\]

is resident, preserves all seven upper layers, preserves the entire lower
hole vector and the lower \(q=1\) multiset, leaves the same seven
zero-candidate targets, and changes the exact Hall deficiency

\[
                         29\longrightarrow28.                   \tag{0.2}
\]

This proves one Shadow--Braid descent.  It does not prove that the process
can be iterated to zero.

## 1. Exact segment-braid theorem

Let

\[
                         X=(X_0,X_1,\ldots,X_{N-1})
\]

be a Johnson path.  Choose

\[
                         0<a<u\le v<N-1
\]

and write

\[
\begin{aligned}
A&=(X_0,\ldots,X_{a-1}),\\
B&=(X_a,\ldots,X_{u-1}),\\
C&=(X_u,\ldots,X_v),\\
D&=(X_{v+1},\ldots,X_{N-1}).
\end{aligned}                                                   \tag{1.1}
\]

For a sign \(\epsilon\in\{+,-\}\), let \(Y^\epsilon\) mean \(Y\) in its
forward or reversed orientation.  Define

\[
                         X'=A\,C^{\epsilon_C}\,
                            B^{\epsilon_B}\,D.                   \tag{1.2}
\]

Let \(c_-,c_+\) be the first and last states of \(C^{\epsilon_C}\), and
let \(b_-,b_+\) be the first and last states of \(B^{\epsilon_B}\).

### Theorem 1.1 (endpoint tests are necessary and sufficient)

The word \(X'\) is a Johnson path if and only if

\[
                         X_{a-1}\sim c_-,
                         \qquad c_+\sim b_-,
                         \qquad b_+\sim X_{v+1},                 \tag{1.3}
\]

where \(\sim\) denotes Johnson adjacency.  Whenever (1.3) holds, \(X'\)
enumerates exactly the same deck as \(X\), with the same multiplicities.

#### Proof

Every adjacency internal to \(A,B,C,D\) is inherited from \(X\); reversing
a segment preserves its undirected adjacencies.  The only new adjacent
pairs are the three displayed in (1.3), proving necessity and sufficiency.
Equation (1.2) is a permutation of the indexed states of \(X\), so its deck
is identical. \(\square\)

For the four orientations, (1.3) specializes as follows:

\[
\begin{array}{c|ccc}
(\epsilon_C,\epsilon_B)&A|C&C|B&B|D\\ \hline
(+,+)&X_{a-1}\sim X_u&X_v\sim X_a&X_{u-1}\sim X_{v+1}\\
(-,+)&X_{a-1}\sim X_v&X_u\sim X_a&X_{u-1}\sim X_{v+1}\\
(+,-)&X_{a-1}\sim X_u&X_v\sim X_{u-1}&X_a\sim X_{v+1}\\
(-,-)&X_{a-1}\sim X_v&X_u\sim X_{u-1}&X_a\sim X_{v+1}.
\end{array}                                                   \tag{1.4}
\]

In the last row the middle test is an old edge and is automatic; this is
ordinary reversal of the interval \([a,v]\).

## 2. Exact all-depth shadow locality

For \(q\ge1\), define the consecutive upper and lower labels

\[
 U_q(i)=\bigcup_{j=0}^{q}X_{i+j},
 \qquad
 L_q(i)=\bigcap_{j=0}^{q}X_{i+j}.                    \tag{2.1}
\]

Let \({\cal I}_q(K)\) be the set of window starts whose index interval
\([i,i+q]\) crosses at least one cut in a cut set \(K\).  For the old and
new words take

\[
 K_{\rm old}=\{a,u,v+1\},
 \qquad
 K_{\rm new}=\{a,a+|C|,v+1\}.                       \tag{2.2}
\]

Coincident or automatically retained seams are counted only once.

### Theorem 2.1 (Shadow--Braid ledger)

There is a bijection between the starts outside
\({\cal I}_q(K_{\rm old})\) and those outside
\({\cal I}_q(K_{\rm new})\) under which both labels in (2.1) are equal.
Consequently, for either sign \(\star\in\{U,L\}\) and every target \(S\),

\[
 m'_{q,\star}(S)
 =m_{q,\star}(S)-d_{q,\star}(S)+a_{q,\star}(S),      \tag{2.3}
\]

where \(d\) counts old boundary windows and \(a\) counts new boundary
windows.  Moreover,

\[
 |{\cal I}_q(K_{\rm old})|\le3q,
 \qquad
 |{\cal I}_q(K_{\rm new})|\le3q.                    \tag{2.4}
\]

Thus the complete depth-\(q\) shadow change has at most \(3q\) deleted and
\(3q\) inserted window occurrences on each shore.

#### Proof

A window which crosses no cut is contained in one of the four segments.
Translation transports a forward segment window, while reflection
transports a reversed segment window in reverse order.  Union and
intersection are invariant under reversal, so both labels agree.  Removing
these paired internal windows leaves exactly the two boundary sets and
gives (2.3).  One cut is crossed by at most the \(q\) starts immediately
preceding it; taking a union over three cuts proves (2.4), including
overlapping collars. \(\square\)

If the old upper rank-\((8+q)\) layer is complete, the exact support test is

\[
 m_{q,U}(S)-d_{q,U}(S)+a_{q,U}(S)\ge1
 \quad\text{for every }|S|=8+q.                     \tag{2.5}
\]

Fractional balance or unchanged aggregate multiplicity is not enough.

## 3. Residence is also a seam condition

Assume every internal coordinate run in \(X\) has length at least \(d+1\).
Every run wholly internal to one segment is transported with the same
length.  Only runs meeting a new seam can split or merge.

### Lemma 3.1 (local residence test)

The braid \(X'\) is depth-\(d\) resident if and only if every internal
coordinate run meeting a new seam has length at least \(d+1\).  It is
sufficient to inspect the \(d+1\) states on each side of each new seam.

#### Proof

All runs disjoint from the seams are inherited.  A seam run is determined
until either the coordinate disappears or \(d+1\) consecutive occurrences
have been seen.  Hence no information farther from the seam affects whether
that run is too short. \(\square\)

For the present carrier \(d=3\), so the residence audit is confined to
constant-size four-state collars at the three seams.

## 4. Locality of the exact Hall graph

Let \(P\) be the depth-three maximal erosion controller.  A compiler cell
has the form \(J=[s,s+e]\) with \(e\in\{0,1,2\}\).  Its exact candidate
predicate depends on:

1. the controller states \(P_j\) for \(j\in J\); and
2. the carrier-incidence sets inside the four-position intervals
   \([i,i+3]\) which can be contained in \(J\).

Only \(i\in[s-3,s+e]\) can contribute.  Therefore the entire neighbourhood
of \(J\) is determined by

\[
                         P_{s-3},\ldots,P_{s+e+3}.    \tag{4.1}
\]

### Lemma 4.1 (Hall collar bound)

After transporting internal cells with their segment, every cell whose
interval (4.1) avoids the three-position controller collars of all old and
new seams has exactly the same target neighbourhood.  A middle seam at
\(c\) can change only \(P_c,P_{c+1},P_{c+2}\).  For one seam, the possible
changed starts at depth \(e\) therefore form an interval of size at most
\(e+9\).  Hence at most

\[
                         (9+10+11)\cdot3=90           \tag{4.2}
\]

old cells and 90 new cells belong to the full Hall boundary.

The smaller number

\[
                         (3+4+5)\cdot3=36
\]

counts envelope changes only.  It is not safe for the exact Hall graph,
because mandatory carrier subsets use the expanded interval (4.1).

#### Proof

The exact envelope, mandatory-coordinate, and nonempty-hit predicates are
functions of (4.1).  On one oriented segment this controller word is merely
translated or reflected, so the predicate is transported identically.
The interval \([s-3,s+e+3]\) meets the changed controller collar
\([c,c+2]\) only when

\[
                         c-e-3\le s\le c+5,
\]

which gives \(e+9\) starts.  Sum over \(e=0,1,2\) and three seams.
\(\square\)

The bound is on boundary cells after the internal identification; it is not
a bound on the number of target edges incident to them.

## 5. Exact matching-descent criterion

Let \(G\) and \(G'\) be the old and braided target--cell graphs after the
stable internal cells have been identified.  Write

\[
 \delta(G)=\max_{A\subseteq L}\bigl(|A|-|N_G(A)|\bigr)=h           \tag{5.1}
\]

and define the old Hall slack of \(A\) by

\[
 \sigma_G(A)=h-|A|+|N_G(A)|\ge0.                                  \tag{5.2}
\]

For the braid \(Q\), put

\[
\begin{aligned}
 g_Q(A)&=|N_{G'}(A)\setminus N_G(A)|,\\
 \ell_Q(A)&=|N_G(A)\setminus N_{G'}(A)|,\\
 \Delta_Q(A)&=g_Q(A)-\ell_Q(A).
\end{aligned}                                                     \tag{5.3}
\]

### Theorem 5.1 (exact Shadow--Braid Hall dual)

The new deficiency is

\[
 \boxed{\delta(G')=
 h-\min_{A\subseteq L}\bigl(\sigma_G(A)+\Delta_Q(A)\bigr).}        \tag{5.4}
\]

Consequently the braid decreases deficiency by at least one if and only if

\[
                         \sigma_G(A)+\Delta_Q(A)\ge1
                         \qquad(A\subseteq L),                     \tag{5.5}
\]

and it decreases deficiency by exactly one if and only if the minimum in
(5.4) equals one.

If at most \(b\) old boundary cells can disappear, then
\(\ell_Q(A)\le b\).  Hence every set with \(\sigma_G(A)\ge b+1\)
automatically satisfies (5.5).  For the present three-seam depth-three
compiler, \(b\le90\), so it is enough to check the finite slack shells

\[
                         0\le\sigma_G(A)\le90,                     \tag{5.6}
\]

where a shell of slack \(t\) requires

\[
                         g_Q(A)-\ell_Q(A)\ge1-t.                   \tag{5.7}
\]

#### Proof

For every \(A\subseteq L\),

\[
\begin{aligned}
 |A|-|N_{G'}(A)|
 &=|A|-|N_G(A)|-\Delta_Q(A)\\
 &=h-\sigma_G(A)-\Delta_Q(A).
\end{aligned}
\]

Taking the maximum over \(A\) proves (5.4) and therefore (5.5).  The
boundary claim follows from
\(\Delta_Q(A)\ge-\ell_Q(A)\ge-b\). \(\square\)

The theorem is the exact noncircular descent condition: every old
deficiency-\(h\) shore and every near-tight shore must receive enough new
boundary neighbours to compensate for those it loses.

For an equivalent matching certificate, fix a maximum matching \(M\) of
\(G\), and put

\[
                         M_0=M\cap E(G'),
                         \qquad r=|M|-|M_0|.                         \tag{5.8}
\]

Thus \(r\le90\) by Lemma 4.1.

### Theorem 5.2 (boundary augmenting-path criterion)

Let \(\alpha\) be the maximum number of pairwise vertex-disjoint
\(M_0\)-augmenting paths in \(G'\).  Then

\[
                         \boxed{\delta(G')=h+r-\alpha.}            \tag{5.9}
\]

Consequently the braid decreases Hall deficiency by at least one if and
only if \(\alpha\ge r+1\).  In particular, if \(M\subseteq E(G')\), one
ordinary augmenting path is necessary and sufficient.

#### Proof

Simultaneously augmenting along \(\alpha\) disjoint paths produces a
matching of size \(|M_0|+\alpha\).  Conversely, the symmetric difference
of \(M_0\) with a maximum matching of \(G'\) has exactly
\(\nu(G')-|M_0|\) more forward-augmenting than reverse-augmenting
components, and in particular contains that many disjoint forward
augmenting paths.  Thus

\[
                         \nu(G')=|M_0|+\alpha.
\]

Since \(|M_0|=|M|-r\), subtracting from the fixed target count gives (5.9).
In particular, augmenting along \(r+1\) disjoint paths produces a matching
of size

\[
                         |M_0|+r+1=|M|+1,
\]

so deficiency falls; the reverse implication follows from (5.9).
\(\square\)

This is the exact descent interface.  It protects against the hidden
failure in which a new portal is created but too many old boundary-matching
edges are destroyed.

## 6. The certified \(29\to28\) braid

For (0.1), the segment lengths are

\[
                         |B|=1856,\qquad |C|=3130.
\]

The three old seam pairs are

\[
 (X_{470},X_{471}),\quad
 (X_{2326},X_{2327}),\quad
 (X_{5456},X_{5457}),
\]

and the three new seam pairs are

\[
 (X_{470},X_{5456}),\quad
 (X_{2327},X_{471}),\quad
 (X_{2326},X_{5457}).                               \tag{6.1}
\]

All three new pairs are Johnson edges.  Hence Theorem 1.1 proves deck
exactness and the Johnson path property without enumeration.  The finite
collar audits then prove:

\[
\begin{array}{c|c|c}
\text{quantity}&\text{old}&\text{new}\\ \hline
\text{Hall deficiency}&29&28\\
\text{matching size}&16354&16355\\
\text{zero-candidate targets}&7&7\\
\text{missing lower }q=1\text{ colours}&4&4.
\end{array}                                                   \tag{6.2}
\]

The seven zero-candidate targets themselves are unchanged:

\[
 2575,\ 5801,\ 13616,\ 13620,\ 17738,\ 21641,\ 29776. \tag{6.3}
\]

The complete lower-support hole vector is unchanged:

\[
                         (4,21,4,1,0,0,0)
                         \qquad(q=1,\ldots,7).                     \tag{6.4}
\]

The four lower \(q=1\) holes themselves remain

\[
                         5801,\ 7267,\ 8877,\ 13620.               \tag{6.5}
\]

At the three seams, the lower colours are unchanged as a list,

\[
                         (6253,6317,6191)\longmapsto
                         (6253,6317,6191),
\]

while the upper colours are merely cyclically permuted,

\[
                         (7405,7343,7279)\longmapsto
                         (7279,7405,7343).
\]

The entire lower-\(q=1\), upper-\(q=1\), and upper-\(q=2\) occurrence
multisets are preserved.  At every other upper depth the support test (2.5)
passes.  Multiplicities do change at lower depths \(q=2,\ldots,6\) and
upper depths \(q=3,\ldots,6\), so higher-depth multiset preservation is not
asserted.

The old canonical deficient shore \(A_{29}\) satisfies

\[
 |A_{29}|=1524,\qquad |N_X(A_{29})|=1495,\qquad
 |N_{X'}(A_{29})|=1496.                              \tag{6.6}
\]

The new canonical shore obeys

\[
 A_{28}\subset A_{29},\qquad
 |A_{28}|=1489,\qquad |N_{X'}(A_{28})|=1461.          \tag{6.7}
\]

Thus the move creates a literal portal into the old alternating tree and
does not merely move an equal deficiency-\(29\) block elsewhere.  The
canonical finite artifacts are

\[
\begin{gathered}
\text{scratch/search\_k15\_segment\_braid\_native.cpp},\\
\text{scratch/k15\_segment\_braid\_hall28.json}.
\end{gathered}
\]

The finite artifact supplies the two matching sizes in (6.2); Theorems
5.1--5.2 explain their exact exchange meaning.  In particular, the move has
minimum dual transfer equal to one in (5.4).

This is an exact Hall-graph statement.  It does not by itself construct one
common physical lower word realizing all matched cells.

## 7. Conditional descent theorem and the remaining lemma

Let \({\cal X}\) be the directed exchange graph whose vertices are exact
middle-deck Johnson paths which are depth-three resident, support every
upper layer through \(q=7\), and obey chosen lower-hole and zero-candidate
bounds.  Draw an edge for every segment braid which preserves those
conditions.  Let \(h(X)\) be exact Hall deficiency.

For an admissible edge \(X\to X'\), define

\[
 \omega(X,X')=
 \min_{A\subseteq L}\bigl(\sigma_X(A)+\Delta_{X,X'}(A)\bigr)
 =h(X)-h(X').                                         \tag{7.1}
\]

Thus Hall deficiency is an exact integer Lyapunov function: positive-weight
edges descend, zero-weight components may be contracted, and negative
weights are precisely worsening exchanges.

### Theorem 7.1 (Shadow--Braid descent principle)

Fix \(X_0\in{\cal X}\).  Suppose that at every vertex \(X\) reachable from
\(X_0\) with \(h(X)>0\), some outgoing braid satisfies the equivalent
conditions of Theorems 5.1--5.2.  Then after at most \(h(X_0)\) braids one
reaches a vertex with deficiency zero, without leaving \({\cal X}\).

#### Proof

Each selected edge stays in \({\cal X}\) and decreases the nonnegative
integer \(h\) by at least one.  Iteration therefore terminates at zero after
at most its initial value. \(\square\)

Theorem 7.1 is conditional.  The counts \(12\,013\) and \(9\,243\) at the
initial carrier do not imply that every later carrier has a descending
move, and a single \(29\to28\) example does not exclude a positive-deficiency
local minimum.

There is also an unavoidable zero-target floor:

\[
                         h(X)\ge z(X),                \tag{7.2}
\]

where \(z(X)\) is the number of targets of degree zero.  The certified move
keeps \(z=7\), so it reduces the nonzero-degree contribution to deficiency
from \(29-7=22\) to \(28-7=21\).  A complete descent must eventually use a
braid, or another move, which lowers the zero-target count itself.

The minimum remaining hypothesis is now precise:

> For every positive-deficiency vertex in the admissible Shadow--Braid
> exchange component, there is a three-seam braid for which all old Hall
> shores satisfy (5.5), equivalently one which destroys \(r\) edges of some
> maximum matching and whose new Hall graph contains \(r+1\) disjoint
> augmenting paths, while preserving residence, all upper layers, and the
> chosen lower/zero bounds.

Proving this boundary-augmentation statement would give a genuine descent
theorem.  Failing it, an explicit admissible positive-deficiency vertex
with no such outgoing braid is the exact obstruction.
