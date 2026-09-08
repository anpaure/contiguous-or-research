# Cross-audit of mathematical attack H: hard-quota absorber

Date: 2026-07-24

Audited source: MATH_ATTACK_H_HARD_QUOTA_ABSORBER_20260724.md.

Method: theorem-proof analysis only. No web search, finite search, random
experiment, or solver was used.

## 0. Executive verdict

The principal hard-quota reduction is correct.

* The ceiling/floor criterion in Theorem 2.1 is an exact if-and-only-if
  statement for integral partial loads.
* The deletion-transversal formulation in Theorem 4.1 is exactly equivalent
  to domination by fixed balanced quotas, with one common deletion set at
  all depths.
* The weighted inequalities in Theorem 6.1 are exactly the dual
  characterization of a **fractional** deletion of budget \(b\).
* The Fano-plane example has fractional cover mass \(7/4\) and integral
  cover number \(3\). It is a valid generic integrality counterexample, but
  not a counterexample for a wreath deletion matrix.
* The two-lift formula and directed lift-cycle criterion in Section 8 are
  correct for their stated star-fibre move class. The proof needs two small
  missing justifications, supplied below.

There is one important scope correction:

\[
\boxed{\text{Section 8 is not a classification of general }C_8
\text{ wreath trades}.}
\]

It classifies only simultaneous replacements by the two twin lifts of
fixed \(P_v\)-traces. General alternating \(C_8\) switches may change those
traces. The correct general \(C_8\) theorem is proved in Section 8 of this
audit: every exact alternating \(C_8\) switch cuts two old wreaths twice
each, and the two cut-path profiles must agree as unordered pairs.

There are three qualifications, none fatal to the reduction.

1. All fixed-window incidence statements are asymptotic statements for
   sufficiently large \(m\), so that \(K_A\le m-1\). At \(q=m\), the
   binary incidence convention and “\(n\) distinct intervals” fail.
2. The Hall theorem uses an integral budget \(b\). For nonintegral \(b\),
   the support function has a fractional last order statistic.
3. The Fano example proves that generic Hall duality does not round itself.
   It does not prove that the actual wreath deletion polytope is nonintegral.

The audit also gives one unconditional strengthening of Section 8:

\[
\boxed{\text{for }m\ge4,\text{ the lift map has no directed }3
\text{-cycle}.}
\]

Thus every nontrivial fixed-star twin-lift switch uses at least four wreaths
when \(m\ge4\). This sharpening still does not classify or exclude general
two-wreath \(C_8\) switches.

The source report remains a valid exact reduction, not a proof of MWB.

---

## 1. Notation and mass

Let

\[
n=2m+1,\qquad
W=\binom nm,\qquad
t=\frac Wn=\operatorname{Cat}_m.
\]

At depth \(q\), put

\[
r=m-q,\qquad
N_q=\binom nr,\qquad
\lambda_q=\frac W{N_q},\qquad
c_q=\lfloor\lambda_q\rfloor,\qquad
\rho_q=W-c_qN_q.
\]

A balanced quota has \(\rho_q\) entries \(c_q+1\) and
\(N_q-\rho_q\) entries \(c_q\). If \(X\) is a family of wreaths and
\(1\le r\le n-1\), then each wreath has \(n\) distinct cyclic
\(r\)-intervals, so

\[
\sum_S\mu_q^X(S)=n|X|.
\tag{1.1}
\]

For fixed \(A\), \(K_A=\lceil A\sqrt m\rceil\le m-1\) for all sufficiently
large \(m\), so (1.1) applies throughout the audited window.

The product and upper bound used in the source are correct:

\[
\lambda_q
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}
=\prod_{i=0}^{q-1}
\left(1+\frac{2(i+1)}{m-i}\right),
\tag{1.2}
\]

\[
\log\lambda_q
\le\sum_{i=0}^{q-1}\frac{2(i+1)}{m-i}
\le\frac{q(q+1)}{m-q+1}.
\tag{1.3}
\]

Hence, uniformly on a fixed Gaussian window,

