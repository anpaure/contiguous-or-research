# Boundary flags in an OR--Pascal factor

Date: 2026-07-27

## 1. Outcome

There are two separate issues in passing from a central Johnson path to an
OR word:

1. does the central row have a Boolean OR preimage of delay (d)?
2. can prescribed lower cells survive in such a preimage?

Both questions have exact coordinatewise answers.  The first is the familiar
residence condition.  The second is an interval hitting criterion.  At a
linear endpoint this criterion simplifies further: a nested missing-shadow
flag can be put on a boundary anti-diagonal if and only if its membership
thresholds dominate the terminal residence lengths.

This is not by itself a proof of the exact formula.  It removes the
factorization/integrality ambiguity from the one-flag line and isolates the
remaining requirement: enough nonboundary lower witnesses must survive the
chosen endpoint truncations.

It also led to new canonical representatives.  The published (k=7), the
stored (k=10) and (k=12) optima, and the length-465 (k=11) near-solution
admit respectively one, four, four, and two envelope-preserving edits after
which the shortest-window grading is exact by rank.  For (k=11), the right
boundary is the literal
flag

\[
\{1,2,3,4,5\}\supset
\{1,2,3,4\}\supset
\{1,2,4\}.
\tag{1.1}
\]

The modified (k=11) word is stored in
`k11_upper549_rank_exact_flag.txt`; all four sparse edit certificates are
checked by `scratch/verify_rank_exact_representatives.py`.

## 2. Binary factorability

Let

\[
T=(T_0,\ldots,T_{W-1}),\qquad
A=(A_0,\ldots,A_{W+d-1})
\]

be set-valued rows, and write

\[
(D^dA)_i=\bigcup_{j=i}^{i+d}A_j.
\]

For a position (j), define the maximal envelope

\[
E_j:=\bigcap_{\max(0,j-d)\le i\le\min(W-1,j)}T_i.
\tag{2.1}
\]

Every factor (D^dA=T) satisfies (A_j\subseteq E_j).

### Theorem 2.1 (exact residence criterion)

There is an (A) with (D^dA=T) if and only if every internal (1)-run of
every coordinate in (T) has length at least (d+1).  In that case the
maximal envelope itself is a factor:

\[
D^dE=T.
\tag{2.2}
\]

#### Proof

Work with one coordinate.  For an internal (1)-run ([l,r]), the only
positions at which the coordinate may occur in (A) are

\[
[l+d,r].
\]

Indeed, the zero immediately before the run kills positions through
(l+d-1), and the zero immediately after it kills positions from (r+1)
onward.  The first (1)-window can be hit only at (l+d), so the interval is
nonempty only if (r-l+1\ge d+1).  Conversely, putting the coordinate at
every position of ([l+d,r]) hits precisely the central windows in the run.

For an initial run ([0,r]), the envelope positions are ([0,r]); for a
terminal run ([l,W-1]), they are
([l+d,W+d-1]).  These always reproduce their respective runs.  Taking the
union over all coordinate runs gives (2.2).  Since coordinates are
independent, this proves the theorem.  \(\square\)

The maximal factor also converts central intersections into literal
OR--Pascal cells.

### Lemma 2.2 (maximal core identity)

If (E) is the maximal factor and (1\le q\le d), then

\[
(D^{d-q}E)_{i+q}=\bigcap_{h=0}^{q}T_{i+h}
\qquad(0\le i<W-q).
\tag{2.3}
\]

#### Proof

The cell on the left is the union of the envelope positions
([i+q,i+d]).  If a coordinate occurs at one of those positions, every one
of the central windows ([i,i+d],\ldots,[i+q,i+q+d]) contains that position,
so the coordinate lies in the intersection on the right.

Conversely, suppose the coordinate lies throughout (T_i,\ldots,T_{i+q}),
and let ([l,r]) be the (1)-run containing this interval.  The envelope
portion belonging to the run intersects ([i+q,i+d]): for an internal run it
is ([l+d,r]), and the inequalities (i+d\ge l+d) and (i+q\le r) give the
intersection.  Initial and terminal runs are even easier.  \(\square\)

Thus the maximal factor preserves *all* lower central shadows through depth
(d).  Shrinking the envelope is the only source of lost core witnesses.

## 3. Prescribed cells have an exact interval criterion

A **pin** is a triple ((s,j,L)), meaning that the desired tableau cell is

\[
(D^sA)_j=L,\qquad 0\le s\le d.
\]

Associate to the pin the interval (J=[j,j+s]) of positions of (A).

### Theorem 3.1 (pin survival iff interval hitting)

Fix any finite collection (\mathcal P) of pins.  There exists an (A)
realizing all pins if and only if the following holds for every coordinate
(x).

