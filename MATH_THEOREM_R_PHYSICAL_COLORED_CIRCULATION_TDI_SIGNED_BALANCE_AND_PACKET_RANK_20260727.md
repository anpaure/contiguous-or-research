# Physical coloured circulation at constant one: whole-packet columns, TDI failure, signed balance, and the mesoscopic fusion wall

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 W=\binom{2m}{m},\qquad
 H=\lfloor\sqrt{m\log m}\rfloor,\qquad
 M=m+H,\qquad N=N_H=\binom{2m}{m-H}.
\tag{0.1}
\]

All asymptotics are as \(m\to\infty\). This report gives the following
resolution of the integral coloured-circulation/physical-packet route.

1. The exact physical linear formulation must use **whole-packet
   columns**. A column records every ordered state, owner, signed target,
   seam-crossing window, port, resource, tag, component, voltage, and
   implementation cost of one jointly legal packet. Edgewise seam
   variables are only a projection. With complete packet columns, binary
   solutions are literally physical, and the component, seam, and
   installation ledgers are linear.

2. For the common-core tight-path fusion (CCTPF) catalogue, every column
   is one direct literal path. Hence a target-simple matching of
   \(t=N-\ell\) roots has

   \[
             C=t\le N,\qquad K_{\rm phys}=0,
   \tag{0.2}
   \]

   and exact protected-target leave

   \[
             \mathfrak H=\Delta+k\ell,
             \qquad \Delta=o(W).
   \tag{0.3}
   \]

   Thus \(\ell=o(N/\sqrt m)\) gives coefficient one. The
   \(O(N)\)-component and direct physical-installation requirements are
   already solved in this reduction; the unresolved condition is the
   near-perfect integral matching.

3. The natural physical column relaxation is neither TU nor TDI. There
   are six genuine one-component, zero-monodromy promotion frames on
   three roots whose coefficient matrix contains a \(6\times6\) minor of
   determinant \(2\). An integral objective has fractional optimum
   \(3/2\) and integral optimum \(1\). On the six-column
   root-saturating restriction the unique point is \(1/2\) on every
   option, while no integral point exists. This is a literal
   Hamilton-packet obstruction, not a target-node surrogate.

4. The calibrated CCTPF odd-port prism strengthens the preceding
   obstruction: the same half-integral root saturation respects every
   protected middle, lower, and upper target under one admissible common
   nested tag profile. Hence adding the actual coloured rows does not
   restore a general TDI theorem.

5. There is nevertheless an exact positive signed-graph regime. For a
   reciprocal two-choice packet system, the root-saturating relaxation is
   integral exactly when its signed constraint graph is balanced.
   Unbalanced components are forced to the unique half vector. Moreover,
   if the two choices come from two already legal complete endpoint
   factors and every added port constraint is pairwise affine in the
   component shore bits, the signed graph is automatically balanced and
   gauges to equality constraints. Thus the genuine two-endpoint
   pairwise-affine subproblem has a TU description.

6. Balancedness does not guarantee useful mobility. Port constraints may
   merge every bare owner-overlay component into one block, leaving only
   the two endpoint factors. Higher-arity packet constraints also escape
   the graphic/TU theorem.

7. The full PBBS seam ledger gives a sharp final-component aggregation
   requirement. If
   \(C\le K N\) final components rebundle all inherited PBBS runs, then a
   positive fraction of the inherited-run mass lies in components
   containing

   \[
        \Omega\!\left({m\over KH}\right)
   \tag{0.4}
   \]

   runs. In particular, final components of uniformly bounded inherited
   run rank cannot number only \(O(N)\). This does not prevent a
   correlated sequence of bounded primitive switches from building such
   components. The proved PBBS lower scale is mesoscopic,
   \(\Omega(m/H)\); an abstract ordered-word construction attains
   \(O(m/H)\), but its realization by PBBS-authorized packets remains
   open. A directly literal whole-cycle packet at any certified rank
   has \(K_{\rm phys}=0\); seam count alone creates no extra-letter
   charge.

8. Every isolated, empty-exterior CCTPF obstruction on fewer than

   \[
   \exp\left\{
     \left({\log2\over4}-o(1)\right)\sqrt{m\log m}
   \right\}
   \tag{0.5}
   \]

   roots repairs integrally with one direct literal path per root. Thus
   the determinant-two prism and every bounded signed blossom are
   locally repairable. A maximum matching which defeats this repair must
   exhibit the global exterior-exposure inequality (8.6); high exposure
   is necessary for failure of the greedy repair, not sufficient for an
   obstruction.

Coefficient one is not proved. The natural unaugmented incidence
description is definitively non-TDI; odd-cycle cuts or an extended
formulation are not excluded. The pairwise two-endpoint signed regime is
solved, and the
component/physical-cost part is reduced to final-component aggregation. What
remains is a near-perfect matching or a cancellative augmentation through
the global exterior wall.

## 1. Calibrated common-history parameters

Write

\[
 s=m-H,\qquad L=m-3H+1,\qquad \Lambda={W\over N}.
\tag{1.1}
\]

The calibrated choice satisfies, for fixed positive constants
\(c_0,C_0\),

