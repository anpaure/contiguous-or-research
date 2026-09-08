# Finite PBBS phase telescope and the exact cross-interval residual

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, or external input

## 0. Result

This note closes the proposed third-phase refinement of a two-phase
nonoverlap carrier **inside one physical PBBS return**.

Let the exact adjacent tail identities be

\[
 \overline T_j0R_j=R_{j+1}0S_{j+1}\qquad(0\le j<s).
 \tag{0.1}
\]

For phases \(a<b\), put

\[
 A_{a,b}=(\overline T_{b-1}0)\cdots(\overline T_a0),
 \qquad
 C_{a,b}=(0S_b)\cdots(0S_{a+1}).
 \tag{0.2}
\]

Suppose phases \(t<u\) are in the nonoverlap branch, so that for a unique
word \(Z\)

\[
 R_u=A_{t,u}Z,
 \qquad
 R_t=ZC_{t,u}.
 \tag{0.3}
\]

Then every intermediate phase \(v\in[t,u]\) has the forced form

\[
 \boxed{R_v=A_{t,v}ZC_{v,u}.}
 \tag{0.4}
\]

More generally, every subpair \(p<q\) in \([t,u]\) is itself in the
nonoverlap branch with common word

\[
 \boxed{Z_{p,q}=A_{t,p}ZC_{q,u}.}
 \tag{0.5}
\]

Thus any finite collection of intermediate phases is only a refactorization
of one literal word. It imposes no new condition on \(Z\), and its order of
insertion is irrelevant.

There is also an exact normal form for phases added outside \([t,u]\).
Take \(a\le t<u\le b\), and set

\[
 L=A_{a,t},
 \qquad
 R=C_{u,b},
 \qquad
 \eta=|Z|-|L|-|R|.
 \tag{0.6}
\]

If \(\eta\ge0\), there is a unique word \(W\) such that

\[
 \boxed{Z=LWR,}
 \tag{0.7}
\]

and the enlarged endpoint pair \((a,b)\) remains nonoverlap with corridor
\(W\). If \(\eta<0\), the enlarged pair is in the overlap branch with its
unique bridge \(H\), and in the free group on \(\{0,1\}\)

\[
 \boxed{H=RZ^{-1}L,\qquad |H|=|L|+|R|-|Z|.}
 \tag{0.8}
\]

Actual PBBS compatibility says precisely that the reduced word on the
right of (0.8) is a positive word. Hence outer phases also supply no
independent projection: they monotonically consume the two ends of \(Z\),
and after the two consumptions meet they produce the already known unique
overlap bridge.

Consequently a genuinely noncommuting extra phase cannot belong to the
same return. It must come from a second physical return interval. The exact
packing residual is then a pair of support-disjoint return arcs on one
\(\tau\)-cycle, coupled only by an exterior transport \(\tau^g\). This
residual is stated exactly in Theorem 4.2 below.

## 1. The tail cocycle

Use the empty word for \(A_{a,a}\) and \(C_{a,a}\). Concatenating (0.1)
gives

\[
 A_{a,b}R_a=R_bC_{a,b}.
 \tag{1.1}
\]

For \(a<b<c\), the collars obey the literal cocycle identities

\[
 A_{a,c}=A_{b,c}A_{a,b},
 \qquad
 C_{a,c}=C_{b,c}C_{a,b}.
 \tag{1.2}
\]

Both identities retain the order of the letters; no commutation is being
used. They are immediate from (0.2).

The standard free-monoid dichotomy will be used repeatedly. If

\[
 AX=YC,
 \qquad
 |Y|-|A|=|X|-|C|=\delta,
 \tag{1.3}
\]

then:

* if \(\delta\ge0\), there is a unique \(Z\) with
  \(Y=AZ\) and \(X=ZC\);
* if \(\delta<0\), there is a unique \(H\) with
  \(A=YH\) and \(C=HX\).

This is just prefix and suffix cancellation in the free monoid.

## 2. Every internal third phase telescopes

### Theorem 2.1 (finite internal-phase normal form)

Assume (0.3). Then (0.4) holds for every \(t\le v\le u\). Moreover,
for every \(t\le p<q\le u\), (0.5) satisfies

\[
 R_q=A_{p,q}Z_{p,q},
 \qquad
 R_p=Z_{p,q}C_{p,q}.
 \tag{2.1}
\]

