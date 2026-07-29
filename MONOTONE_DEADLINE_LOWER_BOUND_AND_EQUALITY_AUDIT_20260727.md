# Monotone deadlines: a valid proof of the rank-slack lower bound

Date: 2026-07-27

## 1. Verdict

The proposed monotonicity proof of

\[
\nu(k)\ge B(k)
\]

is valid after fixing indexing conventions.  It is a particularly clean
proof: middle-layer witnesses create monotone physical deadlines, and those
deadlines cap the total number of lower-rank cells.

The stronger equality claims need correction.  Zero slack really does force
the flat central row and a bijective lower band, explaining (k=6,9).
Positive slack does not force flatness, rank ordering, a boundary flag, or
exact higher-row ranks.  Those remain selected structural properties of the
known representatives.

## 2. The proof

Let (A=(A_1,ldots,A_L)) be a nonzero universal word.  Put

\[
r=\lceil k/2\rceil,qquad W=\binom kr,qquad e=L-W,qquad
\Lambda=\sum_{s=1}^{r-1}\binom ks.
\]

For (0\le j\le L-i), define

\[
C_i^{(j)}=A_i\cup\cdots\cup A_{i+j}.
\]

Let (f_i) be the number of initial cells in column (i) having rank below
(r), and put (F_i=i+f_i).  If the whole column is lower, then
(F_i=L+1).

### Lemma 2.1 (monotone deadlines)

The sequence (F_1,ldots,F_L) is nondecreasing.

#### Proof

For (f_i\ge2),

\[
C_{i+1}^{(f_i-2)}\subseteq C_i^{(f_i-1)},
\]

so (f_{i+1}\ge f_i-1), hence (F_{i+1}\ge F_i).  For
(f_i\in\{0,1\}), the inequality follows directly from (f_{i+1}\ge0).
\(\square\)

### Lemma 2.2 (middle witnesses have distinct deadlines)