\[
 L+c_0H\le \Lambda\le m+C_0H
\tag{1.2}
\]

for all sufficiently large \(m\). For \(1\le q<H\), define

\[
 b_0=L,
\qquad
 b_q=\min\left\{L-1,\,
 \max\left\{0,\left\lfloor{N_q\over N}\right\rfloor-1\right\}
 \right\},
\tag{1.3}
\]

where \(N_q=\binom{2m}{m-q}\). Put

\[
 k=L+2\sum_{q=1}^{H-1}b_q
   =(\sqrt\pi+o(1))m^{3/2}.
\tag{1.4}
\]

For a fixed CCTPF root \(U\), fixed good \(2H\)-core, and fixed nested
tag profile of sizes \(b_q\), let \(\mathcal F_U\) be its set of literal
tail histories. Every \(F\in\mathcal F_U\) has one complete protected
target set

\[
                         \Gamma(F),
 \qquad |\Gamma(F)|=k,
\tag{1.5}
\]

containing its retained middle targets and both signed active traces.
The same tail order produces all of them.

The maximal normalized single-target port exposure is

\[
 p_*=\max\left\{
 {L\over\binom{s}{H}},
 \max_{\substack{1\le q<H\\b_q>0}}
 \left\{
 {b_q\over\binom{s}{H-q}},
 {b_q\over\binom{s}{H+q}}
 \right\}
 \right\}.
\tag{1.6}
\]

The audited port count gives

\[
 \log {1\over kp_*}
 \ge
 \left({\log2\over4}-o(1)\right)\sqrt{m\log m}.
\tag{1.7}
\]

## 2. Exact whole-packet coloured-circulation formulation

A physical **master-packet** column \(P\) is not merely a list of
proposed joins. It contains its entire jointly legal, component-closed
output. Distinct selected columns are not subsequently fused: a fusion
and its connector must either be one larger certified column or be
represented in an expanded connector model whose component count is
recomputed from the resulting occurrence graph. In the component-closed
master formulation, record the following integral data.

* \(u_{P,\xi}\): every owner, carrier, exclusivity, packet-overlap,
  entry-port, exit-port, collar, and other physical resource incidence;
* \(\chi_P(o)\): every selected tagged ordered occurrence
  \(o=(A,e,\tau,\xi)\), including physical provenance \(\xi\);
* \(a_P(D)\): the complete middle-owner load, including all
  seam-crossing windows;
* \(b^\pm_{P,q}(T)\): the complete tagged signed-target loads;
* \(n(P)\): principal literal phase count;
* \(c(P)\): number of component-closed output paths/cycles;
* \(r(P)\): number of inherited PBBS runs, when a PBBS provenance is
  being retained;
* \(s(P)\): number of certified internal rethreading seams;
* \(a_P^{\rm seam}(D)\) and
  \(b_{P,q}^{\pm,{\rm seam}}(T)\): the subloads contributed by windows
  crossing those seams; these are marked subcounts of \(a_P(D)\) and
  \(b_{P,q}^{\pm}(T)\), not new target copies;
* \(k_{\rm phys}(P)\): literal installation length not already contained
  in the packet word and its ordinary component collars.

The column is called **certified** only if its ordered state flow, start
injection, diagonal ports, one-pass voltage/stabilizer condition, tag
schedule, and every internal resource equality have already been checked.
In particular, all seam-crossing owners and signed traces occur in
\(a_P,b^\pm_{P,q}\).

Let \(x_P\in\{0,1\}\). The exact packet/resource integer system is

\[
 \sum_Pu_{P,\xi}x_P\le {\rm cap}(\xi)
 \qquad(\hbox{every physical resource }\xi),
\tag{2.1}
\]

\[
 \mu_0(D)=\sum_Pa_P(D)x_P,
\qquad
 \mu^\pm_{q,T}=\sum_Pb^\pm_{P,q}(T)x_P,
\tag{2.2}
\]

together with every root/site choice equality, exact owner/resource
exhaustion equality, common-tag census, and target capacity or defect
row. Omitting those equalities leaves only a conditional schema, not an
exact-factor formulation. Its exact scalar ledgers are

\[
 C(x)=\sum_Pc(P)x_P,\qquad
 R(x)=\sum_Pr(P)x_P,\qquad
 S(x)=\sum_Ps(P)x_P,\qquad
 K_{\rm phys}(x)=\sum_Pk_{\rm phys}(P)x_P.
\tag{2.3}
\]

The full seam-crossing census is likewise linear:

\[
 \mu_0^{\rm seam}(D)=\sum_Pa_P^{\rm seam}(D)x_P,
 \qquad
 \mu_{q,T}^{\pm,{\rm seam}}
   =\sum_Pb_{P,q}^{\pm,{\rm seam}}(T)x_P.
\tag{2.3a}
\]

The quantities in (2.3a) are already included in the corresponding
total loads in (2.2). They are exposed separately only to prevent a
projection from silently dropping crossing windows.

For an absolute master-column catalogue with a disjoint frozen exterior,
the correct occurrence link is

\[
 z_o=z_o^{\rm ext}+\sum_P\chi_P(o)x_P.
\tag{2.4}
\]

For a seed-relative trade catalogue, instead record the signed change
\(\delta\chi_P(o)\in\mathbb Z\) and use

