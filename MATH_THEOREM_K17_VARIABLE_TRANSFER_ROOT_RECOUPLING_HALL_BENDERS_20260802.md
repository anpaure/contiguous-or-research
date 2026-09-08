# K17 variable-transfer root recoupling: exact Hall aperture and Benders theorem

Date: 2026-08-02

Status: proof-safe supplier-projection theorem. It replaces the obsolete
fixed-438 premise by an arbitrary regenerated-parent transfer subset. It is
conditional on literal common-parent, protected-row, occurrence, and root-flow
contracts. It is not a chronology, residence, compiler, or word theorem.

## 1. Correct finite face

The authoritative strict-def84 recompressed parent is the zero-transfer table
with SHA-256

    bf5b946f9e1cd5165ba323c894208e9370e7a2b671578ef2a6231535c2ba3241

and chain counts

\[
(\mathrm{LLR},\mathrm{LMR},\mathrm{LR},\mathrm{MR})
=(0,16915,4862,2533).
\tag{1.1}
\]

The old 438-mode table

    9dafc568f9b93151822053618fe4574b2b50452e944b7fb98a093c47dda9e2f3

is one calibration overlay, not a required cardinality or a prospective
parent. Its \(51/17\) Hall shore and deficiency 34 belong only to that
materialized child.

For the recompressed parent, the fresh structural transfer catalogue has
115,086 edges, with all 4,862 unprotected LR hosts and 11,450 unprotected LMR
donors considered; its endpoint matching rank is 3,420. The relevant bindings
are

    structural catalogue  e51b1688e977c11fb7dee80338f4bcc7e86b83c232c416f48bd774ac6f4d9746
    structural audit      f86ff3e8045f2eac24bb8e856df1360f3f3eb33091382b6bc93827cf819f0f38
    state-support audit   0d8a3510b14f7a055f020774ca469012ded0372dc8951d3ad9231e0a27e315dd
    exact-tuple catalogue 2c399790b1af274f652d42308ecc54d16e0a3f7ef96c42d7b4dc3c21af23329a

The exact one-transfer marginal screens are:

\[
\begin{array}{c|c|c}
\text{screen}&\text{eligible edges}&\text{maximum endpoint-row-disjoint rank}\\
\hline
\text{positive in both transported phases}&5821&250\\
\text{one declared }(q,\alpha,\beta)\text{ common to both phases}&5228&208\\
\text{one literal }(q,\alpha,\beta,\mathrm{pred},\mathrm{succ})\text{ tuple}&3171&161.
\end{array}
\tag{1.2}
\]

The ranks in (1.2) are maxima of **one-transfer-priced subgraphs** and are
necessary screens, not simultaneous occurrence packings. In particular, the
208 matching permits different predecessor and successor physical rows in the
two phases. Even the 161 exact-tuple matching does not enforce witness-row
disjointness across different selected modes or survival of one mode's witness
after another mode is selected. Conversely, another selected transfer can
create a long witness for a mode that was individually zero. Therefore 208
and 161 are ceilings only on their stated individually screened subcatalogues,
not on a full compound-state selector over all 115,086 structural modes.

If \(S\) is a jointly legal transfer matching and \(a=|S|\), then

\[
(\mathrm{LLR},\mathrm{LMR},\mathrm{LR},\mathrm{MR})
=(a,16915-a,4862-a,2533+a).
\tag{1.3}
\]

Thus \(0\le a\le208\) on the individually declared-common-state **screened
subface**, and \(0\le a\le161\) on the individually literal-exact-tuple
subface. There is no lower bound forcing \(a>0\). A full compound-state model
must retain all 115,086 structural modes with exact state DNFs and cannot use
208 as a global cardinality cap.

The particular \(a=0\) recompressed table has supplier rank
\(16846/16898\), deficiency 52, 43 zero heads, and a \(60/8\) Hall shore.
This proves only that this one fixed root completion is not supplier-perfect;
it does not rule out a different protected root recoupling at \(a=0\).

## 2. Complete master states

Fix \(K\le208\) and first restrict to the 5,228 individually
common-declared-state modes. Let \(\Theta_K^{\mathrm{scr}}\) be the family of
complete literal states \(\theta\) consisting of:

