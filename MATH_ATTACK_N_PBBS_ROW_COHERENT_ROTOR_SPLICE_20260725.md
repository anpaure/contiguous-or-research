# Lane N: the sharp row-coherent PBBS rotor-splice theorem

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, finite search,
solver, or long-running job is used.

## 0. Outcome and exact boundary

Put

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 B=\operatorname {Cat}_m={W\over n}.
\tag{0.1}
\]

This report proves the sharp sufficient splice theorem requested for the
two-sided PBBS \(q=1\) transition construction. Its new point is that the
two signed residence defects are not independent. If two consecutive
occurrences of one PBBS omitted label have gap

\[
 g=2s+1,
\tag{0.2}
\]

then one step-two row has a positive run of length \(s+1\), while the other
row has a zero run of length \(s\). Both are too short for signed
radius \(H\) at exactly the same threshold

\[
 s\le H-1\quad\Longleftrightarrow\quad g\le2H-1.
\tag{0.3}
\]

A single **row-coherent atom** deletes two consecutive-index projected
transition edges, one from each conceptual row. For every gap in (0.3), every atom which hits
the zero-run interval automatically hits the positive-run interval. The
simultaneous two-sided cutting problem is consequently one ordinary
circular-interval transversal problem, not two unrelated transversals.

For the already linear two-sided \(q=1\) forest, let

\[
 \widehat\nu_H
\tag{0.4}
\]

be the maximum number of pairwise disjoint residual atom-site intervals
defined in Section 3. The construction in Theorem 5.1 deletes at most

\[
 \boxed{4\widehat\nu_H}
\tag{0.5}
\]

retained Johnson edges and turns every remaining component into a genuine,
endpoint-recanonicalized, zero-portal signed natural-departure
radius-\(H\) rotor path. The constant \(4\) consists of the sharp
circular-interval factor at most \(2\), followed by two projected edges per
row-coherent atom. On a line the first factor is \(1\), so the bound is
\(2\widehat\nu_H\).

In particular, for every fixed \(A,K>0\), uniformly for

\[
 1\le H\le A\sqrt m,
\tag{0.6}
\]

the bound

\[
 \boxed{\widehat\nu_H\le K B}
\tag{0.7}
\]

implies an \(O(B)\)-edge row-coherent splice. It destroys at most
\(4KB=o(W/H)\) old lower colours and the same number of old upper colours.
Together with the previously proved PBBS \(q=1\) forest ledger, the final
number of paths and both missing-colour counts remain \(o(W/H)\), and the
literal signed reset cost is \(o(W)\).

Equation (0.7) is also the exact remaining PBBS-specific gate for this
canonical zero-portal, row-coherent-atom cut architecture, up to the
displayed absolute factors: every such repair deletes at least
\(\widehat\nu_H\) distinct old edges. It is **not proved here**. Therefore this
report does not prove the constant-one conjecture.

Two audits delimit the remaining gate sharply.

1. A genuine level-three PBBS component contains at least

   \[
     2\left\lfloor{3(2m-1)-1\over9}\right\rfloor
   \tag{0.8}
   \]

   pairwise edge-disjoint radius-three defects. Thus component count, or
   laminarity by itself, cannot yield an \(O(1)\)-per-component estimate
   toward (0.7).

2. A proposed stronger obstruction based only on the height of a
   primitive Dyck root is false. Section 9 gives an exact symbolic
   counterexample. Hence neither a positive nor a negative answer to
   (0.7) follows from Dyck height alone.

All integrality, colour, component, and literal-reset constants are proved
below.

## 1. The exact signed rotor convention

Throughout the rotor statements, \(1\le H<m\). This includes (0.6) for
all sufficiently large \(m\).

Let

\[
 X_{t+1}=X_t-\{r_t\}+\{a_t\}
\tag{1.1}
\]

be a directed Johnson path. An internally bounded positive run begins
when a coordinate is inserted and ends when it is next removed. An
internally bounded zero run begins when a coordinate is removed and ends
when it is next inserted.

The canonical zero-portal signed natural-departure radius-\(H\) conditions
are

\[
 \boxed{
 a_p\ne r_q\quad(0<q-p\le H),
 }
\tag{1.2}
\]

and

\[
 \boxed{
 r_p\ne a_q\quad(0<q-p\le H-1).
 }
\tag{1.3}
\]

Equivalently, every internally bounded positive run has at least \(H+1\)
owners and every internally bounded zero run has at least \(H\) owners.
The one-unit asymmetry is essential.