In particular, imposing the transported tail equation at any finite set
of phases in \([t,u]\) leaves exactly the same allowable \(Z\)-language as
the two endpoint equations.

#### Proof

From (1.1),

\[
 A_{t,v}R_t=R_vC_{t,v}.
 \tag{2.2}
\]

Substitute \(R_t=ZC_{t,u}\), and use
\(C_{t,u}=C_{v,u}C_{t,v}\). This gives

\[
 A_{t,v}ZC_{v,u}C_{t,v}=R_vC_{t,v}.
\]

Right cancellation proves (0.4).

Now put \(Z_{p,q}=A_{t,p}ZC_{q,u}\). By (1.2) and (0.4),

\[
\begin{aligned}
 R_q
 &=A_{t,q}ZC_{q,u}\\
 &=A_{p,q}A_{t,p}ZC_{q,u}
 =A_{p,q}Z_{p,q},
\end{aligned}
\]

while

\[
\begin{aligned}
 R_p
 &=A_{t,p}ZC_{p,u}\\
 &=A_{t,p}ZC_{q,u}C_{p,q}
 =Z_{p,q}C_{p,q}.
\end{aligned}
\]

This proves (2.1). Every displayed phase equation is therefore a formal
consequence of the endpoint equations and the adjacent cocycle. Conversely,
the formula (0.4) visibly satisfies all of them. Hence no additional phase
shrinks the solution language. \(\square\)

### Corollary 2.2 (all internal reset phases are redundant)

Retain the exact PBBS phase factorization identities

\[
 Q_{j+1}=S_j1Q_j,
 \qquad
 V_j=V_{j+1}1\overline T_j,
 \qquad
 S_j1P_j=P_{j+1}1\overline T_j.
 \tag{2.3}
\]

Then \(P_j=Q_jV_j\) at one phase if and only if it holds at every phase.
Together with Theorem 2.1, a finite collection of intermediate terminal
reset tests and tail-carrier tests is a conjugate copy of one test, not a
product of tests.

#### Proof

Equation (2.3) gives

\[
 P_j=Q_jV_j
 \Longleftrightarrow
 P_{j+1}1\overline T_j
 =Q_{j+1}V_{j+1}1\overline T_j
 \Longleftrightarrow
 P_{j+1}=Q_{j+1}V_{j+1},
\]

by right cancellation; the reverse implication follows by left
cancellation of \(S_j1\). Iterate and combine with Theorem 2.1. \(\square\)

## 3. Outer phases only consume the common corridor

### Theorem 3.1 (two-sided outer-consumption law)

Assume (0.3), choose \(a\le t<u\le b\), and define \(L,R,\eta\) by
(0.6). Then the free-monoid branch parameter for the enlarged pair
\((a,b)\) is exactly \(\eta\):

\[
 |R_b|-|A_{a,b}|=|R_a|-|C_{a,b}|=\eta.
 \tag{3.1}
\]

If \(\eta\ge0\), the enlarged pair has the unique nonoverlap factorization

\[
 R_b=A_{a,b}W,
 \qquad
 R_a=WC_{a,b},
 \tag{3.2}
\]

and its middle word is characterized by \(Z=LWR\).

If \(\eta<0\), the enlarged pair has the unique overlap factorization

\[
 A_{a,b}=R_bH,
 \qquad
 C_{a,b}=HR_a,
 \tag{3.3}
\]

where \(H\) is the positive reduction of \(RZ^{-1}L\) and has the length
in (0.8).

#### Proof

From transport between \(u\) and \(b\),

\[
 A_{u,b}R_u=R_bR.
 \tag{3.4}
\]

Since \(R_u=A_{t,u}Z\), taking lengths in (3.4) gives

\[
 |R_b|=|A_{u,b}|+|A_{t,u}|+|Z|-|R|.
 \tag{3.5}
\]

The cocycle gives

\[
 A_{a,b}=A_{u,b}A_{t,u}L.
 \tag{3.6}
\]

Subtracting lengths in (3.5)--(3.6) proves the first equality in (3.1);
the second follows from the length balance in (1.1).

If \(\eta\ge0\), the free-monoid dichotomy applied to the endpoint
transport gives the unique word \(W\) in (3.2). Equations (3.4) and (3.6)
then imply

\[
 A_{u,b}A_{t,u}Z
 =R_bR
 =A_{u,b}A_{t,u}LWR.
\]

Left cancellation yields \(Z=LWR\), proving (0.7).

