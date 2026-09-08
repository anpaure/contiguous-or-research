# Candidate degrees and the exact Gram kernel of the independent \(Q_4\) braid cube

Date: 2026-07-26

Method: pure mathematics only.  No Poisson surrogate, independence
heuristic, search, or generic nibble theorem is used.

## 0. Verdict

Consider one Hamming-syndrome \(Q_h\)-cell, with \(h\ge4\), and the
owner-disjoint braid components from the common-phase \(Q_4\) switch.
Every component contains two \(C_{2h}\)'s, hence \(4h\) phase owners, and
has two shores:

\[
\begin{aligned}
 \sigma_0&=1,2,3,4,5,\ldots,h,1,2,3,4,5,\ldots,h,\\
 \sigma_1&=1,4,3,2,5,\ldots,h,1,4,3,2,5,\ldots,h.
                                                               \tag{0.1}
\end{aligned}
\]

The cell has

\[
                         {2^h\over4h}                \tag{0.2}
\]

independent braid components.  Choose one shore independently in every
component.

At a fixed signed depth \(1\le q\le h\), let \(D_\omega(T)\) be the
number of selected phase occurrences having physical target \(T\).
For a component \(C\), let \(n^s_C(T)\) be its target multiplicity on
shore \(s\in\{0,1\}\), and put

\[
 \Delta_C(T)=n^1_C(T)-n^0_C(T),\qquad
 \overline D(T)={1\over2}\sum_C(n^0_C(T)+n^1_C(T)).  \tag{0.3}
\]

If \(\xi_C\in\{-1,1\}\) are independent fair signs, then the complete
candidate-degree law is the exact Rademacher sum

\[
 \boxed{
 D_\omega(T)=\overline D(T)
       +{1\over2}\sum_C\xi_C\Delta_C(T).}             \tag{0.4}
\]

Equivalently, its probability generating function is

\[
 \boxed{
 \mathbb E_\omega z^{D_\omega(T)}
 =\prod_C {z^{\,n_C^0(T)}+z^{\,n_C^1(T)}\over2}.}    \tag{0.5}
\]

The full joint generating function, retaining every target correlation,
is

\[
 \boxed{
 \mathbb E_\omega\prod_Tz_T^{D_\omega(T)}
 =\prod_C{\,\prod_Tz_T^{n_C^0(T)}
             +\prod_Tz_T^{n_C^1(T)}\over2}.}         \tag{0.6}
\]

Thus no marginal products have been used.

The exact centered target Gram kernel is

\[
 \boxed{
 K_q(T,U):=\operatorname {Cov}_\omega(D_\omega(T),D_\omega(U))
 ={1\over4}\sum_C\Delta_C(T)\Delta_C(U).}            \tag{0.7}
\]

In particular,

\[
 \boxed{
 \mathbb E_\omega\sum_T(D_\omega(T)-\overline D(T))^2
 ={1\over4}\sum_C\|\Delta_C\|_2^2.}                 \tag{0.8}
\]

Equivalently,

\[
 \mathbb E_\omega\sum_TD_\omega(T)^2
 =\sum_T\overline D(T)^2+\operatorname {tr}K_q.      \tag{0.8a}
\]

The correction is positive semidefinite.  Thus braid averaging cannot
cancel an existing outer second-moment mode; it only adds the centered
energy quantified below.

The braid cube is nevertheless a sparse edit at each depth.  Define

\[
             \nu_{h,q}=8\min\{2,q,h-q\}.             \tag{0.9}
\]

On one component, the two target-occurrence histograms differ at no more
than \(\nu_{h,q}\le16\) phase owners.  Consequently

\[
 \|\Delta_C\|_1\le2\nu_{h,q}\le32,\qquad
 \|\Delta_C\|_2^2\le2\nu_{h,q}^2\le512.              \tag{0.10}
\]

If each shore is target-injective inside the component, the sharper
bound is

\[
 \Delta_C(T)\in\{-1,0,1\},\qquad
 \|\Delta_C\|_2^2\le2\nu_{h,q}\le32.                 \tag{0.11}
\]

For a global owner mass \(G\) tiled by \(Q_h\)-cells, there are exactly
\(G/(4h)\) braid components.  Hence, at either sign and one depth,

\[
\boxed{\begin{aligned}
 \sum_T|\overline D(T)-D_0(T)|&\le {4G\over h},\\
 \sup_\omega\sum_T|D_\omega(T)-D_0(T)|&\le {8G\over h},\\
 \#\{T:\Delta_C(T)\ne0\text{ for some }C\}&\le {8G\over h},\\
 \operatorname {tr}K_q&\le {32G\over h}.
\end{aligned}}                                      \tag{0.12}
\]