Indeed, an insertion at transition \(p\) and the following removal at
transition \(q\) produce the positive owners

\[
 X_{p+1},X_{p+2},\ldots,X_q,
\]

so that the run length is \(q-p\). A removal at \(p\) and following
insertion at \(q\) analogously produce a zero run of length \(q-p\).
This proves the equivalence with (1.2)--(1.3).

When (1.2)--(1.3) hold, the forced internal queue prefix at \(X_i\) is

\[
\begin{aligned}
 B_i&=X_i\setminus\{r_i,r_{i+1},\ldots,r_{i+H-1}\},\\
 \Pi_i&=(B_i,
 \{r_{i+H-1}\},\ldots,\{r_i\},
 \{r_{i-1}\},\ldots,\{r_{i-H}\},\mathcal R_i).
\end{aligned}
\tag{1.4}
\]

The first \(H\) singleton blocks are the next departures and the second
\(H\) are the previous departures. The run inequalities say exactly that
the former are distinct members of \(X_i\) and the latter are distinct
nonmembers. Moving from \(X_i\) to \(X_{i+1}\) shifts these queues by one
and gives the consecutive flags

\[
 \Gamma^-_{i,q}=\bigcap_{u=0}^qX_{i+u},
 \qquad
 \Gamma^+_{i,q}=\bigcup_{u=0}^qX_{i-u}.
\tag{1.5}
\]

At a finite endpoint, absent past or future transitions are replaced by
dummy boundary departures. For completeness, at the terminal owner order
its \(m\) coordinates by increasing time of last entry, with coordinates
present throughout first. Exclude the latest one and dummy-depart any
\(H\) of the other \(m-1\) coordinates in increasing last-entry order.
For a selected coordinate in position \(t\), the genuine departures caused
by later terminal entries and the earlier selected dummy departures total
at least

\[
 (m-t)+\max\{0,t-1-(m-H-1)\}\ge H.
\]

Thus no short positive run is created. Reverse time and
complement for the initial endpoint. Thus a safe path with \(v\) retained
owners has an independently recanonicalized literal signed lift of exact
length

\[
 \boxed{v+2H.}
\tag{1.6}
\]

The retained depth-one colours remain literally
\(X_i\cap X_{i+1}\) and \(X_i\cup X_{i+1}\); endpoint dummy flags do not
alter them.

The scope in this section matters. Conditions (1.2)--(1.3) are exact for
the canonical zero-portal natural-departure architecture. They are not
necessary for arbitrary priority-prefix rotors: a queued arrival can be
paid for by a portal, and an upper-singleton re-entry can bypass a short
zero run. Every construction below is a genuine zero-portal rotor
construction, but the lower bounds are asserted only in this canonical
class.

## 2. The PBBS return dictionary on both rows

Work in one local pair-omission ground set \(Q\), of odd size

\[
 N=2r+1.
\tag{2.1}
\]

Let

\[
 A_0,A_1,\ldots,A_{L-1}
\]

be an oriented component of the canonical PBBS odd-graph factor, with all
indices circular modulo \(L\). Let \(\lambda_i\) be the omitted coordinate
on the edge \(A_iA_{i+1}\). The audited recurrence is

\[
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.
\tag{2.2}
\]

Put \(X_i=Q\setminus A_i\), and index the projected transition edges by

\[
 E_t:X_{t-1}\longrightarrow X_{t+1}.
\tag{2.3}
\]

Then

\[
 E_t\text{ removes }\lambda_{t-1}
 \quad\text{and inserts }\lambda_t.
\tag{2.4}
\]

Consecutive occurrences of one omitted label have odd gap at least three.
Write such a pair as

\[
 \lambda_i=\lambda_j,
 \qquad j-i=2s+1,
 \qquad s\ge1.
\tag{2.5}
\]

### Lemma 2.1 -- synchronized signed defect

For (2.5), the row containing \(E_i\) has a positive run of length \(s+1\)
whose boundary-transition interval is

\[
 I^+_{i,j}=\{E_i,E_{i+2},\ldots,E_{j+1}\},
 \qquad |I^+_{i,j}|=s+2.
\tag{2.6}
\]

The other step-two row has a zero run of length \(s\) whose boundary
interval is

\[
 I^0_{i,j}=\{E_{i+1},E_{i+3},\ldots,E_j\},
 \qquad |I^0_{i,j}|=s+1.
\tag{2.7}
\]

