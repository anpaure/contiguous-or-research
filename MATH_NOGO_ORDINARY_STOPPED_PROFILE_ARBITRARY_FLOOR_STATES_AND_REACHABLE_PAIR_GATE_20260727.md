# Ordinary stopped profiles: deterministic optimality, an arbitrary-state no-go, and the reachable pair gate

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad r=m-q_0,\qquad
 q_0=a\sqrt m+O(1),\qquad H=b\sqrt m+O(1),
\]

where \(0<a<b\) are fixed, and put

\[
 J=H-q_0=(b-a)\sqrt m+O(1),\qquad
 V_d=\binom{[n]}{r-d},\qquad N_d=|V_d|.
\]

This note audits the stopped-profile target of
`MATH_THEOREM_ORDINARY_ANNULAR_STOPPED_PROFILE_FUNCTIONAL_20260727.md`.
It has three conclusions.

1. **Randomization gives no one-step advantage.**  At any fixed state and
   fixed bite size, the least possible conditional stopped-profile drift is
   attained by a deterministic bite.  For one packet \(e\), its exact signed
   loss is

   \[
    \boxed{
    \ell_{\mathcal M}(e)
      =\sum_{d=0}^J
        \bigl(|e_d\cap S_d|-(n-c_d)\bigr).}
   \tag{0.1}
   \]

   Thus a stochastic hole-biased law can help only by making a useful
   trajectory likely; at a fixed residual it cannot beat the best legal
   deterministic packet.

2. **No uniform statewise theorem is possible.**  There are integer load
   profiles \((\mu_d)_{d=0}^J\), each exactly at its separate-rank
   integrality floor,

   \[
     \mu_d\in\{0,1\},\qquad
     \sum_{T\in V_d}\mu_d(T)=G,
   \tag{0.2}
   \]

   and with at least one entrance-legal packet, for which every packet
   satisfies

   \[
      \ell(e)\ge c_{a,b}m^{3/2}.
   \tag{0.3}
   \]

   More generally every nonempty bite of \(s\) packets, as long as the bite
   stays below scalar saturation, has drift at least

   \[
      c_{a,b}s m^{3/2}.
   \tag{0.4}
   \]

   The profiles may be made complement-coherent on the upper shore.  Hence
   layer sizes, balanced integer loads, complement symmetry, complete-
   catalogue degrees, codegrees, and time-zero pair profiles do not imply
   the stopped-profile inequality for arbitrary states.

3. **The missing input is genuinely reachability-specific.**  The profiles
   in (0.2)--(0.4) are not proved to be the supports of one common entrance
   matching.  They therefore do not refute the desired process.  They show
   that a valid theorem must exploit the representation

   \[
      S_d=\bigcup_{f\in\mathcal M}f_d
   \tag{0.5}
   \]

   for the *same* packet family at every depth.  An exact common-interval
   sufficient condition for such reachable states is proved in Section 4.
   It includes the same-bite coalescence term and identifies the remaining
   target as a floor-correct, trajectory-level pair profile, not a
   time-zero degree/codegree estimate.

The no-go is at exactly the scale relevant to the proof.  A critical
matching selects \(\Theta(W/n)\) packets, so the allowed average profile
drift is \(o(n)\).  The arbitrary floor states below force
\(\Theta(n\sqrt m)\) drift per packet, a factor \(\sqrt m\) too large.

## 1. Exact deterministic optimum of a conditional bite law

Let \(\mathcal M\) be a current entrance matching.  Write

\[
 G=n|\mathcal M|,\qquad
 S_d=\bigcup_{f\in\mathcal M}f_d,\qquad
 \mathcal H_d=V_d\setminus S_d.
\tag{1.1}
\]

For a bite \(\mathcal B\) of \(s\) new packets, put

\[
 c_d=\min\{G+ns,N_d\}-\min\{G,N_d\},
\tag{1.2}
\]

\[
 \nu_{d,\mathcal B}(T)
   =|\{e\in\mathcal B:T\in e_d\}|,
\tag{1.3}
\]

and

\[
 Z_d(\mathcal B)
   =\left|\left(\bigcup_{e\in\mathcal B}e_d\right)
                 \cap\mathcal H_d\right|.
\tag{1.4}
\]

