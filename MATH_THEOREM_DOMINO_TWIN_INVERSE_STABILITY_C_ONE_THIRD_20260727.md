# Domino-twin inverse stability with exponent \(1/3\)

> **RETRACTED (2026-07-27).**  Theorem 0.1 and Lemma 2.1 are false.
> A synchronized two-front re-pairing family has defect at most
> \(8u+16\) and cardinality
> \(\exp((4-o(1))u\log u)\), forcing every bound
> \(e^{O(m)}n^{cs}\) to have \(c\ge1/2\).  See
> `MATH_AUDIT_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md`,
> Section 4.  The survivor conclusion in Section 4 also omits the size
> of the first allowed overlap shell.

Date: 2026-07-27

> **RETRACTED (2026-07-27).**  Lemma 2.1's row claiming that a
> two-target top anchor releases no element label is false.  A genuine
> top-only shared edge leaves two arbitrary endpoint mates; see
> `MATH_COUNTERAUDIT_DOMINO_ZIPPER_TWO_POINT_ANCHOR_20260727.md` and
> `MATH_AUDIT_DOMINO_TWIN_STAR_TO_TOP_DEFERRED_MATE_CHARGE_20260727.md`.
> More decisively, the theorem's numerical conclusion is false uniformly
> for \(s=o(m)\): the aligned double-segment family in
> `MATH_AUDIT_DOMINO_DOUBLE_SEGMENT_HALF_EXPONENT_AND_COLLAR_OVERLAP_20260727.md`
> has list exponent \(1/2-o(1)\).  The text below is retained only as the
> superseded argument being audited.

> **Audit status: retracted.**  Lemma 2.1's load-bearing assertion that
> a two-target top-phase anchor releases no label is false: the common
> edge fixes the \((r+1)\)-domino carrier but leaves an arbitrary
> endpoint domino.  The paired recurrence encounters the same unknown
> two-set again and does not determine its two members.  Moreover the
> globally aligned two-segment family contradicts the numerical
> \(\exp(Cm)n^{s/3}\) bound for \(s=o(m)\).  See
> MATH_AUDIT_PAIRED_WINDOW_ZIPPER_PHASE_RELEASE_INVERSE_FAILURE_20260727.md.
> The text below is retained as the retracted argument, not as a theorem.

## 0. Statement

Put

\[
 n=2m,\qquad R=2r+1,\qquad 1<r<m-1,\qquad K=4m=2n,
\]

and let \(\mathcal H^\square\) be the simple domino-twin packet
catalogue.  In the annular application \(R=m-q_0\) is odd and
\(q_0=O(\sqrt m)\); no identity between \(2r+1\) and the number \(m\)
of dominoes is assumed.  For a
fixed packet \(F\), write

\[
 B_s(F)=\{G\in\mathcal H^\square:|F\setminus G|\le s\}.
\]

> **Theorem 0.1 (inverse stability).**  There is an absolute constant
> \(C\) such that, uniformly for \(s=o(m)\),
> \[
> \boxed{
> |B_s(F)|\le \exp(Cm)n^{s/3}.}
> \tag{0.1}
> \]
> Consequently
> \[
> \#\{G:|F\cap G|\ge K-s\}
> \le \exp(Cm)n^{s/3}.                                  \tag{0.2}
> \]

The exponent is strictly below the survivor threshold \(1/2\).  The
contiguous re-pairing construction in the macro-overlap note gives the
lower exponent \(1/4-o(1)\), so (0.1) leaves only the genuine interval

\[
 \frac14\le c\le\frac13
\]

between the known lower and upper list exponents.

The proof below is a list-decoding proof for the literal four-target
cell word.  The point which improves the former \(n^{3s}\) trace count
is that a cell containing a common edge is an **anchor**, even when that
edge changes from the star realization in \(F\) to the top realization
in \(G\).  Only cells containing at most one common target release a
letter of the paired cyclic word, and every such cell spends at least
three units of the defect.

## 1. Four-target cells and the two sorts of anchors

Write the paired cyclic word of \(F\) as

\[
 (B_0,B_1,\ldots,B_{m-1}),\qquad |B_i|=2,
\]

with indices modulo \(m\), and put

\[
 A_i=B_i\cup B_{i+1}\cup\cdots\cup B_{i+r-1},
 \qquad
 Q_i=B_{i-1}\cup B_{i+r}.
\]

Then the support of \(F\) is the disjoint union

\[
 \mathcal S_i(F)=\{A_i\cup\{x\}:x\in Q_i\},
 \qquad i\in\mathbb Z_m.                               \tag{1.1}
\]

For a second packet \(G\), define

\[
 J_i=\mathcal S_i(F)\cap G,qquad
 d_i=4-|J_i|.                                           \tag{1.2}
\]

Thus

