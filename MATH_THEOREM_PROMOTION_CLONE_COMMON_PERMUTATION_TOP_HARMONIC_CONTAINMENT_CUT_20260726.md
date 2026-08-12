# The promotion clone relaxation has an exact top-harmonic common-permutation containment cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, search, or web
input is used.

## 0. Outcome

Put

\[
 M=m+H,\qquad R=\binom{2m}{M},\qquad T=MR,
 \qquad H=(1+o(1))\sqrt{m\log m},
\tag{0.1}
\]

where \(H\) is either tuned critical crossing height, so that
\(T=(1+o(1))W\). Let

\[
 0\le q=o(\sqrt m),\qquad r=m-q,\qquad \ell=M-r=H+q.
\tag{0.2}
\]

Here \(W=\binom{2m}{m}\). Work in the
mechanical support atlas of
`MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md`.

This note proves that the separate middle and entrance clone Hall
matchings cannot in general be coupled, even after an \(o(W)\) leave.
The obstruction is the first literal growing-degree character.

Index both rows by the start \(a\in\mathbb Z_M\) of the physical
middle owner. If \(J_a\) is its complementary \(H\)-set and \(S_a\)
is its lower rank-\(r\) entrance, then every common cyclic order obeys

\[
             J_a\subseteq C_a:=U\setminus S_a,
             \qquad |C_a|=H+q.
\tag{0.3}
\]

Let \({\cal M}_0\) and \({\cal M}_r\) be any two integral clone Hall
matchings, one in the middle row and one in the entrance row, each
matching \(T-o(W)\) phase clones. There is a conjugate of
\({\cal M}_r\) under \(S_P\times S_{P^c}\) such that, even after an
arbitrary rootwise phase alignment \(\sigma_A\) between the two tables,

\[
 \bigl|\{(A,a):J_{A,a}\subseteq C_{A,\sigma_A(a)}\}\bigr|=o(W),
\tag{0.4}
\]

although the domains of the two matchings overlap in \(T-o(W)\)
clones under every such alignment. More precisely, away from
exponentially few root types, the
conditional containment probability is at most

\[
 \boxed{
 \left(\frac{H+q+4}{M}\right)^H
 =\exp\left(-(1/2+o(1))H\log m\right)
 =m^{-\omega(1)}.}
\tag{0.5}
\]

Consequently every repair of this pair into a common-permutation
coupling must change or discard \(W-o(W)\) paired clone incidences.
Near-perfect separate Hall balance is therefore insufficient by a
linear amount.

The cut is genuinely in the growing Johnson sector. For a fixed
\(\ell\)-set \(C\subset U\), the containment character

\[
                     f_C(J)={\bf1}_{J\subseteq C},
                     \qquad J\in\binom UH,
\tag{0.6}
\]

has exact top-harmonic mass

\[
 \boxed{
 \|P_Hf_C\|_2^2
 =\frac{\left(\binom MH-\binom M{H-1}\right)
             \binom{M-2H}{q}}
            {\binom M{H+q}}>0.}
\tag{0.7}
\]

More generally, every near-top degree \(j=H-s\) has the exact mass

\[
 \boxed{
 \|P_{H-s}f_C\|_2^2
 =\frac{\left(\binom M{H-s}-\binom M{H-s-1}\right)
          \binom{q+s}{s}\binom{M-2H+s}{q}}
        {\binom M{H+q}}
 \quad(0\le s\le H).}
\tag{0.8}
\]

Thus (0.3) is not another degree-zero, degree-one, degree-two, or
profile cut.  In paired-clone variables it is an exact integral support
inequality with a \(W-o(W)\) gap.

This is an obstruction to **arbitrarily coupling the two separate clone
Hall matchings**.  It is not an obstruction to the existence of a
jointly chosen pair of matchings arising from common cyclic orders, and
therefore it does not prove an integrality gap for the original
one-frame-per-top program.

## 1. The exact physical phase alignment

Fix a top \(U\), a labelled cyclic order on it, and an owner phase
\(a\in\mathbb Z_M\). Write \(I(a,s)\) for the cyclic interval of length
\(s\) beginning at \(a\). The middle owner and its omitted set are

\[
X_a=I(a,m),\qquad
J_a=U\setminus X_a=I(a+m,H).
\tag{1.1}
\]

