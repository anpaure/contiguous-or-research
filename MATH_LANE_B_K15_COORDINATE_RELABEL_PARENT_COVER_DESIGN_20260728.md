# Lane B: coordinate-relabel parents form a cross-stratum compiler covering design

Date: 2026-07-28

**Index convention.** Every coordinate tuple copied from a relabel screen in
this note is zero based.  The main conversions are `[1,12]_0=(2,13)_1`,
`[3,4]_0=(4,5)_1`, `[10,11]_0=(11,12)_1`,
`[3,13]_0=(4,14)_1`, and `[5,7]_0=(6,8)_1`.

Method: pure mathematics.  The finite H29 target list, the displayed
motif-count vectors, the three fixed DM-family sizes, and the parent
arc-intersection ledgers are taken as audited frontier data.  No
enumeration, solver output, or random-search assertion is used in the
structural proofs below.

## 0. Result

Let \(H\) be a residence-safe directed middle-layer parent on
\(\binom{[15]}8\), written as an oriented Hamilton path.  A
**parent-pure interior motif** for a compiler target \(T\) is a bounded
consecutive segment of \(H\) which realizes \(T\) in the exact compiler
relation and does not use either outer endpoint collar.

For every target rank \(s\), let

\[
 {\cal T}_s=\binom{[15]}s,\qquad N_s=\binom{15}s,
\tag{0.1}
\]

and let

\[
 c_H(T)=\#\{\hbox{parent-pure residence-safe interior motifs for }T\},
\tag{0.2}
\]

\[
 B_s(H)=\{T\in{\cal T}_s:c_H(T)>0\},\qquad
 Z_s(H)={\cal T}_s\setminus B_s(H),\qquad z_s=|Z_s(H)|.
\tag{0.3}
\]

The main conclusion is an exact orbit-covering theorem.

### Theorem A (simultaneous-rank relabel cover)

Let \(D\) be any fixed set of compiler targets, or the union of the
target shores of any fixed finite collection of DM families.  Put

\[
 d_s=|D\cap Z_s(H)|.
\tag{0.4}
\]

If

\[
 \sum_s d_s\left({z_s\over N_s}\right)^t<1,
\tag{0.5}
\]

then there are at most \(t\) coordinate permutations
\(\sigma_1,\ldots,\sigma_t\) such that every target in \(D\) has a
parent-pure residence-safe interior motif in at least one of

\[
 H,\ \sigma_1H,\ldots,\sigma_tH.
\tag{0.6}
\]

The same permutations serve all ranks simultaneously.  No independent
rankwise choice is made.

More quantitatively, the proportion of ordered \(t\)-tuples of
permutations which have this property is at least

\[
 1-\sum_s d_s\left({z_s\over N_s}\right)^t.
\tag{0.7}
\]

In particular, if

\[
 \epsilon=\max_{s:z_s>0}{z_s\over N_s}<1,
\qquad d=\sum_sd_s,
\tag{0.8}
\]

then it is enough to take any integer

\[
 t>{\log d\over\log(1/\epsilon)}.
\tag{0.9}
\]

At fixed \(k=15\), this is an absolute \(O(1)\) parent catalogue for
every fixed compiler target family.

### H29 corollary

For the current H29 fixed-target frontier relation, the exact
parent-level zero set handed to this lane is

\[
\begin{split}
 Z_6(H29)&=\{2575,13616,17738,21641,29776\},\\
 Z_7(H29)&=\{5801,13620\},
\end{split}
\tag{0.10}
\]

and there are no other H29 frontier zeros.  Hence

\[
 \sum_s{z_s^2\over N_s}
 ={25\over\binom{15}6}+{4\over\binom{15}7}
 ={25\over5005}+{4\over6435}<1.
\tag{0.11}
\]

Theorem A with \(D=Z(H29)\) and \(t=1\) proves, without searching
permutations, that one coordinate-relabel parent clears all seven
zeros simultaneously.

The audited explicit choice

\[
 \tau=(10,11)
\tag{0.12}
\]

does so.  In the order

\[
 (2575,5801,13616,13620,17738,21641,29776)
\tag{0.13}
\]

its parent-pure interior motif counts are

\[
 (4,1,2,1,3,3,3).
\tag{0.14}
\]

Thus the two-parent directed catalogue

\[
 {\cal E}(H29)\cup{\cal E}(\tau H29)
\tag{0.15}
\]

contains at least one residence-safe parent-pure interior motif for
every H29 compiler target.  On the seven old zeros it contains exactly
the certified positive supply in (0.14), of total mass \(17\).