1. a row-disjoint subset \(S_\theta\) of the regenerated catalogue with
   \(|S_\theta|\le K\);
2. one allowed declared state and one compatible occurrence in each phase for
   every selected mode, with the exact shared state/flag one-hots, all
   phase-indexed physical-row capacities, and residual direct long-long
   completion;
3. all 7,213 private rows and the protected socket dependency closure fixed,
   or an explicit final occurrence-matching repair;
4. an exact root-recoupled completion of the resulting chain table, including
   the low-middle-root and direct-low flow equations; and
5. the fully materialized table and complete supplier graph

   \[
   G_\theta=(H_\theta,U;E_\theta).
   \tag{2.1}
   \]

The root completion is inside \(\theta\), before supplier separation. A
supplier failure of one arbitrary residual root completion is not a no-good
for its transfer subset.

For the unrestricted compound-state model, replace
\(\Theta_K^{\mathrm{scr}}\) by \(\Theta_K^{\mathrm{full}}\), built from all
115,086 structural modes and their complete compound DNFs; \(K\) is then a
chosen budget rather than the number 208. Every theorem below applies to
either declared family. We write \(\Theta_K\) when the choice is explicit.

If root recourse is allowed to create additional LLR chains not named by the
transfer catalogue, equality \(a=|S_\theta|\) in (1.3) is no longer exact.
Those LLR variables and their phase occurrence columns must then be exposed
explicitly. The theorem below remains valid, but the catalogue ceiling 208 no
longer bounds those uncatalogued chains.

## 3. Variable-cardinality min-max theorem

Let \(\widehat H\) be the finite universe of mode-labelled hard-head
occurrences. For \(h\in\widehat H\), let \(b_h(\theta)\) be its final activity
bit. For supplier identity \(u\), let \(e_{hu}(\theta)\) be the exact final
incidence bit, including both endpoint modes and the selected state. For
\(Q\subseteq\widehat H\), define

\[
n_{Q,u}(\theta)
=
\bigvee_{h\in Q}
\bigl(b_h(\theta)\wedge e_{hu}(\theta)\bigr)
\tag{3.1}
\]

and the Hall excess

\[
\Delta(\theta)
=
\max_{Q\subseteq\widehat H}
\left[
\sum_{h\in Q}b_h(\theta)
-
\sum_{u\in U}n_{Q,u}(\theta)
\right].
\tag{3.2}
\]

The empty set shows \(\Delta(\theta)\ge0\).

### Theorem 3.1 (exact zero/low-transfer criterion)

Define

\[
D_K:=\min_{\theta\in\Theta_K}\Delta(\theta).
\tag{3.3}
\]

Set \(D_K=+\infty\) when \(\Theta_K=\varnothing\).

Then a protected common-state table with at most \(K\) transfers and full
supplier rank exists if and only if

\[
\boxed{D_K=0.}
\tag{3.4}
\]

Equivalently,

\[
\boxed{
\exists\theta\in\Theta_K\ \forall Q\subseteq\widehat H:
\quad
\sum_{h\in Q}b_h(\theta)
\le
\sum_{u\in U}n_{Q,u}(\theta).}
\tag{3.5}
\]

#### Proof

For fixed \(\theta\), (3.5) is precisely Hall's condition for the active left
vertices of \(G_\theta\); inactive mode-labelled occurrences contribute
nothing. Hence it is equivalent to a matching saturating every active hard
head. Taking the existential minimum over the complete protected states gives
(3.3)--(3.4). \(\square\)

The quantifier order is load-bearing. In general

\[
\min_{\theta}\max_Q \Delta_Q(\theta)
\ne
\max_Q\min_{\theta}\Delta_Q(\theta).
\tag{3.6}
\]

A root recoupling may remove one incumbent shore while creating a different
one, so there is no single old shore that can be repaired before choosing the
completion.

On the individually screened fixed-parent subface, define

\[
\tau_{\mathrm{scr}}^*
=
\min\left\{
|S_\theta|:
\theta\in\Theta_{208}^{\mathrm{scr}},\
\Delta(\theta)=0
\right\},
\tag{3.7}
\]