Here \(D_0=\sum_Cn_C^0\) is the unswitched target multiplicity.  Under
componentwise target injectivity, the last constant improves to

\[
                         \operatorname {tr}K_q\le {2G\over h}. \tag{0.13}
\]

Therefore independent braid switches do **not** average out the
negative-binomial or physical-profile lognormal lower tail.  If
\(\mathcal D_q(L)=\sum_T(1-L_q(T))_+\), then the braid-averaged and
unswitched loads obey

\[
 \boxed{
 |\mathcal D_q(\overline D)-\mathcal D_q(D_0)|
 \le {4G\over h}.}                                   \tag{0.14}
\]

Every deterministic braid state also obeys

\[
 \boxed{
 |\mathcal D_q(D_\omega)-\mathcal D_q(D_0)|
 \le {8G\over h}.}                                   \tag{0.14a}
\]

Through \(q\le H\), the total possible change is \(O(GH/h)=o(W)\) in
the packet regime \(G=(1+o(1))W\), \(H/h=o(1)\).  A pre-existing
\(\Theta(W)\) defect at a Gaussian depth therefore survives.

More explicitly, after the complete formal local-label and ambient-order
average, at \(q=A\sqrt m+o(\sqrt m)\),

\[
\begin{aligned}
 {1\over N_q}\mathcal D_q(\overline D_{\rm braid})
 \ge{}&
 \Phi\!\left({14A\over\sqrt{102}}\right)
 -e^{A^2}\Phi\!\left({-20A\over\sqrt{102}}\right)
 -O\!\left({W\over hN_q}\right).
                                                               \tag{0.15}
\end{aligned}
\]

The first two terms have a strictly positive difference.  Hence the
Gaussian lower-tail defect remains \(\Theta(W)\).

## 1. The literal braid cell

The common-phase \(Q_4\) factor has two rows in every shore.  The
unswitched shore has direction word

\[
                         1234\,1234,                 \tag{1.1}
\]

and the switched shore has direction word

\[
                         1432\,1432.                 \tag{1.2}
\]

After adjoining directions \(5,\ldots,h\), or equivalently embedding the
switch in the standard syndrome factor, the two component shores have
the words (0.1).  They have exactly the same \(4h\) owners and the same
phase colouring.  Thus every owner \(X\) has one common phase
\(j\in\mathbb Z_{2h}\) on both shores.

For a sign \(\epsilon\in\{-,+\}\), write

\[
 \tau_{C,s,q}^\epsilon(X)
\]

for the intersection or union target of the \(q\)-edge window starting
at \(X\) on shore \(s\).  Define the occurrence histogram

\[
 n^s_C(T)
 =\#\{X\in V(C):\tau_{C,s,q}^\epsilon(X)=T\}.        \tag{1.3}
\]

No injectivity is assumed in (1.3).  In every shore,

\[
                         \sum_Tn_C^s(T)=4h.          \tag{1.4}
\]

## 2. Exact count of switch-sensitive phases

Index outgoing edge phases by \(\mathbb Z_{2h}\), starting at zero.  The
only direction labels which move between the two words are \(2\) and
\(4\).  In the unswitched word their occurrences are

\[
 P_2=\{1,h+1\},\qquad P_4=\{3,h+3\};                 \tag{2.1}
\]

the switched word interchanges these two occurrence sets.

For a phase \(j\), let

\[
 I_{j,q}=\{j,j+1,\ldots,j+q-1\}\pmod {2h}            \tag{2.2}
\]

be its edge window.  The unordered direction sets on the two shores
agree unless

\[
 |I_{j,q}\cap P_2|\ne|I_{j,q}\cap P_4|.             \tag{2.3}
\]

### Lemma 2.1 (exact phase sensitivity)

The number of phase classes satisfying (2.3) is

\[
                         4\min\{2,q,h-q\}.           \tag{2.4}
\]

Since a component has two owners in every phase class, the number of
owner-starts whose \(q\)-window can change is exactly \(\nu_{h,q}\) from
(0.9).

#### Proof

Membership in \(P_2\) is \(h\)-periodic.  Modulo \(h\), it is the
indicator of a cyclic interval of \(q\) possible starting phases.
Membership in \(P_4\) is the translate of this interval by two.

