# Context arrays, physical face incidence, and the affine outer Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is
used.

## 0. Outcome

Let one canonical all-\(Q_2\) tensor packet be partitioned into its
\(6^r\) physical cells \(c\cong Q_s\), where

\[
                              s=2r
\tag{0.1}
\]

is a power of two.  The context-dependent permutation-array theorem and the
packet-wide shadow-injectivity theorem do not combine in the form in which
they were originally stated.

The exact conclusions are as follows.

1.  The original balanced array is correct as a macro-support theorem for
    the uniform-order Hamming factor.  Its exact physical phase multiplicity
    is, however, either zero or a power of two which is at least
    \(2^q/s\).  In particular, every factor having one common cyclic
    coordinate order in a cell has at most

    \[
                              s2^{s-q}
    \tag{0.2}
    \]

    distinct depth-\(q\) lower targets, and the same bound holds above.
    Hence, if \(q=x\sqrt m+o(\sqrt m)\), \(x>0\), no orthogonal array of
    such one-order cell factors can satisfy even the all-target Hall cut:
    it hits only \(o(W)\) distinct targets at a rank containing
    \(\Theta_x(W)\) targets.

2.  There is a corrected positive combination.  Put the two directions of
    each tensor block in one bottom sibling pair of the recursive factor
    \(F_{2r}\), and conjugate \(F_{2r}\) independently in the \(6^r\)
    cells by block permutations.  For every \(H=o(r)\), some deterministic
    block-permutation array gives, simultaneously for
    \(q\le H\) and \(J\in\binom{[r]}q\),

    \[
       L_{q,J}=(1+o(1)){24^r\over\binom rq}.
    \tag{0.3}
    \]

    The same factor is literally lower- and upper-shadow injective on all
    \(24^r\) packet owners through depth \(r\).  Thus (0.3) is a valid
    packet-wide injective macro census, but its proof is by group averaging,
    not by the original four-start argument.

3.  For a physical target \(T\), its candidate cell, order, translation,
    and start-phase multiplicities can be computed exactly.  If
    \(d_q^\epsilon(T)\) is its number of geometric candidate cells and the
    full affine cube menu

    \[
                              \Gamma_s=\mathbb F_2^s\rtimes S_s
    \tag{0.4}
    \]

    is used, then

    \[
      \deg_{\Gamma_s}(q,\epsilon,T)
       =|\Gamma_s|{2^q\over\binom sq}\,d_q^\epsilon(T),
    \tag{0.5}
    \]

    and every menu label counted in (0.5) contains the target at one unique
    start phase.  For a fixed coordinate permutation, the admissible
    translations are explicit unions of cosets of the \(q\)-dimensional
    direction subspace.  Exact uniformity on all such cosets is binary
    orthogonal-array strength \(s-q\), not ordinary shallow-strength or
    macro-support balance.

4.  The full affine menu satisfies a literal weighted expansion theorem.
    Give a tagged physical target \(t=(q,\epsilon,T)\) demand \(b_t\), put

    \[
                 p_t={2^q\over\binom sq},\qquad d_t=d_q^\epsilon(T),
    \tag{0.6}
    \]

    and let \(D_{\rm frac}\) be the minimum fractional unmet demand when
    one affine conjugate must be chosen from every cell menu.  Then

    \[
       \boxed{
       D_{\rm frac}\le
       \sum_t (b_t-p_td_t)_+.}
    \tag{0.7}
    \]

    In particular, \(p_td_t\ge b_t\) for every target implies every
    weighted outer Hall inequality.  The aggregate condition

    \[
                         \sum_t(b_t-p_td_t)_+=o(W)
    \tag{0.8}
    \]

    implies fractional spill \(o(W)\).

Statement (0.7) is a genuine literal expansion theorem, but (0.8) is not
proved for the canonical outer packet atlas.  Nor is a one-choice integral
rounding theorem proved.  Thus this note does not prove MWB or coefficient
one.  It proves the corrected packet theorem, refutes the common-order
orthogonal-array route at Gaussian depth, and isolates the remaining
physical candidate-degree lower tail exactly.

## 1. Cells and physical candidate faces