Both runs violate the full signed radius-\(H\) conditions precisely when

\[
 s\le H-1.
\tag{2.8}
\]

#### Proof

By (2.4), \(E_i\) inserts \(\lambda_i\). Since the two displayed
occurrences are consecutive, that coordinate remains present along its
step-two row until \(E_{j+1}\), which removes \(\lambda_j\). The transition
distance is

\[
 {j+1-i\over2}=s+1,
\]

giving (2.6) and the positive-run length \(s+1\).

On the opposite row, \(E_{i+1}\) removes \(\lambda_i\), while \(E_j\)
inserts \(\lambda_j\). Their transition distance is

\[
 {j-(i+1)\over2}=s,
\]

giving (2.7) and the zero-run length \(s\). A positive run is forbidden
when its length is at most \(H\); a zero run is forbidden when its length
is at most \(H-1\). Both inequalities reduce to (2.8). \(\square\)

Thus every short omitted-label return creates one synchronized signed
defect packet. This is the property which makes row-coherent cutting
possible.

## 3. Row-coherent atoms and their exact demand intervals

At an underlying PBBS boundary \(t\), define the row-coherent cut atom

\[
 \mathcal C_t=\{E_t,E_{t+1}\}.
\tag{3.1}
\]

If \(L\) is even, its two edges lie on the two step-two parity cycles. If
\(L\) is odd, the step-two projection is one cycle and they are two
consecutive-parity edges of that cycle. In either case the operation
preserves the common PBBS history: it cuts both projected rows at the same
underlying boundary.

For a short gap (2.5), let circular integer intervals be read in the
orientation from \(i\) through \(j\). Directly from (2.6)--(2.7),

\[
\begin{aligned}
 \{t:\mathcal C_t\cap I^+_{i,j}\ne\varnothing\}
    &=[i-1,j+1],\\
 \{t:\mathcal C_t\cap I^0_{i,j}\ne\varnothing\}
    &=[i,j].
\end{aligned}
\tag{3.2}
\]

Indeed, an edge \(E_k\) belongs to exactly the two atoms
\(\mathcal C_{k-1}\) and \(\mathcal C_k\). Taking those two site indices
for the alternating lists in (2.6)--(2.7) fills the displayed intervals
without gaps. In particular,

\[
 [i,j]\subset[i-1,j+1].
\tag{3.3}
\]

Every atom which hits the zero defect therefore hits the positive defect
as well.

Now let \(\Gamma\) be any already linear subforest obtained by retaining
projected PBBS transition edges. A boundary interval is called
**internal** if all its old edges survive consecutively in one directed
component of \(\Gamma\). For every gap satisfying (2.8), define its
residual row-coherent demand interval by

\[
 K_{i,j}(\Gamma)=
 \begin{cases}
 [i,j],&I^0_{i,j}\text{ is internal};\\
 [i-1,j+1],&I^0_{i,j}\text{ is not internal but }
                I^+_{i,j}\text{ is internal};\\
 \varnothing,&\text{neither interval is internal}.
 \end{cases}
\tag{3.4}
\]

The first line also covers the case in which both intervals are internal:
a site in \([i,j]\) hits both.

### Lemma 3.1 -- exact paired feasibility

A set \(T\) of row-coherent atom sites destroys every internally bounded
short positive and zero run inherited from \(\Gamma\) if and only if

\[
 T\cap K_{i,j}(\Gamma)\ne\varnothing
\tag{3.5}
\]

for every nonempty demand interval in (3.4).

#### Proof

If the zero interval is internal, it must be hit. By the second identity
in (3.2), this is equivalent to choosing a site in \([i,j]\), and (3.3)
then hits the positive interval too if it is internal. If only the
positive interval is internal, the first identity in (3.2) gives the
second line of (3.4). If neither is internal, the old forest has already
split both bad runs. These cases are exhaustive. \(\square\)

Deleting old edges only splits components, so it cannot create a new
internally bounded run. Lemma 3.1 is therefore both the local necessity
and the global sufficiency statement for cut-only row-coherent repair.

## 4. Circular interval transversals with exact constants

Let \(\mathcal K\) be a nonempty family of proper circular intervals on one
atom-site circle. Write \(\tau(\mathcal K)\) for its minimum transversal
number and \(\nu(\mathcal K)\) for its maximum number of pairwise disjoint
members. For a site \(e\), let \(\mathcal K_e\) be the intervals not
containing \(e\), opened onto the line at \(e\).

### Lemma 4.1 -- exact circular formula