The exact bite loss is

\[
 L_{\mathcal M}(\mathcal B)=\sum_{d=0}^J(c_d-Z_d(\mathcal B)).
\tag{1.5}
\]

### Lemma 1.1 (occurrence decomposition)

For every bite,

\[
 \boxed{
 \begin{aligned}
 L_{\mathcal M}(\mathcal B)
 &= -\sum_{d=0}^J(ns-c_d)
    +\sum_{d=0}^J\sum_{T\in S_d}\nu_{d,\mathcal B}(T)\\
 &\quad+
    \sum_{d=0}^J\sum_{T\in\mathcal H_d}
       (\nu_{d,\mathcal B}(T)-1)_+ .
 \end{aligned}}
\tag{1.6}
\]

The second line is precisely same-bite coalescence on current holes.

#### Proof

At depth \(d\), the bite has \(ns=\sum_T\nu(T)\) occurrences, while

\[
 Z_d=\sum_{T\in\mathcal H_d}{\bf1}_{\{\nu(T)>0\}}.
\]

Consequently

\[
 ns-Z_d
 =\sum_{T\in S_d}\nu(T)
  +\sum_{T\in\mathcal H_d}
       \bigl(\nu(T)-{\bf1}_{\{\nu(T)>0\}}\bigr),
\]

and the last parenthesis equals \((\nu(T)-1)_+\).  Add
\(c_d-ns\) and sum over \(d\). \(\square\)

For \(s=1\), the coalescence term vanishes and (1.6) becomes (0.1).

### Theorem 1.2 (deterministic conditional optimum)

Fix the current state and a nonempty finite family
\(\mathfrak B_s(\mathcal M)\) of legal bites of size \(s\).  For every
conditional probability law \(\pi\) on this family,

\[
 \boxed{
 \mathbb E_\pi L_{\mathcal M}(\mathcal B)
 \ge
 \min_{\mathcal B\in\mathfrak B_s(\mathcal M)}
       L_{\mathcal M}(\mathcal B).}
\tag{1.7}
\]

Equality is attained by a point mass on a minimizing bite.

#### Proof

The conditional expectation is a convex combination of the finitely many
numbers \(L_{\mathcal M}(\mathcal B)\). \(\square\)

Thus there is no probabilistic improvement hidden inside the one-step law.
Probability is useful only for proving that the sequence of states produced
by a scheduler remains in a class having small deterministic minimum loss.

## 2. Random floor profiles with no good packet

We now construct the arbitrary-state obstruction.

Choose

\[
 \rho={1\over4}{N_J\over N_0}>0,
 \qquad
 G=n\left\lfloor{\rho N_0\over n}\right\rfloor.
\tag{2.1}
\]

The Gaussian annulus ratio formula gives

\[
 {N_J\over N_0}
 =\exp[-(b^2-a^2)+o(1)],
\tag{2.2}
\]

so \(\rho=\rho_{a,b}+o(1)\) is bounded below by a positive constant.
Moreover, for all sufficiently large \(m\),

\[
 G+n\le N_J\le N_d\qquad(0\le d\le J).
\tag{2.3}
\]

Fix one packet \(e^*\).  Choose any \(G\)-set

\[
 S_0\subseteq V_0\setminus e^*_0.
\tag{2.4}
\]

For every \(1\le d\le J\), independently choose \(S_d\) uniformly from
the \(G\)-subsets of \(V_d\).  Define the formal integer loads

\[
 \mu_d(T)={\bf1}_{\{T\in S_d\}}.
\tag{2.5}
\]

Every separate rank is perfectly balanced: its mass is \(G<N_d\), its
support has size \(G\), its floor-correct support deficit is zero, and its
floor-correct pair energy is zero.

### Lemma 2.1 (uniform lower tail for one packet)

For a fixed packet \(e\), put

\[
 X_e=\sum_{d=1}^J|e_d\cap S_d|.
\tag{2.6}
\]

Then

\[
 \mathbb E X_e
   =\sum_{d=1}^J {nG\over N_d}
   \ge {\rho nJ\over2}
\tag{2.7}
\]

