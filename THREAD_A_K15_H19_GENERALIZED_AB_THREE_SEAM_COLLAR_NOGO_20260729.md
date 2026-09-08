# Thread A: exact generalized-`A/B` three-seam collar obstruction at H19

Date: 2026-07-29

Status: two complete solver-free finite results.  First, the full
authenticated native FF/RF/FR-plus-ordinary-RR catalogue contains no exact
generalized-q1 braid.  On the forced q1 defect support, a separate 32-row
argument also closes the same-order double-reversal mode and hence every
intact-four-component reassembly.  Second, after imposing depth-three block
length and endpoint separation, no such native move composes with either
audited `7267` tail under fixed-`A(M0)` core transport.  No length-6457 word
is produced.  This is not a no-go for short or endpoint-overlapping compiler
collars, an internal-vertex-changing multi-parent exchange, an arbitrary
same-order double reversal at unrelated cuts in the compiler-only problem, a
two-collar composition, or arbitrary generalized 429-run `A/B` rewiring.

## 1. Frozen state and the two questions

The authoritative H19 carrier is

```text
scratch/k15_h20_h19_root8216_chain/final/candidate_0000.json
SHA-256 86dcb9f16739b0a75eca8cde6bc9c824876453ab3b8fc70f01144da517dd4c0b
```

Its middle row is a Hamilton path

\[
 T=(T_0,\ldots,T_{6434})
\tag{1.1}
\]

through all rank-eight subsets of `[15]`.  The exact common-word baseline is
the entrywise-maximal reconstruction \(A^0=A(M_0)\) frozen in

```text
scratch/thread_a_k15_h19_m0_a0_baseline_20260729.json
SHA-256 12a59780e8920469b385250bdb95ec9265259b2f0c9dac05c51f9262587ec09f
```

It has \(D^3A^0=T\), covers a set \(\mathcal C_0\) of 16,362 lower targets,
and has the 21-mask residual

\[
\begin{split}
\{&685,960,1103,2420,2575,2676,4469,5801,7267,7504,8250,9524,\\
  &12825,13616,13620,17683,17738,19098,19568,21641,29776\}.
\end{split}
\tag{1.2}
\]

There are two nested finite questions.

1. Can one intact-component three-cut braid turn the present H19 path into
   the exact open generalized-Pascal `A/B` braid at coordinate \(z=14\)?
2. Even without demanding that exact one-hole lower rainbow, can any
   endpoint-separated fixed-\(A^0\)-core segment braid create durable
   nonterminal services for every lost target, in particular `7682` and
   `7683`, and then compose with an audited endpoint tail creating `7267`?

Both answers are no in the declared class.  The first has a 32-row endpoint
certificate; the second has an exhaustive unary-\(Q\) Hall certificate.

## 2. The correct open generalized-braid counts

Distinguish \(z=14\), and call a middle owner `A` if it contains \(z\), `B`
otherwise.  There are

\[
 |A|=\binom{14}{7}=3432,
 \qquad |B|=\binom{14}{8}=3003.
\tag{2.1}
\]

### Lemma 2.1 (open-sector counting law)

If a Hamilton path has \(r_A\) maximal `A` runs and begins and ends in `B`,
then its channel counts are

\[
 AA=3432-r_A,\qquad AB=BA=r_A,\qquad BB=3002-r_A.
\tag{2.2}
\]

If, moreover, the `AA` intersections enumerate all
\(\binom{14}{6}=3003\) lower colours containing \(z\), while the non-`AA`
intersections are distinct (the open generalized-Pascal lower-channel
condition), then \(r_A=429\), and hence

\[
 (AA,AB,BA,BB)=(3003,429,429,2573).
\tag{2.3}
\]

#### Proof

Each `A` run with \(s\) vertices contributes \(s-1\) `AA` edges and one
entry and exit, giving the first three equations.  Since both endpoints lie
in `B`, the number of `B` runs is \(r_A+1\), which gives `BB`.