\[
 z_o=z_o^{,0}+\sum_P\delta\chi_P(o)x_P.
\tag{2.4a}
\]

One must not add nonnegative absolute occurrence columns to a baseline
which those columns replace. In either formulation, impose the
safe-state balance, coordinate degree, subtour or
cycle-factor, tag, and one-pass voltage rows on \(z\). Equations
(2.4)--(2.4a) are the essential diagonal links. Replacing them by independent target-node or
seam-edge flows permits a prefix of one packet to leave through another
packet's suffix and is not physical.

### Theorem 2.1 (exactness and literal cost of whole columns)

Suppose every catalogue column is certified in the literal sense just
defined, and suppose (2.1)--(2.4), or the signed variant (2.4a), contain
all and only the intercolumn
compatibility conditions for this catalogue, including every
higher-order condition after any required state expansion. Then the
binary solutions of (2.1)--(2.4) are exactly its globally compatible
physical installations. For every such solution,

\[
 L_{\rm packet}
 \le
 \sum_Pn(P)x_P+2HC(x)+K_{\rm phys}(x)
 +\mathfrak H(x),
\tag{2.5}
\]

where \(\mathfrak H(x)\) is the number of genuinely missing protected
targets appended literally.

A directly emitted literal cyclic or path packet has
\(k_{\rm phys}(P)=0\). Its internal non-PBBS successors create no term
proportional to \(Hr(P)\); the full target effects are already present in
the column. Owner-multiset preservation is an additional hypothesis for
an in-place exact-factor splice and is not implied merely by completing
isolated coordinate words.

#### Proof

Every certified column is one actual literal object. The resource rows
are precisely the compatibility conditions between selected objects, so
binary feasibility is sufficient and necessary. Component closure makes
\(C=\sum_Pc(P)x_P\) exact; a separate cross-column connector model would
instead have to derive \(C\) from its selected occurrence graph. Concatenate one
linearization of each output component. Its principal positions give
\(\sum n(P)x_P\), and the standard full-radius opening repeats at most
\(2H\) positions per component. Add the explicitly declared
implementation length and append every remaining target once. This is
(2.5).

All windows crossing an internal seam lie inside the already selected
whole packet and were included in (2.2). Charging a fresh collar at each
internal seam would count the same literal object twice. \(\square\)

### CCTPF specialization

For the CCTPF catalogue, the natural rooted matching relaxation is

\[
 \mathcal P_{\rm CCTPF}=
 \left\{x\ge0:
 \sum_{F\in\mathcal F_U}x_F\le1\ (\forall U),\
 \sum_{F:T\in\Gamma(F)}x_F\le1\ (\forall T)
 \right\}.
\tag{2.6}
\]

Its integral points are exactly target-simple physical history
matchings. The root-saturating face replaces the root inequalities by
equalities.

For an arbitrary integral objective \(c_F\), the exact linear-programming
dual is

\[
 \min\left\{
 \sum_U\alpha_U+\sum_T\beta_T:
 \alpha_{\operatorname{root}(F)}
 +\sum_{T\in\Gamma(F)}\beta_T\ge c_F,\
 \alpha,\beta\ge0
 \right\}.
\tag{2.7}
\]

The root-local path network is integral before the common target rows are
adjoined. Thus every failure below comes from physical inter-root colour
coupling, not from a fractional tail order inside one root.

## 3. Components, physical installation, and the exact matching leave

Let

\[
 B=W+2\sum_{q=1}^{H-1}N_q
\tag{3.1}
\]

be the protected target count, and put

\[
 \Delta=B-kN
 =(W-LN)+2\sum_{q=1}^{H-1}(N_q-b_qN)
 =o(W).
\tag{3.2}
\]

### Theorem 3.1 (near-perfect CCTPF matching ledger)

Let \(\mathcal M\) be a target-simple CCTPF history matching of size

\[
                         t=N-\ell.
\tag{3.3}
\]

Then:

1. the selected histories cover exactly \(kt\) distinct protected
   targets, so
   \[
                        \mathfrak H=B-kt=\Delta+k\ell;
   \tag{3.4}
   \]
2. each history is one direct literal path, hence
   \[
                        C=t\le N,\qquad K_{\rm phys}=0;
   \tag{3.5}
   \]
   it has no internal rethreading seam, and every ordinary consecutive
   delayed-atom adjacency is already part of its whole column rather
   than a separately installable edge;
3. before the exterior product-SCD block, a literal central word has
   length at most
   \[
          t(L+2H)+(B-kt)+2N;
   \tag{3.6}
   \]
4. if \(\ell=o(N/\sqrt m)\), then (3.6), the exterior block, and the odd
   lift give coefficient one.

#### Proof

Target simplicity and (1.5) give (3.4). Emit the delayed-atom
linearization of every selected core-safe path. Each costs at most
\(L+2H\), proving (3.5) and the first term of (3.6). Append every
uncovered protected target and the two complete depth-\(H\) boundary
layers, proving (3.6).

At \(t=N\), equation (3.6) is

\[
 W+2HN+2N+
 2\sum_{q=1}^{H-1}(N_q-b_qN)=W+o(W).
\tag{3.7}
\]