with \(\tau_{\mathrm{scr}}^*=+\infty\) if the set is empty. The analogous
quantity on a complete compound catalogue replaces the state family and its
declared budget. Supplier perfection with at most \(K\) transfers is
equivalent to the corresponding minimum being at most \(K\).

### Corollary 3.2 (root recoupling alone)

Zero transfers suffice exactly when

\[
\boxed{
\exists\theta\in\Theta_0:
\quad \nu(G_\theta)=|H_\theta|.}
\tag{3.8}
\]

On the compressed-normal \(a=0\) face, the static chain table may be described
by the common basis of \(M_L\) and \(M_7^*\oplus U_{16915,M}\), together with
its representing matchings. Condition (3.8) is an additional supplier
matching condition on that literal representation. It is not a weight on the
common-basis elements and does not reduce to weighted two-matroid
intersection.

There is therefore no valid lower bound \(\tau_{\mathrm{scr}}^*\ge34\) from the old
\(51-17\) shore. Root recoupling can change many hard-head modes and expose
many supplier identities with \(S_\theta=\varnothing\). Conversely, 34
individually favorable transfers can still share suppliers or alternating
bottlenecks and fail Hall.

## 3A. Exact fixed-\(bf5b\) optimum and the root-retirement lift

Let \(\mathcal Z_{bf5b}^{\mathrm{scr}}\) be the supplier relaxation containing
every row-disjoint subset of the 5,228 individually common-declared-state
modes on the fixed \(bf5b\) root completion, with arbitrary cardinality. It
does not assert simultaneous occurrence-witness packing. This relaxation now
has an exact optimum:

\[
\boxed{
\min_{z\in\mathcal Z_{bf5b}^{\mathrm{scr}}}
\Delta(z)=40.}
\tag{3A.1}
\]

A ten-mode projection table attains supplier rank \(16858/16898\), deficiency
40. Its
selected fresh edge indices are

    29162 47595 58729 77643 81966
    82676 112912 113721 114811 114957

Target deficiency 39 is DRAT-UNSAT. The sharp certificate is one
mode-labelled Hall template \(P\) with 50 potential head requirements. Three
supplier identities are fixed compatible neighbors:

    cut summary       60291d7a1aa6f1cfb633731dcfbd3b54c2af81c10b85ffb77aafb7f41c960f02
    cut heads         7d7d7eee16f44c63d57034e26d27b79cde10934011527d3f2cca129f1d7d0d28
    cut fixed         743220831d09b3f0eaa19ce693eac2da72ec55669cfd8d5479c993527007a1ec
    cut terms         dc19946727ba993be1a09fb5749d6da0d0378ceb29f5acf2ed2978f494dabb4d
    target39 CNF      b7f8d17bae5130948143da3702159485a46a1dfe9cf42bd05a2c98f38dd4cadb
    target39 DRAT     9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa
    DRAT verification 9f026f2a57755ad0993d16c5991eadf5100b61465f12396ea155738b959d3266
    def40 audit       a6dbb10f4db0afd4d5562234457afd513c08e2caf787995ce3a1bd1227e718d4
    def40 selection   e47ceaafaf441afc1f7475b24741b8bf37af0ea7f7479c57421c4ab2dfb72938
    def40 transcript  5217b9cf2d3ff228ff312d84d260ec4b1922f6a706e5d4fc814df1a1b62926a6

    12973 13581 20737

and there are exactly seven dynamic Boolean credits:

- inactivity of the transfer-mode head at row 14797; and
- six distinct supplier-neighbor ORs at rows
  \(2793,5895,6540,6560,12586,14851\).

For a fixed-root mode choice \(z\), define

\[
\Gamma_P(z)
=
\sum_{p\in P}(1-a_p(z))
+
\sum_{u\in U} b^P_u(z),
\qquad
b^P_u(z)
=
\bigvee_{p\in P}
\bigl(a_p(z)\wedge e_{pu}(z)\bigr).
\tag{3A.2}
\]

