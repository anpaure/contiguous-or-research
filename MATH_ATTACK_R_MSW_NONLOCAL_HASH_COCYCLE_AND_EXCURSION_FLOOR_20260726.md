# Nonlocal Dyck-hash MSW twists: the exact ownership cocycle and a hereditary (1/9) excursion floor

> **Superseded draft.** This file suffered delimiter loss during an
> intermediate write and is retained only for provenance. The authoritative
> clean theorem report is
> MATH_THEOREM_R_HASH_TWISTED_MSW_LATIN_COCYCLE_AND_EXCURSION_FLOOR_20260726.md;
> the independently audited context/collar extension is
> MATH_LEMMA_R_MSW_HASH_EXCURSION_COCYCLE_OBSTRUCTION_20260726.md.

Date: 2026-07-26

Method: pure mathematics only.  No computation, finite search, solver, or
web input is used.

## 0. Outcome

There is a clean exact answer for the most direct recursive-hash version
of the proposed construction.

Let (D_r) be the Dyck (r)-subsets of ([2r]), let (F_r) be the
anchored MSW/Chung--Feller factor, and put

\[
 H_r=\langle s_i=(2i\ \ 2i+1):1\le i<r\rangle .
\tag{0.1}
\]

Allow the row rooted at (P\in D_r) to read an arbitrary, genuinely
nonlocal hash of the whole Dyck word and to choose

\[
 h_P\in H_r,
 \qquad
 G_h(P)=h_PF_r(h_PP).
\tag{0.2}
\]

This contains every static recursive scheme in which the complete row is
obtained by simultaneously relabelling aligned adjacent bridge pairs,
with each relabelling decision allowed to read an arbitrary hash of the
complete local root.  It does not contain a recursive splice which changes
the physical exterior or whose final row is not one coordinate-conjugate
MSW row.  The hash range has size (2^{r-1}); no finite-hash pigeonhole
argument is being used.

The results are as follows.

1.  Exact middle ownership is equivalent to a simultaneous lower/upper
    Latin-section condition.  In physical-owner form, for every lower or
    upper token (T),
    \[
      \sum_{a\in H_r}{\bf1}_{\{h_{\lambda_a(T)}=a\}}=1,
      \qquad
      \lambda_a(T)=a\rho(aT).
      \tag{0.3}
    \]
    Here \(\rho(T)\) is the canonical MSW owner root.  This condition is
    necessary and sufficient; checking only the Dyck rows, only one
    Chung--Feller layer, or only the hash is insufficient.

2.  Nonconstant nonlocal hashes satisfying (0.3) do exist for every
    (r\ge3).  For each (R\in D_{r-2}), the reciprocal pair
    \[
                 K_R=\{1100R,1010R\}
                 \tag{0.4}
    \]
    is a complete owner-overlay component between (F_r) and its
    (s_1)-conjugate.  Hence an arbitrary suffix hash
    \(\eta:D_{r-2}\to\{0,1\}\) may independently select the packets
    (K_R), producing a literal integral exact factor.  Thus exactness
    does not force the hash to be constant.  More strongly, for every
    fixed (\varepsilon>0), bounded-level component randomization gives
    one exact factor at rooted-row distance greater than
    ((1/8-\varepsilon)C_r) from every global (H_r)-conjugate, while
    reducing the canonical first-child target load to at most
    (C_{r-1}-C_{r-2}).

3.  Nevertheless every row of (0.2), whether or not the selector is
    exact, has an unavoidable fibre.  There is a set
    \(\mathcal E_r\subset D_r\) of size (R_{r-1}) such that every
    (P\in\mathcal E_r) has first inserted coordinate (2r) in
    (G_h(P)).  Its generating function and asymptotic size are
    \[
      \sum_{n\ge0}R_nz^n={1\over1-z^2C(z)^2}
        ={C(z)^2\over2C(z)-1},
      \qquad
      {R_{r-1}\over C_r}\longrightarrow {1\over9}.
      \tag{0.5}
    \]
    Therefore no nonlocal hash in the class (0.2) can make all first-edge
    fibres (o(C_r)).