Reducing \(t\) by \(\ell\) increases the bound by at most \(k\ell\).
Since \(k=(\sqrt\pi+o(1))m^{3/2}\) and
\(N=(1+o(1))W/m\),

\[
       k\ell=o(W)
       \quad\Longleftrightarrow\quad
       \ell=o(N/\sqrt m).
\tag{3.8}
\]

The exterior product-SCD word is \(o(W)\), and the standard trimmed lift
preserves coefficient one. \(\square\)

Thus the \(O(N)\)-component and direct physical-installation gates do not
remain after a near-perfect CCTPF matching. The sole unresolved
condition in this route is integral target-simple selection at precision
(3.8).

## 4. A literal zero-monodromy TDI obstruction

This section works directly in the full promotion-frame catalogue.
Assume

\[
 H\ge2,\qquad m\ge\max\{5,3H-2\}.
\tag{4.1}
\]

Choose \(K\subset[2m]\) with \(|K|=m+1\), and choose pairwise disjoint

\[
 E_0,E_1,E_2\subset[2m]\setminus K,
 \qquad |E_i|=H-1.
\tag{4.2}
\]

This is possible because \(m+1+3(H-1)\le2m\). Choose six distinct
labels

\[
 z_{i,b}\in K,
 \qquad i\in\mathbb Z/3\mathbb Z,\quad b\in\{0,1\}.
\tag{4.3}
\]

Put

\[
 U_i=K\mathbin{\dot\cup}E_i,\qquad
 A_i=[2m]\setminus U_i.
\tag{4.4}
\]

For every \(i,b\), choose a cyclic permutation \(c_i^b\) of \(U_i\)
containing the consecutive block

\[
                z_{i-1,b},\quad E_i,\quad z_{i,b},
\tag{4.5}
\]

with \(E_i\) in a fixed order. Let \(F_i^b\) be its literal promotion
frame

\[
 F_i^b=
 \left\{
 A_i\cup J:
 J\hbox{ is a cyclic }H\hbox{-window of }c_i^b
 \right\}.
\tag{4.6}
\]

Every \(F_i^b\) is one integral Hamilton coordinate frame, one physical
component, and zero monodromy.

For each \(i,b\), define the middle owner

\[
 D_{i,b}=([2m]\setminus K)\cup\{z_{i,b}\}.
\tag{4.7}
\]

### Theorem 4.1 (physical odd triangle and TDI failure)

The six complete frames above have the following properties.

1. \(D_{i,b}\) occurs exactly in \(F_i^b\) and \(F_{i+1}^b\) among the
   six columns.
2. Every middle-owner row has degree at most two on these six columns.
3. The whole-frame coefficient matrix contains a \(6\times6\) minor of
   determinant \(2\).
4. The natural unaugmented rooted incidence system, containing only root
   and physical target-capacity rows, is not TDI: an integral objective
   has fractional optimum \(3/2\) and integral optimum \(1\).
5. On the six-column restricted face (all other columns at these roots
   fixed to zero)
   \[
                   x_i^0+x_i^1=1\qquad(i=0,1,2),
   \tag{4.8}
   \]
   the unique feasible point is
   \[
                   x_i^0=x_i^1={1\over2},
   \tag{4.9}
   \]
   and there is no integral point.

#### Proof

The two cyclic \(H\)-windows containing all \(H-1\) consecutive letters
of \(E_i\) are precisely its two flank windows. By (4.5), their extra
letters are \(z_{i-1,b}\) and \(z_{i,b}\). This proves that the displayed
owners occur as claimed.

Suppose one owner \(D\) occurs in frames with two distinct root indices
\(i\ne j\). Since \(D\) contains both \(A_i\) and \(A_j\),

\[
 [2m]\setminus K=A_i\cup A_j\subseteq D.
\tag{4.10}
\]

As \(|D|=m\), one has

\[
 D=([2m]\setminus K)\cup\{z\}
\tag{4.11}
\]

for one \(z\in K\). Its \(H\)-window in root \(i\) must be
\(E_i\cup\{z\}\), hence a flank window. The six flank labels in (4.3)
are distinct, so this owner occurs in exactly the two adjacent frames
indexed by that label and cannot also occur in the other option of
either root. An owner confined to one root index occurs in at most the
two options there. This proves Item 2.

Order the columns as

\[
 (x_0^0,x_1^0,x_2^0\mid x_0^1,x_1^1,x_2^1).
\]

Take the three root rows followed by the three rows
\(D_{0,1},D_{1,1},D_{2,1}\). The resulting matrix is

\[
 \begin{pmatrix}
 I_3&I_3\\
 0&A
 \end{pmatrix},
 \qquad
 A=
 \begin{pmatrix}
 1&1&0\\
 0&1&1\\
 1&0&1
 \end{pmatrix},
 \qquad \det A=2.
\tag{4.12}
\]

This proves non-TU.

For TDI, give objective coefficient one to
\(F_0^1,F_1^1,F_2^1\), and zero to every other column of the complete
catalogue. Weighting those three columns by \(1/2\) is feasible: every
root load is \(1/2\), and Item 2 makes every target load at most one.
Its value is \(3/2\). Summing the three displayed \(b=1\) target rows
gives the matching upper bound \(3/2\). Equivalently, the dual (2.7)
puts weight \(1/2\) on these three targets and zero elsewhere.