This closes the **cross-stratum source-supply** question.  It does not
yet select one mixed successor factor containing all those motifs.

In fact, (0.7) and (0.11) show that the proportion of coordinate
permutations which clear all seven old zeros is at least

\[
 1-{25\over5005}-{4\over6435}>0.994.
\tag{0.16}
\]

Thus \(\tau\) is an explicit legal witness to a dense relabel class,
not an isolated exceptional permutation.

### Deeper fixed-DM update

For the three fixed shores \(A29,R3,R4\), the exact raw requirement is
one added relabel parent:

\[
 t_{\rm raw}=1.
\]

H29 alone has only \(1495<1524\) cells against \(A29\).  Either
\((10,11)H29\) or the stronger max-min-slack winner
\(\tau_1=(1,12)\) supplies point support and positive aggregate
interior slack in all three shores.  The second winner
\(\tau_2=(5,7)\) is a collision-reserve parent which supplies all
twelve targets exposed by the subsequent successor selections.  It
does not change the raw minimum from one to two.

The exact remaining gate is a coloured independent-transversal problem
in a bounded conflict hypergraph: two-edges encode shared
successor/predecessor collisions, and hyperedges of size at most four
encode mixed depth-three residence returns.  Sections 9--14 give the
full statement and quantitative ledgers.

## 1. Equivariance of parent-pure motifs

Let \(G=S_{15}\) act on middle masks, targets, directed Johnson edges,
and paths by coordinate relabelling.  If

\[
 P=(X_0,X_1,\ldots,X_\ell)
\tag{1.1}
\]

is an interior compiler motif for \(T\) in \(H\), then

\[
 \sigma P=(\sigma X_0,\sigma X_1,\ldots,\sigma X_\ell)
\tag{1.2}
\]

is an interior compiler motif for \(\sigma T\) in \(\sigma H\).

Indeed, the exact compiler map is built from unions, intersections,
complements inside \([15]\), and ordered consecutive incidence.  All
these operations commute with \(\sigma\).  Johnson adjacency is also
preserved.  Since \(P\) avoids both endpoint collars, so does
\(\sigma P\).

The depth-three residence predicate is likewise coordinate-free: it is
an equality/intersection condition on the masks in a bounded consecutive
segment.  Hence a residence-safe motif stays residence-safe.

Therefore:

### Lemma 1.1 (exact motif equivariance)

For every \(\sigma\in S_{15}\) and target \(T\),

\[
 c_{\sigma H}(T)=c_H(\sigma^{-1}T).
\tag{1.3}
\]

Consequently

\[
 B_s(\sigma H)=\sigma B_s(H),
\qquad
 Z_s(\sigma H)=\sigma Z_s(H).
\tag{1.4}
\]

In particular, coordinate relabelling can move supply within a rank
stratum but cannot move supply between different ranks.

## 2. The orbit blocks are exact \(1\)-designs

Fix a rank \(s\).  The blocks

\[
 \{\sigma B_s(H):\sigma\in S_{15}\}
\tag{2.1}
\]

form a regular covering design on \({\cal T}_s\).  Equivalently, the
zero blocks

\[
 \{\sigma Z_s(H):\sigma\in S_{15}\}
\tag{2.2}
\]

form a regular design of block size \(z_s\).

### Lemma 2.1 (exact point degree)

For every \(T\in{\cal T}_s\),

\[
 {1\over |S_{15}|}
 |\{\sigma:T\in\sigma Z_s(H)\}|
 ={z_s\over N_s}.
\tag{2.3}
\]

#### Proof

For uniform \(\sigma\), the inverse image \(\sigma^{-1}T\) is uniform
on \({\cal T}_s\), because \(S_{15}\) acts transitively on \(s\)-sets.
The event \(T\in\sigma Z_s(H)\) is exactly
\(\sigma^{-1}T\in Z_s(H)\), which has probability \(z_s/N_s\).
Multiplying by \(|S_{15}|\) gives (2.3). \(\square\)

This is the only design input needed.  Pairwise independence, a
two-transitive action, or a classification of motif shapes is
unnecessary.

## 3. Proof of the simultaneous-rank cover theorem

Choose \(\sigma_1,\ldots,\sigma_t\) independently and uniformly from
\(S_{15}\).  A target \(T\in D\setminus Z(H)\) is already supplied by
the base parent \(H\).  Suppose

\[
 T\in D\cap Z_s(H).
\tag{3.1}
\]