An `AA` intersection contains \(z\); after deleting \(z\), it is a rank-six
subset of `[14]`.  Completeness of this channel therefore gives

\[
 AA=\binom{14}{6}=3003.
\]

Equation (2.2) now gives \(r_A=429\).  The non-`AA` intersections are
rank-seven subsets of `[14]`; their number is consequently

\[
 AB+BA+BB=3431.
\]

Their assumed distinctness leaves the single unavoidable open-path hole in
the no-\(z\) channel, and (2.3) follows.
\(\square\)

For the frozen path

\[
 T_0=9901\in B,\qquad T_{6434}=7779\in B,
\]

and the actual channel vector is

\[
 (AA,AB,BA,BB)=(3004,428,428,2574).
\tag{2.4}
\]

Thus an exact generalized-braid repair has channel current

\[
 (\Delta AA,\Delta AB,\Delta BA,\Delta BB)=(-1,+1,+1,-1).
\tag{2.5}
\]

This is the open-path correction to the cyclic count.  Imposing cyclic
`BB=2574` on the 6,434-edge path is an off-by-one error.

Plain distinctness of all 6,434 lower colours, without the channel-
completeness condition, also permits \(r_A=430\), with the unique missing
colour in the \(z\)-containing channel.  From (2.4) that alternative would
have current \((-2,+2,+2,-2)\), or `cross` current `+4`, and hence cannot be
produced by only three new seams.  It is not the generalized-Pascal channel
target studied below.

## 3. The complete lower-defect support

The present lower holes are

\[
 H=\{5801,7267,8877,13620\};
\tag{3.1}
\]

all avoid \(z\).  The exact lower multiplicities are:

* among the 3,004 `AA` edges, after deleting \(z\), the histogram is
  \(1^{3002}2^1\); the repeated label is `756`, on edge starts
  `2582,5917`;
* among the 2,574 `BB` edges, the histogram is \(1^{2572}2^1\); the repeated
  label is `12685`, on edge starts `840,5046`;
* among all non-`AA` edges the only two repeated labels are `12685` and
  `3868`; the latter occurs on the `BB` edge start `2553` and the cross edge
  start `5549`.

The two repeated `AA` edges are explicitly

```text
2582: 17142--21236, reduced lower 756, reduced upper 4854
5917: 17148--17396, reduced lower 756, reduced upper 1020.
```

The `BB` skeleton itself has the exact audited signature

\[
\begin{array}{c|c}
\text{edges}&2574\\
\text{distinct rank-nine upper colours}&2002/2002\\
\text{B-vertex degree histogram}&2^{2152}1^{844}0^7\\
\text{cross slots }\sum_{X\in B}(2-d_{BB}(X))&858\\
\text{lower-label histogram}&1^{2572}2^1.
\end{array}
\tag{3.2}
\]

### Lemma 3.1 (forced old-cut support)

Any three-old-edge/three-new-edge exchange satisfying (2.5) and reducing
the number of lower holes from four to one must delete:

1. one of the two `AA` occurrences of reduced label `756`;
2. one of the two `BB` occurrences of label `12685`; and
3. one occurrence of the `BB`--cross overlap label `3868`.

The third edge may be its `BB` occurrence or its cross occurrence.  The three
new lower labels must be three distinct members of \(H\).

#### Proof

The lower support must increase by three, the maximum possible after adding
three edges.  Therefore every deleted colour must retain an old occurrence,
and every added colour must be a distinct old hole.  The displayed
multiplicity tables list all and only old edges whose deletion retains their
colour.

Write \((a,b,x)\) for the old `AA`, `BB`, cross channel counts among the
three cuts.  Equation (2.5) permits only the relevant cases

\[
 (a,b,x)=(1,1,1)\quad\text{or}\quad(1,2,0).
\]