In a physical constant-weight cube \(c\cong Q_s\), write its active pairs
as \(E_1,\ldots,E_s\).  An affine \(q\)-face is determined by

\[
               (D,y),\qquad D\in\binom{[s]}q,\quad
               y\in\{0,1\}^{[s]\setminus D}.
\tag{1.1}
\]

Its lower physical trace makes every pair indexed by \(D\) empty and keeps
the endpoint choices \(y\) on the other pairs.  Its upper trace makes every
pair indexed by \(D\) full and keeps the same outside choices.

Fix a tagged target

\[
                         t=(q,\epsilon,T),qquad\epsilon\in\{-,+\}.
\tag{1.2}
\]

The local face-separation theorem gives either no face of \(c\) with trace
\(T\), or a unique such face, denoted

\[
                         R_c(t)=R_c^\epsilon(T).
\tag{1.3}
\]

Define the geometric candidate-cell set and degree by

\[
 \mathscr C(t)=\{c:R_c(t)\text{ exists}\},
 \qquad d_t=|\mathscr C(t)|.
\tag{1.4}
\]

Within one canonical tensor packet, a physical target is a face of at most
one product cell.  This follows block by block from the six-\(Q_2\)
face-separation theorem.  Across an owner-disjoint family of packets, the
same physical target can have many candidate cells; those are exactly the
outer incidences counted by \(d_t\).

## 2. Exact audit of the original uniform-order array

Write the directions of tensor block \(i\) as

\[
                         \alpha_i,\beta_i,qquad i\in[r].
\tag{2.1}
\]

For \(\pi\in S_r\), the separated order is

\[
 \omega_\pi=
 (\alpha_{\pi_1},\ldots,\alpha_{\pi_r},
  \beta_{\pi_1},\ldots,\beta_{\pi_r}).
\tag{2.2}
\]

The uniform-order Hamming factor has direction word
\(\omega_\pi\omega_\pi\) on every component.

### 2.1 Exact compatible-order census

Let \(R\) be a \(q\)-face, where \(q<r\), and put

\[
 A=\{i:\alpha_i\in\operatorname {dir}R\},\qquad
 B=\{i:\beta_i\in\operatorname {dir}R\},
 \qquad a=|A|,\quad b=|B|.
\tag{2.3}
\]

### Lemma 2.1

The number of \(\pi\in S_r\) for which \(\operatorname {dir}R\) is a
consecutive \(q\)-window of (2.2) is

\[
 N_{a,b}(R)=
 \begin{cases}
 0,&A\cap B\ne\varnothing,\\[1mm]
 q!(r-q+1)!,&(a,b)=(q,0)\text{ or }(0,q),\\[1mm]
 2a!b!(r-q)!,&a,b>0,\quad a+b=q.
 \end{cases}
\tag{2.4}
\]

#### Proof

The two directions in one tensor block are cyclically \(r\) positions
apart, so a window of length less than \(r\) cannot contain both.  An
all-\(\alpha\) or all-\(\beta\) set must be one ordinary consecutive block
in \(\pi\).  Ordering its \(q\) entries and then treating it as one object
with the other \(r-q\) entries gives \(q!(r-q+1)!\).

If both types occur, the window crosses one of the two seams.  At the
\(\alpha/\beta\) seam, the last \(a\) entries of \(\pi\) are the elements
of \(A\), the first \(b\) entries are the elements of \(B\), and the
remaining entries are arbitrary.  This gives \(a!b!(r-q)!\).  The other
seam gives the same number.  \(\square\)

For every compatible \(\pi\), the physical direction set occurs at two
phases in a length-\(2s=4r\) component.  Summing (2.4) over all
\(A\dot\cup B=J\), for fixed \(J\in\binom{[r]}q\), gives

\[
 \sum_{A\dot\cup B=J}N_{|A|,|B|}
 =2r q!(r-q)!.
\tag{2.5}
\]

Multiplication by the two physical phases gives
\(4r q!(r-q)!\), which is exactly the four-start macro count of the
context-array theorem.  Thus that macro count is correct.  It forgets the
\(\alpha/\beta\) split, the outside state \(y\), and the multiplicity with
which the corresponding affine face is traversed.

There is already an exact signed-direction obstruction inside the separated
family.  In one fundamental word \(\omega_\pi\), the \(2r\) cyclic
\(q\)-windows consist of