4.  The same obstruction is hereditary in every fixed-exterior aligned
    packet.  A local depth-((r-1)) window has one target of multiplicity
    at least (R_{r-1}).  Before any cyclic row phases, (N) such packet
    copies at point-cap (p) have raw excess at least
    \[
             N(R_{r-1}-p)_+.
             \tag{0.6}
    \]
    For occurrence-disjoint packet copies, after arbitrary independent
    powers of one ambient (p)-cycle, the
    (R_{r-1}) occurrences occupy at most (p) physical images, so the
    phase-robust bound is
    \[
             N(R_{r-1}-p^2)_+.
             \tag{0.7}
    \]
    Thus, when (C_r/p^2\to\infty), a positive-density fixed-carrier
    deployment has linear collision excess even after arbitrary row
    phases.  Taking
    (r=\lceil2\log_4p+2\log_4\log p\rceil) gives
    (r=O(\log p)=o(\sqrt p)) and (C_r/p^2\to\infty), so this
    obstruction already lies inside every fixed Gaussian depth band.

The conclusion is a sharp class obstruction, not a no-go for arbitrary
MSW rewiring.  A construction can escape only by leaving the rowwise
(H_r)-conjugate class, or by moving the exterior/crossing collars so
that the local rows are not a fixed-carrier packet.  General
phase-permutation factors, suspended pentagons, and cross-parent compiler
resolutions are not ruled out.

## 1. The exact two-shore row bijection

Write

\[
 \mathcal L_r=\binom{[2r]}r,
 \qquad
 \mathcal U_r=\binom{[2r]}{r+1}.
\tag{1.1}
\]

For (P\in D_r), let the canonical row be

\[
 X_0(P),X_1(P),\ldots,X_r(P),
 \qquad
 X_0(P)=P,quad X_r(P)=[2r]\setminus P,
\tag{1.2}
\]

and put

\[
                         Y_t(P)=X_t(P)\cup X_{t+1}(P)
                         \quad(0\le t<r).
\tag{1.3}
\]

The two canonical incidence maps

\[
\begin{aligned}
 \xi_X:D_r\times\{0,\ldots,r\}&\longrightarrow\mathcal L_r,
 &\xi_X(P,t)&=X_t(P),\\
 \xi_Y:D_r\times\{0,\ldots,r-1\}&\longrightarrow\mathcal U_r,
 &\xi_Y(P,t)&=Y_t(P)
\end{aligned}
\tag{1.4}
\]

are bijections.  This is exactly the two-shore ownership theorem for the
canonical factor.

For an arbitrary selector (h:D_r\to H_r), define

\[
 X_t^h(P)=h_PX_t(h_PP),
 \qquad
 Y_t^h(P)=h_PY_t(h_PP).
\tag{1.5}
\]

Every individual row is a legal complementary Johnson geodesic.  Indeed,
coordinate relabelling preserves adjacency and (h_P^2=1), so

\[
 X_0^h(P)=P,
 \qquad
 X_r^h(P)=[2r]\setminus P.
\tag{1.6}
\]

Define maps on the two canonical owner domains by

\[
 C_\epsilon^h(P,t)
   =\xi_\epsilon^{-1}
      \bigl(h_P\xi_\epsilon(h_PP,t)\bigr),
 \qquad \epsilon\in\{X,Y\}.
\tag{1.7}
\]

### Theorem 1.1 (simultaneous Latin-section criterion)

The candidate (G_h) is an exact anchored odd-graph factor if and only if

\[
                         C_X^h\text{ and }C_Y^h
                         \text{ are both bijections.}
\tag{1.8}
\]

#### Proof

By (1.7), applying the bijection \(\xi_\epsilon\) to the image multiset
of (C_\epsilon^h) gives exactly the selected token multiset in (1.5).
Thus (C_X^h) is bijective exactly when every lower token occurs once,
and (C_Y^h) is bijective exactly when every upper token occurs once.
These are precisely the two ownership ledgers.  Individual row legality
and endpoint closure were already checked in (1.6), so no further
condition remains. \(\square\)

The (Y)-condition cannot in general be replaced by a phasewise row
permutation: coordinate action may move a canonical upper token between
different canonical columns.

## 2. Physical owner cocycle

Let

\[
 \rho:\mathcal L_r\mathbin\sqcup\mathcal U_r\longrightarrow D_r
\tag{2.1}
\]

send each physical token to its unique canonical owner root.  If one uses
the same global label (a\in H_r) on every row, then the owner of (T)
in that conjugate factor is

\[
                         \lambda_a(T)=a\rho(aT).
\tag{2.2}
\]

Indeed (aT) is canonically owned by \(\rho(aT)\), and conjugating that
row sends its root to (a\rho(aT)).