In the rooted mechanical notation, the matched middle target is
\(D_a=A\cup J_a=[2m]\setminus X_a\). Thus passing between the physical
middle owner \(X_a\) and the clone target \(D_a\) is global
complementation and preserves distinctness.

After \(q\) lower deletions, the entrance is the terminal interval

\[
 S_a=I(a+q,m-q).
\tag{1.2}
\]

Since (q+(m-q)=m), its complement is

\[
 C_a=U\setminus S_a=I(a+m,H+q).
\tag{1.3}
\]

Equations (1.1) and (1.3) prove the nested-complement identity

\[
                         J_a\subseteq C_a.
\tag{1.4}
\]

This is independent of orientation conventions: reversal reverses both
intervals, and a common rotation shifts both starts.

The clone graphs in the mechanical-atlas theorem were indexed by the
start of the interval in the relevant row.  Reindex the middle clone by
\(a\mapsto a+m\) and the entrance clone by \(a\mapsto a+q\). Both are
bijections of \(\mathbb Z_M\), so neither clone graph nor either Hall
matching changes.  They merely put the two rows in the common physical
owner-phase convention (1.1)--(1.3).

Fix the balanced half \(P\in\binom{[2m]}m\). If

\[
 t=|U\cap P|,\qquad \alpha=t/M,
\tag{1.5}
\]

the mechanical word gives prescribed counts

\[
 j=|J_a\cap P|,
 \qquad c=|C_a\cap P|
\tag{1.6}
\]

with

\[
             |j-H\alpha|<1,
             \qquad |c-\ell\alpha|<1.
\tag{1.7}
\]

The strict inequalities may be replaced by weak inequalities without
affecting anything below.  Notice that the mechanical word itself
satisfies \(J_a\subset C_a\); in particular \(j\le c\) and
\(H-j\le\ell-c\).

## 2. Exact conditional containment probability

Let

\[
                         G=S_P\times S_{P^c}.
\tag{2.1}
\]

It preserves every root type, every mechanical clone graph, and all
target distinctness.

### Lemma 2.1 (profile-conditioned containment)

Let \(A,B\) be roots of the same type \(t\), with tops \(U_A,U_B\).
Fix an \(H\)-set \(J\subset U_A\) having \(P\)-count \(j\), and an
\(\ell\)-set \(C\subset U_B\) having \(P\)-count \(c\). If \(g\) is
uniform in \(G\), conditional on \(gB=A\), then

\[
\begin{aligned}
 \Pr(J\subseteq gC\mid gB=A)
 &=\frac{\binom{t-j}{c-j}}{\binom tc}
   \frac{\binom{M-t-H+j}{\ell-c-H+j}}
        {\binom{M-t}{\ell-c}}                                      \\
 &=\frac{(c)_j}{(t)_j}
   \frac{(\ell-c)_{H-j}}{(M-t)_{H-j}}.
\end{aligned}
\tag{2.2}
\]

Here a binomial coefficient with an infeasible lower index is zero and
\((x)_s=x(x-1)\cdots(x-s+1)\).

If

\[
                         M/4\le t\le3M/4,
\tag{2.3}
\]

and \(j,c\) satisfy (1.7), then

\[
 \Pr(J\subseteq gC\mid gB=A)
 \le\left(\frac{\ell+4}{M}\right)^H.
\tag{2.4}
\]

#### Proof

Conditional on \(gB=A\), the restriction of \(g\) to the two shores of
\(U_B\) is a uniformly random pair of bijections

\[
 U_B\cap P\longrightarrow U_A\cap P,
 \qquad
 U_B\cap P^c\longrightarrow U_A\cap P^c.
\tag{2.5}
\]

Thus \(gC\) is uniform among the \(\ell\)-sets in \(U_A\) with
\(P\)-count \(c\). To contain \(J\), it must choose its remaining
\(c-j\) points from the \(t-j\) unused \(P\)-points and its remaining
\(\ell-c-H+j\) points from the \(M-t-H+j\) unused \(P^c\)-points.
This proves the first line of (2.2); cancellation of factorials proves
the second.

For \(0\le s\le x\le y\),

\[
                       \frac{(x)_s}{(y)_s}
                       \le\left(\frac xy\right)^s,
\tag{2.6}
\]

because \((x-u)/(y-u)\le x/y\) for every \(0\le u<s\).
Under (2.3) and (1.7),