\[
 |F\setminus G|=\sum_i d_i.                            \tag{1.3}
\]

Call \(i\) an **edge anchor** when \(|J_i|\ge2\), and weak otherwise.
If \(|J_i|=3\), the three common sets have intersection of size
\(R-1\), so they can only lie in a canonical star \(K_4\) of \(G\);
they cannot lie in a top \(K_4\), three of whose members have
intersection of size \(R-2\).  Hence they recover the star core
\(A_i\).  The same is of course true when \(|J_i|=4\).

If \(|J_i|=2\), let its members be \(X,Y\).  In the Johnson graph they
form an edge.  The exact local clique census for a twin packet says that
every packet edge is contained in its canonical star or its canonical
top (and a mate edge is contained in both).  Therefore there are at most
two possibilities:

\[
 \begin{array}{c|c}
 \text{star phase}&X\cap Y\text{ is the union of }r
                     \text{ consecutive }G\text{-dominoes},\\[1mm]
 \text{top phase}&X\cup Y\text{ is the union of }r+1
                     \text{ consecutive }G\text{-dominoes}.
 \end{array}                                             \tag{1.4}
\]

This is the complete star-to-top ambiguity.  Recording one bit at every
two-point anchor records all such coincidences, at total cost at most
\(2^m=\exp(O(m))\).  Notice in particular that a star-to-top edge does
not release an element label.

Nor does an anchor require an unrecorded choice of one of \(m\) packet
positions.  After the complete cells have been globally aligned, take
the nearest complete cells on the two sides of the anchor.  Their core
distances to \(X\cap Y\) in the star phase, or to \(X\cup Y\) in the
top phase, give the two cyclic distances to the anchor.  Since the
intervening gap has length at most \(s<\min(r,m-r)-2\), these two
distances determine its position and orientation.  The mate-edge case
has the two phase choices already recorded above.  Thus anchor placement
also has only finite branching.

Here the assertion about packet edges is not being inferred merely from
the clique-number bound.  It follows directly from (1.1): comparing two
members and cancelling their common complete dominoes shows that a
Johnson-distance-one pair either has the same \(A_i\) (the star case) or
uses the two shores of one sliding-window transition (the top case).
Those are exactly the two canonical \(K_4\)'s.  Thus there is no third
loose-edge case hidden in (1.4).

## 2. The paired-window zipper

We use the following elementary decoding lemma.  It is stated separately
because it is useful outside the present inverse theorem.

> **Lemma 2.1 (paired-window zipper).**  Fix a cyclic word in disjoint
> unordered two-sets and its four-target cells (1.1).  Fix a second such
> word, one complete common cell (which fixes the global dihedral
> alignment), the sets \(J_i\), and, at every edge anchor, one of the at
> most two phases in (1.4).  If \(w\) of the indices are weak, then the
> number of second paired words realizing these data is at most
> \[
> C^m n^w.                                               \tag{2.1}
> \]

### Proof

Let \(C_j\) denote the dominoes of the second word and let

\[
 W_j=C_j\cup C_{j+1}\cup\cdots\cup C_{j+r-1}.
\]

At a star anchor (1.4) specifies \(W_j\); at a top anchor it specifies
\(W_j\cup C_{j+r}\).  The phase and the two neighbouring phases tell
which of these two alternatives is being used.  There are only eight
endpoint states (star/top, orientation, and which shore of the mate
edge), so all endpoint-state choices cost \(C^m\).

Between consecutive anchors expose the unknown word simultaneously at
its two window fronts.  The two recurrences are

\[
 W_{j+1}=(W_j\setminus C_j)\cup C_{j+r},
 \qquad
 W_{j-r+1}=(W_{j-r}\setminus C_{j-r})\cup C_j.          \tag{2.2}
\]

Thus the domino which leaves the transition at \(j\) is the domino which
enters the paired transition at \(j-r\).  This is the
``zipper'': an unordered pair is never chosen independently at both
fronts.

The local exposure has the following exhaustive table.  Here \(k\) is
the number of prescribed common members of the current four-cell and
``free letters'' means element labels not determined by the already
exposed two fronts.

\[
\begin{array}{c|c|c}
k&\text{information supplied}&\text{new free letters}\\ \hline
4&\text{complete star cell}&0\\
3&\text{star core and three boundary letters}&0\\
2&\text{star core or top union; one phase bit}&0\\
1&\text{one boundary equation}&\le1\\
0&\text{no equation at this front}&\le1
\end{array}                                             \tag{2.3}
\]

Here is the exact injection behind the last two lines.  Regard the two
identities (2.2), for all \(j\), as a two-front exposure graph.  A
domino \(C_j\) has precisely two occurrences in this graph: it leaves at
the \(j\)-front and enters at the \((j-r)\)-front.  Traverse every
component, starting at its first anchor.  If a component has no anchor,
start at its least weak index (this spends that weak index).

