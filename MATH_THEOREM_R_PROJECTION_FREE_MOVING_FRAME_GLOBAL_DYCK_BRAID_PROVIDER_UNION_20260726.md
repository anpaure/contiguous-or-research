# Projection-free moving-frame global braids: strip rigidity, the exact ledger cocycle, and a provider-union/floor-Gram theorem

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

This note separates three statements which must not be conflated.

1. A genuinely moving frame cannot move *inside* an isometric Johnson
   strand. Every isometric \(2h\)-cycle has the unique normal form

   \[
   X_i=K\mathbin{\dot\cup}
       \{z_i,z_{i+1},\ldots,z_{i+h-1}\},
       \qquad i\in\mathbb Z/(2h),                         \tag{0.1}
   \]

   for distinct \(z_0,\ldots,z_{2h-1}\). Its edge at phase \(i\)
   exchanges \(z_i\) with \(z_{i+h}\), and the matching

   \[
   M_C=\{\{z_i,z_{i+h}\}:0\le i<h\}                     \tag{0.2}
   \]

   is determined uniquely by the physical cycle. Thus a projection-free
   construction built from isometric \(C_{2h}\) strands must be a
   *cyclewise or packetwise frame mosaic*. It cannot be a stepwise change
   of frame along one such strand.

2. Such a mosaic admits an exact global-braid formulation. If
   \(L_{P,u}\) is the complete signed physical \(X/Y\)-ledger change of
   using local phase \(u\) in parent packet \(P\), and
   \(\pi_P:Z\to U_P\) is its root-dependent phase schedule, then, under
   the boundary-incidence and gluing hypotheses of Theorem 2.1, the common
   phase \(z\) is a legal exact factor if and only if

   \[
   \boxed{\sum_P L_{P,\pi_P(z)}=0\quad(z\in Z).}          \tag{0.3}
   \]

   Equality is in the free abelian group on literal typed resources, so
   (0.3) is stronger than equality of counts or profiles. It permits
   cancellation between different parents and retains every dependence.

3. For *any* finite catalogue \(\{F_z:z\in Z\}\) of complete legal
   exact factors satisfying (0.3), there is an exact all-depth
   provider-union theorem. For one typed layer \(\ell\), let
   \(n_{z,\ell}(T)\) be the literal target load, let \(G_\ell\) be its
   fixed total occurrence mass, put

   \[
   N_\ell=|\mathcal T_\ell|,\qquad
   k_\ell=\left\lfloor {G_\ell\over N_\ell}\right\rfloor,
   \qquad
   B_\ell=2k_\ell G_\ell-k_\ell(k_\ell+1)N_\ell,       \tag{0.4}
   \]

   and define the ordered collision Gram

   \[
   \Gamma_\ell(z)=
       \sum_{T\in\mathcal T_\ell}
          n_{z,\ell}(T)(n_{z,\ell}(T)-1).             \tag{0.5}
   \]

   Then, statewise and with no probabilistic independence,

   \[
   \boxed{
   \Gamma_\ell(z)-B_\ell
     =\sum_T(n_{z,\ell}(T)-k_\ell)
             (n_{z,\ell}(T)-k_\ell-1).}              \tag{0.6}
   \]

   Every summand is a nonnegative integer. If \(k_\ell\ge1\), every
   missing target contributes exactly \(k_\ell(k_\ell+1)\). Therefore

   \[
   \boxed{
   \exists z_*\in Z:\quad
   \sum_{\ell\in\mathcal L}H_\ell(F_{z_*})
   \le
   \sum_{\ell\in\mathcal L}
      {\overline\Gamma_\ell-B_\ell
       \over k_\ell(k_\ell+1)},}                    \tag{0.7}
   \]

   where \(H_\ell(F_z)=|\{T:n_{z,\ell}(T)=0\}|\) and the bar is the
   uniform average over the *complete factor states* \(z\). Thus the
   signs and all depths use one common integral state.

For a complete even-carrier catalogue with \(G_\ell=W\), at
central-binomial Gaussian depths \(q\le A\sqrt m\), the floors in (0.4)
are \(O_A(1)\). Consequently the exact estimate

\[
 \overline\Gamma_{q,\varepsilon}
 \le B_q+C_A{W\over m}                                \tag{0.8}
\]

uniformly for both signs and all \(1\le q\le A\sqrt m\) implies

\[
 \max\left\{
 \sum_{1\le q\le A\sqrt m,\ \varepsilon=\pm}
 H_{q,\varepsilon}(F_{z_*}),
 \sum_{1\le q\le A\sqrt m,\ \varepsilon=\pm}
 O_{q,\varepsilon}(F_{z_*})
 \right\}
 =O_A(W/\sqrt m)=o(W).                                \tag{0.9}
\]

This is a projection-free, fully dependent, all-depth missing-shadow
and balanced-quota-overload estimate; \(O\) is defined in (6.3a). It is
sufficient, not necessary: a covering state can have large quadratic
energy.

There are also two sharp negative conclusions.

* Independent diffuse parent hashes leave \(\Omega_A(W)\) Gaussian-depth
  holes in expectation. Ordinary decorrelation is therefore the wrong
  dependence: a successful braid needs a near-Latin or floor-balanced
  negative dependence between parents.
* In an orientation-cell selector construction, a branchwise fixed
  \(Y\)-palette determines the active matching directions. Hence a
  surjective translation of branch labels cannot change the active frame
  while remaining a cellwise exact substitution. Frame movement must be
  balanced by *cross-parent* \(Y\)-ledger cancellation in (0.3), or the
  local options may only regroup a fixed edge palette.

A concrete XOR-addressed packet mosaic, conditional on the certified
two-sided trace-injective \(C_{2r}\)-compiler assumed in Theorem 3.2,
supplies root-dependent frames, statewise macroscopic-cut crossing, and
exact within-parent rainbows. It therefore escapes every fixed
macroscopic coordinate cut. What is not
proved is a nonconstant solution of the global literal ledger equation
(0.3) whose provider sets satisfy the near-Latin condition below, nor,
alternatively, the strictly stronger floor-Gram certificate (0.8). Thus
coefficient one is not claimed. Corollary 3.3 also rules out a profile
invariant under every XOR frame, but not an arbitrary projection or an
owner-coupled invariant.

## 1. Isometric-strip rigidity

Let \(J(n,m)\) be the Johnson graph on the \(m\)-subsets of an \(n\)-set,
with

\[
 d_J(X,Y)=|X\setminus Y|=|Y\setminus X|.
\]

An oriented simple cycle

\[
 C=(X_0,X_1,\ldots,X_{2h-1})                         \tag{1.1}
\]

is *isometric* if

\[
 d_J(X_i,X_j)=\min\{|i-j|,2h-|i-j|\}                 \tag{1.2}
\]

for all \(i,j\), with indices modulo \(2h\). We assume \(h\ge2\).

### Theorem 1.1 (unique orientation-cube normal form)

Every isometric cycle (1.1) has a unique frozen set (K) and, after
choosing the displayed root and orientation, unique distinct coordinates

\[
 z_0,z_1,\ldots,z_{2h-1}
\]

such that (0.1) holds. The unordered matching (0.2) is independent of
the root and orientation and is the unique matching frame subordinate to
(C).

Necessarily

\[
 h\le\min\{m,n-m\},\qquad |K|=m-h.                  \tag{1.2a}
\]

