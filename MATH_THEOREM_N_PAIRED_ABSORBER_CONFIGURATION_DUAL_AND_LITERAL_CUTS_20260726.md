# Paired-cycle absorber configurations: exact dual, routing criterion, and literal cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Throughout, the middle ground set is \([2m]\),

\[
                       W=\binom{2m}{m},
\]

and \(H\ge2,\ R\ge4H-3\) whenever an \(R\)-axis local absorber is used.

## 0. Outcome

This note continues the diverse-order physical \(2\)-opt absorber from
MATH_THEOREM_N_TWO_COLOR_PRODUCT_SCD_PHYSICAL_ENDPOINT_FUSION_20260726.md.

One raw absorber replaces, at each sign and depth \(q\),

\[
                         2q\ \hbox{old columns}
        \quad\hbox{by}\quad 2q\ \hbox{new columns},              \tag{0.1}
\]

and its signed image-indicator displacement has norm \(4q\). Across both
signs and every \(q\le H\), it has

\[
\begin{aligned}
\#\{\hbox{new tokens}\}
 &=\#\{\hbox{old tokens}\}=2H(H+1),\\
\|\Delta\|_1&=4H(H+1).                                         \tag{0.2}
\end{aligned}
\]

The global problem is not ordinary endpoint matching. It is a
complement-coupled, collar-capacitated, graphic-forest configuration
problem on the literal target columns. This note proves the following.

1. There is an exact integral formulation incorporating complement
   pairs, \(H\)-separated cut ports, the component-forest inequalities,
   axis-Euler balance, a prescribed fusion count, and the all-depth
   missing-shadow hinge.

2. In the one-hot equal-mass special case, if \(D=N-A\) is the selected
   literal target derivative and \(h\) is the old hole indicator, then
   the increase in missing shadows is exactly

   \[
                    \boxed{\Delta_{\rm miss}
                    =\sum_j[D_j-h_j]_+.}                        \tag{0.3}
   \]

   Equivalently,

   \[
   \boxed{
   \Delta_{\rm miss}
    =\max_{Q\subseteq\mathscr T_H}
       \left[
        \sum_{p\ {\rm selected}}
          \bigl(|N_p\cap Q|-|A_p\cap Q|\bigr)
        -|Q\cap\mathscr H|
       \right].}                                                \tag{0.4}
   \]

   For an arbitrary physical old load, after the cut slots and hence
   \(A\) are fixed, the final hole count instead has an exact
   maximum-coverage dual over every subset of the zero-residual target
   family. Thus arbitrary literal target families, not point weights,
   are the exact dual objects.

3. In that one-hot system, the fractional maximum-fusion problem with
   loss allowance \(L\) has an exact LP dual, including the target term

   \[
                         \lambda(N_p)-\lambda(A_p).              \tag{0.5}
   \]

   Point-margin Euler balance annihilates only constant and
   coordinate-additive choices of \(\lambda\).

4. If a complement-closed absorber family is exactly targetwise
   balanced, equal-target token matching decomposes it into
   complement-closed, exactly column-balanced routing components. Every
   physically legal union of those components has zero additional
   missing-shadow loss.

5. A literal touched-face cylinder obstructs every bounded or
   subexponential physically labelled collar-template menu. If a full
   \(Q_{R+1}\)-slab factor uses at most \(L\) such complete templates and
   \(2^q\ge8bLR\), its capacity-\(b\) deficiency at one sign and depth is
   at least

   \[
                              {q2^{R-1}\over R}.                  \tag{0.6}
   \]

   For slabs covering \(G\) owners, if

   \[
                    2^{\lceil H/2\rceil}\ge8bLR,                 \tag{0.7}
   \]

   the aggregate two-sign deficiency is at least

   \[
                              {GH^2\over8R}.                     \tag{0.8}
   \]

   There are \(G/(4R)\) paired-cycle fusions, so this is at least
   \(H^2/2\) per fusion.

6. The cylinder cut is sharp in scope. At the level of arbitrary safe
   local contexts, one can realize every touched set

   \[
                 \{e\}\cup K,\qquad K\in
                    \binom{D\setminus\{i\}}{q-1}.                \tag{0.9}
   \]

   The exact necessary template entropy for zero deficiency is

   \[
                              L_q\ge {2^{q-2}\over bR}.           \tag{0.10}
   \]

7. In an ideal independently composable full-affine menu, the local face
   codegrees permit a greedy simultaneous packing. The theorem requires
   every option to lie in the actual all-depth allowed pool of old holes
   and vacated columns. No current factor theorem supplies that menu.

8. A projection cut survives arbitrary context entropy: if every
   transition of the factor and of every selected absorber deletes and
   inserts inside one carrier \(E\subset[2m]\) of size
   \(m/2+o(\sqrt m)\), then at \(q=A\sqrt m+O(1)\) every complete
   configuration has \(\Omega_A(W)\) literal lower holes, and the
   complement-paired upper cut is identical.

Consequently no unrestricted positive selection theorem is proved. The
surviving projection-free route needs exponentially many
context-dependent collar supports and a common-factor allowed-pool
routing theorem. Point Euler balance supplies neither.

No coefficient-one conclusion is claimed.

## 1. Literal absorber columns and complementation

Let

\[
\mathscr T_H
 =\bigsqcup_{q=1}^{H}
  \left(
   \{(-,q,T):T\in\tbinom{[2m]}{m-q}\}
   \mathbin{\dot\cup}
   \{(+,q,U):U\in\tbinom{[2m]}{m+q}\}
  \right)                                                    \tag{1.1}
\]

be the typed target-token universe, with involution

\[
 \kappa(-,q,T)=(+,q,[2m]\setminus T).                           \tag{1.2}
\]

For one raw certified absorber \(\omega\), let
\(A_{\omega,\epsilon,q}\) and \(N_{\omega,\epsilon,q}\) be its old
vacated and new crossing columns. The paired-cycle theorem gives

\[
 |A_{\omega,\epsilon,q}|=|N_{\omega,\epsilon,q}|=2q,\qquad
 A_{\omega,\epsilon,q}\cap N_{\omega,\epsilon,q}=\varnothing.  \tag{1.3}
\]

