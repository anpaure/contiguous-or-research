# Lane X: cross-seam repacketization of the verified cyclic-strip packets

Date: 2026-07-25

## 0. Outcome and exact boundary

Let

\[
 k=2m,\qquad W=\binom{2m}{m}.
\]

The verified nonproduct construction in
`MATH_ATTACK_X_NONPRODUCT_PACKET_AGGREGATION_20260725.md` consists of
target-disjoint cyclic strips.  If a selected strip has cyclic length
\(s=2\ell\), its old canonical realization independently initializes a
\((2H+2)\)-block state.  Across \(p\) strips this pays
\((2H+1)p\), which is already \(o(W)\), but the resulting physical word is
sealed into independent packet epochs.  Merely declaring their union to be
one packet does not create cross-seam witnesses.

This report proves the missing band-level repacketization theorem.

1. **Useful-prefix tail inheritance.**  Full residual synchronization is
   unnecessary.  Reverse-writing only the first \(2H+1\) useful blocks of
   the next strip makes its complete band flag exact and leaves the previous
   residual state behind those blocks.  After one initial complement letter
   globally, all selected strips form one genuine MTF chronology.

2. **Exact global ledger.**  If \(U\) is the total unmatched band leave,
   \(u_0\) is its middle-rank part, and

   \[
   2\ell p=W-u_0,
   \]

   then one fully initialized literal word covers the verified band and has
   exact length

   \[
   \boxed{
   n=W+(U-u_0)+2Hp+1.}
   \tag{0.1}
   \]

   Since \(U=o(W)\) and \(H/\ell\to0\), this is \(W+o(W)\).  The one-packet
   state and root surpluses are separately \(o(W)\).

3. **Actual Gaussian-or-larger repacketization.**  Grouping
   \(g=\lceil k/(2\ell)\rceil\) strips at a time gives genuine MTF
   macro-packets, each owning at least \(k\) middle targets.  Both the total
   state surplus and total root surplus are \(o(W)\), with exact formulas in
   Theorem 4.1.  Joining the macro-packets by the same useful-prefix seams
   recovers the one chronology in (0.1).

4. **Wholesale asymmetric recoding.**  The same selected strips may be run
   with lower and upper useful depths

   \[
   a=H+c_-,\qquad b=H+c_+.
   \]

   If \(c_-+c_+=o(\ell)\), the word remains \(W+o(W)\), still covers every
   previously verified band target, and replaces all \(W-u_0\) old
   principal letters by deeper cores.  Thus the construction can perform
   pervasive physical recoding without linear length loss.

5. **Sharper obstruction beyond the verified band.**  If a word covers
   every rank-\(r\) target, at least \(\binom{k}{r}\) of its physical
   letters have size at most \(r\).  Applied at
   \(r=m-H-1\), this proves that every \(W+o(W)\) full-cube completion of
   the old canonical strip word must recode \(W-o(W)\) principal endpoints.
   Even after arbitrary interval recoding, the witnesses for the old lower
   cores must have total overlap \((1-o(1))W\).

Thus the chronology and Gaussian packet-mass gates are solved for the
verified central band.  The remaining missing input is **distinct target
support outside that band**: no theorem here shows that the additional rows
exposed by asymmetric recoding have aggregate leave \(o(W)\).  No full-cube
or coefficient-one conclusion is claimed.

The positive theorem constructs transparent cross-seam **states** and
removes repeated full-state initialization.  The already verified band
witnesses may still be chosen inside their individual strip modules; the
theorem does not assert that a new proper target has a decisive witness
crossing a seam.  Producing such target support outside the old band is part
of the remaining gate.

All constructions and bounds below are integral.  Every update is a literal
nonempty Boolean mask, every advertised target is a literal contiguous OR,
and all floor baselines are exact.

---

## 1. Imported verified strip data

For a selected strip choose disjoint cores \(C,D\subset[2m]\), each of
size \(m-\ell\), and cyclically order the remaining \(2\ell\) coordinates
as

\[
 z_0,z_1,\ldots,z_{2\ell-1}.
\]

Write \(I(i,h)\) for the cyclic interval

