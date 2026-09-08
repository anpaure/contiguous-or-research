# Lane K10: a positive Catalan-cylinder rebundling and an all-depth orbit menu

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver,
computer experiment, or long local job is used.

## 0. Outcome

Put

\[
 n=2m+1,\qquad C_j=\operatorname{Cat}_j,\qquad
 B=C_m,\qquad W=nB,
\]

and, for fixed \(A>0\),

\[
 H=\lceil A\sqrt m\rceil,\qquad
 N_q=\binom n{m-q},\qquad
 W=c_qN_q+\rho_q,\qquad 0\le \rho_q<N_q.
\]

All assertions below are for sufficiently large \(m\), so in particular
every displayed Catalan suffix has nonnegative semilength.

This report gives a positive answer to the orbit-design part of the lane and
an unconditional literal multidepth rebundling theorem.

### A. A literal positive-density dependent rebundling

The canonical size-two \((2\ 3)\)-components can be signed once, with one
common integral choice through all depths \(q\le H\), so that every certified
Catalan suffix cylinder is split as evenly as integrality permits.  The
signing is obtained from a laminar totally unimodular matrix, not from
independent rounding.  It switches

\[
 \left(\frac1{16}+o(1)\right)B
\]

wreath rows and makes the piecewise root map nontrivial on

\[
 \left(\frac1{16}+o(1)\right)W
\]

middle roots.  Every certified lower private arm, and simultaneously its
complementary upper arm, has signed discrepancy at most one at every
\(q\le H\).

This is an actual path to one literal integral exact factor.  The assertion
concerns the certified tagged arms in the audited four-arm formula; it does
not assert that untagged occurrences have disappeared from the same targets.

### B. One fixed \(O(H)\)-colour tree releases the private hierarchy at all depths

Set

\[
 s=\left\lceil\frac{3H}{4}\right\rceil.
\]

There is one fixed transposition forest of exactly

\[
 u=2s+2H+5\le \frac72H+7
\]

colours whose generated group is

\[
 G=\operatorname{Sym}(\mathcal U)\times
   \operatorname{Sym}(\{\beta_s,\gamma_s\}).
\]

At depth \(H\) it consists of protected internal paths, one
always-in--to--always-out exit edge, and the
\(\beta_s\gamma_s\)-edge; at shallower depths part of the large out-atom has
variable membership.  For every \(q\le H\), every orbit of the certified
shifted Catalan tokens nevertheless has exponentially more target capacity
than tagged mass.  More precisely the capacity-to-mass ratio is at least

\[
 2\exp(\delta_0H/2),
\]

where

\[
 \delta_0=
 \frac72\log\frac72-\frac34\log\frac34
 -\frac{11}{4}\log\frac{11}{4}-\log4>0.
\]

The allocations at different depths can be coupled: one group element is
assigned to each two-row packet and routes all of that packet's marked
occurrences simultaneously.  Thus the result is not a collection of
independent rankwise matchings.

At depth \(H\), the pre-exit private factorial certificate still grows as
\(4^{H-s}/\operatorname{poly}(m)\), hence exponentially.  The tree therefore
escapes a genuinely divergent cage, rather than a certificate that was
already negligible on its own factorial scale.

The orbit allocation is integral and packet-coherent.  Its lift to a path of
literal complete-component cuts has one explicit sufficient condition:
fresh ownership components must be monochromatic in the prescribed packet
bit at each stage.  That physical condition is not proved here.

### C. The same positive construction has a connected seam-rich menu

For the literal factor in A, a Johnson-spectral boundary argument supplies a
near-perfect matching \(\mathcal R_m\) of coordinate transpositions carrying
at least

\[
 \left(\frac{11}{128}-o(1)\right)W
\]

distinct genuine nonlocal commutator seams in total.  The carrier forest in
B extends to a Hamilton path \(P_m\) on \([n]\).  Therefore

\[
 \mathcal O_m=P_m\cup\mathcal R_m
\]

has

\[
 |\mathcal O_m|\le 3m,\qquad
 \Delta(\mathcal O_m)\le3,\qquad
 \langle\mathcal O_m\rangle=S_n.
\]

Consequently every rank layer is one final coordinate-group orbit.  The
private-orbit obstruction, and indeed every proper coordinate-profile
invariant, is absent for this menu.  The seams are literal fresh-overlay
seams; the statement does not confuse seams with distinct recomputed
ownership components.

### D. A charged near-TU switch theorem

The K8 all-depth signing theorem extends to arbitrary bad invariant target
sets.  If their actual mass and cardinality have weighted total \(o(W)\),
they may have completely incompatible pair totals; the common integral
signing still gives \(J_A=o(W)\).  This removes the earlier unnecessary
floor-compatibility assumption on deleted rows.