The three fixed neighbors plus the seven binary dynamic terms give
\(\Gamma_P(z)\le10\) for every row-disjoint screened selection. Hall with
target deficiency \(d\) requires

\[
\Gamma_P(z)\ge 50-d.
\tag{3A.3}
\]

Thus \(d=39\) would require 11 credits and is impossible. The ten-mode witness
attains equality \(\Gamma_P=10\), proving (3A.1).

Because the encoded family is a relaxation of any simultaneous protected
common-state packing using those screened modes, the lower bound 40 also
applies to every such packing. The ten-mode table is an upper witness for the
supplier relaxation only until its full occurrence/state packing is replayed.

The number ten is a witness support size, not a credit count and not a
minimum-cardinality theorem. Those ten modes jointly realize the maximum
allowed head-inactivity/supplier-OR pattern. Adding or replacing modes cannot
manufacture an eighth dynamic term for \(P\); the DRAT certificate quantifies
over every cardinality and every row-disjoint subset of all 5,228 screened
modes. This is why ten modes suffice at the fixed roots but no larger
selection closes any of the remaining 40 units.

Now let a root-variable state be

\[
\tau=(C,\mu_7,\mu_L,z,\omega),
\tag{3A.4}
\]

where \(C=C_M\sqcup C_R\) is a common basis of
\(M_L\) and \(M_7^*\oplus U_{16915,M}\),
\(B=R\setminus C_R\) is the rank-seven receiver basis,
\(\mu_7,\mu_L\) are its literal representing matchings,
and \(z,\omega\) are the selected modes and complete common-state witnesses.
Define \(a_p(\tau),e_{pu}(\tau),b^P_u(\tau)\), and \(\Gamma_P(\tau)\) from the
final materialized table.

### Theorem 3A.1 (exact lifted root/head release cut)

Every supplier-perfect joint root/mode state satisfies

\[
\boxed{\Gamma_P(\tau)\ge50.}
\tag{3A.5}
\]

Relative to the fixed-root optimum, which has one inactive \(P\)-head and
nine distinct compatible suppliers, this is

\[
\boxed{
\left[\sum_{p\in P}(1-a_p(\tau))-1\right]
+
\left[\sum_{u\in U}b^P_u(\tau)-9\right]
\ge40.}
\tag{3A.6}
\]

Loss of an old supplier credit is automatically negative in (3A.6). Hence at
least 40 **net Hall credits** must come from root/head requirement retirement
and distinct supplier-bank expansion beyond the best fixed-root selection.
Pure head retirement requires 40 additional \(P\)-head retirements. This does
not imply 40 matroid basis exchanges: one exchange can alter a representing
matching and may change more than one literal head or supplier incidence.

#### Proof

Equation (3A.5) is Hall's inequality
\(|N(P_{\mathrm{active}})|\ge|P_{\mathrm{active}}|\), rewritten by moving
the inactive head count to the neighbor side. The fixed-root witness has
\(\Gamma_P=1+9=10\); subtracting 10 from (3A.5) gives (3A.6).
\(\square\)

Let \(B_0\) be the fixed-\(bf5b\) receiver basis and use the ordinary basis
exchange distance

\[
d_B(B,B_0)=|B_0\setminus B|
=\tfrac12|B\triangle B_0|.
\tag{3A.7}
\]

The exact cut-escape envelope is

\[
\kappa_P(t)
=
\max\left\{
\Gamma_P(\tau)-10:
\tau\text{ is common-basis/representation/common-state feasible},\
d_B(B(\tau),B_0)\le t
\right\}.
\tag{3A.8}
\]

Escaping the certified shore requires \(\kappa_P(t)\ge40\). If an independent
literal support audit proves that one fundamental basis exchange contributes
at most \(\lambda\) net credits to (3A.6), then necessarily

\[
\boxed{t\ge\left\lceil\frac{40}{\lambda}\right\rceil.}
\tag{3A.9}
\]