Put

\[
 D_{j\omega}=N_{j\omega}-A_{j\omega},                          \tag{1.4}
\]

where \(A_{j\omega},N_{j\omega}\) are token multiplicities. For a raw
absorber they are indicators by (1.3); for a compound option,
\(A_p,N_p\) are multisets and all cardinalities below count
multiplicity.

Coordinate complementation sends an absorber to the corresponding one
in the complementary frozen context and satisfies

\[
\begin{aligned}
A_{\bar\omega,+,q,[2m]\setminus T}
 &=A_{\omega,-,q,T},\\
N_{\bar\omega,+,q,[2m]\setminus T}
 &=N_{\omega,-,q,T}.                                           \tag{1.5}
\end{aligned}
\]

When the two owner contexts are disjoint, fuse
\(\omega,\bar\omega\) into one complement superoption
\(p=\{\omega,\bar\omega\}\). It represents two physical component
fusions, so \(w_p=2\). Larger complement-closed compound options are
also allowed; \(w_p\) always means their proved net component reduction.

### Proposition 1.1 (the active-cube antipodal four-cut trap)

Inside one bare active \(Q_{R+1}\)-slab, closing one paired-cycle
absorber under the active-cube antipode by also switching the antipodal
\(i\)-cuts on the same two old \(C_{2R}\)'s is component-neutral.

#### Proof

In a \(C_{2R}\) with direction necklace \(\pi\pi\), the active-cube
antipode is the shift by \(R\). Thus the complement of one \(i\)-edge is
the other \(i\)-edge of the same cycle. Cutting both \(i\)-edges
separates that cycle into two antipodal paths, each with \(R-1\) internal
edges. Doing this in both facets and joining equal orientations by the
four \(e\)-edges pairs the two first half-paths into one cycle of length
\(2R\) and the two second half-paths into another cycle of length
\(2R\). No isometry claim is needed. There are two components before
and two after. \(\square\)

Thus a self-antipodal four-cut option has \(w_p=0\). Full coordinate
complementation normally also complements the frozen exterior context;
it need not be this operation. Genuine complement-paired fusion may use
disjoint complementary frozen contexts, or a separately proved larger
multi-cycle gadget.

## 2. The physical configuration system

Let \(\mathscr C_0\) be the old cycle set. A superoption \(p\) in the
present catalogue contains:

1. a complement-closed collection of physical paired-cycle \(2\)-opts;
2. its component edges \(E_p\) on \(\mathscr C_0\);
3. all old and new typed columns \(A_p,N_p\);
4. its point charge

   \[
      d_p=\sum_{\omega\in p}(\chi_{e_\omega}-\chi_{i_\omega}); \tag{2.1}
   \]

5. a cut-disjoint internal forest \(E_p\), with
   \(w_p=|E_p|\), its net component reduction.

Every local word has already passed the four-fringe \(H\)-safety test.
For one old cycle and one cyclic interval \(I\) of \(H\) transition
edges, let \(P_{Ip}\) be the number of cuts used by \(p\) in \(I\).
Reject \(p\) if \(P_{Ip}>1\). For an integral selection
\(y_p\in\{0,1\}\), impose

\[
                         \sum_pP_{Ip}y_p\le1
                         \qquad(I).                              \tag{2.2}
\]

This is the collar-separated class. Selected cuts on one old cycle have
cyclic distance at least \(H\), so every final \(q\)-window,
\(q\le H\), meets at most one new seam collar and inherits its local
certificate.

For \(\varnothing\ne U\subseteq\mathscr C_0\), put

\[
                         F_{Up}=|E_p\cap E(U)|.                  \tag{2.3}
\]

The component multigraph is a forest exactly when

\[
                  \sum_pF_{Up}y_p\le |U|-1
                  \qquad(\varnothing\ne U\subseteq\mathscr C_0).
                                                                    \tag{2.4}
\]

Under (2.2)--(2.4), all cuts are distinct, the \(2\)-opts may be applied
in leaf order, and the component count falls by exactly

\[
                              \sum_pw_py_p.                     \tag{2.5}
\]

For completeness, contract the new seam edges in the final forest
splice. A final arc between two distinct new seams contains an old-cycle
arc between two selected cut edges. Condition (2.2) makes that old arc
contain at least \(H-1\) intervening old edges, so a window containing
both seam edges has at least \(H+1\) edges. If no further selected cut
intervenes, the two seams of one raw \(2\)-opt are separated by the
residual \(2R-1\)-edge arc of one old cycle; if one does intervene, the
preceding two-cut argument applies. Hence no window of at most \(H\)
edges meets two new seams.

Exact point-margin preservation is

\[
                              \sum_pd_py_p=0.                    \tag{2.6}
\]

Overlapping seam collars which might repair one another are outside this
configuration class.

## 3. Exact missing-shadow identity and literal Hall cuts

Assume first that the old load being audited is one-hot. It may be the
actual physical occurrence load, or a chosen one-hot coverage
certificate; in the latter case the conclusions below are exact for the
certificate and become physical hole statements only when the
certificate accounts for the relevant background. Write

\[
 b_j\in\{0,1\},\qquad h_j=1-b_j,\qquad
 \mathscr H=\{j:h_j=1\}.                                      \tag{3.1}
\]

Impose the critical-old-column admissibility condition

\[
                         a_j(y):=\sum_pA_{jp}y_p\le b_j.        \tag{3.2}
\]

If \(b\) is the actual one-hot occurrence load and \(A\) records removed
occurrences, this is automatic. For a chosen representative certificate
it is an additional global representative constraint; collar separation
alone does not exclude two different old windows with the same literal
target.

Put

\[
 n_j(y)=\sum_pN_{jp}y_p,\qquad
 D_jy=n_j(y)-a_j(y),\qquad
 \ell_j(y)=b_j+D_jy.                                           \tag{3.3}
\]

### Theorem 3.1 (exact hinge and set-family dual)

\[
 \boxed{
 \mathfrak H(\ell(y))-\mathfrak H(b)
 =\sum_{j\in\mathscr T_H}[D_jy-h_j]_+.}                        \tag{3.4}
\]

