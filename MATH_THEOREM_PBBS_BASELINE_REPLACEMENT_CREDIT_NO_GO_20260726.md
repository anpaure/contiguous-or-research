# PBBS clustered seams: exact erosion reuse, its critical no-go, and the minimal richer replacement

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Put

\[
 H=\lceil A\sqrt m\rceil,\qquad B=\operatorname {Cat}_m,
\]

with \(A>0\) fixed. Work on the quotient owner cycles. For a cut cluster
\(J\), write

\[
 c_J^-=\min J,\qquad c_J^+=\max J,\qquad
 S_J=c_J^+-c_J^-,
\tag{0.1}
\]

and recall the established endpoint-and-seam charge

\[
 \Phi_J=7H+3S_J-3.
\tag{0.2}
\]

There is an exact in-place credit inside the already proved compiler. Let

\[
 V_J=\bigcup_{c\in J}\{c,c+1,\ldots,c+H-1\}
\tag{0.3}
\]

be its virtual-cut set, and define the protected erosion interior

\[
 \boxed{
 K_J=\left\{i\in[c_J^-,c_J^+-1]:
       \{i+1,\ldots,i+H\}\subseteq V_J\right\}.}
\tag{0.4}
\]

Every nonnegative endpoint-capped erosion letter indexed by \(K_J\) may
be deleted from the base word. The original dominance chart and owner
halo then restore every lower and upper target whose canonical erosion
witness was altered, including every singleton owner. Thus, with

\[
 R_{\rm er}=\left|\bigcup_JK_J\right|,
\tag{0.5}
\]

the proved compiler has the sharpened quotient ledger

\[
 \boxed{L_H\le B+2HC_0+\sum_J\Phi_J-R_{\rm er},}
\tag{0.6}
\]

where \(C_0\) is the number of inactive quotient cycles charged a cyclic
collar. However,

\[
 \boxed{R_{\rm er}\le\sum_JS_J.}
\tag{0.7}
\]

The bound in (0.7) is attained by the protected set when the virtual-cut
sets are intervals. It is far below the credit needed at critical
packing. For every projected-edge-disjoint packing \(\mathcal P\),

\[
 \boxed{
 \sum_J\Phi_J-R_{\rm er}
 \ge \sum_{I\in\mathcal P}|E(I)|.}
\tag{0.8}
\]

Consequently critical residence saturation gives

\[
 \boxed{\sum_J\Phi_J-R_{\rm er}=\Omega_A(B).}
\tag{0.9}
\]

So the established cluster chart cannot acquire the required
\(R\ge\Phi-o_A(B)\) merely by erasing the baseline letters whose old
witness jobs it visibly assumes.

There is a stronger in-place local substitution. The whole Johnson collar
of a cluster has a \(2M+1\)-letter dominance word, where

\[
 M=S_J+2H-1.
\]

It preserves every singleton owner and every floor-correct lower and upper
window wholly inside the collar. Against its \(M+1\) literal owner
baseline, its exact excess is only

\[
 \Psi_J=S_J+2H-1.
\tag{0.10}
\]

Even granting cost-free splicing at the two outer collar boundaries, the
critical fixed-core packing forces

\[
 \boxed{\sum_J\Psi_J=\Omega_A(B).}
\tag{0.11}
\]

Thus neither canonical erosion deletion nor independent whole-collar
replacement closes the critical branch.

This is not a universal impossibility theorem for in-place words. A
sliding-core Johnson cycle with critical tiled residences has a word of
length \(B+O(H)\). The minimal richer replacement is therefore a
nonlocal rank-monotone braid: it must rethread positions across many
clusters, reuse baseline endpoints for almost all fixed-rank targets, keep
the shared endpoints nested across depths, retain right-endpoint witnesses
for all upper targets, and preserve every middle singleton owner. Such a
PBBS-specific braid is not proved here.

## 1. The base word and the two auxiliary blocks

Open an active owner cycle at the selected cuts. On each resulting path,
extend the owner sequence constantly at both endpoints and retain only the
nonnegative endpoint-capped erosion letters

\[
 D_i=\bigcap_{h=0}^{H}\widetilde X_{i+h},
 \qquad 0\le i\le v-1.
\tag{1.1}
\]

