# K16 C106 full-arc group hull, return toll, and robust R2--R4 cuts

Date: 2026-07-30  
Status: **proved for the frozen source-relative seam catalogue; no R2--R4 feasibility verdict is claimed**

## 1. Scope and notation

Let \(E\) be the authenticated catalogue of 211,604 direction-coherent
length-eight K16 seams.  Its port set is \(V\).  For a seam \(e:u\to v\),
write

\[
 h_e\in\{0,1\}^{D},\qquad j_e:=|h_e|\in\{0,1,2\},
 \qquad s_e\in\{0,1,\ldots,7\}
\]

for its incidence on the 93 frozen source defects and its exact scale-two
direct-dual slack.  There is no seam hitting two lower defects.  The direct
certificate supplies target prices \(b_t\in\{1,2,4\}\) and an integer port
potential \(y\) such that

\[
 s_e=2+y_v-y_u-b\mathbin\cdot h_e\ge0.                 \tag{1.1}
\]

The fifteen price-one lock targets are partitioned into the five triples

\[
\begin{aligned}
T_1&=\{35044,36935,40066\},&
T_2&=\{37320,41102,47364\},\\
T_3&=\{33906,36417,51235\},&
T_4&=\{33337,50976,58385\},\\
T_5&=\{41872,49436,61960\}.&&
\end{aligned}                                           \tag{1.2}
\]

Throughout this note \(x_e\ge0\) is allowed to be real.  The port equations
are

\[
 \sum_{e\in\delta^+(v)}x_e=
 \sum_{e\in\delta^-(v)}x_e,
 \qquad
 \sum_{e\in\delta^+(v)}x_e\le1                       \tag{1.3}
\]

for every \(v\), and the seam count is

\[
                         \sum_e x_e=106.               \tag{1.4}
\]

Thus every integral capacity-one circulation is included, but all results
below remain valid for the full continuous relaxation.  In particular, no
individual-row truncation \(s_e\le R\) is made.

## 2. The only safe all-arc SCC reduction

### Lemma 2.1 (positive balanced arcs are cycle eligible)

If \(x\ge0\) satisfies the balance equations in (1.3), then every seam with
\(x_e>0\) lies on a directed cycle contained in the positive support of
\(x\).  Consequently its two endpoints lie in one strongly connected
component of the full directed seam graph.

#### Proof

Fix a positive seam \(e:u\to v\), and let \(W\) be the set of vertices
reachable from \(v\) in the positive-support digraph.  If \(u\notin W\), no
positive seam leaves \(W\), while \(e\) is a positive seam entering \(W\).
Summing the balance equations over \(W\) would then say that its zero
outflow equals a strictly positive inflow, a contradiction.  Hence there is
a positive directed path from \(v\) back to \(u\), and this path together
with \(e\) contains a directed cycle through \(e\).  \(\square\)

The full all-slack graph has 211,469 authenticated cycle-eligible seams; the
remaining 135 can be discarded even fractionally.  This is the only SCC
filter used here.  For \(R>0\), discarding seams merely because \(s_e>R\) is
not sound for a continuous flow: such a seam may occur with mass at most
\(R/s_e\).

## 3. The exact partition-matroid hull of all signatures

Fix \(R\in\{0,1,2,3,4,5\}\) and put \(Q=5-R\).  Let
\(L=\bigcup_iT_i\).
Define the demand polytope

\[
\begin{split}
\mathcal D_R=\{d:\;&d_t=1\quad(t\notin L),\\
&d_t=1+u_t\quad(t\in L),\quad u_t\ge0,\\
&\sum_{t\in T_i}u_t\le1\quad(i=1,\ldots,5),\\
&\sum_{t\in L}u_t=Q\}.                                \tag{3.1}
\end{split}
\]

### Lemma 3.1 (normal-form convex hull)

\(\mathcal D_R\) is exactly the convex hull of the
\(\binom5Q3^Q\) fixed C106 lock signatures having \(R\) symbols `S`.

#### Proof

Put \(w_i=\sum_{t\in T_i}u_t\).  The projection in the \(w\)-coordinates is
the hypersimplex

\[
                  0\le w_i\le1,\qquad\sum_iw_i=Q.
\]