By Lemma 2.1, the probability that the \(i\)-th added parent also misses
\(T\) is exactly \(z_s/N_s\).  Independence of the chosen permutations
therefore gives

\[
 \Pr\!\left(
 c_{\sigma_iH}(T)=0\text{ for every }i=1,\ldots,t
 \right)
 =\left({z_s\over N_s}\right)^t.
\tag{3.2}
\]

Let \(U\) be the number of targets in \(D\) missed by the base and all
added parents.  Summing (3.2) over targets yields the exact expectation

\[
 {\mathbb E}U
 =\sum_s d_s\left({z_s\over N_s}\right)^t.
\tag{3.3}
\]

Since \({\bf1}_{\{U>0\}}\le U\), Markov's elementary integer bound gives

\[
 \Pr(U=0)\ge
 1-\sum_s d_s\left({z_s\over N_s}\right)^t,
\tag{3.4}
\]

which is the quantitative assertion (0.7).

Under (0.5), this expectation is strictly below one.  Since \(U\) is a
nonnegative integer, some deterministic tuple of permutations has
\(U=0\).  Removing repeated or redundant permutations can only reduce
the number of parents.  This proves Theorem A.

This expectation proof is equivalently a conditional-expectation greedy
set-cover proof.  At each stage, average over the next orbit block and
choose a permutation no worse than the average.  Hence Theorem A is an
exact finite design statement, not an appeal to random-like behaviour
of the successor catalogue.

## 4. One added parent: the exact cross-stratum criterion

The case \(t=1\) is particularly transparent.

### Proposition 4.1 (one-parent criterion)

Let \(D_s\subseteq Z_s(H)\).  If

\[
 \sum_s {|D_s|z_s\over N_s}<1,
\tag{4.1}
\]

then there is one coordinate permutation \(\sigma\) for which

\[
 D_s\cap Z_s(\sigma H)=\varnothing
\qquad\text{for every }s.
\tag{4.2}
\]

#### Proof

For uniform \(\sigma\), Lemma 2.1 and linearity of expectation give

\[
 {\mathbb E}\left|
 \bigcup_s(D_s\cap\sigma Z_s(H))
 \right|
 =\sum_s {|D_s|z_s\over N_s}<1.
\tag{4.3}
\]

The quantity inside the expectation is an integer, so it is zero for
some \(\sigma\). \(\square\)

Taking \(D_s=Z_s(H)\) gives the clean self-separation condition

\[
 \sum_s{z_s^2\over N_s}<1.
\tag{4.4}
\]

It says that one orbit block can be chosen disjoint from the original
zero block simultaneously in all strata.  For H29, (4.4) is exactly
(0.11).  The transposition \(\tau=(10,11)\) is an explicit member of
the nonempty set certified abstractly by (4.4).

The argument is genuinely cross-stratum: the same \(\sigma\) occurs in
every summand of (4.3).  Linearity of expectation, rather than
independent choices in ranks six and seven, supplies the common
permutation.

## 5. Fixed DM families and quantitative motif mass

Let \({\mathfrak A}=\{A_1,\ldots,A_J\}\) be any fixed finite collection
of DM target shores.  Put

\[
 D=\bigcup_{j=1}^J A_j.
\tag{5.1}
\]

Applying Theorem A to \(D\cap Z(H)\) gives one common parent catalogue
which supplies every target in every \(A_j\).  In particular, if

\[
 c_\Sigma(T)=c_H(T)+\sum_{\sigma\in\Sigma}c_{\sigma H}(T),
\tag{5.2}
\]

then

\[
 c_\Sigma(T)\ge1
\qquad(T\in A_j,\ 1\le j\le J).
\tag{5.3}
\]

Thus every fixed DM family has full point support in the parent-level
motif incidence graph.

For the explicit H29 pair \(\Sigma=\{\tau\}\), define

\[
 g=(4,1,2,1,3,3,3)
\tag{5.4}
\]

on the ordered zero list (0.13).  Every fixed target shore \(A\) obeys
the quantitative lower bound

\[
 \sum_{T\in A}c_{\{\tau\}}(T)
 \ge
 |A|+
 \sum_{T\in A\cap Z(H29)}(g_T-1).
\tag{5.5}
\]

Indeed, every nonzero H29 target contributes at least one base motif,
and every old zero contributes the corresponding \(\tau\)-motif count.
If \(A\) contains all seven old zeros, (5.5) gives at least

\[
 |A|+10
\tag{5.6}
\]