Together, A--D settle the private-orbit design constraint and give a literal
positive-density multidepth rebundling.  They do not yet prove
\(J_A=o(W)\): the remaining physical theorem is to quotient the coherent
packet routes by the freshly recomputed complete ownership components, or to
verify the charged near-TU hypotheses for one seam-rich menu overlay.

---

## 1. The laminar half-packet theorem

### 1.1 The certified packet ledger

Put

\[
 M=m-2,\qquad \tau=(2\ 3).
\]

For every \(R\in\mathcal D_M\), the canonical MSW factor has the audited
complete size-two \(\tau\)-component

\[
 K_R=\{1100R,1010R\}.                                \tag{1.1}
\]

The components in (1.1) are pairwise row-disjoint, and switching any
subfamily gives a literal integral exact middle wreath factor.

Fix \(1\le q\le H\).  If

\[
 R=UV,\qquad U\in\mathcal D_q,\quad V\in\mathcal D_{M-q},
\]

the exact four-arm identity contains a marked lower occurrence whose two
possible targets are

\[
 X_{q,V}=\{2,n\}\cup
       \bigl(4+2q+\operatorname{Down}(V)\bigr),
 \qquad
 Y_{q,V}=\tau X_{q,V}.                               \tag{1.2}
\]

Because \(s=0<q\), the audited \(q>s\) marker case applies: the positive
even-suffix arm contains \(n\), while the negative even-prefix arm and both
odd arms omit \(n\).  Thus each \(U\) contributes an uncancelled
\(+1/-1\) dipole on \(\{X_{q,V},Y_{q,V}\}\), with the same orientation.
The canonical side places the marked token at one of these two targets, and
switching \(K_R\) moves it to the other.  Complementation gives a marked
upper occurrence with the same switch bit.

Only this tagged occurrence statement is used below.  Same-sign untagged
arms may also hit a target in (1.2).

For \(V\in\mathcal D_{M-q}\), define the suffix cylinder

\[
 \mathscr C(q,V)={UV:U\in\mathcal D_q\}
 \subseteq\mathcal D_M.                              \tag{1.3}
\]

It has cardinality

\[
 |\mathscr C(q,V)|=C_q.                              \tag{1.4}
\]

### 1.2 Laminarity

#### Lemma 1.1

The family

\[
 \mathscr L={\mathcal D_M\}\cup
 \{\mathscr C(q,V):1\le q\le H,
 V\in\mathcal D_{M-q}\}                             \tag{1.5}
\]

is laminar.

#### Proof

At a fixed \(q\), distinct suffix cylinders are disjoint.  Suppose
\(q\le q'\) and two cylinders meet.  For a word in their intersection,

\[
 UV=U'V',\qquad
 U\in\mathcal D_q,\quad U'\in\mathcal D_{q'}.
\]