\[
 I(i,h)=\{z_i,z_{i+1},\ldots,z_{i+h-1}\},
\]

with indices modulo \(s=2\ell\).

The verified matching theorem supplies \(p\) strips whose targets are
pairwise disjoint in every rank

\[
 m-H,m-H+1,\ldots,m+H.
\]

Every strip contains exactly \(s\) targets in each such rank.  If
\(u_q^\pm\) denotes the unmatched count at rank \(m\pm q\), then

\[
 u_0=W-sp,
 \qquad
 u_q^-=u_q^+=\binom{2m}{m-q}-sp,
\tag{1.1}
\]

and

\[
 U:=u_0+\sum_{q=1}^{H}(u_q^-+u_q^+)=o(W).
\tag{1.2}
\]

The verified parameters also satisfy

\[
 H\to\infty,
 \qquad
 \frac{H}{\ell}\to0,
 \qquad
 H=o(\sqrt m),
 \qquad
 p=\frac{W-u_0}{2\ell}.
\tag{1.3}
\]

Only these already proved facts are imported below.  In particular, no new
matching theorem is assumed.

---

## 2. Asymmetric useful-prefix states

The useful-prefix lemma is stated with different lower and upper depths.
This makes explicit which part of the state is needed for target exposure
and which part may be inherited across a seam.

Fix integers

\[
 0\le a,b<\ell.
\tag{2.1}
\]

Define the lower core

\[
 A_i^{(a)}
 =C\cup I(i+a,\ell-a),
 \qquad |A_i^{(a)}|=m-a,
\tag{2.2}
\]

and the ordered useful prefix

\[
 \Lambda_i^{a,b}
 =\bigl(
 A_i^{(a)},
 \{z_{i+a-1}\},\ldots,\{z_i\},
 \{z_{i-1}\},\ldots,\{z_{i-b}\}
 \bigr).
\tag{2.3}
\]

Empty singleton strings are omitted when \(a=0\) or \(b=0\).  The blocks
in (2.3) are pairwise disjoint.  Their union is

\[
 C\cup I(i-b,\ell+b),
\tag{2.4}
\]

which is proper because \(b<\ell\).  Thus its complement is a nonempty set
of size \(m-b\).

### Lemma 2.1 — tail-independent MTF transition

Let \(\Sigma_i\) be any ordered partition of \([2m]\) whose first blocks
are exactly \(\Lambda_i^{a,b}\); the remaining tail may be arbitrary.
Then

\[
 \boxed{
 M_{A_{i+1}^{(a)}}(\Sigma_i)
 \text{ begins with }\Lambda_{i+1}^{a,b}.}
\tag{2.5}
\]

#### Proof

The consecutive cores obey

\[
 A_{i+1}^{(a)}
 =\bigl(A_i^{(a)}\setminus\{z_{i+a}\}\bigr)
   \cup\{z_{i+\ell}\}.
\tag{2.6}
\]

After the update, the new core is first.  It is followed by the consecutive
singleton blocks

\[
 \{z_{i+a}\},\{z_{i+a-1}\},\ldots,\{z_i\}.
\]

The portion through \(\{z_{i+1}\}\) is the new future queue.  This also
covers \(a=0\), when that future queue is empty and \(\{z_i\}\) is the
residue of the old first block rather than an old explicit marker.

If \(b\ge1\), \(\{z_i\}\) is the first new past marker and the retained
older past markers are

\[
 \{z_{i-1}\},\ldots,\{z_{i-b+1}\}.
\]

The oldest old marker \(\{z_{i-b}\}\) is then allowed to fall into the
unrestricted tail.  If \(b=0\), there is no desired past queue and
\(\{z_i\}\) itself simply begins that unrestricted tail.  The entering
coordinate \(z_{i+\ell}\) is deleted from whichever old block contained
it.  Since \(b<\ell\), it is not one of the retained past markers.  These
are exactly the blocks in
\(\Lambda_{i+1}^{a,b}\), in the required order. \(\square\)

### Lemma 2.2 — exact exposed rows

The prefix unions of every state beginning with \(\Lambda_i^{a,b}\)
contain

\[
 \boxed{
 C\cup I(i+q,\ell-q),
 \qquad 0\le q\le a,}
\tag{2.7}
\]

