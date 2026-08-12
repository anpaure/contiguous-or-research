# Independent audit: the fixed-(K=16)-subsequence marked sector

Date: 2026-07-31  
Status: **GO**, with a one-unit strengthening of the final orientation bound  
Scope: one authenticated source word only; no unrestricted (K=17) no-go

## 1. Exact model under audit

Let

~~~
X = answers/k16.word
~~~

have length \(n=12{,}873\) and SHA-256

~~~
890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe.
~~~

The model keeps all cells of \(X\), with the same values and in the same
order, as the complete subsequence avoiding a new coordinate \(z\).  It adds
exactly \(11{,}440\) cells, each containing \(z\).  The total length is thus

\[
                   12{,}873+11{,}440=24{,}313.
\]

Changing, deleting, reordering, or \(z\)-marking a source cell is outside the
model.

## 2. Complete insertion-gap criterion

For a nonzero old target \(T\subseteq[16]\), let

\[
 e(T)=\min\{j:\operatorname{OR}(X_i,\ldots,X_j)=T\text{ for some }i\},
\]

and

\[
 \ell(T)=\max\{i:\operatorname{OR}(X_i,\ldots,X_j)=T\text{ for some }j\}.
\]

Number the internal gap between \(X_{g-1}\) and \(X_g\) by
\(1\le g\le n-1\).

### Lemma 2.1

Every \(T\)-witness crosses gap \(g\) if and only if

\[
                         \ell(T)<g\le e(T).                 \tag{2.1}
\]

Indeed, a witness avoids \(g\) exactly when it ends before \(g\), or starts
at or after \(g\).  Such a left witness exists iff \(e(T)<g\), and such a
right witness exists iff \(\ell(T)\ge g\).  Negating both conditions gives
(2.1).

Consequently

\[
 K_T=[\ell(T)+1,e(T)]
\]

is the exact set of gaps at which insertion of a \(z\)-cell destroys all
old witnesses for \(T\).

The independent replay computes \(e(T)\) with forward OR frontiers and
\(\ell(T)\) twice: directly with latest-start frontiers and from earliest
deadlines in the reversed word.  The two latest-start arrays agree exactly.
The replay finds all \(65{,}535\) old targets and gives:

| quantity | exact value |
|---|---:|
| targets with nonempty \(K_T\) | 44,698 |
| target-gap incidences | 117,146 |
| internal gaps | 12,872 |
| safe internal gaps | **0** |
| minimum / maximum targets killing one gap | 1 / 14 |

The kernel-length histogram is

~~~
1:8295, 2:12864, 3:13496, 4:7657, 5:2324, 6:47, 7:15.
~~~

The number of killing targets per gap has histogram

~~~
1:1, 2:1, 3:1, 4:1, 5:153, 6:840, 7:1548,
8:2256, 9:3022, 10:2318, 11:1339, 12:917, 13:314, 14:161.
~~~

The JSON retains one checked target for each of the 12,872 gaps.  Its
canonical two-byte certificate-vector digest is

~~~
9ba5481047d7ce16bd53443e073e952bf81eb0bea9e478e38bc61962bb4fca79.
~~~

### Corollary 2.2

Every added \(z\)-cell lies before all of \(X\), or after all of \(X\).

To see this, suppose a marked cell occupies internal gap \(g\).  A witness
for an old target cannot contain that cell, because OR has no cancellation.
Its projected interval in \(X\) therefore cannot cross \(g\).  Universality
would make \(g\) safe, contradicting the exact census.  This remains true
with arbitrarily many marked cells in the same or different gaps.

Thus the only surviving layout is

\[
                         M_{\rm left}\;X\;M_{\rm right}.
\]

## 3. Rank-nine injection

There are

\[
                       \binom{16}{8}=12{,}870
\]

rank-nine targets of the form \(z\cup S\), \(|S|=8\).