\[
1\le c_q\le C_A,\qquad N_q\ge\kappa_AW,\qquad
\sum_{q\le K_A}\frac1{c_q}=O_A(\sqrt m).
\tag{1.4}
\]

No capacity or Gaussian-scale error was found here.

---

## 2. Exact ceiling/floor criterion

Let an exact factor split as

\[
F=G\sqcup B,\qquad |B|=b,
\]

and fix one depth. Set

\[
\eta(S)=\mu_q^G(S),\qquad
\Delta=\sum_S(c_q-\eta(S))_+.
\]

Since \(G\) has \(t-b\) wreaths,

\[
\sum_S\eta(S)
=W-nb
=c_qN_q+\rho_q-nb.
\tag{2.1}
\]

### Theorem 2.1 (audited partial-quota criterion)

There exists a balanced quota \(\beta_q\) with

\[
\eta(S)\le\beta_q(S)\quad\text{for every }S
\tag{2.2}
\]

if and only if

\[
\max_S\eta(S)\le c_q+1
\tag{2.3}
\]

and

\[
\Delta\le nb.
\tag{2.4}
\]

#### Proof

The ceiling (2.3) is necessary. Assume it, and let

\[
h=\#\{S:\eta(S)=c_q+1\}.
\]

Because the load is integral and no entry exceeds \(c_q+1\),

\[
\sum_S\eta(S)=c_qN_q+h-\Delta.
\]

Comparison with (2.1) gives the exact identity

\[
h=\rho_q-nb+\Delta.
\tag{2.5}
\]

A balanced quota dominates \(\eta\) exactly when its \(\rho_q\) high
positions include all \(h\) entries loaded \(c_q+1\). There are enough
remaining positions for the other \(\rho_q-h\) highs, so this is possible
if and only if \(h\le\rho_q\). By (2.5), this is equivalent to
\(\Delta\le nb\). \(\square\)

No extra lower bound on \(\Delta\) is missing: \(h\ge0\) is automatic.
The case \(\rho_q=0\) is covered as well: (2.4)-(2.5) force \(h=0\).

Integrality is essential. The statement should not be applied verbatim to
the fractional thinnings of Section 7; the source does not do so.

At depth one, \(c_1=1\), so \(\Delta\) is exactly the number of holes.
Thus the specialized zero/double criterion and identity in the source are
correct.

### Consequence for overload

If \(G\le\beta_q\), let \(s_q=\beta_q-\mu_q^G\). Then

\[
\sum_Ss_q(S)=W-(W-nb)=nb
\]

and

\[
\mu_q^F-\beta_q=\mu_q^B-s_q.
\]

Therefore

\[
O_q(F)
\le\sum_S(\mu_q^B(S)-s_q(S))_+
\le\sum_S\mu_q^B(S)
=nb.
\tag{2.6}
\]

Consequently

\[
\sum_{q\le K_A}\frac{O_q(F)}{c_q}
\le nbK_A.
\tag{2.7}
\]

Since \(W=nt\), the hypothesis \(b=o(t/\sqrt m)\) makes (2.7) \(o(W)\).
Every factor \(n\), \(K_A\), and \(c_q\) is correct.

---

## 3. Exact deletion-transversal equivalence

Fix one exact factor \(F\) and balanced quotas \(\beta_q\) at every
controlled depth. For a resource \(a=(q,S)\), define

\[
d_a=(\mu_q^F(S)-\beta_q(S))_+
\]

and, for \(E\in F\),

\[
A_{aE}=
\mathbf1_{\{S\text{ is a cyclic }(m-q)\text{-interval of }E\}}.
\]

On the fixed window and for sufficiently large \(m\), the interval sets
inside one wreath are distinct, so \(A\) is a \(0\)-\(1\) matrix.

### Theorem 3.1 (audited deletion equivalence)

For \(B\subseteq F\) and \(G=F\setminus B\),

\[
\mu_q^G(S)\le\beta_q(S)
\quad\text{for every controlled }(q,S)
\tag{3.1}
\]

