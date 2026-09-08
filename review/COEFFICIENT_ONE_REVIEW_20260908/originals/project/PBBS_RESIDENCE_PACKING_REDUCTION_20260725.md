# PBBS residence is an exact short-return packing problem

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Outcome

Let

\[
N=2r+1,\qquad A={N\choose r},\qquad B=A/N,
\]

and let \(P_r\) be the canonical PBBS odd-graph cycle factor.  Orient the
**complement-projected** step-two Johnson cycles, whose owners have rank
\(r+1\).  Consecutive occurrences of one omitted label at odd gap
\(2s+1\) give one positive coordinate-residence interval of length
\(s+1\) in the projected owner cycle.  Let \(\mathcal I_H\) be the
intervals with \(s+1\le H\).

Write \(\nu_H(P_r)\) for the largest number of members of
\(\mathcal I_H\) which are pairwise disjoint as sets of step-two transition
edges.  Write \(J_H(P_r)\) for the least number of path runs obtained by
cutting the projected cycles so that every remaining path is a genuine
radius-\(H\) rotor run.  Throughout the rotor statements assume
\(H\le (r+1)/2\), which contains the mesoscopic range used below.

The main exact reduction is

\[
\boxed{
   \nu_H(P_r)\le J_H(P_r)
   \le \nu_H(P_r)+c_2(P_r),
}
\tag{0.1}
\]

where \(c_2(P_r)\le B\) is the number of projected step-two cycles.  Thus,
at every scale \(H=o(r)\), a Catalan bound

\[
\nu_H(P_r)=O(A/r)
\tag{0.2}
\]

is equivalent, up to a harmless Catalan term, to the desired physical
PBBS row bound.

There is also an exact inversion of the previously proved PBBS rank-excess
sequence.  If

\[
 E_q(P_r)=\sum_{I\in\mathcal I_\infty}(q-s(I))_+,
\]

then the number of short projected residence intervals is

\[
\boxed{
 |\mathcal I_H|=E_H(P_r)-E_{H-1}(P_r).
}
\tag{0.3}
\]

Consequently