Indices below are written in the original cycle coordinates; at a path
endpoint (1.1) still means the corresponding constant-capped letter. The
base contribution over all paths is exactly the original owner mass.

For a cluster \(J\), the established lower block is the global dominance
staircase for the virtual cuts \(V_J\). It covers every floor-correct
non-singleton lower owner window crossing a member of \(V_J\). The
established upper block is the chronological owner halo

\[
 \mathcal H_J=
 (X_{c_J^- -H},X_{c_J^- -H+1},\ldots,
  X_{c_J^+ +2H-1}).
\tag{1.2}
\]

It covers every upper window contained in that owner interval and every
singleton owner in it. The lower staircase and (1.2) have total length
\(7H+3S_J-3\), under the usual admissibility hypothesis

\[
 3H+S_J\le m+1.
\tag{1.3}
\]

For an internal owner window \([a,b]\) of at most \(H+1\) owners, the
exact endpoint-capped erosion identities give the canonical witnesses

\[
 \bigcap_{t=a}^{b}X_t
   =\bigcup_{i=b-H}^{a}D_i,
\tag{1.4}
\]

and

\[
 \bigcup_{t=a}^{b}X_t
   =\bigcup_{i=a-H}^{b}D_i.
\tag{1.5}
\]

The formulas are used only on one cut path. Targets crossing a path cut,
and targets formerly using a negative erosion index, already belong to the
cluster repair ledger.

## 2. Exact protected-interior deletion theorem

### Theorem 2.1 (certified erosion reuse)

Let the active cuts be partitioned into admissible clusters. Form \(K_J\)
by (0.4), delete from the base word every letter with index in

\[
 K=\bigcup_JK_J,
\tag{2.1}
\]

and keep all the already constructed cluster dominance staircases and
owner halos. Then every intended floor-correct lower target and every
intended upper target through depth \(H\) still has a literal contiguous
witness. In particular every middle singleton owner still has a witness.
The resulting length is (0.6), with \(R_{\rm er}=|K|\).

#### Proof

Any old base witness whose index interval is disjoint from \(K\) remains
a contiguous subword after the deletion. It remains to reroute a canonical
witness which contains some \(i\in K_J\).

First consider a lower window \([a,b]\). By (1.4),

\[
 i\in[b-H,a],
 \qquad\text{hence}\qquad
 i\le a\le b\le i+H.
\tag{2.2}
\]

If \(a<b\), the window crosses the cut between \(X_a\) and \(X_{a+1}\).
Moreover

\[
 a+1\in\{i+1,\ldots,i+H\}\subseteq V_J.
\tag{2.3}
\]

The cluster dominance staircase therefore supplies the lower witness. If
\(a=b\), the target is the singleton owner \(X_a\). Equations (2.2) and
\(c_J^-\le i\le c_J^+-1\) give

\[
 c_J^-\le a\le c_J^++H-1,
\]

so \(X_a\) occurs literally in the halo (1.2).

Now consider an upper window \([a,b]\). From (1.5),

\[
 i\in[a-H,b].
\tag{2.4}
\]

Since \(b-a\le H\), this implies

\[
 i-H\le a\le i+H,
 \qquad
 i\le b\le i+2H.
\tag{2.5}
\]

Using \(c_J^-\le i\le c_J^+-1\), we obtain

\[
 c_J^- -H\le a\le b\le c_J^++2H-1.
\tag{2.6}
\]

Thus the original owner interval \(X_a,\ldots,X_b\) is a literal subword
of (1.2), and its OR is the required upper target.

All targets whose witnesses were altered have now been rerouted. The old
cross-cut and omitted-prefix targets were already assigned to the same two
auxiliary blocks. No emitted letter was changed, so their established
nonemptiness is unaffected. This proves the theorem. \(\square\)

### Corollary 2.2 (exact size of the visible credit)

For every cluster,

\[
 |K_J|\le S_J,
\tag{2.7}
\]

and hence (0.7) holds. If \(V_J\) contains the full interval

\[
 [c_J^-,c_J^++H-1],
\tag{2.8}
\]

then

\[
 K_J=[c_J^-,c_J^+-1],
 \qquad |K_J|=S_J.
\tag{2.9}
\]

#### Proof

The interval in (0.4) has exactly \(S_J\) integer points. Under (2.8),
every one of those points satisfies the \(H\)-step protection condition.
\(\square\)