If columns (i<i') contain distinct rank-(r) targets, their corresponding
deadlines are distinct.

#### Proof

A column which meets rank (r) does so first at row (f_i), on interval
([i,F_i]).  If (F_i=F_{i'}), then

\[
[i',F_i]\subset[i,F_i],
\]

so the two OR labels are nested.  Equal-rank nested sets are equal, contrary
to distinctness.  \(\square\)

All (W) middle targets must occur, so (F) has at least (W) distinct
values at most (L).

### Lemma 2.3 (depth cap)

For every (i),

\[
f_i\le\min\{e,L-i+1\}.
\tag{2.1}
\]

#### Proof

Let (v_1<\cdots<v_p\le L) be the distinct deadline values not equal to
(L+1); then (p\ge W).  If (F_i=v_t), monotonicity puts at least
(t-1) earlier distinct values before (i), so (i\ge t), while room for
the later distinct values gives (v_t\le L-(p-t)).  Therefore

\[
f_i=v_t-i\le L-p\le L-W=e.
\]

If (F_i=L+1), then (i\ge p+1\ge W+1), so again
(f_i=L+1-i\le e).  The column length supplies the other cap. \(\square\)

Every lower target appears among these lower cells.  Hence

\[
\Lambda\le\sum_i f_i
\le\sum_{i=1}^{L}\min\{e,L-i+1\}
=eL-\binom e2
=eW+\binom{e+1}{2}.
\tag{2.2}
\]

By the definition of (d(k)), this forces (e\ge d(k)), and therefore

\[
\boxed{\nu(k)\ge W+d(k)=B(k).}
\]

## 3. The exact equality ledger

Now take (L=W+d), and define

\[
g_i=\min\{d,L-i+1\},qquad
\sigma=\sum_i g_i-\Lambda
=dW+\binom{d+1}{2}-\Lambda.
\]

There are two independent losses:

\[
\Delta_{\rm depth}=\sum_i(g_i-f_i),
\qquad
\Delta_{\rm repeat}=\sum_i f_i-\Lambda.
\]

The second quantity is exactly the number of repeated lower-cell occurrences,
counted with multiplicity.  Equation (2.2) gives the exact decomposition

\[
\boxed{\sigma=\Delta_{\rm depth}+\Delta_{\rm repeat}.}
\tag{3.1}
\]

This is the correct general equality analysis.  In particular:

- at most (sigma) units of the deadline cap are unused;
- there are at most (sigma) repeated lower occurrences;
- neither loss is individually determined when (sigma>0).

### Zero slack

If (sigma=0), then (f_i=g_i) for every column and every lower cell is a
different lower target.  For (i\le W), one has (f_i=d); all later columns
are entirely lower.  Consequently the (W) middle targets must occur exactly
as

\[
C_1^{(d)},\ldots,C_W^{(d)},
\]

so (D^dA) is a permutation of the middle layer.  This rigorously explains
the rigidity at (k=6,9).

Even at zero slack, cells above the central row are only forced to have rank
at least (r); they may repeat a middle target.  Exact successive upper-rank
grading does not follow from the scalar proof.

### Positive slack

For (k=11), (sigma=369), comparable with (W=462).  Equation (3.1)
therefore does not force the flat middle row or the observed waste vector
((234,134,1)).  The optimal (k=4) word

\[
(10,9,5,1,2,4,8)
\]

already shows that an optimal word need not have a flat central derivative.
Thus capacity ordering and central flattening require the separate exchange
theorems isolated in `MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md`.

The fact that row (d-1) has (W+1) cells in odd dimension is a useful
capacity observation.  It becomes a one-spare-cell statement only after one
chooses the normal form in which that row enumerates the adjacent middle
rank.  It does not by itself force the nested boundary flag.

## 4. Corrections to the Catalan/run interpretation

The Catalan block counts require the extra one-hole lower-rainbow hypothesis;
they do not follow from an arbitrary middle permutation.  For a central
rank-((m+1)) path on (2m+1) points,

\[
\#\{T:x\in T\}=\binom{2m}{m}=(m+1)C_m,
\]

while the ballot theorem gives (C_m) or (C_m+1) containing blocks,
depending on the endpoint flag.  The mean block length is therefore
approximately (m+1), with an exact endpoint correction—not identically
(m) in every coordinate.

The coordinatewise residence criterion is exact:

\[
D^dA=T
\quad\Longleftrightarrow\quad
\text{every internal coordinate 1-run of (T) has length at least (d+1)}.
\]

Here the equivalence permits an empty physical letter.  In the nonzero-word
problem one must additionally require that every physical position have a
nonempty legal erosion envelope.  This is automatic for the resident
Johnson carriers used in the exact constructions (their flat erosion has
rank `r-d>0`), but it is false for an arbitrary ordering: for example,
`T=({1},{2})` at depth one passes the internal-run test while forcing the
middle physical letter to be empty.

But wreaths are only special perfectly periodic solutions with much longer
residence.  Periodicity of the individual coordinate traces is not sufficient
to make their phases arise from one cyclic order, and the minimum-residence
condition certainly does not force a wreath.

## 5. Correction to the diamond-lift inference

At the (2m+1\to2m+3) lift, a new coordinate occurs in

\[
\binom{2m+2}{m+1}=(m+2)C_{m+1}
\]

central vertices.  The one-hole ballot theorem forces about (C_{m+1})
containing blocks, so their mean length is (m+2), not approximately
(2k).

This mean is still much larger than (d=\Theta(\sqrt k)), but a large mean
does not imply the required minimum.  The q1-perfect (k=11) connector has
the correct forced block count and nevertheless has many runs of length two
and three.  Therefore residence is not free under batching; equitable block
lengths—or the fresh-rotor/hazard transversal—remain necessary.

The genuinely open diamond question is exactly the one identified in the
proposal: can the sector braid preserve both shadow marginals while keeping
all residence runs above the compiler threshold?  The Catalan block count
alone answers neither part.

## 6. Correction to the (k=11) reduction

Projecting a Middle Levels Hamilton cycle does make the immediate lower
rank perfect automatically.  Consecutive rank-six sets have unions of rank
seven, so the opposite immediate condition concerns

\[
\binom{[11]}7,
\]

not \(\binom{[11]}8\).  Rank eight is the next, three-vertex window and remains
a separate condition.  Thus the seed removes one immediate rainbow gate,
but does not reduce the whole upper tower to a single condition.

## 7. Net contribution

The useful new content is:

1. a short independent proof of the known rank-slack lower bound;
2. the exact slack identity (3.1), separating missed depth capacity from
   repeated lower occurrences; and
3. a clean explanation of why the zero-slack cases force the observed flat
   central row.

The positive-slack rank grading, boundary flag, minimum residence, and
two-sided diamond lift remain genuine construction phenomena rather than
corollaries of the scalar proof.