\[
 \boxed{
 \tau(\mathcal K)=1+\min_e\nu(\mathcal K_e),
 \qquad
 \nu(\mathcal K)\le\tau(\mathcal K)
       \le\nu(\mathcal K)+1.}
\tag{4.1}
\]

#### Proof

On a line, the greedy rule which repeatedly chooses the right endpoint of
the interval with leftmost right endpoint gives both a transversal and a
pairwise disjoint packing of the same size. Hence line intervals satisfy
\(\tau=\nu\).

For any circular site \(e\), choose \(e\), open the remaining intervals at
that site, and apply the line theorem. This gives

\[
 \tau(\mathcal K)\le1+\nu(\mathcal K_e).
\]

Conversely, if \(T\) is a minimum circular transversal and \(e\in T\),
then \(T\setminus\{e\}\) hits \(\mathcal K_e\), so

\[
 |T|-1\ge\nu(\mathcal K_e)
          \ge\min_f\nu(\mathcal K_f).
\]

This proves the equality. Choosing \(e\) in any member of a maximum
packing gives the upper sandwich; the lower sandwich is true for every
set system. \(\square\)

For fixed \(A\) and \(H\le A\sqrt m\), all intervals in (3.4) are proper
for sufficiently large \(m\), because a PBBS component has length at least
\(2m-1\), whereas their lengths are at most \(2H+2\).

Take the disjoint union of all underlying PBBS atom-site circles used by
\(\Gamma\). Let

\[
 \widehat\tau_H(\Gamma)
   =\sum_C\tau(\mathcal K_H(C;\Gamma)),
 \qquad
 \widehat\nu_H(\Gamma)
   =\sum_C\nu(\mathcal K_H(C;\Gamma)),
\tag{4.2}
\]

where an empty family contributes zero. Each active circle has
\(\nu\ge1\). Summing (4.1) therefore gives

\[
 \boxed{
 \widehat\nu_H(\Gamma)
 \le\widehat\tau_H(\Gamma)
 \le2\widehat\nu_H(\Gamma).}
\tag{4.3}
\]

The construction is explicit: on each active circle choose a site \(e\)
minimizing the line packing number, select \(e\), and then greedily select
right endpoints in the opened family.

There is a useful comparison with the previously isolated positive-return
packing number. Let \(\nu_H^+\) be the maximum number of pairwise
edge-disjoint positive intervals (2.6) in the **full original PBBS
family**, whether or not those intervals remain internal after the
preliminary forest cuts, over the same disjoint union of PBBS components.
Then

\[
 \boxed{\widehat\nu_H\le3\nu_H^+.}
\tag{4.4}
\]

To prove this, take a pairwise disjoint family of \(k\) demand intervals.
Associate to each its full positive interval \(I^+\). A demand of type
\([i-1,j+1]\) contains all edge indices of \(I^+\). A demand of type
\([i,j]\) contains all of them except possibly its final edge \(E_{j+1}\).
Therefore the intersection graph of the associated positive intervals has
maximum degree at most two: an interval can meet only the immediately
preceding or following demand, through such an exposed final edge. Every
graph of maximum degree two has an independent set of size at least
\(k/3\). Those independent positive intervals are edge-disjoint, proving
(4.4). The factor three allows an odd circular triangle and is the sharp
conclusion of this abstract comparison. For example, on a twelve-site
circle the disjoint site arcs

\[
 [0,3],\quad[4,7],\quad[8,11]
\]

may have associated positive edge sets

\[
 \{0,2,4\},\quad\{4,6,8\},\quad\{8,10,0\},
\]

whose intersection graph is a triangle.

If one begins with the uncut cyclic transition factor rather than an
already linear forest, at least one atom is additionally required on every
underlying PBBS component. The exact site number on component \(C\) is

\[
 \widehat\kappa_H(C)
   =\max\{1,\tau(\mathcal K_H(C))\}.
\tag{4.5}
\]

One atom cuts both parity cycles when \(L\) is even and cuts the unique
step-two cycle when \(L\) is odd. The number of local PBBS components is
at most

\[
 {1\over2m-1}{2m-1\choose m-1}
 =\operatorname {Cat}_{m-1}
 ={m+1\over2(2m-1)}B.
\tag{4.6}
\]

Here every PBBS component length is a positive multiple of \(2m-1\),
which gives the first inequality.

Thus the compulsory cyclic linearization term is itself Catalan for one
complete local factor. For the already linear first-avoided-pair forest,
it has already been paid and (4.2)--(4.3) are the relevant additional
ledger.