\[
 2(r-q+1)\text{ pure }\alpha/\beta\text{ windows},
 \qquad 2(q-1)\text{ mixed windows}.
\tag{2.6}
\]

Thus every weighted multiset of separated orders has pure signed-support
fraction \((r-q+1)/r\).  Uniformity over the \(2^q\) signed lifts of a
macro support would require pure fraction \(2/2^q=2^{1-q}\).  These are
unequal for every \(2\le q<r\).  Hence no orthogonal array confined to the
separated orders is fully uniform even on signed direction supports.  This
does not by itself prove a physical Hall cut, but it is another exact reason
that macro-support balance cannot be promoted by adding more separated
orders.

### 2.2 Exact phase multiplicity in the Hamming factor

Let \(s=2^t\).  In the syndrome construction of the uniform-order factor,
let

\[
 \phi:\mathbb F_2^s\longrightarrow\mathbb F_2^{t+1},
 \qquad K=\ker\phi,
\tag{2.7}
\]

and let \(\mathbf1\notin K\) be the antipodal vector.  Put

\[
                         L=K\oplus\langle\mathbf1\rangle.
\tag{2.8}
\]

Then \(L\) has codimension \(t\).  Let \(p_j\) be the standard cycle
prefix at a first-half phase \(j\), let \(z\) be the resolution-class
translation, and let \(\rho\) be the chosen coordinate permutation.

If \(D=\operatorname {dir}R\) is not the image under \(\rho\) of a cyclic
\(q\)-interval beginning at phase \(j\), then the phase multiplicity is
zero.  Otherwise the exact number of directed starts whose face is \(R\)
is