parent-pure motifs, because \(\sum_T(g_T-1)=10\).

## 6. Directed-successor legality

Adjoin the usual dummy endpoint to each oriented parent and view its
successor relation as a perfect matching from a source copy of the
middle layer to a target copy.  For a relabel set \(\Sigma\), define

\[
 {\cal E}_\Sigma
 ={\cal E}(H)\cup
   \bigcup_{\sigma\in\Sigma}{\cal E}(\sigma H).
\tag{6.1}
\]

Every motif counted by \(c_{\sigma H}(T)\) is a directed path all of
whose successor arcs lie in \({\cal E}_\Sigma\).  Because it is wholly
inside one parent:

1. its source and target incidences are ordered correctly;
2. every arc is Johnson-adjacent;
3. the complete bounded collar used by the compiler is present;
4. it is residence-safe; and
5. no artificial seam or endpoint payment is used.

Thus Theorem A supplies literal installable motif atoms, not merely
target labels or an averaged fractional incidence vector.

## 7. The exact remaining boundary

The theorem proves **catalogue supply**, not simultaneous selection.
Three constraints remain.

1. **Arc competition.**  Two parent-pure motifs may demand incompatible
   outgoing or incoming successor arcs.  A selected successor factor
   cannot automatically retain every supplied motif.
2. **Mixed residence and upper shadows.**  Each parent-pure motif is
   safe, but a switch between parents can create a new bounded segment.
   Those cross-parent segments still require the exact residence and
   upper-shadow clauses.
3. **DM capacity.**  Full point support of a DM shore does not imply
   \(|N(A)|\ge|A|\).  The selected cells must remain sufficiently
   distinct.  The H29 deficiency can therefore relocate even after all
   seven zero targets become positive.

Accordingly, the next exact object should be a **motif-preserving
successor-factor selection** on the two-parent catalogue
\({\cal E}(H29)\cup{\cal E}(\tau H29)\), or on the bounded catalogue
given by Theorem A for several DM witnesses.  Its variables should mark
whole parent-pure motifs before individual successor arcs; otherwise
the solver or switching argument can destroy the very supply established
here.

There is also a sharp orbit obstruction.  If a permitted relabel group
\(\Gamma\) has an orbit \({\cal O}\) on which \(B(H)\cap{\cal O}\) is
empty, then no number of \(\Gamma\)-relabel parents can supply a target
in \({\cal O}\).  For a restricted group, Theorem A remains true after
replacing rank strata by the \(\Gamma\)-orbits and replacing
\(z_s/N_s\) by

\[
 {|Z(H)\cap{\cal O}|\over|{\cal O}|}.
\tag{7.1}
\]

For the full coordinate group \(S_{15}\), the orbits are exactly the
rank strata, and H29 has positive support in every relevant stratum.
Hence this orbit obstruction is absent.

## 8. Lane-B verdict

The seven H29 zeros are not a persistent source-capacity obstruction.
The exact self-separation inequality (0.11) already forces a common
one-parent relabel cover, and \(\tau=(10,11)\) realizes it with the
positive vector (0.14).  More generally, coordinate-relabel parents
form a regular orbit design, and Theorem A selects \(O(1)\) parents for
every fixed collection of compiler targets or DM families.

What remains is a packing problem inside the directed successor
catalogue: preserve enough of these parent-pure motifs simultaneously
while enforcing one-in/one-out degree, residence, upper shadows, and
the full DM inequalities.  The parent-supply layer itself is now
closed.

## 9. Three different meanings of “enough cells”

The fixed DM shores in the current frontier are

\[
 |A29|=1524,\qquad |R3|=1530,\qquad |R4|=1374.
\tag{9.1}
\]

For a parent catalogue \({\cal P}\), let \({\cal C}_{\cal P}(T)\) be
the set of residence-safe parent-pure **interior** compiler cells which
accept target \(T\), after identifying identical physical cells.  For
\(X\) a target set, put

\[
 {\cal C}_{\cal P}(X)=\bigcup_{T\in X}{\cal C}_{\cal P}(T).
\tag{9.2}
\]

There are three increasingly strong supply gates.

1. **Point support**
   \[
   {\cal C}_{\cal P}(T)\ne\varnothing\quad(T\in X).
   \tag{P}
   \]
2. **Scalar family supply**
   \[
   |{\cal C}_{\cal P}(X)|\ge |X|.
   \tag{S}
   \]
3. **Cell Hall**
   \[
   |{\cal C}_{\cal P}(Y)|\ge |Y|
   \quad\text{for every }Y\subseteq X.
   \tag{CH}
   \]