Thus the bound is not losing a hidden factor \(H\). Dense virtual cuts
make every erosion index between the two extreme cuts reusable, but no
more than that is certified by the unchanged halo boundaries.

## 3. Packed trace mass survives the erosion credit

Let \(\mathcal P\) be a family of short residence intervals with pairwise
disjoint quotient edge supports. Choose one transversal cut from each
interval and assign the interval to the cluster containing that cut. The
interval-order lemma gives, cluster by cluster,

\[
 \sum_{I\mapsto J}|E(I)|
 \le S_J+2(H+1).
\tag{3.1}
\]

### Theorem 3.1 (critical no-go for the established in-place deletion)

For \(H\ge2\), every cut transversal, every admissible clustering, and the
credit of Theorem 2.1 satisfy

\[
 \boxed{
 \sum_J\Phi_J-R_{\rm er}
 \ge\sum_{I\in\mathcal P}|E(I)|.}
\tag{3.2}
\]

Consequently

\[
 \sum_J\Phi_J-R_{\rm er}\ge\Lambda_{m,H},
\tag{3.3}
\]

where \(\Lambda_{m,H}\) is the maximum packed trace mass.

#### Proof

By Corollary 2.2,

\[
 \sum_J\Phi_J-R_{\rm er}
 \ge\sum_J(7H+2S_J-3).
\tag{3.4}
\]

For every cluster,

\[
 S_J+2(H+1)
 \le 7H+2S_J-3,
\tag{3.5}
\]

because the difference is \(5H+S_J-5\ge0\). Combine (3.1) and
(3.5), then sum over the clusters. Maximizing over \(\mathcal P\) proves
(3.3). \(\square\)

The critical double-deck saturation theorem supplies, on failure of
\((\mathrm{ST}_A)\), a fixed-core packing with

\[
 \sum_{I\in\mathcal P}|E(I)|\ge c_A B.
\tag{3.6}
\]

Equations (3.2)--(3.6) prove (0.9). In particular the necessary credit

\[
 R\ge\sum_J\Phi_J-o_A(B)
\tag{3.7}
\]

cannot be the protected erosion credit \(R_{\rm er}\).

## 4. Literal coincidence has the same obstruction

The preceding result concerns deletion with complete witness provenance,
not merely equality of letters. There is also a ceiling on what literal
coincidence alone can prove from abstract Johnson geometry.

For the lower endpoint chart of \(J\), the virtual-cut span is at most

\[
 T_J=S_J+H-1.
\]

Its southeast path has side length

\[
 L_J=H+T_J-1=2H+S_J-2.
\tag{4.1}
\]

A genuine interior erosion letter \(D_i\) is the endpoint-plane letter at

\[
 z_i=(-i,i+H),
 \qquad z_{i,1}+z_{i,2}=H.
\tag{4.2}
\]

### Proposition 4.1 (diagonal coincidence ceiling)

There are floor-rigid Johnson collars, satisfying all rank and adjacency
hypotheses of the cluster theorem, for which a lower chart letter equals a
base erosion letter only at a path vertex on the diagonal (4.2), and no
owner-halo letter equals an erosion letter. On every southeast unit path,
the number of such diagonal vertices is at most

\[
 \boxed{L_J+1=2H+S_J-1.}
\tag{4.3}
\]

Hence no theorem using only abstract Johnson adjacency, floor correctness,
and literal equality can guarantee coincidence credit larger than
\(2H+S_J-1\) for this cluster, even before the placement of all old
witness intervals is checked.

#### Proof

Use a monotone collar in which every transition removes a fresh initial
coordinate and inserts a fresh coordinate which is not removed in the
collar. Every consecutive intersection then has its floor cardinality,
and distinct endpoint intervals give distinct set letters. A chart letter
indexed by \(z=(\alpha,\beta)\) is the intersection of
\(\alpha+\beta+1\) owners and has rank
\(m+1-(\alpha+\beta)\). It can equal an \((H+1)\)-fold erosion letter
only when \(\alpha+\beta=H\), and distinct endpoint intervals then force
the same erosion index. Halo letters have rank \(m+1\), while erosion
letters have rank \(m+1-H\), so they cannot coincide.

Along a southeast unit path, an east step raises
\(\alpha+\beta-H\) by one and a south step lowers it by one. Between two
successive visits to zero there are at least two steps. The path has
\(2L_J\) steps, so it has at most \(L_J+1\) zero visits. \(\square\)