For example, a proved one-credit locality would give 40 exchanges; a proved
one-head-plus-one-new-supplier locality would give 20. Matroid basis exchange
alone supplies no such \(\lambda\): the representing alternating paths can
change many literal rows. Without that support audit, 40 net credits is the
sharp numeric theorem, while no positive numeric basis-distance bound is
justified. In particular, the certificate rules out the fixed literal
\(bf5b\) completion, not every alternative representing matching of the same
basis \(B_0\); \(\kappa_P(0)\) itself still requires audit.

Finally, for a root-distance budget \(t\) and a declared mode family
\(\mathcal F\), define

\[
\mathcal D(t)
=
\min_{\substack{
C\in\mathcal B(M_L)\cap
\mathcal B(M_7^*\oplus U_{16915,M})\\
d_B(R\setminus C_R,B_0)\le t\\
\mu_7,\mu_L\in\operatorname{Rep}(C),\
(z,\omega)\in\mathcal F(C,\mu_7,\mu_L)
}}
\quad
\max_{Q\subseteq\widehat H}
\left[
\sum_{h\in Q}a_h
-
\sum_{u\in U}
\bigvee_{h\in Q}(a_h\wedge e_{hu})
\right].
\tag{3A.10}
\]

Then root/mode supplier perfection within distance \(t\) is equivalent to

\[
\boxed{\mathcal D(t)=0.}
\tag{3A.11}
\]

This is common-basis branching plus exact Hall Benders separation. Supplier
compatibility depends on the representing matchings and OR-incidences, so it
is not a third matroid and not a weight on common-basis elements.

The fixed 5,228-edge catalogue and its DRAT core remain parent-local. If a root
change creates or destroys prospective long states outside its pinned
presentation, \(\mathcal F\) in (3A.10) must be regenerated for that parent or
replaced by a complete state-expanded catalogue.

## 4. Exact localized aperture after a completion is fixed

The global formulation above is required while root recoupling is free. Once
a complete child is materialized, a smaller exact slave is available.

Let \(K_\theta\subseteq E_\theta\) be a matching whose literal edges are
required to stay fixed and which covers every hard head outside a local
aperture. Put

\[
C_\theta
=H_\theta\setminus V_H(K_\theta),
\qquad
W_\theta
=U\setminus V_U(K_\theta),
\tag{4.1}
\]

and \(R_\theta=G_\theta[C_\theta,W_\theta]\).

### Theorem 4.1 (frozen-carrier contraction)

\[
\boxed{
\max\{|N|:K_\theta\subseteq N\subseteq E_\theta,\ N\text{ a matching}\}
=
|K_\theta|+\nu(R_\theta).}
\tag{4.2}
\]

In particular, \(K_\theta\) extends to supplier perfection if and only if

\[
\boxed{
\nu(R_\theta)=|C_\theta|
\iff
|N_{R_\theta}(Q)|\ge|Q|
\quad\forall Q\subseteq C_\theta.}
\tag{4.3}
\]

#### Proof

Every extension edge must join a head and supplier uncovered by
\(K_\theta\), hence belongs to \(R_\theta\). Every matching in \(R_\theta\)
is disjoint from \(K_\theta\) and can be adjoined. Hall's theorem gives
(4.3). \(\square\)

This is the smallest exact bipartite/transversal slave. Its left size is a
child-specific aperture size. It is 51 only for the old 438 child when its
16,847-edge outside carrier survives literally. If deleting old modes or
changing root types destroys any carrier edge, either enlarge the aperture or
regenerate the carrier; silently reusing the old \(51/17\) cut is invalid.

If outside heads need only remain saturated and their partners may change,
replace the free supplier bank in (4.3) by the following strict gammoid
\(\Gamma_\theta\). Its ground set is \(U\), its terminals are
\(W_\theta=U\setminus V_U(K_\theta)\), and its alternating network contains
only the outside heads \(H_\theta\setminus C_\theta\): orient
\(K_\theta\)-edges supplier-to-head and all allowed nonmatching outside edges
head-to-supplier, with unit vertex capacities. Rado's exact condition is

\[
\boxed{
r_{\Gamma_\theta}
\left(
\bigcup_{h\in Q}N_{G_\theta}(h)
\right)
\ge|Q|
\quad\forall Q\subseteq C_\theta.}
\tag{4.4}
\]