if and only if

\[
\sum_{E\in B}A_{aE}\ge d_a
\quad\text{for every resource }a.
\tag{3.2}
\]

#### Proof

For \(a=(q,S)\),

\[
\mu_q^G(S)
=\mu_q^F(S)-\sum_{E\in B}A_{aE}.
\tag{3.3}
\]

If \(\mu_q^F(S)\le\beta_q(S)\), (3.1) is automatic and \(d_a=0\).
Otherwise (3.1) requires deletion of at least
\(\mu_q^F(S)-\beta_q(S)=d_a\) occurrences. This is exactly (3.2).
\(\square\)

The same column variable \(\mathbf1_{\{E\in B\}}\) appears at every depth.
Thus this is genuinely a common-depth deletion problem.

Residual exact factorability is automatic: because \(B\subseteq F\), the
wreaths of \(B\) partition exactly the middle-layer leave of \(G\).

Let

\[
\Xi_q=\sum_Sd_{q,S},\qquad
\Xi_A=\sum_{q\le K_A}\Xi_q,
\]

and let \(\tau_A(F,\beta)\) be the minimum size of an integral deletion
cover. Summing (3.2) gives

\[
\max_q\frac{\Xi_q}{n}\le\tau_A,\qquad
\frac{\Xi_A}{nK_A}\le\tau_A.
\tag{3.4}
\]

For the reverse crude bound, \(d_{q,S}\le\mu_q^F(S)\). Choose
\(d_{q,S}\) distinct owner wreaths for each positive-demand resource and
take their union. This gives

\[
\tau_A\le\Xi_A.
\tag{3.5}
\]

The source bounds are therefore correct. Integer ceilings could strengthen
the lower bounds in (3.4), but are not needed.

### Equivalence with \(HQ_A\)

Existentially, the source's missing lemma

\[
\tau_A(F_m,\beta)=o(t_m/\sqrt m)
\tag{3.6}
\]

is equivalent to \(HQ_A\).

* From (3.6), choose an optimal \(B\), put \(G=F\setminus B\), and use
  (3.1). Theorem 2.1 then gives the quota-free ceiling/floor conditions.
* From \(HQ_A\), Theorem 2.1 supplies quotas dominating the same common
  core \(G\). Its exceptional family \(B\) satisfies (3.2), so
  \(\tau_A\le|B|=o(t/\sqrt m)\).

The little-\(o\) statements should formally be read as sequences: for each
fixed \(A\), choose witnesses for all sufficiently large \(m\) with
\(|B_{A,m}|\sqrt m/t_m\to0\).

---

## 4. Fractional Hall duality

Let the resource set be \(\mathcal R\), and keep \(A,d\). For an
**integer** budget \(b\), put

\[
P_b=\left\{
x\in[0,1]^F:\sum_{E\in F}x_E\le b
\right\}.
\]

For \(y\in\mathbb R_{\ge0}^{\mathcal R}\), define

\[
w_E(y)=\sum_aA_{aE}y_a.
\]

### Theorem 4.1 (audited fractional Hall theorem)

There exists \(x\in P_b\) with

\[
Ax\ge d
\tag{4.1}
\]

if and only if, for every \(y\ge0\),

\[
\sum_ad_ay_a
\le\operatorname{Top}_b(w_E(y):E\in F),
\tag{4.2}
\]

where \(\operatorname{Top}_b\) is the sum of the \(b\) largest entries.

#### Proof

Consider

\[
\mathcal C=AP_b-\mathbb R_{\ge0}^{\mathcal R}.
\]

Condition (4.1) is equivalent to \(d\in\mathcal C\). If
\(d\notin\mathcal C\), separation produces \(y\) with

\[
y^\mathsf Td>\sup_{z\in\mathcal C}y^\mathsf Tz.
\]

The supremum is finite only when \(y\ge0\), and then

\[
\sup_{z\in\mathcal C}y^\mathsf Tz
=\max_{x\in P_b}\sum_Ew_E(y)x_E.
\]

