# Disjoint adjacent-priority layers: simultaneous interval legality and additive floor descent

Date: 2026-07-25

Method: pure mathematics only.  No computation, search, solver, or
long-running job is used.

## 0. Outcome

Let (n=2m+1), let (P_1,ldots,P_m) be the ordered disjoint
coordinate pairs, and let (M_0) be the first-avoided token matching for
this order.  Let

\[
 \Lambda\subseteq\{1,\ldots,m-1\},
 \qquad |j-k|\ge2\quad(j\ne k\in\Lambda),
\tag{0.1}
\]

so that the adjacent blocks ((P_j,P_{j+1})), (j\in\Lambda), are
pairwise disjoint.  This includes either full parity layer

\[
 \Lambda_{\rm odd}=\{1,3,5,\ldots\},
 \qquad
 \Lambda_{\rm even}=\{2,4,6,\ldots\}.
\tag{0.2}
\]

For every (j\in\Lambda), let \(\theta_j\) exchange (P_j) with
(P_{j+1}) coordinatewise and suppose

\[
 F_{j+1}=\theta_jF_j.
\tag{0.3}
\]

In the rows of (F_j), break the affected carrier

\[
 \mathcal D_j=
 \left\{S\in\binom{[n]}{m-1}:
 S\cap P_h\ne\varnothing\ (h<j),\quad
 S\cap(P_j\cup P_{j+1})=\varnothing\right\}
\tag{0.4}
\]

into maximal physical intervals.  Choose independently on every such
interval whether all its lower targets use their (F_j)-tokens or their
conjugate (F_{j+1})-tokens.  Make these choices simultaneously for all
(j\in\Lambda).

The resulting token set is always a full lower-saturating,
middle-injective matching.  Thus simultaneous legality costs no thinning
and no compatibility condition among the interval bits.

If (r_j) is the number of intervals for block (j), and
(r_\Lambda=\sum_{j\in\Lambda}r_j), then

\[
 \boxed{
 r_j\le\min\{2j\operatorname{Cat}_{m-1},|\mathcal D_j|\},
 \qquad
 J(M_\varepsilon)\le J(M_0)+2r_\Lambda.}
\tag{0.5}
\]

Uniformly for either parity layer,

\[
 \boxed{
 r_\Lambda=O\!\left(\frac{W\log ^2m}{m}\right),
 \qquad
 J(M_\varepsilon)=O\!\left(\frac{W\log ^2m}{m}\right).}
\tag{0.6}
\]

Here (W=\binom{2m+1}{m}).  Hence at (H=L\sqrt m), with fixed
(L), all choices satisfy

\[
 HJ(M_\varepsilon)=O_L\!\left(
       \frac{W\log ^2m}{\sqrt m}\right)=o(W).
\tag{0.7}
\]

The number of newly created run boundary edges is at most
(4r_\Lambda), while the total endpoint budget is at most

\[
 2J(M_0)+4r_\Lambda
 =O\!\left(\frac{W\log ^2m}{m}\right).
\tag{0.7a}
\]

Moreover, for every integer \(\ell\ge1\), the total
number of affected tokens lying in packets of length less than \(\ell\)
is less than \(\ell r_\Lambda).  In particular, at
(\ell=H=L\sqrt m), short packets contain only (o(W)) tokens.

There is also an exact simultaneous floor-descent identity.  For
(1\le q\le H\le m-2), arbitrary finite weights (w_q^+\ge0), and
the doubled factorial floor energy \(\mathcal Q_w\), define

\[
 \mathcal C_j=
 \sum_{q=1}^H w_q^+
 \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
       \binom{\mu_{j,q,U}}2,
\tag{0.8}
\]

where \(\mu_{j,q,U}\) is the number of phase-(j) tokens over
(S\in\mathcal D_j) having upper depth-(q) flag (U).  Fair
independent interval choices in the whole layer satisfy