### Theorem 2.1 (exact owner-section equation)

For an arbitrary map (h:D_r\to H_r),

\[
 \boxed{
 G_h\text{ is exact}
 \iff
 \sum_{a\in H_r}{\bf1}_{\{h_{\lambda_a(T)}=a\}}=1
 \quad
 (T\in\mathcal L_r\mathbin\sqcup\mathcal U_r).}
\tag{2.3}
\]

#### Proof

Fix (a\in H_r).  The physical token (T) appears in the selected
label-(a) rows precisely when the row rooted at its global-(a) owner
\(\lambda_a(T)\) chose label (a).  Summing this indicator over all
labels gives the left side of (2.3), which is therefore exactly the
multiplicity of (T).  Requiring multiplicity one on both shores is
Theorem 1.1. \(\square\)

Equation (2.3) is the ownership cocycle obstruction to an arbitrary hash.
The hash graph must meet every owner block

\[
                         \{(\lambda_a(T),a):a\in H_r\}
\tag{2.4}
\]

in exactly one point.

There is a particularly transparent binary specialization.  Fix
(g,k\in H_r), let (A=\{P:h_P=k\}), and form the multigraph
\(\Gamma_{g,k}) on (D_r) with one edge

\[
                         \lambda_g(T)\ --\ \lambda_k(T)
\tag{2.5}
\]

for every lower and upper token (T).

### Corollary 2.2 (binary component rule)

If (h_P\in\{g,k\}) for every (P), then

\[
 \boxed{
 G_h\text{ is exact}
 \iff
 A\text{ is a union of connected components of }\Gamma_{g,k}.}
\tag{2.6}
\]

#### Proof

The multiplicity of (T) is

\[
 {f1}_{\{\lambda_g(T)\notin A\}}
 +{f1}_{\{\lambda_k(T)\in A\}}.
\]

It equals one exactly when the indicator of (A) agrees at the two ends
of (2.5).  This must hold for every edge. \(\square\)

Thus a nonlocal Boolean hash is legal precisely when it factors through
the full two-shore overlay-component quotient.  Rootwise independence is
false.

## 3. A literal nonlocal-hash family

Put (s_1=(2\ 3)).  For (R\in D_{r-2}), define

\[
                         P_R=1100R,
 \qquad                  Q_R=1010R.
\tag{3.1}
\]

Suppress the common shifted suffix state.  The first three states of the
two canonical rows are

\[
\begin{array}{c|ccc}
 P_R&12R&14R&34R\\
 Q_R&13R&23R&24R.
\end{array}
\tag{3.2}
\]

The corresponding (s_1)-conjugate rows are

\[
\begin{array}{c|ccc}
 P_R&12R&23R&34R\\
 Q_R&13R&14R&24R.
\end{array}
\tag{3.3}
\]

Both sides use the same six lower states and the same four upper colours

\[
                         123R,124R,134R,234R
\tag{3.4}
\]

once each, and the rows rejoin after the displayed slab.  Consequently

\[
                         K_R=\{P_R,Q_R\}
\tag{3.5}
\]

is a complete connected component of \(\Gamma_{1,s_1}\).  The sets
(K_R) are pairwise disjoint.

### Theorem 3.1 (arbitrary suffix-hash exact factor)

For every function

\[
                         \eta:D_{r-2}\to\{0,1\},
\tag{3.6}
\]

choose the (s_1)-conjugate row on

\[
                         A_\eta=\bigcup_{\eta(R)=1}K_R
\tag{3.7}
\]

and the canonical row elsewhere.  The resulting (G_\eta) is a literal
integral exact anchored factor.

#### Proof

Equation (3.2)--(3.4) shows directly that changing both rows in one
(K_R) preserves both ownership ledgers and both rooted endpoints.  The
old owner unions of distinct (K_R)'s are disjoint because the canonical
factor is a partition.  Since each replacement has the same owner union
as its old packet, different replacements remain disjoint.  Equivalently,
(3.7) is a union of components and Corollary 2.2 applies. \(\square\)

The selector in (3.6) may depend on every bit of (R), its complete
first-return tree, or any other nonlocal statistic.  The theorem is
all-(r) and has no bounded-hash hypothesis.

There is also a near-minimal one-sided load version.  Put

\[
                         w_r=\prod_{i=1}^{r-1}s_i.
\tag{3.8}
\]

