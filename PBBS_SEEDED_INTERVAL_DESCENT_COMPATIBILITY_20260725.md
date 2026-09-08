# PBBS-seeded adjacent-interval descent: exact compatibility and its boundary

Date: 2026-07-25

Method: explicit mathematics only. No computation or literature search is
used.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W={n\choose m},\qquad
 A={2m-1\choose m-1}.
\]

There is a genuine compatibility theorem between the PBBS transition-factor
first-shadow seed and the adjacent-pair interval chart.  The theorem is
conditional only on making the PBBS projected cycles physically valid through
depth \(H\), i.e. on the already isolated PBBS short-residence cut estimate.
Under that hypothesis:

1. the PBBS phases may be chosen in one recursively conjugate family, without
   losing the \(O(W\log ^2m/m)\) category-component estimate;
2. every disjoint adjacent-pair interval layer is legal and physical;
3. every such corner keeps the exact lower first-shadow ledger and can only
   improve the PBBS upper first-shadow hole/collision ledger;
4. its component count remains \(o(W/H)\);
5. at depths \(q\ge2\), its exact factorial-floor descent is the number of
   activated equal-flag pairs lying in different physical packets.

The PBBS seed does **not** justify the stronger assertion

\[
 \mathcal C_{j,1}=0.
\]

That assertion is correct for the original tight cyclic-window interval
chart, but its proof uses more than exact middle ownership.  In a general
transition 2-factor, two consecutive transitions may have the same union and
share their middle state.  For PBBS the presently proved multiplicity theorem
does not exclude this.  Fortunately no zero-charge assertion is needed:
partial switching moves each load pair monotonically between two permuted
coherent endpoints, so every convex first-shadow defect is deterministically
nonincreasing.

Thus adjacent-interval descent introduces no new first-shadow or component
obstruction.  After physical PBBS residence is supplied, the remaining new
gate is a renewable charged-frame inequality for the depths \(q\ge2\).

## 1. Abstract transition-token hypotheses

Partition \(2m\) coordinates into ordered pairs

\[
 P_1,\ldots,P_m
\]

and leave one coordinate unpaired.  Put

\[
 Q_j=[n]\setminus P_j.
\]

On \(Q_j\), consider an oriented transition factor whose state cycles are
\(m\)-sets

\[
 \cdots,X_i,X_{i+1},\cdots
\]

and whose edge tokens are

\[
 S_i=X_i\cap X_{i+1},\qquad U_{i,1}=X_i\cup X_{i+1}.
\tag{1.1}
\]

We require the two exact properties supplied by the PBBS transition
dictionary:

* the states \(X_i\) run through every \(m\)-set of \(Q_j\) once;
* the lower labels \(S_i\) run through every \((m-1)\)-set of \(Q_j\)
  once.

After physical cuts, each retained edge token has flags

\[
 L_{i,q}=\bigcap_{h=0}^{q}X_{i+h},\qquad
 U_{i,q}=\bigcup_{h=0}^{q}X_{i+h}
\tag{1.2}
\]

of sizes \(m-q\) and \(m+q\), respectively, for \(q\le H\).  We call such a
piece an \(H\)-physical transition run.  Notice that

\[
 L_{i,q}\subseteq S_i.
\tag{1.3}
\]

Here an \(H\)-physical run includes its standard endpoint initialization
and terminal collar, of total cost \(O(H)\) per run, so the displayed
flags are available also at the ends of a run.  This formulation allows
repeated deeper flags inside one run.  No same-run simplicity is assumed.

## 2. One recursively conjugate PBBS family retains the low-component ledger

Let \(\mathcal D_1\) be one PBBS transition factor on \(Q_1\).  For
\(1\le j<m\), let \(\theta_j\) exchange \(P_j\) and \(P_{j+1}\)
coordinatewise, and define

\[
 \phi_1=1,\qquad
 \phi_j=\theta_{j-1}\cdots\theta_1,\qquad
 \mathcal D_j=\phi_j\mathcal D_1.
\tag{2.1}
\]

