# Exact affine candidate degrees for first-eligible \(B_4\) packets and the three-seed component cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The geometric candidate-cell degree of every physical target in a fixed
first-eligible \(B_4\) atlas has an exact closed form. It can be written
either as a prefix coefficient for the actual block order or, after
averaging over block orders, as one elementary hypergeometric expression.

Let

\[
 h=2r,\qquad q\le r,
\]

and let

\[
 p_{h,q}=\frac{2^q}{\binom hq}.
\tag{0.1}
\]

For a fixed labelled seed and fixed first-eligible order, define the local
target types \(E,C_1,C_2,N\) as follows:

\[
\begin{array}{c|cccc}
 &E&C_1&C_2&N\\ \hline
 \text{lower}&T_i\in\mathcal A&|T_i|=1&|T_i|=0&
       \text{all other states}\\
 \text{upper}&T_i\in\mathcal A&|T_i|=3&|T_i|=4&
       \text{all other states}.
\end{array}
\tag{0.2}
\]

Here

\[
 \mathcal A=\{12,23,34,14\}
\tag{0.3}
\]

is the chosen four-state \(B_4\) cycle. Then the exact geometric degree is

\[
 \boxed{
 d_q^\epsilon(T)
 =[x^rz^q]\sum_{\ell=1}^{b}
      m_{\pi(\ell)}^\epsilon(x,z)
      \prod_{j<\ell}g_{\pi(j)}^\epsilon(x,z),}
\tag{0.4}
\]

where

\[
\begin{array}{c|cccc}
\tau&E&C_1&C_2&N\\ \hline
g_\tau&x&1+xz&1+xz^2&1\\
m_\tau&x&xz&xz^2&0.
\end{array}
\tag{0.5}
\]

Every candidate packet contains one unique physical affine \(q\)-face
with trace \(T\). Therefore the target's exact degree in the full affine
factor menu is

\[
 \boxed{
 \deg_{\Gamma_h}(q,\epsilon,T)
 =|\Gamma_h|p_{h,q}d_q^\epsilon(T),\qquad
 \Gamma_h=\mathbb F_2^h\rtimes S_h.}
\tag{0.6}
\]

If \(e,c_1,c_2\) are the numbers of blocks of the first three types in
(0.2), then averaging (0.4) over all physical block orders gives

\[
 \boxed{
 \frac1{b!}\sum_{\pi\in S_b}d_{q,\pi}^\epsilon(T)
 =
 \sum_{a+2c=q}
 \binom{c_1}{a}\binom{c_2}{c}
 \Phi_{r,a+c}(e),}
\tag{0.7}
\]

where

\[
 \Phi_{r,k}(e)=
 \begin{cases}
 0,&e+k<r,\\[1mm]
 \displaystyle
 \frac{\binom e{r-k}}{\binom{e+k}r}
 =\frac{(r)_k}{(e+k)_k},&e+k\ge r.
 \end{cases}
\tag{0.8}
\]

Equations (0.4)--(0.8) are pointwise: they determine the degree of every
physical target, not only its average over a rank.

There is, however, an exact obstruction to using *all* relabelled \(B_4\)
seeds as independent packet states.

The \(24\) coordinate relabellings produce only three distinct owner
supports

\[
 \mathcal A_j=\binom{[4]}2\setminus M_j,
\tag{0.9}
\]

where \(M_1,M_2,M_3\) are the three perfect matchings of \(K_4\). The
stabilizer of one \(\mathcal A_j\) has order eight. Only those eight
relabelings preserve an existing packet; they are already cube
automorphisms counted in (0.6). A relabelling taking \(\mathcal A_i\) to
\(\mathcal A_j\), \(i\ne j\), changes the middle-owner support.

On the six local middle owners, the three supports have incidence matrix

\[
 B=
 \begin{pmatrix}
 0&1&1\\
 1&0&1\\
 1&1&0
 \end{pmatrix},
 \qquad \det B=2,
\tag{0.10}
\]

after grouping the owners into the three omitted matching pairs. Exact
ownership would require

\[
 Bz=\mathbf1.
\tag{0.11}
\]

Its unique solution is

\[
 z_1=z_2=z_3=\frac12,
\tag{0.12}
\]

so there is a perfect fractional seed mixture and no integral mixture of
whole seed cells.

This is the requested inseparable component cut. It shows that an affine
lower-tail proved by averaging the three seed supports, or by changing the
global first-eligible block order, does not admit an independent integral
packet-state assignment. Such averaging changes the owner partition
itself. A positive theorem must either:

1. work inside one fixed seed atlas using only the degree sequence (0.4);
   or
2. construct a nonlocal repacketization trade which resolves the
   determinant-two overlay while preserving all target traces.

The present affine Hall theorem supplies neither operation automatically.

## 1. The three local \(B_4\) seed supports