All \(w_E(y)\) are nonnegative. The last maximum is obtained by putting
weight one on the \(b\) largest entries, proving (4.2) and the converse.
\(\square\)

There is no omitted dual variable for \(x_E\le1\); those upper bounds are
what produce the top-\(b\) support function.

For nonintegral \(b\), the support function would include the appropriate
fraction of the next-largest weight. Here \(b=|B|\) is integral.

---

## 5. The Fano integrality example

Let the seven Fano points be the resources, and for each line \(L\) let

\[
C_L=P\setminus L
\]

be a deletion candidate. Each point lies in four candidates. Weighting
every candidate by \(1/4\) covers every resource and has total mass

\[
7/4<2.
\tag{5.1}
\]

Thus the fractional Hall conditions hold for budget \(b=2\).

For distinct lines \(L_1,L_2\),

\[
C_{L_1}\cup C_{L_2}
=P\setminus(L_1\cap L_2).
\tag{5.2}
\]

The lines meet in one point, so two candidates always miss that point.
Three complements of nonconcurrent lines cover all points. Hence the
integral cover number is exactly

\[
\tau=3.
\tag{5.3}
\]

This verifies a strict fractional/integral gap. Its scope must not be
enlarged: the Fano matrix is not asserted to arise from an exact wreath
factor. The valid conclusion is only

\[
\boxed{\text{generic weighted Hall inequalities do not themselves supply
integral rounding}.}
\]

One still needs a wreath-specific ideality theorem, rounding theorem, or
absorber. It would be incorrect to cite this example as proof that the
actual wreath deletion polytope is nonintegral.

---

## 6. The two star-fibre lifts

Fix \(v\in[n]\), and split the middle layer into

\[
P_v=\{M:v\in M\},\qquad Q_v=\{M:v\notin M\}.
\]

Every wreath has \(m\) intervals in \(P_v\) and \(m+1\) in \(Q_v\).

### Theorem 6.1 (audited two-lift lemma)

For \(m\ge2\), every projected trace \(T=E\cap P_v\) has exactly two
unoriented wreath lifts. Up to reversal, they have coordinate words

\[
(r_1,\ldots,r_{m-1},v,s_1,\ldots,s_{m-1},x,y)
\tag{6.1}
\]

and the word obtained by interchanging \(x,y\).

#### Proof

The \(m\) middle intervals containing \(v\) have \(m\) consecutive start
positions. If two are \(d\) starts apart, \(1\le d\le m-1\), their
intersection has size \(m-d\). Hence the Johnson graph induced by the trace
is exactly a path. This justifies its cyclic-start ordering.

Orienting the path reveals the leaving and entering label at each step. It
reconstructs the two ordered side strings around \(v\), up to simultaneous
reversal. Their union with \(v\) has \(2m-1\) labels, so two labels \(x,y\)
are missing. They occupy the opposite two-position gap in either order.
\(\square\)

### Exact lower-interval effect

For \(2\le\ell\le m\), swapping \(x,y\) changes only the two
\(\ell\)-windows containing exactly one of them. If \(S_\ell,R_\ell\) are
the \(\ell-1\) labels on the two outer sides of the gap, the signed change is

\[
\Delta_{T,\ell}
=\mathbf1_{S_\ell\cup\{y\}}
+\mathbf1_{R_\ell\cup\{x\}}
-\mathbf1_{S_\ell\cup\{x\}}
-\mathbf1_{R_\ell\cup\{y\}}.
\tag{6.2}
\]

The side blocks are disjoint because

\[
2(\ell-1)\le2m-2<n-2=2m-1.
\]

They avoid \(x,y\), so the four targets are distinct. A further detail
omitted in the source proof is needed for “exactly two old into two new”:
a new target cannot be an unchanged old interval. In the old order it is an
\((\ell-1)\)-block plus a label separated from that block by the omitted
gap label. The other side of the block is separated from that label by the
nonempty complementary arc, since \(n=2m+1\) and \(\ell\le m\).
Consequently its cyclic indicator has two components and four boundary
transitions, whereas a proper cyclic interval has one component and two.
Thus it is not an old cyclic \(\ell\)-interval.