Its vertices are the zero-one vectors with exactly \(Q\) ones, so write an
arbitrary \(w\) as a convex combination of their incidence vectors.  In a
term whose chosen group set contains \(i\), independently choose a target
\(t\in T_i\) with probability \(u_t/w_i\) (groups with \(w_i=0\) never
occur).  After also averaging these target choices, the expected coordinate at \(t\)
is

\[
 \Pr(i\text{ chosen})\frac{u_t}{w_i}=w_i\frac{u_t}{w_i}=u_t.
\]

Thus every point of (3.1) is a convex combination of normal-form signatures.
The reverse inclusion is immediate from the displayed constraints.  \(\square\)

Every \(d\in\mathcal D_R\) has the two exact totals

\[
                  \mathbf1\mathbin\cdot d=98-R,
          \qquad b\mathbin\cdot d=207+Q=212-R.         \tag{3.2}
\]

### Lemma 3.2 (the slack row is redundant on the group hull)

If \(x\) satisfies (1.3)--(1.4) and \(Hx=d\in\mathcal D_R\), then

\[
                         \sum_es_ex_e=R.               \tag{3.3}
\]

#### Proof

Multiply (1.1) by \(x_e\) and sum.  Balance cancels the endpoint potential,
so

\[
 \sum_es_ex_e=2\sum_ex_e-b\mathbin\cdot Hx
              =212-(212-R)=R.                         \tag{3.4}
\]

No integrality was used.  \(\square\)

Thus the full-arc **group-convex relaxation** is exactly whether the target image of the
count-106 capacity-circulation polytope meets \(\mathcal D_R\).  High-slack
fractional seams are retained automatically; their total is controlled by
(3.3).

## 4. One complete rational cut system for R2--R4

Let

\[
 \mathcal X_{106}=\{x\ge0:\text{(1.3) and (1.4) hold}\},
 \qquad
 \Phi(\lambda)=\max_{x\in\mathcal X_{106}}
                    \sum_e(\lambda\mathbin\cdot h_e)x_e.             \tag{4.1}
\]

This support function uses every full-catalogue seam.  It does not depend on
\(R\).  With the balance convention

\[
 (Bx)_v=\sum_{e\in\delta^+(v)}x_e-
        \sum_{e\in\delta^-(v)}x_e,
\]

ordinary LP duality gives the finite formula

\[
\boxed{
\begin{aligned}
\Phi(\lambda)=\min\;&106\kappa+\sum_{v\in V}q_v\\
\text{subject to }&q_v\ge0,\quad \kappa\in\mathbb R,
                    \quad p_v\in\mathbb R,\\
&q_u\ge \lambda\mathbin\cdot h_e-\kappa+p_u-p_v
                     \qquad(e:u\to v\in E).
\end{aligned}}                                         \tag{4.2}
\]

For \(\lambda\in\mathbb R^D\), put

\[
 a_i(\lambda)=\min_{t\in T_i}\lambda_t
\]

and write \(a_{(1)}\le\cdots\le a_{(5)}\) for these five numbers in
nondecreasing order.  The lower support of the signature hull is

\[
 \ell_R(\lambda):=\min_{d\in\mathcal D_R}\lambda\mathbin\cdot d
 =\sum_{t\in D}\lambda_t+\sum_{j=1}^{5-R}a_{(j)}(\lambda).             \tag{4.3}
\]

Indeed, one puts the \(Q=5-R\) units into the \(Q\) cheapest lock triples
and, in each, onto a cheapest target.

### Theorem 4.1 (exact group-hull Farkas criterion)

For fixed \(R\), the full continuous capacity relaxation contains some
demand in the convex hull \(\mathcal D_R\) if and only if

\[
                         \ell_R(\lambda)\le\Phi(\lambda)              \tag{4.4}
\]

for every \(\lambda\in\mathbb R^D\).

Equivalently, a theorem-grade rational certificate excluding the whole
convex hull, and hence **all** fixed signatures at that \(R\), consists of rational

\[
 \lambda_t,\quad\kappa,\quad p_v,\quad q_v\ge0
\]

such that every one of the 211,604 column inequalities in (4.2) holds and

\[
 106\kappa+\sum_vq_v
 <\sum_t\lambda_t+\sum_{j=1}^{5-R}a_{(j)}(\lambda).                    \tag{4.5}
\]

#### Proof