Let \(B=\{1,2,3,4\}\). The displayed seed is

\[
 \mathcal A=\{14,12,23,34\}
 =\binom B2\setminus\{13,24\}.
\tag{1.1}
\]

Its four states form the physical square

\[
 14\longrightarrow12\longrightarrow23
 \longrightarrow34\longrightarrow14.
\tag{1.2}
\]

The lower one-edge traces are

\[
 1,2,3,4,
\tag{1.3}
\]

and the upper one-edge traces are

\[
 124,123,234,134.
\tag{1.4}
\]

Thus every singleton and every triple occurs exactly once. The lower
two-direction trace is \(\varnothing\), and the upper two-direction trace
is \(B\).

Every coordinate relabelling sends the omitted matching in (1.1) to a
perfect matching. Conversely \(S_4\) is transitive on the three perfect
matchings, and the stabilizer of one matching has size

\[
 \frac{24}{3}=8.
\tag{1.5}
\]

Therefore the orbit contains the three supports (0.9), each with eight
relabelling labels.

### Lemma 1.1 (support-preserving relabellings)

A coordinate relabelling is an owner-preserving state of a fixed local
\(B_4\) packet if and only if it stabilizes the omitted perfect matching.

#### Proof

The owner support is exactly the complement of that matching in
\(\binom B2\). Preserving the support is therefore equivalent to
preserving the matching. \(\square\)

The eight allowed labels can change the orientation, phase, and naming of
the two cube axes. They do not create a new geometric candidate cell.

## 2. Local trace classification

Partition the physical coordinates into ordered complete four-blocks

\[
 B_1,\ldots,B_b
\]

and a remainder of size at most three. Fix one seed support
\(\mathcal A_i\) in every complete block.

Let \(P\cong\mathcal A_{i_1}\times\cdots\times\mathcal A_{i_r}\cong Q_h\)
be a canonical first-eligible packet. Consider an affine \(q\)-face
\(R\subseteq P\).

For a selected block, let \(j\in\{0,1,2\}\) be the number of its two cube
directions active in \(R\). By (1.3)--(1.4), the physical local trace is:

\[
\begin{array}{c|ccc}
 &j=0&j=1&j=2\\ \hline
 \text{lower}&\mathcal A_i\text{-state}&\text{singleton}&\varnothing\\
 \text{upper}&\mathcal A_i\text{-state}&\text{triple}&B_i.
\end{array}
\tag{2.1}
\]

Moreover the local affine face is uniquely recovered from its physical
trace:

* at \(j=0\), the trace is its one owner state;
* at \(j=1\), (1.3) or (1.4) identifies its unique edge;
* at \(j=2\), the face is the whole local square.

### Lemma 2.1 (unique physical candidate face)

Fix a packet \(P\), a sign, a depth \(q\le r\), and a physical target
\(T\). There is at most one affine \(q\)-face in \(P\) having trace \(T\).

#### Proof

Equation (2.1) identifies the number of active directions and the unique
local affine face independently in every selected block. The exterior of
the packet is frozen and must equal the corresponding restriction of
\(T\). Taking the product recovers the unique global face. \(\square\)

## 3. Exact degree in the actual first-eligible order

Fix a physical block order \(\pi(1),\ldots,\pi(b)\). Scan the blocks in
that order. For the target \(T\), assign the four types in (0.2).

A rank-two eligible block is forced into the completed middle owner's
eligible list. A \(C_1\)-block may either remain outside the packet or be
completed along its unique local one-face; choosing it uses one active
direction. A \(C_2\)-block may remain outside or be completed to the whole
local square; choosing it uses two active directions. A neutral block
cannot be selected.

The selected packet stops at the \(r\)-th marked block. Thus:

* \(g_i\) in (0.5) records all possibilities before the stopping block;
* \(m_i\) records that block \(i\) is the \(r\)-th marked block;
* the exponent of \(x\) records the number of selected blocks;
* the exponent of \(z\) records the number of active cube directions.

### Theorem 3.1 (pointwise prefix formula)

For every physical target \(T\), both signs, and every \(q\le r\), its
geometric candidate-packet degree is (0.4).

#### Proof

Given one monomial contributing to \([x^rz^q]\), mark every forced
\(E\)-block before the stopping index and the chosen \(C_1,C_2\)-blocks.
The last factor \(m_{\pi(\ell)}\) makes \(\pi(\ell)\) the \(r\)-th marked
block. Hence these are precisely the completed middle owner's first \(r\)
eligible blocks. The marked \(C_1,C_2\)-blocks use altogether \(q\)
directions and determine, by Lemma 2.1, one physical affine \(q\)-face
with trace \(T\).

Conversely, a candidate packet and its unique face mark exactly these
blocks and have a unique stopping index. Thus the correspondence is
bijective. \(\square\)

This formula includes targets with degree zero.