Then

\[
 \mathcal D_{j+1}=\theta_j\mathcal D_j.
\tag{2.2}
\]

The block permutation \(\phi_j\) sends \(P_1\) to \(P_j\) and sends
\(P_h\) to \(P_{h-1}\) for \(2\le h\le j\).  Consequently

\[
 \phi_j^{-1}(P_h)=P_{h+1}\quad(h<j),
 \qquad
 \phi_j^{-1}(P_{j+1})=P_{j+1}.
\tag{2.3}
\]

Let \(f(x)\) be the number of lower-label-cycle edges of \(\mathcal D_1\)
at which membership of coordinate \(x\) changes.  Since every such edge is
a Johnson edge,

\[
 \sum_{x\in Q_1}f(x)=2A.
\tag{2.4}
\]

Order the coordinates of \(Q_1\) by increasing \(f(x)\), and use them in
that order to form \(P_2,P_3,\ldots\).  Every prefix then satisfies

\[
 \sum_{x\in P_2\cup\cdots\cup P_{j+1}}f(x)
 \le {2j\over 2m-1}\,2A
 =O(jA/m).
\tag{2.5}
\]

In phase \(j\), the carrier used by the adjacent \(j,j+1\) swap is

\[
 \mathcal E_j=\left\{S:
 S\cap P_h\ne\varnothing\ (h<j),\quad
 S\cap(P_j\cup P_{j+1})=\varnothing\right\}.
\tag{2.6}
\]

By (2.3), its pullback to \(\mathcal D_1\) is the predicate

\[
 S\cap P_h\ne\varnothing\ (2\le h\le j),
 \qquad S\cap P_{j+1}=\varnothing.
\tag{2.7}
\]

The truth of (2.7) changes only at a lower-cycle flip of a coordinate in
\(P_2\cup\cdots\cup P_{j+1}\).  If \(c\) is the number of PBBS step-two
cycles, the number of circular carrier intervals is therefore at most

\[
 c+O(jA/m).
\tag{2.8}
\]

For PBBS,

\[
 c=O(A/m).
\tag{2.9}
\]

This proves that recursive conjugacy and the low-fragmentation relabelling
are compatible; independent phase relabellings are not needed.

Suppose a set of \(\rho_H\) edges cuts \(\mathcal D_1\) into
\(H\)-physical pieces, and transport the same cuts by every \(\phi_j\).
For

\[
 t=\lceil20\log m\rceil,
\]

the first-avoided-category seed then has

\[
 J_0
 \le t(c+\rho_H)+O(At^2/m)+N_{>t},
\tag{2.10}
\]

where the usual first-avoided tail satisfies

\[
 N_{>t}=O(Am^{-2}).
\tag{2.11}
\]

In particular, under the already isolated residence hypothesis

\[
 \boxed{
 \rho_H=o\!\left({A\over H\log m}\right),
 \qquad H=o(m/\log ^2m),}
\tag{PR_H}
\]

we have

\[
 \boxed{J_0=o(W/H).}
\tag{2.12}
\]

Supply each piece with the standard radius-\(H\) endpoint initialization
and terminal collar.  Their total cost is \(O(HJ_0)=o(W)\), and no q=1
token is deleted.

## 3. The PBBS first-shadow defect before switching

The first-avoided rule uses every retained lower target once, and the
designated middle owners are distinct.  PBBS supplies, in one unrestricted
phase,

\[
 1\le \mu(T)\le3,
 \qquad
 \sum_T(\mu(T)-1)=A-{2m-1\choose m-2}=O(A/m).
\tag{3.1}
\]

For the compatibility construction, keep these repeated upper occurrences;
do not perform the optional rainbow deletion.  Their total excess is already
small, and retaining the full conjugate occurrence set is what gives the
exact two-endpoint orbit relation used below.