In the first case the cross edge must be the cross occurrence of `3868` and
the `BB` edge must be a `12685` occurrence.  In the second, the two `BB`
edges must be one `12685` occurrence and the `BB` occurrence of `3868`.
Deleting both `12685` occurrences or both `3868` occurrences would lose
that colour.  No case with two `AA` deletions is possible because deleting
both occurrences of `756` loses its colour.  This proves the claim.
\(\square\)

The forced cut triples, written as cut positions rather than edge starts,
are therefore exactly

\[
\begin{gathered}
(841,2554,2583),\ (841,2554,5918),\
(841,2583,5550),\ (841,5550,5918),\\
(2554,2583,5047),\ (2554,5047,5918),\
(2583,5047,5550),\ (5047,5550,5918).
\end{gathered}
\tag{3.3}
\]

## 4. The 32-row Johnson obstruction

Delete three path edges.  This leaves four intact path components
\(A|B|C|D\), with the global first and last endpoints fixed.  There are
eight ways to order and orient the two internal components.  Four change at
most two of the deleted edges and therefore cannot raise lower support by
three.  The four modes that genuinely replace all three seams are

\[
 C B,\quad C^R B,\quad C B^R,\quad B^R C^R.
\tag{4.1}
\]

### Theorem 4.1 (no intact-component exact-defect braid)

For each of the eight forced cut triples in (3.3), every one of the four
reassemblies in (4.1) has a non-Johnson new seam.  In fact the recorded
Hamming distances are all at least six.  Hence no three-seam reassembly of
the four intact old components reaches the exact generalized `A/B` lower
rainbow.

#### Proof

For a proposed seam \(X--Y\) between rank-eight owners, Johnson adjacency is
equivalent to

\[
 |X\mathbin\triangle Y|=2.
\tag{4.2}
\]

The eight cut triples and four component modes give 32 constant-size tests.
The complete table of the three endpoint masks, channel types, lower labels,
and Hamming distances is stored in

```text
scratch/thread_a_k15_h19_generalized_ab_segment_nogo_20260729.json
```

and rebuilt without search by

```text
scratch/verify_thread_a_k15_h19_generalized_ab_segment_nogo_20260729.py.
```

Every row has at least one distance different from two; indeed every listed
distance is in \(\{6,8,10,12\}\).  Thus all 32 modes fail (4.2).  The four
remaining component modes change at most two seam colours, so their support
gain is at most two.  The eight modes exhaust intact-component path
reassemblies. \(\square\)

## 5. Full physical segment-catalogue audit

The native enumerator

```text
scratch/search_k15_segment_braid_native.cpp
SHA-256 889379685f55e1938f24fceffd889951332966fe547021874b5482b1c2fa7d29
```

enumerates every FF/RF/FR contiguous two-block exchange and every ordinary
full-segment reversal whose new seams are Johnson edges, then retains exactly
the depth-three-resident, all-upper-safe rows.  It imposes no common-colour
condition and no `AA/AB/BA/BB` restriction: cross-sector repair edges are
fully allowed.  The authenticated H100 output is

```text
scratch/thread_a_k15_h19_native_physical_moves_20260729.txt
SHA-256 a78bc8b01db947a8a6ee0c02e892893eabf58d422bdc4f8181709fffe59f6e39
```

with 9,164 rows and generation summary

```text
johnson=548377 resident=11957 upper_safe=9164 target=9164.
```

The catalogue is regenerated on H100 CPU by compiling the displayed source
with C++20 and running

```text
search_k15_segment_braid_native candidate_0000.json > physical_moves.txt
```

with no target or Hall-score filter.  Comparing `physical_moves.txt` to the
authenticated SHA above closes the finite-enumeration interface.

An independent seam-delta reconstruction gives

\[
\begin{array}{c|rrrr}
\text{lower holes}&4&5&6&7\\ \hline
\text{rows}&7303&339&1361&161.
\end{array}
\tag{5.1}
\]