An integral matching can choose at most one of the three cost-one
columns because they form a conflict triangle. Hence its value is one.
The right-hand side and objective are integral, but the exact dual
optimum is nonintegral. The unaugmented incidence description is not
TDI. This conclusion does not exclude an integral strengthening by
odd-cycle cuts or a TDI extended formulation.

Finally impose (4.8) and put \(y_i=x_i^1\). The \(b=1\) capacities give

\[
 y_i+y_{i+1}\le1,
\tag{4.13}
\]

while the \(b=0\) capacities give

\[
 y_i+y_{i+1}\ge1.
\tag{4.14}
\]

Thus \(Ay=\mathbf1\). Since \(\det A=2\), its unique solution is
\(y=(1/2,1/2,1/2)\). No integral solution exists. \(\square\)

The obstruction already consists of complete one-component,
zero-monodromy frames. A hypothetical three-root integral choice would
have only three components and collar at most \(6H\). Thus the failure is
integrality, not component proliferation or installation cost.

If the common-tag architecture is present, assigning stopping tag zero
to every phase makes the positive-depth rows silent on this local
subcatalogue. This is a legitimate local packet obstruction, but it does
not by itself meet the global all-depth tag census, and membership in a
narrower PBBS-authorized trade catalogue is not claimed.

## 5. The obstruction survives complete coloured histories

The preceding middle-only witness has a fully coloured physical
counterpart in the CCTPF catalogue.

Assume \(H\ge5\) and \(m\ge5H\). Choose disjoint sets

\[
 |C|=m-H,\qquad |B|=H+1,\qquad |E_i|=H-1,
\tag{5.1}
\]

put \(K=C\cup B\), choose a common \(2H\)-core \(Q\subset C\), and put

\[
                         U_i=K\cup E_i.
\tag{5.2}
\]

Choose six distinct \(z_{i,b}\in B\), and write
\(S_i=U_i\setminus Q\). At root \(i\), choose two literal tail orders on
\(S_i\) whose order contains

\[
                 z_{i-1,b},\quad E_i,\quad z_{i,b}.
\tag{5.3}
\]

For both bits, put the other four special \(z\)-labels in the first
\(H\) tail positions, begin the displayed block at tail position
\(3H\), and fill the unused positions arbitrarily. Thus every other
special label has positional distance at least \(2H\) from the
\(E_i\)-block. The two flank \(H\)-windows occur at retained phases
\(2H\) and \(2H+1\). For all sufficiently large calibrated \(m\),
\(b_1=L-1\); use one admissible nested phase family for both choices at
each root whose unique depth-one-inactive retained phase is
\(a=2H\). Let \(P_i^b\) be the resulting full tagged history. Put

\[
                         T_{i,b}=K\setminus\{z_{i,b}\}.
\tag{5.4}
\]

### Theorem 5.1 (coloured odd-port prism)

The histories \(P_i^b\) satisfy:

1. \(P_i^b\) contains exactly \(T_{i-1,b},T_{i,b}\) among the six
   displayed targets;
2. every protected physical target at every active middle, lower, and
   upper rank belongs to at most two of the six histories;
3. \(x(P_i^b)=1/2\) satisfies all three root equations, the common
   nested tag profile, and every protected target capacity;
4. no integral choice of one history at every root is target-simple.

Consequently the natural unaugmented full-history incidence system is
not TDI. For the integral objective equal to one on these six columns
and zero on every other column, the fractional optimum is three while
the integral optimum is at most two. On the six-column root-saturating
restriction, the displayed hole-plus-repeat defect is zero fractionally
and at least two integrally.

#### Proof

The middle statement is the flank-window argument of Theorem 4.1.
Suppose a protected target is shared by two different roots. It lies in
\(U_i\cap U_j=K\). An upper target of rank at least \(m+2\) is therefore
impossible. A rank-\((m+1)\) target would have to be \(K\), requiring the
deletion interval \(E_i\) at the one phase deliberately made inactive at
depth one.

At a lower rank \(m-q\), write the shared target as \(K\setminus Z\),
where \(|Z|=q+1\). In root \(i\), its deletion interval is
\(E_i\cup Z\), of length at most \(2H-1\). Any such interval containing
the consecutive \(E_i\)-block contains at least one flank label and, by
the prescribed spacing, no other special \(z\)-label. A fixed \(Z\)
therefore occurs in at most the two histories adjacent to that flank.
This proves Item 2. The root and capacity check for the half vector is
immediate.

An integral root-saturating choice is a bit assignment
\((b_0,b_1,b_2)\). Avoiding \(T_{i,b}\) twice requires
\(b_i\ne b_{i+1}\) for all three edges of the triangle, which is
impossible. The defect statement follows because a monochromatic edge
has loads \(2,0\) on its two bit targets.

For the TDI assertion, the half vector has objective value three by
Item 3. For either fixed bit the three corresponding columns form a
conflict triangle witnessed by three distinct middle targets, so an
integral matching uses at most one column of each bit and has objective
at most two. The right-hand side and objective are integral; hence the
unaugmented full column system is not integral and cannot be TDI.
\(\square\)