\[
 \frac ct\le\frac\ell M+\frac4M,
 \qquad
 \frac{\ell-c}{M-t}\le\frac\ell M+\frac4M.
\tag{2.7}
\]

Apply (2.6) to the two factors in (2.2).  Their exponents add to (H),
giving (2.4). \(\square\)

At the tuned height and for \(q=o(\sqrt m)\), one has

\[
 \ell=H+q=(1+o(1))H,
 \qquad
 \log\frac{M}{\ell+4}
   =\left(\frac12+o(1)\right)\log m.
\tag{2.8}
\]

Equations (2.4) and (2.8) give (0.5).

### Lemma 2.2 (extreme root types have negligible mass)

Let

\[
 n_t=\binom mt\binom m{t-H}
\tag{2.9}
\]

be the number of roots of type \(t\). There is an absolute \(c_0>0\)
such that

\[
 \sum_{t<M/4\text{ or }t>3M/4}Mn_t
 \le T\exp(-c_0m)=o(W).
\tag{2.10}
\]

#### Proof

The normalized masses \(n_t/R\) form the hypergeometric law obtained by
choosing an \(M\)-set from a population with \(m\) points in each shore.
For \(|t-M/2|\ge M/4\), the entropy bound

\[
                 \binom m{\rho m}\le\exp(mh(\rho))
\tag{2.11}
\]

puts the numerator in (2.9) below
\(4^m\exp(-c_1m)\) for an absolute \(c_1>0\), uniformly because
\(H=o(m)\). On the other hand, the central-binomial lower bound and
\(H^2/m=O(\log m)\) give

\[
 R=\binom{2m}{m+H}\ge4^m m^{-C}
\tag{2.12}
\]

for an absolute \(C\). Summing over at most \(m+1\) values of \(t\)
absorbs the polynomial factor and proves (2.10). \(\square\)

## 3. Two exact Hall matchings can be linearly incompatible

Let ({\cal L}) be the common owner-phase clone set

\[
                         {\cal L}=\{(A,a):A\in\binom{[2m]}{m-H},
                                      \ a\in\mathbb Z_M\},
 \qquad |{\cal L}|=T.
\tag{3.1}
\]

Use the fixed phase reindexing of Section 1 in the two clone graphs.
Let ({\cal M}_0) be an integral middle clone matching and
({\cal M}_r) an integral entrance clone matching supplied by the exact
clone Hall theorem.  Write (L_0,L_r\subseteq{\cal L}) for their left
domains.  Since all source and target totals differ from (T) by
(o(W)),

\[
                         |L_0|=T-o(W),
                         \qquad |L_r|=T-o(W).
\tag{3.2}
\]

For ((A,a)\in L_0), write (J_{A,a}) for the local (H)-set obtained
from its matched middle target.  For ((B,a)\in L_r), write
(C_{B,a}=U_B\setminus S_{B,a}), where (S_{B,a}) is its matched
entrance target.

For (g\in G), conjugate the entrance matching by

\[
 (B,a)\longmapsto(gB,a),
 \qquad C_{B,a}\longmapsto gC_{B,a}.
\tag{3.3}
\]

This remains an integral matching: (g) is a bijection on roots and
targets, preserves the two shores, and therefore preserves every
mechanical cell.

### Theorem 3.1 (linear common-permutation separation)

There is \(g\in G\) with the following property. For every family of
rootwise phase bijections

\[
                         \sigma_A:\mathbb Z_M\longrightarrow\mathbb Z_M,
\tag{3.4}
\]

the paired domains have size

\[
 \left|\left\{(A,a)\in L_0:
       (g^{-1}A,\sigma_A(a))\in L_r\right\}\right|=T-o(W)
\tag{3.5}
\]

but

\[
 \left|\left\{(A,a)\in L_0:
       (g^{-1}A,\sigma_A(a))\in L_r,\ 
       J_{A,a}\subseteq gC_{g^{-1}A,\sigma_A(a)}
       \right\}\right|=o(W).
\tag{3.6}
\]

#### Proof

The domain bound holds for every \(g\) and every family \(\sigma_A\).
Indeed, a rootwise phase bijection preserves the size of the entrance
domain:

\[
 \left|\left\{(A,a):(g^{-1}A,\sigma_A(a))\in L_r\right\}\right|
 =|L_r|.
\tag{3.7}
\]