for all sufficiently large \(m\), and

\[
 \Pr\left(X_e\le{\rho nJ\over4}\right)
 \le \exp[-c_{a,b}nJ].
\tag{2.8}
\]

#### Proof

At depth \(d\), \(|e_d\cap S_d|\) is hypergeometric with population
\(N_d\), sample size \(G\), and \(n\) distinguished elements.  Its mean
is \(nG/N_d\ge nG/N_0\ge\rho n/2\).  The indicators in a uniform sample
without replacement are negatively associated.  Samples at different
depths are independent.  The standard multiplicative Chernoff argument,
which uses only the corresponding product-moment inequality, therefore
gives

\[
 \Pr(X_e\le\tfrac12\mathbb EX_e)
 \le\exp[-\mathbb EX_e/8].
\]

This implies (2.8). \(\square\)

### Theorem 2.2 (all-packet arbitrary-state obstruction)

There is a deterministic choice of \(S_1,\ldots,S_J\) such that

\[
 \boxed{
 X_e\ge c_{a,b}m^{3/2}
 \quad\hbox{for every ordinary cyclic packet }e.}
\tag{2.9}
\]

In addition, \(e^*\) is entrance-legal relative to \(S_0\).

#### Proof

The number of unoriented cyclic orders is \((n-1)!/2\), and hence

\[
 \log((n-1)!/2)=O(m\log m)=o(m^{3/2})=o(nJ).
\tag{2.10}
\]

Union bound (2.8) over all cyclic orders.  The total failure probability
tends to zero, so a deterministic choice satisfying (2.9) exists.  The
legality of \(e^*\) follows from (2.4). \(\square\)

### Corollary 2.3 (one-packet and whole-bite failure)

For the profile in Theorem 2.2, every entrance-legal packet has

\[
 L(e)\ge c_{a,b}m^{3/2}.
\tag{2.11}
\]

More generally, every nonempty bite \(\mathcal B\) of \(s\) packets with

\[
 G+ns\le N_J
\tag{2.12}
\]

satisfies