\[
 \boxed{
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =\mathcal Q_w(M_0)-\sum_{j\in\Lambda}\mathcal C_j.}
\tag{0.9}
\]

At the first upper depth the reservoir vanishes identically:

\[
 \boxed{\mu_{j,1,U}\le1,
 \qquad \mathcal C_{j,1}=0.}
\tag{0.9a}
\]

Indeed, every interval corner is individually floor-energy-flat at
(q=1), not merely flat on average.  Thus every positive term in (0.9)
comes from (q\ge2).

Consequently one legal integral corner has floor-energy descent at least
(\mathcal C_\Lambda:=\sum_{j\in\Lambda}\mathcal C_j) while creating
at most (4r_\Lambda) new boundary edges.  In the half-floor convention
(\Phi=\mathcal Q/2), the guaranteed descent is
(\mathcal C_\Lambda/2).

For the two parity layers, if

\[
 \mathcal C_{\rm all}=\sum_{j=1}^{m-1}\mathcal C_j,
\tag{0.10}
\]

then the exact charged-coverage pigeonhole bound is

\[
 \boxed{
 \max\{\mathcal C_{\rm odd},\mathcal C_{\rm even}\}
 \ge\frac12\mathcal C_{\rm all}.}
\tag{0.11}
\]

This is not yet an iterative contraction theorem: no lower bound of
(\mathcal C_{\rm all}) by a fixed proportion of the complete
floor-excess is proved, and interval choices in overlapping odd and even
blocks are not covered by the simultaneous-legality argument.  These are
the two exact surviving gates.

## 1. Compatible fixed factors exist for both layers

For one disjoint layer, relations (0.3) can plainly be imposed block by
block.  In fact one fixed family can satisfy the conjugacy relation for
every adjacent pair simultaneously.  Choose any exact factor (F_1) on
([n]\setminus P_1), label the two points inside every pair, and set
recursively

\[
 F_{j+1}=\theta_jF_j,
 \qquad 1\le j<m.
\tag{1.1}
\]

Since \(\theta_j([n]\setminus P_j)=[n]\setminus P_{j+1}\), the image
of an exact factor is an exact factor on the required ground set.
Therefore (1.1) supplies one fixed collection usable by either parity
layer.  There is no cycle-consistency condition because the priority
indices form a path.

The theorem below only needs (0.3) for (j\in\Lambda).

## 2. The affected lower carriers are disjoint

If (j<k), every (S\in\mathcal D_j) avoids (P_j), whereas every
(T\in\mathcal D_k) meets (P_j).  Consequently

\[
 \boxed{\mathcal D_j\cap\mathcal D_k=\varnothing.}
\tag{2.1}
\]

For (S\in\mathcal D_j), write (e_j(S)) for its token in (F_j),
and (Y_j(S)) for the middle owner of that token.  Because
(\theta_jS=S) pointwise, the conjugate token over the same lower target
is

\[
 e_{j+1}(S)=\theta_je_j(S),
 \qquad
 Y_{j+1}(S)=\theta_jY_j(S).
\tag{2.2}
\]

Thus choosing a side never changes the lower target.  By (2.1), choosing
exactly one side for every affected target and retaining the base token
elsewhere saturates every lower target exactly once.

## 3. Exact simultaneous middle-owner legality

We prove that arbitrary tokenwise choices are middle-injective.  Interval
correlation is therefore harmless.

### 3.1 One block

Same-side owners over different lower targets are distinct by exactness
of (F_j) or (F_{j+1}).  Suppose a phase-(j) owner and a
phase-((j+1)) owner coincide:

\[
 Y_j(S)=Y_{j+1}(T)=\theta_jY_j(T).
\tag{3.1}
\]

The left-hand owner avoids (P_j), and the right-hand owner avoids
(P_{j+1}).  Their common value therefore avoids both pairs and is fixed
by \(\theta_j\).  Applying \(\theta_j\) to (3.1) gives
(Y_j(S)=Y_j(T)), whence (S=T) by the injectivity of the owner map in
(F_j).  A corner never chooses both tokens over one lower target, so no
mixed collision occurs.