Thus the minimum remains four.  Exactly 51 rows have the required undirected
channel current \((\Delta AA,\Delta\mathrm{cross},\Delta BB)=(-1,2,-1)\),
24 of them genuine length-at-least-three FF/RF/FR collars, but none has one
lower hole.  Moreover no authenticated row makes the `BB` lower labels
injective while retaining all 2,002 `BB` upper colours:

```text
BB_exact_hard_upper_rows = [].
```

This includes the standard two-opt attempt at the one duplicated `BB`
label.  It explains the sharp boundary: the `BB` skeleton is one duplicate
from exact, but no intact-segment reassembly realizes that correction under
the resident/all-upper physical tests.

The audit artifact has SHA-256

```text
15abb45032f0766d96a1d549d88dd3d49de68caa2e17cc6a1b898ecf7193218f.
```

The independent verifier source has SHA-256

```text
486d82b072b118bec9c6fc2dbfd8aab61813fdbcbb8c27914fd95741d37861f4.
```

## 6. Endpoint-conditioned adaptive service theorem

The exact generalized lower rainbow is stronger than needed for a literal
length-6457 word.  We therefore also test every move in the authenticated
native class against the common compiler without a lower-hole postfilter.

For a move \(m\), let \(G_-\) and \(G_+\) be its old and new depth-three
source gaps.  They have at most nine positions for a genuine three-seam
move and at most six for a reversal.  Let \(\mathcal E_+\) be the short
cells meeting \(G_+\), and define \(\mathcal E_-\) analogously from
\(G_-\); thus \(|\mathcal E_\pm|\le36\).

The two audited endpoint tails are

\[
\begin{aligned}
E^s_{6432,\ldots,6437}&=(17937,1585,1571,1603,3651,7267),\\
E^p_{6432,\ldots,6437}&=(17937,1585,1571,1603,3139,7267).
\end{aligned}
\tag{6.1}
\]

Each has exact trace coverage

\[
 (\mathcal C_0\setminus\{7682,7683\})\cup\{7267\}.
\tag{6.2}
\]

For branch \(\eta\in\{s,p\}\), define the exact endpoint-conditioned service
bank

\[
 \mathcal R_\eta(m)=
 \{S\in\mathcal C_0:
   \text{no occurrence of (S) in (E^\eta) avoids }\mathcal E_-\}.
\tag{6.3}
\]

This definition is essential.  Besides deleting all occurrences of `7682`
and `7683`, the tail deletes one terminal occurrence each of `3587` and
`7747`; their other occurrences can be hit by an internal collar.

For \(S\in\mathcal R_\eta(m)\) and \(c\in\mathcal E_+\), put an edge
\(S\sim c\) if the unique entrywise-maximal fixed-core word satisfying only
the exceptional pin \((S,c)\) is nonempty, has cell trace exactly \(S\), and
still has third derivative equal to the child middle path.

### Theorem 6.1 (unary-service Hall is necessary)

If a fixed-\(A^0\)-core collar and endpoint branch \(\eta\) preserve every
target of \(\mathcal C_0\) and create `7267`, then the unary service graph
between \(\mathcal R_\eta(m)\) and \(\mathcal E_+\) has a matching saturating
\(\mathcal R_\eta(m)\).

#### Proof

Every target in \(\mathcal R_\eta(m)\) has no safe transported occurrence,
so it must use an exceptional cell.  Distinct target values require distinct
cells.  Fix one target-cell pair used by a joint feasible word.  Delete all
other exceptional pins and maximize each gap letter inside its child erosion
envelope and the negative constraint imposed by this one pin.  The joint word
is coordinatewise below the result.  Consequently nonemptiness persists;
the selected OR still contains the old exact target and cannot exceed it;
and every four-letter OR still contains the old exact middle owner and cannot
exceed its erosion envelope.  Thus the pair is a unary edge.  The joint
assignment therefore induces the required matching. \(\square\)

This theorem is only necessary: a unary matching may still fail the joint
maximal-\(Q\) table.  In the present state no unary survivor exists, so no SAT
or joint-\(Q\) phase is needed.