Two length-\(q\) cyclic intervals in \(\mathbb Z_h\) whose initial
points differ by two have symmetric difference

\[
                         2\min\{2,q,h-q\}.           \tag{2.5}
\]

There are two lifts from \(\mathbb Z_h\) to
\(\mathbb Z_{2h}\), proving (2.4).  Each phase class contains one owner
from each of the two component cycles. \(\square\)

For the protected range \(q\le h/2\), this says

\[
 \nu_{h,1}=8,\qquad
 \nu_{h,q}=16\quad(2\le q\le h/2).                  \tag{2.6}
\]

If (2.3) fails, the start owner and the set of touched directions are the
same on the two shores.  A return-free geodesic trace depends only on
these data, not on the order in which the distinct directions are
touched.  Hence

\[
 \tau_{C,0,q}^\epsilon(X)=\tau_{C,1,q}^\epsilon(X)  \tag{2.7}
\]

for all but the \(\nu_{h,q}\) owner-starts counted above.  This assertion
uses only geodesicity; it does not require target injectivity.

Changing the labels of at most \(\nu\) occurrences changes a histogram
by \(\ell^1\)-distance at most \(2\nu\).  Its positive and negative
parts each have mass at most \(\nu\), so its squared \(\ell^2\)-norm is
at most \(2\nu^2\).  Lemma 2.1 therefore proves (0.10).  If both target
maps are injective, their histograms are zero-one, proving (0.11).

## 3. Exact degree distribution under the braid cube

Let \(\omega_C\in\{0,1\}\) be the independently selected shore of
component \(C\).  By definition,

\[
 D_\omega(T)=\sum_C
 \bigl((1-\omega_C)n_C^0(T)+\omega_Cn_C^1(T)\bigr).
                                                               \tag{3.1}
\]

Putting \(\xi_C=2\omega_C-1\) gives (0.4).  Independence of the
\(\omega_C\)'s gives (0.5), and retaining a separate indeterminate for
every target gives (0.6).

There is a particularly transparent specialization when both shores are
target-injective.  Put

\[
\begin{aligned}
 a_T&=\#\{C:T\in S_C^0\cap S_C^1\},\\
 b_T&=\#\{C:T\in S_C^0\triangle S_C^1\},
\end{aligned}                                        \tag{3.2}
\]

where \(S_C^s\) is the target set on shore \(s\).  Then

\[
 \boxed{
 D_\omega(T)\overset d=
 a_T+\operatorname {Bin}(b_T,1/2).}                 \tag{3.3}
\]

If the braid cube has \(M\) bits, the exact number of cube states in which
\(D_\omega(T)=k\) is

\[
 \boxed{
 2^{M-b_T}\binom{b_T}{k-a_T}.}                       \tag{3.4}
\]

The number of states which hit \(T\) at least once is \(2^M\) when
\(a_T>0\), and

\[
                         2^M(1-2^{-b_T})             \tag{3.5}
\]

when \(a_T=0\).  These are exact binomial identities, not Poisson
approximations.

## 4. Exact second moments and correlations

Taking expectations in (0.4) gives

\[
                         \mathbb E_\omega D_\omega(T)=\overline D(T).
                                                               \tag{4.1}
\]

For two targets \(T,U\), orthogonality of the independent fair signs
gives

\[
\begin{aligned}
 \mathbb E_\omega[D_\omega(T)D_\omega(U)]
 =\overline D(T)\overline D(U)
 +{1\over4}\sum_C\Delta_C(T)\Delta_C(U).             \tag{4.2}
\end{aligned}
\]

This proves (0.7).  On the diagonal,

\[
 \operatorname {Var}_\omega D_\omega(T)
 ={1\over4}\sum_C\Delta_C(T)^2.                     \tag{4.3}
\]

Summing (4.3) proves (0.8).  The collision energy also has the exact
form

\[
\boxed{
 \mathbb E_\omega\sum_TD_\omega(T)(D_\omega(T)-1)
 =\sum_T\bigl(\overline D(T)^2-\overline D(T)\bigr)
  +{1\over4}\sum_C\|\Delta_C\|_2^2.}                \tag{4.4}
\]

Thus the entire extra second moment introduced by the braid randomization
is the positive semidefinite rank-one sum in (0.7).

## 5. Global sparse-edit bounds

A \(Q_h\)-cell contains \(2^h/(4h)\) components and \(2^h\) owners.
Therefore a global owner mass \(G\) contains

\[
                         M={G\over4h}                \tag{5.1}
\]

independent braid bits.  Equations (0.10) and (5.1) give