## 5. The sharp sufficient row-coherent splice theorem

### Theorem 5.1

Let \(\Gamma\) be an already linear subforest of a collection of projected
PBBS transition factors. Delete from \(\Gamma\) every retained edge lying
in \(\mathcal C_t\) for the atom sites \(t\) produced by the minimum
transversals of Section 4. If \(c\) is the number of distinct retained
edges deleted, then

\[
 \boxed{
 c\le2\widehat\tau_H(\Gamma)
   \le4\widehat\nu_H(\Gamma).}
\tag{5.1}
\]

Every resulting path is a genuine endpoint-recanonicalized canonical
signed natural-departure radius-\(H\) rotor path.

All retained interiors lie in their original exact PBBS transition factor
with their original cyclic history. The construction uses no averaging
between factors; its only changes are the paired old-edge deletions and
literal endpoint recanonicalizations.

Moreover, \(\widehat\tau_H(\Gamma)\) is the exact minimum number of
row-coherent atom sites in any cut-only repair of this type. If
\(c_{\min}\) is the minimum number of distinct old edges deleted by such a
repair, then

\[
 \boxed{
 \widehat\nu_H(\Gamma)\le c_{\min}
 \le2\widehat\tau_H(\Gamma)
 \le4\widehat\nu_H(\Gamma).}
\tag{5.2}
\]

#### Proof

Each atom contains at most two retained old edges, giving the first
inequality in (5.1); (4.3) gives the second. Lemma 3.1 says that every
internally bounded positive run of length at most \(H\) and every
internally bounded zero run of length at most \(H-1\) has been split.
No new one is created by deletion. Conditions (1.2)--(1.3) now hold on
each component, and the endpoint construction following (1.5) gives the
literal rotor lift.

Conversely, every cut-only row-coherent repair must hit the atom-site
demand interval of every surviving short run by Lemma 3.1. Its site set
is therefore a transversal, and has size at least
\(\widehat\tau_H(\Gamma)\).

For the edge lower bound, take a maximum pairwise disjoint family of
demand intervals. For a demand of type \([i,j]\), use its intact zero
boundary interval \(I^0_{i,j}\), all of whose edge indices lie in
\([i,j]\). For a demand of type \([i-1,j+1]\), use its intact positive
boundary interval \(I^+_{i,j}\), all of whose indices lie in that demand.
The resulting witness edge intervals are pairwise disjoint and all must be
hit. Hence at least \(\widehat\nu_H\) distinct old edges are deleted.
This proves (5.2). \(\square\)

For line intervals the greedy min--max theorem gives

\[
 c\le2\widehat\nu_H.
\tag{5.3}
\]

The circular \(+1\) in (4.1) is real in general, so (5.1) is the sharp
uniform conclusion without more PBBS structure.

### Corollary 5.2 -- the exact Catalan sufficient condition

Fix \(A,K>0\). If, for all sufficiently large \(m\) and every
\(1\le H\le A\sqrt m\),

\[
 \widehat\nu_H(\Gamma)\le KB,
\tag{5.4}
\]

then deleting at most \(4KB\) retained edges gives a signed radius-\(H\)
rotor path forest. Since

\[
 {4KB\over W/H}={4KH\over2m+1}=O_{A,K}(m^{-1/2}),
\tag{5.5}
\]

this is \(o(W/H)\).

This is the promised sharp sufficient splice theorem. Its hypothesis is
a packing bound, not a count of all short returns. Arbitrarily many short
returns are allowed if they cluster through Catalan-many atom sites.
By (4.4), the earlier positive PBBS Catalan packing conjecture
\(\nu_H^+=O(B)\) is a sufficient hypothesis, with no independent
two-sided packing conjecture. In one local pair-omission factor,

\[
 {1\over m}{2m-1\choose m-1}
 ={m+1\over2m}B,
\]

so the previously formulated bound \(O(A_m/m)\) is exactly an \(O(B)\)
bound at this scale.

## 6. Exact seam test and the no-bypass theorem

Cut-only repair already proves Theorem 5.1. If fragments are to be joined
again, q1 adjacency by itself is insufficient. The following exact test
records the additional chronology.

Let the left transitions be indexed \(-u,\ldots,-1\), let a proposed seam
be

\[
 e_0:\ X\longrightarrow Y=X-\{\beta\}+\{\alpha\},
\tag{6.1}
\]