Condition (CH) is equivalent to an injection from targets to distinct
interior cells.  Conditions (P) and (S), even together, do not imply
(CH): many targets may share the same cell neighbourhood.

This failure is exact already on three targets.  Let

\[
 {\cal C}(T_1)={\cal C}(T_2)=\{a\},
 \qquad {\cal C}(T_3)=\{b,c\}.
\tag{9.3}
\]

Then every target is positive and the family has three distinct cells
for three targets, but the two-target shore \(\{T_1,T_2\}\) has
neighbourhood one.  Hence the family totals in (11.7), (11.12) cannot
by themselves certify cell Hall.

There is then a fourth, genuinely chronological gate.  Even a
cell-Hall injection may use cells whose successor arcs are mutually
incompatible.  This is the packability issue treated in Section 13.
For example, two targets with private cells \(a,b\) satisfy (CH), but
are not simultaneously installable if \(a\) and \(b\) demand different
successors at one common source.

## 10. Multiplicity covering under coordinate relabelling

The zero-set argument records only whether \(c_H(T)\) vanishes.  The
complete multiplicity distribution gives a sharper exact design
calculation.

For rank \(s\), define the count enumerator

\[
 F_s(x)={1\over N_s}\sum_{T\in{\cal T}_s}x^{c_H(T)}.
\tag{10.1}
\]

This is a probability generating polynomial: by Lemma 1.1, for a
uniform coordinate permutation \(\sigma\) and any fixed rank-\(s\)
target \(T\),

\[
 {\mathbb E}x^{c_{\sigma H}(T)}=F_s(x).
\tag{10.2}
\]

### Theorem 10.1 (labeled multiplicity cover)

Let \(D\) be a fixed target family, and prescribe an integer demand
\(b_T\ge0\) for every \(T\in D\).  Choose \(t\) coordinate relabels.
Before identifying cells shared by different parents, let

\[
 M_T=\sum_{i=1}^t c_{\sigma_iH}(T)
\tag{10.3}
\]

be the labeled parent-pure cell supply.  If

\[
 \sum_{T\in D}
 \sum_{j=0}^{b_T-1}
 [x^j]\,F_{|T|}(x)^t<1,
\tag{10.4}
\]

then some \(t\) relabel parents satisfy

\[
 M_T\ge b_T\qquad(T\in D).
\tag{10.5}
\]

#### Proof

For fixed \(T\), the random variables
\(c_{\sigma_iH}(T)\) are independent and each has generating function
\(F_{|T|}\), by (10.2).  Hence the generating function of \(M_T\) is
\(F_{|T|}^t\), and

\[
 \Pr(M_T<b_T)
 =\sum_{j=0}^{b_T-1}[x^j]F_{|T|}(x)^t.
\tag{10.6}
\]

The union bound over \(T\in D\) is strictly below one under (10.4).
Therefore a deterministic relabel tuple meets every demand. \(\square\)

For \(b_T=1\), only the constant coefficient of \(F_s\) occurs:

\[
 [x^0]F_s(x)={z_s\over N_s},
\tag{10.7}
\]

and Theorem 10.1 reduces exactly to Theorem A.

The word “labeled” is essential.  Two different parents may expose the
same physical cell, or may expose different cells which demand
incompatible successors.  Formula (10.4) measures orbit supply before
those two collision quotients.  Sections 11--12 perform that separation.

## 11. Exact \(A29,R3,R4\) supply and the minimum parent count

Let \(n_\tau(A)\) be the exact number of compiler cells of the relabel
parent \(\tau H29\) which hit the fixed family \(A\), including both
endpoint palettes.  At most \(36\) of these cells are boundary cells,
so the number \(i_\tau(A)\) of distinct interior cells satisfies

\[
 i_\tau(A)\ge n_\tau(A)-36.
\tag{11.1}
\]

Every such interior cell is residence-safe, because it is a contiguous
subpath of a coordinate relabel of the residence-zero H29 path.

### Proposition 11.1 (raw supply minimum)

Relative to H29, the minimum number of added coordinate-relabel parents
needed for simultaneous point support and scalar interior supply on
\(A29,R3,R4\) is

\[
 \boxed{t_{\rm raw}=1.}
\tag{11.2}
\]

#### Lower bound

With no added parent, the entire H29 neighbourhood of \(A29\), even
including its boundary cells, has size \(1495\).  Since

\[
 1495<1524=|A29|,
\tag{11.3}
\]

