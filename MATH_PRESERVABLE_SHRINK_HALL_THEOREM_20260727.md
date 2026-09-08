# Preservable shrinking is interval stabbing plus Hall

Date: 2026-07-27

## 1. Outcome

Fix a central row

\[
T=(T_0,\ldots,T_{W-1})
\]

and a delay \(d\).  Suppose that some intermediate cells below \(T\) have
already been assigned exact labels.  The remaining factor-label problem has
an exact two-stage normal form:

1. for each coordinate, stab a family of intervals by allowed factor
   positions; and
2. match the desired row-zero masks to positions whose lower witness core is
   contained in the mask and whose upper envelope contains the mask.

There is no further integrality issue.  Conversely, every feasible factor
gives precisely such an interval transversal and Hall matching.

This is a useful strengthening of the pin criterion in
`MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md`: it separates the negative
constraints, the positive witnesses, and the row-zero labels.  It also
identifies a real obstruction.  A coordinatewise *minimum* interval
transversal need not admit the Hall matching.  For the rank-exact \(k=12\)
optimum, the canonical right-endpoint minimum transversal has a five-target,
four-position Hall obstruction.  A one-bit witness split repairs the
central-only instance.

The verified finite data further show that preserving all the designated
intermediate-rank witnesses has a substantial but not total cost.  For
\(k=7,10,11,12\), a Hall-compatible protected core can be chosen with total
bit masses

\[
60,\quad545,\quad976,\quad2546,
\]

against factor masses

\[
66,\quad640,\quad1029,\quad3108.
\]

The computation is reproduced by
`scratch/verify_preservable_shrink_hall.py`.

## 2. Pruned envelopes and demand intervals

Let \(N=W+d\), and put

\[
E_p=\bigcap_{\max(0,p-d)\le i\le\min(W-1,p)}T_i
\qquad(0\le p<N).
\tag{2.1}
\]

Thus every factor \(A\) with \(D^dA=T\) satisfies \(A_p\subseteq E_p\).

Fix a family of exact noncentral pins

\[
\mathcal P=\{(s,j,L):1\le s<d,\ (D^sA)_j=L\}.
\]

The negative part of all pins can be imposed once and for all.  Define the
**pruned envelope**

\[
F_p
=E_p\cap
\bigcap_{\substack{(s,j,L)\in\mathcal P\\p\in[j,j+s]}}L,
\tag{2.2}
\]

where an empty intersection is the full ground set.  A coordinate absent
from a pin label has been deleted from every factor position in that pin's
interval.

For a coordinate \(x\), define its demand family \(\mathcal I_x\) as follows.

* For every \(i\) with \(x\in T_i\), include the central interval
  \([i,i+d]\).
* For every pin \((s,j,L)\) with \(x\in L\), include \([j,j+s]\).

Write

\[
S_x=\{p:x\in F_p\}.
\]

A set \(H_x\subseteq S_x\) is a transversal if it meets every interval in
\(\mathcal I_x\).  Equivalently, with

\[
x\in H_p\quad\Longleftrightarrow\quad p\in H_x,
\]

the row \(H=(H_0,\ldots,H_{N-1})\) supplies one retained occurrence of every
positive coordinate in every prescribed cell.

### Lemma 2.1 (pin feasibility)

The central row and all pins in \(\mathcal P\) are jointly feasible if and
only if every \(\mathcal I_x\) has a transversal in \(S_x\).

#### Proof

Equation (2.2) enforces every negative occurrence constraint.  Every
remaining positive constraint says exactly that an interval in
\(\mathcal I_x\) must contain an allowed occurrence of \(x\).  Coordinates
are independent.  This is Theorem 3.1 of the boundary-flag note after the
negative intervals have been absorbed into \(F\).  \(\square\)

The minimum size \(\tau_x\) of such a transversal is computable greedily.
List \(S_x\) in increasing order.  Its intersection with an ordinary
interval is a consecutive subsequence of this list, so the usual
right-endpoint greedy algorithm is optimal.  Consequently

\[
\tau(\mathcal P,T):=\sum_x\tau_x
\tag{2.3}
\]

is the exact minimum total number of bit occurrences needed to retain the
central row and the chosen intermediate cells inside the pruned envelope.

## 3. The exact Hall--interval theorem

Let \(\mathcal L_0\) be a set of distinct masks which must occur as exact
row-zero entries.  Given a witness core \(H\), form the bipartite graph

\[
G_H=(\mathcal L_0,[0,N-1];\sim)
\]

with

\[
L\sim p
\quad\Longleftrightarrow\quad
H_p\subseteq L\subseteq F_p.
\tag{3.1}
\]