Equivalently,

\[
 \boxed{
 \mathfrak H(\ell(y))-\mathfrak H(b)
 =
 \max_{Q\subseteq\mathscr T_H}
 \left[
   \sum_py_p\bigl(|N_p\cap Q|-|A_p\cap Q|\bigr)
   -|Q\cap\mathscr H|
 \right].}                                                     \tag{3.5}
\]

#### Proof

For an integral nonnegative load \(L\), put

\[
 H(L)=\sum_j(1-L_j)_+,\qquad O(L)=\sum_j(L_j-1)_+.
\]

The identity

\[
                         H(L)-O(L)=|\mathscr T_H|-\sum_jL_j
\]

and equality of old and new occurrence masses give

\[
 H(\ell)-H(b)=O(\ell)-O(b)=O(\ell),
\]

because \(b\) is one-hot. Since
\(\ell_j-1=D_jy-h_j\), this proves (3.4). Finally,

\[
                         \sum_j[r_j]_+
                         =\max_{Q\subseteq\mathscr T_H}
                           \sum_{j\in Q}r_j
\]

with \(r=Dy-h\) proves (3.5). \(\square\)

Zero additional loss is therefore equivalent to

\[
                              Dy\le h.                           \tag{3.6}
\]

On an old covered target this forbids net overload; on an old hole it
permits one net new column. For an arbitrary old load \(L^0\), without
one-hotness, the direct coordinate formula is instead

\[
 \sum_j\left[
   (1-L_j^0-D_jy)_+-(1-L_j^0)_+
 \right].                                                       \tag{3.7}
\]

There is also an exact literal set-family form which does not require
one-hotness.

### Theorem 3.2 (arbitrary-load physical coverage dual)

Fix the physical cut slots, so their aggregate removed occurrence
multiset \(A\) is fixed, and assume

\[
                         0\le A_j\le L_j^0\qquad(j).
\]

For a one-option-per-fixed-slot integral choice \(y\), put

\[
 \mathscr Z(A)=\{j:L_j^0-A_j=0\},\qquad
 N_j(y)=\sum_pN_{jp}y_p .
\]

Then the actual final physical hole count is

\[
\boxed{
 \mathfrak H(L^0-A+N(y))
 =\max_{Q\subseteq\mathscr Z(A)}
   \left[
      |Q|-\sum_py_p|N_p\cap Q|
   \right].}                                                   \tag{3.8}
\]

Consequently it is at most \(L\) if and only if every literal target
family \(Q\subseteq\mathscr Z(A)\) satisfies

\[
                  \sum_py_p|N_p\cap Q|\ge |Q|-L.               \tag{3.9}
\]

#### Proof

A target is missing after the switches exactly when it belongs to
\(\mathscr Z(A)\) and receives no new occurrence. Let \(U\) be this
uncovered family. For any \(Q\subseteq\mathscr Z(A)\), the occurrence
sum on the right of (3.8) is at least the number of covered targets in
\(Q\). Hence the bracket is at most \(|Q\cap U|\le|U|\). Taking
\(Q=U\) gives equality. This proves (3.8), and (3.9) is equivalent.
\(\square\)

The change from the old hole count is (3.8) minus
\(\mathfrak H(L^0)\). Unlike the one-hot equal-mass identity, it can be
negative. Theorem 3.2 is the authoritative physical formulation once
the old factor has multiplicities. If cut slots themselves are optional,
one must replace the frozen \(A\) by \(A(y)\) and apply the theorem
separately on each resulting zero-residual family.

If the old atlas and selected options are complement invariant, every
coefficient in (3.4) occurs twice on a \(\kappa\)-orbit. The maximizing
set in (3.5) may be taken \(\kappa\)-invariant, and the problem may be
divided by two on

\[
                         \widehat{\mathscr T}_H
                         =\mathscr T_H/\langle\kappa\rangle.    \tag{3.10}
\]

Likewise, if \(L^0,A,N(y)\) are complement invariant in Theorem 3.2,
then \(\mathscr Z(A)\) and its uncovered subfamily are
\(\kappa\)-invariant, so the maximizing family in (3.8) may also be
taken \(\kappa\)-invariant.

For a disjoint two-absorber complement superoption, its quotient
new-token mass at depth \(q\) is \(4q\), its old-token mass is \(4q\),
and its raw quotient token motion is \(8q\). The positive and negative
supports of the aggregated derivative can be smaller if constituent
tokens cancel on a quotient target.

### Why point Euler balance is insufficient

For a coordinate-additive price

\[
                         \lambda(T)=c+\sum_{v\in T}\theta_v,   \tag{3.11}
\]

the constant cancels because \(|N|=|A|\). For one raw \(i\to e\)
absorber,

\[
\begin{aligned}
\lambda(D_{-,q,\omega})
 &=q\langle\theta,\chi_i-\chi_e\rangle,\\
\lambda(D_{+,q,\omega})
 &=q\langle\theta,\chi_e-\chi_i\rangle.                       \tag{3.12}
\end{aligned}
\]

Equation (2.6) annihilates every additive price. The exact dual (3.5)
ranges over arbitrary indicators \({\bf1}_Q\), as does the
arbitrary-load physical coverage system (3.9).

## 4. The exact fractional fusion LP and Farkas dual

In the one-hot system of Theorem 3.1, allow added missing-shadow loss at
most \(L\), relax \(y_p\) to be nonnegative, and introduce
\(z_j\ge0\):

\[
\begin{aligned}
\Phi_{\rm LP}(L)=\max\quad&
 \sum_pw_py_p\\
\text{subject to}\quad&
 \sum_pP_{Ip}y_p\le1 &&(I),\\
&
 \sum_pF_{Up}y_p\le|U|-1
   &&(\varnothing\ne U\subseteq\mathscr C_0),\\
&
 Ay\le b,\\
&
 Dy-z\le h,\qquad \sum_jz_j\le L,\\
&
 \sum_pd_py_p=0,\qquad y,z\ge0.
\end{aligned}                                                   \tag{4.1}
\]