If \(\eta<0\), the same dichotomy gives the unique positive word \(H\)
in (3.3), with \(|H|=-\eta\). Work temporarily in the free group. Put

\[
 A_0=A_{u,b}A_{t,u}.
\]

Equations (3.4) and (3.6) become

\[
 A_0Z=R_bR,
 \qquad
 A_0L=R_bH.
\]

Therefore

\[
 H=R_b^{-1}A_0L=RZ^{-1}L.
\]

Because the monoid dichotomy already produced \(H\) as a literal positive
word, this group identity is an exact positive-reduction formula, not a
formal relaxation. Its length is \(-\eta=|L|+|R|-|Z|\). \(\square\)

### Corollary 3.2 (no noncommuting third phase in one return)

Start from any nonoverlap pair and insert arbitrarily many phases, in any
order, from the same physical return.

* Phases between the current extrema telescope by Theorem 2.1.
* Enlarging the extrema subtracts exactly the newly exposed left and right
  collar lengths from \(\eta\).
* While \(\eta\ge0\), all insertion orders produce the same remaining
  subword \(W\) of \(Z\).
* Once \(\eta<0\), all insertion orders produce the one bridge prescribed
  by (0.8).

Thus the branch changes at most once. There is no third phase, and indeed
no finite phase system within one physical return, whose chronology is not
already contained in the one-dimensional tail cocycle.

#### Proof

The first assertion is Theorem 2.1. For the others, if the final extrema
are \(a,b\), then \(L=A_{a,t}\) and \(R=C_{u,b}\) depend only on those
extrema, not on the order in which intermediate extrema were visited.
Theorem 3.1 says that the sign is the sign of
\(|Z|-|L|-|R|\), which decreases whenever either extremum is enlarged.
Equations (0.7)--(0.8) give the unique final word. \(\square\)

## 4. Quotient-edge collision and the exact exterior residual

Let \(e_D\) denote the quotient transition edge indexed by the normalized
root \(D\). A nonwrapping return of parameter \(s\), rooted at \(D\), has
the exact quotient support

\[
 Q(D,s)=\{e_D,e_{\tau D},\ldots,e_{\tau^{s+1}D}\}.
 \tag{4.1}
\]

The endpoint \(s+1\) is essential: it is the second boundary edge.

### Theorem 4.1 (general aligned-phase collision)

Let two return intervals on the same \(\tau\)-cycle have roots \(D\) and
\(E=\tau^gD\), and parameters \(s\) and \(r\). If there are phase-support
indices

\[
 0\le i\le s+1,
 \qquad
 0\le j\le r+1,
 \qquad
 i\equiv g+j\pmod{\ell(D)},
 \tag{4.2}
\]

then the two intervals contain the common quotient edge

\[
 e_{\tau^iD}=e_{\tau^jE}.
 \tag{4.3}
\]

Consequently, on a long cycle and after choosing nonwrapping integer lifts
and ordering the second interval after the first, quotient-edge-disjointness
is exactly

\[
 \boxed{s+2\le g\le \ell(D)-r-2.}
 \tag{4.4}
\]

In particular, a phase from a second physical return cannot be inserted
temporally inside the first return's support in an edge-disjoint packing.

#### Proof

Equation (4.3) follows immediately from (4.2) and the edge indexing. The
support index sets are the two cyclic integer intervals

\[
 \{0,\ldots,s+1\},
 \qquad
 \{g,\ldots,g+r+1\}.
\]

They are disjoint precisely when, after ordering the second after the
first without wrap, its first index is at least \(s+2\) and its last index
is at most \(\ell(D)-1\). This is (4.4). \(\square\)

The exact critical-corner theorem is a strict instance of Theorem 4.1.
For that family the nontrivial word calculation proves that every phase
choice contains

\[
 C(s,K,Y)=1^s0^KY0^s
\]

as one of its support roots. Hence all those intervals satisfy (4.2) at
that root, and their apparent phase-pair multiplicity collapses to one
edge. Theorem 4.1 does not assert that every PBBS carrier has such a
phase-independent corner; producing one is exactly the missing global
incidence problem.

### Theorem 4.2 (exact genuinely noncommuting residual)

For fixed rank, every extra phase proposed as a constraint on a two-phase
nonoverlap corridor falls into exactly one of the following classes.

1. **Same physical return, internal phase.** It has the form (0.4) and
   telescopes by Theorem 2.1.