and index right transitions \(1,\ldots,v\). Write their removal and
insertion labels as \(r_k,a_k\). Assuming each arm is internally safe, the
concatenation is safe if and only if all of the following hold:

\[
 a_{-d}\notin
 \{\beta,r_1,\ldots,r_{\min(v,H-d)}\}
 \quad(1\le d\le\min(u,H)),
\tag{6.2}
\]

\[
 \alpha\notin\{r_1,\ldots,r_{\min(v,H)}\},
\tag{6.3}
\]

\[
 r_{-d}\notin
 \{\alpha,a_1,\ldots,a_{\min(v,H-1-d)}\}
 \quad(1\le d\le\min(u,H-1)),
\tag{6.4}
\]

and

\[
 \beta\notin\{a_1,\ldots,a_{\min(v,H-1)}\}.
\tag{6.5}
\]

These are simply every cross-seam instance of (1.2)--(1.3). If both arms
have at least \(H\) transitions, the exact numbers of ordered comparisons
are

\[
 N_+={H(H+3)\over2},\qquad
 N_0={(H-1)(H+2)\over2},
\tag{6.6}
\]

and hence

\[
 \boxed{N_++N_0=H^2+2H-1.}
\tag{6.7}
\]

This counts comparisons, not necessarily distinct forbidden values.
When two seams lie within \(H\) transitions, testing them independently is
not sufficient: a forbidden pair can cross both. The exact associative
composition state consists of the first and last \(H\) oriented
transition labels, the length truncated at \(H\), and a safety bit. At
each concatenation one tests every cross pair in (1.2)--(1.3).

There is also an exact no-bypass statement in the canonical
natural-departure class. Let \(\kappa_H^\pm(G)\) be the minimum number of
old edges which meet every short positive and zero boundary interval of an
old path/cycle collection \(G\), and which meet every old cycle at least
once. Then

\[
 \boxed{
 \min_{R}|E(G)\triangle E(R)|=\kappa_H^\pm(G),}
\tag{6.8}
\]

where \(R\) ranges over splices formed by deleting old edges, arbitrarily
permuting or reversing the retained fragments, adding arbitrary Johnson
seams, requiring the output to be a path forest, and requiring every
output path to satisfy (1.2)--(1.3).

For the lower bound, if a short interval contains no deleted old edge, all
of it remains consecutive in one retained fragment. Reversal preserves
its run type and length, so the final path is not safe. Every retained old
cycle must also be cut. For the upper bound, delete a minimum transversal
and add no seams. This proves (6.8). On an old path the contribution is
the line interval transversal number; on an old cycle it is
\(\max\{1,\tau\}\).

Equation (6.8) must not be extended to arbitrary priority-prefix or
endogenous-upper rotors. Such paths can bypass a residence defect by
paying portal letters. A universal lower bound there would require a new
weighted cut-versus-portal theorem.

## 7. Colour, component, and literal reset ledgers

Assume that \(\Gamma\) initially has injective lower and upper edge-colour
maps

\[
 c^-(XY)=X\cap Y,
 \qquad
 c^+(XY)=X\cup Y,
\tag{7.1}
\]

and initially misses \(\delta_-\) and \(\delta_+\) targets. Deleting \(c\)
old edges and adding no seams gives the exact ledger

\[
 \boxed{
 \delta_-^{\rm new}=\delta_-+c,
 \qquad
 \delta_+^{\rm new}=\delta_++c,}
\tag{7.2}
\]

with no duplicate colours. If \(s\) seams are added and \(u_\pm\) denotes
the number of distinct seam colours not already present in the retained
ledger, then more generally

\[
 \boxed{
 M_\pm^{\rm new}=\delta_\pm+c-u_\pm,
 \qquad
 O_\pm^{\rm new}=s-u_\pm.}
\tag{7.3}
\]

Here \(M\) is missing support and \(O\) is duplicate excess. Formula
(7.3) follows just by comparing the number of distinct new colours with
the number of new edges; no asymptotics or divisibility is hidden.

If the initial forest has \(p\) path components, deleting \(c\) distinct
old edges and adding no seams gives exactly

\[
 J=p+c
\tag{7.4}
\]

components. If \(s\) acyclic seams are added between distinct ports, then

\[
 J=p+c-s.
\tag{7.5}
\]

For a retained owner set \(U\), the exact independently recanonicalized
literal signed length is

\[
 \boxed{|U|+2HJ.}
\tag{7.6}
\]

Apply this to the proved two-sided PBBS \(q=1\) forest. It has