The row \(Ay\le b\) is the critical-old-column packing constraint
(3.2). It cannot in general be inferred from physical collar
separation, because distinct old windows can have the same literal
target.

### Theorem 4.1 (exact fractional dual)

\[
\begin{aligned}
\Phi_{\rm LP}(L)=\min\quad&
 \sum_I\alpha_I+
 \sum_{\varnothing\ne U\subseteq\mathscr C_0}
        (|U|-1)\beta_U+
 \sum_jb_j\gamma_j+
 \sum_jh_j\lambda_j+L\tau                                  \tag{4.2}\\
\text{subject to}\quad&
 \sum_IP_{Ip}\alpha_I+
 \sum_UF_{Up}\beta_U+
 \sum_jA_{jp}\gamma_j+
 \sum_jD_{jp}\lambda_j+
 \langle\pi,d_p\rangle
 \ge w_p
 &&(p),                                                       \tag{4.3}\\
&
 \alpha_I,\beta_U,\gamma_j,\tau\ge0,\qquad
 0\le\lambda_j\le\tau,\qquad
 \pi\ \hbox{free}.
\end{aligned}
\]

In particular,

\[
             \sum_jD_{jp}\lambda_j
             =\lambda(N_p)-\lambda(A_p).                       \tag{4.4}
\]

#### Proof

Dualize the collar, forest, old-column, target-hinge, total-loss, and
Euler rows. The old-column multiplier is \(\gamma\), and the free
multiplier of (2.6) is \(\pi\). The \(y_p\)-column gives (4.3). The
\(z_j\)-column has coefficient \(-1\) in the target row and \(+1\) in
the total-loss row, forcing \(0\le\lambda_j\le\tau\). This proves
(4.2). \(\square\)

A dual solution of value less than \(K\) proves that no integral
selection can make \(K\) fusions with loss at most \(L\). The converse
gives only a fractional solution. Indeed, the three-port incidence minor

\[
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix}
\]

has determinant \(2\): its half-vector has value \(3/2\), while every
integral port packing has value at most \(1\).

## 5. The exact all-depth packing hypergraph

Freeze a physical collar-separated forest with slot set \(\mathcal S\).
A slot fixes its physical cut edges and hence fixes, independently of
the remaining context/order choice, the old affected sets \(A_{s,c}\).
Only options preserving that whole old \(H\)-collar are admitted.
Discard any option whose new typed columns have an internal repetition.

For an arbitrary actual old load \(L^0\), let
\(A=\sum_sA_s\) and
\(\mathscr Z(A)=\{j:L_j^0-A_j=0\}\). Define the physical configuration
coverage hypergraph with vertices
\(\mathcal S\mathbin{\dot\cup}\mathscr Z(A)\) and option edges

\[
       E(s,\omega)=\{s\}\mathbin{\dot\cup}
             (N_s(\omega)\cap\mathscr Z(A)).
\]

A one-edge-per-slot transversal leaves precisely the uncovered target
vertices as physical holes. Thus Theorem 3.2 says that it has at most
\(L\) final physical holes if and only if

\[
 \boxed{
 \sum_{s\in\mathcal S}|N_s(\omega_s)\cap Q|
       \ge |Q|-L
 \quad\hbox{for every }Q\subseteq\mathscr Z(A).}               \tag{5.0}
\]

This is the exact arbitrary-load configuration-covering dual. It
already couples all signs and depths because \(Q\) is typed and one
physical \(\omega_s\) fixes every \(N_{s,c}\).

For the rest of this section specialize to the one-hot equal-mass
system of Theorem 3.1. Then \(\mathscr Z(A)\) is precisely the union of
old holes and vacated columns; subtracting the old hole count and using
\(|N|=|A|\) converts the covering deficit into the packing defect below.
At colour \(c=(\epsilon,q)\), define its allowed target pool by

\[
 \mathcal D_c
   =\mathscr H_c\cup\bigcup_{s\in\mathcal S}A_{s,c}.             \tag{5.1}
\]

These are exactly the old holes and the columns vacated by the chosen
cuts.  Let \(\Omega_s^{\mathcal D}\) be the options satisfying

\[
                         N_{s,c}(\omega)\subseteq\mathcal D_c
                         \qquad\hbox{for every }c.               \tag{5.2}
\]

Define a hypergraph with:

* one slot vertex for every \(s\in\mathcal S\);
* one capacity-one vertex \((c,T)\) for every
  \(T\in\mathcal D_c\); and
* for every \(\omega\in\Omega_s^{\mathcal D}\), the hyperedge

  \[
       \{s\}\mathbin{\dot\cup}
       \bigdotcup_c\{(c,T):T\in N_{s,c}(\omega)\}.               \tag{5.3}
  \]

For one choice \(\boldsymbol\omega=(\omega_s:s\in\mathcal S)\), write

\[
 r_{c,T}(\boldsymbol\omega)
   =|\{s:T\in N_{s,c}(\omega_s)\}|.
\]

Because the fixed old collars are disjoint in the old one-hot atlas,
their available capacity is
\(h_{c,T}+\sum_sA_{s,c,T}={\bf1}_{\{T\in\mathcal D_c\}}\).
Consequently Theorem 3.1 gives the exact integral defect formula

\[
\boxed{
 \Delta_{\rm miss}(\boldsymbol\omega)
  =\sum_{c,T}
    \left[
      r_{c,T}(\boldsymbol\omega)
      -{\bf1}_{\{T\in\mathcal D_c\}}
    \right]_+.}                                              \tag{5.3a}
\]

Equivalently, it is the maximum, over literal typed families \(Q\), of

\[
 \max_{Q\subseteq\mathscr T_H}
 \left[
  \sum_{s\in\mathcal S}|N_s(\omega_s)\cap Q|
       -|Q\cap\bigsqcup_c\mathcal D_c|
 \right].                                                     \tag{5.3b}
\]

Thus an \(o(W)\)-loss multiway selection is exactly a one-edge-per-slot
hypergraph selection with total capacity violation \(o(W)\). This is
strictly stronger information than point-margin balance.

### Theorem 5.1 (zero-loss matching equivalence)