This proposition is a limitation of the local data, not a claim about the
actual PBBS collar. A PBBS-specific equality can do better only by using
additional recurrence or factor structure; that is precisely the new
phenomenon which would have to be proved.

## 5. The strongest proved local owner-collar substitution still costs trace mass

There is a more aggressive replacement than deleting selected erosion
letters. Consider the full owner collar

\[
 \mathcal C_J=[c_J^- -H,c_J^++H-1].
\tag{5.1}
\]

It has

\[
 M_J+1=S_J+2H
 \quad\text{owners},\qquad
 M_J=S_J+2H-1
 \quad\text{transitions}.
\tag{5.2}
\]

The admissibility inequality (1.3) gives
\(M_J=S_J+2H-1\le m-H\le m\), exactly the rank hypothesis needed by the
global Johnson-block staircase.

The global Johnson-block staircase gives one word of length

\[
 2M_J+1=2S_J+4H-1
\tag{5.3}
\]

which represents every singleton owner, every upper owner window, and
every floor-correct lower owner window wholly inside (5.1). Relative to
the \(M_J+1\) literal owner positions, this is an exact local excess

\[
 \boxed{\Psi_J=M_J=S_J+2H-1.}
\tag{5.4}
\]

Equivalently, compared with the old additive charge, this substitution
earns the formal credit

\[
 R_J^{\rm collar}=\Phi_J-\Psi_J=5H+2S_J-2.
\tag{5.5}
\]

This is a standalone collar theorem. It does not itself preserve windows
crossing the two outer boundaries of (5.1), and the erosion baseline is
not literally an owner baseline. The next theorem deliberately grants
both splice issues for free; even that optimistic ledger remains critical.

### Theorem 5.1 (critical obstruction to independent collar replacement)

Suppose the critical fixed-core family \(\mathcal Q\) has pairwise
disjoint edge supports and

\[
 a\sqrt m\le |E(I)|\le H+1,
 \qquad
 \sum_{I\in\mathcal Q}|E(I)|\ge cB.
\tag{5.6}
\]

For every cut transversal and clustering,

\[
 \boxed{\sum_J\Psi_J\ge cB-o_A(B).}
\tag{5.7}
\]

#### Proof

Assign each \(I\in\mathcal Q\) to a cluster containing a chosen
transversal cut. If \(\mathcal J_*\) is the set of clusters receiving an
assignment, (3.1) and (5.4) give

\[
 \sum_{I\mapsto J}|E(I)|
 \le S_J+2H+2=\Psi_J+3.
\tag{5.8}
\]

The supports are disjoint and each has length at least \(a\sqrt m\), so

\[
 |\mathcal J_*|\le|\mathcal Q|
 \le {B\over a\sqrt m}=o(B).
\tag{5.9}
\]

Summing (5.8) over receiving clusters yields

\[
 \sum_J\Psi_J
 \ge cB-3|\mathcal J_*|=cB-o_A(B).
\]

\(\square\)

Thus the best currently proved whole-collar replacement still leaves
positive-density net excess. It improves constants dramatically, and it
preserves the middle singleton owners inside each collar, but it remains
an independent-cluster construction whose cost sees packed trace mass.

## 6. Why this is not a universal no-go

The tiled sliding-core model shows that a stronger replacement can escape
every additive cluster ledger. Let

\[
 X_i=G\cup\{a_i,a_{i+1},\ldots,a_{i+H-1}\}
\tag{6.1}
\]

on a cyclic index set, with all \(a_i\) distinct and
\(|G|=m+1-H\). Its length-\(H\) positive runs force a critical tiled cut
pattern. Nevertheless, with

\[
 E_i=G\cup\{a_i\},
\tag{6.2}
\]

every lower and upper owner window through depth \(H\) is a contiguous
union of the \(E_i\)'s, after a \(2H-1\)-letter cyclic linearization
collar; the common depth-\(H\) intersection is the one extra letter \(G\).
The total length is

\[
 M+2H
\tag{6.3}
\]

for \(M\) cyclic baseline owners.

So packed trace mass rules out append-only seams and independent local
substitutions, but it does not rule out a wholesale rank-monotone
factorization. The new word in (6.2) abandons the old cluster boundaries
and lets one baseline start serve a nested family of ranks.