condition (S) fails.  Thus \(t_{\rm raw}\ge1\).

#### Upper bound

The single relabel \(\tau=(10,11)\) supplies all seven H29 zeros, by
(0.14).  Its exact fixed-family cell counts are

\[
\begin{array}{c|ccc}
 A&A29&R3&R4\\ \hline
 n_\tau(A)&1579&1873&1695\\
 n_\tau(A)-36&1543&1837&1659\\
 (n_\tau(A)-36)-|A|&19&307&285.
\end{array}
\tag{11.4}
\]

Thus, even after discarding every boundary cell, one relabel has
positive scalar interior slack in all three families.  Together with
H29 it has point support for every target.  This proves
\(t_{\rm raw}\le1\).

Proposition 11.1 is deliberately a (P)+(S) statement.  It does not
assert cell Hall or successor packability.

### The max-min-slack first winner

The first portfolio winner is

\[
 \tau_1=(1,12).
\tag{11.5}
\]

It supplies the seven H29 zeros with vector

\[
 (4,1,4,1,2,1,3)
\tag{11.6}
\]

and has

\[
\begin{array}{c|ccc}
 A&A29&R3&R4\\ \hline
 n_{\tau_1}(A)&1616&1889&1707\\
 n_{\tau_1}(A)-36&1580&1853&1671\\
 (n_{\tau_1}(A)-36)-|A|&56&323&297.
\end{array}
\tag{11.7}
\]

Hence \(\tau_1\) is another one-parent proof of Proposition 11.1, with
a larger minimum normalized DM margin and more new arcs relative to the
initial three-parent catalogue.

After successor selections using this first reserve, twelve further
targets were exposed as zeros in the accumulated round ledger:

\[
\begin{split}
 D_{12}=\{&
 1707,6669,8855,9494,9495,9522,9526,\\
 &17547,21832,25682,29332,29972\}.
\end{split}
\tag{11.8}
\]

The parent \(\tau_1H29\) has positive interior counts on only five of
these twelve:

\[
 (0,0,1,1,1,0,0,0,0,0,1,1).
\tag{11.9}
\]

The second portfolio winner

\[
 \tau_2=(5,7)
\tag{11.10}
\]

supplies all twelve with vector

\[
 (1,4,1,3,1,4,1,4,2,3,1,1),
\tag{11.11}
\]

of total interior mass \(26\), and its family ledger is

\[
\begin{array}{c|ccc}
 A&A29&R3&R4\\ \hline
 n_{\tau_2}(A)&1739&1907&1737\\
 n_{\tau_2}(A)-36&1703&1871&1701\\
 (n_{\tau_2}(A)-36)-|A|&179&341&327.
\end{array}
\tag{11.12}
\]

Thus the chosen pair \(\{\tau_1,\tau_2\}\) is a two-parent
**collision-reserve portfolio**: \(\tau_1\) clears the original seven
zeros with strong family slack, while \(\tau_2\) clears all twelve
zeros subsequently exposed by successor selections.

The number two is not the raw set-cover minimum.  For example,
\(\tau=(10,11)\) is positive on both the original seven and the twelve
targets in (11.8).  The two winners were selected for stronger DM slack,
arc novelty, and distance from the existing parent catalogue.  This is
the first concrete distinction between minimum supply and robust
packability.

## 12. Shared-successor collisions

Let \(P,Q\) be two directed Hamilton paths on the same \(n\)-vertex
middle layer.  Write

\[
 e(P,Q)=|E(P)\cap E(Q)|.
\tag{12.1}
\]

An arc common to \(P,Q\) is compatible.  A **successor collision** is a
vertex \(x\) at which both paths have an outgoing arc but choose
different successors.  A predecessor collision is defined dually.

### Lemma 12.1 (exact disagreement count)

For \(n=6435\),

\[
 6433-e(P,Q)
 \le \gamma^+(P,Q),\gamma^-(P,Q)
 \le 6434-e(P,Q),
\tag{12.2}
\]

where \(\gamma^+\) and \(\gamma^-\) are the numbers of successor and
predecessor collisions.

#### Proof

Each Hamilton path has \(n-1=6434\) arcs.  If the two terminal vertices
coincide, their outgoing domains coincide and every noncommon outgoing
arc gives one collision, so
\(\gamma^+=6434-e(P,Q)\).  If the terminal vertices differ, the common
outgoing domain has size \(n-2=6433\); every common arc lies in that
domain, so \(\gamma^+=6433-e(P,Q)\).  The predecessor statement follows
by applying the same argument to the reversed paths. \(\square\)