At \(\ell=1\), the singleton family is unchanged.

At \(\ell=m\), put

\[
R_E=\{Sx,Ry\},\qquad A_E=\{Sy,Rx\}.
\tag{6.3}
\]

Each is a pair of complementary \(m\)-subsets of
\([n]\setminus\{v\}\), and the four targets are distinct.

---

## 7. Exact lift-cycle conservation

For an exact factor \(F\), decompose the \(Q_v\)-targets of each wreath into
its \(m-1\) fixed targets and its variable pair \(R_E\). Exactness gives

\[
Q_v=\mathcal H\;\dot\cup\!
\bigsqcup_{E\in F}R_E,
\tag{7.1}
\]

where \(\mathcal H\) is the family of fixed targets.

Define a partial map

\[
\phi(E)=E'\quad\Longleftrightarrow\quad A_E=R_{E'}.
\tag{7.2}
\]

If \(A_E\) contains a target in \(\mathcal H\), leave \(\phi(E)\)
undefined. Here “meets” means intersection as families of middle targets.
Otherwise \(A_E\) equals one unique variable complementary pair.

### Theorem 7.1 (audited lift-cycle theorem)

For \(I\subseteq F\), replace every \(E\in I\) by its twin. The result is
an exact factor if and only if \(\phi\) is defined on \(I\) and
\(\phi|_I\) is a permutation of \(I\). Equivalently, \(I\) is a disjoint
union of directed \(\phi\)-cycles.

#### Proof

All \(P_v\)-targets and fixed \(Q_v\)-targets remain unchanged. Exact
variable coverage is equivalent to

\[
\{A_E:E\in I\}=\{R_E:E\in I\}
\tag{7.3}
\]

as multisets. By (7.2), this says exactly that \(\phi\) maps \(I\)
bijectively to itself. \(\square\)

Only flipped core wreaths change the core histogram, so the source's
coordinatewise quota-slack test is exact.

### No one- or two-cycle

A loop is impossible for \(m\ge2\) because \(R_E\cap A_E=\varnothing\).

