# Internal dominance collapses the all-width upper guard

Date: 2026-07-31  
Lane: A, full-signature buffered C6/ECO upper compression  
Status: exact unary-dominance composition and row-energy theorem proved;
the abstract fixed-4 C6 serialization has exact graded internal-deck equality;
one antipodal physical seam and equal-length materialization remain

## 0. Verdict

Full prefix/suffix signature and one internal-deck inclusion are sufficient
to preserve the entire old upper coverage under a local replacement:

\[
 \Sigma_\vee(X)=\Sigma_\vee(Y),\qquad
 {\cal D}(X)\subseteq{\cal D}(Y).                                \tag{0.1}
\]

The first row preserves every crossing interval pointwise.  The second row
rehosts every old internal interval value somewhere inside the new packet.
Although a length-\(O(d)\) block has \(\Theta(d^2)\) internal intervals,
(0.1) is one unary legality check on a candidate.  Those interval values do
not become \(\Theta(d^2)\) cross-list semantic tickets.

Consequently the full protected row energy remains \(O(dm^3)\) provided:

* the combined signature/dominance failure graph has an \(O(d)\) star cover;
* the packet has only \(O(d)\) physical/local tokens of full-atlas exposure
  \(O(m^3)\); and
* the equal-length suspension uses one distinct source-private unused-cell
  token.

There is a genuine positive local identity.  The signature-transparent
fixed-4 serialization from the companion note has not only equal boundary
signature but identical internal union multisets at every length.  Thus its
upper guard is completely neutral.  It still has one Johnson-distance-two
seam in each phase, so it is not yet a literal tight owner packet.

## 1. Internal union decks

For a length-\(h\) fragment \(X\), define the ungraded internal union deck

\[
 {\cal D}(X)=
 \left\{\bigcup_{i=s}^tX_i:1\le s\le t\le h\right\}               \tag{1.1}
\]

as a set of target values.  If width or multiplicity matters, define
\({\cal D}_q(X)\) to be the multiset of unions of the length-\(q\) internal
intervals.

### Theorem 1.1 (unary upper-dominance replacement)