Restriction to a category cannot increase this duplicate excess.  Hence,
through the first \(t\) phases, the total upper first-shadow duplicate
excess is

\[
 O(At/m)=O(W\log m/m).
\tag{3.2}
\]

The later category tail contributes at most \(N_{>t}\), and the unavoidable
difference between the number of upper first-shadow targets and token starts
is

\[
 W-{n\choose m-1}={2W\over m+2}.
\tag{3.3}
\]

Thus the uncut PBBS seed has upper first-shadow hole and collision defect

\[
 O(W\log m/m)=o(W).
\tag{3.4}
\]

Physical endpoint release adds only \(o(W)\) under \((PR_H)\).  This is the
near-rainbow ledger which must survive the deeper descent.

## 4. Legality of one interval layer

Fix \(j\), abbreviate

\[
 A_0=P_j,\qquad B_0=P_{j+1},\qquad \theta=\theta_j.
\]

For \(S\in\mathcal E_j\), the pointwise identity \(\theta S=S\) and
(2.2) give two candidate tokens

\[
 e_B(S)=\theta e_A(S).
\tag{4.1}
\]

Break \(\mathcal E_j\) into maximal intervals in the physical phase-
\(j\) paths.  On each interval choose either every \(A_0\)-candidate or
every \(B_0\)-candidate.

Every such choice preserves lower ownership because both candidates have
the same lower label.  It also preserves middle injectivity.  Indeed, if
an \(A_0\)-owner over \(S\) equals a \(B_0\)-owner over \(T\), their common
value avoids both \(A_0\) and \(B_0\), hence is fixed by \(\theta\).  The
two old owners are then equal, and injectivity of the old lower-to-owner
map gives \(S=T\).  A corner never takes both candidates over one target.
The unchanged background is compatible with each candidate because it
occurs with that candidate at one of the two coherent endpoints.

For nonconsecutive indices

\[
 \Lambda\subseteq\{1,\ldots,m-1\},
 \qquad |j-k|\ge2\quad(j\ne k),
\tag{4.2}
\]

the choices tensorize.  A changed owner from block \(j\) has first avoided
category in \(\{j,j+1\}\); these category pairs are disjoint over
\(j\in\Lambda\).  Hence cross-block owner collisions are impossible.

Every selected physical interval remains a piece of an old run or of its
coordinate conjugate.  Only its two endpoints are new boundaries.  If
\(r_\Lambda\) is the total number of carrier packets, then

\[
 \boxed{J(M_\varepsilon)\le J_0+2r_\Lambda.}
\tag{4.3}
\]

Equations (2.5), (2.8), and the category tail give

\[
 r_\Lambda
 \le t(c+\rho_H)+O(At^2/m)+N_{>t}
 =o(W/H)
\tag{4.4}
\]

under \((PR_H)\).  Therefore every corner satisfies

\[
 \boxed{J(M_\varepsilon)=o(W/H).}
\tag{4.5}
\]

The endpoint initialization/collar cost of every corner is
\[
 O\bigl(H(J_0+r_\Lambda)\bigr)=o(W).
\tag{4.6}
\]
Thus no flag occurrence has to be released at a newly created boundary.

## 5. Orbit monotonicity: the PBBS q=1 ledger cannot worsen

All lower flags are fixed.  Indeed, by (1.3),

\[
 L_{i,q}\subseteq S_i,
\]

and every changed \(S_i\) avoids \(A_0\cup B_0\).  Thus

\[
 \theta L_{i,q}=L_{i,q}
\tag{5.1}
\]

for every \(q\le H\).

Every nonfixed old upper flag has category \(j\), and its image has
category \(j+1\).  Fix one two-point target orbit

\[
 \{U,\theta U\}.
\]

Let its loads at the old coherent endpoint be \((a,b)\).  At the other
coherent endpoint they are \((b,a)\).  All changed occurrences move in the
same direction, from the category-\(j\) member to the category-\(j+1\)
member.  Hence, after orienting the orbit so that \(a\ge b\), the total
number of moving occurrences is

