# Purging q=1 repeats preserves all-depth wreath coverage

**Date:** 2026-08-21  
**Method:** pure mathematics; the finite checker is an audit only  
**Status:** exact conditional all-depth lift; construction of the required
all-depth low-hole middle factor remains open

## 0. Outcome

Put

\[
 b=2r+1,\qquad
 \mathcal M=\binom{[b]}r,\qquad
 A=|\mathcal M|,\qquad
 m=A/b=\operatorname{Cat}_r,
 \tag{0.1}
\]

where \(r\ge2\), and let \(\mathscr F\) be an exact middle-wreath factor.
For a row \(C\), a start \(i\in\mathbb Z_b\), and
\(1\le q\le H<r\), let

\[
             T_q(C,i)=I_C(i,r-q)\in\binom{[b]}{r-q}
 \tag{0.2}
\]

be its same-start lower target.  Write

\[
 \begin{aligned}
 A_q&=\binom b{r-q},\\
 \mu_q(T)&=|\{(C,i):T_q(C,i)=T\}|,\\
 h_q&=|\{T:\mu_q(T)=0\}|,\\
 Q_q&=\sum_T(\mu_q(T)-1)_+.
 \end{aligned}
 \tag{0.3}
\]

There are exactly \(A=bm\) start occurrences at every depth, so the exact
collision ledger is

\[
                        Q_q=A-A_q+h_q.                 \tag{0.4}
\]

Assume the two logically separate inputs

\[
             Q_1=O(A/b),\qquad
             \sum_{q=1}^H h_q=o(A),\qquad H=o(b).
 \tag{0.5}
\]

The first is the Catalan-scale q=1 collision bound supplied, for example,
by the capacity-pruning theorem once a low-hole factor is known.  The
second is the weak all-depth wreath-cover condition itself.

There is then an explicit common dirty-start set.  Mark dirty **every**
occurrence whose q=1 target is repeated.  If \(D\) is this set, then

\[
                  |D|\le2Q_1=O(A/b).                 \tag{0.6}
\]

After deleting \(D\):

1. all retained q=1 lower targets are distinct;
2. all retained middle targets are distinct;
3. at every depth q, at most \(|D|\) new lower targets become missing;
4. consequently

   \[
                  \sum_{q=1}^H h'_q
                    \le\sum_{q=1}^Hh_q+H|D|=o(A);     \tag{0.7}
   \]

5. the retained flags can be paired into genuine ribbons after discarding
   at most \(m+|D|=O(A/b)\) further flags; and
6. the total number of row fragments and the cost of an H-boundary collar
   are both \(O(m+|D|)\) and \(O(H(m+|D|))=o(A)\), respectively.

Thus q=1 target co-design and all-depth coverage do compose, at negligible
cost, once the same exact middle factor already has aggregate all-depth
hole count \(o(A)\).  No simultaneous multicommodity flow is needed.

Conversely, a deletion-only compiler can never repair a pre-existing
deeper hole.  Therefore the q=1 hypothesis alone does not close the
all-depth gate: the precise remaining input is the second condition in
(0.5), or another construction which adds missing deeper targets rather
than merely deleting starts.

## 1. Exact ledgers before and after a common deletion

### Lemma 1.1 (full-factor collision ledger)

For every \(1\le q<r\), equation (0.4) holds.  Hence

\[
       \sum_{q=1}^H Q_q
        =HA-\sum_{q=1}^H A_q+\sum_{q=1}^Hh_q.         \tag{1.1}
\]

#### Proof

The \(A\) row-start occurrences at depth q have support size \(A_q-h_q\).
For any finite multiplicity vector, total duplicate excess is total mass
minus support size.  Thus

\[
 Q_q=A-(A_q-h_q),
\]

and summing gives (1.1). \(\square\)