\[
 {1\over4}\sum_C\|\Delta_C\|_2^2
 \le {1\over4}\cdot512\cdot{G\over4h}
 ={32G\over h},                                     \tag{5.2}
\]

and the injective estimate (0.13) follows similarly from (0.11).

Moreover,

\[
\begin{aligned}
\sum_T|\overline D(T)-D_0(T)|
 &\le {1\over2}\sum_C\|\Delta_C\|_1
 \le {4G\over h},\\
 \sum_T|D_\omega(T)-D_0(T)|
 &\le\sum_C\|\Delta_C\|_1
 \le {8G\over h},\\
 \#\{T:\Delta_C(T)\ne0\text{ for some }C\}
 &\le\sum_C\|\Delta_C\|_1
 \le {8G\over h}.                                   \tag{5.3}
\end{aligned}
\]

The first inequality allows cancellations between different components;
the displayed bound does not assume them.  The second uses that every
nonzero histogram difference is an integer.

Finally, \(x\mapsto(1-x)_+\) is one-Lipschitz.  Applying it pointwise to
(5.3) proves (0.14) and (0.14a).  For the averaged load, summing over the
two signs and \(q\le H\) costs at most

\[
                         {8GH\over h}.               \tag{5.4}
\]

This is \(o(W)\) whenever \(G=(1+o(1))W\) and \(H/h=o(1)\).
For an arbitrary deterministic braid state the corresponding bound is
\(16GH/h=o(W)\).

## 6. Persistence of the two known lower tails

There are two relevant base catalogues.

### 6.1 Fixed first-eligible atlas

At \(q=c\sqrt r+o(\sqrt r)\), \(h=2r\), the normalized base load has the
negative-binomial lognormal limit

\[
 L_q^0(T)\Longrightarrow e^{-c^2+\sqrt2cN}.
                                                               \tag{6.1}
\]

Its one-sided deficit is

\[
 {1\over N_q}\sum_T(1-L_q^0(T))_+
 \longrightarrow2\Phi(c/\sqrt2)-1>0.                \tag{6.2}
\]

Equation (0.14), with \(G/h=o(W)\), gives the same positive limiting
lower bound after averaging all independent syndrome-cell braid switches.
Equation (0.14a) shows that even an adversarial deterministic choice of
all braid bits changes the deficit by only \(o(W)\).

### 6.2 Formal independent local labels and ambient block orders

At \(q=A\sqrt m+o(\sqrt m)\), the fully symmetrized base load satisfies

\[
 \log L_q^0(T)\Longrightarrow
 -{14\over3}A^2+\sqrt{{34\over3}}\,A\,N.             \tag{6.3}
\]

Consequently its normalized deficit is

\[
 \delta_{\rm phys}(A)=
 \Phi\!\left({14A\over\sqrt{102}}\right)
 -e^{A^2}\Phi\!\left({-20A\over\sqrt{102}}\right)>0.
                                                               \tag{6.4}
\]

Since \(N_q/W\to e^{-A^2}\), equations (0.14) and (6.4) prove

\[
 \boxed{
 \sum_T(1-L_q^{\rm braid}(T))_+
 \ge(\delta_{\rm phys}(A)e^{-A^2}-o(1))W.}           \tag{6.5}
\]

Thus even the incompatible all-order average retains a linear Gaussian
defect.  The braid cube changes only \(O(W/h)\) target incidences at that
depth and cannot change this conclusion, whether the bits are averaged or
chosen deterministically.

## 7. Exact surviving possibility

The theorem rules out using independent copies of this one \(Q_4\)
generator as a concentration mechanism.  It does not rule out a
braid-network completion in which overlapping adjacent transpositions
move a positive proportion of the \(2h\) phase positions.

The quantitative requirement is now exact.  To modify a
\(\Theta(W)\) lower-tail cut at one depth, a replacement family must have

\[
 \sum_C\|\Delta_C\|_1=\Omega(W),                    \tag{7.1}
\]

not \(O(W/h)\).  Equivalently, a typical owner-start must lie in
\(\Omega(1)\) switch-sensitive windows at that depth.  Independent
owner-disjoint \(Q_4\) cells expose only \(O(1/h)\) of the starts, so they
miss this threshold by a factor \(\Theta(h)\).

This is the remaining structural escape: a dense overlapping braid
network, together with a new exact owner-partition theorem.  The existing
independent syndrome-cell braid cube has the exact law (0.4)--(0.8) and
cannot average out either known lower-tail defect.