Here uniqueness concerns the active \(h\)-pair matching. An ambient
perfect matching on coordinates frozen by the cycle may have many
extensions.

#### Proof

The two opposite vertices satisfy (d_J(X_0,X_h)=h). Put

\[
 K=X_0\cap X_h,\qquad
 A=X_0\setminus X_h,\qquad B=X_h\setminus X_0.       \tag{1.3}
\]

Then (|A|=|B|=h). The first half of the cycle is a geodesic from
(X_0) to (X_h), so its (i)-th edge removes a distinct
\(a_i\in A\) and inserts a distinct \(b_i\in B\). After indexing by
chronology,

\[
 X_i=K\mathbin{\dot\cup}
       \{a_i,a_{i+1},\ldots,a_{h-1}\}
       \mathbin{\dot\cup}
       \{b_0,b_1,\ldots,b_{i-1}\},
       \qquad0\le i\le h.                           \tag{1.4}
\]

The first edge of the second half removes some \(b'_0\in B\) and adds
some \(a'_0\in A\). Hence

\[
 X_{h+1}=K\mathbin{\dot\cup}(B\setminus\{b'_0\})
                  \mathbin{\dot\cup}\{a'_0\}.       \tag{1.5}
\]

Isometry for the shifted opposite pair (X_1,X_{h+1}) requires their
intersection to have size (m-h=|K|). Besides (K), their intersection
contains (a'_0) unless (a'_0=a_0), and contains (b_0) unless
(b'_0=b_0). Thus necessarily

\[
 a'_0=a_0,\qquad b'_0=b_0.                            \tag{1.6}
\]

Apply the same argument after cyclically shifting the root by (i).
The edge at phase (h+i) reverses precisely the exchange at phase (i):

\[
 X_{h+i+1}=X_{h+i}-b_i+a_i.                           \tag{1.7}
\]

Set

\[
 z_i=a_i,\qquad z_{h+i}=b_i\quad(0\le i<h).         \tag{1.8}
\]

Equations (1.4) and (1.7) give (0.1) for all phases. The physical edge
supports of (C) are exactly the (h) disjoint pairs
(\{a_i,b_i\}), each occurring twice. Therefore the matching (0.2) is
read directly from the cycle and is unique. The rooted orientation fixes
the chronological order in (1.8), proving the remaining uniqueness. Also

\[
 K=\bigcap_{i=0}^{2h-1}X_i,                           \tag{1.9}
\]

so the frozen core is independent of the initially chosen opposite pair.
The 2h moving coordinates are distinct and lie outside a core of size
m-h, which also proves (1.2a).
\(\square\)

### Corollary 1.2 (fresh endpoints in every geodesic window)

Every \(t\)-edge segment of \(C\), \(1\le t\le h\), uses \(t\) distinct
matching directions and \(2t\) distinct physical endpoints.

In particular, a complete isometric \(C_{2h}\) strand cannot change its
active matching frame. For a general longer nonisometric cycle, the local
conclusion is only Lemma 1.2a: every protected geodesic window uses a
set of fresh disjoint exchange pairs. It does not determine a unique
ambient matching extension, and the local pair set may slide after the
window.

### Lemma 1.2a (local geodesic freshness)

Let

\[
 X_0,X_1,\ldots,X_q                                   \tag{1.10}
\]

be any Johnson geodesic, and write its chronological exchanges as
\(a_i\mapsto b_i\), \(0\le i<q\). Then all \(2q\) coordinates
\(a_0,\ldots,a_{q-1},b_0,\ldots,b_{q-1}\) are distinct, and

\[
 \bigcap_{i=0}^qX_i=X_0\setminus\{a_0,\ldots,a_{q-1}\},\qquad
 \bigcup_{i=0}^qX_i=X_0\cup\{b_0,\ldots,b_{q-1}\}.   \tag{1.11}
\]

#### Proof

The endpoint distance is \(q\). Any repeated removal, repeated insertion,
reinsertion of a removed coordinate, or later removal of an inserted
coordinate would cancel at least one chronological exchange and make the
endpoint distance smaller than \(q\). Thus all exchange endpoints are
fresh and distinct. A removed coordinate never returns, while an inserted
coordinate never leaves, giving (1.11). \(\square\)

Thus even when the full cycle is not isometric, every protected geodesic
window spends fresh physical axes throughout the window.

### Corollary 1.3 (what projection-free can mean)

Let a factor be a union of isometric cycles. Any frame invariant proved
cyclewise is legitimate, but no one matching need be shared by two
different cycles. Therefore a fixed-frame Gaussian cut extends to such a
factor only if it comes from a statistic common to all cycle frames. A
catalogue whose frame-union graph is connected has no nonconstant
coordinate-occupancy invariant common to every frame: the simple exclusion
graph on (m)-subsets of a connected graph is connected.

This does not rule out a root-coupled invariant. It says that an
obstruction to a projection-free mosaic must use the root/frame coupling,
not a coordinate-occupancy invariant common to every frame.

## 2. The exact global ledger cocycle

Let \(F^0\) be one exact factor. Partition its replaceable material into
physical parent packets \(P\in\mathcal P\). A local option \(u\in U_P\)
is required to be a literal integral path/cycle replacement. Its boundary
data include the ordered incidences at every port and the induced
port-to-port pairing, not merely the unordered set of ports. Write

\[
 L_{P,u}\in\mathbb Z^{\mathcal R}                    \tag{2.1}
\]

for its signed change in the complete resource multiset. The coordinate
set \(\mathcal R\) contains every physical lower \(X\)-state, every
adjacent-union \(Y\)-colour, both complementary ports, and any chronology
or collar token that the outer compiler requires. It also contains a
separate basis token for every boundary incidence and port pairing used by
the gluing. Thus \(L_{P,u}=0\) is literal resource and boundary equality,
not a profile statement.

Let \(Z\) be a finite common phase space and choose arbitrary schedules

\[
 \pi_P:Z\longrightarrow U_P.                         \tag{2.2}
\]

At common phase \(z\), install option \(\pi_P(z)\) in every parent.

### Theorem 2.1 (necessary and sufficient exact braid equation)

Assume:

1. every local option is itself a valid path/cycle system;
2. simultaneous interiors are vertex-disjoint away from identified ports;
3. equality of the encoded boundary-incidence and port-pairing tokens
   makes the phasewise gluing compatible; and
4. exact factorhood has no additional unencoded global topology
   requirement (the number and lengths of resulting cycles may change).

Then the phase-\(z\) union is an exact replacement of \(F^0\) if and only
if (0.3) holds.

#### Proof

Because physical interiors are disjoint, the resource-and-boundary
multiset of the new union is the baseline multiset plus the sum of the
signed local changes. It equals the baseline multiset exactly if and only
if that sum is zero in the free abelian resource group. The encoded
incidence/pairing equality and hypothesis 3 make the local path systems
glue to a 2-regular global factor. Hypothesis 4 says there is no further
condition for exactness. This proves (0.3). No cancellation has been
projected or divided, so the assertion is integral and literal.
\(\square\)

### Remarks on scope

1. If every (L_{P,u}=0), all parent choices are independently legal.
   This is the familiar port-closed packet case.
2. A genuinely global braid may have \(L_{P,u}\ne0\) and cancel ledgers
   between parents. The cancellation must hold separately at every common
   phase \(z\); cancellation only after averaging over \(z\) is not enough.
3. If every \(\pi_P\) is a bijection of a common local phase set, summing
   (0.3) over \(z\) gives the necessary average condition

   \[
   \sum_P\sum_{u\in U_P}L_{P,u}=0.                   \tag{2.3}
   \]

   It is not sufficient for the pointwise equations (0.3).
4. Complement symmetry is imposed by fusing complementary parents and
   requiring the paired schedules to be transported by the complement
   involution. It is not selected independently after (0.3).

In the MSW/PBBS specialization, \(P\) is a physical exterior context,
the rows inside \(P\) are indexed by Dyck roots, and \(u\) specifies one
complete root-dependent interleaving of those rows. Equation (0.3) is then
exactly the common \(X/Y\)-ownership condition for the global Dyck braid.
No fixed exterior background or common coordinate alphabet is assumed in
Theorem 2.1.

## 3. A root-dependent interleaved phase model

The following construction describes the strongest currently certified
projection-free skeleton. It is stated first as an owner-cycle atlas; the
additional full \(Y\)-ledger issue is audited in Section 4.

Assume

\[
 \ell\ge4,\qquad 2m=2^\ell,\qquad
 K=\mathbb F_{2^{\ell-1}},\qquad
 G=K\times\mathbb F_2.                               \tag{3.1}
\]

Choose \(\alpha\in K\setminus\{0,1\}\) and define the fixed-point-free
involution

\[
 \tau(u,0)=(\alpha u,1),\qquad
 \tau(v,1)=(\alpha^{-1}v,0).                         \tag{3.2}
\]

For a middle owner \(X\in\binom Gm\), put

\[
 \sigma(X)=\bigoplus_{x\in X}x,\qquad
 a(X)=\sigma(X)+\tau(\sigma(X)),                     \tag{3.3}
\]

and let

\[
 M_a=\{\{x,x+a\}:x\in G\}/2.                        \tag{3.4}
\]

Define the selected orientation cell

\[
 \mathscr C(X)=\mathcal C_{M_{a(X)}}(X).             \tag{3.5}
\]

### Lemma 3.1 (owner-addressed cell partition)

The selected cells in (3.5) are equal or disjoint and partition the
middle layer. Complementation permutes the selected cells, sending
\(\mathscr C(X)\) bijectively to \(\mathscr C(G\setminus X)\).

#### Proof

Flipping one split \(M_a\)-edge changes \(\sigma(X)\) by \(a\). If
\(s=\sigma(X)\) and \(a=s+\tau(s)\), the only hashes reached inside the
cell are \(s\) and \(s+a=\tau(s)\). Both choose the same label \(a\).
The full/empty/split status is unchanged. Hence every member of a selected
cell selects that same cell, proving equality or disjointness and
exhaustion.

For \(\ell\ge4\), the XOR of all coordinates of \(G\) is zero. Therefore
\(\sigma(G\setminus X)=\sigma(X)\), so complementing \(X\) preserves the
selected matching. It swaps every full matching pair with an empty pair
and sends every split orientation to its complement. Consequently

\[
 \mathscr C(G\setminus X)
 =\{G\setminus Y:Y\in\mathscr C(X)\}.                \tag{3.5b}
\]

The two cells are equal only when every matching pair is split.
\(\square\)

Discarding cells of dimension below \(m/3\) loses
\(e^{-\Omega(m)}\binom{2m}m\) owners. In each retained
\(\mathscr C\cong Q_D\), put

\[
 s=\left\lceil4r\log_2(2em)\right\rceil              \tag{3.5a}
\]

and choose \(s\) selector axes. Since \(D\ge m/3\), the assumption
\(r\log m=o(m)\) ensures \(s+r<D\) for all sufficiently large \(m\).
Identify the selector branches with

\[
 B=\mathbb F_2^s.                                    \tag{3.6}
\]

Take \(r=2^\rho\ge2\). This divisibility is necessary for a
\(C_{2r}\)-factor of \(Q_r\), because \(2r\mid2^r\), and it is satisfied
by the certified compiler dimensions.

Fix one certified literal \(C_{2r}\)-factor which is two-sided
trace-injective through every \(q\le H\). Define
\(\Lambda_{\mathscr C}\) as the formal labelled catalogue of its
conjugates indexed by

\[
 (R,\eta,\pi)\in
 \binom{[d]}r\times\mathbb F_2^r\times S_r,\qquad d=D-s. \tag{3.6a}
\]

The label chooses the active \(r\)-set \(R\), the parallel
\(Q_r\)-packet subdivision on those axes, and the
\((\eta,\pi)\)-conjugate certified factor in every packet. In particular,
every active \(r\)-set occurs with the same multiplicity \(2^rr!\), so
the uniform label law has an exactly uniform active-set marginal.
Coincident physical conjugates, if any, remain distinct formal labels;
this preserves the exact multiplicity statement. Let

\[
 \ell_{\mathscr C}:B\longrightarrow
       \Lambda_{\mathscr C}                          \tag{3.7}
\]

be a balanced array. For a common phase space \(Z\), choose arbitrary
root-dependent shifts

\[
 h_{\mathscr C}:Z\longrightarrow B                  \tag{3.8}
\]

and give branch \(b\) at phase \(z\) the label

\[
 \boxed{
 \ell_{\mathscr C,z}(b)=
 \ell_{\mathscr C}(b+h_{\mathscr C}(z)).}            \tag{3.9}
\]

For this explicit label catalogue,

\[
 M:=|\Lambda_{\mathscr C}|
 =\binom dr2^rr!\le(2m)^r\le(2em)^r.                \tag{3.9a}
\]

Assigning its labels as evenly as possible among the \(2^s\) branches
gives total-variation discrepancy at most \(M/2^{s+1}\). Enforcing the
complement pairings changes this by at most a factor two, so we may use

\[
 \epsilon_m\le {M\over2^s}
 \le (2em)^{-3r}.                                    \tag{3.9b}
\]

Thus \(\epsilon_m=o(m^{-C})\) for every fixed \(C>0\) in the intended
growing-\(r\) regime.

Every phase of (3.9) is an integral owner-cycle factor: it only permutes
complete labels among owner-disjoint selector branches. Complementary
cells use the same shift and transported labels. If every label is
individually port-closed, (3.9) is already a complete exact packet
substitution. In general, its exact-factor legality is precisely equation
(0.3).

The useful maximally correlated specialization is

\[
 Z=B,\qquad
 h_{\mathscr C}(z)=\pi_{\mathscr C}(z),\qquad
 \pi_{\mathscr C}\in\operatorname{Sym}(B),           \tag{3.10}
\]

where the permutations may be chosen separately for different parents.
Every local shift is then uniform over the array inputs and hence
\(\epsilon_m\)-close to uniform over the catalogue, while all cross-parent
dependencies are designed by the relative permutations
\(\pi_{\mathscr D}\pi_{\mathscr C}^{-1}\). This is not an independent
cube signing.

Complementary parents are one fused parent for this purpose: their
permutations and transported labels must agree under complementation.

### Theorem 3.2 (phasewise projection escape)

Assume

\[
 r=2^\rho\longrightarrow\infty,\qquad
 r\log m=o(m),\qquad H<r,\qquad H=o(m^{2/3}),         \tag{3.11}
\]

and use the explicit uniform-active-set catalogue above, every member of
which is two-sided trace-injective through \(H\). Take the balanced arrays
with selector imbalance \(o(m^{-C})\) for every fixed \(C>0\). For every
fixed \(\delta>0\), every common phase
\(z\), every coordinate set \(A\subseteq G\) with

\[
 2\delta m\le |A|\le2(1-\delta)m,                    \tag{3.12}
\]

and every \(1\le q\le H\), the retained based depth-\(q\) windows which
contain an exchange crossing \(A\) have cardinality at least

\[
 \bigl(\delta(1-\delta)-o_\delta(1)\bigr)W,          \tag{3.13}
\]

where \(W=\binom{2m}m\). Every retained selected cell is also a literal
rainbow separately at each protected depth and sign.

#### Proof

The frame labels \(a\) in (3.2) form the one-factorization of the complete
bipartite graph between the two (K)-shores. If (b_a(A)) is the number
of (M_a)-edges crossing (A), and (a_i) is the number of points of
(A) on shore (i), then

\[
 \sum_a b_a(A)=a_0(m-a_1)+a_1(m-a_0)
 \ge2\delta(1-\delta)m^2.                            \tag{3.14}
\]

The exact conditional split-edge census in the selected hash cells turns
(3.14) into

\[
 \sum_P |P|t_A(P)
 \ge(\delta(1-\delta)-o_\delta(1))rW,                \tag{3.15}
\]

where \(t_A(P)\) is the number of active packet axes crossing \(A\).
The census used here is the uniform exact estimate

\[
 \#\{X\in\Omega_a:|X\cap e|=1\}
 ={W\over2m-1}+O(m2^m)                               \tag{3.14a}
\]

for every frame label \(a\) and every \(e\in M_a\), where
\(\Omega_a\) is the two-hash owner class selecting \(M_a\). Fourier
inversion on the quotient by \(\langle a\rangle\) gives the main term;
every nontrivial character contributes a coefficient of
\((1-z^2)^m\) with two linear factors deleted, hence \(O(2^m)\).
Summing fewer than \(2m\) characters gives the displayed uniform error.
Under the uniform formal-label law, after the selector axes are removed,
each remaining split axis has exact active-set marginal
\(r/(D-s)\ge r/m\). The empirical balanced array is
\(\epsilon_m\)-close in total variation, so a single-axis marginal is
\(r/(D-s)+O(\epsilon_m)\), and the expectation of the bounded statistic
\(0\le t_A(P)\le r\) changes by at most \(r\epsilon_m\). Summing (3.14a)
over the crossing edges in (3.14) yields (3.15); the aggregate array error
is \(O(r\epsilon_mW)=o(rW)\), and all Fourier, selector, and discarded-cell
errors are \(o_\delta(rW)\).

Translating the balanced array in (3.9) permutes equal-size branches and
preserves the same active-axis histogram, so (3.15) holds at every phase.

In a doubled-permutation \(C_{2r}\)-factor, the incidence count between
based depth-\(q\) windows and the \(t_A(P)\) crossing axes is

\[
 |P|{q\,t_A(P)\over r}.                               \tag{3.16}
\]

One window contributes at most \(q\) such incidences. It follows that at
least \(|P|t_A(P)/r\) of its based windows cross \(A\). Sum over packets
and use (3.15) to obtain (3.13).

Inside a packet, certified two-sided trace injectivity separates all
targets. Parallel packets differ on an inactive spectator axis, and
selector branches differ on a selector spectator. Those coordinates
survive every protected intersection or union, proving the cell rainbow.
\(\square\)

The conclusion is occurrence-level macroscopic-cut escape in every
realized state, not merely connectedness of a catalogue union. It does not
exclude arbitrary projections or owner-coupled invariants.

### Corollary 3.3 (no common target-only exchange profile)

The union of the translation matchings (M_a),
\(a\in K\times\{1\}\), is exactly the complete bipartite graph between
the two (K)-shores. Consequently, if a function on the nontrivial
(k)-subsets of (G) is invariant under every occupancy exchange along
every one of these matching edges, then it is constant.

#### Proof

Every cross-shore pair has a unique difference in
\(K\times\{1\}\), proving the first assertion. The edge transpositions of
a connected graph generate the full symmetric group on its vertices.
Equivalently, its (k)-token simple-exclusion graph is connected: along a
transposition word, swaps whose endpoints have equal occupancy are idle,
and every nonidle swap is one allowed exclusion move. Thus an invariant
of all allowed moves is constant. \(\square\)

This only kills a profile common to *all* XOR frames. The owner-addressed
selector does not expose every frame at every owner, so the corollary does
not prove target coverage and does not exclude a root-coupled invariant.

## 4. The branchwise \(Y\)-palette obstruction

Projection escape does not prove exact \(Y\)-ownership. There is a simple
detector showing why a nonconstant branch translation is not automatically
a legal exact packet trade.

Fix one orientation cell with split coordinate pairs

\[
 e_i=\{x_i,y_i\},\qquad 1\le i\le D.                 \tag{4.1}
\]

Fix a selector branch (b), and let a label choose a common active set
\(R\subseteq[D]\setminus S\), \(|R|=r\), on all parallel \(Q_r\)-packets
of that branch. Let \(\mathcal Y_b(R)\) be the multiset of adjacent
upper unions used by its doubled-permutation factor.

For a split axis \(i\notin S\), define the physical detector

\[
 D_i(\mathcal Y)=
   \sum_{U\in\mathcal Y}{\bf1}_{\{e_i\subseteq U\}}. \tag{4.2}
\]

### Theorem 4.1 (active-frame recovery from the \(Y\)-palette)

For a branch with (d=D-|S|) nonselector split axes,

\[
 D_i(\mathcal Y_b(R))=
 \begin{cases}
  2^d/r,&i\in R,\\
  0,&i\notin R.
 \end{cases}                                         \tag{4.3}
\]

In particular, the literal \(Y\)-palette determines \(R\).

#### Proof

An orientation-cube Johnson edge in direction (i) has an upper union
containing both endpoints of (e_i), and exactly one endpoint of every
other split pair. Hence (4.2) counts precisely the factor edges in
direction (i).

There are (2^{d-r}) parallel (Q_r)-packets. A doubled-permutation
factor on one (Q_r) has (2^r/(2r)) cycles; every cycle uses every one
of its (r) directions twice. Thus it has (2^r/r) edges in each active
direction. Multiplication by (2^{d-r}) gives (2^d/r). Inactive
directions are never used. \(\square\)

Different selector branches have disjoint upper palettes: every upper
union retains the selected endpoint of every selector pair and therefore
records its branch tag.

### Corollary 4.2 (cellwise translation rigidity)

Let (R(u)) be the active set attached to array label
\(\ell_{\mathscr C}(u)\). Suppose the complete \(Y\)-palette

\[
 \biguplus_{b\in B}\mathcal Y_b(R(b+a))              \tag{4.4}
\]

is independent of the shift \(a\) in a set \(A_0\subseteq B\). Then

\[
 R(b+a)=R(b+a')\qquad
 \quad(b\in B,\ a,a'\in A_0).                        \tag{4.5}
\]

Consequently (R) is constant on the cosets of

\[
 H_0=\langle a-a':a,a'\in A_0\rangle.                \tag{4.6}
\]

If \(A_0=B\), then \(R\) is constant on all branches.

#### Proof

Restrict equality of (4.4) to the disjoint physical selector tag (b).
The palette \(\mathcal Y_b(R(b+a))\) is independent of \(a\). The
detectors (4.2)--(4.3) then give (4.5). Translation by the generators in
(4.6) proves coset constancy. \(\square\)

Thus the simple scheme “permute different active frames among selector
branches, independently inside every parent” cannot be both surjective and
cellwise \(Y\)-closed. The exact escapes are:

* keep the active frame fixed and vary only cycle regroupings with the
  same edge palette;
* use mixed subpacket mosaics with identical complete direction ledgers;
  or
* allow nonzero parent ledgers which cancel globally through (0.3).

The third is the intended projection-free global-braid route.

## 5. Literal provider sets and the whole-union identity

Return now to an arbitrary finite catalogue of complete legal states

\[
 \mathcal F=\{F_z:z\in Z\}                            \tag{5.1}
\]

From this section onward \(G_\ell\), or \(G\) when one layer is fixed,
denotes an occurrence mass. It is unrelated to the coordinate group
\(G=K\times\mathbb F_2\) used only in Section 3.

satisfying (0.3). Let \(\mathcal L\) be any finite set of typed depths
and signs. At layer \(\ell\), every state uses the same controlled owner
set \(\mathcal O_\ell\) of size \(G_\ell\), and each controlled owner
emits one literal target in \(\mathcal T_\ell\).

For an owner \(X\) and target \(T\), define its phase-provider set

\[
 S_{X,\ell}(T)=\{z\in Z:T^{F_z}_\ell(X)=T\}.          \tag{5.2}
\]

If the owner set is partitioned into parent rainbows \(P\), define

\[
 S_{P,\ell}(T)=\bigcup_{X\in P}S_{X,\ell}(T).         \tag{5.3}
\]

The rainbow condition makes the union in (5.3) disjoint at each fixed
phase, but no independence between parents is assumed.

### Theorem 5.1 (exact provider-union averaging)

Statewise,

\[
 \boxed{
 H_\ell(F_z)=N_\ell-G_\ell+
       \sum_{T\in\mathcal T_\ell}(n_{z,\ell}(T)-1)_+.} \tag{5.3a}
\]

For every layer,

\[
 \boxed{
 {1\over|Z|}\sum_{z\in Z}H_\ell(F_z)
 =\sum_{T\in\mathcal T_\ell}
    \left(1-{|\bigcup_XS_{X,\ell}(T)|\over|Z|}\right).} \tag{5.4}
\]

Consequently

\[
 \boxed{
 \exists z_*:\quad
 \sum_{\ell\in\mathcal L}H_\ell(F_{z_*})
 \le {1\over|Z|}\sum_{\ell,T}
       |Z\setminus\bigcup_XS_{X,\ell}(T)|.}          \tag{5.5}
\]

The same formulas hold with the parent sets (5.3) in place of the owner
sets.

#### Proof

The \(G_\ell\) occurrences split into one first occurrence for each of
the \(N_\ell-H_\ell\) hit targets and the repeat excess. This gives
(5.3a).

For a fixed \(T,z\), the target is missing exactly when \(z\) belongs to
none of the provider sets \(S_{X,\ell}(T)\). Sum its indicator first over
\(z\), then over \(T\), to obtain (5.4). Sum (5.4) over all typed layers.
At least one common phase is no larger than the average, proving (5.5).
\(\square\)

Thus the exact projection-free near-Latin condition is

\[
 \boxed{
 \sum_{\ell,T}|Z\setminus\bigcup_XS_{X,\ell}(T)|
 =o(W|Z|).}                                          \tag{5.6}
\]

It retains the literal physical targets and the full common-state
dependence.

### Explicit branch-array form

For the model (3.9), let \(A_{\mathscr C,b}(v)\) be the labels which make
branch (b) emit the typed literal target (v). Then

\[
 \boxed{
 S_{\mathscr C}(v)=
 \bigcup_{b\in B}
 \{z:\ell_{\mathscr C}(b+h_{\mathscr C}(z))
                   \in A_{\mathscr C,b}(v)\}.}       \tag{5.7}
\]

In the additive specialization (Z=B) and
\(h_{\mathscr C}(z)=z+\gamma_{\mathscr C}\),

\[
 \boxed{
 S_{\mathscr C}(v)=
 \bigcup_{b\in B}
 \left(\ell_{\mathscr C}^{-1}
              (A_{\mathscr C,b}(v))+b+\gamma_{\mathscr C}\right).} \tag{5.8}
\]

Every membership in (5.7)--(5.8) certifies an actual consecutive window
in an integral cycle; no formal target profile occurs.

### Quotient near-Latin certificate

For every typed target (v), suppose a quotient

\[
 \rho_v:Z\twoheadrightarrow Q_v                      \tag{5.9}
\]

has equal fibres and there are residue sets
\(R_{P,v}\subseteq Q_v\) satisfying

\[
 \rho_v^{-1}(R_{P,v})\subseteq S_P(v).               \tag{5.10}
\]

Then

\[
 |Z\setminus\bigcup_PS_P(v)|
 \le {|Z|\over|Q_v|}
       |Q_v\setminus\bigcup_PR_{P,v}|.               \tag{5.11}
\]

Hence

\[
 \sum_v {|Q_v\setminus\bigcup_PR_{P,v}|\over|Q_v|}=o(W) \tag{5.12}
\]

is a sufficient, exact, projection-free provider theorem.

### Forced repeat baseline

Assume now that every parent is a rainbow. Put

\[
 I_T=\sum_P|S_{P,\ell}(T)|,\qquad
 U_T=|\bigcup_PS_{P,\ell}(T)|,\qquad
 E_T=I_T-U_T.                                        \tag{5.13}
\]

Each state emits \(G_\ell\) controlled occurrences, so

\[
 \sum_T I_T=|Z|G_\ell.                               \tag{5.14}
\]

Substitution in (5.4) gives the exact identity

\[
 \boxed{
 {1\over|Z|}\sum_zH_\ell(F_z)
 ={1\over|Z|}\sum_TE_T-(G_\ell-N_\ell).}            \tag{5.15}
\]

Thus when \(G_\ell\ge N_\ell\), provider overlap is not supposed to be
zero. Rearranging (5.15) gives the exact formula

\[
 \boxed{
 \sum_TE_T
 =|Z|(G_\ell-N_\ell)+
   |Z|\left({1\over|Z|}\sum_zH_\ell(F_z)\right).}     \tag{5.16}
\]

Thus the overlap equals the forced surplus plus the hole term. It equals
the forced surplus up to \(o(W|Z|)\) precisely under the desired
average-hole hypothesis. Ordinary independent coverage produces too much
overlap and too many holes simultaneously.

## 6. The integral floor-Gram theorem

For a state \(z\), abbreviate

\[
 n_T=n_{z,\ell}(T),\qquad
 \sum_Tn_T=G_\ell.                                   \tag{6.1}
\]

Let \(k_\ell,B_\ell,\Gamma_\ell\) be as in (0.4)--(0.5).

### Theorem 6.1 (exact floor-defect identity)

For every state and layer, (0.6) holds. In particular,

\[
 \Gamma_\ell(z)\ge B_\ell.                           \tag{6.2}
\]

If \(k_\ell\ge1\), then

\[
 \boxed{
H_\ell(F_z)
 \le{\Gamma_\ell(z)-B_\ell\over
          k_\ell(k_\ell+1)}.}                       \tag{6.3}
\]

Moreover, let the balanced-quota overload be

\[
 O_\ell(F_z)=
 \min_{\substack{b_T\in\{k_\ell,k_\ell+1\}\\
                 \sum_Tb_T=G_\ell}}
       \sum_T(n_T-b_T)_+.                            \tag{6.3a}
\]

Then

\[
 \boxed{
 O_\ell(F_z)\le{\Gamma_\ell(z)-B_\ell\over2}.}      \tag{6.3b}
\]

Equality in (6.3) holds exactly when every positive target load belongs
to \(\{k_\ell,k_\ell+1\}\).

#### Proof

Using \(\sum_Tn_T=G_\ell\),

\[
\begin{aligned}
 \Gamma_\ell(z)-B_\ell
 &=\sum_T\{n_T(n_T-1)-2k_\ell n_T
                         +k_\ell(k_\ell+1)\}\\
 &=\sum_T(n_T-k_\ell)(n_T-k_\ell-1).
\end{aligned}                                         \tag{6.4}
\]

For integral \(n_T\), a product of two consecutive integers is
nonnegative. It vanishes exactly when
\(n_T\in\{k_\ell,k_\ell+1\}\). A hole has \(n_T=0\) and contributes
exactly \(k_\ell(k_\ell+1)\). Summing the hole contributions proves
(6.3), including its equality characterization. If \(n_T\ge k_\ell+2\)
and \(d=n_T-k_\ell\), then

\[
 d(d-1)\ge2(d-1)=2(n_T-k_\ell-1).                   \tag{6.4a}
\]

To prove the balanced-overload assertion, put

\[
 L=\sum_T(k_\ell-n_T)_+,\qquad
 U=\sum_T(n_T-k_\ell-1)_+,
 \qquad
 t=|\{T:n_T\ge k_\ell+1\}|.                          \tag{6.4b}
\]

Write \(G_\ell=k_\ell N_\ell+r_\ell\). Relative to the constant quota
\(k_\ell\), the positive overload is both

\[
 \sum_T(n_T-k_\ell)_+=r_\ell+L=t+U.                 \tag{6.4c}
\]

Raising exactly \(r_\ell\) quotas from \(k_\ell\) to \(k_\ell+1\)
optimally lowers this quantity by \(\min\{r_\ell,t\}\). Hence

\[
 O_\ell(F_z)
 =r_\ell+L-\min\{r_\ell,t\}
 =\max\{L,U\}.                                       \tag{6.4d}
\]

For a lower deviation \(n_T=k_\ell-d\), \(d\ge1\), its floor energy is
\(d(d+1)\ge2d\); thus the total energy is at least \(2L\). Equation
(6.4a) shows it is also at least \(2U\). Therefore it is at least
\(2\max\{L,U\}=2O_\ell(F_z)\), proving (6.3b). \(\square\)

The exact floor baseline may also be written as follows. If

\[
 G_\ell=k_\ell N_\ell+r_\ell,\qquad0\le r_\ell<N_\ell, \tag{6.5}
\]

then

\[
 B_\ell=(N_\ell-r_\ell)k_\ell(k_\ell-1)
         +r_\ell k_\ell(k_\ell+1).                  \tag{6.6}
\]

It is the ordered collision count of the unique floor-balanced load
multiset: \(N_\ell-r_\ell\) targets have load \(k_\ell\), and the rest
have load \(k_\ell+1\).

### Provider-intersection form

Let the bar denote uniform average over (Z). Then

\[
 \boxed{
 \overline\Gamma_\ell
 ={1\over|Z|}
   \sum_{X\ne Y}\sum_T
      |S_{X,\ell}(T)\cap S_{Y,\ell}(T)|.}            \tag{6.7}
\]

If the parents are rainbows, this becomes

\[
 \boxed{
 \overline\Gamma_\ell
 ={1\over|Z|}
   \sum_{P\ne Q}\sum_T
      |S_{P,\ell}(T)\cap S_{Q,\ell}(T)|.}            \tag{6.8}
\]

Indeed, (n_T(n_T-1)) counts ordered pairs of distinct providers of
(T). Equations (6.7)--(6.8) follow by interchanging the order of
summation.

### Theorem 6.2 (one common all-depth state)

For any finite typed layer set \(\mathcal L\) with \(k_\ell\ge1\), (0.7)
holds.

#### Proof

Apply (6.3) statewise, sum over all typed layers, and average over the
complete legal state catalogue (Z). One state is no larger than the
average. \(\square\)

No root choice has been made independently in this proof. Every averaged
object is already one complete legal exact factor satisfying (0.3).
The missing-target denominator in (6.3) requires \(k_\ell\ge1\); all
Gaussian applications below start at depth \(q=1\). A layer with
\(k_\ell=0\) must be handled directly from the provider union (5.4), not
from the floor-hole denominator.

### Finite inclusion-exclusion alternative

The floor-Gram criterion is sufficient but not necessary. If target
congestion is uniformly at most \(\Delta\), define

\[
 I_j(T)=\sum_{X_1<\cdots<X_j}
       |\bigcap_{a=1}^jS_{X_a,\ell}(T)|,
 \qquad I_0(T)=|Z|.                                  \tag{6.9}
\]

Then exactly

\[
 |Z\setminus\bigcup_XS_{X,\ell}(T)|
 =\sum_{j=0}^{\Delta}(-1)^jI_j(T).                   \tag{6.10}
\]

Without a congestion cap, every even truncation is still an upper bound.
This gives a bounded-order route when a moving-frame construction has
uniformly bounded physical target congestion.

Indeed, at a phase with \(n\ge1\) providers, the order-\(2s\) truncated
indicator equals

\[
 \sum_{j=0}^{2s}(-1)^j\binom nj=\binom{n-1}{2s}\ge0, \tag{6.10a}
\]

whereas the true missing indicator is zero; for \(n=0\), both are one.

Pair data alone do not determine holes once congestion three is possible.
For example, the two distributions

\[
 (5,1,7,3)/16,\qquad(3,7,1,5)/16                   \tag{6.11}
\]

on loads (0,1,2,3) both have mean (3/2) and factorial second moment
(2), but their hole probabilities are respectively (5/16) and
(3/16). This is why (6.3) must be called a sufficient certificate,
not the uniquely necessary provider gate.

## 7. Gaussian-depth constants

Specialize first to the even packet carrier. Put

\[
 W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q}.                \tag{7.1}
\]

The exact ratio is

\[
 {W\over N_q}=\prod_{i=1}^q{m+i\over m-i+1}.         \tag{7.2}
\]

For fixed \(A\) and \(q\le A\sqrt m\), Taylor expansion term by term
gives, uniformly,

\[
 \log{W\over N_q}={q^2\over m}+O_A(m^{-1/2}),        \tag{7.3}
\]

Indeed,

\[
\log{W\over N_q}
=\sum_{i=1}^q\left[
\log\left(1+{i\over m}\right)
-\log\left(1-{i-1\over m}\right)\right].
\]

The linear terms sum to
\(\sum_{i=1}^q(2i-1)/m=q^2/m\), while the total quadratic-and-higher
remainder is \(O(\sum_{i\le q}i^2/m^2)=O_A(m^{-1/2})\).

Consequently,

\[
 1\le {W\over N_q}\le e^{A^2+o_A(1)},\qquad
 k_q\le K_A:=\lceil e^{A^2+1}\rceil                 \tag{7.4}
\]

for all sufficiently large \(m\).

On the odd carrier \(W=\binom{2m+1}m\), the two signs must remain
separate:

\[
 N_{q,-}=\binom{2m+1}{m-q},\qquad
 N_{q,+}=\binom{2m+1}{m+q}.                          \tag{7.4a}
\]

Uniformly for \(q\le A\sqrt m\),

\[
\begin{aligned}
 \log{W\over N_{q,-}}
   &={q(q+1)\over m}+O_A(m^{-1/2}),\\
 \log{W\over N_{q,+}}
   &={q(q-1)\over m}+O_A(m^{-1/2}).
\end{aligned}                                        \tag{7.4b}
\]

Both equal \(q^2/m+O_A(m^{-1/2})\), but their exact floors and baselines
are sign-specific. In particular \(N_{1,+}=W\). For a controlled core
\(G=W-R<W\), this upper layer has \(k_{1,+}=0\), so it must be handled by
the direct provider union or by its exact completion, not by (6.3).

Return now to the even carrier (7.1). Let the controlled core have

\[
 G=W-R,\qquad R=e^{-\Omega(m)}W.                    \tag{7.5}
\]

Then (7.3)--(7.4) remain valid with \(G/N_q\), and \(k_q\ge1\) for every
\(q\ge1\). If this core is embedded in a complete exact state by a
separately certified completion which leaves the core unchanged, the
completion only adds target occurrences and cannot increase the missing
count. The existence of such a common exact completion is not automatic;
for the concrete XOR skeleton it is part of the global ledger/closure gate
in Section 9.

If \(R<N_q\) and the completion adds \(R\) occurrences in a typed layer,
its full-factor balanced-quota overload is at most the controlled-core
balanced-quota overload plus \(R\). Indeed, an optimal balanced core quota
vector can be extended coordinatewise to a balanced full quota vector:
if the floor is unchanged, raise \(R\) low quotas; if the floor rises by
one, first raise every old low quota and then the required new high quotas.
If \(n'=n+a\) and \(b'=b+d\) are the completed load and the extended quota,
then \(a,d\ge0\), \(\sum a=\sum d=R\), and

\[
 \sum_T(n'_T-b'_T)_+
 \le\sum_T(n_T-b_T)_++\sum_T(a_T-d_T)_+
 \le O^{\rm core}+R.                                 \tag{7.5a}
\]

Therefore an exceptional owner mass \(R\) costs at most \(2HR\) through
\(H\) depths and two signs. In particular, the exponentially small
\(R\) in (7.5) is harmless once exact common completion has been proved.

### Corollary 7.1 (uniform \(O(W/m)\) floor excess on the even carrier)

Let \(H\le A\sqrt m\). If, for every \(1\le q\le H\) and both signs,

\[
 \overline\Gamma_{q,\varepsilon}-B_q
 \le C_A{W\over m},                                  \tag{7.6}
\]

where \(B_q\) is formed with the controlled mass \(G\), then one common
phase satisfies

\[
 \max\left\{
 \sum_{q\le H,\varepsilon}H^{\rm core}_{q,\varepsilon},
 \sum_{q\le H,\varepsilon}O^{\rm core}_{q,\varepsilon}
 \right\}
 \le {H C_AW\over m}
 =O_A(W/\sqrt m).                                    \tag{7.7}
\]

#### Proof

The average total floor energy over the \(2H\) typed layers is at most
\(2HC_AW/m\). Choose one common phase no larger than this average.
Equations (6.3) and (6.3b), using \(k_q(k_q+1)\ge2\), bound each of the
two sums in (7.7) by half of that total energy. \(\square\)

If the common exact completion from the paragraph before Corollary 7.1
has been proved, the same phase satisfies

\[
\begin{aligned}
 \sum_{q\le H,\varepsilon}H^{\rm full}_{q,\varepsilon}
 &\le {HC_AW\over m},\\
 \sum_{q\le H,\varepsilon}O^{\rm full}_{q,\varepsilon}
 &\le {HC_AW\over m}+2HR.
\end{aligned}                                        \tag{7.7a}
\]

### Corollary 7.2 (exact odd-wreath lower-shadow implication)

Let \(W=\binom{2m+1}m\), let
\[
 N_q=\binom{2m+1}{m-q},\qquad
 k_q=\left\lfloor{W\over N_q}\right\rfloor,\qquad
 B_q=2k_qW-k_q(k_q+1)N_q,
\]
and let \(F_z\), \(z\in Z\), be a catalogue of complete exact middle
wreath factors. Fix \(A>0\) and \(H=\lfloor A\sqrt m\rfloor\). If

\[
 \overline\Gamma_q-B_q\le C_A{W\over m}
 \qquad(1\le q\le H),                                \tag{7.7b}
\]

then one common exact factor \(F_{z_*}\) satisfies

\[
 \max\left\{\sum_{q=1}^HH_q(F_{z_*}),
             \sum_{q=1}^HO_q(F_{z_*})\right\}
 \le {HC_AW\over2m}
 =O_A(W/\sqrt m)=o(W).                               \tag{7.7c}
\]

#### Proof

The average total floor energy through the \(H\) lower layers is at most
\(HC_AW/m\). Choose one state no larger than this average and apply
(6.3), whose denominator is at least two, and (6.3b). \(\square\)

For every fixed \(A\), (7.7c) is a quantitative sufficient input to the
frozen unlabelled MWB gate. It does not construct the catalogue satisfying
(7.7b), and it does not imply labelled common-owner synchronization.

More generally, for any typed layer collection with common occurrence
mass \(G\) and with every \(k_{q,\varepsilon}\ge1\), write

\[
 d_{q,\varepsilon}={\overline\Gamma_{q,\varepsilon}\over G},
 \qquad
 b_{q,\varepsilon}={B_{q,\varepsilon}\over G}
 =k_{q,\varepsilon}\left(
   2-{(k_{q,\varepsilon}+1)N_{q,\varepsilon}\over G}\right), \tag{7.8}
\]

Then the exact aggregate requirement is

\[
 \sum_{1\le q\le H,\varepsilon}
 {d_{q,\varepsilon}-b_{q,\varepsilon}\over
  k_{q,\varepsilon}(k_{q,\varepsilon}+1)}=o(1).      \tag{7.9}
\]

The floors in (7.8) must not be replaced by a smooth Gaussian surrogate.
At a floor transition, (6.4) remains exact without any limiting
interpretation.

## 8. Why independent hashes fail

Consider one layer and parent rainbows \(P\). Assume first that every local
option is individually ledger-closed, so every product choice is a legal
state. Form a random state by choosing the local parent phases
independently. For a target
\(T\), let

\[
 p_{P,T}=\Pr(P\text{ emits }T),\qquad
 \lambda_T=\sum_Pp_{P,T},\qquad
 \eta=\max_{P,T}p_{P,T}.                             \tag{8.1}
\]

Because every parent is a rainbow and every state has \(G\) occurrences,

\[
 \sum_T\lambda_T=G.                                  \tag{8.2}
\]

### Theorem 8.1 (diffuse product-selector barrier)

If \(\eta<1\), then

\[
\boxed{
 \mathbb EH\ge N
   \exp\left(-{G/N\over1-\eta}\right).}              \tag{8.3}
\]

On the even central carrier, at \(q\le A\sqrt m\), if \(\eta=o(1)\) and
\(G=(1-o(1))W\), the right side is at least

\[
 \left(e^{-A^2-e^{A^2}}-o_A(1)\right)W.              \tag{8.4}
\]

#### Proof

For every target, independence and
\(\log(1-x)\ge-x/(1-x)\) give

\[
\begin{aligned}
 \Pr(T\text{ is missed})
 &=\prod_P(1-p_{P,T})\\
 &\ge\exp\left(-\sum_P{p_{P,T}\over1-p_{P,T}}\right)\\
 &\ge\exp\left(-{\lambda_T\over1-\eta}\right).
\end{aligned}                                        \tag{8.6}
\]

The function \(x\mapsto\exp(-x/(1-\eta))\) is convex. Jensen's
inequality and (8.2) therefore give (8.3). Equations (7.3)--(7.4) imply
(8.4). \(\square\)

This is a no-go for independent-root averaging. It does not, by itself,
exclude a rare correlated deterministic state in the same option product.
If a symmetry acts transitively on the product states and sends the target
support of one state to that of the next, then the hole count is
state-independent and (8.3) is a statewise no-go for that symmetric
catalogue.

There is a parallel quadratic warning. Under pairwise independent diffuse
parent phases, assume
\(\max_{P,T}p_{P,T}=\eta=o(1)\) and uniform target intensity

\[
 \lambda={G\over N}=k+\theta,\qquad0\le\theta<1,     \tag{8.7}
\]

one has

\[
 \overline\Gamma={G^2\over N}-o(W).                 \tag{8.8}
\]

Indeed, pair independence and the parent rainbow property give

\[
\begin{aligned}
 \overline\Gamma
 &=\sum_T\left(\lambda^2-\sum_Pp_{P,T}^2\right),\\
 0\le\sum_{P,T}p_{P,T}^2
 &\le\eta\sum_{P,T}p_{P,T}=\eta G=o(W),
\end{aligned}                                        \tag{8.8a}
\]

which proves (8.8).

But

\[
 {G^2\over N}-B
 =N\{k+\theta^2\}=\Omega_A(W).                      \tag{8.9}
\]

Thus pairwise decorrelation misses the exact floor energy by a linear
amount. Equation (8.9) says that the floor-Gram proof cannot succeed under
that law; unlike the fully independent estimate (8.3), it is not itself a
lower bound on the holes of every state.

## 9. Exact proved and conditional boundary

The following statements are proved.

1. Isometric \(C_{2h}\) strands have the unique fixed-frame normal form
   (0.1)--(0.2). Within that compiler class, projection freedom can only
   be supplied by a global cycle/packet mosaic. General longer cycles are
   subject only to the local freshness lemma.
2. Under the explicit boundary-incidence, port-pairing, and gluing
   hypotheses of Theorem 2.1, equation (0.3) is the exact necessary and
   sufficient literal resource equation for a cross-parent global braid.
3. Conditional on the certified two-sided trace-injective
   \(C_{2r}\)-compiler assumed in Theorem 3.2, the XOR-addressed
   selected-cell skeleton is an integral root-dependent mosaic with exact
   within-cell rainbows and the phasewise macroscopic-cut bound (3.13).
   Thus no fixed macroscopic coordinate cut gives its missing cut; no claim
   is made about arbitrary owner-coupled projections.
4. The provider-union identities (5.4)--(5.15), the floor identity (0.6),
   and the common all-depth estimate (0.7) are exact and integral.
5. On the even carrier, the uniform Gaussian target (7.6) implies the
   controlled-core missing-shadow and overload estimate (7.7); a proved
   exact completion gives (7.7a). For complete odd wreath factors, the
   sign-correct lower-shadow implication is Corollary 7.2.
6. Independent diffuse parent hashes have the linear expected-hole barrier
   (8.3), and cellwise branch translations cannot move active frames while
   preserving a fixed literal \(Y\)-palette.

The following statements are not proved.

1. No positive-density family of root-dependent *moving active-frame*
   labels is currently shown to solve the pointwise global ledger equations
   (0.3), retain the complete physical \(X/Y\) palettes of one exact wreath
   factor, and act through every Gaussian depth. This does not deny the
   known nonconstant fixed-frame packet trades or conditional split-router
   modules.
2. For the concrete XOR mosaic, neither the near-Latin provider condition
   (5.6)/(5.12) nor the floor-Gram estimate (7.6) is proved. Exact XOR-bin
   balance and within-parent rainbows do not imply either assertion.
3. The dyadic XOR carrier is not an all-\(m\) construction. An exact
   dimension-transfer theorem would still be needed even after the two
   preceding gates were closed.
4. Small unlabelled missing-shadow mass would compose to the frozen MWB
   lane, but it does not by itself prove labelled common-owner
   synchronization.

The surviving coefficient-one object is therefore precise:

\[
 \boxed{
 \begin{gathered}
 \text{construct a catalogue of complete exact global braid states}\\
 \text{satisfying the literal ledger cocycle (0.3), and arrange either}\\
 \sum_{1\le q\le A\sqrt m,\varepsilon,T}
 |Z\setminus\bigcup_PS_P(q,\varepsilon,T)|=o(W|Z|),\\
 \text{or }\quad
 \overline\Gamma_{q,\varepsilon}
       \le B_q+O_A(W/m)
       \text{ uniformly for }1\le q\le A\sqrt m.\\
 \text{The required dependence is near-Latin/floor-balanced across parents,}\\
 \text{not independent root hashing or a fixed macroscopic coordinate cut.}
\end{gathered}}                                      \tag{9.1}
\]

The first alternative in (9.1) is the exact literal missing-shadow gate.
The second is stronger: by (6.3b) it also gives balanced-quota overload
control and therefore the direct fixed-\(A\) MWB implication in
Corollary 7.2.

This is the exact theorem/no-go boundary reached in this lane.

## 10. Independent audit of the decisive steps

The two decisive identities were checked by an independent proof route.

1. For Theorem 1.1, write the two antipodal geodesic arcs as
   \(a_i\mapsto b_i\) and \(c_i\mapsto d_i\). At every prefix length
   \(j\), the antipodal equality

   \[
   d_J(X_j,X_{h+j})=h
   \]

   forces the second arc's removed \(B\)-prefix to equal
   \(\{b_0,\ldots,b_{j-1}\}\) and its inserted \(A\)-prefix to equal
   \(\{a_0,\ldots,a_{j-1}\}\). Equality for every \(j\) gives
   \(c_i=b_i,d_i=a_i\) termwise. This verifies the unique active matching
   without relying on a drawing or an assumed cube representation.

2. For Theorem 6.1, the pointwise inequality

   \[
   n(n-1)\ge
   2kn-k(k+1)+k(k+1)\mathbf 1_{\{n=0\}}
   \]

   follows because for \(n\ge1\) the difference is
   \((n-k)(n-k-1)\ge0\). Summing and using
   \(\sum_Tn_T=G\) gives
   \(\Gamma\ge B+k(k+1)H\), with equality precisely at positive loads
   \(k,k+1\). This independently confirms the floor, denominator,
   integrality, and equality case in (6.3).

The audit also confirms the scope limitation: the XOR union
\(K_{m,m}\) rules out only a target statistic invariant under every frame
exchange. It does not prove the literal provider union, and it does not
exclude an invariant coupled to the owner hash.