\[
 \boxed{
 \mu_{\rho,z,q}(R)
 =\#\{\ell\in L:z+\rho(p_j+\ell)\in R\}.}
\tag{2.9}
\]

Indeed, \(\ell=k+\tau\mathbf1\), with \(k\in K\) and
\(\tau\in\{0,1\}\), records uniquely the component translate and the two
antipodal phases.  Since a face of direction \(D\) is a coset of
\(V_D=\operatorname {span}\{e_i:i\in D\}\), (2.9) is either zero or

\[
 \boxed{
 2^{h_{\rho,D}},\qquad
 h_{\rho,D}=\dim(\rho L\cap V_D).}
\tag{2.10}
\]

As \(\rho L\) has codimension \(t\),

\[
                         h_{\rho,D}\ge q-t,
\tag{2.11}
\]

and therefore every realized face has multiplicity at least

\[
                         2^{q-t}={2^q\over s}.
\tag{2.12}
\]

For an actual balanced array \(\Pi=(\pi_c)\), the physical target load is
exactly

\[
 n_{\Pi,t}
 =\sum_{c\in\mathscr C(t)}
   \mu_{\rho_{\pi_c},z_c,q}(R_c(t)).
\tag{2.13}
\]

The macro statistics \(X_{q,J}(\Pi)\) do not determine or give a useful
targetwise lower bound on (2.13): they average over all cells, whereas
(2.13) samples the target-dependent candidate cells and retains the affine
phase condition.

### 2.3 A global statewise Hall cut

The following obstruction does not depend on the syndrome construction.

### Theorem 2.2 (common-order Hall obstruction)

Suppose \(G\le W\) middle owners are partitioned into owner-disjoint
physical \(Q_s\)-cells,
and every allowed alternative in each cell is a cycle factor whose
components all have one common cyclic order of the \(s\) directions.  At
depth \(q<s\), on either sign, every global selection hits at most

\[
                              {Gs\over2^q}
\tag{2.14}
\]

distinct physical targets.

Consequently, if \(q<s\), \(s\le2m\),
\(q=x\sqrt m+o(\sqrt m)\), where \(x>0\), and \(W-G=o(W)\), the weighted
outer Hall cut with unit demand on every target of that rank fails by
\(\Theta_x(W)\), even if the omitted \(W-G\) owners are completed
arbitrarily.

#### Proof

One cyclic direction word exposes at most \(s\) direction sets of length
\(q\).  For each direction set there are \(2^{s-q}\) affine faces.
Therefore one cell hits at most \(s2^{s-q}\) distinct lower targets, and
the same bound holds above.  There are \(G/2^s\) cells, so the union of all
their target images has size at most (2.14).  This remains true when the
common order and affine phase vary from cell to cell, and also when every
cell is offered an arbitrary menu of common-order alternatives from which
one factor is selected.  An arbitrary completion on the other \(W-G\)
owners contributes at most \(W-G\) further distinct targets at one depth.

For the even normalization, the exact adjacent-rank product is

\[
 {N_q\over W}
 =\prod_{j=0}^{q-1}{m-j\over m+j+1}.
\tag{2.15}
\]

If \(q\le A\sqrt m\), then for all sufficiently large \(m\),
\(j/m\le1/2\) and

\[
 \log{m-j\over m+j+1}
 \ge-{2j\over m}-{j+1\over m}.
\tag{2.16}
\]

Thus the product is bounded below by \(\exp(-O_A(1))\).  The odd
normalization has the same proof, with the denominator shifted by one.
Consequently, for a central or Gaussian rank,

\[
 {N_q\over W}=\exp(-O_x(1))=\Theta_x(1),
\tag{2.17}
\]
and, on the other hand,

\[
 {Gs\over2^q}\le {2mW\over2^{x\sqrt m+o(\sqrt m)}}=o(W).
\tag{2.18}
\]

In the weighted Hall dual, take \(\alpha_T=1\) on all targets at this
rank and sign and zero elsewhere.  The demand side is \(N_q=\Theta_x(W)\),
whereas the maximum contribution of all cell menus and the arbitrary leave
is bounded by \(Gs/2^q+(W-G)=o(W)\).  \(\square\)

Thus no stronger orthogonal array of common Hamming orders repairs the
physical defect.  The factor inside a cell must itself use many
cycle-dependent direction orders.

## 3. The corrected packet-wide balanced array

Use the recursive neighbor permutation \(F_s\) with \(s=2r\), placing the
two directions \(\alpha_i,\beta_i\) of tensor block \(i\) at one bottom
sibling node of the recursion tree.

For \(\pi\in S_r\), let \(\rho_\pi\) send both directions of block \(i\)
to the corresponding two directions of block \(\pi(i)\); thus a block
support \(I\) is sent to \(\pi(I)\).

### Lemma 3.1 (bottom-sibling separation)

In the first period of the direction word of every \(F_s\)-cycle, the two
directions in each bottom sibling pair occur cyclically \(r=s/2\) places
apart.  Consequently every window of at most \(r\) directions uses at
most one direction from each tensor block.

#### Proof

Induct on \(s\).  The assertion is immediate for \(s=2\).  In the
recursion from \(F_h\) to \(F_{2h}\), moves in the left and right halves
alternate.  The internal order of the moves in either half is the parent
order, with every parent position doubled.  A bottom sibling separation
of \(h/2\) in the parent therefore becomes a separation of \(h=(2h)/2\)
in the child.  A cyclic interval of length at most \(s/2\) cannot contain
both endpoints at cyclic distance \(s/2\).  \(\square\)

For \(q\le r\) and \(I\in\binom{[r]}q\), define the exact base
macro-support multiplicity

\[
 a_{q,I}
 =\#\{x\in Q_s:\text{the forward }q\text{-window from }x
                    \text{ touches precisely the blocks in }I\}.
\tag{3.1}
\]

Lemma 3.1 gives

\[
                         \sum_{I\in\binom{[r]}q}a_{q,I}=2^s=4^r.
\tag{3.2}
\]

### Theorem 3.2 (injective balanced block-permutation array)

Let \(H=o(r)\).  There are block permutations

\[
                         \pi_c\in S_r,
                         \qquad c\in[6]^r,
\tag{3.3}
\]

such that the union of the conjugated recursive factors is an exact
\(C_{4r}\)-factor of the packet, is lower- and upper-shadow injective on
all \(24^r\) owners for every \(q\le r\), and satisfies, uniformly for
\(1\le q\le H\) and \(J\in\binom{[r]}q\),

\[
 \boxed{
 L_{q,J}
 =\sum_{c\in[6]^r}a_{q,\pi_c^{-1}J}
 =(1+o(1)){24^r\over\binom rq}.}
\tag{3.4}
\]