## 7. Exhaustive bounded-collar certificate

After excluding short blocks and collars meeting the endpoint support, 1,948
physical moves remain.  Of these, 714 fail the entrywise-maximal fixed-core
middle equations before endpoint branching.  The remaining 1,234 moves give
2,468 endpoint branches.  On each branch the necessary service test fails:

\[
\begin{array}{c|rrr}
\text{branch}&|\mathcal R_\eta|>|\mathcal E_+|&
\text{zero-degree service}&\text{proper Hall shore}\\ \hline
s&78&1153&3\\
p&78&1153&3.
\end{array}
\tag{7.1}
\]

The three Hall failures have gaps \(2,2,3\) in each branch.  Hence the number
of survivors is exactly zero.

The 8.7 MiB reusable certificate records, for every scoped move/branch,
either a maximal-core defect, an explicit capacity cut, a zero-degree target
with all unary obstructions, or a Hall-deficient \(U,N(U)\):

```text
scratch/thread_a_k15_h19_segment_collar_nogo_certificate_20260729.json
SHA-256 b496d40e95102db6fd198d7e248c2b8f546ee3f9f1ce7bb19c9a33309bfc2901
```

Its deterministic H100-CPU builder is

```text
scratch/thread_a_search_k15_h19_adaptive_compound_collar_20260729.py
SHA-256 c24abef48efd2330c1b7bdcffe007f855c5cd5a7f0c0c7769fea240b111e4aa5
```

and the hash-bound rebuild verifier is

```text
scratch/verify_thread_a_k15_h19_segment_collar_nogo_certificate_20260729.py.
```

Its source SHA-256 is

```text
b7a49ccea61ff59bd903676c3c743d883f302b985f42c9662fca38b50e42b4bc.
```

The certificate has 3,182 decision rows, canonical decision SHA

```text
c3c893556b2268fec44291669a434310756f5aab8c904626115e7c7286901730,
```

and no survivors.  The run is solver-free and used H100 CPU only.

## 8. Why a hit would have given 6,457

If one scoped collar had survived the joint maximal-\(Q\) audit, its internal
nonterminal copies of `7682,7683` would survive either tail in (6.1), while
the tail would add `7267`.  The resulting 6,438-letter prefix would cover
\(\mathcal C_0\cup\{7267\}\), leaving 20 masks.  Append the 17 masks

```text
685 960 1103 2420 2575 2676 4469 5801 7504 8250 12825
17683 17738 19098 19568 21641 29776
```

and then `9524,13616`.  Since

\[
 9524\mathbin\lor13616=13620,
\tag{8.1}
\]

these 19 letters cover the whole residual, giving a fully literal word of
length \(6438+19=6457\).  The zero-survivor theorem proves only that this
construction cannot arise from the declared single-collar class.

## 9. Exact remaining move family

The k=13 generalized braid lesson is retained: `AA` upper colours need not be
rainbow, because `AB/BA` seams may repair them.  Nothing in either finite
audit imposed that false common-colour condition.

The new obstruction is geometric.  The complete defect ledger forces the
old cuts to (3.3), but all intact-component endpoint pairings fail Johnson
adjacency.  Therefore a successful exact-q1 repair must change an internal
owner adjacency or owner placement, not merely reorder/reverse old path
components.  The smallest surviving architectures are:

1. a compound two-stage trade that first removes the `BB` duplicate while
   preserving its 2,002-colour upper deck, then performs the `AA`-to-cross
   current; or
2. one internal-vertex-changing alternating circuit whose boundary deletes
   one `756`, one `12685`, and one occurrence of `3868`, and whose three new
   lower labels are three members of \(H\).

Either architecture must be re-audited for exact middle ownership,
depth-three residence, all upper layers, the common fixed-core transport (or
a newly proved replacement for it), and the endpoint-conditioned service
bank.  Failure of the present certificate cannot be promoted beyond the
native FF/RF/FR-plus-ordinary-RR class.