For \(\tau_1=(1,12)\), the audited common-arc counts against
\((H29,H30,H31)\) are

\[
 (2353,487,341).
\tag{12.3}
\]

Consequently its successor and predecessor collision counts lie,
respectively, in

\[
 [4080,4081],\qquad [5946,5947],\qquad [6092,6093].
\tag{12.4}
\]

It contributes \(3861\) arcs outside the union of those three parents.

For \(\tau_2=(5,7)\), the common-arc counts against
\((H29,H30,H31,\tau_1H29)\) are

\[
 (2397,434,222,924),
\tag{12.5}
\]

so the corresponding collision intervals are

\[
 [4036,4037],\quad[5999,6000],\quad
 [6211,6212],\quad[5509,5510].
\tag{12.6}
\]

It contributes \(3877\) arcs outside the four-parent union.

Thus the large parent-level cell margins in (11.7) and (11.12) coexist
with thousands of incompatible successor decisions.  Arc novelty is
useful supply, but every novel outgoing choice competes with the
currently selected outgoing choice at the same source, and dually at
its head.

### Physical-cell duplication

An interior depth-\(d\) compiler cell uses a directed motif of
\(9+d\) arcs, for \(d=0,1,2\).  Let the common arcs of \(P,Q\) decompose
into maximal common directed runs of lengths

\[
 r_1,r_2,\ldots,r_m.
\tag{12.7}
\]

The number of identical depth-\(d\) parent-pure motifs shared by the two
parents is exactly

\[
 \kappa_d(P,Q)
 =\sum_{j=1}^m\max\{r_j-(9+d)+1,0\}.
\tag{12.8}
\]

Indeed, a common motif is precisely a consecutive block of \(9+d\)
common arcs, and every such block lies in one unique maximal run.

Hence labeled orbit multiplicities overcount physically distinct cells
by common-run terms.  For any target \(T\) and parents
\(P_1,\ldots,P_t\),

\[
\left|\bigcup_i{\cal C}_{P_i}(T)\right|
\ge
\sum_i|{\cal C}_{P_i}(T)|
-
\sum_{i<j}|{\cal C}_{P_i}(T)\cap{\cal C}_{P_j}(T)|.
\tag{12.9}
\]

Formula (12.8) gives the exact uncoloured overlap ceiling entering the
last sum.

## 13. Supply versus packability theorem

Let \({\cal C}=\bigcup_{T\in A}{\cal C}_{\cal P}(T)\) be the distinct
physical interior cells supplied to a fixed DM family \(A\).  Each cell
\(C\) has a directed arc set \(E(C)\).