Let \(W=LXS\) and \(W'=LYS\), with \(X,Y\) at the same address and of the
same length.  If

\[
                         \Sigma_\vee(X)=\Sigma_\vee(Y)             \tag{1.2}
\]

and

\[
                         {\cal D}(X)\subseteq{\cal D}(Y),          \tag{1.3}
\]

then every interval-union target covered by \(W\) is covered by \(W'\).

If the stronger graded multiset relations

\[
                         {\cal D}_q(X)\subseteq{\cal D}_q(Y)
                         \quad(1\le q\le h)                        \tag{1.4}
\]

hold, then every internal width and multiplicity is nondecreasing as well.

#### Proof

An old interval disjoint from the slot is unchanged.  An old interval which
meets the slot but is not internal has exactly the same union at the same
address by boundary-signature transparency.  An old interval internal to
\(X\) has a value in \({\cal D}(X)\), hence by (1.3) is the value of an
internal interval of \(Y\).  This proves target coverage.  The same argument
within each width and with multiplicities proves (1.4). \(\square\)

The theorem is about existential contiguous-OR coverage.  Set inclusion in
(1.3) does not preserve occurrence ownership, addresses, multiplicities or
a width-graded compiler state; those require (1.4) or their separately
declared ledgers.

### Theorem 1.2 (disjoint unary replacements compose)

Let \(X_1,\ldots,X_t\) be pairwise position-disjoint slots.  If every
replacement \(X_i\to Y_i\) satisfies (1.2)--(1.3), then applying all
replacements preserves every target covered by the old word.

The statement is also valid on a cycle with fixed slot addresses.

#### Proof

Apply Theorem 1.1 one slot at a time.  A replacement-generated internal
witness lies wholly in its new slot, so every later disjoint replacement
leaves it unchanged.  Crossing intervals remain pointwise invariant at each
step.  The cyclic prefix-union-plus-suffix-union case is covered by the
cyclic boundary-signature theorem. \(\square\)

This is why the \(\Theta(d^2)\) internal values need not be carried as
global witness tokens: the local deck test certifies them all before packet
selection.

## 2. Combined bad-pair graph

For a \((b,c)\)-packet menu, define

\[
\begin{aligned}
 E(G_\Sigma)
   &=\{(b,c):\Sigma_\vee(X_{b,c})\ne\Sigma_\vee(Y_{b,c})\},\\
 E(G_{\cal D})
   &=\{(b,c):{\cal D}(X_{b,c})\nsubseteq{\cal D}(Y_{b,c})\}.
\end{aligned}                                                     \tag{2.1}
\]

The exact upper-legality graph under the interface of Theorem 1.1 is

\[
                         G_{\rm up}=G_\Sigma\cup G_{\cal D}.       \tag{2.2}
\]

### Proposition 2.1 (star-cover audit)

If \(Q_\Sigma\) and \(Q_{\cal D}\) are vertex covers of the two graphs, then
\(Q_\Sigma\cup Q_{\cal D}\) covers \(G_{\rm up}\).  Hence

\[
 |Q_\Sigma|+|Q_{\cal D}|\le Kd
 \quad\Longrightarrow\quad
 |E(G_{\rm up})|\le Kmd.                                         \tag{2.3}
\]

Conversely, internal dominance being a unary predicate does not imply that
\(G_{\cal D}\) has a small cover.  Its failed parameter pairs can form an
arbitrary bipartite graph.  The cover row must be proved from the packet
algebra.

#### Proof

The union of covers covers the union graph.  Every cover vertex is incident
with at most \(m\) parameter pairs, giving (2.3). \(\square\)

Thus the dominance refinement removes semantic-ticket energy, not the need
to retain a quadratic candidate list.

The arbitrariness assertion has a literal rank-two Johnson realization.
Put

\[
 X=(12,13,12),\qquad Y=(12,23,12).                                \tag{2.3a}
\]

The two words have the same prefix/suffix signature, but
\[
 {\cal D}(X)=\{12,13,123\},\qquad
 {\cal D}(Y)=\{12,23,123\},
\]
so \(X\to Y\) loses target \(13\).  Given any bipartite parameter-edge set
\(E\), use \(Y\) on pairs in \(E\) and \(X\) on pairs outside \(E\).
Then \(G_\Sigma\) is empty and \(G_{\cal D}=E\).  In particular, even
\(|E|=m\) can have \(\tau(E)=m\) when \(E\) is a perfect matching.

### Theorem 2.2 (raw anchored C6 combined obstruction)

Let

\[
 Z_{b,c}=(C,\ C+a,\ C-b+a,\ C-b+a+c,\ C-b+c,\ C+c)               \tag{2.4}
\]

be the raw anchored C6 chronology, and fix the off-state
\(Z_{b_0,c_0}\).  Under the combined signature-plus-internal-dominance
interface, the only safe pair is

\[
                              (b,c)=(b_0,c_0).                    \tag{2.5}
\]

Consequently, for \(m\ge2\),

\[
 G_{\rm up}=K_{m,m}-\{(b_0,c_0)\},\qquad
 |E(G_{\rm up})|=m^2-1,\qquad
 \tau(G_{\rm up})=m.                                             \tag{2.6}
\]

#### Proof

The raw signature calculation in the companion note forces \(c=c_0\).
Now consider the old length-two internal target

\[
                              T=C-b_0+a+c_0.
\]

The five length-two unions of \(Z_{b,c_0}\) are

\[
 U,\quad U,\quad C-b+a+c_0,\quad C-b+a+c_0,\quad C+c_0.
\]

Since \(a,c_0\notin C\) are distinct, the old value \(T\) occurs in the
new length-two deck only when \(b=b_0\).  Thus even the upper-only
length-two deck dominance fixes \(b\); singleton-owner coverage is not used.
The graph calculation is immediate, and \(K_{m,m}\) with one edge deleted
still has a perfect matching for \(m\ge2\). \(\square\)

So internal dominance strengthens, rather than repairs, the raw fixed-slot
C6 supply obstruction.  A positive quadratic menu must use a different
serialization or candidate-dependent off-slots.

## 3. Row energy with unary internal certification

Assume each raw list has \(m^2\) candidates and the combined upper graph
(2.2) rejects at most \(Kmd\).  Put

\[
                         \alpha=1-\frac{Kd}{m}>0.                 \tag{3.1}
\]

Suppose every retained packet uses at most \(s_0d+s_1\) physical/local
tokens, each having full eligible-atlas opposite exposure at most
\(\lambda m^3\).  If unequal native packet sizes are balanced by an
unused-cell deletion token \(\delta_e\), assume

\[
 \delta_e\ne\delta_f\quad(e\ne f),\qquad
 \delta_e\text{ occurs in no candidate outside list }e.           \tag{3.2}
\]

### Theorem 3.1 (dominance-compressed protected energy)

Let \(R_m=18m^3+51m^2-4m-5\) be the exact raw C6 row energy.  Then every
retained list has full row energy at most

\[
 \frac{R_m}{\alpha}
   +\lambda(s_0d+s_1)m^3.                                        \tag{3.3}
\]

There is no \(\Theta(d^2)\) semantic term.

#### Proof

Signature and deck dominance are unary candidate predicates.  Failed
candidates are deleted; restricting a list can only lower the raw conflict
numerator, while division by its remaining size costs at most
\(\alpha^{-1}\).  For the local tickets, sum their opposite exposure over
at most \(s_0d+s_1\) tickets per candidate and average over the list.  This
gives the second term.  Condition (3.2) makes the unused-cell token
source-fixed but cross-list private, so it contributes zero external
energy.  Theorem 1.2 supplies simultaneous upper preservation without
additional occurrence tickets. \(\square\)

For \(Kd\le m/2\) and \(d\ge1\), (3.3) is \(O(dm^3)\).  Therefore the
\(m^{-2}\) thinning, two Markov alterations and Haxell extraction in the
protected-row-energy theorem apply whenever \(d=o(m)\).

If the deletion tokens repeat, or one packet's internal witness can be
destroyed from outside its slot, this conclusion is false.  These are
physical/source-privacy failures, not internal-deck failures.

## 4. Exact fixed-4 internal deck

Let \(H\) be fixed and let \(a,b,c,z\) be distinct.  Recall

\[
\begin{aligned}
 X^-={}&(H+ab,\ H+az,\ H+bc,\ H+bz,\ H+cz,\ H+ca),\\
 X^+={}&(H+ab,\ H+bz,\ H+cz,\ H+bc,\ H+az,\ H+ca).
\end{aligned}                                                     \tag{4.1}
\]

The companion note proves
\(\Sigma_\vee(X^-)=\Sigma_\vee(X^+)\).

### Theorem 4.1 (graded multiset neutrality)

For every interval length \(q=1,\ldots,6\),

\[
                         {\cal D}_q(X^-)={\cal D}_q(X^+)          \tag{4.2}
\]

as multisets.  In particular, both directions of the exchange satisfy
internal dominance.

#### Proof

Suppress the common core \(H\).  The complete width table is

\[
\begin{array}{c|c}
q&\text{common multiset of active-coordinate unions}\\ \hline
1&ab,az,bc,bz,cz,ac\\
2&abz,abcz,bcz,bcz,acz\\
3&abcz,abcz,abcz,bcz\\
4&abcz,abcz,abcz\\
5&abcz,abcz\\
6&abcz.
\end{array}                                                       \tag{4.3}
\]

Direct consecutive union in the two words gives the same row in every
case. \(\square\)

Therefore the abstract fixed-4 exchange has

\[
                         G_\Sigma=G_{\cal D}=\varnothing          \tag{4.4}
\]

for each eligible relabeling with four distinct active coordinates, when
that relabeling's \(X^-\) is compared with its own \(X^+\).  It preserves
the full upper interval deck, not only coverage.

This is a candidatewise identity, not yet a quadratic option list at one
task.  Options in one actual list must all replace the same incumbent slot
at the same address.  Varying the relabeling also varies \(X^-\); those
different off-slots cannot be treated as choices in one list unless a
separate common-baseline transport theorem is supplied.

Indeed, with \(H,a,z\) fixed and one incumbent labelled by
\((b_0,c_0)\), the first cell \(H+a+b\) forces \(b=b_0\) and the last cell
\(H+a+c\) forces \(c=c_0\).  The common-incumbent fixed-4 menu therefore
also has only its identical label pair as a full-signature option.

## 5. Physical boundary of the positive identity

Theorem 4.1 does not remove the physical obstruction already isolated in
the companion note:

* \(X^-\) contains the non-Johnson adjacency
  \((H+az,H+bc)\);
* \(X^+\) contains the reverse non-Johnson adjacency
  \((H+bc,H+az)\).

All other internal adjacencies are Johnson edges.  Thus the exact upper
row is solved on this six-owner serialization, while one antipodal physical
seam remains.

Simply cutting the cyclic serialization at that seam does not solve it.
The two resulting first cells are \(H+bc\) and \(H+az\); their symmetric
difference is \(\{a,b,c,z\}\).  A common rank-\((|H|+2)\) owner
Johnson-adjacent to both contains only two of these four active coordinates,
so it cannot mask the first-prefix discrepancy in the fixed-context
criterion.  Nor can one insert a fresh one-step bridge: every common Johnson
neighbor of \(H+az\) and \(H+bc\) is one of
\(H+ab,H+ac,H+bz,H+cz\), all already used in the six-owner block.
An owner-unique repair therefore needs genuinely expanded/rethreaded
support.

The native fixed-4 actuator is a \(2\to3\) atom exchange, whereas Theorem
4.1 uses the virtual balanced \(3\leftrightarrow3\) resource phases.  An
equal-length word materialization must therefore identify one genuinely
unused owner/edge cell on the short side and give it the private token
\(\delta_e\) of (3.2), or construct a different balanced physical
realization.  A formal dummy does not meet the literal-word hypothesis.

Accordingly, the smallest live packet theorem is:

> realize the balanced fixed-4 serialization with one private unused-cell
> token and replace its unique antipodal seam by a Johnson/nonflat connector,
> without changing the full signature or the graded deck, and while retaining
> residence, lower palettes, common cap and topology.

No arbitrary-width upper ticket remains after such a realization.  The
remaining obstruction is physical/compiler, not upper-shadow coverage.

## 6. Scope audit

1. Ungraded deck inclusion preserves target coverage only.  The fixed-4
   identity happens to prove the stronger graded multiset equality.
2. Deck dominance is unary only because slot supports are disjoint and
   boundary signatures compose.  Overlapping/adaptive replacements require
   a joint check.
3. The \(O(dm^3)\) row uses \(O(d)\) physical/local tokens and private
   deletion tokens.  It is not a consequence of dominance alone.
4. The raw anchored C6 chronology still has signature-bad graph
   \(K_{m,m-1}\); internal dominance cannot repair a failed context-free
   boundary signature.
5. The fixed-4 words are exact set words but not yet tight owner
   chronologies because of the displayed distance-two seam.
6. No additive-constant or exact-\(B(k)\) theorem is claimed.