The fixed forest admits a simultaneous all-depth zero-loss option
selection if and only if the hypergraph (5.3) has a matching saturating
every slot vertex.

#### Proof

If a matching saturates the slots, every new column lies in the allowed
pool and no allowed target is used twice.  Thus no new column overloads a
retained old target and no two new columns compete for one vacated
column or old hole.  Equation (3.6) gives zero loss.

Conversely, zero loss makes every summand in (3.4) zero.  Hence every new
column lies in (5.1) and has final multiplicity at most one.  The full
new images therefore form disjoint hyperedges (5.3). \(\square\)

The fractional relaxation of this hypergraph is feasible if and only if,
for every nonnegative target weight \(y\),

\[
 \boxed{
 \sum_{s\in\mathcal S}
   \min_{\omega\in\Omega_s^{\mathcal D}}
      \sum_c\sum_{T\in N_{s,c}(\omega)}y_{c,T}
 \le
 \sum_c\sum_{T\in\mathcal D_c}y_{c,T}.}                        \tag{5.4}
\]

This is the exact weighted fractional Hall inequality.  The minimum is
joint over both signs and every depth: one physical option determines
all of its columns.  Integral feasibility still requires a hypergraph
matching theorem.

#### Proof of the fractional criterion

Let \(v_{s,\omega}\) be the target-incidence vector of an option and put

\[
 \mathcal C=\sum_{s\in\mathcal S}
          \operatorname{conv}\{v_{s,\omega}:
                 \omega\in\Omega_s^{\mathcal D}\}.
\]

A fractional choice exists exactly when the compact convex set
\(\mathcal C\) meets the coordinate down-set
\(\mathcal B=\{x:x\le{\bf1}\}\). If they are disjoint, strong
separation supplies a normal \(y\ge0\): nonnegativity is forced because
\(\mathcal B\) is unbounded in every negative coordinate. With the
orientation chosen toward \(\mathcal C\), separation is

\[
 \min_{x\in\mathcal C}\langle y,x\rangle
   >\sup_{u\in\mathcal B}\langle y,u\rangle
   =\sum_{c,T}y_{c,T}.
\]

The left side is the sum of the slotwise minima in (5.4). Thus
separation is exactly a violation of (5.4), proving both directions.
\(\square\)

### Theorem 5.2 (exact target-routing component criterion)

Let \(\Omega_0\) be a finite complement-closed family of mutually
available absorber options satisfying the full targetwise token
identities

\[
 \sum_{\omega\in\Omega_0}N_{j\omega}
 =
 \sum_{\omega\in\Omega_0}A_{j\omega}
 \qquad(j\in\mathscr T_H).                                      \tag{5.5}
\]

For every \(j\), match its new tokens bijectively to its old tokens,
retaining multiplicity.
Form a graph on \(\Omega_0\) whose edges are these token matches, and
also join every \(\omega\) to \(\bar\omega\).  Every connected component
\(\Gamma\) satisfies

\[
 N_{\Gamma,j}=A_{\Gamma,j}\quad(j\in\mathscr T_H),\qquad
 \bar\Gamma=\Gamma,\qquad
 \sum_{\omega\in\Gamma}d_\omega=0.                              \tag{5.6}
\]

Consequently every union of routing components whose physical cuts
satisfy (2.2)--(2.4) has exact zero all-depth target derivative, exact
complement symmetry, exact point margins, and zero added missing shadows.

#### Proof

Every matched token edge has one new endpoint and one old endpoint of
the same literal type.  No such edge leaves a connected component, so
new and old counts agree inside each component, proving the first
identity.  The added complement edges prove the second.  Summing the
depth-one point derivatives of the first identity gives the third.
The final assertion follows from (3.3)--(3.6). \(\square\)

This theorem turns the desired construction into a concrete routing
problem. If a prospective forest on \(p\) old cycles has initial
remainder \(r_0=p-\sum_p w_p\), and routing or physical conflicts force
rejection of fusion weight \(s\), the final component count is
\(r_0+s\). Thus the required quantitative condition is

\[
                              r_0+s=o(W/H).                       \tag{5.7}
\]

What is not proved is (5.5) for the actual product-SCD absorber menus, or
that the routing components avoid the port and forest conflicts.
Moreover, when the actual product-SCD background has multiplicities,
the authoritative target condition is the coverage system (5.0), not
the one-hot matching equivalence of Theorem 5.1.

## 6. The touched-face cylinder cut

Work inside one physical \(Q_{R+1}\) with old axes
\(D\), \(|D|=R\), and slab axis \(e\).  In a known orientation cube, a
signed depth-\(q\) target is exactly a face descriptor

\[
                              (J,x),                             \tag{6.1}
\]

where \(J\) is the \(q\)-set of touched physical axes and \(x\) chooses
one endpoint on each of the \(R+1-q\) untouched pairs.  For fixed
\(J\), there are exactly

\[
                             2^{R+1-q}                          \tag{6.2}
\]

literal columns of either sign.

For statements using a complete compiler factor, assume \(R\) is an
admissible compiler dimension, in particular \(2R\mid2^R\).

Let \(M\) safe paired-cycle absorbers be proposed in the slab.  Each
creates \(2q\) new signed columns.  Let \(\mathcal J_q\) be the union of
all touched sets appearing in every allowed context/order option.

### Theorem 6.1 (face-cylinder capacity cut)

In any target packing of capacity at most \(b\) per literal column, let
the deficiency mean the number of new occurrences left unmatched to
these capacity slots. Its depth-\(q\), one-sign value is at least

\[
 \boxed{
 \delta_q\ge
 \left[
   2qM-b|\mathcal J_q|2^{R+1-q}
 \right]_+.}                                                    \tag{6.3}
\]

#### Proof

All \(2qM\) new occurrences lie in the literal face cylinder

\[
 \mathcal C_q
 =\{(J,x):J\in\mathcal J_q,\ x\in\{0,1\}^{[R+1]\setminus J}\}.
\]

By (6.2), it contains
\(|\mathcal J_q|2^{R+1-q}\) columns and has total capacity at most \(b\)
times that number.  The all-occurrence side of Hall's inequality gives
(6.3).  Equivalently, \({\bf1}_{\mathcal C_q}\) is the literal target
dual witness. \(\square\)