Define the **successor-conflict graph** \(G_{\cal P}(A)\) on
\({\cal C}\) by joining distinct cells \(C,C'\) when either

\[
 (x,y)\in E(C),\ (x,y')\in E(C'),\quad y\ne y',
\tag{13.1}
\]

or

\[
 (x,y)\in E(C),\ (x',y)\in E(C'),\quad x\ne x'.
\tag{13.2}
\]

Thus an independent set of cells has a union which is a partial
one-in/one-out successor relation.

There is an additional bounded residence constraint.  A forbidden
depth-three return consists of an insertion transition, at most three
intermediate transitions, and the transition which removes the inserted
coordinate.  Hence it uses at most four directed arcs.  Define the
**local conflict hypergraph** \({\mathfrak F}_{\cal P}(A)\) on
\({\cal C}\) as follows:

1. every edge of \(G_{\cal P}(A)\) is a two-vertex hyperedge; and
2. for every forbidden depth-three directed segment, include every
   inclusion-minimal set of cells whose union contains all arcs of that
   segment.

Every hyperedge in the second class has size between two and four.  It
cannot have size one because every parent-pure cell is residence-safe.

### Theorem 13.1 (exact separation)

For a fixed family \(A\):

1. parent-level supply is (P);
2. distinct-cell supply is (CH); and
3. successor-only local packability is equivalent to the
   existence of an injective map
   \[
   \phi:A\longrightarrow{\cal C},
   \qquad \phi(T)\in{\cal C}_{\cal P}(T),
   \tag{13.3}
   \]
   whose image is an independent set of \(G_{\cal P}(A)\); and
4. residence-safe local successor packability is equivalent to (13.3)
   with image independent in \({\mathfrak F}_{\cal P}(A)\).

In particular, (P), (S), and even (CH) do not imply packability.

#### Proof

If a selected successor factor installs one distinct parent-pure cell
for every target, assigning that cell to its target gives (13.3).
The one-out and one-in constraints prohibit (13.1) and (13.2), so the
image is independent in \(G_{\cal P}(A)\).  Residence safety additionally
prohibits every hyperedge of the second class.

Conversely, if (13.3) exists, the union of all arcs in the selected
cells has at most one outgoing and at most one incoming arc at every
middle vertex.  Thus graph independence gives a partial successor
factor.  If the image is independent in \({\mathfrak F}_{\cal P}(A)\),
its union contains no forbidden depth-three segment: any such segment
would generate one of the minimal hyperedges in class 2.  Hence the
partial factor is residence-safe and carries one distinct cell for
every target. \(\square\)

The theorem concerns local installation.  Extending the partial
successor relation to one connected Hamilton path while preserving all
upper shadows is a further global requirement.

### A self-contained successor-packing bound

Let

\[
 \Delta=\Delta(G_{\cal P}(A)),\qquad
 m=\min_{T\in A}|{\cal C}_{\cal P}(T)|.
\tag{13.4}
\]

If

\[
 m>(|A|-1)(\Delta+1),
\tag{13.5}
\]

then a map (13.3) exists.

To prove this, order the targets arbitrarily and choose their cells
greedily.  After \(j\) choices, at most \(j(\Delta+1)\) candidates of
the next target are forbidden by equality or conflict with an earlier
cell.  Condition (13.5) leaves one available cell through the last
step.

There is a useful port-load estimate for \(\Delta\).  Every interior
cell uses at most

\[
 L=11
\tag{13.6}
\]

arcs.  Put

\[
\begin{split}
 \Lambda^+&=\max_x
 |\{C\in{\cal C}:C\text{ uses an arc with tail }x\}|,\\
 \Lambda^-&=\max_y
 |\{C\in{\cal C}:C\text{ uses an arc with head }y\}|.
\end{split}
\tag{13.7}
\]

Then

\[
 \Delta\le L(\Lambda^++\Lambda^-)-1.
\tag{13.8}
\]

Indeed, a conflicting cell must meet one of at most \(L\) used tails
or one of at most \(L\) used heads.  Summing the corresponding port
loads proves (13.8).

The current family totals do not imply either (13.5) or a sharper
independent-transversal theorem: they contain no bound on
\(\Lambda^\pm\) and no coloured conflict expansion.  The collision
intervals (12.4), (12.6) show why that omission is material.

For a sufficient residence-safe version, take the two-section
\(G^*_{\cal P}(A)\) of \({\mathfrak F}_{\cal P}(A)\): join every pair
of cells lying in one common hyperedge.  An independent set in \(G^*\)
is independent in the hypergraph.  Therefore (13.5) remains a
self-contained sufficient condition after replacing \(\Delta\) by
\(\Delta(G^*_{\cal P}(A))\).  The price is that this two-section can be
strictly stronger than necessary.  No bound for its residence part is
presently supplied by the family-total ledgers.

## 14. Updated Lane-B verdict

The exact raw coordinate-parent requirement is

\[
 t_{\rm raw}=1.
\tag{14.1}
\]

One relabel is necessary because H29 has only \(1495\) cells against
the \(1524\)-target family \(A29\), and one is sufficient by either
\(\tau=(10,11)\) or the stronger first winner \(\tau_1=(1,12)\).

The selected two-parent reserve

\[
 \{(1,12),(5,7)\}
\tag{14.2}
\]

has substantially stronger family margins and covers both the original
seven-zero ledger and the twelve collision-exposed targets.  But the
number two is a portfolio choice, not a proved packability threshold.

The remaining exact parameter is

\[
 D_*:=A29\cup R3\cup R4
\tag{14.3}
\]

and

\[
 t_{\rm pack}
 =\min\{t:\text{the coloured conflict hypergraph on }D_*
          \text{ admits (13.3)}\}.
\tag{14.4}
\]

The current proof establishes only

\[
 t_{\rm pack}\ge t_{\rm raw}=1;
\tag{14.5}
\]

it does not prove that the two winners attain \(t_{\rm pack}\), because
their thousands of successor/predecessor disagreements have not been
packed into a common independent transversal.  The next decisive audit
is therefore not another marginal target count.  It is the coloured
successor-conflict Hall problem on the parent-pure cells of
\(H29,\tau_1H29,\tau_2H29\), followed by extension of the resulting
partial successor relation to a residence-safe all-upper Hamilton path.