This theorem uses actual complete tagged histories and nontrivial
coloured rows. It still does not show that the half vector extends to a
global root-saturating solution, and the unused histories in the three
complete root fibres provide integral escapes.

## 6. Exact signed-graph classification

Let \(G=(R,E)\) be a finite loopless multigraph. Root \(i\) has two packet options
\(F_i^0,F_i^1\), with variables

\[
                         x_i^0+x_i^1=1.
\tag{6.1}
\]

Label an edge \(ij\) by \(\sigma_{ij}\in\{0,1\}\).

* If \(\sigma_{ij}=0\), the cross pairs \((0,1),(1,0)\) conflict, so
  equal bits are allowed.
* If \(\sigma_{ij}=1\), the same-bit pairs \((0,0),(1,1)\) conflict, so
  unequal bits are allowed.

Both displayed reciprocal conflict inequalities are imposed for every
edge, together with the root equalities and box bounds.

Call \((G,\sigma)\) balanced when

\[
             \bigoplus_{e\in C}\sigma_e=0
 \qquad(\hbox{every cycle }C).
\tag{6.2}
\]

### Theorem 6.1 (balanced reciprocal systems)

Put \(t_i=x_i^1\). On each connected component:

1. if \((G,\sigma)\) is balanced, the root-saturating relaxation is a
   line segment with two integral endpoints;
2. if it is unbalanced, every variable on that component is forced to
   \(1/2\), and there is no integral point;
3. the balanced system admits a TU and TDI description after a vertex
   gauge;
4. every inclusion-minimal fractional obstruction contains an
   unbalanced cycle; after unimodular path elimination its closing
   equation has determinant \(2\).

#### Proof

For \(\sigma_{ij}=0\), the two conflict inequalities become

\[
 (1-t_i)+t_j\le1,\qquad
 t_i+(1-t_j)\le1,
\]

and hence \(t_i=t_j\). For \(\sigma_{ij}=1\), they become

\[
 (1-t_i)+(1-t_j)\le1,\qquad t_i+t_j\le1,
\]

and hence \(t_i+t_j=1\).

Choose a base vertex. Along any path, every \(t_i\) is either the base
value \(u\) or \(1-u\), according to the path-label parity. If all cycle
parities vanish, this is consistent and \(0\le u\le1\); the two vertices
\(u=0,1\) are integral. Equivalently choose a gauge
\(\varepsilon_i\) with
\(\sigma_{ij}=\varepsilon_i\oplus\varepsilon_j\), and replace
\(t_i\) by \(1-t_i\) when \(\varepsilon_i=1\). Every edge then becomes
an equality of two variables. Node-incidence equalities and box bounds
are TU and have a TDI description.

If one cycle has odd label parity, propagating around it gives
\(u=1-u\), hence \(u=1/2\). Tree propagation forces every variable in
that connected component to \(1/2\). Eliminating the tree equations is
unimodular; the remaining equation is \(2u=1\), giving determinant
\(2\). \(\square\)

If roots may escape to outside options, let

\[
 e_i=1-x_i^0-x_i^1.
\]

Every unbalanced cycle \(C\) gives the exact integral escape cut

\[
       \boxed{\sum_{i\in C}e_i\ge1,}
 \qquad\hbox{equivalently}\qquad
 \sum_{i\in C}(x_i^0+x_i^1)\le |C|-1.
\tag{6.3}
\]

For a simple reciprocal constraint graph, the triangle in Theorem 4.1
is the smallest unbalanced cycle. Contradictory parallel relations can
produce a two-vertex obstruction in a multigraph; the physical
\(3\times3\) determinant-two target minor is nevertheless
dimension-minimal among \(0\)-\(1\) determinant witnesses.

### Theorem 6.2 (two legal endpoints force balance)

Overlay two complete owner-disjoint exact packet partitions. Every bare
owner-overlay component has two complementary shore choices, encoded by
one bit \(z_C\). Suppose all owner, port, monodromy, chronology, and collar
closure conditions are necessary-and-sufficient affine relations involving
exactly two component bits; suppose there are no hidden unary,
higher-arity, quantitative-resource, or coloured target-capacity
conditions; and suppose both complete endpoint factors satisfy every
declared relation. Then the signed constraint graph is balanced. After a
gauge, every constraint is an equality, and the legal hybrids are exactly
one shore bit per connected component of the port-merged graph.

#### Proof

In arbitrary local bit conventions, let \(g_C\) be the shore bit of the
first complete endpoint factor. A nonvacuous pairwise affine relation
preserved by both endpoints has the form

\[
                z_C\oplus z_D=\kappa_{CD}.
\tag{6.4}
\]

Since \(g\) satisfies it,

\[
                \kappa_{CD}=g_C\oplus g_D.
\tag{6.5}
\]

XORing (6.5) around a cycle telescopes to zero. Thus the graph is
balanced. The gauge \(u_C=z_C\oplus g_C\) turns every equation into
\(u_C=u_D\). Hence one bit remains for each connected component of the
port graph. \(\square\)

This theorem is sharp in scope.