### 3.2 Two disjoint blocks

Let (j<k) belong to \(\Lambda\).  By (0.1), (k\ge j+2).  Every
owner chosen over (S\in\mathcal D_j) avoids at least one of
(P_j,P_{j+1}): the phase-(j) owner avoids (P_j), and the
phase-((j+1)) owner avoids (P_{j+1}).

On the other hand, (T\in\mathcal D_k) meets every (P_h), (h<k),
and in particular meets both (P_j,P_{j+1}).  Every owner over (T)
contains (T), so it also meets both pairs.  An earlier-block owner and
a later-block owner therefore cannot be equal.  This argument is
independent of all side choices and of the detailed factors.

### 3.3 The unchanged background

Let (R\notin\bigcup_{j\in\Lambda}\mathcal D_j).  Its retained token is
the base token in (M_0).  A phase-(j) candidate over
(S\in\mathcal D_j) also belongs to (M_0), so it cannot collide with
that background token.

The phase-((j+1)) candidate belongs to the coherent first-avoided
matching obtained by globally swapping priority positions (j,j+1).
That coherent matching changes tokens exactly on \(\mathcal D_j\), so it
contains the same token over (R).  Its middle owners are distinct;
hence this candidate also cannot collide with the background.  Background
owners are mutually distinct because they occur in (M_0).

Sections 3.1--3.3 exhaust all owner pairs and prove simultaneous legality.

## 4. Physical fragmentation and the full-layer sum

Put

\[
 A_m=\binom{2m-1}{m-1},
 \qquad
 R_m=\frac{A_m}{2m-1}=\operatorname{Cat}_{m-1}.
\tag{4.1}
\]

In a row of (F_j), membership in \(\mathcal D_j\) says that the
length-((m-1)) window avoids (P_{j+1}) and meets every (P_h),
(h<j).  For one coordinate pair the avoiding starts form at most two
circular intervals, hence have at most four boundary edges.  The boundary
of the conjunction is contained in the union of the boundaries of these
(j) predicates.  It has at most (4j) boundary edges and at most
(2j) circular components.  Therefore

\[
 r_j\le\min\{2jR_m,|\mathcal D_j|\}.
\tag{4.2}
\]

Changing one packet removes one selected interval from its (F_j)-row
and inserts the conjugate interval in its (F_{j+1})-row.  Each operation
increases the number of runs by at most one.  Distinct blocks in one layer
use distinct source and destination factors.  Even without this last
observation, summing the one-packet bounds gives

\[
 J(M_\varepsilon)-J(M_0)\le2r_\Lambda.
\tag{4.3}
\]

Equivalently, the number of new run boundary edges is at most
(4r_\Lambda).

For completeness, the global sum does not lose a factor (m).  Let
(N_j) be the number of first-avoided category-(j) lower targets.
Then \(\mathcal D_j\subseteq\{S:\kappa(S)=j\}\), and the standard
Bernoulli-conditioning estimate gives an absolute (C) such that

\[
 |\mathcal D_j|\le N_j
 \le C\sqrt m\,A_m(3/4)^{j-1}.
\tag{4.4}
\]

Take (t=\lceil20\log m\rceil).  From (4.2)--(4.4), for either parity
layer (indeed, for every \(\Lambda\) satisfying (0.1)),

\[
\begin{aligned}
 r_\Lambda
 &\le \sum_{j\le t}2jR_m+\sum_{j>t}N_j\\
 &\le R_mt(t+1)+4C\sqrt m\,A_m(3/4)^t\\
 &=O\!\left(\frac{A_m\log ^2m}{m}\right)
  =O\!\left(\frac{W\log ^2m}{m}\right).
\end{aligned}
\tag{4.5}
\]

The exact ratios used in the last line are