Here a **complete collar template** includes the physically
coordinate-labelled distinguished axes \((i,e)\) and all four ordered
\((H-1)\)-fringes. Equivalently, it fixes every two-seam touched set at
every depth; the base orientation \(x\) may still vary and is already
counted in (6.2). Suppose that there are at most \(L\) such templates.
One template supplies at most \(2q\) new touched sets at depth \(q\), so

\[
                              |\mathcal J_q|\le2qL.              \tag{6.4}
\]

For the full pairing of the two old facet factors,

\[
                              M={2^R\over2R}.                    \tag{6.5}
\]

Substitution in (6.3) gives

\[
 \boxed{
 \delta_q\ge {q2^R\over R}
       \left(1-{4bLR\over2^q}\right)_+.}                        \tag{6.6}
\]

If \(2^q\ge8bLR\), then

\[
                              \delta_q\ge {q2^{R-1}\over R}.     \tag{6.7}
\]

### Corollary 6.2 (aggregate bounded-menu toll)

Suppose disjoint full slabs cover \(G\) owners and (0.7) holds.  Summing
(6.7) over \(\lceil H/2\rceil\le q\le H\), over both signs, and over the
\(G/2^{R+1}\) slabs gives

\[
                              \Delta_{\le H}
                              \ge {GH^2\over8R}.                 \tag{6.8}
\]

The number of paired-cycle fusions is

\[
 {G\over2^{R+1}}\cdot{2^R\over2R}={G\over4R}.                  \tag{6.9}
\]

Thus the toll is at least \(H^2/2\) per fusion.

#### Proof

The sum of the integers from \(\lceil H/2\rceil\) through \(H\) is at
least \(H^2/4\).  At each depth, the two-sign, all-slab contribution is
at least \(Gq/(2R)\).  This proves (6.8), and (6.9) gives the per-fusion
form. \(\square\)

For \(b=1\), if every removed old column is critical (old load exactly
one), (6.3) is an actual added-hole bound by Theorem 3.1. For \(b>1\),
or without critical one-hot old columns, it is only an
overload/capacity cut and must not automatically be called a
missing-shadow bound.

If \(L=2^{o(H)}\) and \(\log(bR)=o(H)\), condition (0.7) holds
eventually.  In the regime

\[
 R=O(m/\log m),\qquad H/\sqrt m\longrightarrow\infty,
\]

the right side of (6.8) is \(\omega(W)\) when \(G=(1-o(1))W\).

### Sharp scope of the cut

The obstruction does not survive unrestricted context diversity.  For
any

\[
                         K\in\binom{D\setminus\{i\}}{q-1},
\]

put the axes of \(K\) in the required suffix/prefix positions at one
new \(e\)-seam and complete the other three \((H-1)\)-fringes
disjointly.  The inequality \(R\ge4H-3\) supplies enough axes.  Thus
every touched set \(\{e\}\cup K\) occurs in some safe context, and

\[
 |\mathcal J_q|=\binom{R-1}{q-1}                               \tag{6.10}
\]

is possible.

Already the necessary capacity comparison in (6.6) forces, for zero
deficiency,

\[
                              L_q\ge {2^{q-2}\over bR}           \tag{6.11}
\]

and for deficiency \(o(q2^R/R)\) it forces

\[
                    L_q\ge(1-o(1)){2^{q-2}\over bR}.           \tag{6.12}
\]

Hence the exact conclusion of the cylinder theorem is an exponential
physically labelled context-entropy requirement, not a universal no-go.

## 7. The ideal high-entropy packing theorem

The face count also shows that raw local codegree is not the obstruction.
Fix the seam axis \(e\).  Collapse the lower and upper targets belonging
to the same physical face descriptor into one paired token. Its paired
allowed pool is

\[
 \widehat{\mathcal D}_q
 =\{F:L(F)\in\mathcal D_{-,q}\ \hbox{and}\
        U(F)\in\mathcal D_{+,q}\}.
\]

At depth \(q\), the \(e\)-touching descriptor universe has size

\[
                    V_q=\binom R{q-1}2^{R-q+1}.                 \tag{7.1}
\]

For two descriptors, put

\[
 a=|K\cap K'|,\qquad
 \delta=|\{j\notin K\cup K':x_j\ne x'_j\}|.
\]

The exact affine shell size relative to one descriptor is

\[
 M_q(a,\delta)
 =\binom{q-1}{a}
  \binom{R-q+1}{q-1-a}
  2^{q-1-a}
  \binom{R-2q+2+a}{\delta}.                                  \tag{7.2}
\]

For the diverse-fringe absorber, its ordered internal face-pair counts
are

\[
\begin{aligned}
A_q(q-1-d,0)&=4(q-d) &&(1\le d\le q-1),\\
A_q(0,1)&=2q^2.                                                \tag{7.3}
\end{aligned}
\]

For \(R\ge4q-3\), double counting affine images inside the shells
(7.2) gives

\[
 \max_{\hbox{distinct paired faces}}
 { \hbox{pair codegree}\over\hbox{single-face degree}}
 ={1\over q(R-q+1)}.                                           \tag{7.4}
\]

Here is the maximization. For the same-seam pair type at separation
\(d\),

\[
 \rho_d=
 {2(q-d)\over
   q\binom{q-1}{d}\binom{R-q+1}{d}2^d}
 \le {1\over q(R-q+1)}.
\]

Indeed,
\(\binom{q-1}{d}\ge q-d\),
\(\binom{R-q+1}{d}\ge R-q+1\), and \(2^d\ge2\); equality occurs at
\(d=1\). For the cross-seam type,

\[
 \rho_\times=
 {q\over
   \binom{R-q+1}{q-1}2^{q-1}(R-2q+2)}
 \le {1\over q(R-q+1)}.
\]

For \(q=1\) this is equality. For \(q\ge2\), put
\(n=R-q+1\ge3q-2\); since
\(\binom n{q-1}(n-q+1)=q\binom nq\), the desired inequality reduces to
\(2^{q-1}\binom nq\ge qn\). This follows from
\(\binom nq\ge\binom n2\) and
\(2^{q-2}(n-1)\ge q\).