The gammoid rank is one node-capacitated max-flow. A reachability-only
head-to-port graph is not exact when two escape paths share a unit-capacity
supplier or outside head.

## 5. Charging arbitrary loss of an old carrier

Let \(G^0\) be any reference supplier graph with \(N_0\) heads, deficiency
\(d_0\), and maximum matching \(M^0\). For a final child \(\theta\), retain
only reference edges that remain literal final incidences between active
vertices:

\[
M^\circ_\theta:=M^0\cap E_\theta,
\qquad
\ell_\theta:=|M^0|-|M^\circ_\theta|.
\tag{5.1}
\]

Here reference and child graphs use exhaustive canonical mode-labelled head
tokens and supplier identities, so the intersection in (5.1) is literal.

Starting from \(M^\circ_\theta\), let

\[
\alpha_\theta:=\nu(G_\theta)-|M^\circ_\theta|
\tag{5.2}
\]

be the exact number of cardinality augmentations obtainable in the final
graph; alternating toggles are allowed.

### Lemma 5.1 (carrier-loss identity)

\[
\boxed{
\delta(G_\theta)
=
d_0+(|H_\theta|-N_0)+\ell_\theta-\alpha_\theta.}
\tag{5.3}
\]

When the hard-head census remains 16,898,

\[
\boxed{
G_\theta\text{ is supplier-perfect}
\iff
\alpha_\theta=d_0+\ell_\theta.}
\tag{5.4}
\]

#### Proof

Since \(|M^0|=N_0-d_0\),

\[
\nu(G_\theta)
=|M^\circ_\theta|+\alpha_\theta
=N_0-d_0-\ell_\theta+\alpha_\theta.
\]

Subtracting this from \(|H_\theta|\) gives (5.3). \(\square\)

Relative to the old 438 overlay, \(d_0=34\); relative to the actual
zero-transfer recompressed child, \(d_0=52\). Every lost carrier edge is
charged once through \(\ell_\theta\), and root recoupling plus selected
transfers jointly supply \(\alpha_\theta\). Neither quantity is additive per
transfer.

## 6. What remains of the old \(51/17\) shore

For the one old 438 child, let \(X,Y\) denote its shore of 51 old
**mode-labelled occurrences** and 17 supplier identities,
\(|X|=51\), \(|Y|=17\). In a new materialized state define

\[
X_\theta=X\cap H_\theta,\qquad
d_X=51-|X_\theta|,
\tag{6.1}
\]

\[
\ell_X=|Y\setminus N_\theta(X_\theta)|,
\qquad
g_X=|N_\theta(X_\theta)\setminus Y|.
\tag{6.2}
\]

The Hall inequality for this one persistent labeled set is exactly

\[
\boxed{d_X+g_X-\ell_X\ge34.}
\tag{6.3}
\]

Indeed,
\[
|N_\theta(X_\theta)|=17-\ell_X+g_X
\]
and
\[
|X_\theta|=51-d_X.
\]

Formula (6.3) cleanly distinguishes deletion of old \(X\)-head occurrences,
addition of distinct external supplier identities, and loss of old-bank
suppliers. It is only one necessary Hall row. Deactivating an old head may
activate a replacement head elsewhere, so \(d_X\) need not reduce global
demand.

On the stricter frozen-carrier face, suppose the residual aperture has
\(51-d+r\) heads after \(d\) old-shore demands disappear and \(r\)
replacement demands enter, and the surviving internal bank has matching rank
\(b\le17\). Any full residual matching then needs at least

\[
\boxed{51-d+r-b}
\tag{6.4}
\]

distinct external supplier identities. For fixed hard-head count,
\(r=d\) only when the same literal outside carrier remains fixed and continues
to cover every active head outside the aperture. Under that carrier contract,
deletion alone gives no count gain. Global head-count invariance by itself
does not imply \(r=d\). Full Hall or Rado cuts, not only (6.4), remain
necessary and sufficient.