* A connected port graph, even a path of maximum degree two, may merge
  every bare component and leave only the two original endpoint factors.
  Balancedness proves integrality, not discrepancy mobility.
* A higher-arity affine system is merely a binary linear code containing
  the two endpoint words. For example
  \[
                    z_1\oplus z_2\oplus z_3\oplus z_4=0
  \]
  is not a pairwise graphic equality system.
* The odd prism of Sections 4--5 is a multicolumn catalogue, not the
  overlay of two already legal complete endpoint factors. It therefore
  does not contradict Theorem 6.2.

## 7. Final-component run rank forced by the PBBS seam ledger

Return to a PBBS-provenance root

\[
 A\in\binom{[2m]}{m-H}.
\]

Its active coordinate alphabet is \(U=A^c\), of size \(M=m+H\). Assume the output
preserves exactly the \(M\) PBBS middle-owner occurrences belonging to
this root, although it may distribute and rethread them among one or
several safe-state components. Call a
maximal consecutive run **inherited** when all its successor edges are
the directed successors of the audited strongly geodesic PBBS
provenance.

### Theorem 7.1 (mesoscopic final-component run rank)

Let \(R_A\) be the total number of maximal inherited runs over root
\(A\). Then

\[
 R_A\ge\left\lceil{M\over H+1}\right\rceil.
\tag{7.1}
\]

Consequently, over all \(N\) roots,

\[
 R:=\sum_A R_A
 \ge N\left\lceil{M\over H+1}\right\rceil
 =(1+o(1)){W\over H}.
\tag{7.2}
\]

If the final output has \(C\le K N\) components and \(r_j\) is the
number of inherited runs in component \(j\), then

\[
 {R\over C}
 \ge {1\over K}\left\lceil{M\over H+1}\right\rceil
 =(1+o(1)){m\over KH}.
\tag{7.3}
\]

At least \(R/2\) inherited runs lie in components satisfying

\[
 r_j\ge {R\over2C}
 \ge(1+o(1)){m\over2KH}.
\tag{7.4}
\]

If every component has \(r_j\le b\), then

\[
 C\ge {R\over b},
\qquad
 2HC\ge(2+o(1)){W\over b}.
\tag{7.5}
\]

#### Proof

An inherited run of \(a\) owners is strongly geodesic, so their common
intersection has rank \(m-a+1\). Every one of those owners contains the
fixed root \(A\), whose rank is \(m-H\). Hence

\[
                  m-H\le m-a+1,
\]

and hence \(a\le H+1\). The \(M\) owner phases over root \(A\), summed
over all its coordinate subtours, therefore need at least
\(\lceil M/(H+1)\rceil\) maximal runs. This proves (7.1)--(7.2).

Now \(\sum_jr_j=R\), giving (7.3). Components with
\(r_j<R/(2C)\) contain in total fewer than \(R/2\) runs, proving (7.4).
If \(r_j\le b\), then \(R\le bC\); multiplying this numerical component
bound by \(2H\) gives (7.5). \(\square\)

The expression \(2HC\) in (7.5) is the conventional **upper allowance**
obtained by budgeting at most \(2H\) opening symbols per component. The
inequality is not a lower bound on unavoidable literal cost: a component
may need a shorter opening, and cyclic emission may need none. It is also
not an in-place packet-installation charge.
A directly certified whole-cycle packet has \(K_{\rm phys}=0\), however
many internal seams it absorbs.

The theorem constrains final components, not primitive switches. A
sequence of bounded-rank legal packets may build one mesoscopic-rank
component. In the component-closed master-column formulation of Section
2, that fused output is represented by one larger master column; in a
connector formulation, its component count must be derived after all
connectors are selected.

The rank scale is sharp at the abstract physical-word level. Partition a
cyclic permutation into \(\lceil M/(H+1)\rceil\) runs of length at most
\(H+1\). In the divisible case, the \(H+1\)-spaced \(2H\)-word family
already forms one safe Hamilton coordinate cycle. It is internally
injective for all upper traces and for lower traces below depth \(H\);
the depth-\(H\) lower trace requires the standard at-most-one active
phase per root. Thus seam density, parity, geometric zero monodromy, and
local safe-word geometry do not force positive \(K_{\rm phys}\). This
abstract example does not certify PBBS deck voltage.

What remains PBBS-specific is the actual near-overlap packing. Write

\[
 M=q_0(H+1)+r_0,\qquad 0\le r_0\le H.
\tag{7.6}
\]

If a fixed-top frame contains the extremal number \(q_0\) of
transition-disjoint intact \(H\)-transition blocks, their cyclic gaps are
\(g_1,\ldots,g_{q_0}\) with

\[
 \sum_jg_j=M-q_0H=q_0+r_0,
\qquad
 {1\over q_0}\sum_jg_j=1+{r_0\over q_0}=O(\log m).
\tag{7.7}
\]

Hence all but \(o(q_0)\) joins have \(g_j\le(\log m)^2<H\), and their
ordered suffix--prefix overlap is

\[
                         H-g_j=H-o(H).
\tag{7.8}
\]

No proved theorem controls the actual same-top PBBS near-overlap graph
strongly enough to construct or obstruct this mesoscopic cycle cover.