Suppose \(m\ge3\) and \(E,E'\) formed a two-cycle. The four targets are

\[
Sx,\ Sy,\ Rx,\ Ry.
\]

The only pairs having intersection \(m-1\) are
\(\{Sx,Sy\}\) and \(\{Rx,Ry\}\); cross-intersections have size zero or one.
Thus the second trace has the same side cores \(S,R\). Both traces contain

\[
S\cup\{v\},\qquad R\cup\{v\},
\]

contradicting exactness. The source's no-two-cycle lemma is correct.

The threshold is sharp. For \(m=2\), \(v=0\), the wreaths

\[
(0,1,2,3,4),\qquad(0,2,4,1,3)
\]

partition all two-subsets, and their twins

\[
(0,1,3,2,4),\qquad(0,3,4,1,2)
\]

also partition them, giving a two-cycle.

Thus the one-exceptional-wreath obstruction is valid for \(m\ge3\), but
only for one fixed \(v\), one twin flip, and one additional replacement.

### New strengthening: no three-cycle for \(m\ge4\)

Let the folded Johnson graph have complementary-pair vertices

\[
[A]=\{A,A^c\},\qquad A\in\binom{[n]\setminus\{v\}}m,
\]

with adjacency when suitable representatives meet in \(m-1\) points.
Each trace gives an edge \(R_EA_E\). A directed \(\phi\)-cycle gives a
cycle of these pair vertices.

Assume a directed triangle exists. Choose representatives \(A,B,C\) so

\[
|A\cap B|=|A\cap C|=m-1.
\]

Then \(|B\cap C|\ge m-2\). Folded adjacency says

\[
|B\cap C|\in\{m-1,1\}.
\]

For \(m\ge4\), it follows that \(|B\cap C|=m-1\). Thus \(A,B,C\) form a
triangle in the ordinary Johnson graph. Such a triangle is either a star,
whose sets share an \((m-1)\)-subset, or a top, whose complements share an
\((m-1)\)-subset. In either case the three trace edges have a common side
core. After adjoining \(v\), the three projected traces share a middle
target, contradicting exactness.

Therefore

\[
\boxed{\phi\text{ has no directed cycle of length }1,2,\text{ or }3
\quad(m\ge4).}
\tag{7.4}
\]

For \(m=3\), the folded graph has non-star/top triangles, so this proof
does not improve the source bound. No completion of such a triangle to an
exact factor is asserted.

---

## 8. The genuine \(C_8\) classification

The source's lift cycles should not be called general alternating
\(C_8\) trades. Let

\[
O_m=KG(2m+1,m).
\]

An exact factor is a spanning \(2\)-factor of length-\(n\) wreath cycles.
Let \(C\) be a simple even cycle whose edges alternate between \(F\) and
its complement, and toggle its edges.

### Theorem 8.1 (general exact \(C_8\) classification)

No alternating cycle of length less than eight takes one exact wreath
factor to another. Every exact alternating \(C_8\) switch:

1. removes two edges from each of two old wreaths;
2. cuts them into paths of vertex lengths

   \[
   a,n-a\qquad\text{and}\qquad b,n-b;
   \]

3. reconnects them into two new cycles, one path from each old wreath in
   each new cycle; and
4. satisfies

   \[
   \boxed{\{a,n-a\}=\{b,n-b\}.}
   \tag{8.1}
   \]

Conversely, an alternating \(C_8\) reconnection with two new components and
(8.1) gives another exact factor.

#### Proof

A wreath cycle is induced: two cyclic middle intervals in one coordinate
order are disjoint exactly when their starts differ by \(m\) or \(m+1\),
the two neighboring starts on the odd-graph cycle.

If an old wreath loses exactly one factor edge, it leaves an \(n\)-vertex
path. Its endpoints cannot be rejoined by a new edge, since the only edge
between them inside the induced wreath is the removed edge. Any new
component containing this path is therefore longer than \(n\). Every
touched old wreath must be cut at least twice.

The odd graph has no \(4\)-cycle: two distinct vertices have at most one
common neighbor, because every common neighbor is an \(m\)-subset of the
complement of their union, which has size at most \(m\).

An alternating \(C_6\) removes three factor edges. The two-cut rule forces
all three into one old wreath, but every added edge would then be a chord
of that induced wreath, impossible.

An alternating \(C_8\) removes four factor edges. The two-cut rule and
inducedness force the distribution \(2+2\) on two old wreaths. All added
edges run between them. Cutting gives paths of lengths
\(a,n-a,b,n-b\). The reconnection either makes one \(2n\)-cycle or two
cycles, each pairing one path from each old wreath. Exactness excludes the
\(2n\)-cycle.

Pairing \(a\) with \(b\) requires \(a+b=n\); crossed pairing requires
\(a+(n-b)=n\), equivalently \(a=b\). These alternatives are exactly
(8.1). Conversely, (8.1) makes both new cycles have length \(n\), hence
they are wreaths. \(\square\)

### Relation to the source's Section 8

A directed \(k\)-cycle of \(\phi\) replaces \(k\) wreaths by twins relative
to one fixed \(v\). It is a circulation in an auxiliary folded-Johnson
lift graph, not automatically a simple alternating cycle in \(O_m\).

For \(m\ge3\), no nontrivial two-wreath \(C_8\) can preserve the two
individual \(P_v\)-traces merely by choosing twin lifts. There is no
contradiction: general balanced \(C_8\) switches change those traces.

Thus the two valid classifications are separate:

\[
\boxed{\text{fixed-star twin flips}
\iff\text{ unions of directed }\phi\text{-cycles},}
\]

\[
\boxed{\text{exact alternating }C_8
\iff\text{ balanced }2+2\text{ switch satisfying (8.1)}.}
\]

---

## 9. Remaining checks and quantifiers

The following supporting claims also pass.

### Two-sided prebalance

If \(F=G\sqcup B\) is quota-safe, then

\[
(c_q-\mu_q^F(S))_+
\le(c_q-\mu_q^G(S))_+,
\]

and, since \(\mu_q^G(S)\le c_q+1\),

\[
(\mu_q^F(S)-c_q-1)_+\le\mu_q^B(S).
\]

Summing gives both \(nb\) bounds in Lemma 5.1. Summing over
\(K_A=O_A(\sqrt m)\) depths gives \(o(W)\) when
\(b=o(t/\sqrt m)\).

### Regular high quotas

The divisibility

\[
\frac{r\rho_q}{n}
=rt-c_q\binom{n-1}{r-1}\in\mathbb Z
\]

is correct. The degree-smoothing exchange proves a simple regular
\(r\)-uniform family of \(\rho_q\) high positions. This passes all
singleton star cuts but does not imply containment of a common core.

### Symmetric thinning

The stabilizer of \(v\) is transitive on wreath supports: rotate two
representatives to put \(v\) in the same position and map remaining labels
positionwise. An invariant weighting is constant on all supports, hence
has uniform depth-\(q\) load \(\alpha\lambda_q\). At a depth with
\(1<\lambda_q<2\), low quota cells force \(\alpha\lambda_q\le1\).
Proposition 7.3 is correct within its symmetry scope.

### Recognition of a one-wreath leave

If \(n\) middle sets have degree \(m\) at every coordinate and their
Johnson graph has a Hamilton cycle, every cycle edge contributes one entry
and one exit. There are \(2n\) coordinate transitions, while every
nonconstant cyclic coordinate word has at least two. Equality forces each
coordinate to occupy one run of \(m\) consecutive positions, reconstructing
a wreath. Lemma 9.1 is correct.

### Diagonalization

For every fixed \(A_j\uparrow\infty\), choose a threshold after which the
normalized overload is at most \(1/j\), then choose \(j=j(m)\to\infty\)
slowly enough that

\[
K_{A_{j(m)}}<m,\qquad
\frac1W\sum_{q\le K_{A_{j(m)}}}\frac{O_q}{c_q}\to0.
\]

This gives the required growing window. The source correctly claims only
unlabelled MWB, not a labelled common nested resolution.

---

## 10. Final audit ledger

### Passed exactly

1. Fixed-window bounded capacities.
2. The ceiling plus total floor-deficit criterion.
3. Exceptional-family charging \(O_q(F)\le n|B|\).
4. Common-depth deletion-transversal equivalence.
5. The bounds on the transversal number.
6. Fractional Hall duality with \(\operatorname{Top}_b\).
7. The Fano fractional/integral gap, with its generic scope.
8. The two-lift and gap-change formulas.
9. The directed lift-cycle conservation law.
10. The no-one/two-cycle result for \(m\ge3\).

### Corrections or clarifications

1. Add “for all sufficiently large \(m\), so \(K_A\le m-1\)” to the
   fixed-window incidence model.
2. State explicitly that the Hall budget \(b\) is integral.
3. Preserve the qualification that the Fano matrix is not known to be
   wreath-realizable.
4. In the two-lift proof, justify that the trace's Johnson graph is exactly
   a path and that new gap-flip targets do not coincide with unchanged old
   targets.
5. Replace any phrase “\(C_8\) classification” for source Section 8 by
   “fixed-star twin-lift-cycle classification.”

### New rigorous strengthening

For \(m\ge4\), the partial lift map has no directed \(3\)-cycle, so every
fixed-star twin-lift switch uses at least four wreaths.

### Final logical status

The exact remaining statement in this route is still

\[
\boxed{\tau_A(F_m,\beta)=o(t_m/\sqrt m)
\quad\text{for every fixed }A.}
\]

Neither fractional Hall duality, the Fano example, regular star quotas,
nor the lift-cycle classification proves this integral transversal lemma.
The hard-quota report is a sound reduction with precise obstructions and
fractional benchmarks, but it does not prove MWB or the contiguous-OR width
conjecture.