In particular, there is no same-layer antipodal high-codegree atom for
the crossing-face image.

There is a simple integral theorem which would exploit this dispersion.

### Theorem 7.1 (allowed-pool greedy packing)

Fix a physical forest with \(n\) slots.  For every slot \(s\), suppose
there is an independently composable probability distribution
\(\nu_s\) on \(\Omega_s^{\mathcal D}\), so every option is already
contained in the all-depth allowed pools (5.1).  Suppose

\[
\Pr_{\nu_s}\{T\in N_{s,c}\}\le\beta_{s,c}
 \qquad(T\in\mathcal D_c).                                    \tag{7.5}
\]

Put

\[
               k_c=\max_{r,\omega\in\Omega_r^{\mathcal D}}
                         |N_{r,c}(\omega)|.
\]

If

\[
       (n-1)\max_s\sum_c k_c\beta_{s,c}<1,                     \tag{7.6}
\]

then one option may be chosen in every slot so that all new columns are
pairwise disjoint.  Hence the forest has zero additional missing-shadow
loss.

#### Proof

Choose the slots greedily. After \(k<n\) choices, the forbidden set in
colour \(c\) has at most \(k\,k_c\) entries. A random option for the next
slot \(s\) meets a forbidden column with probability at most

\[
                   k\sum_ck_c\beta_{s,c}<1.
\]

The collision count is a nonnegative integer, so some option has zero
collisions.  Continue.  Every chosen option lies in the allowed pool, so
Theorem 5.1 finishes the proof. \(\square\)

Now apply Theorem 7.1 to the **sign-quotient hypergraph**, whose
capacity vertices at colour \(q\) are
\(F\in\widehat{\mathcal D}_q\) and whose option image
\(\widehat N_{s,q}\) consists of its paired lower/upper faces. In the
ideal full-affine paired-face menu, provided the whole unconditioned
affine orbit already lies in those paired allowed pools,

\[
                         \beta_q={2q\over V_q}.                  \tag{7.7}
\]

Merely conditioning the orbit on
\(\widehat{\mathcal D}_q\) does not preserve (7.7); the inclusion
probability can concentrate. The assertion here is therefore about an
actually admissible full orbit.

Put

\[
                         S_{R,H}
 =\sum_{q=1}^{H}{4q^2\over V_q}.                                \tag{7.8}
\]

Indeed, in this quotient \(k_q=|\widehat N_{s,q}|=2q\), so (7.8) is
exactly \(\sum_qk_q\beta_q\). Applying the typed two-sign theorem
without quotienting would instead give the weaker constant \(96\).

If \(R\ge4H-3\), then

\[
                         S_{R,H}\le48\,2^{-R}.                  \tag{7.9}
\]

Indeed,

\[
 \binom R{q-1}\ge\binom{4q-3}{q-1}\ge4^{q-1},
\]

and therefore

\[
 {4q^2\over V_q}
 \le 2^{-R}{4q^2\over2^{q-1}}.
\]

The sum of \(q^2/2^{q-1}\) over \(q\ge1\) is \(12\), proving (7.9).

Consequently, if \(n<2^R/R\) and \(R>48\), condition (7.6) holds in the
ideal paired-descriptor model. When \(p=2^R/R\) is integral, a forest on

\[
                         p={2^R\over R}
\]

old facet cycles with \(p-r\) raw one-edge slots would then pack with
zero local loss; \(r=o(2^R/H)\) would give the desired component scale
inside the slab. For compound options the ledger is instead
\(p-\sum w_p\).

### Why Theorem 7.1 is still conditional

None of the following is presently proved.

1. A fixed \(4R\)-owner cycle pair does not have a full affine menu.
   Affine conjugation moves its owner set and cut edge.
2. The existing factor chooses one conjugate for an entire \(Q_R\)
   factor.  It does not provide independent conjugates for its cycle
   slots.
3. There is no proved \(H\)-collar-disjoint near-spanning forest in the
   common-edge overlay of the two facet factors.
4. Most importantly, no theorem shows that the full-affine options lie
   inside the physical allowed pools \(\mathcal D_c\) simultaneously at
   all depths and both signs.  A target free in its own slab may be
   retained by another packet.
5. The calculation packs raw sign-collapsed absorber slots. Complement
   superoptions correlate two such menus, and no exact Euler-balanced
   distribution has been supplied. The constant \(48\) has not been
   transferred to that compound catalogue.

Thus (7.9) proves that local descriptor codegree is favorable; it does
not prove the global allowed-pool hypothesis.

## 8. A carrier cut surviving arbitrary context entropy

The bounded-template cut can be evaded by exponentially many contexts.
A frozen physical projection cannot.

Assume first, for clarity, that \(m\) is divisible by \(4\), and choose

\[
                         E\subset[2m],\qquad |E|=e={m\over2}.    \tag{8.1}
\]

Suppose every physical transition in every allowed factor, absorber, and
configuration deletes and inserts coordinates of \(E\).  Thus

\[
                         X_t\cap E^c=X_0\cap E^c                \tag{8.2}
\]

along every path.

For \(Y\subseteq E^c\), define

\[
\begin{aligned}
\mathcal O_Y
 &=\{X\in\tbinom{[2m]}m:X\cap E^c=Y\},\\
\mathcal T_Y
 &=\{T\in\tbinom{[2m]}{m-q}:T\cap E^c=Y\}.
\end{aligned}                                                   \tag{8.3}
\]

Put \(t=m-q-|Y|\).  Their exact sizes are

\[
                         |\mathcal O_Y|=\binom e{t+q},\qquad
                         |\mathcal T_Y|=\binom et.              \tag{8.4}
\]

Every covered target in \(\mathcal T_Y\) comes from a root in
\(\mathcal O_Y\), and each root emits only one lower depth-\(q\) target.
Hence every complete configuration covers at most

\[
                         \min\{|\mathcal O_Y|,|\mathcal T_Y|\}  \tag{8.5}
\]

distinct targets in that fibre.

Fix \(A>0\) and