Globally conjugate (G_\eta) by (w_r).  It then uses the row labels
(w_r) and (w_rs_1), remains exact, and changes exactly
(2|\eta^{-1}(1)|) rows of the all-block factor.  Let

\[
 L(G)=\max_{1\le j\le r,\ x\in[2r]}
 \#\{P:\operatorname{fr}(P)=j, b_1^G(P)=x\}.
\tag{3.9}
\]

The audited all-block quota theorem gives (L(F_r^{w_r})=R_{r-1}).
Changing one row can increase any fixed cell by at most one, hence

\[
 \boxed{
 R_{r-1}\le L(w_rG_\eta w_r)
       \le R_{r-1}+2|\eta^{-1}(1)|.}
\tag{3.10}
\]

The lower bound will be proved independently in Section 4.  Thus choosing
(1\le|\eta^{-1}(1)|=o(C_r)) gives a nonconstant exact hash factor with

\[
                         L=(1/9+o(1))C_r,
\tag{3.11}
\]

but not an (o(C_r)) fibre bound.

For completeness, these sparse examples can be chosen outside every
single covariant global conjugacy class.  Let (Z_r=(10)^r), and choose a
nonempty family in (3.7) whose globally conjugated root set does not
contain (Z_r); this is possible for (r\ge4), since the (K_R)'s are
disjoint and (C_{r-2}\ge2).  The resulting factor agrees with the
all-block factor on the row (Z_r) and differs from it on a selected
rectangle.  If it were the global (a)-conjugate for some (a\in H_r),
then the first target on (Z_r) would force (a=w_r): if
(j) is the least index for which (s_j\notin a), then (aZ_r) first
returns at (2j), so its first inserted target is (2j<2r), whereas the
all-block target is (2r).  Hence (a=w_r), contradicting the changed
rectangle.  Thus the factor is not any single covariant coordinate
conjugate.  This statement does not classify the contravariant
reverse--complement symmetry.

## 3A. A root-distant exact hash factor

The preceding sparse example proves nonconjugacy but changes only
sublinear mass.  A componentwise probabilistic choice gives a stronger
root-distance statement while preserving an exact one-sided child
improvement.

The complete components of the \(F_r\)--\(s_1F_r\) owner overlay are

\[
 \mathcal C_{j,R}=\mathcal A_jR,
 \qquad
 0\le j\le r-2,\quad R\in D_{r-j-2},
\tag{3A.1}
\]

where

\[
 |\mathcal A_j|=b_j=C_{j+1}+C_j.
\tag{3A.2}
\]

Thus there are \(C_{r-j-2}\) components of size \(b_j\).  The \(j=0\)
components are exactly the pairs \(K_R\) in (3.5).

### Theorem 3A.1 (uniform distance from every global \(H_r\)-conjugate)

For every \(\varepsilon>0\), there is an integer \(J=J(\varepsilon)\)
such that, for all sufficiently large \(r\), one can choose an exact
binary component selector with the following properties.

1. Every \(j=0\) component chooses the \(s_1\)-conjugate shore.
2. Only components with \(0\le j\le J\) need be noncanonical.
3. If \(G\) is the resulting rooted factor, then
   \[
    d_{\rm row}(G,F_r^a)>
       (1/8-\varepsilon)C_r
       \qquad(a\in H_r),
   \tag{3A.3}
   \]
   where \(F_r^a(P)=aF_r(aP)\).
4. The old first-child target \(2\) has load at most
   \[
                         C_{r-1}-C_{r-2}.
   \tag{3A.4}
   \]

The same distance conclusion holds simultaneously for any rooted
comparison catalogue of size \(\exp(o(C_r))\).

#### Proof

Force all \(j=0\) components to shore one.  For each component with
\(1\le j\le J\), choose shore zero or one independently with probability
\(1/2\); leave every \(j>J\) component on shore zero.  Every outcome is
exact by Corollary 2.2.

Fix a rooted comparison factor \(H\), and one randomized component
\(\mathcal C\).  At every root \(P\in\mathcal C\), the two candidate rows
\[
                         F_r(P),\qquad s_1F_r(s_1P)
\]
are distinct.  Otherwise every lower and upper token of that row would
have the same owner in the two factors, making \(P\) an isolated overlay
component, contrary to \(|\mathcal C|=b_j\ge3\).  Therefore the two
mismatch indicators against the single comparison row \(H(P)\) have sum
at least one.  If \(Z_{\mathcal C}\) is the mismatch contribution of
this component, then
\[
                         \mathbb E Z_{\mathcal C}
                         \ge {|\mathcal C|\over2}.
\tag{3A.5}
\]