Inclusion-exclusion with \(L_0\) and (3.2) proves (3.5).

To obtain one \(g\) which works for every alignment, count all phase
pairs. Choose \(g\) uniformly in \(G\), and put

\[
 Z(g)=\sum_A\ \sum_{\substack{a:(A,a)\in L_0\\
                              b:(g^{-1}A,b)\in L_r}}
 {\bf1}\{J_{A,a}\subseteq gC_{g^{-1}A,b}\}.
\tag{3.8}
\]

Fix a central middle clone \((A,a)\) and an entrance phase \(b\).
Conditional on \(g^{-1}A=B\), whenever \((B,b)\in L_r\), Lemma 2.1
bounds the containment probability by

\[
                         p_*:=\left(\frac{H+q+4}{M}\right)^H.
\tag{3.9}
\]

If \((B,b)\notin L_r\), its contribution is zero. Averaging over the
possible roots \(B\) of the same type therefore leaves the same upper
bound \(p_*\). There are at most \(M\) entrance phases for each middle
clone. Summing over all central clones and using Lemma 2.2—with one
additional polynomial factor \(M\)—for the remaining clones gives

\[
                         \mathbb E_g Z(g)
 \le Mp_*T+o(W)=o(W).
\tag{3.10}
\]

Some \(g\) attains at most this expectation. For any family
\(\sigma_A\), the containments in (3.6) form a subcollection of the
terms counted by \(Z(g)\), proving (3.6). \(\square\)

### Corollary 3.2 (exact edit-distance obstruction)

For the pair of matchings in Theorem 3.1, every subassignment arising
from common cyclic orders can retain both prescribed targets on only
(o(W)) of their (T-o(W)) common-domain clones.  Consequently at least

\[
                              T-o(W)=W-o(W)
\tag{3.11}
\]

middle or entrance clone incidences must be changed or discarded before
the pair can be realized by common permutations.

#### Proof

If a common cyclic order retains both prescribed targets at owner phase
\(a\), (1.4) forces their local sets to satisfy
\(J_{A,a}\subseteq C_{A,\sigma_A(a)}\), where \(\sigma_A\) is the
relative phase alignment of the two clone tables. Every clone counted
by (3.5) but not (3.6) therefore requires
at least one changed or discarded incidence.  Distinct owner phases are
distinct incidence pairs, so one edit cannot pay for two of them.
Equations (3.5)--(3.6) prove (3.11). \(\square\)

The argument remains valid after one prescribed phase is deleted at
every root: replace (T) by ((M-1)R=T-o(W)), and observe that the
deleted total (R=o(W)) is absorbed by every displayed error term.

## 4. The cut has a literal \(E_H\) component

Let \(I_{H,\ell}\) be the inclusion matrix with rows indexed by
\(H\)-sets, columns indexed by \(\ell\)-sets, and entries

\[
                       (I_{H,\ell})_{J,C}={\bf1}_{J\subseteq C}.
\tag{4.1}
\]

Decompose the \(H\)-set space into Johnson harmonics

\[
                \mathbb R^{\binom UH}=E_0\perp\cdots\perp E_H,
                \qquad
                d_j=\dim E_j=\binom Mj-\binom M{j-1}.
\tag{4.2}
\]

### Lemma 4.1 (exact inclusion spectrum)

On \(E_j\),

\[
 I_{H,\ell}I_{H,\ell}^{\mathsf T}
 =\lambda_j I,
 \qquad
 \lambda_j=\binom{\ell-j}{H-j}
             \binom{M-H-j}{\ell-H}
 \quad(0\le j\le H).
\tag{4.3}
\]

In particular

\[
                         \lambda_H=\binom{M-2H}{\ell-H}
                                  =\binom{M-2H}{q}>0.
\tag{4.4}
\]

#### Proof

Let \(h\) be a harmonic function on the \(j\)-sets, so every one-step
down-sum of \(h\) is zero, and define its lift to the \(k\)-th slice by

\[
                 (L_{j,k}h)(K)=\sum_{\substack{Z\subseteq K\\|Z|=j}}h(Z).
\tag{4.5}
\]

The images of \(L_{j,H}\) are exactly \(E_j\). Two elementary
double-counts, the second using the zero down-sum successively, give