\[
 p=O(W\log^2m/m)=o(W/H),
 \qquad
 \delta_\pm=o(W/H)
\tag{7.7}
\]

uniformly for (0.6). Under (5.4), Theorem 5.1 gives \(c\le4KB\), so

\[
 J=p+c=o(W/H),
 \qquad
 \delta_\pm^{\rm new}=o(W/H).
\tag{7.8}
\]

Finally,

\[
 {H B\over W}={H\over2m+1}=O_A(m^{-1/2}),
\tag{7.9}
\]

and

\[
 {Hp\over W}=O_A(\log^2m/\sqrt m)=o(1).
\tag{7.10}
\]

Thus (7.6) has additive \(o(W)\) reset cost. This proves all claimed
constants and shows why \(O(B)\) must count actual changed edges, not sites
which each rewrite \(O(H)\) edges.

The queue evolution (1.4) is the established literal rotor encoding: each
transition appends an actual set-letter, and the two endpoint completions
append \(2H\) actual letters. Concatenating these component lifts therefore
constructs an actual contiguous-OR word segment; no fractional averaging
or passage between exact factors is used.

This conclusion is a literal q1 physical-spine theorem conditional on
(5.4). It does not by itself prove higher-depth colour coverage or the
full contiguous-OR constant-one theorem.

## 8. A genuine PBBS component with linearly many short returns

The Catalan packing hypothesis cannot be proved component by component.
The following exact packet is a counterexample to that strategy.

Let \(n_0=2r+1\), \(r\ge3\), and normalize an odd-graph state by placing its
unique unmatched zero first. The remaining \(2r\) bits form a Dyck word
\(D\). If the first up-step reaching the global maximum splits

\[
 D=P\,1\,Q,
\]

then one PBBS step has the skew-product form

\[
 (u,D)\longmapsto
 (u+|P|+1,\ \overline Q\,0\,\overline P),
\tag{8.1}
\]

with the first coordinate reduced modulo \(n_0\).

Put

\[
\begin{aligned}
 D_0&=11(01)^{r-2}00,\\
 D_1&=(10)^{r-2}1100,\\
 D_2&=110(01)^{r-2}0.
\end{aligned}
\tag{8.2}
\]

The first maximum-reaching positions are respectively

\[
 2,\qquad n_0-3,\qquad2,
\tag{8.3}
\]

and direct substitution in (8.1) gives

\[
 D_0\longmapsto D_1\longmapsto D_2\longmapsto D_0.
\tag{8.4}
\]

The three words are distinct for \(r\ge3\), so this quotient period is
exactly three.

The three-step voltage is

\[
 2+(n_0-3)+2=n_0+1\equiv1\pmod {n_0}.
\tag{8.5}
\]

Hence the skew-product lift is one PBBS component of exact length
\(3n_0\): every return time is a multiple \(3j\), and then the root has
advanced by \(j\), so the least positive solution is \(j=n_0\). At times
\(3k,3k+1,3k+2\), its omitted labels are

\[
 u+k,\qquad u+k+2,\qquad u+k-1
 \pmod {n_0}.
\tag{8.6}
\]

Because \(3n_0\) is odd, its step-two projection is one cycle.

Starts in phases zero and one have their next equal label exactly five
steps later. Starts in phase two have their next equal label after
\(3n_0-10\) steps. Thus every ground label has consecutive-gap multiset

\[
 \boxed{\{5,5,3n_0-10\}.}
\tag{8.7}
\]

For clarity, the phase-zero occurrence at time \(3k\) next appears in
phase two at time \(3(k+1)+2\), and the phase-one occurrence at time
\(3k+1\) next appears in phase zero at time \(3(k+2)\). Both gaps are
five, and the intermediate labels in (8.6) are different. For a phase-two
start \(3k+2\), the first future phase-one solution of
\(u+j+2=u+k-1\pmod {n_0}\) is \(j=k+n_0-3\), giving gap
\(3n_0-10\). The phase-zero and phase-two solutions occur later, at gaps
\(3n_0-5\) and \(3n_0\).

Each gap-five return has positive residence three. Its positive boundary
interval has four step-two edges. Let

\[
 J_0=\left\lfloor{3n_0-1\over9}\right\rfloor.
\]

For \(0\le k<J_0\), choose the two starts \(3+9k\) and \(4+9k\). Their
edge intervals are

\[
 \{3,5,7,9\}+9k,
 \qquad
 \{4,6,8,10\}+9k.
\tag{8.8}
\]