Let

\[
Q_x=[0,W+d-1]\setminus
\bigcup_{(s,j,L)\in\mathcal P:\ x\notin L}[j,j+s].
\tag{3.1}
\]

Then every positive pin interval contains an allowed position:

\[
x\in L\quad\Longrightarrow\quad [j,j+s]\cap Q_x\ne\varnothing.
\tag{3.2}
\]

When this condition holds, the coordinatewise maximal realization is simply

\[
x\in A_j\quad\Longleftrightarrow\quad j\in Q_x.
\tag{3.3}
\]

#### Proof

A pin excluding (x) forbids (x) at every position of its interval, which
gives (3.1).  A pin containing (x) requires at least one occurrence in its
interval, giving the necessity of (3.2).  Conversely, selecting every allowed
position as in (3.3) avoids all negative pins and hits all positive pins.
Do this independently for each coordinate.  \(\square\)

Including all central pins ((d,i,T_i)) specializes Theorem 3.1 to a complete
and polynomial-time test for a partial lower compiler.  There is no separate
integral rounding problem: after the target cells have been assigned, the
maximal legal factor is explicit.

## 4. The endpoint flag theorem

Assume now that (T) is a permutation of a nontrivial uniform layer, so no
coordinate is present at every central position.  For
(x\in T_{W-1}), let

\[
\lambda_x:=\max\{L:T_{W-L},\ldots,T_{W-1}\text{ all contain }x\}
\tag{4.1}
\]

be its terminal residence length.

The right boundary anti-diagonal consists of

\[
B_q(A):=(D^{d-q}A)_{W+q-1}
=\bigcup_{j=W+q-1}^{W+d-1}A_j,
\qquad 1\le q\le d.
\tag{4.2}
\]

It is automatically nested:

\[
B_1\supseteq B_2\supseteq\cdots\supseteq B_d.
\]

### Theorem 4.1 (boundary-flag absorption, exact form)

Suppose (T) satisfies Theorem 2.1.  Let

\[
F_1\supseteq F_2\supseteq\cdots\supseteq F_d
\tag{4.3}
\]

be prescribed sets.  There exists a factor (D^dA=T) satisfying
(B_q(A)=F_q) for every (q) if and only if

1. (F_q\subseteq T_{W-1}) for every (q); and
2. for every (q),
   \[
   \{x\in T_{W-1}:\lambda_x\le d-q+1\}\subseteq F_q.
   \tag{4.4}
   \]

Equivalently, put

\[
h_x=\max\{q:x\in F_q\},
\]

with (h_x=0) if (x\notin F_1).  The condition is

\[
\lambda_x\ge d-h_x+1
\qquad(x\in T_{W-1}).
\tag{4.5}
\]

#### Proof

Let the terminal run of (x) begin at (l=W-\lambda_x).  The zero preceding
that run forces the first possible occurrence of (x) in (A) to be

\[
p_0=l+d=W-\lambda_x+d,
\]

and the first central (1)-window forces (x\in A_{p_0}).  Hence (x) is
forced into (B_q) exactly when

\[
p_0\ge W+q-1,
\]

which is equivalent to (lambda_x\le d-q+1).  This proves necessity.

For sufficiency, let

\[
p_x=W+h_x-1
\]

(with (p_x=W-1) when (h_x=0)), and put (x) at every terminal-run
envelope position from (p_0) through (p_x).  Condition (4.5) says this
interval is nonempty.  It hits every central window in the terminal run, and
it meets the suffix in (4.2) exactly for (q\le h_x).  Use the maximal
envelope on every other run.  The construction is coordinatewise, so it
simultaneously realizes the whole flag.  \(\square\)

There is an identical left-boundary theorem using initial residence lengths
and the cells ((D^{d-q}A)_0).

For a single boundary cell, Theorem 3.1 gives a useful more general formula.
For (0\le t<q), the cell

\[
(D^{d-q}A)_{W+t}
\]

must contain every terminal coordinate whose residence length lies in

\[
q-t\le\lambda_x\le d-t.
\tag{4.6}
\]

It can contain only coordinates with (lambda_x\ge q-t).  Thus the exact
single-cell interval is

\[
\{x:q-t\le\lambda_x\le d-t\}
\ \subseteq\ (D^{d-q}A)_{W+t}\ \subseteq\
\{x:\lambda_x\ge q-t\}.
\tag{4.7}
\]

Every set between these two bounds is attainable when this is the only extra
prescribed cell.  The anti-diagonal in Theorem 4.1 has (t=q-1), so its
upper bound is the whole terminal set, while its lower bound is precisely
the residence condition (4.4).

## 5. Endpoint-rooted middle-levels normal form