at rank \(m-q\), and

\[
 \boxed{
 C\cup I(i-q,\ell+q),
 \qquad 1\le q\le b,}
\tag{2.8}
\]

at rank \(m+q\).  As \(i\) runs through \(\mathbb Z_s\), these are the
entire corresponding strip rows.

#### Proof

Starting from \(A_i^{(a)}\), add the first \(a-q\) future singleton
blocks.  Their union is (2.7).  Adding all \(a\) future blocks gives the
middle target \(C\cup I(i,\ell)\); adding the first \(q\) past blocks then
gives (2.8).  Cyclic translation of \(i\) enumerates every start. \(\square\)

### Lemma 2.3 — transparent useful-prefix reset

Let

\[
 \Lambda=(B_1,\ldots,B_h),
 \qquad h=1+a+b,
\tag{2.9}
\]

be the useful prefix of a new strip.  From any current full MTF state,
appending

\[
 B_h,B_{h-1},\ldots,B_1
\tag{2.10}
\]

produces a state beginning exactly with \(\Lambda\).  Behind it remains the
old state with \(B_1\cup\cdots\cup B_h\) deleted.

#### Proof

The blocks in (2.10) are disjoint.  Their last-occurrence times are in the
reverse of the writing order, so the new state begins
\(B_1,\ldots,B_h\).  Coordinates outside their union were not updated and
retain their previous relative order. \(\square\)

This differs decisively from a full reset.  The masks in (2.10) cover only
the proper set (2.4), not all of \([2m]\); the previous residual tail is
therefore inherited rather than erased.

---

## 3. One global chronology

The next theorem applies to strips of possibly different lengths and useful
depths.  It is the exact cross-seam repacketization statement.

### Theorem 3.1 — global useful-prefix repacketization

Let \(\alpha=1,\ldots,p\) index cyclic-strip pieces.  Piece \(\alpha\)
has \(s_\alpha=2\ell_\alpha\) principal states and useful depths
\((a_\alpha,b_\alpha)\), with

\[
 0\le a_\alpha,b_\alpha<\ell_\alpha.
\]

Then the pieces can be traversed in any prescribed order by one fully
initialized literal MTF chronology of exact length

\[
 \boxed{
 n_{\rm prin}
 =\sum_{\alpha=1}^{p}s_\alpha
  +1+
   \sum_{\alpha=1}^{p}(a_\alpha+b_\alpha).}
\tag{3.1}
\]

Every strip row in the depths

\[
 -a_\alpha,-a_\alpha+1,\ldots,b_\alpha
\]

is exposed literally on its own piece.

#### Proof

For the first piece, let \(V\) be the union of its useful-prefix blocks.
Emit the nonempty complement \(V^c\), followed by the useful-prefix blocks
in reverse order.  The current full ordered partition is now exactly the
useful prefix followed by \(V^c\).  Emit the remaining
\(s_1-1\) principal updates.  Lemmas 2.1--2.2 expose all advertised rows.

At every later seam, emit only the next useful-prefix blocks in reverse
order.  Lemma 2.3 makes that prefix exact while inheriting the old tail.
Then emit the next \(s_\alpha-1\) principal updates.

The first piece costs

\[
 1+(1+a_1+b_1)+(s_1-1)
 =s_1+a_1+b_1+1.
\]

Every later piece costs

\[
 (1+a_\alpha+b_\alpha)+(s_\alpha-1)
 =s_\alpha+a_\alpha+b_\alpha.
\]

Summation gives (3.1).  Every emitted mask is nonempty. \(\square\)

If one permits the standard unseen-coordinate tail before its first positive
occurrence, the initial complement letter may be omitted and the right side
of (3.1) decreases by one.  We retain it throughout so that every state is
a fully initialized ordered partition and every prefix chain has its literal
suffix interpretation.

### Corollary 3.2 — exact ownership ledger with repair

Suppose piece \(\alpha\) owns \(M_\alpha\) middle targets.  After the
principal chronology, append \(U\) uncovered targets literally, of which
\(u_0\) are middle targets, and assume