Put
\[
 M_{J,r}=\sum_{j=1}^J
       (C_{j+1}+C_j)C_{r-j-2}.
\tag{3A.6}
\]

The randomized components are independent and have size at most
\(B_J=\max_{1\le j\le J}b_j\).  Hoeffding's inequality gives, for every
fixed \(\delta>0\),
\[
 \Pr\!\left[
   d_{\rm row}(G,H)<{M_{J,r}\over2}-\delta C_r
 \right]
 \le \exp(-c_{J,\delta}C_r).
\tag{3A.7}
\]

Indeed
\[
 \sum_{\mathcal C}|\mathcal C|^2
 \le B_JM_{J,r}=O_J(C_r).
\]

For fixed \(J\),
\[
 {M_{J,r}\over C_r}\longrightarrow
 \mu_J:=\sum_{j=1}^J{C_{j+1}+C_j\over4^{j+2}}.
\tag{3A.8}
\]

Using \(C(1/4)=2\),
\[
 \sum_{j\ge0}{C_{j+1}+C_j\over4^{j+2}}
 ={1\over16}
  \left({C(1/4)-1\over1/4}+C(1/4)\right)
 ={3\over8}.
\tag{3A.9}
\]

The \(j=0\) term is \(1/8\), so
\[
                         \mu_J\uparrow {1\over4}.
\tag{3A.10}
\]

Choose \(J\) with \(\mu_J>1/4-\varepsilon\), then choose the concentration
loss and the finite-\(r\) error small enough that the lower bound in
(3A.7) exceeds \((1/8-\varepsilon)C_r\).  There are
\(|H_r|=2^{r-1}=\exp(O(r))\) global covariant conjugates.  The union of
their failure events has probability
\[
                         \exp(O(r)-c_{J,\varepsilon}C_r)<1
\]
for all sufficiently large \(r\).  Hence one selector satisfies (3A.3)
for all of them.  The same proof handles any \(\exp(o(C_r))\) rooted
catalogue.

It remains to prove (3A.4).  The canonical roots with first-child target
two are exactly
\[
                         \{10v:v\in D_{r-1}\},
\tag{3A.11}
\]
so their old load is \(C_{r-1}\).  For any root \(P\), the first inserted
coordinate of its \(s_1\)-conjugate row is
\[
                 s_1\!\left(2\operatorname{fr}(s_1P)\right).
\tag{3A.12}
\]
If the inner first return is one, this is \(s_1(2)=3\); if it is at least
two, it is an even coordinate at least four and is fixed by \(s_1\).
Thus an \(s_1\)-shore row never contributes target two.  The forced
\(j=0\) components contain exactly the \(C_{r-2}\) roots
\[
                         1010R=10(10R),
                         \qquad R\in D_{r-2},
\tag{3A.13}
\]
from (3A.11).  They all leave the old target.  Every additional selected
component can only remove further occurrences and can never add one.
This proves (3A.4). \(\square\)

The qualifier “rooted” is essential in (3A.3).  An arbitrary coordinate
permutation which does not preserve the Dyck port family does not supply a
canonical row-by-row comparison on \(D_r\).  The full covariant
port-preserving coordinate group is exactly \(H_r\).

## 4. The pointwise excursion-blind set

Write a Dyck word as

\[
                         P=1b_1b_2\cdots b_{r-1}0,
                         \qquad |b_i|=2,
\tag{4.1}
\]

and encode

\[
 11\mapsto U,
 \qquad00\mapsto D,
 \qquad01\mapsto\alpha,
 \qquad10\mapsto\beta.
\tag{4.2}
\]

After forgetting the colour of the horizontal steps, this is a Motzkin
excursion.  Let \(\mathcal E_r\) be the roots having no ground-level
horizontal step of either colour.

Every element of (H_r) preserves the uncoloured Motzkin path: it only
exchanges \(\alpha\) and \(\beta\) in selected slots.  In particular, for
(P\in\mathcal E_r) and every (a\in H_r), the word (aP) has no
ground \(\alpha\)-step and therefore has first return semilength (r).
The canonical MSW first inserted coordinate is

\[
                         b_1^{F_r}(Q)=2\operatorname{fr}(Q).
\tag{4.3}
\]

Every (a\in H_r) fixes coordinate (2r).  Hence