All \(2J_0\) intervals are pairwise disjoint and avoid the circular seam.
Indeed their largest displayed index is \(9J_0+1\), while
\(3n_0-1\bmod9\in\{2,5,8\}\), so \(9J_0+1\le3n_0-1\).
Consequently, for every \(H\ge3\),

\[
 \boxed{
 \nu_H^+\ge
 2\left\lfloor{3n_0-1\over9}\right\rfloor.}
\tag{8.9}
\]

Every canonical signed splice which retains old interiors must delete at
least that many old projected edges on this component. A row-coherent
atom can hit at most two of these disjoint intervals, so it needs at least
\(J_0\) sites.

This is \(\Theta(n_0)\) on one quotient-level-three component. It rules out
an \(O(1)\)-per-component estimate and any argument charging each packed
return to a bounded number of quotient states of its own component. It
does **not** refute the global Catalan bound: this exceptional component has
only \(3n_0\) states, whereas the full local PBBS factor has exponentially
larger Catalan mass.

## 9. Exact failure of the primitive-height obstruction

A tempting attempt to turn Section 8 into a global counterexample is the
claim that a primitive Dyck word of height \(h\) returns its unmatched
coordinate after \(2h+1\) PBBS steps. That claim is false.

Take \(r=6\), \(n_0=13\), and

\[
 D_0=111001011000.
\tag{9.1}
\]

It is primitive and has height three. Repeated exact application of
(8.1) gives the following quotient words and first-maximum increments:

\[
\begin{array}{c|c}
111001011000&3\\
110100111000&9\\
111000101100&3\\
111010011000&3\\
101100111000&9\\
111001001100&3\\
110110011000&5.
\end{array}
\tag{9.2}
\]

For example, the first word splits after its third bit, so

\[
 \overline{001011000}\,0\,\overline{11}
 =110100111000,
\]

and the other rows follow identically from the displayed first maximum.
The first seven increments sum to

\[
 3+9+3+3+9+3+5=35\not\equiv0\pmod {13}.
\tag{9.3}
\]

Their successive partial sums modulo \(13\) are
\(3,12,2,5,1,4,9\), so none is an earlier return either.

Thus the unmatched coordinate does not return after
\(2h+1=7\) steps. The associated proposed universal
\((2h-1)\)-step spine rotation is false as well: the fifth quotient word in
(9.2) is not the first. The failure mechanism is that, after rotation, a
side forest can attain the new global maximum and replace the previously
distinguished spine.

Therefore Catalan height enumeration proves neither
\(\widehat\nu_H=O(B)\) nor \(\widehat\nu_H=\Omega(W/H)\). The remaining
problem is a genuinely global enumeration of PBBS return congruences.

## 10. Final proved/conditional boundary

The following statements are unconditional.

1. Every short PBBS label return produces the synchronized signed packet
   of Lemma 2.1.
2. Paired row-coherent atom feasibility is exactly the interval
   transversal problem of Lemma 3.1.
3. A forest with residual packing number \(\widehat\nu_H\) can be repaired
   by deleting at most \(4\widehat\nu_H\) actual old edges, with all
   colour, component, and reset constants in Sections 5 and 7.
4. The seam tests (6.2)--(6.5) and the canonical natural-departure
   no-bypass theorem (6.8) are exact.
5. The component packet in Section 8 and the primitive-height
   counterexample in Section 9 are exact.

The sole PBBS-specific hypothesis still needed for the requested
\(O(\operatorname {Cat}_m)\)-edge **canonical zero-portal
row-coherent cut construction** is

\[
 \boxed{
 \widehat\nu_H=O(\operatorname {Cat}_m)
 \quad\text{uniformly for }H\le A\sqrt m.}
\tag{10.1}
\]

Under (10.1), the desired row-coherent genuine radius-\(H\) rotor-path
forest, two-sided \(q=1\) colour preservation, \(o(W/H)\) component count,
and \(o(W)\) literal reset cost all follow integrally. No proof or
counterexample to the aggregate bound (10.1) is presently obtained.
This does not exclude a different priority-prefix construction which pays
portal letters instead of cutting all short runs, nor does it construct a
nontrivial seam-joining of the cut fragments.

The synchronized-gap indexing, \(K^0/K^+\) atom arcs, circular constants,
factor-three comparison, signed seam tests, colour/reset ledgers,
level-three packet, and primitive-height counterexample were independently
audited after the final scope corrections.