Let (k=2m+1), and let (T_0,\ldots,T_{W-1}) be a Hamilton path in the
rank-((m+1)) Johnson graph.  Put

\[
C_i=T_i\cap T_{i+1}.
\]

If the (C_i) are distinct, miss only (C_*\in\binom{[k]}m), and
(C_*\subset T_{W-1}), then

\[
T_0,C_0,T_1,C_1,\ldots,C_{W-2},T_{W-1},C_*
\tag{5.1}
\]

is a Hamilton path of the full middle-levels graph.  Thus the first member of
the missing lower flag is naturally rooted at the terminal central set, which
is exactly the geometry required by Theorem 4.1.

The published (k=7) optimum, the (k=9) optimum, and the (k=11)
near-solution have respectively

\[
C_*=81,\qquad170,\qquad31.
\]

The (k=7) deeper deficit continues as the terminal flag
(81\supset80), and Theorem 4.1 applies.  At (k=9), the desired suffix flag
(170\supset42) fails the criterion: coordinate (8) has terminal residence
one, so it is forced into the depth-two suffix cell although (8\notin42).
The stored optimum therefore uses an off-diagonal boundary cell for (42).
This is a concrete demonstration that “one nested flag” alone is not a
sufficient hypothesis; endpoint residence is the missing local condition.

At (k=11,d=3), the terminal residence lengths of the endpoint coordinates
(1,\ldots,6) are

\[
(4,8,2,1,3,15).
\]

The literal suffix flag (31\supset15\supset11) satisfies (4.4): the
successive forced sets are contained in it.  It is realized by the new
rank-exact representative.

## 6. Four rank-exact normalizations

All positions below are zero-based.

### (k=7), exact optimum

In the published word, replace (A_0=42) by (A_0=32).  The union
(A_0\cup A_1=42) is unchanged, hence so is (D^2A), and all masks remain
covered.  Length one now first realizes exactly ranks one and two, and each
subsequent length first realizes exactly the next rank.  The literal word is
`k7_published_rank_exact.txt`.

### (k=10), exact optimum

Starting from `k10_optimal_nonzero.txt`, make

\[
A_0=112,\quad A_1=100,\quad A_{252}=70,\quad A_{253}=69.
\]

The central row (D^2A) is unchanged and all (1023) nonzero masks remain
covered.  The first-occurrence grading is exactly

\[
\begin{array}{c|c}
\text{window length}&\text{new ranks}\\ \hline
1&1,2,3\\
2&4\\
3&5\\
4,5,6,7&6,7,8,9.
\end{array}
\]

### (k=11), length-465 near-solution

Starting from `k11_upper549_natural_array.txt`, make

\[
A_{128}:6\mapsto22,\qquad A_{463}:22\mapsto4.
\]

The central row (D^3A) is unchanged, the same twelve rank-seven masks and
one rank-eight mask are absent, and every rank at most six is covered.  More
strongly,

\[
\begin{array}{c|c}
1&\text{all ranks }1,2,3\\
2&\text{all rank }4\\
3&\text{all rank }5\\
4&\text{all rank }6.
\end{array}
\]

The two edits change no cell of (D^2A).  The terminal anti-diagonal is
exactly (1.1).

### (k=12), exact optimum

Starting from `k12_optimal_nonzero.txt`, make

\[
A_1=1540,\quad A_{182}=1796,\quad A_{381}=801,\quad A_{925}=769.
\]

Again (D^2A) is unchanged and all masks remain covered.  Length one first
realizes exactly ranks (1)--(4), length two exactly rank (5), length
three exactly rank (6), and every subsequent length first realizes exactly
the next rank.

These are not search improvements in length.  They are structural
canonicalizations.  They show that the premature central cells in the old
(k=10) and (k=12) representatives, and the non-strict terminal flag in the
old (k=11) representative, were presentation artifacts rather than forced
features.

## 7. Exact remaining boundary

Theorems 2.1, 3.1, and 4.1 prove:

* factorability is exactly residence;
* a prescribed lower compiler has no hidden integrality gap after its pins
  are chosen; and
* a nested endpoint flag is absorbable exactly when (4.4) holds.

They do **not** prove that every central one-flag path has enough mutually
compatible pins to cover all ranks below (r-d).  Nor do they preserve every
nonmissing central-intersection witness automatically when the suffix of the
maximal envelope is truncated.  Those demands are precisely the
preservable-shrink problem.

For (k=11), however, the literal certificate proves that the complete lower
compiler and the strict boundary flag coexist while leaving the upper defect
unchanged.  Consequently any repair of the thirteen upper masks which keeps
the certified central pins feasible can be handed to Theorem 3.1 without a
separate completion or rounding step.