### Corollary 3.2 (rankwise first moment)

Let \(G\) be the number of middle owners retained by the fixed atlas. Then
for either sign,

\[
 \boxed{
 \sum_T d_q^\epsilon(T)
 =G\,\frac{\binom hq}{2^q}.}
\tag{3.1}
\]

#### Proof

There are \(G/2^h\) packets. Each \(Q_h\)-packet has
\(2^{h-q}\binom hq\) affine \(q\)-faces, and Lemma 2.1 makes every such
face one physical target incidence. Multiplication gives (3.1).
\(\square\)

Consequently

\[
 \sum_Tp_{h,q}d_q^\epsilon(T)=G,
\tag{3.2}
\]

so the affine barycenter has exactly the required total occurrence mass.
The unresolved issue is its targetwise lower tail, not a loss in total
mass.

## 4. Averaging over block orders

Let

\[
 e=|E(T)|,\qquad c_1=|C_1(T)|,\qquad c_2=|C_2(T)|.
\tag{4.1}
\]

Choose \(a\) \(C_1\)-blocks and \(c\) \(C_2\)-blocks with

\[
 a+2c=q,\qquad k=a+c.
\tag{4.2}
\]

For this fixed touched set, only the relative order of its \(k\) blocks
and the \(e\) forced eligible blocks matters. It is admitted exactly when
all \(k\) touched blocks lie among the first \(r\) members of their union.

If \(e+k<r\), this is impossible. Otherwise the first \(r\) relative
positions form a uniform \(r\)-subset of an \((e+k)\)-set, so the exact
probability is

\[
 \frac{\binom e{r-k}}{\binom{e+k}r}
 =\Phi_{r,k}(e).
\tag{4.3}
\]

Summing over the choices of touched blocks proves (0.7).

### Corollary 4.1 (three global seed supports)

Let \(e_j(T)\) be the number of local rank-two blocks of \(T\) whose
two-set lies in \(\mathcal A_j\). Uniformly averaging over the three
globally relabelled seed supports and over all block orders gives

\[
 \boxed{
 \overline d_{q,\mathrm{global}}^\epsilon(T)
 =
 \sum_{a+2c=q}\binom{c_1}{a}\binom{c_2}{c}
 \frac13\sum_{j=1}^3\Phi_{r,a+c}(e_j(T)).}
\tag{4.4}
\]

If raw coordinate-relabel and block-order labels rather than the normalized
average are counted, multiply (4.4) by \(24\,b!\).

### Corollary 4.2 (independent local seed relabellings)

Let \(n_2(T)\) be the number of complete blocks on which \(T\) has local
rank two. Under an independent uniform choice of one of the three seed
supports in every block, each such state is eligible with probability
\(2/3\). Therefore

\[
 \boxed{
 \overline d_{q,\mathrm{local}}^\epsilon(T)
 =
 \sum_{a+2c=q}\binom{c_1}{a}\binom{c_2}{c}
 \sum_{e=0}^{n_2}
 \binom{n_2}{e}\left(\frac23\right)^e
                    \left(\frac13\right)^{n_2-e}
 \Phi_{r,a+c}(e).}
\tag{4.5}
\]

If raw seed-support atlas labels are counted, multiply (4.5) by
\(3^b b!\). If all coordinate relabellings, including their eight-element
stabilizers, are separately labelled, multiply instead by \(24^b b!\).

Equations (4.4)--(4.5) are exact geometric averages. They do not yet assert
that the corresponding atlas choices can be made independently on
different packets.

## 5. Exact specialization of the affine Hall theorem

Install the recursive two-sided trace-injective factor \(F_h\) in every
fixed packet. Let

\[
 \Gamma_h=\operatorname {Aut}(Q_h).
\]

The factor selects \(2^h\) distinct affine \(q\)-faces. Since \(Q_h\) has

\[
 2^{h-q}\binom hq
\]

affine \(q\)-faces and \(\Gamma_h\) is transitive on them, a prescribed
face is selected by the fraction

\[
 p_{h,q}
 =\frac{2^h}{2^{h-q}\binom hq}
 =\frac{2^q}{\binom hq}
\tag{5.1}
\]

of the full affine menu.

Combining Lemma 2.1 with (5.1) proves (0.6). In particular, for one fixed
first-eligible atlas \(\sigma\), the affine-average theorem gives the
fractional deficiency estimate

\[
 \boxed{
 D_{\rm frac}(\sigma)
 \le
 \sum_{q\le H}\sum_{\epsilon=\pm}
 \sum_T\left(1-p_{h,q}d_{\sigma,q}^\epsilon(T)\right)_+.}
\tag{5.2}
\]

The right side is now a completely explicit deterministic expression by
(0.4).

The same conclusion holds with prescribed target demands \(b_T\), replacing
the summand by