\[
 \sum_\alpha M_\alpha+u_0=W.
\tag{3.2}
\]

Then one global chronology covers all advertised targets and has exact
length

\[
 \boxed{
 n=W
  +\sum_\alpha(s_\alpha-M_\alpha)
  +(U-u_0)
  +1
  +\sum_\alpha(a_\alpha+b_\alpha).}
\tag{3.3}
\]

#### Proof

Appending an uncovered nonempty target \(X\) makes \(X\) the first block
of the next state, so the one-letter suffix represents it.  Add \(U\) to
(3.1) and subtract the exact baseline (3.2). \(\square\)

Thus the following conditions are sufficient for a partial family
containing a full middle layer:

\[
 \sum_\alpha(s_\alpha-M_\alpha)=o(W),
 \qquad
 U-u_0=o(W),
 \qquad
 \sum_\alpha(a_\alpha+b_\alpha)=o(W).
\tag{3.4}
\]

No independent full-state reset is paid in (3.3): there is one initial full
state and every later residual tail is inherited.  Physically, the word is
still a sequence of strip modules joined by useful-prefix reset strings; its
new assertion is that these strings belong to one legal nonsealed chronology.

### Corollary 3.3 — the verified symmetric construction

Apply Corollary 3.2 with

\[
 s_\alpha=2\ell,
 \qquad
 M_\alpha=2\ell,
 \qquad
 a_\alpha=b_\alpha=H.
\]

Then

\[
 \boxed{
 n=W+(U-u_0)+2Hp+1.}
\tag{3.5}
\]

Moreover

\[
 \frac{2Hp}{W}
 =\frac{H}{\ell}\left(1-\frac{u_0}{W}\right)
 =o(1),
\tag{3.6}
\]

so \(n=W+o(W)\).

Regard the entire band as one owned packet.  Its first full state has
\(b_{\rm init}=2H+2\) blocks.  If \(t\) is the number of visited states,
then the exact
one-packet ledgers are

\[
\boxed{
 b_{\rm init}-1=2H+1,}
\tag{3.7}
\]

and

\[
 \boxed{
 t-W=(U-u_0)+2H(p-1).}
\tag{3.8}
\]

Indeed \(n=b_{\rm init}+t-1\), and (3.5) gives (3.8).  Both (3.7) and
(3.8) are
\(o(W)\).  Hence the old small-packet chronology obstruction no longer
applies even formally: all middle ownership and all physical states belong
to one legal walk.

---

## 4. Gaussian-or-larger macro-packets

One global packet is stronger than needed.  The same chronology can be cut
into genuine large MTF macro-packets while keeping both additive ledgers
sublinear.

Put

\[
 s=2\ell,
 \qquad
 g=\left\lceil\frac{k}{s}\right\rceil.
\tag{4.1}
\]

For all sufficiently large \(m\), \(p\ge g\).  Define

\[
 q=\left\lfloor\frac{p}{g}\right\rfloor.
\tag{4.2}
\]

Take \(q-1\) groups of exactly \(g\) strips and put every remaining strip
in the last group.  Thus each group has at least \(g\) and fewer than
\(2g\) strips.  Assign all \(U\) repair targets to the last group.

### Theorem 4.1 — exact macro-packet ledger

For common useful depths \((a,b)\), the preceding groups give genuine MTF
packets satisfying

\[
 \boxed{
 \sum_{\beta=1}^{q}(t_\beta-M_\beta)
 =(p-q)(a+b)+(U-u_0),}
\tag{4.3}
\]

and

\[
 \boxed{
 \sum_{\beta=1}^{q}(b_\beta-1)
 =q(a+b+1).}
\tag{4.4}
\]

Every macro-packet owns at least

\[
 \boxed{sg\ge k}
\tag{4.5}
\]

middle targets.  The total packet excess is exactly

\[
 \boxed{
 p(a+b)+q+(U-u_0).}
\tag{4.6}
\]

#### Proof

Suppose a macro-packet contains \(h\) strips.  Fully initialize its first
useful-prefix state and use tail-inheriting seams for the other \(h-1\)
strips.  Before repair it has

\[
 t=sh+(h-1)(a+b)
\]