\[
 \frac{A_m}{W}=\frac{m+1}{2(2m+1)},
 \qquad
 \frac{R_m}{W}=\frac{m+1}{2(2m-1)(2m+1)}.
\tag{4.6}
\]

The base matching itself has
(J(M_0)=O(W\log ^2m/m)), proving (0.6)--(0.7).

Finally, a packet of length less than \(\ell\) contains fewer than
(\ell) targets.  Since there are (r_\Lambda) packets,

\[
 \sum_{I:\,|I|<\ell}|I|<\ell r_\Lambda.
\tag{4.7}
\]

This is the exact long-block accounting; it does not assert that every
maximal interval is long.

## 5. Disjoint flag sectors and the multi-block Gram

Fix (j\in\Lambda), (S\in\mathcal D_j), and an upper depth
(1\le q\le H\le m-2).  Let (U_{j,q}(S)) be the phase-(j) upper
flag and put

\[
 d_{j,S,q}=\delta_{\theta_jU_{j,q}(S)}-
             \delta_{U_{j,q}(S)}.
\tag{5.1}
\]

Every lower flag is a subset of (S), so every lower innovation is zero.
For the upper innovation, the one-block calculation gives

\[
 \langle d_{j,S,q},d_{j,T,q}\rangle
 =2\mathbf1_{\{U_{j,q}(S)=U_{j,q}(T),\,
                   U_{j,q}(S)\cap P_{j+1}\ne\varnothing\}}.
\tag{5.2}
\]

There is an additional exact fact across blocks.  If (5.1) is nonzero,
then (U_{j,q}(S)) avoids (P_j), meets (P_{j+1}), and meets every
earlier pair.  Hence its first-avoided category in the base order is
exactly (j).  Its \(\theta_j\)-image has category exactly (j+1).
Thus

\[
 \operatorname{supp}d_{j,S,q}\subseteq
 \{U:\kappa(U)\in\{j,j+1\}\}.
\tag{5.3}
\]

The category pairs in (5.3) are disjoint for distinct
(j\in\Lambda).  Therefore

\[
 \boxed{
 \langle d_{j,S,q},d_{k,T,q}\rangle=0
 \quad(j\ne k\in\Lambda).}
\tag{5.4}
\]

Let \(\mathscr I_j\) be the interval packets of block (j), and set

\[
 z_{j,I,q}=\sum_{S\in I}d_{j,S,q},
 \qquad
 Z_{j,q}=\sum_{I\in\mathscr I_j}z_{j,I,q}.
\tag{5.5}
\]

Distinct proper cyclic windows of one row are distinct for
(q\le m-2).  Hence the token innovations inside one packet are
orthogonal.  Using (5.2),

\[
\begin{aligned}
 \|Z_j\|_w^2-
 \sum_{I\in\mathscr I_j}\|z_{j,I}\|_w^2
 &=4\sum_{q=1}^Hw_q^+
   \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
       \binom{\mu_{j,q,U}}2\\
 &=4\mathcal C_j.
\end{aligned}
\tag{5.6}
\]

Equations (5.4) and (5.6) show that passing to a full disjoint layer loses
none of the individual joined Gram gaps.

### 5.1 Exact nullity at the first upper rank

There is no charged curvature at (q=1).  Consider two occurrences in
(F_j) with the same rank-((m+1)) upper flag (U).  For one occurrence
with lower endpoint (S), the collar

\[
 C(S,U)=U\setminus S
\tag{5.7}
\]

has two points.  The two sets (U\setminus\{c\}), (c\in C(S,U)),
are exactly the two adjacent rank-(m) windows of that occurrence.  If a
second, distinct occurrence with lower endpoint (T) had
(C(S,U)\cap C(T,U)\ne\varnothing), then deleting a common collar point
would give a rank-(m) window occurring twice in (F_j).  Exactness of
the factor forbids this.  Hence collars belonging to distinct occurrences
of one (U) are disjoint.