### Theorem 3.1 (preservable-shrink Hall theorem)

The following are equivalent.

1. There is a factor \(A\) such that \(D^dA=T\), every pin in
   \(\mathcal P\) is realized exactly, and every mask in \(\mathcal L_0\)
   occurs at a distinct row-zero position.
2. There is a witness core \(H\) whose coordinate sets \(H_x\) stab all
   intervals in \(\mathcal I_x\), and \(G_H\) has a matching saturating
   \(\mathcal L_0\).

For a fixed \(H\), the second condition is exactly Hall's inequality

\[
|N_{G_H}(\mathcal S)|\ge |\mathcal S|
\qquad(\mathcal S\subseteq\mathcal L_0).
\tag{3.2}
\]

#### Proof

Suppose first that \(A\) exists.  Since every exact pin is realized,
\(A_p\subseteq F_p\).  Take \(H=A\), or delete redundant occurrences from
each coordinate until it is an inclusion-minimal interval transversal.  The
positions at which the distinct masks of \(\mathcal L_0\) occur give a
matching, and at every such position

\[
H_p\subseteq A_p=L\subseteq F_p.
\]

Conversely, let \(\phi\) be a matching saturating \(\mathcal L_0\).  Define

\[
A_p=
\begin{cases}
L,&p=\phi(L),\\
F_p,&p\notin\phi(\mathcal L_0).
\end{cases}
\tag{3.3}
\]

By (3.1), \(H_p\subseteq A_p\subseteq F_p\) at every position.  The lower
inclusion retains a witness for every positive demand interval.  The upper
inclusion respects every negative pin and introduces no coordinate outside
the central envelope.  Thus all pins and all central cells are exact, while
the matched row-zero labels occur literally.  \(\square\)

This theorem is genuinely an equivalence.  The unresolved choice is not an
LP rounding: it is the coupled choice of the interval transversal \(H\) and
the Hall matching.

One useful bookkeeping consequence is

\[
D^{d+q}A=D^qT\qquad(q\ge0).
\tag{3.4}
\]

Thus all cells above the central row depend only on \(T\).  Theorem 3.1 can
change the lower compiler without changing a single upper witness.

## 4. Exact run form and a local forced core

The interval condition admits a particularly simple description for
noncentral cells.  Consider one coordinate and one of its \(1\)-runs
\([l,r]\) in \(T\).

* If the run is internal, its allowed envelope interval is
  \([l+d,r]\).  Both endpoints are mandatory.
* If it is initial but not terminal, its envelope interval is \([0,r]\),
  and only \(r\) is mandatory.
* If it is terminal but not initial, its envelope interval is
  \([l+d,N-1]\), and only \(l+d\) is mandatory.

Let \(U_x\) be the union of all pin intervals whose labels omit \(x\).  The
central row survives for coordinate \(x\) if and only if, on every run,

1. no mandatory endpoint belongs to \(U_x\); and
2. every connected component of \(U_x\) inside the run's envelope has
   length at most \(d\).

In addition, every positive pin interval for \(x\) must meet the envelope
outside \(U_x\).  This is an exact statewise obstruction.  In particular,
two pins can be individually feasible and jointly impossible: for \(d=2\),
two negative intervals \([3,4]\) and \([4,5]\) delete a component of length
three from the interior of a long envelope.

For one noncentral cell \(I=[j,j+s]\), \(s<d\), define

\[
M_I=\bigcup_{p\in I}E_p
\]

and let \(K_I\) be the coordinates having a mandatory run endpoint in
\(I\).

### Corollary 4.1 (one nonboundary cell)

An exact label \(L\) is attainable at the cell \(I\) if and only if

\[
K_I\subseteq L\subseteq M_I.
\tag{4.1}
\]

#### Proof

The upper containment is availability.  If a mandatory endpoint lies in
\(I\), deleting \(I\) destroys a central window, proving the lower
containment.  Conversely, \(|I|=s+1\le d\).  If \(I\) avoids the mandatory
endpoints of a run, its deletion creates an interior gap of length at most
\(d\), or a boundary gap of length at most \(d\); every central window is
still hit.  Positive coordinates are available by \(L\subseteq M_I\).
\(\square\)

For singleton cells write \(K_p=K_{\{p\}}\).  If \(T\) is a Johnson path,
then

\[
|K_p|\le2.
\tag{4.2}
\]

Indeed, at most one coordinate run ends at time \(p\), and at most one run
starts at time \(p-d\).  This explains why the exact words can place very
small masks at many internal positions even though the maximal envelopes
are central-sized.