\[
 k=a-b.
\tag{5.2}
\]

An arbitrary interval corner moves some integer \(\ell\), with

\[
 0\le\ell\le k,
\]

and its two loads are exactly

\[
 (a-\ell,b+\ell).
\tag{5.3}
\]

Consequently every symmetric separable convex load functional is no larger
at the mixed corner than at either coherent endpoint.  In particular,

\[
 {a\choose2}+{b\choose2}
 -{a-\ell\choose2}-{b+\ell\choose2}
 =\ell(k-\ell)\ge0.
\tag{5.4}
\]

Support cannot decrease either: if \(b>0\), both coordinates remain
positive; if \(b=0\), an interior choice creates a second positive
coordinate, while an endpoint choice leaves one positive coordinate.

Applying (5.3)--(5.4) independently on the disjoint category-pair strata
of a layer proves:

### Theorem 5.1 (deterministic first-shadow preservation)

Every PBBS-seeded interval corner has exactly the same lower q=1 ledger as
the seed, and has no more upper q=1 holes or pair collisions than the seed.
Thus its q=1 defect remains \(o(W)\), deterministically, while its component
count remains \(o(W/H)\).

This conclusion does not require \(\mathcal C_{j,1}=0\).  Positive q=1
charge merely improves the seed.

## 6. Exact deeper floor descent with repeated flags allowed

Let the physical carrier packets in block \(j\) be \(I\).  For a target
orbit \(\{U,\theta_jU\}\) at depth \(q\), let

\[
 k_I(U)=\#\{\text{old occurrences of }U\text{ in packet }I\}.
\tag{6.1}
\]

Only targets meeting \(P_{j+1}\) contribute.  Define the cross-packet
charge

\[
 \boxed{
 \mathcal C^{\rm cross}_j
 =\sum_{q=2}^{H}w_q^+
   \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
   \sum_{I<J}k_I(U)k_J(U).}
\tag{6.2}
\]

Here \(I<J\) is any ordering of the packets; the value is independent of
that ordering.  No simplicity assumption inside a packet is made.

Choose the packet sides independently and fairly.  On one target orbit,
the doubled factorial-floor energy drops by

\[
 2\ell(k-\ell).
\]

Writing \(k=\sum_Ik_I\) and averaging gives

\[
 \mathbb E[2\ell(k-\ell)]
 =\sum_{I<J}k_Ik_J.
\tag{6.3}
\]

All lower innovations vanish.  Distinct blocks in a disjoint layer act on
disjoint first-avoided category pairs, so their charges add exactly.  We
therefore obtain:

### Theorem 6.1 (PBBS-seeded disjoint-layer descent)

For every nonconsecutive \(\Lambda\), fair independent physical-packet
choices satisfy

\[
 \boxed{
 \mathbb E\mathcal Q_{\ge2}(M_\varepsilon)
 =\mathcal Q_{\ge2}(M_0)
  -\sum_{j\in\Lambda}\mathcal C_j^{\rm cross}.}
\tag{6.4}
\]

Hence some integral corner simultaneously obeys

\[
 \boxed{
 \mathcal Q_{\ge2}(M_\varepsilon)
 \le\mathcal Q_{\ge2}(M_0)
  -\sum_{j\in\Lambda}\mathcal C_j^{\rm cross},
 \qquad J(M_\varepsilon)=o(W/H),}
\tag{6.5}
\]

and Theorem 5.1 shows that the same corner retains the q=1 near-rainbow
bound.

If each packet contains at most one occurrence of a fixed proper upper
flag, then (6.2) reduces to the earlier full duplicate charge

\[
 \sum_U{\mu_U\choose2}.
\]

For a PBBS physical run this within-packet simplicity is not known and is
not needed for (6.4); repeated flags inside one packet are simply
uncharged.

## 7. Exact audit of the claim C_{j,1}=0