#### Proof

Choose the \(\pi_c\)'s independently and uniformly from \(S_r\).  For
fixed \((q,J)\), put

\[
                         Y_c=a_{q,\pi_c^{-1}J}.
\tag{3.5}
\]

Transitivity of \(S_r\) on \(q\)-subsets and (3.2) give

\[
 \mathbb EY_c={4^r\over\binom rq},
 \qquad
 \mu_{q,J}:=\mathbb E\sum_cY_c
 ={24^r\over\binom rq}.
\tag{3.6}
\]

As \(0\le Y_c\le4^r\), Hoeffding's inequality gives, for every
\(0<\delta<1\),

\[
 \Pr\left\{\left|\sum_cY_c-\mu_{q,J}\right|>
             \delta\mu_{q,J}\right\}
 \le2\exp\left{-{2\delta^2 6^r\over\binom rq^2}\right\}.
\tag{3.7}
\]

Since \(H=o(r)\),

\[
 \log\sum_{q\le H}\binom rq=o(r),
 \qquad
 \max_{q\le H}\binom rq=\exp(o(r)).
\tag{3.8}
\]

Taking \(\delta=r^{-1}\), the union bound in (3.7) tends to zero.  This
proves the existence of one array satisfying (3.4).

Every block permutation is a cube automorphism, so every conjugate remains
an exact \(C_{2s}=C_{4r}\)-factor.  The recursive shadow theorem gives
injectivity within each cell through \(q=s/2=r\).  The local
six-\(Q_2\) face-separation theorem applies to every affine face, so equal
physical traces from two cells force the cells to be equal.  Thus the
union is packet-wide injective on both signs.  \(\square\)

The cycles of \(F_s\) do not all have one common direction word.  Therefore
(3.4) is a balance theorem for the actual recursive-window multiplicities;
it is not the original per-cell four-start statement in different notation.

## 4. Exact physical incidence for the injective factor

Throughout this section, \(1\le q\le s/2\).  Let

\[
 \mathcal A_q(F_s)
 =\{A_q(x):x\in Q_s\}
\tag{4.1}
\]

be the affine faces selected by the forward \(q\)-windows of \(F_s\).
For \(q\le s/2\), shadow injectivity says that (4.1) consists of exactly
\(2^s\) distinct faces and that each face has one unique start phase.

### 4.1 Diagonal block-permutation menu

Encode an affine face blockwise by one of the nine states

\[
 00,01,10,11,*0,*1,0*,1*,**.
\tag{4.2}
\]

Let \(\mathbf n(R)=(n_\tau(R))_\tau\) be its histogram.  The diagonal
block-permutation group \(S_r\) has exactly these histograms as its orbits
on affine faces.  Put

\[
 a_q(\mathbf n)
 =\#\{R'\in\mathcal A_q(F_s):\mathbf n(R')=\mathbf n\}.
\tag{4.3}
\]

### Proposition 4.1 (exact block-order and phase count)

For a fixed candidate face \(R\), the number of block permutations
\(\rho_\pi\) whose conjugated recursive factor selects \(R\) is

\[
 \boxed{
 N_{\rm block}(R)
 =a_q(\mathbf n(R))\prod_\tau n_\tau(R)!.}
\tag{4.4}
\]

Every permutation counted in (4.4) contains \(R\) at one unique phase.

#### Proof