\[
\boxed{
 {E_H-E_{H-1}\over r+2}
 \le J_H
 \le E_H-E_{H-1}+c_2(P_r).
}
\tag{0.4}

This does not prove the Catalan packing bound (0.2).  It identifies the
remaining theorem sharply: one must rule out a super-Catalan packing of
edge-disjoint PBBS returns of temporal length at most \(H\).  Merely
bounding the total number of short returns is stronger than necessary.

The later sections sharpen this status in six directions.

1. Gap three is impossible, so the PBBS depth-two rank excess is actually
   zero pointwise.
2. Peak deletion is an exact PBBS renormalization and proves the sharp
   pointwise bound \(g\ge2\operatorname{ht}(D)+1\).  It yields
   \(\nu_H=o(B)\) for \(H=o(\sqrt{r/\log r})\).
3. The formerly proposed stronger vacancy bound
   \(g\ge2(r-\operatorname{pk}(D))+1\) is explicitly **retracted and
   disproved**: height-three roots of arbitrarily large peak defect have gap
   seven.  All gap-seven roots are nevertheless classified, and their whole
   physical packing is only \(\Theta(N2^r)=o(B)\).
4. In the intended range \(H\log N=o(r)\), (0.2) is equivalent to the
   super-sparse quotient assertion \(\overline\nu_H=O(B/N)\).  This aggregate
   Dyck-quotient clustering theorem remains open and is the authoritative
   residual of the PBBS residence lane.
5. A global-maximum corridor in the combined forward/reverse unmatched-mark
   word proves complete correct PBBS intersection support at **every** depth.
   Thus target support itself is no longer conjectural.
6. A dominance-staircase seam replaces the former quadratic singleton
   repair by an exact \(O(H)\) chart at each cut.  Consequently constant
   one follows from the weaker fixed-window estimate
   \[
      \nu_{\lceil A\sqrt r\rceil}(P_r)=O_A(B)
   \]
   for every fixed \(A\).  The explicit sharp ledger is recorded in
   Section 24.

## 1. Omitted labels and projected residence intervals

Consider one oriented PBBS component

\[
 A_0,A_1,\ldots,A_{L-1}
\]

and let \(\lambda_i\) be the omitted label of the odd-graph edge
\(A_iA_{i+1}\).  The audited recurrence is

\[
 A_{i+2}=A_i-\{\lambda_{i+1}\}+\{\lambda_i\}.
\tag{1.1}
\]

Every label occurs \(\ell=L/N\) times.  The cyclic gap between consecutive
occurrences of the same label is odd and at least three.

The physical owners in the middle-levels transition construction are the
complements

\[
 X_i=[N]\setminus A_i,
\]

and (1.1) becomes

\[
 X_{i+2}=X_i-\{\lambda_i\}+\{\lambda_{i+1}\}.
\tag{1.2}
\]

Suppose consecutive occurrences of a label are at positions \(i\) and
\(i+2s+1\).  At the projected transition indexed by \(i-1\), that label is
inserted as \(\lambda_i\); at the projected transition indexed by
\(i+2s+1\), it is removed as \(\lambda_{i+2s+1}\).  These transition
indices differ by \(2s+2\), or \(s+1\) step-two moves.  Thus its positive
projected residence length is

\[
 \ell=s+1={g+1\over2}.
\tag{1.3}
\]

This one-step shift is important at depth one: gap three gives projected
residence two, not one.  In particular, projected PBBS cycles have no
positive residence-one obstruction.

Denote by

\[
 I_i=\{i-1,i+1,\ldots,i+2s+1\}
\tag{1.4}
\]

the corresponding circular set of step-two transition edges.  It has
\(s+2=\ell+1\) edges: the insertion edge, the internal residence edges,
and the removal edge.  Cutting any member of \(I_i\) prevents that insertion
and removal from lying in one path run.  Reversing a projected cycle merely
uses the gaps in reverse cyclic order and does not change the resulting
packing/transversal statistics.

Let \(\mathcal I_H(C)\) be the intervals (1.4) on one projected cycle with
\(s+1\le H\), and let

\[
 \tau_H(C)=\min\{|D|:D\text{ is a set of transition edges meeting every }
                         I\in\mathcal I_H(C)\}.
\tag{1.5}
\]

The prescribed-cycle rotor theorem gives

\[
 J_H(C)=\max\{1,\tau_H(C)\}.
\tag{1.6}
\]

The one in (1.6) is the cut needed to linearize a compatible cycle.

## 2. Circular interval packing is exact up to one

Let \(\nu_H(C)\) be the maximum cardinality of a pairwise edge-disjoint
subfamily of \(\mathcal I_H(C)\).

### Theorem 2.1 (circular packing--transversal sandwich)

For every projected cycle,

\[
\boxed{
 \nu_H(C)\le J_H(C)\le \nu_H(C)+1.
}
\tag{2.1}

#### Proof

Every cut edge meets at most one member of a pairwise disjoint family, so
\(\tau_H(C)\ge\nu_H(C)\).  Hence (1.6) gives the lower bound in (2.1).

If \(\mathcal I_H(C)\) is empty, one arbitrary cut gives \(J_H(C)=1\), so
the upper bound holds.  Otherwise choose any transition edge \(e\) which
belongs to one short interval.  Use \(e\) as one cut.  All intervals not
hit by \(e\) avoid \(e\); after opening the circle at \(e\), they are
ordinary intervals on a line.  For line intervals, the greedy
right-endpoint algorithm gives a transversal whose size equals the maximum
number of pairwise disjoint intervals.  That packing number is at most
\(\nu_H(C)\).  Thus all short intervals, and the cycle itself, are cut by
at most \(1+\nu_H(C)\) edges.  This proves (2.1).  \(\square\)

Summing (2.1) over all projected cycles proves (0.1).

The PBBS level ledger gives

\[
c_2(P_r)\le B=A/(2r+1).
\tag{2.2}
\]

Therefore, whenever \(H=o(r)\),

\[
 Hc_2(P_r)=o(A).
\tag{2.3}
\]

The cycle-linearization term is not part of the mesoscopic obstruction.

## 3. Exact slope inversion of the PBBS rank excess

Let \(M_s\) be the number of consecutive omitted-label gaps \(2s+1\),
summed over all PBBS components.  The audited gap identity is

\[
 E_q(P_r)=\sum_{s\ge1}(q-s)_+M_s.
\tag{3.1}
\]

### Theorem 3.1 (discrete derivative identities)

For every \(q\ge1\),

\[
\boxed{
 E_q-E_{q-1}=\sum_{s\le q-1}M_s,
}
\tag{3.2}
\]

and

\[
\boxed{
 M_q=E_{q+1}-2E_q+E_{q-1}.
}
\tag{3.3}

In particular (0.3) holds.

#### Proof

For one integer \(s\ge1\),

\[
 (q-s)_+-(q-1-s)_+=\mathbf1_{\{s\le q-1\}}.
\]

Sum this identity against \(M_s\) to obtain (3.2), and difference once
more to obtain (3.3).  \(\square\)

Thus the number of short residence intervals is the *slope*, not the value,
of the PBBS rank-excess potential.

## 4. Exact edge congestion

### Lemma 4.1

Every directed projected step-two transition edge belongs to exactly
\(r+2\) of the full positive-residence intervals \(I_i\), before the cutoff
\(s+1\le H\) is imposed.

#### Proof

Write one projected Johnson transition as

\[
 X\longrightarrow Y=X-\{a\}+\{b\}.
\]

The projected owners have rank \(r+1\).  The positive run of each coordinate
in \(X\cap Y\), of which there are \(r\), contains this edge internally.
The positive run of \(a\) ends at the edge, and the positive run of \(b\)
begins at it.  These are all the possibilities, giving
\(r+2\).  \(\square\)

It follows that one cut edge meets at most \(r+2\) short intervals.  Hence

\[
 { |\mathcal I_H|\over r+2}\le \tau_H(P_r)\le J_H(P_r).
\tag{4.1}
\]

Combining (4.1) with (0.3) gives the lower bound in (0.4).  The trivial
choice of one edge from every short interval gives

\[
 J_H(P_r)\le |\mathcal I_H|+c_2(P_r),
\]

which is the upper bound in (0.4).

There is also a universal, but only constant-order, packing estimate.  If
\(\mathcal P\subseteq\mathcal I_H\) is pairwise disjoint, then

\[
 \sum_{I\in\mathcal P}|I|\le A.
\tag{4.2}
\]

For an interval of projected residence \(\ell=s+1\), its contribution to
\(E_H\) is \(H-s=H+1-\ell\), while \(|I|=\ell+1\).  Therefore

\[
\boxed{
 \nu_H(P_r)\le {A+E_H(P_r)\over H+2}.
}
\tag{4.3}

Equation (4.3) explains why the already known nonnegative gap energy alone
does not give coefficient one: even \(E_H=o(A)\) yields only
\((1+o(1))A/H\) cuts, whose radius-\(H\) initialization still costs order
\(A\), not \(o(A)\).  What is needed is a genuinely subcritical packing
bound.

## 5. Exact residual for the pair-omission PBBS construction

In the pair-omission construction, let

\[
 r=m-1,\qquad A_m={2m-1\choose m-1}.
\]

The first-avoided-pair extraction uses only \(O(\log m)\) nonnegligible
phases.  Its category-boundary and PBBS cycle terms are already

\[
 O(A_m\log^2m/m).
\tag{5.1}

By Theorem 2.1, the remaining residence term may be written with no loss as
the short-return packing number.  A sufficient statement is

\[
\boxed{
 \nu_H(P_{m-1})
 =o\!\left({A_m\over H\log m}\right).
}
\tag{5.2}

For a whole local PBBS factor, (5.2) is also necessary up to the harmless
cycle term: every family of pairwise disjoint short-return arcs requires that
many distinct row cuts.  Category restriction can discard some arcs before
they become physical requirements, so (5.2) is only a clean sufficient
uniform estimate for the global first-avoided extraction, not a necessity for
every more adaptive category assignment.

A Catalan estimate

\[
\boxed{
 \nu_H(P_{m-1})=O(A_m/m)
}
\tag{5.3}

is more than enough throughout

\[
 H=\sqrt m\,\omega(m),\qquad
 \omega(m)\to\infty,\qquad
 \omega(m)=o\!\left({\sqrt m\over\log^2m}\right),
\tag{5.4}

because

\[
 {A_m/m\over A_m/(H\log m)}={H\log m\over m}=o(1).
\]

At \(H=1\), the projected interval family is empty.  In fact the exact
Dyck-quotient calculation below shows that PBBS has no gap-three return, so

\[
 |\mathcal I_2|=E_2(P_{m-1})=0.
\]

Thus (5.3) is trivial at \(H=2\).  No theorem presently extends (5.3) to
the growing window in (5.4).

## 6. The remaining positive theorem

The PBBS residence lane is therefore reduced exactly to the following
statement.

> **PBBS Catalan short-return packing theorem.**  For the canonical PBBS
> factor on \(KG(2m-1,m-1)\), every family of pairwise edge-disjoint
> omitted-label return arcs with odd gaps at most \(2H-1\) has size
> \(O(A_m/m)\), uniformly for \(H\) in (5.4).

This is strictly weaker than asking that the *number* of such returns be
Catalan.  Many short coordinate returns are permitted, provided they cluster
through Catalan-many transition edges.  It is also the sharp statistic for
literal factorization: Theorem 2.1 loses at most one cut per PBBS cycle and
nothing else.

The complete-colour theorem, point homomesy, odd-gap rule, and the known
\(g=3\) estimate do not prove this packing theorem.  A proof must use the
specific parenthesis/PBBS dependence to show that short returns cluster, or
else replace the PBBS chronology by a row-coherent splice.

## 7. Quotient size and exact point margins do not prove the packing bound

The following deterministic construction shows why merely quotienting by
coordinate rotation cannot prove (5.3).  It is a theorem about projected
Johnson cycles, not a counterexample to the canonical PBBS map.

### Theorem 7.1 (many packed short returns with exact rank)

Let \(N=2r+1\), put \(k=r+1\), and let

\[
 2\le H=o(N).
\]

For all sufficiently large \(N\), there is a simple directed Johnson cycle

\[
 X_0,X_1,\ldots,X_{N-1}
 \quad\text{in }J(N,k)
\]

with all of the following properties.

1. Every coordinate is the entering coordinate exactly once and the
   departing coordinate exactly once.
2. The sum of all coordinate residence lengths is exactly \(Nk\), as it
   must be for rank \(k\).
3. The cycle contains at least

   \[
      \left\lfloor {N\over4H}\right\rfloor
   \]

   pairwise edge-disjoint positive-residence intervals of length exactly
   \(H\).

Thus exact arrival/departure margins and distinct projected owners permit
\(\Omega(N/H)\) packed short intervals in a single cycle.

#### Proof

Work in \(\mathbb Z_N\).  For a permutation \(\tau\) without fixed points,
put

\[
 R_i=(\tau(i)-i)\bmod N\in\{1,\ldots,N-1\}.
\tag{7.1}
\]

Coordinate \(i\) will be present at owner times

\[
 i,i+1,\ldots,i+R_i-1.
\tag{7.2}

Choose

\[
 p=\left\lfloor {N\over4H}\right\rfloor
\]

disjoint blocks of length \(4H\).  In block \(j\), choose two positions

\[
 a_j=4Hj+1,\qquad b_j=a_j+H,
\]

and make \((a_j\ b_j)\) a transposition of \(\tau\).  All these endpoints
have both cyclic neighbours outside the chosen endpoint set.  The two
residences supplied by this transposition are

\[
 R_{a_j}=H,\qquad R_{b_j}=N-H.
\tag{7.3}

Let \(R\) be the remaining set of positions and put \(M=|R|=N-2p\).
Then \(M\) is odd.  List its members in increasing cyclic order as

\[
 x_0<x_1<\cdots<x_{M-1}
\]

and set

\[
 w={M+1\over2},\qquad
 \tau(x_j)=x_{j+w\pmod M}.
\tag{7.4}

Since \(2w-M=1\), one has \(\gcd(w,M)=1\), so (7.4) is one cycle on all
of \(R\).  In the sorted cyclic order, the step \(j\mapsto j+w\) wraps
exactly \(w\) times.  Hence

\[
 \sum_{x\in R}R_x=wN.
\tag{7.5}

Every transposition contributes \(N\) to the residence sum.  Since

\[
 w={N-2p+1\over2}=k-p,
\]

equations (7.3)--(7.5) give

\[
 \sum_{i\in\mathbb Z_N}R_i=pN+wN=kN.
\tag{7.6}

Define

\[
 X_t=\{i:t-i\pmod N\in\{0,1,\ldots,R_i-1\}\}.
\tag{7.7}

The departure times \(\tau(i)=i+R_i\) are distinct.  Thus one coordinate
enters and one coordinate leaves at every transition.  All \(|X_t|\) are
equal, and (7.6) says their average is \(k\); hence every \(X_t\) is a
\(k\)-set and consecutive owners are Johnson adjacent.

We next verify simplicity.  For two times \(a\ne b\), let \(I\) be the
proper cyclic interval of arrival indices encountered after \(a\) and through
\(b\).  Then

\[
 X_a=X_b
 \quad\Longleftrightarrow\quad
 \tau(I)=I.
\tag{7.8}

Indeed, equality across the interval means that every coordinate has either
both its arrival and departure in \(I\), or neither; this is exactly
\(\tau(I)=I\).

Every invariant set of \(\tau\) is a union of some chosen transposition
pairs and, possibly, the one large cycle \(R\).  A nonempty union of chosen
pairs is not a cyclic interval: every one of its points has a neighbouring
unchosen point, and the two endpoints of each pair are separated by
\(H\ge2\).  Its complement is not a cyclic interval for the same reason.
Therefore no nonempty proper invariant set is a cyclic interval.  By (7.8),
the \(X_t\)'s are distinct.

Finally, each coordinate \(a_j\) has residence interval
\([a_j,b_j)\) of length \(H\).  The containing blocks have length \(4H\),
so even after adjoining the insertion and removal transition edges, these
\(p\) intervals are pairwise edge-disjoint.  This proves all assertions.
\(\square\)

### Consequence

Theorem 7.1 rules out a proof of the PBBS Catalan packing theorem using only

* one rotation quotient state per coordinate orbit;
* bijective arrival and departure labels;
* exact rank/point-incidence totals; and
* simplicity of the projected Johnson cycles.

The missing restriction is the actual parenthesis map.  In normalized
Dyck-root coordinates it is a specific skew product, not an arbitrary
departure permutation.  Any successful proof of (5.3) must exploit that
specific cocycle.

## 8. Even actual PBBS components can have linearly large packing

The next exact family shows that a Catalan proof cannot work component by
component.  One genuine PBBS component of quotient level three already has
\(\Theta(N)\) disjoint projected residence-three intervals.

### 8.1 The normalized Dyck-root cocycle

Normalize a middle state by rotating its unique unmatched zero to the first
position.  It then has the form

\[
 0D,
\]

where \(D\) is a Dyck word of semilength \(r\).  Let the first visit to the
maximum height of \(D\) end with the marked up-step in

\[
 D=P\,1\,Q,
\]

and put

\[
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q\,0\,\overline P.
\tag{8.1}
\]

Here the bar interchanges zero and one.

### Lemma 8.1 (exact PBBS skew product)

The word \(\phi(D)\) is Dyck, and the parenthesis/PBBS map is

\[
 (u,D)\longmapsto (u+\delta(D)\pmod N,\phi(D)),
\tag{8.2}
\]

where \(u\) is the coordinate of the unmatched zero.

#### Proof

The marked step is the first step reaching the maximum height \(h\).
The suffix \(Q\), read from height \(h\), never goes above its starting
height and ends at zero.  Thus \(\overline Q\) has nonnegative partial sums
and total height \(h\).  The following zero lowers this to \(h-1\).
Every prefix of \(P\) has height at most \(h-1\), so, when read from height
\(h-1\), \(\overline P\) never goes below zero and ends at zero.  Hence
\(\phi(D)\) is Dyck.

The PBBS update leaves the unmatched zero fixed and complements every bit
of \(D\), giving the cyclic word \(0\overline D\).  Its new unmatched zero
is exactly the complemented marked up-step at position \(|P|+1\).  Cutting
immediately after it reads \(\overline Q0\overline P\), proving (8.2).
\(\square\)

### Theorem 8.2 (a level-three PBBS packing family)

For every \(r\ge3\), the canonical PBBS factor on \(KG(2r+1,r)\) has one
component of length \(3N\) whose complement-projected step-two cycle obeys

\[
 \boxed{\nu_3\ge \lfloor N/2\rfloor=r.}
\tag{8.3}
\]

#### Proof

Put \(t=r-3\), and consider the three Dyck words

\[
\begin{aligned}
D_0&=110100(10)^t,\\
D_1&=1011(01)^t00,\\
D_2&=(10)^t110010.
\end{aligned}
\tag{8.4}
\]

Their first maximum-reaching up-steps occur respectively at positions

\[
 2,\qquad4,\qquad2t+2=N-5.
\tag{8.5}
\]

Applying (8.1) directly gives

\[
 D_0\longmapsto D_1\longmapsto D_2\longmapsto D_0,
\tag{8.6}
\]

so the quotient voltages are

\[
 (2,4,N-5).
\tag{8.7}
\]

Their total is \(N+1\equiv1\pmod N\), so this quotient three-cycle lifts
to one PBBS component of length \(3N\).  Starting at \(D_1\), the first
five voltage sums are

\[
 4,\quad N-1,\quad N+1,\quad N+5,\quad2N.
\tag{8.8}
\]

The first four are nonzero modulo \(N\), whereas the fifth is zero.  Thus
the next occurrence of the omitted coordinate has gap five and projected
residence three.

Take all \(N\) spatial rotations of this return interval.  The interval
uses four projected transition edges.  Three lie in distinct quotient-edge
orbits; the remaining quotient-edge orbit is used twice, at phases differing
by two.  Hence two rotations by phases \(a,b\in\mathbb Z_N\) intersect if
and only if

\[
 a-b\equiv\pm2\pmod N.
\tag{8.9}
\]

Their conflict graph is therefore
\(\operatorname{Cay}(\mathbb Z_N,\{\pm2\})\cong C_N\), since \(N\) is
odd.  Its independence number is \(\lfloor N/2\rfloor=r\).  Choosing a
maximum independent set gives \(r\) pairwise projected-edge-disjoint
residence-three intervals inside the single lifted component. \(\square\)

### Consequence for the Catalan attack

Theorem 8.2 is not a counterexample to the global bound (5.3), because the
global Catalan mass \(B\) is exponentially larger than \(N\).  It does prove
two useful negative facts about a prospective proof:

1. no bound \(O(\ell)\) is possible for a PBBS quotient component of level
   \(\ell\); and
2. one cannot inject packed arcs with bounded multiplicity into the quotient
   states of their own component.

A proof of (5.3) must instead be an **aggregate enumeration theorem over all
Dyck-root quotient cycles**.  It must show that components like (8.4) have
small total Catalan mass, even though each such component is individually
bad.

## 9. Two PBBS steps are an exact first-maximum block rotation

The one-step formula (8.1) can be sharpened substantially.  Let the marked
up-step of a Dyck word (D) be its first step which attains the global
maximum.  Starting immediately after that step, let the displayed zero below
be the first step which returns the path to height zero.  There is then a
unique factorization

\[
 D=P\,1\,R\,0\,S.                                      \tag{9.1}
\]

Thus (S) is a Dyck word: it is precisely the suffix of complete primitive
components lying after the first primitive component which attains the
global maximum.  The words (P) and (R) need not themselves be Dyck.

### Theorem 9.1 (two-step block rotation and deficit voltage)

For the factorization (9.1),

\[
 \boxed{
 \begin{aligned}
  \delta(D)&=|P|+1,\\
  \delta(\phi D)&=|R|+1,\\
  \phi^2(D)&=S\,1\,P\,0\,R.
 \end{aligned}}
                                                               \tag{9.2}
\]

Consequently, on putting

\[
 d(D)=|S|+1,
                                                               \tag{9.3}
\]

the two-step voltage obeys the ordinary integer identity

\[
 \boxed{
  \delta(D)+\delta(\phi D)=N-d(D),
 }
                                                               \tag{9.4}
\]

and the even-time skew product is

\[
 \boxed{
  (u,D)\longmapsto (u-d(D)\pmod N,\ \phi^2D).
 }
                                                               \tag{9.5}
\]

#### Proof

In (9.1), the suffix after the marked up-step is (R0S).  Formula
(8.1) gives

\[
 \phi(D)=\overline R\,1\,\overline S\,0\,\overline P.
                                                               \tag{9.6}
\]

Before the displayed (1), the path in (9.6) is the complement of the
descent from the old maximum down to height one.  It stays below the old
maximum height and reaches that height for the first time at the displayed
(1).  The remainder (overline S0\overline P) never exceeds it.  Hence
this displayed (1) is exactly the first maximum-reaching step of
(phi(D)), proving (delta(\phi D)=|R|+1).

Applying (8.1) once more to (9.6) gives

\[
 \phi^2(D)
 =\overline{\,\overline S0\overline P\,}\,0\,
   \overline{\overline R}
 =S1P0R,
\]

which proves (9.2).  Since

\[
 |P|+1+|R|+1+|S|=2r=N-1,
\]

equation (9.4) follows.  Reducing (9.4) modulo (N) in the skew product
(8.2) proves (9.5).  \(□\)

The important feature of (9.5) is that the complicated pair of
first-maximum positions has disappeared.  Its residue is the negative of a
positive odd integer (d(D)), and that integer is the length of an explicit
terminal Dyck suffix plus one.

## 10. Exact short-return word equations

Put

\[
 \tau=\phi^2.
\]

For (D_h=\tau^hD), use the unique decomposition

\[
 D_h=P_h1R_h0S_h                                      \tag{10.1}
\]

from (9.1).  Theorem 9.1 is equivalent to the word recursion

\[
 \boxed{
  P_{h+1}1R_{h+1}0S_{h+1}=S_h1P_h0R_h.
 }
                                                               \tag{10.2}
\]

### Theorem 10.1 (complete odd-return criterion)

The omitted coordinate at ((u,D)) returns after (2s+1) PBBS steps if
and only if

\[
 \boxed{
  \sum_{h=0}^{s-1} (|S_h|+1)
       \equiv |P_s|+1 \pmod N.
 }
                                                               \tag{10.3}
\]

It is the *first* return exactly when the same congruence fails with (s)
replaced by every (0\le j<s).  Equivalently, for a uniquely determined
integer (a\ge0),

\[
 \boxed{
  \sum_{h=0}^{s-1} (|S_h|+1)=|P_s|+1+aN.
 }
                                                               \tag{10.4}
\]

#### Proof

After (s) applications of (9.5), the spatial root is

\[
 u-\sum_{h=0}^{s-1}d(D_h)\pmod N.
\]

The final odd PBBS step adds (delta(D_s)=|P_s|+1).  It returns to (u)
precisely when (10.3) holds.  Positivity gives the unique integer form
(10.4), and applying the same statement to each shorter odd prefix gives
the first-return assertion.  \(□\)

Thus the aggregate PBBS problem has been reduced to a system of literal word
equations (10.2), the first-maximum admissibility conditions in (10.1), and
one length equation (10.4).  For the family in Theorem 8.2, start the
gap-five return at \(D_1\).  Then \(s=2\), \(\tau D_1=D_0\), and, with
\(t=r-3\),

\[
 \bigl(d(D_1),d(D_0)\bigr)=(1,2t+1)=(1,N-6),
 \qquad
 \delta(\tau^2D_1)=\delta(D_2)=N-5.
\]

Thus \(1+(N-6)=N-5\), so the return lies in the zero-winding case
\(a=0\).  The shorter display \((1,3)\) with endpoint deficit \(4\)
is only the special case \(r=4\), not the general family.

## 11. Exact enumeration of the one-step deficit

Although correlations between successive deficits remain unresolved, the
marginal distribution of (d(D)) has a closed Catalan generating function.
Let (C_h(z)) be the generating function for Dyck paths of height at most
(h), with semilength marked by (z).  Set

\[
 C_{-1}(z)=0,qquad C_0(z)=1,qquad
 C_h(z)={1\over1-zC_{h-1}(z)}.                       \tag{11.1}
\]

Let (b_{r,j}) be the number of (D\in\mathcal D_r) for which the suffix
(S) in (9.1) has semilength (j), equivalently (d(D)=2j+1).

### Theorem 11.1 (first-highest-component formula)

For (0\le j<r),

\[
 \boxed{
 b_{r,j}
 =\sum_{h\ge1}
  [z^{,r-j}]\,
     zC_{h-1}(z)\bigl(C_{h-1}(z)-C_{h-2}(z)\bigr)
  \;[z^j]C_h(z).
 }
                                                               \tag{11.2}
\]

Equivalently, the full bivariate generating series is

\[
 \boxed{
 \sum_{r\ge1}\sum_{0\le j<r} b_{r,j}x^{r-j}y^j
 =\sum_{h\ge1}
   xC_{h-1}(x)\bigl(C_{h-1}(x)-C_{h-2}(x)\bigr)C_h(y).
 }
                                                               \tag{11.3}
\]

#### Proof

Decompose a nonempty Dyck path into its primitive components.  Let (h) be
its global height and distinguish the first primitive component of height
(h).  The components preceding it form an arbitrary Dyck path of height
at most (h-1), contributing (C_{h-1}).  A primitive component of exact
height (h) has the form (1E0), where (E) has exact height (h-1),
and therefore contributes

\[
 z\bigl(C_{h-1}-C_{h-2}\bigr).
\]

The suffix after that distinguished component is an arbitrary Dyck path of
height at most (h), contributing (C_h).  The decomposition is unique,
and marking the first two parts by (x) and the suffix by (y) proves
(11.3), hence (11.2).  \(□\)

As a consistency check, setting (x=y=z) and using

\[
 zC_{h-1}(C_{h-1}-C_{h-2})C_h=C_h-C_{h-1}
\]

telescopes (11.3) to (C(z)-1), as required.

Theorem 11.1 removes the one-step counting problem completely.  The exact
remaining enumeration is genuinely a **correlation** problem for the block
rotation (10.2): bound edge-disjoint solutions of (10.2)--(10.4) after
summing over all Dyck roots.  In particular, replacing the successive
suffixes (S_h) by independent samples from (11.2) would discard precisely
the PBBS structure still needed for the Catalan packing theorem.

## 12. Winding is exactly chargeable; zero winding is the irreducible case

For a return interval (I) of odd PBBS gap (2s+1), define its
**two-step winding** (a(I)) by (10.4).  Its (s) step-two edges carry the
deficit weights

\[
 d(D_0),d(D_1),\ldots,d(D_{s-1}).
\]

Let

\[
 \mathscr D_r=\sum_{D\in\mathcal D_r}d(D)
              =\sum_{j=0}^{r-1}(2j+1)b_{r,j}.          \tag{12.1}
\]

### Theorem 12.1 (exact winding ledger for a packed family)

If (mathcal P) is any pairwise step-two-edge-disjoint family of PBBS
return intervals, then

\[
 \boxed{
  \sum_{I\in\mathcal P}
    \bigl(\delta(D_{s(I)}(I))+N a(I)\bigr)
  \le N\mathscr D_r.
 }
                                                               \tag{12.2}
\]

In particular,

\[
 \boxed{
  \sum_{I\in\mathcal P}a(I)\le\mathscr D_r.
 }
                                                               \tag{12.3}
\]

#### Proof

Equation (10.4) says that the deficit weight summed on the step-two edges
of (I) is exactly

\[
 \delta(D_{s(I)}(I))+Na(I).
\]

The intervals in (mathcal P) use disjoint step-two edges.  Every
normalized Dyck edge type (D) has exactly (N) spatial translates in the
full PBBS factor.  Hence the total available deficit weight on all physical
step-two edges is exactly (N\sum_Dd(D)=N\mathscr D_r).  Summing over the
packed intervals proves (12.2), and dropping the positive terminal terms
proves (12.3).  \(□\)

The theorem cleanly separates what a scalar voltage argument can and cannot
do.  Every positive-winding return consumes a full additional (N) units
of the explicit Catalan deficit mass (12.1).  But the family in Theorem 8.2
has (a(I)=0) for all of its short returns, so no estimate based only on
winding can control the required packing.  The irreducible enumeration
problem is therefore the zero-winding word equation

\[
 \boxed{
  \sum_{h=0}^{s-1}(|S_h|+1)=|P_s|+1,
 }
                                                               \tag{12.4}
\]

together with (10.2) and its positive-winding perturbations.  This is a
strictly narrower target than arbitrary modular cocycle return.

## 13. Endpoint parity alone is already saturated on the Gaussian scale

There is a tempting weaker approach to (10.2): retain only the initial and
terminal Dyck words.  That loses too much information at exactly the desired
scale.

Let (D) be a Dyck word and give a (1)-step sign (+1) and a (0)-step
sign (-1).  If an odd PBBS segment of length (g) begins and ends with the
same unmatched coordinate, then outside the coordinates which occur an odd
number of times as intermediate unmatched coordinates, the terminal Dyck
word is the bitwise complement of (D).  If the odd-support positions in
the balanced part are (R), the terminal height is therefore

\[
 H_E(t)=-H_D(t)+2\sum_{i\in R,,i\le t}\operatorname{sgn}_D(i).
                                                               \tag{13.1}
\]

The next theorem shows that this necessary endpoint condition is essentially
vacuous once (g) reaches the natural Dyck-height scale.

### Theorem 13.1 (canonical complement repair by record steps)

Let (D) have height (h).  For each (1\le a\le h), mark

* the first up-step of (D) which enters height (a); and
* the last down-step of (D) which leaves height (a).

Let (R(D)) be these (2h) marked positions, and obtain (E(D)) by
keeping the bits of (D) on (R(D)) and complementing every other bit.
Then

\[
 \boxed{E(D)\text{ is a Dyck word and }
        |{i:E_i(D)=D_i}|=2h.}                     \tag{13.2}
\]

#### Proof

The marked up-steps contribute (+1) and the marked down-steps contribute
(-1), so the correction term in (13.1) ends at zero and (E(D)) is
balanced.

At a time (t), let (M(t)) be the greatest height reached by (D) up to
time (t), and let (L(t)) be the greatest level whose last downward exit
has already occurred.  Before any marked last exits, the correction in
(13.1) is (2M(t)), which dominates (H_D(t)).  More generally, after the
last exit from levels (h,h-1,\ldots,a+1), the future path has height at
most (a), while the correction still has value (2a).  Between record
events its value is constant.  Thus at every time

\[
 2\sum_{i\in R(D),,i\le t}\operatorname{sgn}_D(i)
 \ge H_D(t),
\]

and (13.1) gives (H_E(t)\ge0).  Hence (E(D)) is Dyck.  The first-entry
up-steps and last-exit down-steps are all distinct, giving exactly (2h)
agreements.  \(□\)

Thus every height-(h) Dyck root satisfies the endpoint parity algebra of
an odd segment using only (2h+1) odd-support coordinates (including the
returned unmatched coordinate).  Height-bounded Dyck paths are counted
exactly by

\[
 [z^r]C_h(z).
                                                               \tag{13.3}
\]

For (h) on the order of (sqrt r), this is already a nonnegligible
fraction of the Catalan scale (as follows, for example, from the standard
finite-path transfer matrix for (11.1)).  Consequently no argument using
only

* the parity formula for the two endpoint states,
* the number of exceptional coordinates, and
* Dyck nonnegativity at the two endpoints

can prove the required Catalan packing bound in a Gaussian window.  The
intermediate first-maximum constraints in the word recursion (10.2) are
indispensable.  This is an endpoint-level obstruction, not a counterexample
to the actual PBBS theorem.

## 14. Exact peak-deletion renormalization

There is a further exact self-similarity which is invisible in the scalar
deficit ledger.  It does not by itself prove the Catalan packing theorem, but
it turns every prospective violation of the vacancy-gap bound into a smaller
PBBS passage problem.

Let a cyclic rank-\(r\) word \(w\) have distinguished unmatched zero \(u\),
so that cutting after \(u\) gives \(0D\) with \(D\) Dyck.  Put

\[
 k=\operatorname{pk}(D),\qquad d=r-k,
 \qquad p=N-2k=2d+1.                                  \tag{14.1}
\]

Call an edge of the coordinate cycle an **equality particle** when its two
endpoint bits agree.  There are exactly \(p\) such edges: each peak accounts
for one \(10\)-edge and cyclic balance gives equally many \(01\)-edges, so
the other \(N-2k\) edges are equal.  The edge immediately before \(u\) is a
\(00\)-particle and the edge immediately after \(u\) is unequal.

Label the equality particles in cyclic order.  Record on a particle the
common bit on its two endpoints.  Start at the particle immediately before
\(u\).  The resulting cyclic word has the form

\[
 0\,\partial D,                                      \tag{14.2}
\]

where \(\partial D\) is obtained from \(D\) by simultaneously deleting
every peak \(10\).

### Theorem 14.1 (PBBS renormalizes on equality particles)

The word \(\partial D\) is Dyck of semilength \(d\).  Under one PBBS
update of the original \(N\)-site state:

1. the distinguished equality particle moves forward by one physical edge;
2. every other equality particle stays on its physical edge;
3. the bit recorded on the distinguished particle remains zero, while all
   other recorded bits are complemented; and
4. the newly distinguished equality particle is the unique unmatched zero
   of the updated length-\(p\), rank-\(d\) particle word.

Consequently the recorded particle word evolves by the canonical PBBS map on
\(KG(p,d)\).

#### Proof

Write

\[
 D=1^{a_1}0^{b_1}\cdots1^{a_k}0^{b_k}.
\]

Deleting the last \(1\) and first \(0\) at every peak leaves

\[
 1^{a_1-1}0^{b_1-1}\cdots1^{a_k-1}0^{b_k-1},          \tag{14.3}
\]

with empty powers omitted.  This is exactly the sequence of common bits on
the equality edges after the distinguished root particle.  Simultaneous
deletion of peak pairs from a Dyck path leaves a Dyck path: deleting a local
\(10\) excursion changes neither endpoint height nor any height outside that
two-step excursion.  Its semilength is \(r-k=d\), proving (14.2).

The original PBBS update complements every bit except the unmatched zero
\(u\).  Hence an equality edge not incident with \(u\) stays equal and its
recorded bit is complemented.  The equality edge before \(u\) is \(00\) and
becomes unequal; the edge after \(u\) is \(01\) and becomes \(00\).  Thus the
distinguished particle moves from the former edge to the latter and keeps
recorded bit zero.  Its destination was not occupied by another equality
particle, so cyclic particle order is preserved.

Apply the first paragraph to the updated original state.  Its particle word,
rooted immediately before its new unmatched coordinate, again has a Dyck
tail.  Therefore that root particle is precisely the unique unmatched zero
of the particle word.  The recorded-bit update is complement-everything-
except-that-zero, which is the PBBS rule on \(KG(2d+1,d)\). \(\square\)

Label the equality particles persistently in cyclic order, and let
\(x_j(t)\in\mathbb Z_N\) be the physical edge occupied by particle \(j\) at
time \(t\).  If \(\kappa_t\) is the omitted label of the renormalized PBBS,
then Theorem 14.1 gives the exact skew system

\[
 \boxed{
 \begin{aligned}
  x_{\kappa_t}(t+1)&=x_{\kappa_t}(t)+1,\\
  x_j(t+1)&=x_j(t)\quad(j\ne\kappa_t),\\
  \lambda_t&=x_{\kappa_t}(t)+1.
 \end{aligned}}
                                                               \tag{14.4}
\]

All positions are read modulo \(N\); integer lifts may be chosen so that
particle order is preserved.

### Corollary 14.2 (a short return is an adjacent-particle passage)

Suppose \(\lambda_t=\lambda_{t+g}\), with no intervening occurrence of that
physical label, and \(g<N\).  If particle \(a=\kappa_t\) makes the first
entry into that physical edge, then

\[
 \boxed{\kappa_{t+g}=a-1\pmod p,}                    \tag{14.5}
\]

where \(a-1\) is the immediate predecessor in cyclic particle order.
Moreover particle \(a\) is selected at least once at an intermediate time.

#### Proof

After time \(t\), particle \(a\) occupies the edge labelled
\(\lambda_t\).  It must be selected again before that edge can be entered a
second time.  Equality particles never overtake.  Hence the next particle
which can enter the vacated edge is the immediate predecessor of \(a\).
The alternative in which \(a\) itself travels once around the physical
cycle uses at least \(N\) particle moves, impossible because \(g<N\).
This proves both assertions. \(\square\)

At this stage the formerly proposed vacancy-gap statement
\(g\ge p=2d+1\) becomes an adjacent-particle passage assertion in the smaller
PBBS.  Section 18 below explicitly disproves it.  The recursive reduction is
nevertheless useful: it proves the sharp height bound in Section 16 and gives
the complete gap-seven classification in Section 18.

## 15. Depth two is completely covered

Let \(B_i=A_{2i}\) be an original PBBS step-two Johnson cycle and put

\[
 C_i=B_i\cap B_{i+1},\qquad T_i=C_i\cap C_{i+1}.
                                                               \tag{15.1}
\]

The \(C_i\)'s are the depth-one lower colours, while

\[
 T_i=B_i\cap B_{i+1}\cap B_{i+2}                       \tag{15.2}
\]

is the depth-two target produced by the consecutive two-edge turn.  The
no-gap-three theorem says exactly that \(C_i\ne C_{i+1}\), and hence \(T_i\)
has the desired depth-two rank.  Coverage requires an additional
deficit-five argument, which is now available.

Write

\[
 \mu^{\rm turn}_2(S)=\#\{i:T_i=S\},\qquad
 M^{\rm turn}_2=\#\{S:\mu^{\rm turn}_2(S)=0\}.        \tag{15.3}
\]

### Theorem 15.1 (complete second PBBS turn shadow)

For the canonical PBBS on \(KG(2m+1,m)\), every
\(S\in\binom{[2m+1]}{m-2}\) occurs, and

\[
 \boxed{1\le\mu^{\rm turn}_2(S)\le10.}               \tag{15.4}
\]

#### Proof

Fix \(S\), and let \(U_+(S)\) and \(U_-(S)\) be its five forward and five
reverse unmatched zeros.  In physical circular order form a ten-symbol word:
write \(A_x\) for \(x\in U_+(S)\), \(C_x\) for
\(x\in U_-(S)\), and at a shared coordinate use the local order
\(C_x,A_x\).  The word contains five symbols of each kind, so it has a cyclic
transition

\[
 A_c,C_b.                                             \tag{15.5}
\]

An arbitrary \(A\to C\) transition need not work; this corrects the
earlier version of this proof.  Index the \(C\)-symbols cyclically and let
\(z_i\) be the number of \(A\)-symbols between consecutive \(C_i,C_{i+1}\).
Choose \(C_i\) at a global maximum of the prefix potential with increments
\(z_i-1\), as in Lemma 21.1.  Its preceding symbol is an \(A\), and at this
boundary there are at most one \(A\)-symbol before the next \(C\)-symbol and,
dually, at most one \(C\)-symbol before the previous \(A\)-symbol.

Let \(a\) be the next \(C\)-mark after \(C_b\), and let \(d\) be the
previous \(A\)-mark before \(A_c\).  Flipping \(b\) leaves the three old
forward marks immediately preceding \(b\) and the three old reverse marks
immediately succeeding \(b\).  The two corridor inequalities therefore make
\(A_c,C_a\) the surviving strict predecessor/successor pair.  The reversed
statement at \(c\) makes \(A_d,C_b\) the other pair.  The exact
deficit-three rule gives

\[
 f^2(S\cup\{a,b\})=S\cup\{b,c\},\qquad
 f^2(S\cup\{b,c\})=S\cup\{c,d\}.                   \tag{15.6}
\]

The three even-time states contain \(S\), and the no-gap-three theorem says
their intersection has rank exactly \(m-2\); it is therefore \(S\).  This
proves the lower bound in (15.4).  For the upper bound, a correct path deletes
two distinct labels from its initial state, both among the five reverse
unmatched zeros of \(S\).  That unordered pair determines the initial state
and hence the PBBS path, giving at most \(\binom52=10\) occurrences.
\(\square\)

For all sufficiently large \(m\), the depth-two balanced floor is one.  Put

\[
 R_2=W-\binom{2m+1}{m-2}
 ={6(m+1)W\over(m+2)(m+3)}<12\operatorname{Cat}_m.   \tag{15.7}
\]

Complete support and total mass give

\[
 \sum_S(\mu^{\rm turn}_2(S)-1)=R_2.                 \tag{15.8}
\]

Consequently the balanced overload and floor-corrected pair collision obey

\[
 \boxed{
  O_2(P_m)\le R_2<12\operatorname{Cat}_m,
  \qquad
  \sum_S\binom{\mu^{\rm turn}_2(S)-1}{2}
  \le4R_2<48\operatorname{Cat}_m.}                  \tag{15.9}
\]

The second inequality uses \(\mu-1\le9\) and
\(\binom{x}{2}\le4x\) for \(0\le x\le9\).  Thus both depth-two gates are
closed: every turn has the correct rank, every target occurs, and its total
overload/collision defect is Catalan.  The unresolved multidepth core now
begins genuinely at depth three.

## 16. Return gap dominates Dyck height

The renormalization theorem proves a pointwise restriction which is sharp but
still subcritical for the desired Gaussian-above window.

### Theorem 16.1 (height-gap theorem)

Let \((u,D)\) start a consecutive omitted-label return of odd gap \(g\) in
the PBBS on \(KG(2r+1,r)\).  Then

\[
 \boxed{g\ge 2\operatorname{ht}(D)+1.}               \tag{16.1}
\]

#### Proof

We induct on \(g\).  If \(g\ge N=2r+1\), then
\(\operatorname{ht}(D)\le r\le(g-1)/2\), so suppose \(g<N\).

Use the equality-particle PBBS of Theorem 14.1.  At the initial return edge,
particle \(a\) moves into the physical edge which is to be revisited.  By
Corollary 14.2, \(a\) must be selected again before the predecessor particle
can make the final entry.  Let \(h\) be its first subsequent selection time.
Then \(h\) is a consecutive omitted-label gap in the renormalized PBBS.
Same-label gaps are odd, and equality at gap one would repeat a factor state;
hence \(h\ge3\).  Also \(h<g\), and since both are odd,

\[
 h\le g-2.                                            \tag{16.2}
\]

The normalized Dyck root of the renormalized PBBS is \(\partial D\).
By induction (the case in which its circumference is at most \(h\) is
already covered by the first, trivial branch),

\[
 \operatorname{ht}(\partial D)\le {h-1\over2}.       \tag{16.3}
\]

Simultaneously deleting every peak from a nonempty Dyck path lowers its
height by exactly one.  This is immediate in the plane-tree contour
bijection: peaks are precisely leaf edges, and pruning every leaf lowers the
tree height by one.  Therefore

\[
 \operatorname{ht}(D)
 =\operatorname{ht}(\partial D)+1
 \le {h+1\over2}
 \le {g-1\over2},
\]

which is (16.1).  The induction starts because a gap-one return is
impossible. \(\square\)

For gap five the argument is sharper.  The intermediate return in the
renormalized PBBS must have gap three.  The no-gap-three theorem forces that
renormalized system to have rank one.  Hence every gap-five root satisfies

\[
 r-\operatorname{pk}(D)=1.                           \tag{16.4}
\]

This explains why the explicit family in Theorem 8.2 has only polynomial
Catalan mass despite its linear spatial-translate packing.

### Corollary 16.2 (sub-Gaussian Catalan packing)

If

\[
 H=o\!\left(\sqrt{r/\log r}\right),                  \tag{16.5}
\]

then the *total number*, not merely the maximum packing, of PBBS residence
intervals of length at most \(H\) is \(o(B)\).  In particular,

\[
 \boxed{\nu_H(P_r)=o(B).}                            \tag{16.6}
\]

#### Proof

A residence interval of length at most \(H\) comes from a gap at most
\(2H-1\).  Theorem 16.1 forces its normalized root to have height at most
\(H-1\).  The number of Dyck paths of semilength \(r\) and height at most
\(h\) is the number of length-\(2r\) closed walks from zero in the path graph
on \(\{0,1,\ldots,h\}\).  Its adjacency spectral radius is

\[
 2\cos{\pi\over h+2},
\]

so this number is at most

\[
 (2\cos(\pi/(h+2)))^{2r}
 \le 4^r\exp(-c r/h^2)                               \tag{16.7}
\]

for an absolute \(c>0\).  Every quotient root has exactly \(N\) physical
rotations.  Since \(B=\operatorname{Cat}_r\asymp4^r/r^{3/2}\), the ratio of
all possible short-return starts to \(B\) is at most

\[
 O\!\left(r^{5/2}e^{-c r/H^2}\right)=o(1)            \tag{16.8}
\]

under (16.5).  This proves (16.6). \(\square\)

Theorem 16.1 is sharp at the level of height: the recorded rank-six example
has height three and gap seven.  But typical Dyck height is of order
\(\sqrt r\), so (16.7) becomes useless when
\(H=\sqrt r\,\omega(r)\).  The remaining constant-one theorem must therefore
use packedness or a statistic stronger than height; endpoint parity and peak
pruning alone cannot reach the required window.

## 17. Exact deck reduction to a super-sparse Dyck-quotient packing

The spatial rotation deck can be removed completely after the short quotient
cycles are discarded.  This identifies the scale of the genuinely global
enumeration theorem.

Let \(\overline P_r\) be the quotient of the complement-projected step-two
factor by cyclic coordinate rotation.  Its directed edge set is naturally
indexed by the \(B\) Dyck roots, and its cycle permutation is
\(\tau=\phi^2\).  A physical short-return interval projects to a consecutive
edge interval in one \(\tau\)-cycle; the return criterion is independent of
the spatial phase, so every quotient interval has all \(N\) spatial lifts.

Call a quotient cycle **short** when its length is at most \(H+1\), the
largest number of projected transition edges in a residence-\(H\) interval.
Let \(Z_H\) be the number of quotient edges on short cycles.  On the other
cycles every relevant quotient interval is nonwrapping and uses distinct
quotient edges.  Let \(\overline\nu_H\) be the maximum cardinality of an
edge-disjoint family of these nonwrapping quotient intervals.

### Theorem 17.1 (deck packing/transversal equivalence)

Let \(\tau_H(P_r)\) be the minimum number of physical transition edges
meeting every residence-\(H\) interval.  Then

\[
 \boxed{
  N\overline\nu_H
  \le \nu_H(P_r)
  \le \tau_H(P_r)
  \le 2N\overline\nu_H+NZ_H .}
                                                               \tag{17.1}
\]

#### Proof

Choose an edge-disjoint quotient family of size \(\overline\nu_H\).  For one
member, its \(N\) spatial lifts use different physical edges above every
quotient edge in its trace, and hence are pairwise disjoint.  Lifts belonging
to two selected quotient intervals are also disjoint because their quotient
edge traces are disjoint.  This gives the first inequality in (17.1).

For the reverse direction, work on one long quotient cycle which contains at
least one short-return interval.  The circular interval packing--transversal
sandwich gives a quotient hitting set of size at most \(\bar\nu_C+1\).  Since
\(\bar\nu_C\ge1\), this is at most \(2\bar\nu_C\).  Lift every chosen quotient
edge through all \(N\) spatial phases.  The lifted set hits every physical
lift of every interval on that quotient cycle.  Summing over long cycles
costs at most \(2N\overline\nu_H\).  Finally, cutting every physical edge
above every short-cycle quotient edge costs \(NZ_H\) and hits all remaining
intervals.  This proves the last inequality; the middle inequality is the
elementary packing lower bound for a transversal. \(\square\)

The quotient short-cycle term is negligible throughout the intended PBBS
range.  Indeed, an ordered voltage itinerary of length \(q\) determines a
quotient \(\phi\)-cycle of period \(q\), so the number of quotient states on
cycles of period at most \(Q\) is at most \(QN^Q\).  A \(\tau\)-cycle of
length at most \(H+1\) comes from a \(\phi\)-cycle of length at most
\(2H+2\).  Hence

\[
 Z_H\le (2H+2)N^{2H+2}.                              \tag{17.2}
\]

If \(H\log N=o(r)\), in particular in (5.4), then

\[
 NZ_H=\exp(o(r))=o(B).                               \tag{17.3}
\]

### Corollary 17.2 (the exact quotient gate)

Uniformly when \(H\log N=o(r)\),

\[
 \boxed{
  \nu_H(P_r)=O(B)
  \quad\Longleftrightarrow\quad
  \overline\nu_H=O(B/N).}                           \tag{17.4}
\]

The implication from right to left uses (17.1)--(17.3); the converse uses
the first inequality of (17.1).

Thus a successful PBBS proof must establish an unexpectedly sparse global
fact inside the Dyck quotient: among its \(B\) transition edges, all
short-return intervals together have interval packing number only
\(O(B/N)\).  A single bad quotient interval on a long cycle already supplies
\(N\) disjoint physical intervals.  The explicit level-three obstruction is
harmless only because one quotient interval is still negligible compared
with \(B/N\).  Marginal voltage rarity, endpoint parity, and componentwise
estimates do not imply (17.4); the needed input is a cross-orbit clustering or
enumeration theorem at the precise \(1/N\) quotient scale.

## 18. Peak-defect vacancy is false: an all-dimensional gap-seven family

The stronger candidate

\[
 g\ge 2(r-\operatorname{pk}(D))+1                   \tag{18.1}
\]

is false.  The equality-particle recursion gives an explicit symbolic
counterfamily without search.

First classify defect-one roots.  For semilength \(d\), every Dyck path with
\(d-1\) peaks has a unique form

\[
 E(a,b,c)=(10)^a\,1(10)^b0\,(10)^c,                 \tag{18.2}
\]

where \(a,c\ge0\), \(b\ge1\), and \(a+b+c=d-1\).  Direct substitution in
(8.1) gives

\[
 \boxed{
  \phi E(a,b,c)=E(b-1,c+1,a),\qquad
  \delta(E(a,b,c))=2(a+1).}                         \tag{18.3}
\]

In particular this affine action has period three, and the three voltages are

\[
 2(a+1),\qquad2b,\qquad2(c+1),                       \tag{18.4}
\]

whose sum is \(2d+2=(2d+1)+1\).

Fix \(d\ge2\), put \(p=2d+1\), and take

\[
 E_d=E(d-2,1,0)=(10)^{d-2}1100.                    \tag{18.5}
\]

Starting its omitted particle label at zero, (18.3) gives the first eight
labels

\[
 0,\quad p-3,\quad p-1,\quad1,\quad p-2,\quad0,
 \quad2,\quad p-1.                                  \tag{18.6}
\]

Thus particle zero returns at time five, while its immediate cyclic
predecessor \(p-1\) is selected at times two and seven.

### Theorem 18.1 (gap seven with arbitrary peak defect)

Let \(d\ge2\) and \(r\ge2d-1\).  Put

\[
 D_{r,d}
 =(10)^{,r-(2d-1)}(1100)^{d-2}111000.              \tag{18.7}
\]

Then \(D_{r,d}\) is a Dyck word of semilength \(r\), has height three and
peak defect \(d\), and starts a consecutive PBBS omitted-label return of gap
seven.  Hence (18.1) fails whenever \(d\ge4\).  In particular it fails in
every semilength \(r\ge7\) by taking \(d=4\).

#### Proof

Every displayed block in (18.7) is Dyck, so the concatenation is Dyck and its
height is three.  It has

\[
 r-(2d-1)+(d-2)+1=r-d
\]

peaks, hence peak defect \(d\).  Simultaneous peak deletion gives

\[
 \partial D_{r,d}=(10)^{d-2}1100=E_d.               \tag{18.8}
\]

Because \(D_{r,d}\) ends in \(000\), the distinguished equality particle
and its immediate predecessor occupy adjacent physical edges.  Let the
returned physical coordinate be \(u\).  At time zero, particle zero moves
from edge \(u-1\) to edge \(u\).  By (18.6), particle \(p-1\) moves at time
two; it starts at edge \(u-2\), so it moves to \(u-1\).  Particle zero is not
selected again until time five, when it moves from \(u\) to \(u+1\).
Particle \(p-1\) is next selected at time seven and moves from \(u-1\) to
\(u\).  No particle can enter the occupied edge \(u\) earlier, and after time
five the predecessor already blocks it until time seven.  Equation (14.4)
therefore gives a consecutive physical omitted-label return exactly at gap
seven.

For \(d\ge4\), its proposed vacancy lower bound is \(2d+1\ge9>7\), proving
the counterexample. \(\square\)

Theorem 18.1 shows that no pointwise statistic depending only on peak defect,
the number of equality particles, or the first pruned core can establish the
mesoscopic residence estimate.  The true pointwise restriction (16.1) is
already sharp on a family with unbounded defect.  What remains in (17.4) is
therefore irreducibly an aggregate packing/clustering theorem over many Dyck
quotient cycles.

The gap-seven roots can in fact be classified and counted exactly.

### Theorem 18.2 (complete gap-seven classification)

A Dyck root \(D\) of semilength \(r\) starts a consecutive gap-seven return
if and only if, for some \(d\ge2\),

\[
 \boxed{
  \partial D=(10)^{d-2}1100
  \quad\text{and}\quad D\text{ ends in }00.}          \tag{18.9}
\]

Consequently the exact number of quotient roots starting a gap-seven return
is

\[
 \boxed{R_7(r)=2^{r-1}-r.}                           \tag{18.10}
\]

#### Proof

Suppose first that \(D\) starts a gap-seven return and let
\(E=\partial D\) be the equality-particle PBBS root of rank \(d\).  The
leading particle must be selected again before the final predecessor entry.
Its first repeat in the compressed PBBS has odd gap either three or five.

If that gap is three, the no-gap-three theorem forces \(d=1\).  But the
rank-one PBBS omitted labels advance cyclically by one on three labels, so at
time seven the selected label is the successor, not the predecessor, of the
initial label.  This contradicts Corollary 14.2.

Hence the compressed repeat has gap five.  As noted after Theorem 16.1, this
forces \(E\) to have defect one.  Write it as \(E(a,b,c)\) in (18.2).  The
first five voltages are the first two full-cycle voltages repeated after the
three-voltage sum \(p+1\).  Modulo \(p=2d+1\), their sum is

\[
 1+2(a+1)+2b=p-2c.                                  \tag{18.11}
\]

It vanishes exactly when \(c=0\).  After this return, the next two voltages
are \(2\) and \(2(a+1)\), so the selected particle is the predecessor at time
seven exactly when

\[
 2a+4=p-1=2d.                                       \tag{18.12}
\]

Thus \(a=d-2\), \(b=1\), proving the first condition in (18.9).

For this compressed root, the predecessor particle is selected exactly at
times two and seven.  It enters the original returned physical edge on its
second move if and only if it started immediately behind the distinguished
particle.  In the rooted word \(0D\), those two equality particles occupy
adjacent edges exactly when the last two bits of \(D\) are \(00\).  This
proves necessity.  The particle itinerary (18.6) proves the converse exactly
as in Theorem 18.1.

It remains to count.  Under the plane-tree contour bijection, \(\partial D\)
is obtained by pruning every leaf.  Fix a nonempty core tree \(T\) with
\(d\) edges and \(k\) leaves.  Every preimage is obtained by attaching new
leaf children in the ordered child slots of the \(d+1\) core vertices, with
at least one new child at each of the \(k\) core leaves.  Since the sum of
the numbers of child slots is

\[
 \sum_{v\in T}(\deg^+(v)+1)=2d+1,                   \tag{18.13}
\]

the attachment generating function is

\[
 {z^k\over(1-z)^{2d+1}}.                            \tag{18.14}
\]

For the core in (18.9), \(k=d-1\).  The terminal condition \(D\) ends in
\(00\) forbids new leaf children in the final root slot (the rightmost core
child is already nonleaf), reducing the exponent in (18.14) by one.  The
number of semilength-\(r\) preimages is therefore

\[
 [z^{r-d}]{z^{d-1}\over(1-z)^{2d}}
 =\binom r{2d-1}.                                    \tag{18.15}
\]

Summing over \(d\ge2\) gives the sum of all odd binomial coefficients except
\(\binom r1\):

\[
 R_7(r)=\sum_{d\ge2}\binom r{2d-1}=2^{r-1}-r.
\]

This proves (18.10). \(\square\)

### Corollary 18.3 (the exact exponential scale of gap-seven packing)

Let \(\nu^{(7)}(P_r)\) be the maximum number of pairwise projected-edge-
disjoint residence intervals arising specifically from gap-seven returns.
Then

\[
 \boxed{
 {N\over9}\bigl(2^{r-1}-r-O(N^{10})\bigr)
 \le \nu^{(7)}(P_r)
 \le N(2^{r-1}-r).}                                 \tag{18.16}
\]

In particular

\[
 \boxed{\nu^{(7)}(P_r)=\Theta(N2^r)=o(B).}           \tag{18.17}
\]

#### Proof

Every gap-seven quotient interval contains five consecutive projected
transition edges.  Quotient \(\tau\)-cycles of length at most five contain
only \(O(N^{10})\) quotient states by the voltage-itinerary estimate used in
(17.2).  On every remaining quotient cycle the intervals are ordinary
length-five intervals.  One such interval intersects intervals beginning at
at most nine possible quotient edges.  A greedy packing therefore selects at
least one ninth of all their starts.  Lifting each selected quotient interval
through all \(N\) phases gives the lower bound in (18.16), by Theorem 17.1.
The upper bound is simply the total number \(NR_7(r)\) of physical gap-seven
starts.  Finally \(B\asymp4^r/r^{3/2}\), which proves (18.17). \(\square\)

Thus gap seven already supplies exponentially many short returns and an
exponentially large physical packing, but only at base two rather than the
Catalan base four.  It is rigorously harmless for constant one.  Any genuine
obstruction to (17.4) must arise from gaps growing with \(r\), where the
iterated pruned cores have enough entropy to approach Catalan scale.

For reference, the same calculation gives an exact classification one gap
earlier.

### Corollary 18.4 (all gap-five roots)

A semilength-\(r\) Dyck root starts a consecutive gap-five return if and only
if

\[
 \boxed{D=(10)^a1(10)^b0,qquad a\ge0, b\ge1, a+b=r-1.}
                                                               \tag{18.18}
\]

Hence there are exactly \(r-1\) quotient roots and \(N(r-1)\) physical
gap-five starts.

#### Proof

The intermediate equality-particle return has gap three, so the pruned PBBS
has rank one; equivalently \(D\) has defect one.  Write \(D=E(a,b,c)\) as in
(18.2).  Equation (18.11) is the gap-five congruence and holds exactly when
\(c=0\).  The proper partial returns are excluded by the odd-gap rule and the
no-gap-three theorem.  There are \(r-1\) pairs \((a,b)\). \(\square\)

At rank depth three, gap three is absent and every gap-five start contributes
one unit to the PBBS intersection-rank excess.  Therefore

\[
 \boxed{E_3(P_r)=N(r-1).}                            \tag{18.19}
\]

This is polynomial, hence much smaller than the Catalan scale.  Thus the
depth-three rank gate is also closed after polynomially many local cuts; its
target-support question is separate, just as depth-two support required the
deficit-five theorem in Section 15.

## 19. A literal five-rank PBBS word

The complete depth-two support theorem is already strong enough to produce a
genuine contiguous-OR word for five consecutive ranks, with no separate
factorability or pin-survival hypothesis.

### Theorem 19.1 (literal depth-two PBBS conversion)

Put \(n=2m+1\) and \(W=\binom{n}{m}\).  For every \(m\ge2\), there is a
nonzero contiguous-OR word of length at most

\[
 \boxed{W+4\operatorname{Cat}_m}                    \tag{19.1}
\]

which covers every set in the five ranks

\[
 \boxed{m-1,m,m+1,m+2,m+3.}                         \tag{19.2}
\]

In particular its length is \(W+O(W/m)\).

#### Proof

Let \((A_i)\) run over the PBBS odd-graph factor on the rank-\(m\) sets,
and put \(X_i=[n]\setminus A_i\).  The step-two sequences

\[
 \ldots,X_i,X_{i+2},X_{i+4},\ldots                  \tag{19.3}
\]

form disjoint Johnson cycles on rank \(m+1\).  Consecutive occurrences of an
omitted label have gap at least five.  By the residence calculation (1.3),
every positive coordinate run in every cycle (19.3) therefore has at least
three vertices.

On one such cycle, reindex consecutive vertices as
\(X_0,\ldots,X_{L-1}\), cyclically, and define

\[
 D_i=X_i\cap X_{i+1}\cap X_{i+2}.                   \tag{19.4}
\]

Emit

\[
 D_0,D_1,\ldots,D_{L-1},D_0,D_1,D_2,D_3.            \tag{19.5}
\]

For a fixed coordinate, its indicator on the \(X\)-cycle is a union of
cyclic one-runs of length at least three.  Taking the indicators in (19.4)
erodes every run by two positions.  Dilating back by unions of consecutive
entries gives, pointwise and hence as set identities,

\[
\begin{aligned}
D_i&=X_i\cap X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2},\\
D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2},\\
D_i\cup\cdots\cup D_{i+3}&=X_{i+2}\cup X_{i+3},\\
D_i\cup\cdots\cup D_{i+4}&=X_{i+2}\cup X_{i+3}\cup X_{i+4}.
                                                               \tag{19.6}
\end{aligned}
\]

The four repeated entries in (19.5) expose all windows crossing the cyclic
seam.

It remains to identify the five target families.  Restoring the original
PBBS indices, disjointness of adjacent odd-graph states gives

\[
\begin{aligned}
X_i\cap X_{i+2}\cap X_{i+4}
 &=A_{i+1}\cap A_{i+3},\\
X_i\cap X_{i+2}
 &=[n]\setminus(A_i\cup A_{i+2})=A_{i+1},\\
X_i&=[n]\setminus A_i,\\
X_i\cup X_{i+2}
 &=[n]\setminus(A_i\cap A_{i+2}),\\
X_i\cup X_{i+2}\cup X_{i+4}
 &=[n]\setminus(A_i\cap A_{i+2}\cap A_{i+4}).       \tag{19.7}
\end{aligned}
\]

The first equality uses the correct rank supplied by no gap three; the
containment is immediate from adjacent disjointness and both sides have size
\(m-1\).  The PBBS complete first-shadow theorem says the two-state
intersections in (19.7) cover every rank-\((m-1)\) set.  Theorem 15.1 says
the three-state intersections cover every rank-\((m-2)\) set.  Complements
and the middle ownership of the factor therefore show that the five lines of
(19.6) cover respectively every set of ranks

\[
 m-1,m,m+1,m+2,m+3.
\]

All entries \(D_i\) have size \(m-1\), so they are nonzero.  Finally, a PBBS
component of length \(\ell N\) gives at most \(\ell\) step-two cycles, and
the sum of all levels \(\ell\) is \(W/N=\operatorname{Cat}_m\).  Thus the
number of words (19.5) is at most \(\operatorname{Cat}_m\).  Their unextended
parts contain exactly \(W\) entries, and the four seam entries per cycle cost
at most \(4\operatorname{Cat}_m\).  Concatenating the words proves (19.1).
\(\square\)

This is a genuine depth-two result: rank correctness, complete lower and
upper shadows, erosion factorization, coordinate residence, and cyclic seam
repair are all proved.  It upgrades the earlier three-rank first-band theorem
to five ranks in one parity.  It still does not address a growing central
band, so it does not by itself prove constant one.

## 20. A literal seven-rank PBBS word

The complete third-turn support theorem gives one further exact band.  At
this depth four-fold erosion is not everywhere invertible: a projected
coordinate can have a positive run of length three.  The obstruction is
nevertheless negligible, because such runs are exactly the gap-five returns
classified in Corollary 18.4.

### Theorem 20.1 (literal depth-three PBBS conversion)

Put \(n=2m+1\), \(W=\binom{n}{m}\), and assume \(m\ge3\).  There is a
nonzero contiguous-OR word of length at most

\[
 \boxed{
 W+6\operatorname{Cat}_m+21(2m+1)(m-1)}              \tag{20.1}
\]

which covers every set in the seven ranks

\[
 \boxed{m-2,m-1,m,m+1,m+2,m+3,m+4.}                 \tag{20.2}
\]

In particular its length is \(W+O(W/m)\).

#### Proof

Use the complement-projected step-two PBBS cycles \(X_i=[n]\setminus A_i\)
from Theorem 19.1, and on one such cycle reindex consecutive vertices as
\(X_0,\ldots,X_{L-1}\).  Put

\[
 D_i=X_i\cap X_{i+1}\cap X_{i+2}\cap X_{i+3}.       \tag{20.3}
\]

The identity \(X_i\cap X_{i+1}=A_{i+1}\), with the old PBBS indices
restored, shows more generally that \(D_i\) is the intersection of three
consecutive states on the interleaved step-two \(A\)-cycle.  The pointwise
depth-two rank theorem therefore gives

\[
 |D_i|=m-2,                                           \tag{20.4}
\]

so every emitted entry is nonzero.

Emit around this cycle

\[
 D_0,D_1,\ldots,D_{L-1},D_0,D_1,\ldots,D_5.          \tag{20.5}
\]

First suppose a fixed coordinate has no positive \(X\)-run of length three.
Every positive run then has length at least four.  Four-fold erosion followed
by dilation gives, pointwise and hence as set identities,

\[
\begin{aligned}
D_i&=X_i\cap X_{i+1}\cap X_{i+2}\cap X_{i+3},\\
D_i\cup D_{i+1}&=X_{i+1}\cap X_{i+2}\cap X_{i+3},\\
D_i\cup D_{i+1}\cup D_{i+2}&=X_{i+2}\cap X_{i+3},\\
D_i\cup\cdots\cup D_{i+3}&=X_{i+3},\\
D_i\cup\cdots\cup D_{i+4}&=X_{i+3}\cup X_{i+4},\\
D_i\cup\cdots\cup D_{i+5}&=X_{i+3}\cup X_{i+4}\cup X_{i+5},\\
D_i\cup\cdots\cup D_{i+6}&=X_{i+3}\cup X_{i+4}\cup X_{i+5}\cup X_{i+6}.
                                                               \tag{20.6}
\end{aligned}
\]

A positive run of length three is erased completely by (20.3).  For that
coordinate it spoils at most respectively

\[
 1,2,3,4,5,6                                           \tag{20.7}
\]

of the windows on the last six lines of (20.6), and none on the first line.
Thus it creates at most \(21\) bad intended windows.  For every intended
window on which (20.6) fails, append its right-hand-side target literally.

By (1.3), positive projected runs of length three are in bijection with
consecutive omitted-label gaps of length five.  Corollary 18.4 counts exactly

\[
 (2m+1)(m-1)                                           \tag{20.8}
\]

such starts.  Hence all literal repairs together cost at most the last term
in (20.1).

It remains to identify the intended target families.  With the original
indices restored, the first four lines of (20.6) are respectively

\[
\begin{aligned}
X_i\cap X_{i+2}\cap X_{i+4}\cap X_{i+6}
  &=A_{i+1}\cap A_{i+3}\cap A_{i+5},\\
X_i\cap X_{i+2}\cap X_{i+4}
  &=A_{i+1}\cap A_{i+3},\\
X_i\cap X_{i+2}&=A_{i+1},\\
X_i&=[n]\setminus A_i.                                \tag{20.9}
\end{aligned}
\]

The last three lines are complements of, respectively, two-, three-, and
four-state intersections on the other step-two (A)-cycle.  Complete
depth-one support, Theorem 15.1, and the complete third-turn support theorem
therefore show that the seven right-hand sides cover every set in the ranks
listed in (20.2).  At depth three we use only the correct-rank four-state
occurrences supplied by that theorem; if one of their intended windows is
bad, it was included in the literal repair above.

The unextended cycle words contain exactly \(W\) entries in total.  As in
Theorem 19.1, the number of step-two cycles is at most
\(\operatorname{Cat}_m\), and six repeated entries per cycle expose every
window crossing a seam.  Adding the repair bound proves (20.1).  \(\square\)

Theorem 20.1 settles literal factorability through depth three.  It remains
a fixed-depth theorem: constant one still requires an analogue for a band
whose depth tends past the Gaussian scale.

## 21. Every PBBS turn shadow has complete support

The fixed-label ladder is false for an arbitrary \(A\to C\) boundary; an
explicit counterexample is recorded in
PBBS_GENERAL_MARK_LADDER_AUDIT_20260725.md.  The stronger global-maximum
boundary in Lemma 21.1 avoids that obstruction.  Independent targeted
audits of both its forward and reverse surviving-mark calculations, including
shared coordinates, verify the proof below.

Thus the target-support question is removed at every depth.  The remaining
constant-one obstruction is the physical residence/erosion cost.

Fix \(1\le q\le m\) and

\[
 S\in\binom{[2m+1]}{m-q}.
\]

The word of \(S\) has \(d=2q+1\) forward-unmatched zeros and \(d\)
reverse-unmatched zeros.  Form their expanded circular word by writing
\(A_x\) at every forward mark and \(C_x\) at every reverse mark, with the
local order \(C_x,A_x\) at a shared coordinate.

### Lemma 21.1 (global-maximum two-sided corridor)

There is an \(A_0,C_0\) boundary such that, if
\(C_0,C_1,\ldots,C_{d-1}\) are the \(C\)-symbols in forward order and
\(A_0,A_1,\ldots,A_{d-1}\) are the \(A\)-symbols in backward order, then

\[
\begin{aligned}
x_j&:=\#\{\text{\(A\)-symbols strictly between \(C_0\) and \(C_j\)}\}
     \le j,\\
y_j&:=\#\{\text{\(C\)-symbols met backwards from \(A_0\) to \(A_j\)}\}
     \le j
\end{aligned}                                                   \tag{21.1}
\]

for every \(1\le j\le d-1\).

#### Proof

Index the \(C\)-symbols cyclically and put

\[
 z_i=\#\{\text{\(A\)-symbols strictly between \(C_i\) and \(C_{i+1}\)}\}.
\]

Then \(\sum_i z_i=d\).  Define a periodic prefix potential by

\[
 H(i+1)-H(i)=z_i-1.                                  \tag{21.2}
\]

Choose \(i\) at a global maximum of \(H\).  Since
\(H(i)-H(i-1)=z_{i-1}-1\ge0\), the gap before \(C_i\) contains an
\(A\)-symbol, and its final symbol supplies the required \(A_0,C_0\)
boundary.  For every \(j\ge1\),

\[
 \sum_{h=0}^{j-1}z_{i+h}-j=H(i+j)-H(i)\le0,           \tag{21.3}
\]

which is \(x_j\le j\).

For the reverse inequality, the \(L\) gaps immediately preceding \(C_i\)
contain

\[
 \sum_{h=1}^{L}z_{i-h}
 =d-\sum_{h=0}^{d-L-1}z_{i+h}\ge L.                  \tag{21.4}
\]

Taking \(L=j+1\), the current gap and the preceding \(j\) gaps contain at
least \(j+1\) \(A\)-symbols.  Starting at the final \(A\)-symbol of the
current gap, the \(j\)-th previous \(A\)-symbol is therefore reached after
crossing at most \(j\) \(C\)-symbols.  Thus \(y_j\le j\).  \(\square\)

### Theorem 21.2 (complete correct PBBS support at every depth)

For every \(1\le q\le m\) and every
\(S\in\binom{[2m+1]}{m-q}\), there is a canonically oriented \(q\)-edge
path under \(g=f^2\),

\[
 B_0\longrightarrow B_1\longrightarrow\cdots\longrightarrow B_q,
\]

such that

\[
 \boxed{\bigcap_{t=0}^{q}B_t=S.}                     \tag{21.5}
\]

Moreover the number of correct-rank occurrences satisfies

\[
 \boxed{
 1\le\mu_{P,q}^{\mathrm{corr}}(S)\le\binom{2q+1}{q}.} \tag{21.6}
\]

#### Proof

Use the boundary from Lemma 21.1 and define

\[
 P_t=
 \{C_0,\ldots,C_{q-t-1}\}
 \cup
 \{A_0,\ldots,A_{t-1}\},
 \qquad0\le t\le q.                                  \tag{21.7}
\]

We prove that \(B_t=S\cup P_t\) are the required states.  Fix
\(0\le t<q\), put \(r=q-t-1\), and let

\[
 K_t=S\cup\{C_0,\ldots,C_{r-1}\}
          \cup\{A_0,\ldots,A_{t-1}\}.                \tag{21.8}
\]

This is the proposed common rank-\((m-1)\) core of \(B_t,B_{t+1}\).
Write the forward marks as

\[
 F_0=A_0,F_1,\ldots,F_{d-1},
 \qquad A_j=F_{d-j}.
\]

Process the flips \(C_0,\ldots,C_{r-1}\).  Inductively, the first \(j\)
flips remove \(F_1,\ldots,F_{2j}\): before \(C_j\) is flipped,
\(x_j\le j\le2j\) says every old forward mark preceding it has already
been removed, so its flip removes the next two surviving marks
\(F_{2j+1},F_{2j+2}\).  The selected cyclically consecutive marks
\(A_0,\ldots,A_{t-1}\) then remove themselves and the next \(t\)
surviving marks.  Exactly

\[
 U_+(K_t)=\{A_t,A_{t+1},A_{t+2}\}                   \tag{21.9}
\]

remain.  The inequality \(x_r\le r\le2r\) makes \(A_t\) the strict
predecessor of \(C_r\) in this triple.  The reversed argument gives

\[
 U_-(K_t)=\{C_r,C_{r+1},C_{r+2}\},                  \tag{21.10}
\]

with \(C_r\) the strict successor of \(A_t\).  The exact deficit-three
predecessor/successor law now gives

\[
 g(K_t\cup\{C_r\})=K_t\cup\{A_t\},                  \tag{21.11}
\]

which is the \(t\)-th arrow.

It remains only to exclude collisions between selected \(A\)- and
\(C\)-labels.  If \(C_j=A_h\), the forced local order \(C_x,A_x\) gives

\[
 d-h-1=x_j\le j.                                    \tag{21.12}
\]

This is incompatible with \(j+h\le q-1\).  Hence no coordinate is
duplicated inside a \(P_t\), and none belongs to every \(P_t\).  Thus every
\(|P_t|=q\) and \(\bigcap_tP_t=\varnothing\), proving (21.5).

For the cap, the \(q\) labels deleted from the initial state are distinct
members of the \(2q+1\) reverse-unmatched zeros of \(S\), and determine the
oriented PBBS path.  This gives (21.6).  \(\square\)

Theorem 21.2 is an all-depth support theorem, but not yet an all-depth
literal word.  To erode by \(q+1\) consecutive projected owners and dilate
back, every positive coordinate run shorter than \(q+1\) must be cut or
repaired.  By (0.1), the exact remaining assertion is still

\[
 \nu_H(P_m)=O\!\left(\frac{W}{m}\right)
\]

for \(H=\sqrt m\,\omega(m)\), equivalently the quotient packing bound
\(\overline\nu_H=O(\operatorname{Cat}_m/(2m+1))\) from Corollary 17.2.

The preceding (O(W/m)) target belongs to the pair-omission residence
architecture studied earlier in this note.  For a direct all-depth
erosion of the PBBS turn shadows, cut repair carries a quadratic-in-(H)
toll.  The following fixed-window little-oh formulation is a clean
residence-only sufficient theorem for the literal constant-one problem.

## 22. Fixed-window residence packing implies constant one

Put

\[
 B_m=\operatorname{Cat}_m=\frac{W}{2m+1},
 \qquad H_A=\lceil A\sqrt m\rceil .                 \tag{22.1}
\]

Consider the following statement for each fixed \(A>0\):

\[
 \boxed{\nu_{H_A}(P_m)=o_A(B_m).}                   \tag{RP_A}
\]

Here the little-oh is as \(m\to\infty\), with \(A\) fixed.  No uniformity
in \(A\) is required.

### Lemma 22.1 (exact endpoint-capped erosion)

Let

\[
 X_0,X_1,\ldots,X_{v-1}
\]

be a directed Johnson path of rank-\((m+1)\) owners.  Assume every
internally bounded positive coordinate run has at least \(H+1\) owners.
Extend the path constantly at its endpoints:

\[
 \widetilde X_i=
 \begin{cases}
 X_0,&i<0,\\
 X_i,&0\le i<v,\\
 X_{v-1},&i\ge v.
 \end{cases}
\]

For \(-H\le i\le v-1\), put

\[
 D_i=\bigcap_{j=0}^{H}\widetilde X_{i+j}.            \tag{22.2}
\]

Then the word

\[
 D_{-H},D_{-H+1},\ldots,D_{v-1}                     \tag{22.3}
\]

has length \(v+H\), all its entries are nonempty, and it represents every
intersection and every union of at most \(H+1\) consecutive owners lying
wholly in the path.

More exactly, for \(1\le t\le H+1\),

\[
 \bigcup_{a=0}^{t-1}D_{i+a}
 =\bigcap_{a=t-1}^{H}\widetilde X_{i+a},             \tag{22.4}
\]

and, for \(0\le s\le H\),

\[
 \bigcup_{a=0}^{H+s}D_{i+a}
 =\bigcup_{a=H}^{H+s}\widetilde X_{i+a}.             \tag{22.5}
\]

#### Proof

Fix one coordinate.  Constant endpoint extension makes every positive run
touching an endpoint infinite, while every internally bounded positive run
has length at least \(H+1\).  The indicator of \(D_i\) is the ordinary
\((H+1)\)-fold erosion of this binary run sequence.  Unions of \(t\)
consecutive eroded indicators dilate it back by \(t-1\) positions.  On
each positive run this gives exactly (22.4) for \(t\le H+1\), and then
(22.5) for the following \(H\) dilations.  The identities are coordinatewise,
hence are set identities.

For an intersection \(X_b\cap\cdots\cap X_{b+p-1}\), choose
\(t=H-p+2\) and \(i=b-H+p-1\) in (22.4).  For a union
\(X_b\cup\cdots\cup X_{b+p-1}\), choose \(s=p-1\) and \(i=b-H\) in
(22.5).  The inequalities \(1\le p\le H+1\) and
\(0\le b\le b+p-1<v\) put all required \(D\)-indices in
\([-H,v-1]\).

Finally, an intersection of \(H+1\) consecutive rank-\((m+1)\) Johnson
owners loses at most one coordinate per transition, and therefore has size
at least \(m+1-H>0\).  Endpoint repetitions only increase it.  Thus every
entry in (22.3) is nonzero.  \(\square\)

### Theorem 22.2 (residence-only constant-one reduction)

If \((\mathrm{RP}_A)\) holds for every fixed \(A>0\), then

\[
 \boxed{\nu(k)\le(1+o(1))
        \binom{k}{\lfloor k/2\rfloor}.}             \tag{22.6}
\]

#### Proof

Work first in odd dimension \(n=2m+1\).  Use the complement-projected
step-two PBBS Johnson cycles \(X_i=[n]\setminus A_i\), of rank \(m+1\).
Their total number \(c_2(P_m)\) is at most \(B_m\), and their total number
of vertices is \(W\).

Fix \(H<m\).  Call a projected cycle *good* if it has no positive
coordinate residence of length at most \(H\).  On a good cycle of length
\(L\), use the cyclic \(H\)-fold erosion

\[
 D_i=\bigcap_{j=0}^{H}X_{i+j}
\]

and repeat its first (2H) entries.  The erosion--dilation identities
give a literal word of length (L+2H) exposing every intended lower
intersection and upper union through depth (H), including those crossing
the cyclic seam.

Now let \(C\) be a bad cycle.  Choose a transversal of its short residence
intervals.  By Theorem 2.1 it has size

\[
 \tau_H(C)\le\nu_H(C)+1\le2\nu_H(C),               \tag{22.7}
\]

because a bad cycle has \(\nu_H(C)\ge1\).  Cut at those transition
edges.  Every resulting path has no short internal positive run, so the
endpoint-capped erosion theorem applies.  The erosion entries cost
\(L+H\tau_H(C)\).  At one cut, at depth \(q\), at most \(q\) lower and
\(q\) upper intended windows are destroyed.  Appending every destroyed
target literally therefore costs at most

\[
 2\sum_{q=1}^{H}q=H(H+1)                            \tag{22.8}
\]

per cut.  Thus the complete bad-cycle cost is at most

\[
 L+(H^2+2H)\tau_H(C)
 \le L+2(H^2+2H)\nu_H(C).                          \tag{22.9}
\]

Summing good and bad cycles yields a literal central-band word of length

\[
 \boxed{
 W+2HB_m+2(H^2+2H)\nu_H(P_m).}                     \tag{22.10}
\]

All its entries are nonempty, since an \(H\)-edge Johnson window can lose
at most \(H\) coordinates from a rank-\((m+1)\) owner and \(H<m\).

Before cutting, the intended lower families are consecutive intersections
of projected owners, hence shifted consecutive intersections of PBBS middle
states.  The intended upper families are their complements.  Theorem 21.2
supplies every correct lower target at every depth, and hence also every
complementary upper target.  The literal repair counted in (22.8) restores
every intended occurrence destroyed by cutting.  Consequently the word in
(22.10) covers all ranks

\[
 m+1-H,m+2-H,\ldots,m+1+H.                         \tag{22.11}
\]

For fixed \(A\), take \(H=H_A\).  Under \((\mathrm{RP}_A)\), the two
normalized excesses in (22.10) satisfy

\[
 \frac{HB_m}{W}=O_A(m^{-1/2})=o_A(1),
 \qquad
 \frac{H^2\nu_H(P_m)}{W}=o_A(1).                  \tag{22.12}
\]

We now diagonalize.  For each positive integer \(j\), choose \(M_j\) so
large that for \(m\ge M_j\),

\[
 \nu_{\lceil j\sqrt m\rceil}(P_m)\le B_m/j^4,
 \qquad m\ge j^4.                                  \tag{22.13}
\]

Increase the \(M_j\)'s further so that the already proved product-SCD tail
word outside the depth-\(j\sqrt m\) band has normalized length tending to
zero as \(j\to\infty\).  Put \(a(m)=j\) on
\(M_j\le m<M_{j+1}\) and \(H_m=\lceil a(m)\sqrt m\rceil\).  Then

\[
 a(m)\to\infty,\qquad H_m=o(m),                    \tag{22.14}
\]

and (22.10), (22.13) give

\[
 \frac{2H_mB_m+2(H_m^2+2H_m)\nu_{H_m}(P_m)}{W}
 =O\!\left(\frac{a(m)}{\sqrt m}+\frac1{a(m)^2}\right)
 =o(1).                                             \tag{22.15}
\]

Appending the product-SCD tail word therefore covers every remaining rank
at cost \(o(W)\).  This proves (22.6) in odd dimension.  The standard
trimmed one-coordinate lift transfers the same leading constant to even
dimension. \(\square\)

Theorem 22.2 removes every shadow-support and multiplicity issue, but its
singleton repair is not optimal.  Section 24 replaces the quadratic term
in (22.10) by a linear cut seam; the resulting sufficient packing gate is
big-oh Catalan rather than little-oh Catalan.

## 23. Retraction of a proposed zero-winding converse

An attempted converse asserted that \(d(D)=1\) forces the next omitted-label
return to have gap \(2\operatorname{ht}(D)+1\).  That assertion and the
resulting claimed counterexample to \((\mathrm{RP}_A)\) are **retracted**.

The error was in a proposed first-deepest-spine sector shift: after applying
\(\tau\), a transported \(A_i\)-forest can become the new first deepest
branch.  Controlling only the transported \(B_i\)-forests does not preserve
the displayed spine.

A concrete counterexample is

\[
 D=1110011000.
 \tag{23.1}
\]

It has \(d(D)=1\), but its quotient orbit has

\[
 (\delta,d)=(3,1),(3,5),(7,1)
 \tag{23.2}
\]

and returns to \(D\).  At the proposed height time the cumulative deficit
is not the terminal first-maximum position, so the claimed return does not
occur.  A second example is

\[
 D=11100011110000,
 \tag{23.3}
\]

whose \(\tau\)-orbit has deficits \((1,1,7)\) and first-maximum positions
\((10,4,4)\); again the claimed gap fails.

The converse also fails inside the primitive family used in the attempted
Catalan lower bound.  The primitive root

\[
 D=1111100001110000
 \tag{23.4}
\]

has height five and \(d(D)=1\), but its five-state \(\tau\)-cycle has
deficits \((1,1,1,7,1)\) and first-maximum positions
\((11,5,5,5,11)\) in cycle order.  Starting at the displayed root, the
five deficits sum to \(11\) while the terminal first-maximum position is
\(5\), so there is no gap-eleven return.

The path-graph estimate showing that primitive height-\(O(\sqrt r)\) roots
have positive Catalan mass is correct, but the primitive counterexample
shows that it yields no residence lower bound.  Therefore
\((\mathrm{RP}_A)\) is currently neither proved nor disproved.  The
independent counteraudit is recorded in
PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md.

## 24. Linear dominance-staircase seams and the weakened packing gate

The \(H(H+1)\) literal-repair term in (22.8) is not intrinsic. Fix one
cut between adjacent rank-\((m+1)\) owners \(X_{-1},X_0\), and assume
\(2H\le m+1\). For \(1\le s,t\le H\), set

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i,
 \qquad C=X_{-1}\cap X_0.
\tag{24.1}
\]

For each \(x\in C\), let \(u_x,v_x\in[H]\) be the capped left and right
lengths of its positive run through the cut. Then

\[
 P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.
\tag{24.2}
\]

Call \(P_{s,t}\) floor-correct when
\(|P_{s,t}|=m+2-s-t\).

### Lemma 24.1 (southwest exclusion)

If \(P_{s,t}\) is floor-correct, there is no \(x\in C\) with
\(u_x<s\) and \(v_x<t\).

#### Proof

The window in (24.1) has \(s+t-1\) Johnson transitions. Map each
coordinate of \(X_{-s}\setminus P_{s,t}\) to its first departure
transition. This is injective. A coordinate with both strict extent
inequalities has an internal arrival and a later internal departure; that
later departure is not the first departure of any initial coordinate.
Hence at most \(s+t-2\) transitions occur in the injection, which gives
\(|P_{s,t}|\ge m+3-s-t\), a contradiction. \(\square\)

Take the Pareto-minimal points among the distinct pairs \((u_x,v_x)\).
Join them, in increasing first and decreasing second coordinate, by a
southeast unit lattice path \(\Gamma\) from \((1,H)\) to \((H,1)\), moving
east before south between consecutive minima. It has exactly \(2H-1\)
vertices. Emit the set-letter \(P_z\) at every vertex \(z\) of \(\Gamma\).

### Lemma 24.2 (linear lower chart)

For every floor-correct \(q=(s,t)\),

\[
 \boxed{
 P_q=\bigcup_{\substack{z\in V(\Gamma)\\z\ge q}}P_z.}
\tag{24.3}
\]

The selected vertices form one contiguous subpath, and every emitted
letter is nonempty.

#### Proof

Monotonicity of the two coordinates along \(\Gamma\) makes the selected
vertices contiguous, and (24.2) gives one inclusion. Conversely, if
\(x\in P_q\), choose a Pareto-minimal extent point below
\((u_x,v_x)\). Lemma 24.1 excludes the strictly southwest case. The
east-before-south convention then forces \(\Gamma\) to meet the rectangle
\([q,(u_x,v_x)]\); at such a vertex \(z\), (24.2) gives \(x\in P_z\).
Finally \(P_z\) intersects at most \(2H\) owners, so its size is at least
\(m+2-2H\ge1\). \(\square\)

The literal owner word

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}
\tag{24.4}
\]

has length \(2H\) and represents every crossing upper union of at most
\(H+1\) owners. Concatenating (24.3) and (24.4) gives a nonzero one-cut
chart of exact length

\[
 \boxed{4H-1.}
\tag{24.5}
\]

If a cycle of length \(L\) is opened at a residence transversal of size
\(J\), endpoint-capped erosion costs \(L+HJ\), and the charts cost
\((4H-1)J\). Thus its complete cost is

\[
 \boxed{L+(5H-1)J.}
\tag{24.6}
\]

Taking a minimum transversal on every active projected cycle and using
\(J\le2\nu_H\), while inactive cycles retain their cyclic \(2H\) collars,
gives the global central-band ledger

\[
 \boxed{
 L_H\le W+2HB_m+2(5H-1)\nu_H(P_m).}
\tag{24.7}
\]

### Theorem 24.3 (Catalan-order residence packing suffices)

Suppose that for every fixed \(A>0\), with
\(H_A=\lceil A\sqrt m\rceil\),

\[
 \boxed{\nu_{H_A}(P_m)=O_A(B_m).}
\tag{CP_A}
\]

Then

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\tag{24.8}
\]

#### Proof

For fixed \(A\), (24.7) has excess
\(O_A(H_AB_m)=O_A(W/\sqrt m)=o_A(W)\). Diagonalize over integer
\(A\to\infty\) slowly enough to absorb the implicit constants in
\((CP_A)\), append the proved product-SCD tail, and use the trimmed
one-coordinate lift for the other parity, exactly as in Theorem 22.2.
\(\square\)

After discarding the negligible short quotient cycles, \((CP_A)\) is
equivalent, up to absolute factors, to

\[
 \boxed{
 \overline\nu_{H_A}=O_A\!\left({B_m\over2m+1}\right).}
\tag{24.9}
\]

This big-oh Catalan packing statement is a convenient strong sufficient
input, but the linear ledger (24.7) permits the following weaker threshold.

### Theorem 24.4 (critical reciprocal-height packing suffices)

Suppose that, for every fixed \(A>0\),

\[
 \boxed{\nu_{H_A}(P_m)=o_A(B_m\sqrt m).}
\tag{ST_A}
\]

Then (24.8) holds. Equivalently, after discarding the negligible short
quotient cycles,

\[
 \boxed{\overline\nu_{H_A}=o_A(B_m/\sqrt m).}
\tag{QST_A}
\]

#### Proof

The last term of (24.7) is
\(O_A(\sqrt m)\,o_A(B_m\sqrt m)=o_A(mB_m)=o_A(W)\),
and the collar term is already \(o_A(W)\). The same diagonal tail and
parity argument as Theorem 24.3 completes the proof. The deck equivalence
uses the exact long-cycle inequalities
\(N\overline\nu_H\le\nu_H\le2N\overline\nu_H+NZ_H\), with
\(NZ_{H_A}=\exp(o(m))\).
\(\square\)

The height-gap theorem and the exact Dyck height spectrum already give

\[
 \overline\nu_{H_A}=O_A(B_m/\sqrt m).
\tag{24.10}
\]

Thus the sharp remaining input of the separate-cut architecture is only a
vanishing improvement over reciprocal-height saturation.  The stronger
\((CP_A)\) remains useful for the fixed-core completion route.  The
complete independent seam proof is recorded in
MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md, and the corrected
threshold audit in MATH_ATTACK_L_CORRECTED_CHRONOLOGY_TRACE_GATE_20260725.md.

## 25. Reduction to simple fixed-core open-wreath sectors

Call a consecutive omitted-label return of gap \(2s+1\) **simple** when
its half-open label list

\[
 \lambda_0,\lambda_1,\ldots,\lambda_{2s}
\]

is pairwise distinct.  Write

\[
 a_j=\lambda_{2j}\ (0\le j\le s),
 \qquad b_j=\lambda_{2j+1}\ (0\le j<s).
\]

The PBBS recurrence alone then gives disjoint cores \(K,K'\), each of
size \(r-s\), such that

\[
 A_{2j}=K\cup\{a_0,\ldots,a_{j-1}\}
             \cup\{b_j,\ldots,b_{s-1}\},
\tag{25.1}
\]

\[
 A_{2j+1}=K'\cup\{b_0,\ldots,b_{j-1}\}
               \cup\{a_{j+1},\ldots,a_s\}.
\tag{25.2}
\]

Thus both owner parities are fixed-core consecutive halves of one cyclic
window system, and the two endpoint Kneser edges form the exact core-swap
square

\[
 (K\cup U,K'\cup V),
 \qquad (K'\cup U,K\cup V),
\tag{25.3}
\]

where \(U=\{b_0,\ldots,b_{s-1}\}\) and
\(V=\{a_1,\ldots,a_s\}\).  No winding assumption is used.

### Theorem 25.1 (factor-two minimal-return reduction)

Every projected-edge-disjoint family of return intervals contains a
projected-edge-disjoint family of simple returns of at least half its
cardinality, with no increase in the maximum gap.

#### Proof

Inside each return, repeatedly choose two consecutive occurrences of an
internally repeated label.  The resulting strictly nested process ends at a
simple subreturn.  If that subreturn begins an even number of one-step
edges after its parent, its projected trace is contained in the parent
projected trace.  If it begins an odd number, its projected trace is
contained in the global one-edge translate of the parent trace.  Split all
subreturns by this parity.  Translation is a bijection of the full
projected edge set, so each parity class is edge-disjoint; retain the larger
class. \(\square\)

Consequently

\[
 \nu_H^{\rm simp}(P_r)\le\nu_H(P_r)
 \le2\nu_H^{\rm simp}(P_r),
\tag{25.4}
\]

and the same holds in the long-cycle rotation quotient.  Therefore
\((CP_A)\) is, up to a factor two, exactly the statement that the
fixed-core open-wreath sectors (25.1)--(25.3) have quotient packing
\(O_A(B_r/(2r+1))\).  Internal nesting and the zero/positive-winding split
are no longer part of the local geometry.  The full proof and parity audit
are recorded in PBBS_MINIMAL_RETURN_FIXED_CORE_NORMAL_FORM_20260725.md.

## 26. Multi-cut clustering removes the per-cut initialization toll

The one-cut chart can be shared by every collection of cuts lying in one
short owner interval.  If a cut cluster has leftmost and rightmost cuts
separated by span \(S\), and

\[
 3H+S\le m+1,
\tag{26.1}
\]

then a single global endpoint-plane Pareto staircase covers all
floor-correct lower targets crossing the cluster, including the lower
targets formerly carried by the negative endpoint-erosion prefix.  One
owner halo covers the corresponding upper targets and singleton owners.
The exact auxiliary length is at most

\[
 \boxed{7H+3S-3.}
\tag{26.2}
\]

The base erosion word keeps only its nonnegative entries, so its total
length over all cut paths is exactly the original owner length, with no
remaining \(HJ\) initialization term.

More explicitly, every maximal positive coordinate run \([L,R]\) is
represented by the endpoint point \((-L,R)\).  An owner intersection over
\([a,b]\) contains that coordinate exactly when

\[
 (-L,R)\ge(-a,b).
\]

Floor correctness again excludes a point strictly southwest of the query.
One east-before-south Pareto path through the endpoint rectangle therefore
gives all cluster intersections as contiguous unions.  Adding virtual cuts
in the first \(H\) positions after every actual path start supplies exactly
the witnesses lost by deleting the negative erosion entries.  The full
proof is in PBBS_MULTI_CUT_DOMINANCE_CLUSTER_20260725.md.

For cut clusters of spans \(S_j\) on all physical owner cycles, define

\[
 \mathfrak S_H=\sum_j(7H+3S_j-3).
\tag{26.3}
\]

Then the complete central-band word has length

\[
 \boxed{W+2HB_m+\mathfrak S_H.}
\tag{26.4}
\]

### Theorem 26.1 (clustered-span sufficient gate)

If, for every fixed \(A>0\), one can choose residence transversals and
clusters at \(H_A=\lceil A\sqrt m\rceil\) satisfying (26.1) and

\[
 \boxed{\mathfrak S_{H_A}=o_A(W),}
\tag{CS_A}
\]

then coefficient one follows by the same diagonal product-tail argument as
Theorems 22.2 and 24.3.

For deck-invariant choices, the quotient form of \((CS_A)\) asks for
clustered-span cost \(o_A(B_m)\).  The current direct packing-and-clustering
ledger gives only \(O_A(B_m)\).  Thus this fusion route is missing a
vanishing active-span density.  The weakest separate-cut route is
\((QST_A)\), asking for a vanishing improvement over
\(O_A(B_m/\sqrt m)\); \((CP_A)\) is the stronger fixed-core completion
target.

## 27. Fractional ambient completions give a second scalar form of \((CP_A)\)

For a simple return of gap \(2s+1\), retain the notation of Section 25 and
put

\[
 U=\{b_0,\ldots,b_{s-1}\},\qquad
 A=\{a_0,\ldots,a_s\},\qquad q=r-s.
\]

Order the two inactive cores \(K,K'\) independently and uniformly.  The
resulting ambient wreath consists of the fixed open PBBS segment and two
random Boolean chains.  For a fixed middle vertex \(T\), its probability
of occurring outside the open segment is exactly

\[
 \mathbf1_{\{T\cap Z=U\}}
 {1\over\binom qj^2},
 \qquad j=|T\cap K|,
 \tag{27.1}
\]

or

\[
 \mathbf1_{\{T\cap Z=A\}}
 {1\over\binom qj\binom q{j+1}},
 \qquad j=|T\cap K'|.
 \tag{27.2}
\]

The excluded odd endpoints already belong to the fixed open segment.  The
formula follows by requiring the indicated subsets to be prefixes or
suffixes of the two independent core orders.

For a projected-edge-disjoint simple-sector family, every middle vertex
lies in at most four fixed open segments.  If \(\pi_I(T)\) denotes the sum
of (27.1)--(27.2), the exact double-counting criterion is therefore

\[
 \boxed{
  \sup_T\sum_{I\in\mathcal P}\pi_I(T)=O_A(1)
  \quad\Longrightarrow\quad
  |\mathcal P|=O_A(B_r).}
 \tag{27.3}
\]

Indeed every completed wreath contains \(N=2r+1\) middle vertices, so

\[
 N|\mathcal P|
 =\sum_T\sum_I\Pr(T\hbox{ lies in the completion of }I)
 \le (O_A(1)+4)\binom Nr.
\]

Compatibility in (27.1)--(27.2) means that the entire simple omitted-label
word alternates across \((T,T^c)\).  Equivalently, the two PBBS owner
parities form oppositely directed unit-slope staircases in
\(h_T(Y)=|T\cap Y|\).  Generic Johnson-level or bounded-endpoint-degree
counting still loses one factor \(\sqrt r\); the unresolved assertion is
PBBS-specific suppression of these long perfectly alternating staircases.
The exact kernel and its independent audit are recorded in
PBBS_SIMPLE_SECTOR_AMBIENT_COMPLETION_KERNEL_20260725.md and
PBBS_OPEN_WREATH_COMPLETION_CONGESTION_GATE_20260725.md.