\[
 b_1^{aF_r(aP)}(P)
 =a\bigl(2\operatorname{fr}(aP)\bigr)
 =a(2r)=2r
 \qquad(P\in\mathcal E_r).
\tag{4.4}
\]

This proof is pointwise and does not use the ownership equations.

### Theorem 4.1 (unbounded-hash excursion floor)

For every map (h:D_r\to H_r), exact or not,

\[
 \boxed{
 \#\{P\in D_r:\operatorname{fr}(P)=r,
                  b_1^{G_h}(P)=2r\}
 \ge |\mathcal E_r|=R_{r-1}.}
\tag{4.5}
\]

Moreover

\[
                         {R_{r-1}\over C_r}\longrightarrow{1\over9}.
\tag{4.6}
\]

#### Proof

Equation (4.4) proves the inclusion and hence (4.5).  It remains to count
\(\mathcal E_r\).

An arbitrary two-coloured Motzkin excursion has generating function
(C(z)^2).  An excursion with no ground horizontal step is a sequence of
elevated blocks (UMD), each with generating function
(z^2C(z)^2).  Therefore

\[
 R(z)=\sum_{n\ge0}R_nz^n
     ={1\over1-z^2C(z)^2}
     ={C(z)^2\over2C(z)-1}.
\tag{4.7}
\]

At the Catalan singularity,

\[
 C(z)=2-2\sqrt{1-4z}+O(1-4z).
\]