states, owns \(M=sh\) middle targets, and begins with
\(a+b+2\) blocks.  Hence

\[
 t-M=(h-1)(a+b),
 \qquad
 b_\beta-1=a+b+1.
\]

The last packet gains \(U\) states and \(u_0\) middle owners, adding
\(U-u_0\) to its state surplus.  Summing \(h-1\) over the \(q\) groups
gives \(p-q\), proving (4.3)--(4.4).  Equation (4.5) follows from the
definition of \(g\), and (4.6) is their sum. \(\square\)

For the verified construction \(a=b=H\),

\[
 (p-q)2H+(U-u_0)=o(W).
\tag{4.7}
\]

Also

\[
 q\le\frac{p}{g}
 \le\frac{W/s}{k/s}
 =\frac{W}{k},
\tag{4.8}
\]

and therefore

\[
 q(2H+1)=o(W).
\tag{4.9}
\]

Thus both ledgers are individually \(o(W)\), and every packet has middle
mass at least \(k\gg\sqrt{k}\).  This proves the Gaussian-or-larger packet
requirement for the verified partial band, not merely by relabeling target
owners but by explicit MTF walks.  Replacing the later macro roots by
useful-prefix seams joins them into the single chronology of Theorem 3.1.

---

## 5. Asymmetric wholesale depth recoding

The useful-prefix theorem also shows how the endpoint-floor obstruction in
Section 7 can be escaped geometrically.

Retain the same verified radius-\(H\) matched strips, but choose

\[
 a=H+c_-,
 \qquad
 b=H+c_+,
 \qquad
 0\le c_-,c_+,
 \qquad
 a,b<\ell.
\tag{5.1}
\]

### Theorem 5.1 — exact asymmetric repacketization

The resulting one chronology still covers every target certified by the
original radius-\(H\) matching and has exact length

\[
 \boxed{
 n=W+(U-u_0)+p(2H+c_-+c_+)+1.}
\tag{5.2}
\]

If

\[
 c_-+c_+=o(\ell),
\tag{5.3}
\]

then \(n=W+o(W)\).  If \(c_->0\), every old principal letter of size
\(m-H\) is replaced by a core of size \(m-H-c_-\).

#### Proof

Lemmas 2.1--2.2 expose every depth between \(-a\) and \(b\), hence in
particular every old depth between \(-H\) and \(H\).  Formula (5.2) is
(3.5) with \(a+b=2H+c_-+c_+\).  Finally,

\[
 p(c_-+c_+)
 \le\frac{W}{2\ell}(c_-+c_+)
 =o(W),
\]

which proves the asymptotic statement. \(\square\)

This is a genuine pervasive recoding rather than a semantic packet merge.
For the lower cores, away from the chosen linear cut one has the exact
identity

\[
 \boxed{
 A_i^{(H)}
 =\bigcup_{j=i-c_-}^{i}A_j^{(H+c_-)}.}
\tag{5.4}
\]

Indeed the first new interval begins at \(i+H\), the last ends at
\(i+\ell-1\), and consecutive intervals overlap or are adjacent.  At the
cut, the extra
future singleton blocks in the reverse-written useful prefix give the same
old lower flags as literal suffix ORs.  Thus all old lower-core witnesses
are maintained while essentially every principal endpoint is physically
changed.

The newly exposed rows with \(H<q\le a\) or \(H<q\le b\) are only
**candidate occurrences**.  The old matching theorem gives neither
target-disjointness nor small aggregate leave in those new rows.  This is
the exact support gap left by Theorem 5.1.

---

## 6. Why exact canonical-root bridges do not suffice

The positive theorem works because it abandons the prescribed residual
block at every later root.  If exact canonical roots are retained, every
bridge is physically OR-sealing.

For ordered partitions \(\Sigma\) and
\(\Pi=(B_1,\ldots,B_h)\), put

\[
 U_0=\varnothing,
 \qquad
 U_j=B_1\cup\cdots\cup B_j
\]

and let \(D_X(\Sigma)\) denote the ordered partition obtained by deleting
\(X\) from every source block.  Define