For a fixed left start, interval ORs increase with the right deadline.
Therefore that start can deliver at most one distinct rank-nine target: two
distinct equal-rank sets are incomparable.  Every witness starting in \(X\)
must reach the right marked block and hence contains the entire suffix
\(X_i,\ldots,X_{n-1}\).  Its old suffix OR must have rank at most eight.
There are exactly four such starts:

~~~
i = 12869,12870,12871,12872;  suffix OR = 0xf30c; rank = 8.
~~~

The reported start-oriented bound is therefore correct:

\[
  \#\text{marked rank-nine targets}
       \le 11{,}440+4=11{,}444<12{,}870,
\]

with deficiency \(1{,}426\).

### Stronger reverse orientation

The same injection may be made into right endpoints.  A witness ending in
\(X\) must originate in the left marked block and hence contains the entire
prefix \(X_0,\ldots,X_j\).  Prefix rank is at most eight only for

~~~
j=0: prefix OR 0xc3c8, rank 7
j=1: prefix OR 0xc3ca, rank 8
j=2: prefix OR 0xc3ca, rank 8.
~~~

Thus the endpoint-oriented bound is one unit stronger:

\[
                 11{,}440+3=11{,}443<12{,}870,
\]

with deficiency \(1{,}427\).  This is a strengthening, not a correction to
the validity of the reported \(1{,}426\) start bound.

### Strongest label-aware form

The four eligible suffix starts do not provide four possible target labels.
Each complete suffix has the same old OR \(R=\mathtt{0xf30c}\), already of
rank eight.  If an interval from any of those starts represents \(z\cup S\)
with \(|S|=8\), then

\[
                         R\subseteq S,\qquad |R|=|S|=8,
\]

so \(S=R\).  Collectively, all source starts can therefore add at most the
single marked target \(z\cup\mathtt{0xf30c}\) beyond targets assigned to
marked starts.  The strongest audited bound is

\[
                 11{,}440+1=11{,}441<12{,}870,
\]

with deficiency \(1{,}429\).  The reported \(r=4\) count remains a valid
coarser physical-start certificate.

## 4. Small exact split validation

The exact answer words \(k=2,3,4,5\) have six tight coordinate splits, where
deleting all cells containing the chosen coordinate leaves exactly
\(\nu(k-1)\) cells and a universal \((k-1)\)-word:

~~~
(k,coordinate) = (2,0),(2,1),(3,0),(4,0),(4,3),(5,0).
~~~

The two nontrivial internal insertions behave exactly as the gap lemma
requires:

* \(k=4\), coordinate 0: all three marked cells occupy safe gap 1;
* \(k=5\), coordinate 0: two marked cells occupy safe gap 4.

For every marked target \(z\cup S\), the literal interval block

\[
 \bigvee_{I:\,I\cap M\ne\varnothing}
 \left[
   \bigwedge_{p\in I}(A_p\subseteq z\cup S)
   \ \wedge\
   \bigwedge_{b\in z\cup S}\bigvee_{p\in I}(b\in A_p)
 \right]                                                   \tag{4.1}
\]

agrees with direct interval replay in all six splits.  Formula (4.1) is the
exact marked-target DNF underlying a CEGAR encoding.  The primary audit also
exhausts every marked-value assignment for the frozen \(k=2,3,4\) merge
skeletons; the independent audit checks the authenticated assignments and
their complete witness multiplicities.

## 5. Verdict and scope

**GO.**  The fixed-source marked-sector class is solver-free impossible, so
an H100 solve for that class would be redundant.  A viable equality search
must rethread or alter the \(z\)-free carrier, permit a different optimal
\((K=16)\) source, or leave this exact split model.

This is not an unrestricted \((K=17)\) lower bound and does not rule out a
length-24,313 word outside the stated fixed-subsequence class.

Independent replay artifacts:

~~~
scratch/audit_k17_k16_fixed_subsequence_marked_sector_independent_20260731.py
scratch/k17_k16_fixed_subsequence_marked_sector_independent_20260731.audit.json
~~~