\[
\begin{aligned}
 I_{H,\ell}^{\mathsf T}L_{j,H}h
   &=\binom{\ell-j}{H-j}L_{j,\ell}h,\\
 I_{H,\ell}L_{j,\ell}h
   &=\binom{M-H-j}{\ell-H}L_{j,H}h.
\end{aligned}
\tag{4.6}
\]

For the first identity, fix an \(\ell\)-set \(C\): each \(j\)-set
\(Z\subset C\) lies in exactly \(\binom{\ell-j}{H-j}\) intermediate
\(H\)-sets. For the second, add the \(\ell-H\) outside coordinates one
at a time. At a step from a \(k\)-set to a \((k+1)\)-set, the terms
whose harmonic \(j\)-set uses the new coordinate cancel by the
one-step down-sum, leaving multiplier \(M-k-j\); division by the
\(\ell-H\) unordered insertion orders gives
\[
 \frac{(M-H-j)_{\ell-H}}{(\ell-H)!}
 =\binom{M-H-j}{\ell-H}.
\]
Composing the two identities in (4.6) proves (4.3).

Equivalently, (4.3) follows by applying finite differences of order
\(j\) to the kernel

\[
 (I_{H,\ell}I_{H,\ell}^{\mathsf T})(J,J')
 =\binom{M-|J\cup J'|}{\ell-|J\cup J'|}.
\tag{4.7}
\]

Putting \(j=H\) proves (4.4). \(\square\)

All columns of \(I_{H,\ell}\) are conjugate under \(S_U\). Therefore

\[
 \binom M\ell\,\|P_jf_C\|_2^2
 =\operatorname{tr}\!\left(P_jI_{H,\ell}
                               I_{H,\ell}^{\mathsf T}\right)
 =d_j\lambda_j.
\tag{4.8}
\]

Taking \(j=H\), \(\ell=H+q\), and using (4.4) proves (0.7).
More generally, put \(j=H-s\) in (4.3) and (4.8). Then

\[
 \lambda_{H-s}
 =\binom{q+s}{s}\binom{M-2H+s}{q},
\tag{4.9}
\]

which proves (0.8).

To display the integral separator explicitly, introduce a paired-clone
variable \(z_{A,a,J,C}\) which is one when owner phase \((A,a)\) is
assigned the middle local set \(J\) and the entrance complement \(C\).
Every common-permutation column satisfies the support equality

\[
 \boxed{
 \sum_{A,a}\ \sum_{J\not\subseteq C}z_{A,a,J,C}=0.}
\tag{4.10}
\]

The paired point formed from the two matchings in Theorem 3.1 has left
side (W-o(W)).  Thus (4.10) is an exact integral separating equality
with linear gap.  Formula (0.7) identifies its nonzero top Johnson
component.  The equality is linear after the two clone rows are lifted
to their joint variables; in the two separate marginal tables it is,
necessarily, a bilinear support condition.

## 5. Exact boundary and next gate

Proved here:

1. the exact owner-phase nesting (J_a\subseteq U\setminus S_a) for a
   physical promotion frame;
2. the profile-conditioned containment probability (2.2);
3. its uniform (m^{-\omega(1)}) bound on all but exponentially few
   roots;
4. two integral (T-o(W)) clone Hall matchings whose common-permutation
   edit distance is (W-o(W));
5. the exact top- and near-top-harmonic inclusion masses (0.7)--(0.8);
   and
6. the lifted integral support separator (4.10).

Not proved here:

1. that every pair of near-perfect clone matchings is far from a common
   permutation;
2. that no jointly designed nested clone matching exists;
3. an integrality gap for the actual frame-column LP; or
4. coefficient one.

The theorem closes one tempting inference sharply: separate clone Hall
theorems, even with exact profile balance and only (o(W)) unmatched
clones, do not compose through a common permutation.  The next positive
object must impose (4.10) from the outset.  Its atoms should be nested
pairs

\[
                 (J,C),\qquad J\in\binom UH,
                 \quad C\in\binom U{H+q},\quad J\subset C,
\tag{5.1}
\]

and then enforce the lag-(H) and lag-((H+q)) rotor equations across
all phases of a root.  Equivalently, a useful compound exchange must
move an entire nested interval flag of one cyclic order; independent
middle and entrance exchanges are separated from that semigroup by
(W-o(W)).