## 8. Integral repair of every local odd obstruction

For a target family \(\mathcal B\), define its additive exposure in root
\(U\) by

\[
 \omega_U(\mathcal B)
 =\sum_{T\in\mathcal B}
 {\#\{F\in\mathcal F_U:T\in\Gamma(F)\}\over|\mathcal F_U|}.
\tag{8.1}
\]

Every single target has exposure at most \(p_*\), and every complete
history has \(k\) distinct protected targets.

### Theorem 8.1 (ordered physical block repair)

Let \(\mathcal B_{\rm ext}\) be a frozen target-simple exterior. Suppose
roots \(U_1,\ldots,U_r\) satisfy

\[
 \omega_{U_i}(\mathcal B_{\rm ext})+(i-1)kp_*<1
 \qquad(1\le i\le r).
\tag{8.2}
\]

Then one can choose one direct literal full history in every root so
that the chosen histories avoid the exterior and are pairwise
target-disjoint. They have

\[
 C=r,\qquad K_{\rm phys}=0,
\qquad L_{\rm paths}\le r(L+2H).
\tag{8.3}
\]

#### Proof

Choose histories greedily in the displayed order. Before root \(U_i\),
the forbidden target set is the exterior together with the \(i-1\)
previous histories. Its exposure is at most the left side of (8.2),
because one history contributes at most \(kp_*\). The union bound on the
literal tail-order fibre leaves at least one order avoiding all forbidden
ports. Continue. Every chosen history is emitted directly, giving
(8.3). \(\square\)

With empty exterior, every root set satisfying

\[
                         (r-1)kp_*<1
\tag{8.4}
\]

repairs integrally. By (1.7), this includes every bounded, polynomial,
or

\[
 \exp\{o(\sqrt{m\log m})\}
\tag{8.5}
\]

union of odd-port prisms. In particular, the determinant-two gadgets in
Sections 4--5 are not closed obstructions after the complete root fibres
are restored.

There is an exact converse at a maximum matching. Remove any set of
matched histories, adjoin at least one unmatched root, and call the
resulting root set \(A\), \(|A|=a\). If
\(\mathcal B_{\rm ext}\) is the unchanged exterior, maximality forces

\[
 \boxed{
 \max_{U\in A}\omega_U(\mathcal B_{\rm ext})
 \ge1-(a-1)kp_*.
 }
\tag{8.6}
\]

Otherwise every ordering would satisfy (8.2) and augment the matching.
For \(a\le1/(2kp_*)\), some root has exterior exposure at least \(1/2\),
supplied by at least \(1/(2kp_*)\) distinct exterior histories.

Thus balanced signed propagation and local blossom repair terminate at a
genuine global wall. A first-moment exposure sum cannot exclude it:
one matched history may contribute total additive exposure as large as
\(k\) over all roots, while the desired leave is only
\(o(N/\sqrt m)\).

## 9. Precise proved and unproved boundary

### Proved

1. The exact whole-packet physical column/occurrence formulation,
   including all owner, coloured target, port, tag, voltage, component,
   seam, and implementation ledgers.
2. The exact CCTPF near-perfect matching identity
   \(\mathfrak H=\Delta+k\ell\), with \(C\le N\) and
   \(K_{\rm phys}=0\).
3. A complete literal zero-monodromy six-frame minor proving non-TU and
   non-TDI of the natural rooted physical matching system.
4. A full-history common-tag odd-port prism proving that all protected
   coloured rows retain the half-integral obstruction.
5. The complete balanced/unbalanced classification of reciprocal binary
   packet systems.
6. Automatic balancedness and a TU description for the reduced
   owner/port-closure bits under genuinely pairwise affine constraints
   between two already legal complete endpoint factors. Arbitrary
   coloured target-capacity rows are outside that TU claim.
7. The mesoscopic final-component run-rank lower bound (7.3)--(7.5), including the
   positive-fraction strengthening.
8. Integral physical repair below the exponential port radius with empty
   exterior, and the exact necessary exterior-exposure inequality at a
   maximum matching.

### Not proved

1. A CCTPF matching with leave \(o(N/\sqrt m)\).
2. Exclusion or construction of a globally interlocked exponential
   exterior port wall.
3. A bound \(o(W)\) on the largest port-merged component in the
   two-endpoint balanced regime.
4. A complete PBBS-authorized catalogue, or correlated composition, of
   whole cycles aggregating \(\Omega(m/H)\) inherited runs while satisfying
   every owner and all-depth target row.
5. That the fractional prisms extend to the complete global census, or
   that they obstruct the fixed global defect objective.
6. Coefficient one.

The final boundary is exact:

> Whole-packet columns remove the fictitious seam cost, and
> \(O(N_H)\) components are compatible with coefficient one. The natural
> unaugmented singleton-target incidence formulation is neither TU nor
> TDI, although the reduced two-endpoint pairwise-affine closure subsystem
> is balanced and integral. Any successful PBBS fusion must make its final
> components aggregate \(\Omega(m/H)\) inherited runs, whether directly or
> through correlated smaller switches. Any failed local CCTPF repair must
> cross the necessary global exterior-exposure wall. Neither remaining
> theorem is supplied by the present local odd-cycle analysis.