For the literal old carrier with \(d=r=0\), split its free supplier bank as
\(Y\sqcup P\). On the 51 aperture heads let \(\mathcal T_Y\) and
\(\mathcal T_P\) be the transversal matroids of head sets matchable into
\(Y\) and \(P\), respectively. A perfect residual matching using all 17 old
suppliers and exactly 34 external suppliers exists if and only if

\[
\boxed{
r(\mathcal T_Y)=17
\quad\text{and}\quad
\mathcal T_Y^*
\text{ and }
\operatorname{Tr}_{34}(\mathcal T_P)
\text{ have a common basis}.}
\tag{6.5}
\]

Equivalently, a 51-unit residual min-cost matching with cost zero on
\(Y\)-edges and one on \(P\)-edges has optimum 34, with infeasible flow
assigned value \(+\infty\). Formula (6.5) is exact only
on that fixed child and carrier; it must be regenerated after changing the
root completion or transfer subset. Indeed, the 34 heads assigned externally
must be the complement of a 17-head \(\mathcal T_Y\)-basis and simultaneously
a 34-head \(\mathcal T_P\)-independent set; these are exactly the common bases
in (6.5).

## 7. Proof-safe selector and cuts

For a complete integer candidate \(\theta\):

1. replay its phase-indexed occurrence choices and protected dependency
   closure;
2. solve the exact fixed-mode root-recoupling flow, or include its integral
   flow variables in the master;
3. materialize the one literal final table and complete supplier graph;
4. compute a maximum supplier matching; and
5. on failure, return an active Hall shore \(Q\).

For that \(Q\), add exact neighbor-OR variables

\[
z_{Q,u}
\iff
\bigvee_{h\in Q}
\bigl(b_h\wedge e_{hu}\bigr)
\tag{7.1}
\]

and the lazy cut

\[
\boxed{
\sum_{u\in U}z_{Q,u}
\ge
\sum_{h\in Q}b_h.}
\tag{7.2}
\]

This cut permits root recoupling, old-head retirement, replacement-head
activation, and supplier-bank expansion while counting each supplier identity
once. Its incidence literals must be final-table DNFs, not old edge IDs or
per-transfer gain scores.

For (7.2) to be valid across root completions, \(\widehat H\) and \(U\) must
be exhaustive canonical universes for every allowed completion, and
\(b_h,e_{hu},z_{Q,u}\) must be exact functions of exposed root/table-state
variables. A shore expressed only in the physical row labels of one hidden
completion is not a global master cut.

If root recoupling is hidden in an oracle, failure of one chosen completion is
not a valid no-good for the primary transfer/ticket assignment. The oracle
must either produce a cut valid for **every** compatible residual completion
or expose the root-flow variables and cut the actual completion. Likewise,
two recoupled parents require separate regenerated catalogues unless one
state-expanded master explicitly includes all parent-dependent incidence and
occurrence columns.

For fixed \(\theta\), the supplier slave is a TU bipartite flow. The joint
mode, occurrence, root, and supplier selector is not thereby TU or matroidal.
The known nonmonotone supplier-rank counterexample forbids treating transfer
sets as a matroid-rank ascent.

## 8. Exact conclusion and remaining work

The proof-safe conclusion is:

\[
\boxed{
\text{zero or low transfer count succeeds exactly when some complete,
protected root completion satisfies every final Hall cut.}}
\tag{8.1}
\]

For zero transfers this is (3.8). For \(K>0\) it is (3.4), with no equality
fixing \(|S_\theta|\). On the fixed-\(bf5b\), individually screened 5,228-mode
supplier relaxation, (3A.1) strengthens this to a complete no-go: the exact
optimum deficiency is 40, attained by a ten-mode projection table. Escaping
that face requires the
40-credit lifted root/head cut (3A.6), followed by every other Hall cut. The
old deficiency 34 is not a transfer lower bound, and the screened rank 208 is
neither a global compound-state ceiling nor a supplier-feasibility theorem.

Still required are:

- full simultaneous two-phase occurrence packing for the chosen subset;
- a root completion and supplier-perfect table satisfying the cuts above;
- regeneration of catalogues whenever root recoupling changes prospective
  long states outside the pinned-parent face; and
- the open outer-state, residual long-long chronology, residence, upper,
  compiler, and word gates.