Let \(K=H(\mathcal X_{106})\).  Both \(K\) and \(\mathcal D_R\) are compact
rational polytopes.  They meet if and only if, for every linear functional,
the minimum over \(\mathcal D_R\) is at most the maximum over \(K\).  The two
support values are (4.3) and (4.1).  If they are disjoint, strict separation
provides a \(\lambda\) violating (4.4).  Formula (4.2) is the dual of (4.1):
for every feasible \(x\), multiply its column inequalities by \(x_e\), use
balance to cancel \(p_u-p_v\), use the count equation, and then use the tail
capacities to obtain

\[
 \lambda\mathbin\cdot Hx\le106\kappa+\sum_vq_v.
\]

Strong LP duality gives equality at the optimum.  Rational polyhedral
separation and rational LP duality permit all certificate entries to be
rational.  \(\square\)

The three requested inequalities are therefore explicitly

\[
\begin{array}{c|c}
R&\ell_R(\lambda)\\ \hline
2&\displaystyle\sum_t\lambda_t+a_{(1)}+a_{(2)}+a_{(3)},\\[2mm]
3&\displaystyle\sum_t\lambda_t+a_{(1)}+a_{(2)},\\[2mm]
4&\displaystyle\sum_t\lambda_t+a_{(1)}.
\end{array}                                             \tag{4.6}
\]

The right side \(\Phi(\lambda)\) is common to all three rows.  In
particular, a rational ray obtained from one group LP should be evaluated on
all three ordered-minimum expressions before a new solve is attempted.

For an individual signature \(\alpha\), the same cut excludes it whenever

\[
 \sum_t\lambda_t+
 \sum_{i:\alpha_i\ne S}\lambda_{t_i(\alpha)}
 >106\kappa+\sum_vq_v.                                 \tag{4.7}
\]

Thus one ray classifies a Cartesian family of signature digits.

### Corollary 4.2 (constructive fixed face)

Suppose a rational tuple \((\lambda,\kappa,p,q)\) satisfies every column
inequality in (4.2) and has

\[
 106\kappa+\sum_vq_v=\ell_R(\lambda).
\]

If a signature demand \(d\) and a feasible flow \(x\in\mathcal X_{106}\)
satisfy \(Hx=d\), then:

1. its \(Q\) repeated groups are \(Q\) groups attaining the \(Q\) smallest
   values \(a_i(\lambda)\), and each repeated target minimizes \(\lambda\)
   in its group (up to ties);
2. every used seam satisfies equality in its column of (4.2);
3. every port with \(q_v>0\) is saturated to outgoing mass one.

#### Proof

The chain

\[
 \ell_R(\lambda)\le\lambda\mathbin\cdot d
 =\lambda\mathbin\cdot Hx\le\Phi(\lambda)=\ell_R(\lambda)
\]

has equality throughout.  The first equality gives item 1.  Complementary
slackness in the proof of (4.2) gives items 2 and 3.  \(\square\)

This is a proof-guided construction face, not merely an infeasibility test.

## 5. Exact universal return-toll identity

Let

\[
 E_{00}=\{e:j_e=0,\ s_e=0\}.
\]

### Theorem 5.1 (tight-hitless compensation)

Every full-arc C106 group-hull circulation, fractional or integral, obeys

\[
 \boxed{\sum_e(1-j_e-s_e)x_e=8}                         \tag{5.1}
\]

and therefore

\[
 \boxed{
 x(E_{00})=8+
 \sum_{e:j_e+s_e\ge2}(j_e+s_e-1)x_e.}                  \tag{5.2}
\]

#### Proof

By (1.4), (3.2), and (3.3),

\[
 \sum_e(1-j_e-s_e)x_e
 =106-(98-R)-R=8.                                      \tag{5.3}
\]

Because \(j_e,s_e\) are nonnegative integers, the coefficient
\(1-j_e-s_e\) is \(+1\) exactly on \(E_{00}\), is zero exactly for a tight
singleton or a slack-one hitless seam, and is negative otherwise.
Rearranging (5.1) gives (5.2).  \(\square\)

Consequences include the signature-independent cuts

\[
                         x(E_{00})\ge8,                 \tag{5.4}
\]

and, since every double-provider seam has \(j_e=2\),

\[
                         x(E_{00})-x(\{j_e=2\})\ge8.   \tag{5.5}
\]