\[
                         q=A\sqrt m+O(1).
\]

Write

\[
                         t={e\over2}-{q\over4}+x
\]

and take the band \(|x|\le q/8\).  Uniformly in this band, Stirling's
central expansion gives

\[
\begin{aligned}
\log{|\mathcal O_Y|\over|\mathcal T_Y|}
 &=-{2\over e}
  \left[
   \left({3q\over4}+x\right)^2
   -\left(-{q\over4}+x\right)^2
  \right]+o(1)\\
 &\le-{q^2\over2e}+o(1)
  =-A^2+o(1).                                             \tag{8.6}
\end{aligned}
\]

Let \(\mathcal B_q^-\) be the union of the target fibres in this band.
The hypergeometric local central limit theorem, equivalently the same
uniform Stirling expansion summed over the band, has variance
\((3/32+o(1))m\). Hence the band mass tends to
\(2\Phi(A/\sqrt6)-1\), where \(\Phi\) is the standard normal
distribution function. In particular, with

\[
                  c_A={2\Phi(A/\sqrt6)-1\over2}>0,
\]

for all sufficiently large \(m\),

\[
                         |\mathcal B_q^-|
                         \ge(c_A-o(1))N_q.                       \tag{8.7}
\]

Here \(N_q=\binom{2m}{m-q}\). Also

\[
                         {N_q\over W}=e^{-A^2+o(1)}.             \tag{8.8}
\]

The same estimates hold uniformly for
\(e=m/2+o(\sqrt m)\). In that case center the band at

\[
                     t={e\over2}-{eq\over2m}+x,\qquad |x|\le q/8.
\]

The two binomial deviations are
\(-eq/(2m)+x\) and \(q-eq/(2m)+x\); their squared difference is
\((1-e/m)q^2+2qx\). After multiplication by \(2/e\), its minimum over
the band is \(A^2+o(1)\). The corresponding hypergeometric band still
has positive \(A\)-dependent mass. Thus (8.6)--(8.8), and the theorem
below, are unchanged.

### Theorem 8.1 (literal carrier Hall cut)

For every fixed \(A>0\), every integer sequence
\(q=q_m=A\sqrt m+O(1)\le H\), and every carrier
\(|E|=m/2+o(\sqrt m)\), every complete joint factor/absorber
configuration satisfying (8.2) has, as \(m\to\infty\),

\[
 \boxed{
 \mathfrak H_q^-
 \ge(1-e^{-A^2}-o(1))|\mathcal B_q^-|
 =\Omega_A(W).}                                                \tag{8.9}
\]

The complement upper family gives the same bound.

#### Proof

Sum (8.5) and (8.6) over the disjoint fibres defining
\(\mathcal B_q^-\).  At most an \(e^{-A^2}+o(1)\) fraction of that band
can be covered.  Equations (8.7)--(8.8) make the deficit a positive
constant times \(W\).  Complementation proves the upper statement.
\(\square\)

The indicator of

\[
 \mathcal B_q^-\mathbin{\dot\cup}
 \kappa(\mathcal B_q^-)
\]

is a complement-symmetric literal configuration-dual witness.  The cut
is statewise and therefore survives arbitrary correlation, arbitrary
collar-template entropy, every forest choice, and exact point-Euler
balance.

This obstruction is nonvacuous for the carrier-restricted partial atlas
in the present scale. One may choose an admissible \(R\) with

\[
                         {m\over512}<R\le {m\over256},
\]

take \(E\) to be a union of complete \(O(\log m)\)-sized macroblocks,
put all physical packet and slab axes inside \(E\), and take
\(H\le R/4\). Then \(|E|=m/2+O(\log m)\). The rank-twisted carrier
packetization has owner leave

\[
                             L=e^{-\Omega(m)}W.
\]

Even granting the leave arbitrary favorable traces repairs at most
\(L=o(W)\) targets at the fixed depth, so (8.9) survives. Availability
of each local safe absorber remains conditional on its already stated
parallel-cut and four-port hypotheses; no abundance theorem is asserted
here.

Theorem 8.1 does not obstruct a projection-free atlas whose allowed axes
connect every positive-density coordinate cut.  It proves that such a
projection-free hypothesis is logically necessary; local safety,
complement symmetry, template entropy, and point balance do not imply it.

## 9. Audited boundary

### Proved

* the exact constants \(2q,4q,2H(H+1),4H(H+1)\);
* the complement token quotient and the active-cube antipodal
  component-neutrality trap;
* exact collar and graphic-forest constraints for separated absorbers;
* the literal hinge identity (3.4) and arbitrary-target cut (3.5);
* the arbitrary-load physical coverage dual (3.8)--(3.9);
* the full fractional LP/Farkas dual (4.2)--(4.4);
* the exact defect packing hypergraph, its zero-loss matching
  equivalence, and the weighted fractional Hall inequality;
* the exact target-routing component criterion;
* the touched-face cylinder cut and the zero-deficiency entropy
  threshold \(2^{q-2}/(bR)\);
* the conditional full-affine greedy theorem with constant \(48\);
* the \(\Omega_A(W)\) physical carrier cut.

### Not proved

* targetwise balance (5.5) for the actual product-SCD absorber menu;
* an \(H\)-separated near-spanning common-edge forest;
* independently composable affine options on fixed cycle slots;
* the all-depth allowed-pool hypothesis (5.2);
* integral rounding of the unrestricted configuration LP;
* an \(\Omega(W)\) target cut for a fully projection-free,
  exponentially context-diverse absorber atlas;
* a multiway selection with \(o(W)\) missing shadows in that unrestricted
  atlas; or
* coefficient one.

The physically coordinate-labelled bounded-template lane satisfying
\(\log(bR)=o(H)\), and the frozen-carrier lane, are therefore closed by
literal physical cuts. This does not cover a bounded abstract
description whose one template itself contains exponentially many
coordinate-labelled touched sets. The fully dispersed lane remains
open, but its exact missing statement is now narrow: construct a
projection-free, complement-compatible routing decomposition whose
complete options lie in the common all-depth allowed pools, or exhibit a
nonadditive target price in (4.4) with linear dual gain.