\[
 \boxed{L(\mathcal B)\ge c_{a,b}s m^{3/2}.}
\tag{2.13}

This remains true after restricting to entrance-disjoint bites.

#### Proof

By (2.3), \(c_d=ns\) at every depth.  For each \(d\),

\[
 \begin{aligned}
 Z_d(\mathcal B)
 &\le\sum_{e\in\mathcal B}|e_d\cap(V_d\setminus S_d)|\\
 &=ns-\sum_{e\in\mathcal B}|e_d\cap S_d|.
 \end{aligned}
\tag{2.14}
\]

Therefore

\[
 \sum_d(c_d-Z_d)
 \ge\sum_{e\in\mathcal B}\sum_{d=1}^J|e_d\cap S_d|,
\]

and (2.9) proves (2.13).  The case \(s=1\) proves (2.11). \(\square\)

If an upper profile is desired, define it by taking complements of the
lower targets.  The cyclic-interval complementation identity then makes
the obstruction exactly complement-coherent.

## 3. What the obstruction proves, and what it does not

The construction has all of the following properties.

* Every rank has the correct common occurrence mass \(G\).
* Every rank is exactly at the integer support and pair-energy floor.
* The entrance residual contains a legal packet.
* The lower and upper profiles may be made complement-coherent.
* The underlying ordinary catalogue retains all its exact regular degrees,
  \(O(m^{-2})\) normalized maximum pair codegree, and
  \(O(m^{-1})\) edge-local pair energy.

Nevertheless every possible next bite has the wrong stopped-profile drift
by a factor \(\Theta(\sqrt m)\).  Consequently none of those data implies
a uniform statewise version of (SD) or (SP).

There is one essential qualification.  The sets \(S_d\) were selected
separately.  We did **not** construct an entrance matching \(\mathcal M\)
for which

\[
 S_d=\bigcup_{f\in\mathcal M}f_d
\quad(0\le d\le J).
\tag{3.1}
\]

Indeed, realizing (3.1) while every \(|S_d|=G\) would already be a
simultaneous rainbow packet family.  Thus Theorem 2.2 is not a reachable-
residual counterexample and does not refute the ordinary construction.
Its exact implication is that **reachability is the only remaining source
of the necessary hole bias**.  Any proof which forgets the common owners in
(3.1), even if it retains every separate-rank load moment, cannot work.

One elementary reachable constraint, absent from the random construction,
is worth making explicit.  If \(s=|\mathcal M|=G/n\), then for every
coordinate \(x\in[n]\),

\[
 \boxed{
 \sum_{\substack{T\in V_d\\x\in T}}\mu_d(T)
   =s(r-d).}
\tag{3.2}
\]

Indeed, in one cyclic packet a fixed coordinate belongs to exactly
\(r-d\) of the \(n\) intervals of length \(r-d\).  Thus every reachable
load is element-regular at every depth.  In addition, its occurrences
admit an owner-labelled integral endpoint flow from depth \(d\) to depth
\(d+1\), because every interval has its two endpoint truncations.  The
profiles in Section 2 were not claimed to satisfy either condition.
Consequently a positive theorem may legitimately use element regularity,
the endpoint flow, or the still stronger common-owner representation
(3.1); none is encoded by separate-rank energy alone.

At time zero the distinction is visible in the opposite direction.  With
\(S_d=\varnothing\), every single packet has zero stopped-profile loss.
The obstruction is therefore not a time-zero catalogue defect.  It is a
failure of arbitrary cross-depth states, and the desired theorem must prove
that the genuine trajectory never resembles them.

## 4. Exact reachable common-interval sufficient condition

For two packets \(e,f\), write

\[
 C_d(e,f)=|e_d\cap f_d|.
\tag{4.1}
\]

For a reachable state (3.1) and a bite \(\mathcal B\), define

\[
 \begin{aligned}
 R_d(\mathcal B;\mathcal M)
 &=\sum_{e\in\mathcal B}\sum_{f\in\mathcal M}C_d(e,f)\\
 &\quad+
   \sum_{\{e,e'\}\in\binom{\mathcal B}{2}}C_d(e,e').
 \end{aligned}
\tag{4.2}
\]

### Theorem 4.1 (whole-bite reachable pair bound)

For every reachable state and every legal bite of \(s\) packets,

\[
 \boxed{
 L_{\mathcal M}(\mathcal B)
 \le
 \sum_{d=0}^J
   \bigl(R_d(\mathcal B;\mathcal M)-(ns-c_d)\bigr).}
\tag{4.3}
\]

#### Proof

In (1.6), every occurrence of a current covered target in a new packet
has at least one old owner.  Charging it to one such owner, and allowing
overcounting, bounds the covered-target term by the old--new part of
(4.2).  Also

\[
 (k-1)_+\le\binom k2,
\]

so the same-bite coalescence term is at most the new--new part of (4.2).
Substitute these two bounds in (1.6). \(\square\)

Consequently a concrete whole-bite law sufficient for (SP) is

\[
 \boxed{
 \mathbb E\sum_{j<\tau}\sum_{d=0}^J
 \left[
  R_d(\mathcal B_j;\mathcal M_j)-(nb_j-c_{d,j})
 \right]=o(W).}
\tag{RPK}
\]

Unlike complete-catalogue pair spread, (RPK) is evaluated along the actual
reachable trajectory and is centered by the exact scalar saturation
credit.  It includes whole-bite coalescence automatically.

The distinction from time-zero pair spread is quantitative.  Complete-
catalogue incidence counting gives, for a fixed old packet \(f\),

\[
 {1\over E}\sum_e C_d(e,f)
 ={n(D_d-1)\over E}
 =(1+o(1)){n^2\over N_d}.
\tag{4.3a}
\]

Thus a target-blind candidate against \(|\mathcal M|=G/n\) old packets
has expected old--new pair mass

\[
 (1+o(1)){Gn\over N_d}.
\tag{4.3b}
\]

At an unsaturated macroscopic depth this is \(\Theta(n)\), whereas the
scalar credit \(n-c_d\) is zero.  The exact compatible-pair census in
`MATH_AUDIT_ANNULAR_REPEAT_EXCESS_LOCAL_COMPATIBILITY_AND_POISSON_GATE_20260727.md`
shows that conditioning a pair to be entrance-compatible does not remove
this leading deeper common-interval incidence.  Therefore ordinary
pair-spread or regeneration toward the complete-catalogue mean proves the
wrong, Poisson-scale value of (RPK).  A positive theorem must be explicitly
hole-biased, or must produce a non-Poisson common-owner cancellation across
depths.

There is a particularly clean form on a binary-load annulus.  Suppose the
terminal mass \(G_\tau\) satisfies

\[
 G_\tau<2N_J.
\tag{4.4}
\]

Let

\[
 P_d(\mathcal M)=\sum_T\binom{\mu_d(T)}2
 =\sum_{\{e,f\}\subseteq\mathcal M}C_d(e,f).
\tag{4.5}
\]

Since the balanced mean load is then below two at every depth, its exact
pair-energy floor is

\[
 P_d^{\min}=(G_\tau-N_d)_+.
\tag{4.6}

The standard integer-floor identity therefore gives

\[
 \boxed{
 \mathfrak C_\tau
 \le\sum_{d=0}^J
 \left(P_d(\mathcal M_\tau)-(G_\tau-N_d)_+\right).}
\tag{4.7}

The right side is exactly the telescoped version of (RPK).  For a critical
mass \(G_\tau=(1-o(1))N_0\), condition (4.4) is equivalent to the narrow-
annulus restriction

\[
 b^2-a^2<\log2-o(1).
\tag{4.8}

Outside this binary range, raw pair energy overcharges the unavoidable
higher load floor.  One must either use the exact hole functional or center
the common-interval energy by its full integer floor, as in
`MATH_THEOREM_ANNULAR_PACKET_COMMON_INTERVAL_ENERGY_AND_PAIR_GADGET_GATE_20260727.md`.

## 5. Exact whole-bite LP dual and the two remaining gaps

There is an exact fractional formulation which cleanly separates hole
capacity from entrance-matching integrality.  Fix a reachable state, let
\(\mathcal L\) be its legal packet catalogue, and fix a bite size \(s\).
For every current hole \(h=(d,T)\), introduce a coverage variable \(y_h\),
and for every \(e\in\mathcal L\) a packet variable \(x_e\).  Consider

\[
 \begin{aligned}
 Z_s^*=\max\quad&\sum_{h}y_h\\
 \text{subject to}\quad
 &\sum_{e:v\in e_0}x_e\le1 &&(v\in V_0\setminus S_0),\\
 &y_h\le\sum_{e:h\in e}x_e &&(h\text{ a current hole}),\\
 &0\le y_h\le1,\qquad x_e\ge0,\\
 &\sum_e x_e=s.
 \end{aligned}
\tag{5.1}
\]

If \(x\) is integral, its support is a legal bite and the best choice of
\(y\) records its fresh union.  Hence the integral optimum
\(Z_s^{\rm int}\) is exactly

\[
 Z_s^{\rm int}
 =\max_{\mathcal B\in\mathfrak B_s(\mathcal M)}
      \sum_d Z_d(\mathcal B),
\tag{5.2}
\]

and the minimum deterministic bite loss is

\[
 \min_{\mathcal B}L_{\mathcal M}(\mathcal B)
 =\sum_dc_d-Z_s^{\rm int}.
\tag{5.3}
\]

### Theorem 5.1 (fractional Hall dual)

The fractional optimum in (5.1) equals

\[
 \boxed{
 \begin{aligned}
 Z_s^*=\min\quad
 &\sum_v a_v+\sum_h(1-p_h)+s z\\
 \text{subject to}\quad
 &z+\sum_{v\in e_0}a_v\ge\sum_{h\in e}p_h
       &&(e\in\mathcal L),\\
 &a_v\ge0,\qquad 0\le p_h\le1,
       \qquad z\in\mathbb R.
 \end{aligned}}
\tag{5.4}
\]

#### Proof

Give the entrance-capacity constraints dual variables \(a_v\ge0\), the
constraints \(y_h-\sum_{e\ni h}x_e\le0\) variables \(p_h\ge0\), the
constraints \(y_h\le1\) variables \(q_h\ge0\), and the bite-size equality
a free variable \(z\).  The dual conditions are

\[
 z+\sum_{v\in e_0}a_v\ge\sum_{h\in e}p_h,
 \qquad p_h+q_h\ge1,
\]

and its objective is \(\sum_va_v+\sum_hq_h+sz\).  At optimum
\(q_h=(1-p_h)_+\).  Values \(p_h>1\) may be reduced to one: this does not
increase the objective and only relaxes the packet inequalities.  This
gives (5.4), and finite-dimensional LP duality gives equality. \(\square\)

Thus a whole-bite proof has exactly two quantitative tasks:

\[
 \underbrace{\sum_dc_d-Z_s^*}_{\text{fractional labelled deficiency}}
 +
 \underbrace{Z_s^*-Z_s^{\rm int}}_{\text{integral rounding gap}}
 =o(\text{allowed bite error}).
\tag{5.5}
\]

Neither term is controlled by unlabelled entrance degrees alone.

The arbitrary floor state of Section 2 already fails at the first,
fractional, task.  Indeed, for any feasible \(x\) of total mass \(s\),

\[
 \begin{aligned}
 \sum_h y_h
 &\le\sum_{d=0}^J\sum_{T\in\mathcal H_d}
                  \sum_{e:T\in e_d}x_e\\
 &=ns(J+1)-\sum_e x_e\sum_{d=0}^J|e_d\cap S_d|\\
 &\le ns(J+1)-c_{a,b}s m^{3/2}.
 \end{aligned}
\tag{5.6a}
\]

As long as the bite stays unsaturated,
\(\sum_dc_d=ns(J+1)\), so its fractional labelled deficiency is already
\(\Omega(s m^{3/2})\).  By (5.4), an equally large dual certificate
exists.  It can be written explicitly: take \(p_h=1\) for every hole,
\(a_v=0\), and

\[
 z=\max_e|\{h:h\in e\}|.
\]

The packet inequalities in (5.4) then hold, while Theorem 2.2 gives
\(z\le n(J+1)-c_{a,b}m^{3/2}\).  Thus the arbitrary-state obstruction is
not an entrance-matching rounding artifact; it is a genuine labelled-
capacity obstruction.  Its only missing property remains reachability.

At time zero, however, the fractional deficiency vanishes exactly.  Let
\(D_0\) be the entrance degree, \(D_d\) the degree of a depth-\(d\)
target, and \(E\) the packet count.  The uniform choice

\[
 x_e={s\over E}
\tag{5.6}
\]

has entrance load

\[
 {sD_0\over E}={sn\over N_0}\le1
\]

whenever \(sn\le N_0\).  Its depth-\(d\) load is

\[
 {sD_d\over E}={sn\over N_d},
\]

because \(D_d/D_0=N_0/N_d\).  Taking
\(y_{d,T}=\min\{1,sn/N_d\}\) gives

\[
 \sum_{d,T}y_{d,T}=\sum_d\min\{N_d,sn\}=\sum_dc_d.
\tag{5.7}
\]

So the complete initial catalogue has an exact simultaneous fractional
solution.  The difficulty begins only after insisting on an integral
entrance matching and on hereditary continuation.  Formula (5.4) is the
precise labelled dual which a reachable-residual theorem must control.

## 6. Final status

The weakest conditional one-step law is deterministic minimum loss; a
random scheduler cannot do better at a fixed state.  A universal
statewise estimate is false even for complement-coherent, separately
floor-perfect profiles, and it fails by the full \(\sqrt m\) factor.

The theorem still needed for the ordinary route is therefore genuinely
hereditary:

> Along a legal entrance-packet trajectory, the common-owner
> representation (3.1) forces either the exact stopped loss (1.6), or the
> floor-correct reachable pair loss (RPK), to have cumulative mass \(o(W)\).

The existing time-zero degree/codegree and pair-profile estimates do not
prove this statement, because they are insensitive to the target-labelled
support geometry exhibited in Section 2.  Conversely, Section 2 is not a
reachable counterexample.  The live question is now sharply separated
from both: prove a reachable common-owner self-correction theorem, or
construct an actual critical entrance matching whose support profile
approximates the arbitrary floor state above.