More precisely, a positive provider seam of slack \(s\) costs at least
\(s\) additional units on the right of (5.2), while a hitless seam of slack
\(s\ge2\) costs \(s-1\).

Define the toll

\[
 \tau(x)=\sum_{j_e+s_e\ge2}(j_e+s_e-1)x_e.
\]

Then \(x(E_{00})=8+\tau(x)\).  The minimum-toll face \(\tau=0\) has the
following exact mass ledger:

\[
\begin{array}{c|c}
\text{seam type}&\text{mass}\\ \hline
(j,s)=(0,0)&8,\\
(j,s)=(1,0)&98-R,\\
(j,s)=(0,1)&R,
\end{array}                                             \tag{5.6}
\]

and every other type has mass zero.  Thus (5.6) is the first constructive
face to test at \(R=2,3,4\).  If it is empty, (5.2) gives an exact increasing
toll hierarchy; high-slack fractional arcs do not evade it.

There is also a finite capacity cut.  Let \(\mu_{00}\) be the maximum
matching size in the bipartite graph whose left and right classes are copies
of the ports and whose edges are the seams in \(E_{00}\).  Restricting a
feasible \(x\) to \(E_{00}\) gives a fractional bipartite matching, hence

\[
                  \tau(x)\le\mu_{00}-8.                \tag{5.7}
\]

This may equivalently be certified by a vertex cover of the \(E_{00}\)
graph.  Equation (5.7) is symbolic here; no numerical value of
\(\mu_{00}\) is claimed.

## 6. High-slack-safe endpoint Hall cuts

The exact support criterion (4.4) is complete but may have a large rational
dual.  The following weaker cut family is combinatorial and explicitly
protects against high-slack fractional arcs.

Let \(w_t\ge0\) be rational target weights and put

\[
 w(h_e)=\sum_{t\in H(e)}w_t,
 \qquad c(w)=\max_{e\in E}w(h_e).                       \tag{6.1}
\]

For an integer \(K\ge0\), let \(M_K(w)\) be the maximum weight of a
bipartite matching of seams with \(s_e\le K\), where seam \(e\) has weight
\(w(h_e)\) and its endpoints are its tail and head port copies.  Equivalently,
\(M_K(w)\) is the optimum of the fractional tail/head-capacity LP; it is
integral when the edge weights are integral.

### Theorem 6.1 (robust low-slack matching cut)

Every C106 normal-form realization at slack \(R\), even a fractional one,
satisfies

\[
 \boxed{
 \ell_R(w)\le M_K(w)+\frac{c(w)R}{K+1}.}                \tag{6.2}
\]

#### Proof

Restrict \(x\) to seams with \(s_e\le K\).  The outgoing capacity and, by
balance, the incoming capacity are at most one at every port.  Hence this
restriction is a fractional bipartite matching and its \(w\)-service is at
most \(M_K(w)\).

On the remaining seams \(s_e\ge K+1\).  The exact slack equation gives

\[
 \sum_{s_e\ge K+1}x_e\le\frac{R}{K+1},
\]

so their \(w\)-service is at most \(c(w)R/(K+1)\).  Finally every fixed
signature demand has \(w\cdot d\ge\ell_R(w)\).  \(\square\)

For a target set \(A\subseteq D\), take \(w=\mathbf1_A\) and define

\[
 g(A)=|\{i:T_i\subseteq A\}|.
\]

Then

\[
                         \ell_R(\mathbf1_A)
 =|A|+\max(0,g(A)-R).                                  \tag{6.3}
\]

Indeed, among the five group minima there are \(5-g(A)\) zeroes and
\(g(A)\) ones.

If \(A\) consists only of lower defects, no seam hits two members of \(A\),
so \(c(\mathbf1_A)\le1\).  Taking \(K=R\) in (6.2), using integrality of the
matching optimum, and observing \(R/(R+1)<1\), gives the exact necessary
conditions

\[
\boxed{
\begin{array}{ll}
R=2:&M_2(A)\ge |A|+\max(0,g(A)-2),\\
R=3:&M_3(A)\ge |A|+\max(0,g(A)-3),\\
R=4:&M_4(A)\ge |A|+\max(0,g(A)-4).
\end{array}}                                           \tag{6.4}
\]