For every selected source face \(R'\) with the same histogram as \(R\),
exactly \(\prod_\tau n_\tau(R)!\) block permutations send \(R'\) to
\(R\).  Conversely, equal histograms are necessary.  For a fixed
permutation, its source face is \(\rho_\pi^{-1}R\), so two distinct source
faces cannot be counted by the same permutation.  The uniqueness of the
phase follows from shadow injectivity.  \(\square\)

Thus for a target \(t\), the exact degree in the full block-permutation
menu is

\[
 \deg_{\rm block}(t)
 =\sum_{c\in\mathscr C(t)}
   a_q(\mathbf n(R_c(t)))\prod_\tau n_\tau(R_c(t))!,
\tag{4.5}
\]

whereas its actual load under the array of Theorem 3.2 is

\[
 \boxed{
 n_\Pi(t)
 =\sum_{c\in\mathscr C(t)}
   \mathbf1_{\{\rho_{\pi_c}^{-1}R_c(t)\in\mathcal A_q(F_s)\}}.}
\tag{4.6}
\]

Formula (4.6) is the exact candidate-cell/order/phase ledger.  The phase is
unique whenever the indicator is one.  The macro census (3.4) sums over
all cell faces of a given block support and does not control (4.6) for a
fixed physical target.

### 4.2 Full labeled affine menu

For \(A\in\binom{[s]}q\), define

\[
 m_q(A)=\#\{R'\in\mathcal A_q(F_s):
                         \operatorname {dir}R'=A\},
 \qquad \sum_A m_q(A)=2^s.
\tag{4.7}
\]

### Theorem 4.2 (order--translation--phase census)

Fix an affine face \(R\) of direction \(D\).  For a prescribed coordinate
permutation \(\sigma\in S_s\), the number of translations
\(z\in\mathbb F_2^s\) for which

\[
                         (z,\sigma)F_s(z,\sigma)^{-1}
\tag{4.8}
\]

selects \(R\) is

\[
 \boxed{
                         2^q m_q(\sigma^{-1}D).}
\tag{4.9}
\]

Summing over all orders gives

\[
 \boxed{
 N_{\Gamma_s}(R)
 =2^{s+q}q!(s-q)!
 =|\Gamma_s|{2^q\over\binom sq}.}
\tag{4.10}
\]

Every affine menu label counted in (4.9)--(4.10) contains \(R\) at one
unique start phase.

#### Proof

Let \(R'\in\mathcal A_q(F_s)\) have direction \(\sigma^{-1}D\).  The
translations sending \(\sigma R'\) to \(R\) form one coset of the
translation stabilizer \(V_D\), hence there are exactly \(2^q\).  The
cosets obtained from distinct \(R'\)'s are disjoint, proving (4.9).

For each \(A\in\binom{[s]}q\), exactly \(q!(s-q)!\) permutations satisfy
\(\sigma A=D\).  Therefore

\[
 \sum_{\sigma\in S_s}2^qm_q(\sigma^{-1}D)
 =2^qq!(s-q)!\sum_Am_q(A)
 =2^{s+q}q!(s-q)!,
\tag{4.11}
\]

which is (4.10).  Phase uniqueness again follows from injectivity of
\(x\mapsto A_q(x)\).  \(\square\)

Applying (4.10) in every candidate cell proves (0.5).

### 4.3 The required fibrewise orthogonal-array strength

For fixed \(\sigma\) and fixed source face \(R'\), the translations in
(4.9) form

\[
                         z(R,R',\sigma)+V_D.
\tag{4.12}
\]

Within one fixed permutation fibre \(\sigma\), uniformity on all cosets of
all \(q\)-dimensional coordinate subspaces is equivalent to uniformity of
the translation projection onto every complementary set of \(s-q\)
coordinates.  In standard terminology this is binary orthogonal-array
strength \(s-q\).  More generally, for a sub-menu
\(\mathcal G\subseteq\Gamma_s\), the exact incidence of \(R\) is

\[
 \sum_{\sigma\in S_s}
 \sum_{\substack{R'\in\mathcal A_q(F_s)\\
                  \operatorname {dir}R'=\sigma^{-1}D}}
 \#\left(\mathcal G_\sigma\cap
          (z(R,R',\sigma)+V_D)\right).
\tag{4.13}
\]

More explicitly, suppose the translation multiset \(Z_\sigma\) in fibre
\(\sigma\) is an OA of strength \(s-q\) and index

\[
                         \lambda_\sigma={|Z_\sigma|\over2^{s-q}}.
\tag{4.14}
\]

Then every coset in (4.12) contains \(\lambda_\sigma\) rows and

\[
 N_{\mathcal G}(R)
 =\sum_{\sigma\in S_s}
       \lambda_\sigma m_q(\sigma^{-1}D).
\tag{4.15}
\]

Thus equal fibre indices are sufficient for direction-independent
incidence, whereas unequal indices require a separate weighted balance of
the direction catalogue.

For all depths beginning with \(q=1\), a translation array which is
face-regular separately in every permutation fibre by this sufficient
mechanism needs strength \(s-1\).  Fibrewise strength alone does not balance
the fibre weights or the direction catalogue \(m_q(\sigma^{-1}D)\), and a
joint array can in principle compensate between permutation fibres.  Thus
strength \(s-q\) is an exact fibrewise criterion, not a necessary
characterization of aggregate face regularity.  A low-strength array on
block labels, even one which is perfectly balanced on all macro supports
through \(H\), does not control (4.13).

There are also inseparable local resources.  The lower and upper traces of
one face occur together.  In any isometric \(2s\)-cycle, every length-\(s\)
arc uses all \(s\) directions.  Comparing the length-\(s\) direction sets
beginning at consecutive phases gives

\[
                              w_{i+s}=w_i.
\tag{4.16}
\]

The vertex after \(s\) steps is antipodal and the following \(q\)-window
has the same directions.  Hence \(R+\mathbf1\) occurs whenever \(R\)
occurs.  Thus

\[
 L(R),\quad U(R),\quad L(R+\mathbf1),\quad U(R+\mathbf1)
\tag{4.17}
\]

have identical local menu incidence.  A rounding theorem must quotient or
retain these quartets; no codegree-small assertion is available before
that quotient.

## 5. A literal weighted outer expansion theorem

Let \(\mathcal T\) be any collection of tagged physical targets, possibly
containing several depths \(q(t)\le s/2\) and both signs.  In every cell use
the full labeled affine menu \(\Gamma_s\).  Distinct labels which induce
the same factor through a stabilizer are retained; quotienting them divides
all relevant degrees by the same stabilizer and does not change a maximum.
For \(g\in\Gamma_s\), let \(\mathcal S(c,g)\) be the
set of tagged targets supplied by the conjugated injective factor in cell
\(c\).

Give target \(t\) demand \(b_t\ge0\).  Consider the fractional completion
program

\[
\begin{aligned}
 \min\quad&\sum_tz_t,\\
 \text{subject to}\quad&
 \sum_{g\in\Gamma_s}x_{c,g}=1 &&(c\in\mathscr C),\\
 &\sum_{c,g:t\in\mathcal S(c,g)}x_{c,g}+z_t\ge b_t
                                                &&(t\in\mathcal T),\\
 &x_{c,g}\ge0,\qquad z_t\ge0.
\end{aligned}
\tag{5.1}
\]

Its exact dual value is

\[
 D_{\rm frac}
 =\max_{0\le\alpha_t\le1}
 \left[
   \sum_tb_t\alpha_t
   -\sum_c\max_{g\in\Gamma_s}
                 \sum_{t\in\mathcal S(c,g)}\alpha_t
 \right].
\tag{5.2}
\]

### Theorem 5.1 (affine-average Hall expansion)

With \(p_t=2^{q(t)}/\binom{s}{q(t)}\) and
\(d_t=|\mathscr C(t)|\),

\[
 \boxed{
 D_{\rm frac}\le\sum_t(b_t-p_td_t)_+.}
\tag{5.3}
\]

Consequently the exact weighted cuts

\[
 \sum_tb_t\alpha_t
 \le\sum_c\max_g\sum_{t\in\mathcal S(c,g)}\alpha_t
 \qquad(0\le\alpha\le1)
\tag{5.4}
\]

all hold if \(p_td_t\ge b_t\) for every \(t\).

#### Proof

For a fixed cell and fixed nonnegative \(\alpha\), maximum is at least
average:

\[
 \max_g\sum_{t\in\mathcal S(c,g)}\alpha_t
 \ge {1\over|\Gamma_s|}
      \sum_{g\in\Gamma_s}
      \sum_{t\in\mathcal S(c,g)}\alpha_t.
\tag{5.5}
\]

By Theorem 4.2, a target in a candidate cell occurs in the fraction \(p_t\)
of that cell's menu, and a target outside a candidate cell never occurs.
Summing (5.5) over cells gives

\[
 \sum_c\max_g\sum_{t\in\mathcal S(c,g)}\alpha_t
 \ge\sum_tp_td_t\alpha_t.
\tag{5.6}
\]

Substitution in (5.2), followed by \(0\le\alpha_t\le1\), yields

\[
 D_{\rm frac}
 \le\max_{0\le\alpha\le1}
      \sum_t(b_t-p_td_t)\alpha_t
 =\sum_t(b_t-p_td_t)_+.
\tag{5.7}
\]

This proves the theorem.  \(\square\)

The candidate degrees have the exact first moment

\[
 \sum_{T}d_q^\epsilon(T)
 ={G\over2^s}\binom sq2^{s-q}
 =G{\binom sq\over2^q}.
\tag{5.8}
\]

Hence

\[
 \sum_Tp_{s,q}d_q^\epsilon(T)=G,
 \qquad
 {1\over N_q^\epsilon}\sum_Tp_{s,q}d_q^\epsilon(T)
 ={G\over N_q^\epsilon}.
\tag{5.9}
\]

Thus (5.3) asks for a lower-tail theorem at the correct mean scale; it does
not waste a constant in the total supply.  But (5.9) alone does not imply
(0.8).  A target-dependent candidate set contains at most one cell from
each fixed packet, so unconditional balance of the group labels over all
cells does not imply balance on those candidate transversals.

An orthogonal array can be used in Theorem 5.1 in either of two precise
ways.

* If it is a face-regular sub-menu in every cell, with the same incidence
  fraction \(p_t\), the averaging proof (5.5)--(5.7) is unchanged.
* If one row is assigned integrally to each cell, ordinary global OA
  marginals give no weighted Hall theorem.  The needed statistic is the
  target-fibre load

  \[
   \sum_{c\in\mathscr C(t)}
    \mathbf1_{\{g_c^{-1}R_c(t)\in\mathcal A_{q(t)}(F_s)\}},
  \tag{5.10}
  \]

  simultaneously for every physical target.  Requiring (5.10) to meet all
  demands is the literal outer assignment problem itself.

## 6. Proved boundary and adversarial audit

The following distinctions are essential.

1.  Theorems 2.1, 3.1, and 4.1 and Corollary 4.2 of the original
    context-array note remain valid for what they state: exact factorhood
    and macro owner-start counts for the uniform-order Hamming factor.  The
    invalid inference is to attach packet-wide growing-depth face
    injectivity to that same factor.  Equations (2.9)--(2.12), or the
    elementary support bound (0.2), rule this out.

2.  Theorem 3.2 repairs the combination without weakening exact ownership.
    It uses the recursive factor in every cell and is literally injective at
    both shadows.  What it balances is the actual macro-support
    multiplicity.  It does not produce one common macro word in a cell and
    does not control arbitrary weights on fine physical targets.

3.  Formula (4.4) shows why even the full block-permutation menu can be
    nonuniform: its degree depends on the complete nine-state histogram of
    the candidate face.  Formula (4.13) shows why adding translations
    requires almost-full OA strength at shallow depth.

4.  Theorem 5.1 is a fractional weighted-Hall theorem.  It neither rounds
    one menu choice per cell nor controls the long-cycle collars after
    different outer packets are assembled.  The condition in (0.8) is
    sufficient, not asserted necessary.

5.  The common-order cut, Theorem 2.2, is fully statewise and global: it
    sums the maximum possible number of distinct physical targets over all
    owner cells, so cross-packet coincidences can only decrease its right
    side.  It closes every route which keeps one common cyclic direction
    word per cell, regardless of how strongly the cell orders are
    orthogonally balanced.

The smallest explicit additional hypothesis used by the affine-average
proof is the physical candidate-degree lower-tail estimate

\[
 \boxed{
 \sum_{q\le H}\sum_{\epsilon=\pm}\sum_T
 \left(
   b_q^\epsilon(T)
   -{2^q\over\binom sq}d_q^\epsilon(T)
 \right)_+=o(W),}
\tag{6.1}
\]

for an owner-disjoint canonical packet atlas, followed by a one-sided
integral rounding theorem respecting the inseparable atoms (4.17) and the
common all-depth choice.  Condition (6.1) is sufficient rather than
necessary; without it, the exact minimal fractional hypothesis is the full
cut system (5.4).  The macro array proves neither clause.  No claim of MWB
or of the constant-one conjecture is made.