\[
 j_*(\Sigma,\Pi)
 =\min\{0\le j\le h:
 D_{U_j}(\Sigma)=(B_{j+1},\ldots,B_h)\}.
\tag{6.1}
\]

The exact nonempty MTF distance is

\[
 d^+_{\rm MTF}(\Sigma,\Pi)=\max\{1,j_*(\Sigma,\Pi)\}.
\tag{6.2}
\]

Indeed, after any update word the coordinates receiving new last-occurrence
times form a target prefix, while the untouched source is precisely the
deleted source tail.  Conversely, writing
\(U_j,U_{j-1},\ldots,U_1\) realizes the target state when \(j\ge1\).
When \(j=0\), source and target coincide and the nonempty idempotent update
\(B_1\) realizes the stated distance one.

### Theorem 6.1 — exact-root bridge classification and sealing

Let \(\Sigma\) be the terminal exact canonical state of a verified
radius-\(H\) strip, and let \(\Pi'\) be a fresh exact canonical root of
another strip.  Write

\[
 h=2H+2.
\]

Let \(L\) be the first block of \(\Sigma\) and \(R'\) the final residual
block of \(\Pi'\).  Then

\[
 |L|=|R'|=m-H
\]

and

\[
 \boxed{
 d^+_{\rm MTF}(\Sigma,\Pi')
 =
 \begin{cases}
 h-1,&R'=L,\\
 h,&R'\ne L.
 \end{cases}}
\tag{6.3}
\]

Moreover, for every exact bridge word,

\[
 \boxed{
 L\ \cup\!\bigcup_{X\text{ in the bridge}}X=[2m].}
\tag{6.4}
\]

Consequently every interval beginning in the old principal payload and
ending in the new principal payload has OR \([2m]\); no proper target can
use such a seam.

#### Proof

At the end of a complete canonical strip traversal, the only source block
of size at least \(m-H\) is its first block \(L\).  All intermediate
blocks are singletons, and the remaining nonsingleton residual is the fixed
opposite core \(D\).  More explicitly, the fresh residual is

\[
 R_0=D\mathbin{\dot\cup}I(\ell,\ell-H).
\]

The first \(\ell-H\) principal updates delete exactly this active cyclic
interval from \(R_0\), leaving \(D\); subsequent deletions affect only
active singleton blocks, and every lower core is disjoint from \(D\).
Thus the terminal state has first block \(L\), residual block \(D\), and
otherwise only singleton blocks.  In particular, the residual has size

\[
 m-\ell<m-H.
\]

If \(j_*<h\), the target's final block \(R'\), of size \(m-H\), must be a
restriction of the unique sufficiently large source block \(L\).  It must
therefore equal \(L\).  But \(L\) is first in the source order and \(R'\)
is last in the target suffix.  Hence that suffix has only one block, so
\(j_*=h-1\).  Conversely, if \(R'=L\), deleting
\(U_{h-1}=[2m]\setminus L\) leaves exactly \((L)\), proving
\(j_*=h-1\).  If \(R'\ne L\), only \(j_*=h\) remains.  This proves
(6.3).

For an arbitrary exact bridge, let \(j\) be the number of target-prefix
blocks generated by its new last-occurrence times.  Its mask union is
\(U_j\), and it necessarily satisfies

\[
 D_{U_j}(\Sigma)=(B_{j+1},\ldots,B_h).
\]

The same size-and-order argument therefore gives \(j\in\{h-1,h\}\), with
\(j=h-1\) possible only when \(R'=L\).  Hence the bridge-mask union is
either \([2m]\setminus L\) or \([2m]\).  The last literal of the old
canonical traversal is exactly \(L\), proving (6.4).
Every old-to-new interval contains that terminal letter and every bridge
letter, so it has full OR. \(\square\)

Theorem 6.1 does not contradict Theorem 3.1.  Useful-prefix seams do not
end in the prescribed exact residual block \(R'\); they retain an arbitrary
old tail and synchronize only those leading blocks which expose the desired
flags.

---

## 7. Fixed-rank endpoint floor and retained-letter obstruction

The next theorem applies to every Boolean word, with no packet, state, or
seam hypothesis.

### Theorem 7.1 — fixed-rank endpoint floor

If a Boolean OR word

\[
 X_1,X_2,\ldots,X_n
\]

covers every target of rank \(r\), where \(1\le r\le k\), then

\[
 \boxed{
 \#\{j:|X_j|\le r\}\ge\binom{k}{r}.}
\tag{7.1}
\]

#### Proof

Choose one witnessing interval for every rank-\(r\) target and record its
right endpoint.  Two distinct targets cannot have the same right endpoint:
the ORs of suffix intervals ending at one position are nested, hence
comparable, while two comparable sets of the same cardinality are equal.
Thus the selected right endpoints are pairwise distinct.

The terminal letter of a witnessing interval is contained in the interval
OR.  Therefore every selected endpoint letter has size at most \(r\).
There are \(\binom{k}{r}\) targets, proving (7.1). \(\square\)

For all sufficiently large \(m\), the imported condition
\(H=o(\sqrt m)\) gives \(H\le m-2\).  Return to the verified strips and put

\[
 0\le H\le m-2,
 \qquad
 r=m-H-1,
 \qquad
 N_{H+1}=\binom{2m}{m-H-1}.
\tag{7.2}
\]

The old principal word has

\[
 P=2\ell p=W-u_0
\tag{7.3}
\]

principal occurrences, and every one of their letters has size \(m-H>r\).

### Corollary 7.2 — exact retained-slot recoding ledger

Suppose a final word has length

\[
 n=W+e
\]

and retains all but \(a_{\rm rec}\) of the \(P\) old principal occurrences
with their old letters.  If it covers rank \(m-H-1\), then

\[
 \boxed{
 a_{\rm rec}+e+u_0\ge N_{H+1}.}
\tag{7.4}
\]

#### Proof

Here retaining an occurrence means retaining that unchanged physical
letter; its location and the surrounding order may be arbitrary.
The \(P-a_{\rm rec}\) retained letters all have size greater than \(r\).
Hence at most

\[
 n-(P-a_{\rm rec})
 =a_{\rm rec}+e+u_0
\]

positions are eligible for the endpoint floor (7.1). \(\square\)

The exact central-binomial ratio is

\[
 \frac{N_{H+1}}W
 =\prod_{i=1}^{H+1}\frac{m-i+1}{m+i}.
\tag{7.5}
\]

Since

\[
 1-\prod_i(1-x_i)\le\sum_i x_i,
\]

one has

\[
 \boxed{
 1-\frac{N_{H+1}}W
 \le\frac{(H+1)^2}{m}.}
\tag{7.6}
\]

Thus the verified regime \(H=o(\sqrt m)\) gives

\[
 N_{H+1}=(1-o(1))W.
\]

If \(e=o(W)\) and \(u_0=o(W)\), Corollary 7.2 forces

\[
 \boxed{
 a_{\rm rec}=(1-o(1))W.}
\tag{7.7}
\]

This permits arbitrary strip ordering, arbitrary ownership reassignment,
one global chronology, inherited residual tails, and unrestricted
cross-seam witnesses.  The obstruction is physical: almost every old
principal letter must change.

The asymmetric construction in Section 5 meets this necessary condition
when \(c_->0\): it changes every principal core.  What it does not supply is
near-surjective support in the newly exposed row.

---

## 8. Pervasive interval-recoding necessity

The retained-letter statement can be strengthened to arbitrary interval
recoding.  The underlying counting lemma is included for completeness.

Let \(B_1,\ldots,B_P\) be the \(P=W-u_0\) distinct old lower-strip targets
of rank \(m-H\).  They are distinct because the imported strip matching is
target-disjoint in this row.  In a final word of length \(n\), choose an
arbitrary witness interval \(I_i\) for each \(B_i\).  Put

\[
 E=n-P,
\tag{8.1}
\]

let

\[
 R=\#\{j:j\notin I_i\text{ for every }i\},
\tag{8.2}
\]

and define the total interval-incidence overlap

\[
 O=\sum_{i=1}^{P}|I_i|-\left|\bigcup_{i=1}^{P}I_i\right|.
\tag{8.3}
\]

### Theorem 8.1 — strip-core overlap trilemma

If the final word also covers every target of rank \(m-H-1\), then

\[
 \boxed{
 2E+O\ge N_{H+1}+R.}
\tag{8.4}
\]

This holds for every choice of one witness interval for each \(B_i\).

#### Proof

By Theorem 7.1, at least \(N_{H+1}\) physical letters have size at most
\(m-H-1\).  Hence at most \(n-N_{H+1}\) physical letters have size at
least \(m-H\).

If a witness \(I_i\) is a singleton, its physical letter equals the
rank-\((m-H)\) target \(B_i\).  Since the \(B_i\) are distinct, at most
\(n-N_{H+1}\) of their witnesses are singletons.  Therefore at least

\[
 P-n+N_{H+1}=N_{H+1}-E
\]

of the intervals have length at least two.  It follows that

\[
 \sum_i(|I_i|-1)\ge N_{H+1}-E.
\tag{8.5}
\]

On the other hand,

\[
 \begin{aligned}
 \sum_i(|I_i|-1)
 &=\left|\bigcup_iI_i\right|+O-P\\
 &=(n-R)+O-P\\
 &=E+O-R.
 \end{aligned}
\tag{8.6}
\]

Combining (8.5)--(8.6) proves (8.4). \(\square\)

If \(n=W+e\), then

\[
 E=e+u_0.
\]

At \(H=o(\sqrt m)\), every \(W+o(W)\) full-cube word consequently obeys

\[
 \boxed{
 O\ge(1-o(1))W.}
\tag{8.7}
\]

Thus even wholesale replacement of the old principal letters is not
enough if their new witnesses remain essentially disjoint.  Linear total
interval overlap is necessary.  Identity (5.4) shows how asymmetric
useful-prefix recoding can create precisely this kind of pervasive overlap
without appending a new letter for every old core.

---

## 9. Precise proved and conditional boundary

### Proved unconditionally from the verified matching

1. The target-disjoint radius-\(H\) strip family has one fully initialized
   literal MTF chronology covering its entire verified band, with exact
   length (3.5) and seam loss \(2Hp+1=o(W)\).
2. The same family admits genuine macro-packets owning at least \(k\)
   middle targets each, with both exact aggregate packet surpluses \(o(W)\).
3. Full exact-root bridges are OR-sealing; useful-prefix tail inheritance is
   a genuine physical change, not a semantic regrouping of sealed epochs.
4. The entire old band survives asymmetric depth recoding with
   \(c_-+c_+=o(\ell)\), still at length \(W+o(W)\).
5. Covering even the next lower rank at coefficient one requires recoding
   \(W-o(W)\) old principal endpoints and linear total overlap among the
   witnesses of the old lower cores.

### Conditional extension theorem

Corollary 3.2 is the exact compositional statement.  Any family of
asymmetric strip pieces and an integral target ownership rule which covers a
desired target family containing the whole middle layer and satisfies

\[
 \sum_\alpha(s_\alpha-M_\alpha)=o(W),
 \qquad
 U-u_0=o(W),
 \qquad
 \sum_\alpha(a_\alpha+b_\alpha)=o(W)
\]

has one literal global chronology of length \(W+o(W)\) for that target
family.  If the desired family were the whole nonempty Boolean lattice,
this would give the coefficient-one theorem.  No such full-lattice support
and ownership system is proved here.

### Still open

The verified matching controls distinct targets only through depths
\(|q|\le H\).  The asymmetric chronology exposes further occurrences, but
their collisions and leave are uncontrolled.  The next mathematical gate is
therefore not chronology, root cost, or packet mass.  It is:

> **Deep support allocation — UNPROVED.**  Construct a multiscale family of
> asymmetric useful-prefix strips, with one integral ownership assignment,
> whose exposed target support covers the required deeper ranks with total
> leave \(o(W)\), while the three exact surplus terms in (3.4) remain
> \(o(W)\).

The endpoint-floor and overlap theorems show what any solution must do: it
must physically recode a leading fraction of the old endpoints and reuse
their witness intervals at linear total multiplicity.  The asymmetric
useful-prefix theorem proves that this amount of recoding and overlap is
compatible with an \(o(W)\) chronology ledger.  Distinct deep support is the
remaining boundary.