These are endpoint-capacity Hall cuts on the entire catalogue, not on the
662-seam `SSSSS` support.  Fractional use of seams with \(s_e>R\) contributes
strictly less than one unit and therefore cannot repair a one-unit integral
matching deficit in (6.4).

For an arbitrary target set, \(c(\mathbf1_A)\le2\).  Taking \(K=2R\) yields

\[
                 M_{2R}(A)\ge |A|+\max(0,g(A)-R).       \tag{6.5}
\]

For \(R=2,3\), this uses respectively the slack-at-most-four and
slack-at-most-six graphs while remaining valid against every higher-slack
fractional seam.  For \(R=4\), \(2R=8\) contains the whole catalogue, so
(6.5) reduces to the ordinary full endpoint-matching cut.

Finally, the authenticated double-provider graph has 18 pair-isolated
targets, none belonging to a lock triple.  If \(A\) is any subset of these
targets, every seam meeting \(A\) has \(w(h_e)\le1\), \(g(A)=0\), and (6.4)
gives

\[
                         M_R(A)\ge|A|.                  \tag{6.6}
\]

In particular, the slack-at-most-\(R\) provider graph on all eighteen must
have endpoint matching number at least eighteen.  This is necessary, not
sufficient: it does not by itself enforce distinct target labels inside the
matching.

## 7. Exact proved boundary

The following statements are now theorem-grade for \(R=2,3,4\).

1. The continuous group-convex relaxation is exactly the intersection problem
   \(H(\mathcal X_{106})\cap\mathcal D_R\), with no separate slack row and no
   high-slack truncation.
2. Equations (4.2)--(4.6) are a complete rational Farkas interface for the
   convex hull of all signatures at fixed \(R\).  Feasibility of this hull
   need not yield a feasible fixed signature.
3. The return-toll identity (5.2) and the endpoint matching cuts
   (6.2)--(6.6) hold for all full-arc fractional points.
4. The minimum-toll ledger (5.6) is an explicit first construction face.

No rational ray excluding \(R=2,3,\) or \(4\), and no feasible circulation
at any of those values, is proved here.  Running disjunctive or group LP
statuses remain numerical evidence until a rational certificate is replayed
against all 211,604 columns.  In particular, a negative solve on
`row_slack <= R` is only an integral-WLOG presolve result and is not promoted
to a continuous theorem.

## 8. Adversarial audit

* **Why high-slack arcs are not silently removed.**  They occur in every
  column inequality in (4.2).  In Section 6 they are bounded only by the
  exact aggregate slack identity, not deleted.
* **Why the slack equality may be omitted in Section 4.**  This is valid only
  after count 106, balance, and \(Hx\in\mathcal D_R\) are imposed.  Lemma 3.2
  proves that any point in the intersection automatically has slack \(R\).
  It is not a claim about an arbitrary capacity circulation.
* **Why one-sided capacity suffices in (4.2).**  Balance turns outgoing
  capacity at a port into the identical incoming bound.  Section 6 uses both
  only after restricting a feasible balanced flow to a subset of its seams.
* **Why matching cuts are not claimed sufficient.**  Restricting to low
  slack destroys balance, chronology, and target-label exactness.  It remains
  a fractional bipartite matching, which is enough only for the upper bound
  used in Theorem 6.1.
* **Why (5.2) is not an integrality argument.**  It uses only three exact
  real equalities: count, total target service, and total direct slack.

## 9. Frozen lineage

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cycle_dual_exact_20260730.audit.json
  SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d

scratch/k16_c106_lock_normal_form_20260730.audit.json
  SHA-256 975f8847ecedb0c40ac5ba92aea03dab814cf004490bbf0fb6dc092f5bc3e2bb

scratch/k16_defect_provider_edge_cover_20260730.audit.json
  SHA-256 7e0d51edfa2c933eea20808e43ea1445672cfe25e60f68afe3ed11e05c56ed27

MATH_CORRECTION_K16_C106_CONTINUOUS_ROW_SLACK_TRUNCATION_20260730.md
  SHA-256 cdb5b45b9cb6752baea96a699f6b0c287adabb4dc23a903c096fb463e21e2867

scratch/k16_floor106_r1_group_convex_full_20260730.audit.json
  SHA-256 4791d9f784aac7cb6c6e65e1086cc6c527a28020356504dfa24612107f695e63
```

This note does not rerun C105 and does not modify the frozen floor-106
theorem.