Now suppose both lower endpoints lie in \(\mathcal D_j\) and
(U\cap P_{j+1}\ne\varnothing).  Since both (S) and (T) avoid
(P_{j+1}), every point of (U\cap P_{j+1}) lies in both collars.  The
collars intersect, a contradiction.  Therefore

\[
 \boxed{
 \mu_{j,1,U}\le1
 \quad\text{whenever }U\cap P_{j+1}\ne\varnothing,}
\tag{5.8}
\]

which proves \(\mathcal C_{j,1}=0\).

In fact the conclusion is pointwise over interval corners.  Let (x) be
the complete base load and let (U) be the nonfixed upper flag of a
changed occurrence.  By (5.8), the coherent block innovation has value
(-1) at (U) and (+1) at \(\theta_jU\), with no other changed
occurrence on this two-point orbit.  Pair symmetry says that the coherent
endpoint load is \(\theta_jx\).  Thus, writing

\[
 x_U=a,\qquad x_{\theta_jU}=b,
\]

the identity (x+Z_j=\theta_jx) gives (a-1=b) and (b+1=a).
Switching this occurrence merely changes the orbit loads

\[
 (a,b)=(b+1,b)\quad\longleftrightarrow\quad(b,b+1),
\tag{5.9}
\]

and preserves its collision and factorial-floor energy.  The nonfixed
orbits of different changed occurrences are disjoint: an equality
(U=\theta_jV), with both (U,V\subseteq[n]\setminus P_j), would force
both to avoid (P_{j+1}) and hence be fixed.  Therefore every tokenwise
choice, and in particular every simultaneous interval corner, has exactly
the same (q=1) floor energy as (M_0).

## 6. Exact simultaneous factorial-floor descent

For each global bit vector \(\eta\in\{0,1\}^{\Lambda}\), tie all
interval bits inside block (j) to \(\eta_j\).  The resulting matching
is the coherent first-avoided matching for the priority obtained by the
corresponding disjoint adjacent transpositions.

All these coherent corners have the same doubled factorial floor energy,
rank by rank.  Indeed, a global flip in block (j) permutes the load on
the category-(j,j+1) stratum by \(\theta_j\), fixes every lower flag,
and does not affect the disjoint strata belonging to the other blocks.
Write their common weighted energy as (Q_0=\mathcal Q_w(M_0)).

The fair global-bit ensemble and the fair independent-interval ensemble
have the same load midpoint.  At a fixed upper rank, the former has Haar
variance

\[
 \frac14\sum_{j\in\Lambda}\|Z_{j,q}\|_2^2,
\tag{6.1}
\]

whereas the latter has variance

\[
 \frac14\sum_{j\in\Lambda}
       \sum_{I\in\mathscr I_j}\|z_{j,I,q}\|_2^2.
\tag{6.2}
\]

Every corner has the same total mass.  Consequently the linear term and
the exact integer-floor minimum cancel when the two expectations are
subtracted.  Summing (5.6) over the layer proves

\[
 \mathbb E\mathcal Q_w(M_\varepsilon)
 =Q_0-\sum_{j\in\Lambda}\mathcal C_j,
\tag{6.3}
\]

 including the first upper rank, where the floor quotient is zero and the
 corresponding descent term is identically zero by Section 5.1.  No
 division by a floor quotient is used.

Since every interval corner is legal and obeys the deterministic boundary
bound, some integral corner simultaneously satisfies

\[
 \mathcal Q_w(M_\varepsilon)
 \le Q_0-\mathcal C_\Lambda,
 \qquad
 \partial_{\rm new}(M_\varepsilon)\le4r_\Lambda.
\tag{6.4}
\]

If (r_\Lambda>0), this may be recorded as the certified descent per
permitted new boundary edge

\[
 \frac{Q_0-\mathcal Q_w(M_\varepsilon)}{4r_\Lambda}
 \ge\frac{\mathcal C_\Lambda}{4r_\Lambda}.
\tag{6.5}
\]