Now let \(D\) be any common set of dirty row-start occurrences, put
\(d=|D|\), and let \(\mu'_q,h'_q,Q'_q\) be the retained multiplicities,
holes, and duplicate excess.  The same \(A-d\) starts survive at every
depth.

### Lemma 1.2 (post-deletion ledger and monotonicity)

For every q,

\[
 Q'_q=A-d-A_q+h'_q,                                  \tag{1.2}
\]

and

\[
             0\le h'_q-h_q\le d.                    \tag{1.3}
\]

More exactly, if \(d_q(T)\) is the number of deleted occurrences of T at
depth q, then

\[
 h'_q-h_q
   =|\{T:\mu_q(T)>0,\ d_q(T)=\mu_q(T)\}|.            \tag{1.4}
\]

#### Proof

Equation (1.2) is the mass-minus-support identity with retained mass
\(A-d\).  A previously present target disappears exactly when all of its
occurrences are deleted, which is (1.4).  Distinct newly missing targets
require disjoint nonempty sets of deleted occurrences, so their number is
at most d. \(\square\)

Summing (1.2) also gives the exact nested retained collision ledger

\[
       \sum_{q=1}^H Q'_q
       =H(A-d)-\sum_{q=1}^H A_q+\sum_{q=1}^Hh'_q.     \tag{1.5}
\]

This distinguishes the unavoidable collision floor from the hole excess.
The desired all-depth coverage controls the last term, not the much larger
unavoidable first two terms.

## 2. The repeated-q=1 purge

Let

\[
 \mathcal R_1=\{T:\mu_1(T)\ge2\},\qquad
 D=\{(C,i):T_1(C,i)\in\mathcal R_1\}.                \tag{2.1}
\]

### Lemma 2.1 (Catalan-size common dirty set)

The dirty set in (2.1) satisfies

\[
 |D|=\sum_{T\in\mathcal R_1}\mu_1(T)
     =Q_1+|\mathcal R_1|\le2Q_1.                    \tag{2.2}
\]

Every retained q=1 target is globally unique.

#### Proof

Every target in \(\mathcal R_1\) contributes at least one to \(Q_1\), so
\(|\mathcal R_1|\le Q_1\).  The displayed identity follows by writing
\(\mu=(\mu-1)+1\) on repeated targets.  All their occurrences are deleted;
every retained occurrence therefore came from a target of original
multiplicity one. \(\square\)

### Theorem 2.2 (conditional all-depth preservation)

Under (0.5), deleting the common dirty set D from (2.1) leaves mutually
distinct middle and q=1 lower targets and satisfies (0.7).  The analogous
upper nested decks also acquire at most \(H|D|\) new holes in aggregate.

#### Proof

Middle targets were distinct before deletion because \(\mathscr F\) is an
exact middle factor.  Lemma 2.1 handles q=1.  Lemma 1.2 gives

\[
 \sum_{q=1}^Hh'_q
   \le\sum_{q=1}^Hh_q+H|D|.
\]

By (0.5)--(0.6), \(H|D|=O(AH/b)=o(A)\), proving (0.7).

For a full cyclic row, complementation sends its family of
rank-\((r+1+q)\) intervals bijectively (after a cyclic shift of starts) to
its rank-\((r-q)\) interval family.  Hence the full upper deck has the same
initial hole count \(h_q\).  At each upper depth, one dirty start deletes
one upper occurrence, so the support of that depth can fall by at most
\(|D|\).  Summing gives the same aggregate bound. \(\square\)

Theorem 2.2 deliberately deletes every occurrence of a repeated q=1
target.  It may sacrifice \(O(A/b)\) otherwise usable q=1 targets, but this
is already \(o(A)\).  This robust choice avoids the edge-capacity and
phase-switching issues of a target-demand flow.

## 3. Ribbon pairing and fragment cost

Within one row, the graph on starts joining disjoint rank-r middle windows
is the cycle C_b generated by the step r.  Put

\[
                    d_C=|D\cap(\{C\}\times\mathbb Z_b)|.
 \tag{3.1}
\]

If \(d_C>0\), deleting those starts leaves at most \(d_C\) paths, whose
maximum matchings leave at most \(d_C\) starts unmatched.  If \(d_C=0\),
the odd cycle C_b has a matching leaving one start unmatched.

### Theorem 3.1 (all-depth fragmented-ribbon lift)

After the purge, discard at most

\[
           |\{C:d_C=0\}|+\sum_{C:d_C>0}d_C
             \le m+|D|                                     \tag{3.2}
\]

additional starts.  The remaining q=1 flags partition into genuine
ribbons with disjoint middle endpoints.  All retained middle and q=1 lower
targets remain mutually distinct, and (0.7) remains true after replacing
its right side by

\[
       \sum_{q=1}^Hh_q+H\bigl(m+2|D|\bigr)=o(A).       \tag{3.3}
\]

#### Proof

The path/cycle matchings above give (3.2), and every matched edge joins two
disjoint middle windows.  The lower facets are their same-start q=1
targets.  Further deletion preserves distinctness.

There were \(|D|\) initial dirty starts and at most \(m+|D|\) pairing
discards.  Lemma 1.2, applied once to their union, bounds the aggregate new
holes by \(H(m+2|D|)\).  Since \(m=A/b\), \(|D|=O(A/b)\), and \(H=o(b)\),
this is o(A). \(\square\)

The number of nonempty path fragments made by D is at most
\(m+|D|=O(A/b)\): count one cyclic component for a row with \(d_C=0\), and
at most \(d_C\) paths otherwise.  Cutting a boundary collar of width H at
every fragment endpoint therefore costs \(O(H(m+|D|))=o(A)\).  This is a
cost statement only; joining the fragments into one prescribed product
order remains a separate factor/order theorem.

## 4. Why a single ordinary max-flow is not the all-depth theorem

For arbitrary common clean-start selection, introduce variables
\(x_{C,i}\in\{0,1\}\).  Simultaneous upper capacities have the form

\[
 \sum_i x_{C,i}\ge b-c_C,
 \qquad
 \sum_{(C,i):T_q(C,i)=T}x_{C,i}\le u_{q,T}
 \quad(1\le q\le H).                                  \tag{4.1}
\]

At q=1 alone this is bipartite b-matching.  Across several depths a column
\(x_{C,i}\) meets one constraint in every target layer, so (4.1) is a
multilayer hypergraph packing system, not an ordinary one-commodity flow.

The failure is already visible in three individually physical nested
profiles at r=4:

\[
 \begin{array}{c|ccc}
 &q=3&q=2&q=1\\ \hline
 P_1&\{1\}&\{1,3\}&\{1,2,3\}\\
 P_2&\{2\}&\{1,2\}&\{1,2,3\}\\
 P_3&\{1\}&\{1,2\}&\{1,2,4\}.
 \end{array}                                            \tag{4.2}
\]

For example, these are the start-zero prefix profiles of the cyclic rows

\[
 (1,3,2,5,4,6,7,8,9),\quad
 (2,1,3,6,4,5,7,8,9),\quad
 (1,2,4,7,3,5,6,8,9),                              \tag{4.2a}
\]

respectively.  Their rank-four middle hosts at those starts are distinct.

The three shared-target rows, respectively at q=1 for P1,P2, q=2 for
P2,P3, and q=3 for P3,P1, restrict to the matrix

\[
 \begin{pmatrix}
 1&1&0\\0&1&1\\1&0&1
 \end{pmatrix},
 \qquad \det=2.                                        \tag{4.3}
\]

Thus the natural multilayer constraint matrix for physical row profiles is
not totally unimodular;
with unit capacities its fractional point (1/2,1/2,1/2) has value 3/2,
while the integral optimum is one.  Each profile in (4.2) is a same-start
prefix chain of a cyclic row, so nesting alone does not remove the gate.

This non-TU example does not obstruct Theorems 2.2--3.1.  Those theorems
use the explicit common purge D and ask only for q=1 injectivity plus
all-depth coverage, not simultaneous injectivity or prescribed capacities
at every depth.

## 5. Scope

The proved content is:

1. the exact pre- and post-deletion collision ledgers (0.4), (1.2), and
   (1.5);
2. an explicit Catalan-size common dirty set giving q=1 target
   disjointness;
3. aggregate all-depth hole preservation at cost O(AH/b)=o(A);
4. an O(A/b)-fragment genuine-ribbon lift with o(A) collar cost; and
5. an explicit nested non-TU minor explaining why separate-depth flows do
   not automatically coinstantiate.

The theorem assumes, and does not construct, the aggregate deeper-hole
bound in (0.5).  It does not prove the C8 energy target, an all-depth factor,
the final fragment-order compiler, or a universal word.  It also does not
claim simultaneous target injectivity at depths q>=2, which is generally
incompatible with the layer cardinalities.

## 6. Checker

The finite audit is

```text
scratch/audit_q1_repeat_purge_all_depth_coverage_20260821.py
```

It constructs the canonical factors through b=11, checks every exact
ledger and purge bound at every lower depth, materializes the ribbon
pairing, and checks the determinant-two nested profile minor.  The finite
computation is an audit only; the proofs above are solver-independent.