2. **Same physical return, outer phase.** It obeys the consumption law of
   Theorem 3.1 and either shortens \(Z\) or produces its unique overlap
   bridge.
3. **Second physical return, aligned support.** It gives the common edge
   (4.3) and is forbidden in a quotient-edge-disjoint packing.
4. **Second physical return on a different \(\tau\)-cycle.** It has no
   common physical itinerary with the first return and therefore is not a
   transported third-phase constraint at all.
5. **Second physical return, same cycle and exterior support.** After
   possibly swapping
   the two intervals, it has the following exact data:

   \[
   \begin{gathered}
   E=\tau^gD,
   \qquad s+2\le g\le\ell(D)-r-2,\\
   R_u=A_{t,u}Z,
   \qquad R_t=ZC_{t,u},\\
   \widetilde R_q=\widetilde A_{p,q}\widetilde Z,
   \qquad
   \widetilde R_p=\widetilde Z\widetilde C_{p,q},
   \end{gathered}
   \tag{4.5}
   \]

   together with the genuine first-return chronology for the return rooted
   at \(D\) and for the return rooted at \(\tau^gD\).

Class 5 is the only genuinely noncommuting residual. Its coupling is not
another local phase equation: it is re-canonicalization after the exterior
transport \(\tau^g\).

#### Proof

An extra phase either belongs to the first physical return or it does not.
In the first case it lies between the chosen endpoints or enlarges at least
one endpoint; Theorems 2.1 and 3.1 give Classes 1 and 2. In the second case,
if the other return lies on a different \(\tau\)-cycle there is no common
physical itinerary and hence no transported third-phase constraint; this is
Class 4. If it lies on the same cycle, write its root uniquely as
\(\tau^gD\) modulo the cycle length. Theorem 4.1 splits aligned and
support-disjoint cases. The aligned case is Class 3. In the support-disjoint case choose the
nonwrapping order to obtain (4.4), and apply the two-phase free-monoid
dichotomy separately inside each actual return to obtain (4.5). There is
no adjacent identity spanning the unused gap from \(s+2\) to \(g\); the
only exact link is \(E=\tau^gD\) plus the two first-return predicates.
This is Class 5. The cases are exhaustive and disjoint. \(\square\)

## 5. The exact coefficientwise gate left by the theorem

Let \(\mathcal N_m(s;t,u)\) be the set of rank-\(m\) normalized roots
which satisfy all of the following:

1. they begin a genuine first zero-winding return of parameter \(s\);
2. phases \(t<u\) are in the nonoverlap branch;
3. all canonical height and first-return inequalities are retained.

Theorem 4.2 shows that a noncommuting phase argument can only act on the
shifted intersections

\[
 \boxed{
 \mathcal N_m(s;t,u)
 \cap
 \tau^{-g}\mathcal N_m(r;p,q),
 \qquad
 s+2\le g\le\ell(D)-r-2.}
 \tag{5.1}
\]

The dependence of the upper limit on the cycle containing \(D\) is part
of the statement. Equivalently, (5.1) is the family of two genuine return
arcs whose complete quotient-edge supports are disjoint but whose two
canonical decompositions are linked by the same exterior PBBS itinerary.

No equation from a third, fourth, or finite collection of phases inside
either return reduces (5.1): Theorem 2.1 proves that all of them are already
logical consequences of the two adjacent tail cocycles. Therefore a strict
coefficient saving must prove one of the following genuinely new facts:

* an aligned-root theorem, as in the exact common-corner family, forcing
  (4.2) for most critical pairs; or
* a shifted-incidence estimate showing that the support-separated
  intersections (5.1) have vanishing critical mass.

This is sharper than the statement that a third phase might be useful.
There is no local third-phase gate. The only surviving geometry is an
**exterior two-return incidence problem with disjoint quotient arcs**.

## 6. Proved boundary

Proved exactly:

1. all intermediate and finite same-return phase constraints telescope;
2. arbitrary outer same-return phases obey the two-sided consumption law
   (0.7)--(0.8), with at most one nonoverlap-to-overlap transition;
3. every aligned phase of a second return creates a literal common
   quotient edge;
4. the only noncommuting residual is the support-separated shifted
   intersection (5.1).

Not proved:

1. that a general critical return has a phase-independent common corner;
2. a vanishing coefficient bound for (5.1);
3. the coefficient-one theorem.