\[
 \left(b_T-p_{h,q}d_{\sigma,q}^\epsilon(T)\right)_+.
\tag{5.3}
\]

There is no loss from intrapacket collisions: the recursive factor is
two-sided trace-injective through \(q\le r\).

## 6. The inseparable three-seed component

Let \(M_1,M_2,M_3\) be the three perfect matchings of \(K_4\), and write

\[
 P_j=M_j
\]

for the corresponding two-owner classes. The seed cell

\[
 \mathcal A_j=\binom{[4]}2\setminus M_j
\]

contains every owner in \(P_k\) for \(k\ne j\) and no owner in \(P_j\).
Thus the cell-versus-owner-class incidence is exactly (0.10).

### Theorem 6.1 (determinant-two seed obstruction)

No union of whole relabelled \(B_4\) seed cells covers each of the six
local middle owners exactly once. The unique fractional exact cover uses
weight \(1/2\) on each of the three cells.

#### Proof

If \(z_j\) is the multiplicity of \(\mathcal A_j\), exact coverage of the
two owners in \(P_1,P_2,P_3\) gives

\[
 z_2+z_3=1,\qquad
 z_1+z_3=1,\qquad
 z_1+z_2=1.
\tag{6.1}
\]

Subtracting pairs of equations makes the three variables equal; then each
equals \(1/2\). This is fractional and is not integral. \(\square\)

Tensoring with any fixed exterior owner set or any fixed factors in other
selected blocks preserves this obstruction: it merely repeats the same
matrix on disjoint six-owner fibres. Hence cross-seed choices are
inseparable owner components, not independent packet colors.

### Corollary 6.2 (no packetwise rounding of all-seed averaging)

The averages (4.4)--(4.5) cannot be used as barycentric packet-state loads
and then rounded by choosing one relabelled seed independently in every
packet.

#### Proof

On a packet, changing to a different seed support replaces one local
\(\mathcal A_i\)-factor by \(\mathcal A_j\). The middle-owner support
changes. On the three-support overlay, Theorem 6.1 is the exact local
ownership equation, and it has no integral solution. \(\square\)

This remains true even if the target-side affine Hall inequalities are
strictly feasible. The obstruction is on the owner side and precedes
target rounding.

## 7. Block permutations: internal versus external

There are two different operations called a block permutation.

1. A permutation of the \(r\) already selected local squares inside one
   fixed packet preserves its \(4^r\)-owner support. It is a cube
   automorphism and is already contained in \(\Gamma_h\). It changes the
   factor state but not the geometric degree (0.4).

2. A permutation of the ambient ordered list \(B_1,\ldots,B_b\) changes
   which eligible blocks are first. It changes the packet partition.
   Formula (0.7) is an average over these different global atlases, not a
   menu of independent states on a fixed packet.

Thus neither global seed relabelling nor global first-eligible-order
averaging supplies the product-of-packet-simplices required by an integral
packet-state theorem.

## 8. Exact remaining positive theorem

The valid fixed-atlas problem is now sharply separated from the invalid
all-seed shortcut.

> **Fixed-seed \(B_4\) resolvable affine cover — open.** Fix one seed
> support and one ambient first-eligible block order. Using only
> owner-preserving affine conjugates in each resulting packet, choose one
> state per packet so that
> \[
> \sum_{q\le H}\sum_{\epsilon=\pm}
> \#\{T:T\text{ receives no actual consecutive trace}\}=o(W).
> \]

For this theorem:

* the exact physical candidate degrees are (0.4);
* the exact affine target degrees are (0.6);
* the affine-average sufficient lower tail is (5.2);
* all intrapacket trace collisions are absent.

What remains is either:

1. prove that (5.2) is \(o(W)\) in a suitable parameter range and then
   prove a one-sided integral rounding theorem for the packet trace towers;
   or
2. find a target-side weighted cut inside this one fixed owner atlas.

Any attempt to average the other two seed supports must first supply a
nonlocal owner-repacketization trade resolving (0.10). The determinant-two
component proves that local packetwise seed switching cannot do it.

## 9. Audit checklist

1. Local ranks \(2,1,0\) below and \(2,3,4\) above determine respectively
   zero, one, and two active directions.
2. The physical target determines the unique local face in every selected
   block.
3. The stopping factor \(m_\ell\), rather than the full product
   \(\prod_i g_i\), is essential: eligible blocks after the \(r\)-th one
   are frozen exterior data.
4. The block-order average tests whether all chosen touched blocks occur
   among the first \(r\) members of their union with the forced eligible
   blocks; this is exactly (0.8).
5. The three seed supports, not the \(24\) relabelling labels, are the
   geometric alternatives.
6. Only the eight-label stabilizer of one seed is owner-preserving.
7. The determinant-two matrix is an owner-incidence obstruction. It does
   not assert that the fixed-seed target Hall system is infeasible.