Counting the endpoints already present in the coherent base as well, the
same corner satisfies the total-endpoint ratio

\[
 \boxed{
 \frac{Q_0-\mathcal Q_w(M_\varepsilon)}
      {,2J(M_0)+4r_\Lambda,}
 \ge
 \frac{\mathcal C_\Lambda}
      {,2J(M_0)+4r_\Lambda,}.}
\tag{6.6}
\]

The denominator in (6.6) is
(O(W\log ^2m/m)=o(W/H)) at (H=L\sqrt m).

No positive universal lower bound on the right side has been proved.

## 7. What the two parity layers charge

For a duplicate pair of phase-(j) upper occurrences with common flag
(U), the collision is charged by block (j) exactly when

1. (U\cap P_{j+1}\ne\varnothing); and
2. both lower endpoints avoid (P_{j+1}), equivalently both belong to
   \(\mathcal D_j\).

The category of (U) is then (j), so a charged collision belongs to a
unique index (j).  Odd and even layers partition these indices.  This
proves (0.11).  A purely multiplicity-form lower bound is also available.
Put

\[
 a_{j,q}=\sum_{U:\,U\cap P_{j+1}\ne\varnothing}\mu_{j,q,U},
 \qquad
 K_{j,q}=|\{U:\mu_{j,q,U}>0,\ U\cap P_{j+1}\ne\varnothing\}|.
\tag{7.1}
\]

When (K_{j,q}>0), Cauchy--Schwarz gives

\[
 \boxed{
 \sum_{U:\,U\cap P_{j+1}\ne\varnothing}
       \binom{\mu_{j,q,U}}2
 \ge\frac12\left(\frac{a_{j,q}^2}{K_{j,q}}-a_{j,q}\right).}
\tag{7.2}
\]

Thus (0.11) and (7.2) are a literal charged-coverage lower bound for one
of the two layers.  They become a quantitative contraction once one
proves that the right-hand side captures a stated fraction of the current
floor excess.

The present structure alone does not prove that comparison.  Collisions
whose common flag avoids (P_{j+1}), collisions for which one lower
window already contains (P_{j+1}), and the final category (j=m) are
uncharged by (0.8).  Therefore replacing \(\mathcal C_{\rm all}\) by the
complete floor energy would be an additional theorem, not a consequence
of simultaneous legality.

The (q=1) part of this failure is absolute rather than merely
uncontrolled: Section 5.1 proves that the entire first-upper-rank layer is
flat at every interval corner.  Any contraction supplied by this atlas
must be charged at depths (2\le q\le H).

## 8. Exact iterative boundary

The legality proof uses (k\ge j+2) in Section 3.2.  It therefore applies
to every odd layer and every even layer separately.  It does not show
that an odd mixed interval corner can be used as the unchanged background
for an even mixed interval update: adjacent charts (j) and (j+1)
share (P_{j+1}), and a phase-((j+1)) owner from the earlier chart and
an owner from the later chart can both avoid that pair.  The separating
category argument then disappears.

Accordingly, a genuine iteration requires one of the following precise
additional statements:

1. an owner-collision theorem for overlapping adjacent charts, possibly
   after a state-adaptive packet restriction of total mass (o(W)); or
2. a reset/re-encoding theorem which returns a descended interval corner
   to a coherent first-avoided base at (o(W)) energy and
   (o(W/H)) boundary cost.

Together with a lower bound

\[
 \mathcal C_{\rm all}\ge\gamma_m\mathcal Q_w(M_0)-o(W),
\tag{8.1}
\]

at a rate \(\gamma_m\) large enough relative to the number of permitted
iterations, either statement would turn (6.3) into an iterative
contraction.  Neither (8.1) nor the overlapping-layer compatibility is
proved here.  Thus this note establishes the complete one-layer legality
and additive floor descent, but makes no constant-one claim.