For the original tight cyclic-window chart, the claim is correct.  Here is
the complete proof, including the adjacency case omitted from the earlier
short argument.

Fix a local cyclic row.  A q=1 occurrence with lower endpoint \(S\) and
upper target \(U\) has a two-point collar

\[
 C_S=U\setminus S.
\tag{7.1}
\]

The two adjacent rank-\(m\) windows are \(U\setminus\{c\}\),
\(c\in C_S\).  Suppose two distinct occurrences of the same \(U\) have
intersecting collars, and choose \(c\) in their intersection.  Then the
rank-\(m\) state \(U\setminus\{c\}\) belongs to both occurrences.

If the occurrences lie in different rows, or are nonadjacent in one row,
this repeats a rank-\(m\) window in the exact local wreath factor, which is
impossible.  If they are adjacent in one row, their upper targets are two
consecutive cyclic windows of length \(m+1\).  These are distinct because

\[
 m+1<2m-1
\]

in the range \(H\le m-2\).  Hence this case cannot have the same \(U\)
either.  The collars are therefore disjoint.

If both lower endpoints lie in the changed carrier and \(U\) meets the
partner pair \(P_{j+1}\), then both lower endpoints avoid that pair, so

\[
 \varnothing\ne U\cap P_{j+1}
 \subseteq C_S\cap C_T,
\]

a contradiction.  Thus at most one moving occurrence uses any activated
q=1 target, and

\[
 \boxed{\mathcal C_{j,1}=0}
\tag{7.2}
\]

for the tight cyclic-window chart.

The proof does not extend to an arbitrary transition factor.  Two
consecutive transitions

\[
 U\setminus\{a\},\quad U\setminus\{b\},\quad U\setminus\{c\}
\]

have the same union \(U\) on both edges and collars \(\{a,b\}\) and
\(\{b,c\}\).  They legitimately share the middle state
\(U\setminus\{b\}\).  Exact state ownership does not forbid this.  If the
partner pair meets \(U\) only in \(b\), both lower intersections avoid the
partner pair and the q=1 charge is positive.  The currently proved PBBS
angle-multiplicity theorem does not rule out this local pattern.

Therefore the correct statement is:

\[
 \boxed{
 \mathcal C_{j,1}=0\text{ for tight cyclic-window charts, but not as a
 formal consequence of the transition-factor axioms.}}
\tag{7.3}
\]

For PBBS compatibility it is replaced by the stronger-for-purpose
deterministic monotonicity of Theorem 5.1.

## 8. The remaining theorem after compatibility

The present theorem proves that no q=1 ledger conflict and no component
explosion occurs when one PBBS-seeded disjoint interval layer is applied.
Two issues are outside the compatibility theorem.

First, the known PBBS colour theorem alone does not prove \((PR_H)\).
That is exactly the previously isolated short-residence transversal problem.

Second, even after \((PR_H)\), the explicit charge (6.2) need not control
all \(q\ge2\) floor excess, and a mixed corner is not automatically a new
coherent PBBS base for another overlapping layer.  The one genuinely new
statement required by this lane may be packaged as follows.

> **Renewable PBBS charged-frame lemma (open).**  Starting from an
> \(H\)-physical recursively conjugate PBBS seed, there is a sequence of
> legal disjoint adjacent-pair interval layers such that:
>
> 1. every next layer has a coherent conjugate representation on its
>    active blocks;
> 2. the sum of its cross-packet charges is the \(q\ge2\) floor excess up to
>    \(o(W)\);
> 3. the total number of physical packet boundaries over the sequence is
>    \(o(W/H)\).

Theorems 5.1 and 6.1 show that this lemma would reduce the complete central
band while retaining the PBBS q=1 defect and an \(o(W)\) reset cost.  No
additional first-shadow repair theorem would be needed.

Thus the sharp status is:

\[
 \boxed{
 \text{PBBS q=1 seed + physical residence is compatible with }
 q\ge2
 \text{ interval descent; charged-frame renewal remains open.}}
\]