### Corollary 4.2 (dense safe singleton reservoir)

Let \(P\subseteq[0,N-1]\) contain no \(d+1\) consecutive positions.  Assign
labels \(L_p\) for \(p\in P\) satisfying

\[
K_p\subseteq L_p\subseteq E_p.
\]

Then all singleton pins \(A_p=L_p\) are jointly feasible.  Hence a family of
target masks can be installed whenever the corresponding local-containment
graph on \(P\) satisfies Hall.

The maximum possible size of such a fixed safe reservoir is

\[
N-\left\lfloor{N\over d+1}\right\rfloor,
\tag{4.3}
\]

so this gives a deterministic pin density asymptotic to \(d/(d+1)\).

#### Proof

For each coordinate, the deleted singleton positions form a subset of
\(P\), so every deleted component has length at most \(d\).  Mandatory
endpoints cannot be deleted because they are included in \(K_p\).  Apply the
run criterion above.  Formula (4.3) is the extremal binary-string count for
avoiding \(d+1\) consecutive selected positions.  \(\square\)

## 5. Quantitative witness mass on a Johnson path

For the central demands alone, a coordinate run of length \(\lambda\) needs
exactly

\[
\left\lceil{\lambda\over d+1}\right\rceil
\tag{5.1}
\]

witness occurrences.  For an internal run these include its two mandatory
endpoints; the gaps between consecutive witnesses are at most \(d+1\).

If \(T\) is a Hamilton path through a uniform rank-\(r\) layer, the total
number of coordinate runs is

\[
W+r-1:
\]

there are \(r\) initial runs and every Johnson transition starts one new
run.  Since the sum of all run lengths is \(rW\), a minimum central witness
core has total mass at most

\[
\sum_{p=0}^{N-1}|H_p|
\le
{rW+d(W+r-1)\over d+1}.
\tag{5.2}

Thus the average mandatory witness load is about

\[
{r+d\over d+1},
\]

far below the maximal envelope rank.  The difficulty is not total witness
capacity; it is aligning the phases of these sparse witnesses with the Hall
neighbourhoods of the desired small masks.

## 6. Verified finite audit

For each rank-exact representative, the verifier makes the following fixed
choices.

1. In every intermediate row \(1\le s<d\), place each target of rank
   \(r-d+s\) at its first certified occurrence.
2. Form the pruned envelope \(F\) and all positive demand intervals.
3. Compute the coordinatewise right-endpoint minimum transversal in \(F\).
4. Separately compute a transversal restricted to occurrences in the
   certified factor \(A\).  This second core is Hall-compatible because the
   certified row-zero occurrences supply a matching.

The results are:

| \(k\) | factor mass | pruned-envelope mass | minimum witness mass | Hall size for that minimum | certified Hall-compatible core |
|---:|---:|---:|---:|---:|---:|
| 7 | 66 | 76 | 60 | 26/28 | 60 |
| 10 | 640 | 766 | 539 | 175/175 | 545 |
| 11 | 1029 | 1404 | 963 | 231/231 | 976 |
| 12 | 3108 | 3708 | 2474 | 790/793 | 2546 |

For every Hall-compatible core the construction (3.3) was carried out and
verified independently: the central row, every protected intermediate cell,
and every required row-zero mask survive.  Consequently all upper rows are
unchanged by (3.4).

There is also a smaller central-only obstruction at \(k=12\).  The canonical
right-endpoint minimum core has mass 2164, but its row-zero graph has matching
size 792 instead of 793.  One Hall-deficient set is

\[
\{1168,1169,1200,1232,1680\}
\]

with neighbourhood

\[
\{44,343,609,644\}.
\tag{6.1}
\]

This is not a factor obstruction; it is a statewise obstruction to that
canonical witness phase.  Split the witness for coordinate 12 at position
527 into witnesses at positions 526 and 528.  The core mass rises by one,
the central row remains exact, and the Hall matching becomes 793/793.

So even in a solved optimum, minimum interval mass and Hall compatibility
are distinct objectives.  The preservable-shrink gate is precisely their
joint optimization.

## 7. What remains

The theorem removes the ambiguity in the factor-label stage, but it does not
choose the intermediate pin placement or prove Hall for a general central
path.  A complete construction theorem can now target the following finite
object:

> Choose one cell for every intermediate-rank target so that the resulting
> pruned envelopes admit coordinate interval transversals whose column cores
> satisfy Hall against the row-zero lower ideal.

This is stronger and cleaner than asking vaguely for a factor completion.
Negative constraints are encoded by \(F\); positive constraints are interval
stabbing; the only global integrality condition is ordinary Hall.