For \(\Phi(u)=u^2/(2u-1)\), one has \(\Phi'(2)=4/9\), so

\[
                         R_n\sim{4\over9}C_n.
\tag{4.8}
\]

Finally (C_{r-1}/C_r\to1/4), proving (4.6). \(\square\)

This is stronger than a finite-hash residual-fibre lemma.  Even a hash
with one independent bit at every paired coordinate cannot move these
roots out of the cell (4.5).

## 5. Hereditary fixed-carrier form

Let a local (D_r)-port factor be installed on a coordinate block
(J\) of size (2r), and suppose a distinguished ambient interval has one
common fixed exterior intersection (K).  For a rooted local path, write

\[
 X_t=(P\setminus A_t)\cup B_t,
\tag{5.1}
\]

where (A_t) and (B_t) are the first (t) deleted and inserted
coordinates.  The exact interval formula is

\[
                 \bigcap_{t=i}^{j}X_t
                 =(P\setminus A_j)\cup B_i.
\tag{5.2}
\]

For the child window (X_1,\ldots,X_r), this becomes

\[
                         \bigcap_{t=1}^rX_t=\{b_1\}.
\tag{5.3}
\]

Adjoining the common exterior gives the ambient target

\[
                         K\cup\{b_1\}.
\tag{5.4}
\]

### Theorem 5.1 (hereditary packet fibre)

Install any rowwise (H_r)-hash factor (0.2) in such a fixed-exterior
packet.  Its distinguished depth-((r-1)) target

\[
                         K\cup\{2r\}
\tag{5.5}
\]

has multiplicity at least (R_{r-1}).

If (N) packet copies are installed with pairwise disjoint distinguished
rooted occurrences, arbitrary carriers, and ambient phase capacity (p),
then their contributions alone satisfy

\[
 \boxed{
 \sum_S(\mu_{r-1}(S)-p)_+
       \ge N(R_{r-1}-p)_+.}
\tag{5.6}
\]

#### Proof

For every (P\in\mathcal E_r), Theorem 4.1 gives (b_1=2r), and
(5.3)--(5.4) give the common target (5.5).  This proves the first claim.

Group the (N) packet copies according to their physical target in
(5.5).  If (n_S) copies have target (S), then their contribution is
at least (n_SR_{r-1}).  When (R_{r-1}>p),

\[
 \sum_S(n_SR_{r-1}-p)_+
 =NR_{r-1}-p\,|\{S:n_S>0\}|
 \ge N(R_{r-1}-p).
\]

When (R_{r-1}\le p), the asserted right side is zero.  Adding all other
occurrences can only increase the cap excess. \(\square\)

The point-cap bound (5.6) is not invariant under subsequent cyclic row
phases: the rows of one packet may spread their common target around its
ambient coordinate orbit.  The exact phase-robust correction costs one
further factor (p), not more.

### Theorem 5.2 (arbitrary cyclic phases)

Let (\sigma) be any coordinate (p)-cycle, and after constructing the
occurrence-disjoint packets allow every row an arbitrary exponent in
(\mathbb Z_p).  Then

\[
 \boxed{
 \sum_S(\mu_{r-1}^{\rm phased}(S)-p)_+
       \ge N(R_{r-1}-p^2)_+.}
\tag{5.7}
\]

#### Proof

Before phasing, the (R_{r-1}) certified occurrences in one packet have
one target (S_0).  After arbitrary row exponents, every one lies in

\[
                         \{\sigma^aS_0:a\in\mathbb Z_p\},
\]

a set of at most (p) physical targets.  If their multiplicities are
(d_1,\ldots,d_\ell), with (\ell\le p), then

\[
 \sum_{j=1}^\ell(d_j-p)_+
 \ge\left(\sum_jd_j-\ell p\right)_+
 \ge(R_{r-1}-p^2)_+.
\tag{5.8}
\]

For nonnegative (u,v), the point-cap functional is superadditive:

\[
                         (u+v-p)_+\ge(u-p)_++(v-p)_+.
\tag{5.9}
\]

Therefore overlap between the target orbits of different packets cannot
decrease the sum of their individual lower bounds.  Summing over the
(N) packets proves (5.7). \(\square\)

If the distinguished starts in these packets have total mass

\[
                         M=NC_r,
\tag{5.10}
\]

then, whenever (C_r/p^2\to\infty), (4.6) and Theorem 5.2 give

\[
 \sum_S(\mu_{r-1}^{\rm phased}(S)-p)_+
 \ge(1/9-o(1))M.
\tag{5.11}
\]

Thus a deployment covering a positive fraction of the relevant starts by
fixed-carrier recursive hash packets has linear raw collision excess.
For the odd middle factor (p=2m+1), the unavoidable duplicate baseline
at depth (q=o(\sqrt m)) is

\[
                         W-N_q=O(q^2W/m)=o(W).
\tag{5.12}
\]

Consequently a linear lower bound in (5.11) remains linear after the exact
baseline correction; it is not merely harmless unavoidable duplicate
mass.

To place this inside the protected shallow range, take

\[
 r=\left\lceil2\log_4p+2\log_4\log p\right\rceil.
\tag{5.13}
\]

The Catalan asymptotic gives

\[
 C_r=\Theta\!\left({4^r\over r^{3/2}}\right)
     \gg p^2,
\tag{5.14}
\]

while (r=O(\log p)=o(\sqrt m)), since (p=2m+1).  Hence the depth
(q=r-1) lies below (A\sqrt m) for every fixed (A>0) and all
sufficiently large (m).

## 6. What the obstruction does and does not close

The class closed here is the **context-functorial adjacent-bridge hash
class**:

* the local packet has fixed complementary Dyck ports;
* the exterior carrier is common to the packet rows;
* a recursive decision may read the whole local Dyck word;
* every decision acts by a product of the adjacent bridge swaps in
  (H_r); and
* exactness is enforced by the two-shore owner cocycle (2.3).

For this class, increasing the hash range, correlating all hash bits, and
choosing a nonconstant exact component section do not remove hereditary
excursion blindness.  Equation (5.11) rules out a positive-density local
deployment as a coefficient-one seed.

The theorem does **not** classify all exact MSW/Chung--Feller factors.
In particular it leaves open:

1. phasewise row permutations not induced by (H_r);
2. longer zero-ledger alternating cycles in the lower/upper inclusion
   matchings;
3. suspended packets which exchange lower and upper columns;
4. row-dependent motion of the exterior carrier; and
5. cross-parent compiler resolutions whose collars are decoded only
   after several packets are combined.

Those escapes are precisely outside the fixed-carrier cocycle proved
here.  A proposed recursive twist using any of them must re-prove the
literal lower and upper ownership bijections; it cannot inherit
exactness merely from a Dyck-word hash.

This is consistent with the authoritative CPCR reduction.  CPCR already
assumes packetwise literal injectivity and asks for cross-parent,
all-depth floor covariance.  The present theorem says that replacing its
cross-parent resolution by independent fixed-carrier MSW bridge hashes
cannot work: at the logarithmic scale (5.13), any positive-density bank
of those local packets contributes a linear cap defect before the CPCR
floor can be balanced.  It neither disproves CPCR nor returns the problem
to a common-order or within-packet gate; it identifies exterior motion or
non-(H_r) row interleaving as necessary for this proposed seed route.