Whenever an element label is not forced by the exposed anchors and
earlier recurrences, call its first occurrence a **release**.  Assign
the release to its current front cell.  The other member of the same
domino is first encountered at the paired front in (2.2), and is
assigned there unless already forced.  Therefore two releases from one
domino are assigned to its two distinct front cells.  A front cell
containing a common edge cannot receive a release: in the star phase the
intersection and the two displayed boundary labels are known, while in
the top phase the union and the two omitted boundary labels are known.
Taking the appropriate set difference in (2.2) supplies the current
label.  Thus every release is assigned to a weak cell.

The assignment is injective.  After a release has been assigned at a
front, (2.2) fixes the outgoing/entering occurrence before that front is
visited again; a second unforced label at the same front would constitute
a second unknown domino occurrence, which the displayed recurrence does
not have.  This proves
\[
 \#\{\text{released element labels}\}\le
 \#\{\text{weak cells}\}=u.                             \tag{2.4}
\]
This argument also handles cyclic wrap and arbitrary
\(\gcd(r,m)\): an anchor-free component is started at one of its own
weak cells, and the closing recurrence forces its last label.  No
identity \(2r+1=m\) is used.

Once the identities of the released labels are recorded, all dominoes,
their order, and their pairing are forced by (2.2) and the phase record.
There are at most \(n^u\) possible release records.  An interval whose
two endpoint anchors use different phases only starts or ends the zipper
one half-step later; this changes one of the finite endpoint states and
does not create a release.  These are exactly the star-to-top
shared-edge cases.

One can equivalently verify (2.3) by taking set differences in (2.2):
three or four members give their common \((R-1)\)-core, two give either
their intersection or union, one fixes one of the two boundary labels,
and zero postpones that same boundary label to the opposite recurrence.
No case releases a whole unordered pair.

Every free letter has at most \(n\) values.  Multiplying over the
anchor-free intervals and the finite endpoint states proves (2.1).
\(\square\)

Two details in this lemma are important.  First, the two fronts must be
exposed together; exposing a single Johnson trace is exactly what loses
the former factor \(n^{3s}\).  Second, a two-point star-to-top
coincidence is an endpoint-state bit, not a free label.  Treating it as
a new path start is another way to incur the spurious power of \(n\).

## 3. Proof of inverse stability

Fix \(F\), and consider \(G\in B_s(F)\).  Since the cells of \(F\) are
disjoint, at most \(s\) of them are incomplete.  As \(s=o(m)\), there
are two consecutive complete cells.  The global-alignment lemma in the
macro-overlap note therefore gives one rotation or reflection after
which every complete common cell has the same index in the two packet
words.  There are only \(2m=\exp(O(m))\) choices for this alignment.

Record the following data:

1. every set \(J_i\subseteq\mathcal S_i(F)\) (at most \(16^m\)
   possibilities);
2. the star/top bit at every two-point anchor (at most \(2^m\)); and
3. the finite endpoint states in Lemma 2.1 (at most \(C^m\)).

This costs \(\exp(O(m))\).  If \(w\) is the number of weak cells, then
each weak cell has \(d_i\ge3\), and hence

\[
 3w\le\sum_i d_i=|F\setminus G|\le s.                  \tag{3.1}
\]

For each fixed record Lemma 2.1 gives at most \(C^mn^w\) packets.
Using (3.1) and absorbing all finite records gives

\[
 |B_s(F)|\le\exp(Cm)n^{s/3},
\]

which is (0.1).

## 4. Survivor comparison

At the stopping density \(z=m^{-1/2}\), a pair with overlap \(K-s\)
has tilt

\[
 z^{-(K-s)}=exp((2m-s/2)\log m).
\]

After conflict thinning using (0.1), the loss in logarithmic degree is
at most

\[
 Cm+\frac{s}{3}\log n.
\]

Combining this with \(\log D=2m\log m-O(m)\) leaves

\[
 -\frac{s}{6}\log m+O(m).                              \tag{4.1}
\]

Thus taking \(s=A m/\log m\) with a sufficiently large fixed \(A\)
makes the macroscopic survivor contribution exponentially small.  The
remaining annular task is no longer inverse stability; it is to propagate
the already proved static factorial-overlap estimates through the stopped
trajectory after this quarantine.

## 5. Sharpness information

Re-pairing the \(2\ell\) labels in one contiguous \(\ell\)-domino
segment gives

\[
 \frac{(2\ell)!}{2^\ell(2m)}
\]

distinct packets at defect at most \(8\ell+8\).  Hence no estimate of
the form \(\exp(O(m))n^{cs}\) can have \(c<1/4-o(1)\).  The theorem's
\(1/3\) is therefore within the exact admissible interval and, crucially,
is already on the correct side of the stopped threshold \(1/2\).