Writing \(U'=UA\) and \(V=AV'\), the intervening word \(A\) begins just
after the Dyck prefix \(U\) has returned to height zero and ends when
\(U'\) returns to height zero.  Hence \(A\) is itself Dyck.  For every
\(\widetilde U\in\mathcal D_q\), the concatenation
\(\widetilde U A\) lies in \(\mathcal D_{q'}\).  Therefore

\[
 \mathscr C(q,V)\subseteq\mathscr C(q',V').
\]

Thus intersecting members are nested.  \(\square\)

#### Lemma 1.2

Let \(A\) be the \(0/1\) incidence matrix of \(\mathscr L\) against the
ground set \(\mathcal D_M\).  Then \(A\) is totally unimodular.

#### Proof

Take an arbitrary subfamily of rows.  In its inclusion forest, give a row
sign \(+1,-1,+1,\ldots\) according to its depth.  For a fixed column
\(R\), the selected laminar sets containing \(R\) form a chain.  Their
alternating signed sum is therefore \(0,+1\), or \(-1\).  The
Ghouila--Houri criterion proves total unimodularity.  \(\square\)

### 1.3 One common integral half-signing

#### Theorem 1.3 (literal positive-density all-depth rebundling)

There is a vector

\[
 x=(x_R)_{R\in\mathcal D_M}\in\{0,1\}^{\mathcal D_M}
\]

such that

\[
 \left\lfloor\frac{|L|}{2}\right\rfloor
 \le \sum_{R\in L}x_R
 \le \left\lceil\frac{|L|}{2}\right\rceil
 \qquad(L\in\mathscr L).                             \tag{1.6}
\]

Switch exactly the complete components \(K_R\) with \(x_R=1\).  The
resulting family \(F^{\mathrm{lam}}_m\) is a literal integral exact factor.
For every \(q\le H\) and every \(V\in\mathcal D_{M-q}\), its two marked
lower token counts on (1.2) differ by at most one.  The same assertion holds
simultaneously for the complementary marked upper tokens.

Moreover the number of switched wreath rows is

\[
 2\sum_Rx_R=C_{m-2}+O(1)
 =\left(\frac1{16}+o(1)\right)B,                     \tag{1.7}
\]

and the number of genuinely moved middle owners is

\[
 (2n-4)\sum_Rx_R
 =\left(\frac1{16}+o(1)\right)W.                     \tag{1.8}
\]

#### Proof

Consider the polytope

\[
 \begin{split}
 \mathcal P=\{z\in[0,1]^{\mathcal D_M}:&
 \lfloor |L|/2\rfloor\le z(L)\le\lceil |L|/2\rceil\\
 &\text{for every }L\in\mathscr L\}.
 \end{split}                                         \tag{1.9}
\]

The half-vector belongs to \(\mathcal P\).  By Lemma 1.2, stacking the
laminar inequalities with \(I\) and \(-I\) leaves a TU constraint matrix.
The right sides are integral, so \(\mathcal P\) has an integral vertex
\(x\).  This proves (1.6).

On the cylinder \(\mathscr C(q,V)\), the marked counts after switching are

\[
 |\mathscr C(q,V)|-x(\mathscr C(q,V)),
 \qquad x(\mathscr C(q,V)).                           \tag{1.10}
\]

Their difference has absolute value at most one by (1.6).  The same bit
controls the complementary upper token, proving the simultaneous assertion.

The root constraint \(L=\mathcal D_M\) gives

\[
 \sum_Rx_R=\frac12C_{m-2}+O(1).
\]

Each switched component replaces two wreath rows.  The exact Catalan ratio
is

\[
 \frac{C_{m-2}}{C_m}
 =\frac{m(m+1)}{4(2m-1)(2m-3)}\longrightarrow\frac1{16},
\]

which proves (1.7).  In one packet, exactly \(2n-4\) middle roots are
genuinely moved by \(\tau\).  This proves (1.8).  \(\square\)

### 1.4 Exact multidepth charge of the marked ledger

The number of marked lower tokens at depth \(q\) is

\[
 C_qC_{m-q-2}.
\]

Therefore Catalan convolution gives

\[
 \sum_{q=1}^{H}C_qC_{m-q-2}
 \le \sum_{q=0}^{m-2}C_qC_{m-q-2}
 =C_{m-1}.                                           \tag{1.11}
\]

Including the complementary upper copy doubles this.  Since \(c_q\ge1\),
the entire weighted marked ledger is at most

\[
 2C_{m-1}=\left(\frac12+o(1)\right)B=o(W).           \tag{1.12}
\]

Thus the dependent signing beats the independent cylinder discrepancy
simultaneously, while its complete marked residue is already negligible on
the constant-one scale.  The content of Theorem 1.3 is the literal
positive-density rebundling and the common all-depth integral choice, not a
claim that (1.12) alone balances the rest of the factor.

---

## 2. A fixed orbit tree for the entire shifted private hierarchy

### 2.1 Common membership atoms

Put

\[
 s=\left\lceil\frac{3H}{4}\right\rceil,
 \qquad d_q=m-s-q-2,
 \qquad 1\le q\le H.                                \tag{2.1}
\]

Let

\[
 P_s=1^s0^s,\qquad
 \beta_s=2s+2,\qquad \gamma_s=2s+3.                 \tag{2.2}
\]

For \(V\in\mathcal D_{d_q}\), define

\[
 \mathcal C_{q,V}
 =\mathsf B(P_s)\cup\{n\}\cup
   \bigl(2s+4+2q+\operatorname{Down}(V)\bigr),       \tag{2.3}
\]

and the private pair

\[
 S_{q,V}=\mathcal C_{q,V}\cup\{\beta_s\},
 \qquad
 T_{q,V}=\mathcal C_{q,V}\cup\{\gamma_s\}.         \tag{2.4}
\]

The shifted packet family consists of

\[
 \{P_s1100R,P_s1010R\},\qquad
 R\in\mathcal D_{m-s-2}.                             \tag{2.5}
\]

For every factorization

\[
 R=UV,\qquad U\in\mathcal D_q,\quad V\in\mathcal D_{d_q},
\]

the audited four-arm formula supplies one certified marked occurrence on the
pair (2.4), with a common orientation over all \(U\).  Thus every \(V\)
has exactly \(C_q\) certified tagged occurrences.  Again, this is a tagged
subledger, not an upper bound on the complete unlabelled load of (2.4).

Let

\[
 \mathcal I_s^+=\mathsf B(P_s)\cup\{n,2m\},
 \qquad a=|\mathcal I_s^+|=s+2.                      \tag{2.6}
\]

The last step of every nonempty Dyck word is down, so \(2m\) belongs to
every target in (2.4).  The first step is up.  If
\(\mathcal Z_{s,q}\) is the usual shifted always-out atom, put

\[
 \mathcal Z_{s,q}^+
 =\mathcal Z_{s,q}\cup\{2s+2q+5\}.                  \tag{2.7}
\]

Then

\[
 |\mathcal Z_{s,q}^+|=s+2q+3,\qquad
 \mathcal Z_{s,q}^+\subseteq\mathcal Z_{s,H}^+.      \tag{2.8}
\]

Define

\[
 \mathcal U=\mathcal I_s^+\sqcup\mathcal Z_{s,H}^+,
 \qquad
 u=|\mathcal U|=2s+2H+5,                             \tag{2.9}
\]

and

\[
 E_s=\{\beta_s,\gamma_s\}.
\]

At depth \(q\), put

\[
 \mathcal B_q=\mathcal Z_{s,H}^+\setminus
               \mathcal Z_{s,q}^+,
 \qquad L_q=|\mathcal B_q|=2(H-q).                  \tag{2.10}
\]

Every target in (2.4) contains all \(a\) points of \(\mathcal I_s^+\),
none of \(\mathcal Z_{s,q}^+\), exactly one point of \(E_s\), and some
number

\[
 k=|S_{q,V}\cap\mathcal B_q|
  =|T_{q,V}\cap\mathcal B_q|.                       \tag{2.11}
\]

### 2.2 The menu

Choose a path spanning \(\mathcal I_s^+\), a path spanning
\(\mathcal Z_{s,H}^+\), one edge joining their endpoints, and the edge
\(\beta_s\gamma_s\).  Call this forest \(\mathcal F_H\).  It has exactly

\[
 (a-1)+(|\mathcal Z_{s,H}^+|-1)+1+1=u              \tag{2.12}
\]

distinct transposition colours and generates

\[
 G=\operatorname{Sym}(\mathcal U)\times
   \operatorname{Sym}(E_s).                          \tag{2.13}
\]

The \(\mathcal I_s^+\)-path is protected at every displayed depth.  The
\(\mathcal Z_{s,H}^+\)-path is wholly protected at depth \(H\); at depth
\(q<H\), its subedges internal to \(\mathcal Z_{s,q}^+\) are protected,
whereas the coordinates in \(\mathcal B_q\) have variable membership.  The
single joining edge is the prescribed always-in--to--always-out first exit
for the divergent depth-\(H\) cage.

Since \(s\le3H/4+1\),

\[
 |\mathcal F_H|=u\le\frac72H+7.                     \tag{2.14}
\]

### 2.3 Exact orbit capacity

#### Theorem 2.1 (uniform all-depth orbit release)

Fix \(q\le H\), an outside-\((\mathcal U\cup E_s)\) trace, and an integer
\(k\) as in (2.11).  The number of Dyck indices \(V\) whose private target
lies in this \(G\)-orbit is at most

\[
 \binom{L_q}{k}.                                     \tag{2.15}
\]

The target orbit has exactly

\[
 Q_{q,k}=2\binom{u}{a+k}                             \tag{2.16}
\]

elements, whereas its certified tagged mass is at most

\[
 R_{q,k}=C_q\binom{L_q}{k}.                          \tag{2.17}
\]

Uniformly for every \(q\le H\),

\[
 \boxed{
 \frac{Q_{q,k}}{R_{q,k}}
 \ge2\exp(\delta_0H/2)
 }                                                    \tag{2.18}
\]

for all sufficiently large \(m\), where \(\delta_0\) is the positive
constant in Section 0.

#### Proof

The down-step set determines \(V\).  Once the target outside
\(\mathcal U\) is fixed, the only freedom is the choice of its \(k\)
members of \(\mathcal B_q\), proving (2.15).

The group in (2.13) is transitive on the \((a+k)\)-subsets of
\(\mathcal U\), and independently interchanges \(\beta_s,\gamma_s\).
This proves (2.16).  There are \(C_q\) certified prefix packets per Dyck
index, proving (2.17).

Vandermonde's identity, retaining only its \(k\)-term, gives

\[
 \binom{u}{a+k}
 \ge
 \binom{u-L_q}{a}\binom{L_q}{k}
 =
 \binom{2s+2q+5}{s+2}\binom{L_q}{k}.                \tag{2.19}
\]

It remains to bound the first factor.  Put

\[
 \alpha=s/H,\qquad x=q/H.
\]

The entropy exponent of \(\binom{2s+2q}{s}/4^q\), divided by \(H\), is

\[
 f_\alpha(x)=
 (2\alpha+2x)\log(2\alpha+2x)
 -\alpha\log\alpha
 -(\alpha+2x)\log(\alpha+2x)
 -x\log4.                                            \tag{2.20}
\]

Its derivatives have signs

\[
 \frac{\partial f_\alpha}{\partial x}
 =2\log\frac{\alpha+x}{\alpha+2x}\le0,              \tag{2.21}
\]

and

\[
 \frac{\partial f_\alpha}{\partial\alpha}
 =\log\frac{4(\alpha+x)^2}{\alpha(\alpha+2x)}>0.     \tag{2.22}
\]

Since \(\alpha\ge3/4\) and \(0<x\le1\), the minimum occurs at
\((\alpha,x)=(3/4,1)\) and equals \(\delta_0>0\).

The standard entropy lower bound for a binomial coefficient loses only
\(O(\log H)\).  Also

\[
 \binom{2s+2q+5}{s+2}\ge\binom{2s+2q}{s}.
\]

Consequently, uniformly in \(q\le H\),

\[
 \binom{2s+2q+5}{s+2}
 \ge \exp(\delta_0H/2)4^q                            \tag{2.23}
\]

for large \(m\).  Since \(C_q\le4^q\), equations
(2.16)--(2.19) prove (2.18).  \(\square\)

### 2.4 One group element per packet

Theorem 2.1 is stronger than Hall for separate depths.

#### Theorem 2.2 (coherent multidepth packet allocation)

For every shifted packet \(R\in\mathcal D_{m-s-2}\), one can choose a
single group element \(g_R\in G\) so that, at every depth \(q\le H\), all
certified lower marked occurrences have pairwise distinct images.  The same
choices simultaneously make all complementary upper marked occurrences
pairwise distinct.

In particular the certified tagged load is \(0/1\) at every depth, and hence
embeds below an exact \(c_q/c_q+1\) quota vector because \(c_q\ge1\).

#### Proof

Order the shifted packets arbitrarily and assign their group elements
greedily.  Consider the next packet.  It carries at most one marked lower
and one marked upper occurrence per depth, hence at most \(2H\) tags.

For one tag, let \(Q\) be its target orbit and let \(F\subset Q\) be the
destinations already used by earlier packets in that orbit.  For uniform
\(g\in G\), transitivity gives

\[
 \Pr(gX\in F)=\frac{|F|}{|Q|}.
\]

The total number of source packets in that orbit is at most the quantity
\(R_{q,k}\) in (2.17), so Theorem 2.1 gives

\[
 \frac{|F|}{|Q|}\le\frac12\exp(-\delta_0H/2).
\]

Complementation bijects every lower orbit class with its corresponding upper
orbit class and preserves the ratio \(Q_{q,k}/R_{q,k}\).  Hence the same
forbidden-fraction bound holds for an upper tag.  By the union bound, the
fraction of group elements forbidden by any of the packet's tags is at most

\[
 H\exp(-\delta_0H/2)<1                              \tag{2.24}
\]

for large \(m\).  Choose an allowed \(g_R\).  Induction completes the
assignment.  Distinct tags within one packet remain distinct under a
permutation.  \(\square\)

This greedy proof, rather than a direct sum of rankwise matching matrices,
is what supplies the common cross-depth packet quantifier.

### 2.5 The divergent cage is genuinely opened

At depth \(H\), the shifted AB8/K9 private certificate with this value of
\(s\) has normalized factorial lower term

\[
 \frac{4^{H-s}}{\operatorname{poly}_A(m)}.
\]

Because \(H-s=H/4+O(1)\), this diverges.  Before the cross edge, the
protected internal paths cannot change the private orbit totals.  After the
cross edge, Theorems 2.1--2.2 place every certified token on a distinct
available target, simultaneously through all depths.  Thus the old private
certificate forces no positive quota-capacity violation and no tagged-token
collision in the **tagged orbit-capacity relaxation** after the menu is
opened.

This last phrase is essential.  It does not say that the complete untagged
load of an exact factor has \(O_q=\Phi_q=0\).

The full fixed shifted carrier in (2.5) has only

\[
 2C_{m-s-2}
\]

wreath rows.  Its total two-sided all-depth weighted occurrence mass is at
most

\[
 4HnC_{m-s-2}=o(W),                                  \tag{2.25}
\]

because, uniformly for \(s=O(\sqrt m)\),

\[
 \frac{C_{m-s-2}}{C_m}=O_A(4^{-s}).
\]

Thus this entire carrier may be reserved in a constant-one construction at
an \(o(W)\) action cost.  Equation (2.25) is an occurrence-mass or
path-action charge; it is not an assertion that the target support of the
carrier receives no untagged load from other rows.

---

## 3. A seam-rich connected orbit menu on a literal prepared factor

### 3.1 The selected root set is a one-design

Let \(x\) be the laminar signing from Theorem 1.3, and put

\[
 k=\sum_Rx_R=\frac12C_{m-2}+O(1).
\]

For a selected packet \(K_R\), let \(U_R\) be the union of the \(2n\)
middle roots owned by its two old wreath rows.  Define

\[
 \mathcal E=\bigsqcup_{x_R=1}U_R,
 \qquad
 p=\frac{|\mathcal E|}{W}=\frac{2k}{B}\longrightarrow\frac1{16}. \tag{3.1}
\]

Every wreath row contains each coordinate in exactly \(m\) of its \(n\)
middle windows.  Hence \(\mathcal E\) is a \(1\)-design.  Its centered
indicator on \(J(n,m)\) has no harmonics of degrees zero or one.

Let \(\partial\mathcal E\) be its unordered Johnson edge boundary.  The
degree-two Johnson Laplacian eigenvalue is \(2(n-1)\), so

\[
 |\partial\mathcal E|
 \ge2(n-1)Wp(1-p).                                   \tag{3.2}
\]

### 3.2 Removing nongenuine boundary roots

The set \(\mathcal E\) is \(\tau\)-invariant.  Exactly four roots in each
selected \(2n\)-root packet are fixed by \(\tau=(2\ 3)\).  The Johnson
degree is

\[
 m(m+1)=\frac{n^2-1}{4}.
\]

Deleting every boundary edge incident with one of these fixed roots removes
at most

\[
 4k\,m(m+1)
 =\frac{pW(n^2-1)}{2n}.                              \tag{3.3}
\]

edges.  Combining (3.1)--(3.3) leaves

\[
\begin{aligned}
 &2(n-1)Wp(1-p)-\frac{pW(n^2-1)}{2n}\\
 &\hspace{25mm}=
 \left(\frac{11}{128}-o(1)\right)nW               \tag{3.4}
\end{aligned}
\]

boundary edges whose endpoint in \(\mathcal E\) is genuinely moved by
\(\tau\).

Switching the selected packets defines the piecewise root involution
\(\alpha\), equal to \(\tau\) on \(\mathcal E\) and to the identity off
\(\mathcal E\).  If a remaining boundary edge is

\[
 X\longleftrightarrow \rho X,\qquad
 X\in\mathcal E,\quad \rho X\notin\mathcal E,
\]

then the pulled-back fresh relation contains

\[
 \alpha(\tau X)=X,\qquad
 \alpha(\rho X)=\rho X.
\]

Because \(\tau X\ne X\), its transition is not the original global
\(\rho\)-transition.  It is a genuine piecewise-commutator seam.  Distinct
boundary edges give distinct fresh seams.

### 3.3 A matching of productive colours

Every Johnson edge has the unique coordinate-transposition colour given by
its symmetric difference.  Since \(n\) is odd, the edges of the coordinate
complete graph \(K_n\) partition into \(n\) near-perfect matchings.  Summing
the seam counts in (3.4) over these \(n\) colour classes gives:

#### Theorem 3.1

There is a near-perfect matching \(\mathcal R_m\) of \(m\) coordinate
transpositions such that, in total, its colours support at least

\[
 \boxed{
 \left(\frac{11}{128}-o(1)\right)W
 }
                                                               \tag{3.5}
\]

distinct genuine fresh commutator seams of the literal factor
\(F_m^{\mathrm{lam}}\).

The transposition congestion of \(\mathcal R_m\) is exactly one.  Equation
(3.5) is a seam count, not a distinct-component count.

All seams in (3.5) are certified in their separate fresh colour overlays at
the same prepared factor.  The theorem does not assert that a seam for one
matching colour persists after an earlier matching colour has actually been
cut.

### 3.4 Completing the orbit menu

Choose the two paths in Section 2 so that their joining edge concatenates
them into one path on \(\mathcal U\).  Together with the
\(\beta_s\gamma_s\)-edge they form a linear forest.  Extend this forest to
a Hamilton path \(P_m\) of the coordinate complete graph.  Put

\[
 \mathcal O_m=P_m\cup\mathcal R_m.                   \tag{3.6}
\]

Then

\[
 |\mathcal O_m|\le(n-1)+m=3m,
 \qquad \Delta(\mathcal O_m)\le3.                   \tag{3.7}
\]

The transpositions along a connected coordinate graph generate the full
symmetric group, so

\[
 \langle\mathcal O_m\rangle=S_n.                    \tag{3.8}
\]

Thus every rank-\(r\) target layer is one group orbit.  The menu contains
the all-depth private release tree of Section 2 and the bounded-congestion
seam reservoir of Theorem 3.1.

These structures coexist with the literal laminar preparation.  For
\(s\ge3\), every shifted carrier index \(P_s1100R\) or \(P_s1010R\) begins
with \(111\), whereas every \(s=0\) packet index begins with \(1100\) or
\(1010\).  The two row families are therefore disjoint, so the laminar
preparation leaves every shifted carrier row and tag literally untouched.
Independently, every shifted private target contains \(\{2,3\}\), so every
preliminary \((2\ 3)\)-cut fixes its full target load.

---

## 4. Exact literal lift of a coherent orbit allocation

The orbit allocation can be written with one common finite word.

Order the vertices of the path on \(\mathcal U\) as
\(v_1,\ldots,v_u\), and let

\[
 s_i=(v_i\ v_{i+1}).
\]

The word

\[
 \mathbf w_0=(s_1)(s_2s_1)\cdots
 (s_{u-1}s_{u-2}\cdots s_1)                          \tag{4.1}
\]

is a reduced word for the longest element of \(S_u\).  Every permutation
of \(\mathcal U\) is a subword of (4.1): this is the elementary subword
form of bubble sorting, proved inductively by inserting the largest symbol.
Appending one optional \((\beta_s\gamma_s)\)-slot gives a common word
\(\mathbf W\) of length

\[
 \binom u2+1=O_A(m)                                  \tag{4.2}
\]

whose subwords represent every element of \(G\).

For the coherent assignment in Theorem 2.2, fix for each packet \(R\) a
subword bit vector

\[
 b_R(t)\in\{0,1\},\qquad 1\le t\le|\mathbf W|,
\]

representing \(g_R\).

#### Lemma 4.1 (component-monochromatic lift)

Suppose that, at every stage \(t\), every freshly recomputed ownership
component for the current colour of \(\mathbf W\) is monochromatic in
\(b_R(t)\) among all routed packet rows it contains.  Give a component
containing no routed packet row bit zero, and switch exactly the components
with common bit one.  Then every intermediate family is a literal
integral exact middle wreath factor, and every routed packet follows its
prescribed partial subword.  The terminal factor realizes all coherent
multidepth destinations from Theorem 2.2.

#### Proof

A complete component cut preserves exact middle ownership.  On an
unswitched component, use the identity row transport; on a switched
component, apply the current coordinate transposition to every row.
Monochromaticity makes this choice agree with every packet bit in the
component.  Induction on \(t\) proves that each packet has accumulated
exactly its prescribed subword prefix.  At the end this product is \(g_R\).
\(\square\)

Lemma 4.1 is a sufficient literal lift, not an assumption hidden in the
orbit count.  The unresolved physical question is whether the packet bit
constraints can be made component-monochromatic along one such recomputed
word, or more generally whether their equality quotient retains total
unimodularity.

---

## 5. Charged near-TU signing with arbitrary bad pair totals

This section gives an exact positive switch theorem usable after a menu edge
has produced a fresh transposition overlay.

Fix an exact factor \(F\), a transposition \(\sigma\), and the freshly
recomputed complete ownership components \(K\).  At every depth \(q\), let
\(\mathcal U_q\) be a \(\sigma\)-invariant union of target orbits.  Put

\[
 u_q=|\mathcal U_q|,
 \qquad M_q=\sum_{S\in\mathcal U_q}\mu_q^F(S).        \tag{5.1}
\]

The mass \(M_q\) is invariant under every complete-component signing.

On the complement of \(\mathcal U_q\), assume:

1. every \(\sigma\)-fixed target already has load \(c_q\) or \(c_q+1\);
2. every moved pair has total in
   \(\{2c_q,2c_q+1,2c_q+2\}\);
3. every component leakage coefficient lies in \(\{-1,0,1\}\); and
4. the single matrix obtained by stacking all retained depths, with the same
   component columns, is totally unimodular.

No profile assumption is imposed inside \(\mathcal U_q\).

#### Theorem 5.1 (charged all-depth TU signing)

There is one common integral signing of the complete components such that

\[
 \boxed{
 O_q\le
 \min_{h\in I_q\cap\mathbb Z}
 \frac{M_q+c_qu_q+h+|M_q-c_qu_q-h|}{2}
 \le M_q+(c_q+1)u_q,
 }                                                    \tag{5.2}
\]

where

\[
 I_q=
 \left[
 \max\{0,\rho_q-(N_q-u_q)\},
 \min\{u_q,\rho_q\}
 \right].                                            \tag{5.3}
\]

Consequently,

\[
 \sum_{q\le H}
 \frac{M_q+(c_q+1)u_q}{c_q}=o(W)                    \tag{5.4}
\]

implies \(J_A=o(W)\) for the component-signed exact child factor.

#### Proof

The K8 half-vector polytope on the retained rows is nonempty.  Total
unimodularity gives an integral vertex, so one common signing makes every
retained target exactly \(c_q\) or \(c_q+1\).  Let \(g_q\) be the number
of retained targets having the ceiling value.  Comparing retained total mass
with \(W=c_qN_q+\rho_q\) gives

\[
 g_q=\rho_q-M_q+c_qu_q.                              \tag{5.5}
\]

Choose an integer \(h\in I_q\).  There is a global quota vector with exactly
\(h\) ceiling entries on \(\mathcal U_q\) and \(\rho_q-h\) ceiling entries
off it.  On the retained side, choose its ceiling set nested with the actual
set of size \(g_q\).  The resulting half-\(\ell^1\) cost is

\[
 \frac12|g_q-(\rho_q-h)|
 =\frac12|M_q-c_qu_q-h|.                             \tag{5.6}
\]

On \(\mathcal U_q\), nonnegativity bounds the half-\(\ell^1\) cost by

\[
 \frac12(M_q+c_qu_q+h).                              \tag{5.7}
\]

Adding (5.6)--(5.7) proves the first inequality in (5.2).  Since
\(0\le h\le u_q\), the displayed expression is at most
\(M_q+(c_q+1)u_q\).  Summing proves (5.4).  \(\square\)

Theorem 5.1 is strictly stronger than deleting bad rows while retaining the
old floor-compatible-pair-total hypothesis.  It permits arbitrary invariant
pair totals on the charged target set.  What must be small is its actual
mass and cardinality, not merely the mass of one selected tagged subledger.

---

## 6. Exact constant-one boundary

The following are unconditional and literal.

1. Theorem 1.3 constructs one exact factor obtained by a positive-density
   switch of complete canonical components.  One dependent integral signing
   controls every certified Catalan cylinder at every depth \(q\le H\).

2. Theorems 2.1--2.2 construct one fixed \(O(H)\)-colour orbit tree and one
   packet-coherent integral allocation which removes the entire certified
   shifted private hierarchy from the profile-capacity obstruction at every
   depth.

3. Theorem 3.1 places a \((11/128-o(1))W\) genuine seam reservoir on a
   coordinate matching.  Adding a Hamilton path gives a degree-three menu
   of at most \(3m\) colours which generates \(S_n\).

4. Theorem 5.1 is an exact common-component switch theorem.  It yields
   \(J_A=o(W)\) as soon as one menu overlay has unit/TU leakage off an
   invariant target residue satisfying (5.4), even when the residue has
   arbitrarily bad pair totals.

The one unproved composition is physical rather than orbit-theoretic or
fractional: the coherent packet routes must descend through the identifications
made by the freshly recomputed complete ownership components.  Lemma 4.1
gives an explicit sufficient condition, and Theorem 5.1 gives the exact
near-TU alternative.

Accordingly this report does **not** claim the constant-one theorem.  It does
prove that the private Catalan orbit obstruction is no longer a surviving
constant-one gate: an explicit linear-size palette opens it at all depths,
its tags admit one coherent integral allocation, and its whole fixed carrier
has only \(o(W)\) multidepth action.  The remaining gate is the literal
component quotient for the seam-rich connected menu.

---

## 7. Independent audit record

Two independent proof audits were requested, one for the laminar/spectral
package and one for the orbit-capacity package.  Both passed after the scope
corrections recorded below.

The orbit-capacity audit independently rederived the membership-atom sizes,
the exact orbit size, the Vandermonde factor, the entropy monotonicity, and
the positive constant \(\delta_0\).  It required the following corrections,
all incorporated above:

* \(C_q\) is certified tagged mass, not total private-pair load;
* zero collision is asserted only in the tagged orbit-capacity relaxation;
* one group element per packet comes from the exponential-slack greedy
  argument, not from independent rankwise TU matchings; and
* literal factor realization still requires component-bit coherence or an
  augmented TU theorem.

The laminar/spectral audit independently rederived laminarity, the
Ghouila--Houri signing, the exact half-cardinality constraint, and the
Catalan convolution charge.  It also checked

\[
 |\partial\mathcal E|\ge2(n-1)Wp(1-p),
 \qquad
 4k m(m+1)=\frac{pW(n^2-1)}{2n},
\]

and hence the constants \(11/128\) in (3.4)--(3.5).  It emphasized, as the
text now does, that the laminar theorem balances tagged dipoles rather than
the invariant complete private-pair totals, and that matching-colour seams
are certified in separate overlays without sequential-persistence or
component-dispersion conclusions.

No finite or computational check is used in either audit.
