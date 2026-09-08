# Coordinate deletion cap and the exact meaning of the current \(K=17\) surplus

## 1. Coordinate-deletion lemma

Let \(A=(A_1,\ldots,A_L)\) be a universal OR word on \([k]\), and fix a
coordinate \(z\in[k]\). Delete every entry containing \(z\), preserving
the order of all remaining entries, and call the resulting word \(A^{-z}\).

**Lemma.** \(A^{-z}\) is universal on \([k]\setminus\{z\}\).

**Proof.** Let \(\varnothing\ne S\subseteq[k]\setminus\{z\}\). Some
contiguous interval of \(A\) has union \(S\). No entry of that interval
can contain \(z\). Hence the whole witnessing interval lies in one
maximal run of \(z\)-free entries, and remains a contiguous interval after
all \(z\)-containing entries are deleted. Thus it is still a witness for
\(S\) in \(A^{-z}\). \(\square\)

Consequently, for every coordinate \(z\),

\[
 \#\{i:z\notin A_i\}\ge \nu(k-1),
 \qquad
 \boxed{\#\{i:z\in A_i\}\le L-\nu(k-1).}
 \tag{1.1}
\]

Summing (1.1) over all coordinates gives the global cell-mass bound

\[
 \boxed{\sum_{i=1}^L |A_i|\le k\bigl(L-\nu(k-1)\bigr).}
 \tag{1.2}
\]

This is an exact necessary condition for every word; it does not assume
the flat-carrier, PBBS, Pascal-braid, or staircase normal forms.

### Full deletion hierarchy

The same proof works for a set \(Q\subseteq[k]\): delete every entry
meeting \(Q\). The remaining word is universal on \([k]\setminus Q\), so

\[
 \#\{i:A_i\cap Q=\varnothing\}\ge \nu(k-|Q|).
 \tag{1.3}
\]

Averaging (1.3) over all \(t\)-subsets \(Q\) and double-counting gives

\[
 \boxed{
 \sum_{i=1}^L\binom{k-|A_i|}{t}
 \ge \binom{k}{t}\nu(k-t)
 }
 \qquad(1\le t<k).
 \tag{1.4}
\]

Thus coordinate deletion supplies an exact hierarchy of binomial moments
of the cell-rank distribution. It is necessary but not, by itself,
rigid enough to force the \(K=17\) chronology: the real-valued rank-count
relaxation at length \(24313\) remains feasible with large marginal
ranges. The useful new information is the coordinatewise cap and the
recursive interpretation when one cap is saturated.

## 2. Equality normal form relative to one coordinate

Assume inductively that \(\nu(k-1)=B(k-1)\), and suppose that an equality
word of length \(B(k)\) exists. Then every coordinate has occurrence cap

\[
 c_k:=B(k)-B(k-1).
 \tag{2.1}
\]

If some coordinate \(z\) occurs exactly \(c_k\) times, deleting its
occurrences leaves an optimal \(B(k-1)\)-word. Thus an equality witness
with a saturated coordinate is exactly an optimal parent chronology plus
\(c_k\) marked cells interleaved among it. The hard part of an exact
Pascal induction is therefore not the scalar count: it is choosing those
marked cells and their interleaving so that both the marked and unmarked
witness systems survive simultaneously.

This also explains why a separated double-copy lift is wasteful. It
uses a complete parent-sized marked copy, whereas equality permits only
\(c_k\) marked cells.

## 3. \(K=17\)

Here

\[
 B(16)=12873,
 \qquad
 B(17)=24313,
 \qquad
 c_{17}=B(17)-B(16)=11440=\binom{16}{9}.
 \tag{3.1}
\]

Therefore every length-\(24313\) equality word would satisfy

\[
 \#\{i:z\in A_i\}\le11440
 \quad\text{for every }z.
 \tag{3.2}
\]

The retained length-\(25746\) word is the canonical lift

\[
 X,\ \{z\},\ (X_1\cup\{z\}),\ldots,(X_{12872}\cup\{z\}),
\]

where \(X\) is the verified length-\(12873\) optimum for \(K=16\). It has
exactly \(12873\) \(z\)-free cells and \(12873\) \(z\)-containing cells.
Its excess over \(B(17)\) is therefore

\[
 12873-11440=1433,
\]

exactly the overpopulation of the marked Pascal sector. The current gap
is not hidden in the parent: its \(z\)-free subsequence is already an
optimal \(K=16\) word. Exact equality requires the marked copy to be
replaced by \(11440\) cells which share witnesses with the parent through
a genuine braid.

## 4. Why literal duplicate deletion is not the braid

The first-rank-\(9\) deadline walk in the unmarked parent sector contains
\(12869\) occurrences and covers all \(11440\) rank-\(9\) subsets of
\([16]\). It is a Johnson walk: consecutive unequal states have symmetric
difference two. Collapsing its 329 consecutive holds leaves a
length-\(12540\) Johnson walk, still with \(1100\) nonconsecutive repeat
visits. Keeping only the first visit to each target creates 738
non-Johnson transitions.

Thus the scalar surplus is completely identified, but simply deleting
duplicate carrier visits does not preserve the chronology. The missing
object is precisely a shadow-preserving rethreading/braid which removes
the repeat visits while retaining the lower compiler and all upper
witnesses.

The replay is
scratch/audit_coordinate_deletion_and_k17_middle_surplus_20260731.py.

## 5. Scope

The coordinate-deletion lemma and bounds (1.1)--(1.2) are proved for all
\(k\). The numerical \(K=17\) statements are literal audits of the
retained certified upper word. No compression to length \(24313\) is
claimed here, and this note does not prove \(\nu(17)=B(17)\).