## 7. The minimal richer replacement theorem

The necessary endpoint reuse can be stated without PBBS assumptions.

### Theorem 7.1 (baseline-start necessity)

Let a nonzero literal word have length

\[
 L=M+e.
\]

Suppose it represents \(M\) distinct singleton owners of one rank and
\(D_q\) distinct targets at a fixed lower rank. After choosing one
witness for every represented set, at least

\[
 \boxed{D_q-e}
\tag{7.1}
\]

of the lower targets share their left endpoint with a distinct singleton
owner witness. At every shared endpoint the lower target is contained in
the owner.

For a set \(Q\) of lower depths, at least

\[
 \boxed{
 \left[L-\left(e+\sum_{q\in Q}(L-D_q)\right)\right]_+}
\tag{7.2}
\]

positions simultaneously begin an owner witness and one witness at every
depth in \(Q\); the corresponding sets form a nested rank-monotone flag.
The right-endpoint analogue holds for all upper target families.

#### Proof

Distinct equal-rank targets require distinct witness left endpoints:
intervals with one left endpoint are nested, their ORs are comparable, and
distinct equal-cardinality sets are incomparable. Thus the owner starts
form an \(M\)-subset of the \(L\) positions and the depth-\(q\) starts
form a \(D_q\)-subset. Their intersection has size at least

\[
 M+D_q-L=D_q-e,
\]

which proves (7.1). At a common start the witness intervals are nested,
so their ORs are nested in rank order. Applying the union bound to the
complements of all the start sets gives (7.2). Reversing the word proves
the right-endpoint statement. \(\square\)

Therefore a quotient word of length \(B+o(B)\) representing a
\(\Theta(B)\) distinct family at any fixed Gaussian depth must recycle
baseline starts for all but \(o(B)\) members of that family. The same is
true of right endpoints for the upper family. Appending a chart, deleting
the protected \(K_J\)'s, or substituting independent \(2M+1\) collars
does not create this global endpoint threading.

## 8. Exact remaining PBBS statement

The critical branch is reduced to the following genuinely richer object.

> **Nonlocal PBBS baseline braid — unproved.** Replace, on long blocks or
> complete quotient cycles, the entire endpoint-capped erosion chronology
> by one nonzero word of length
> \[
> B_{\rm block}+o_A(B_{\rm block})+O_A(H)
> \]
> such that:
>
> 1. every assigned middle singleton owner has a literal contiguous
>    witness, with exact ownership never mixed between incompatible
>    factors;
> 2. every intended floor-correct lower target through depth \(H\), both
>    internal and crossing every old cut, has a witness;
> 3. every intended upper target through depth \(H\) has a witness,
>    including those crossing the outer boundaries of any recoded
>    subblock;
> 4. at every fixed lower rank all but the little-oh excess of the target
>    witnesses reuse baseline left endpoints, and the analogous upper
>    witnesses reuse baseline right endpoints;
> 5. whenever endpoints are shared across depths, the corresponding target
>    sets occur in the required nested order; and
> 6. the construction may rethread across many cut clusters, so its net
>    charge is not a sum of positive span costs.

Theorem 7.1 makes clauses 4--5 necessary. The sliding-core construction
shows that such a mechanism exists in the abstract Johnson class. What is
missing is the PBBS-specific recurrence or exact-factor theorem that
constructs it while retaining clauses 1--3.

## 9. Logical boundary

The proved implications are

\[
 \boxed{
 \begin{array}{c}
 \text{established clustered compiler}\\
 +\ \text{the protected-interior deletions of Theorem 2.1}
 \end{array}
 \Longrightarrow
 \Delta\ge\Lambda_{m,H},}
\tag{9.1}
\]

and, in the critical fixed-core branch,

\[
 \boxed{
 \text{independent whole-collar substitution}
 \Longrightarrow
 \Delta=\Omega_A(B).}
\tag{9.2}
\]

Neither statement says coefficient one is false. They prove that the
missing credit cannot be obtained by relabelling the old additive cluster
ledger. The least richer replacement presently isolated is the nonlocal
baseline braid of Section 8, or an equally strong PBBS-specific theorem
producing positive-density cross-cluster witness coincidences together
with all singleton, lower, and upper provenance.
