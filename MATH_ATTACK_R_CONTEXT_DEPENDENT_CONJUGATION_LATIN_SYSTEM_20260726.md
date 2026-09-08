# Context-dependent Dyck conjugation: the exact Latin system, reciprocal cubes, and the frozen top cell

Date: 2026-07-26

Method: pure mathematics only.  No web search, finite search, solver, or
computer enumeration is used.

## 0. Exact outcome

Let

\[
 D=\mathcal D_s,\qquad
 H=H_s=\langle(2i\ 2i+1):1\le i<s\rangle,
\]

and let \(F_s\) be the canonical anchored MSW factor.  Given an arbitrary
map

\[
                         a:D\longrightarrow H,
                         \qquad a(P)=h_P,              \tag{0.1}
\]

form the candidate row

\[
                         G_a(P)=h_PF_s(h_PP).          \tag{0.2}
\]

The inverse is absent in (0.2) only because every element of \(H\) is an
involution.

There are three complete conclusions.

1.  Exact factorhood of (0.2) is equivalent to an explicit simultaneous
    \(X/Y\) Latin-section system.  There is no further completion
    condition.
2.  For \(s\ge3\), nonconstant solutions exist in exponentially growing
    exact cubes.  Already the first reciprocal-rectangle bank gives
    \(2^{C_{s-2}}\) solutions, and its all-selected vertex changes
    \(2C_{s-2}=(1/8+o(1))C_s\) roots.
3.  Context dependence cannot lower the forced top/top cell.  For every
    map (0.1), whether exact or not,
    \[
                         Q_a(s,2s)\ge R_{s-1},          \tag{0.3}
    \]
    where
    \[
       \sum_{n\ge0}R_nz^n={1\over1-z^2C(z)^2},
       \qquad {R_{s-1}\over C_s}\longrightarrow{1\over9}.       \tag{0.4}
    \]
    The constant all-block selector attains equality and is exact.

Let \(\mathcal F_{s,j}\) be the roots whose first return is at \(2j\),
let \(b_1^{G_a}(P)\) be the first coordinate inserted on row \(P\), and
define

\[
 Q_a(j,x)=
 \#\{P\in\mathcal F_{s,j}:b_1^{G_a}(P)=x\}.            \tag{0.4a}
\]

Consequently, if

\[
 L(G_a)=\max_{1\le j\le s,\ x\in[2s]}Q_a(j,x),
\]

then

\[
 \boxed{
 \min_{\substack{a:D\to H\\G_a\ \mathrm{exact}}}L(G_a)
 =
 \begin{cases}
 1,&s=1,2,\\
 R_{s-1},&s\ge3.
 \end{cases}}                                           \tag{0.5}
\]

Thus the entire rowwise coordinate-conjugate library, not merely the
global conjugates, is closed at normalized constant \(1/9\).

Throughout, \(C_n=\operatorname {Cat}_n\) and
\(C(z)=\sum_{n\ge0}C_nz^n=1+zC(z)^2\).

## 1. The two exact ownership ledgers

Put \(J=[2s]\),

\[
 \mathcal L=\binom Js,\qquad \mathcal U=\binom J{s+1}.
\]

Write the canonical row rooted at \(P\in D\) as

\[
 X_0(P),X_1(P),\ldots,X_s(P),
 \qquad X_0(P)=P,\quad X_s(P)=J\setminus P,            \tag{1.1}
\]

and put

\[
                         Y_t(P)=X_t(P)\cup X_{t+1}(P)
                         \qquad(0\le t<s).             \tag{1.2}
\]

Exactness of \(F_s\) says precisely that the two maps

\[
\begin{aligned}
 \xi_X:D\times\{0,\ldots,s\}&\longrightarrow\mathcal L,
 &\xi_X(P,t)&=X_t(P),\\
 \xi_Y:D\times\{0,\ldots,s-1\}&\longrightarrow\mathcal U,
 &\xi_Y(P,t)&=Y_t(P)
\end{aligned}                                           \tag{1.3}
\]

are bijections.

For the row (0.2), define

\[
 X_t^a(P)=a(P)X_t(a(P)P),\qquad
 Y_t^a(P)=a(P)Y_t(a(P)P).                              \tag{1.4}
\]

Every row (1.4) is individually a valid complementary Johnson geodesic:
coordinate relabelling preserves adjacency, and

\[
 X_0^a(P)=a(P)^2P=P,\qquad
 X_s^a(P)=J\setminus P.                               \tag{1.5}
\]

Hence the only possible failure is global ownership.  The standard cut
trace criterion gives

\[
 G_a\text{ is an exact anchored factor}
 \iff
 \begin{cases}
 \{X_t^a(P):P\in D,\ 0\le t\le s\}=\mathcal L
     &\text{once each},\\
 \{Y_t^a(P):P\in D,\ 0\le t<s\}=\mathcal U
     &\text{once each}.
 \end{cases}                                           \tag{1.6}
\]

The second line is indispensable.  Through complementation followed by
adjoining the odd-graph interface coordinate, it is exactly ownership of
the vertices on the other shore.

## 2. Cocycle and Latin-section forms

For \(\epsilon\in\{X,Y\}\), let \(\Omega_\epsilon\) denote the
corresponding domain in (1.3).  Coordinate action induces a representation

\[
 \Lambda_\epsilon(h)=\xi_\epsilon^{-1}\circ h\circ\xi_\epsilon
             \in\operatorname {Sym}(\Omega_\epsilon),             \tag{2.1}
\]

while root action gives

\[
 \widetilde\rho_\epsilon(h)(P,t)=(hP,t).              \tag{2.2}
\]

Define

\[
 c_\epsilon(h)=
 \Lambda_\epsilon(h)\widetilde\rho_\epsilon(h)^{-1}. \tag{2.3}
\]

### Lemma 2.1 (ownership cocycle)

For \(g,h\in H\),

\[
 c_\epsilon(gh)=c_\epsilon(g)\,
 \widetilde\rho_\epsilon(g)c_\epsilon(h)
 \widetilde\rho_\epsilon(g)^{-1}.                   \tag{2.4}
\]

Moreover

\[
 \xi_\epsilon\bigl(c_\epsilon(h)(P,t)\bigr)
      =h\,\xi_\epsilon(hP,t).                        \tag{2.5}
\]

#### Proof

Both \(\Lambda_\epsilon\) and \(\widetilde\rho_\epsilon\) are
representations.  Therefore

\[
\begin{aligned}
 c_\epsilon(g)\widetilde\rho_\epsilon(g)c_\epsilon(h)
       \widetilde\rho_\epsilon(g)^{-1}
 &=\Lambda_\epsilon(g)\Lambda_\epsilon(h)
   \widetilde\rho_\epsilon(h)^{-1}
   \widetilde\rho_\epsilon(g)^{-1}\\
 &=c_\epsilon(gh).
\end{aligned}
\]

Since \(h^{-1}=h\), applying (2.3) to \((P,t)\) first replaces \(P\)
by \(hP\), and then (2.1) applies \(h\) to its physical token.  This is
(2.5). \(\square\)

### Theorem 2.2 (necessary and sufficient Latin system)

For \(\epsilon\in\{X,Y\}\), define

\[
 C_\epsilon^a(P,t)=c_\epsilon(a(P))(P,t).             \tag{2.6}
\]

Then

\[
 \boxed{
 G_a\text{ is an exact anchored factor}
 \iff C_X^a\text{ and }C_Y^a\text{ are bijections}.} \tag{2.7}
\]

#### Proof

By (2.5), applying \(\xi_\epsilon\) to the image multiset of (2.6)
gives exactly the selected token multiset in (1.4).  Since
\(\xi_\epsilon\) is a bijection, that multiset contains every token once
if and only if \(C_\epsilon^a\) is a bijection.  Apply (1.6) on both
shores. \(\square\)

The \(X\)-part can be separated phase by phase.  Because \(H\) preserves
every Chung--Feller \(X\)-layer, define
\(\kappa_t(h)\in\operatorname {Sym}(D)\) by

\[
                         hX_t(P)=X_t(\kappa_t(h)P).    \tag{2.8}
\]

Then the exact \(X\)-condition is

\[
 \boxed{
 P\longmapsto \kappa_t(a(P))a(P)P
 \text{ is a permutation of }D
 \quad(0\le t\le s).}                                \tag{2.9}
\]

There is generally no valid phasewise replacement for the \(Y\)-part:
coordinate action can mix the canonical \(Y\)-columns.  The full
\(\Omega_Y\)-bijection in (2.7) is the necessary condition; checking only
the state ledger or treating a fixed colour-owner column as a permutation
does not prove exactness.

## 3. Physical owner transversals

There is an equivalent formulation without phases.  For a physical token
\(T\in\mathcal L\sqcup\mathcal U\), let \(\rho(T)\in D\) be its unique
canonical owner root.  In the global conjugate with label \(h\), its
physical owner is

\[
                         \lambda_h(T)=h\rho(hT).       \tag{3.1}
\]

Indeed, \(hT\) is canonically owned by \(\rho(hT)\), and conjugating that
row sends its root to (3.1).  Since \(H\) is abelian, the covariance law is

\[
                         \lambda_{gh}(T)=g\lambda_h(gT).           \tag{3.2}
\]

Put

\[
 z_{P,h}=\mathbf1_{\{a(P)=h\}}\in\{0,1\}.            \tag{3.3}
\]

### Theorem 3.1 (integral owner equations)

The candidate \(G_a\) is exact if and only if

\[
 \sum_{h\in H}z_{P,h}=1\qquad(P\in D),               \tag{3.4}
\]

and

\[
 \boxed{
 \sum_{h\in H}z_{\lambda_h(T),h}=1
 \qquad(T\in\mathcal L\sqcup\mathcal U).}           \tag{3.5}
\]

Equivalently, the graph of \(a\) in \(D\times H\) meets each owner block

\[
 L_T=\{(\lambda_h(T),h):h\in H\}                     \tag{3.6}
\]

in exactly one point.

#### Proof

For a fixed label \(h\), token \(T\) occurs in the selected candidate
precisely when the row rooted at its global-\(h\) owner \(\lambda_h(T)\)
has chosen label \(h\).  Its total multiplicity is therefore the left
side of (3.5).  Equations (3.5) on the lower and upper token families are
exactly the two lines of (1.6). \(\square\)

Subtracting (3.4) at the canonical owner \(\rho(T)=\lambda_1(T)\) gives
the coboundary form

\[
 \Delta_a(T):=
 \sum_{h\in H}\bigl(z_{\lambda_h(T),h}-z_{\rho(T),h}\bigr)=0
 \qquad(T\in\mathcal L\sqcup\mathcal U).             \tag{3.7}
\]

Thus legal selectors are precisely the integral zero-defect sections of
the simultaneous \(X/Y\) owner system.

## 4. Complete binary specialization

Fix \(g,k\in H\) and suppose \(a(P)\in\{g,k\}\).  Put

\[
                         A=\{P:a(P)=k\}.               \tag{4.1}
\]

Let \(\Gamma_{g,k}\) be the multigraph on \(D\) having, for every
physical \(X\)- or \(Y\)-token \(T\), an edge

\[
                         \lambda_g(T)\ --\ \lambda_k(T).          \tag{4.2}
\]

Loops and repeated edges are harmless.

### Theorem 4.1 (binary cocycle theorem)

\[
 \boxed{
 G_a\text{ is exact}
 \iff A\text{ is a union of connected components of }
       \Gamma_{g,k}.}                                 \tag{4.3}
\]

#### Proof

The multiplicity of token \(T\) is

\[
 \mathbf1_{\{\lambda_g(T)\notin A\}}
 +\mathbf1_{\{\lambda_k(T)\in A\}}.                 \tag{4.4}
\]

This equals one if and only if

\[
 \mathbf1_A(\lambda_g(T))
      =\mathbf1_A(\lambda_k(T)).                      \tag{4.5}
\]

All token equations hold exactly when \(\mathbf1_A\) is constant along
every edge of \(\Gamma_{g,k}\), which is equivalent to (4.3).
\(\square\)

The graph \(\Gamma_{g,k}\) is the full state-and-colour ownership overlay
of the two global conjugates after contracting the common physical-root
port edges.  Thus (4.3) is exactly the ownership-component shore rule,
not merely a state-overlay condition.

## 5. Reciprocal rectangles are kernel atoms

Assume \(s\ge2\).  Let

\[
                         \sigma_1=(2\ 3).              \tag{5.1}
\]

For \(R\in D_{s-2}\), put

\[
                         P_R=1100R,\qquad Q_R=1010R.   \tag{5.2}
\]

The exact MSW flip-word recursion gives

\[
\begin{aligned}
 \rho_{\rm flip}(1100R)&=(4,2,3,1,4+\rho_{\rm flip}(R)),\\
 \rho_{\rm flip}(1010R)&=(2,1,4,3,4+\rho_{\rm flip}(R)).          \tag{5.3}
\end{aligned}
\]

Suppressing the common shifted tail and writing the shifted root suffix
again as \(R\), the first three states of the two canonical rows are

\[
\begin{array}{c|ccc}
 P_R&12R&14R&34R\\
 Q_R&13R&23R&24R.
\end{array}                                             \tag{5.4}
\]

The corresponding rows of the conjugate \(G_{\sigma_1}\) are

\[
\begin{array}{c|ccc}
 P_R&12R&23R&34R\\
 Q_R&13R&14R&24R.
\end{array}                                             \tag{5.5}
\]

They rejoin their original rows after the displayed slab.  Both shores
use the same six states, and their four union colours are

\[
                         123R,124R,134R,234R            \tag{5.6}
\]

once each.  A changed state gives a cross-owner edge, while all exterior
tokens remain on these two roots.  Hence

\[
                         K_R=\{P_R,Q_R\}               \tag{5.7}
\]

is a complete two-root component of \(\Gamma_{1,\sigma_1}\).  The
different \(K_R\) are pairwise root-disjoint.

### Corollary 5.1 (growing reciprocal-rectangle cube)

For every \(\mathcal R\subseteq D_{s-2}\), define

\[
 a_{\mathcal R}(P)=
 \begin{cases}
  \sigma_1,&P\in\displaystyle\bigcup_{R\in\mathcal R}K_R,\\
  1,&\text{otherwise}.
 \end{cases}                                           \tag{5.8}
\]

Then \(G_{a_{\mathcal R}}\) is an integral exact anchored factor.  Thus
the selector space contains a literal Boolean cube of dimension
\(C_{s-2}\).

#### Proof

The selected \(\sigma_1\)-root set in (5.8) is a union of complete
components of \(\Gamma_{1,\sigma_1}\).  Apply Theorem 4.1.  Equivalently,
changing both roots of one \(K_R\) is a two-row reciprocal rectangle and
is a zero-defect \(\{0,1\}\)-kernel atom of (3.7); changing only one root
would violate a cross-owner token equation.  Root-disjoint atoms may be
chosen independently. \(\square\)

Selecting all these rectangle components changes exactly \(2C_{s-2}\)
rows, and

\[
 {2C_{s-2}\over C_s}
   ={s(s+1)\over2(2s-1)(2s-3)}\longrightarrow{1\over8}.           \tag{5.9}
\]

For \(s\ge3\), this is a genuinely nonconstant positive-density selector.
More generally, the verified full \(\sigma_1\)-overlay components are

\[
 \mathcal C_{j,R}=\mathcal A_jR,\qquad
 0\le j\le s-2,\quad R\in D_{s-j-2},               \tag{5.10}
\]

where

\[
 \mathcal A_j=
 \{1u0:u\in D_{j+1}\}\ \dot\cup\
 \{10\,1v0:v\in D_j\}.                              \tag{5.11}
\]

Their shore sizes are \(C_{j+1}+C_j\).  Theorem 4.1 therefore also gives
the complete binary count

\[
 \#\{a:D\to\{1,\sigma_1\}:G_a\text{ exact}\}
      =2^{\sum_{q=0}^{s-2}C_q}.                       \tag{5.12}
\]

The rectangles (5.7) are precisely the \(j=0\) components.

## 6. Exact top/top formula for an arbitrary selector

Write a Dyck root in paired form

\[
 P=1\,b_1b_2\cdots b_{s-1}\,0,\qquad |b_i|=2,        \tag{6.1}
\]

and use the two-coloured Motzkin encoding

\[
 11\mapsto U,\qquad00\mapsto D,\qquad
 01\mapsto\alpha,\qquad10\mapsto\beta.              \tag{6.2}
\]

A horizontal step is called ground-level when the Motzkin height before
it is zero.  The source first-return fibre \(\mathcal F_{s,s}\) consists
exactly of the roots having no ground \(\alpha\)-step.  For such a root,
put

\[
 B(P)=\{i:b_i\text{ is a ground }\beta\text{-step}\}.             \tag{6.3}
\]

For \(h\in H\), let

\[
 S(h)=\{i:(2i\ 2i+1)\text{ occurs in }h\}.            \tag{6.4}
\]

The element \(h\) fixes the uncoloured Motzkin skeleton and exchanges
\(\alpha,\beta\) exactly at the times in \(S(h)\).

### Theorem 6.1 (sharp selector formula)

For every map \(a:D\to H\), with no exactness assumption,

\[
 \boxed{
 Q_a(s,2s)
 =R_{s-1}
 +\#\{P\in\mathcal F_{s,s}:B(P)\ne\varnothing,
                   \ S(a(P))\cap B(P)=\varnothing\}.}             \tag{6.5}
\]

In particular, (0.3) holds pointwise for every selector.

#### Proof

Let \(\operatorname {fr}(Q)\) be the first-return semilength.  The
canonical first target is

\[
                         b_1^{F_s}(Q)=2\operatorname {fr}(Q).      \tag{6.6}
\]

Thus

\[
 b_1^{G_a}(P)=
 a(P)\bigl(2\operatorname {fr}(a(P)P)\bigr).          \tag{6.7}
\]

Every element of \(H\) fixes \(2s\), and no coordinate \(2k\), \(k<s\),
can be sent to \(2s\).  Hence, for \(P\in\mathcal F_{s,s}\), the target
in (6.7) is \(2s\) exactly when \(a(P)P\) is still in
\(\mathcal F_{s,s}\).  Since \(P\) has no ground \(\alpha\), this occurs
exactly when no ground \(\beta\) is flipped, namely when

\[
                         S(a(P))\cap B(P)=\varnothing.             \tag{6.8}
\]

The roots with \(B(P)=\varnothing\) have no ground horizontal step of
either colour.  Let their number be \(R_{s-1}\).  Splitting (6.8)
according as \(B(P)\) is empty or nonempty proves (6.5). \(\square\)

It remains to verify the count used in the proof.  An arbitrary
two-coloured Motzkin excursion has generating function \(C(z)^2\).  An
excursion with no ground horizontal step is a sequence of elevated blocks
\(U M D\), each with generating function \(z^2C(z)^2\).  Therefore

\[
 R(z)=\sum_{n\ge0}R_nz^n
      ={1\over1-z^2C(z)^2}
      ={C(z)^2\over2C(z)-1},                          \tag{6.9}
\]

and length \(s-1\) gives exactly \(R_{s-1}\) roots.

The all-block element

\[
                         w_s=\prod_{i=1}^{s-1}(2i\ 2i+1)           \tag{6.10}
\]

has \(S(w_s)=[s-1]\).  It intersects every nonempty \(B(P)\), so (6.5)
gives

\[
                         Q_{w_s}(s,2s)=R_{s-1}.        \tag{6.11}
\]

Because the constant selector \(a(P)=w_s\) is one global coordinate
conjugate, it satisfies the full Latin system.

Finally, at the Catalan singularity,

\[
 C(z)=2-2\sqrt{1-4z}+O(1-4z).
\]

For \(\Phi(u)=u^2/(2u-1)\), one has \(\Phi'(2)=4/9\).  Equation (6.9)
therefore gives

\[
                         R_n\sim{4\over9}C_n.          \tag{6.12}
\]

Since

\[
                         {C_{s-1}\over C_s}={s+1\over4s-2}
                         \longrightarrow{1\over4},    \tag{6.13}
\]

the normalized limit in (0.4) is exactly \(1/9\).

## 7. Minimax consequence and sharp boundary

Every legal selector satisfies

\[
                         L(G_a)\ge Q_a(s,2s)\ge R_{s-1}.           \tag{7.1}
\]

For \(s\ge3\), the exact full-swap quota matrix has largest entry
\(R_{s-1}\).  Thus it attains both inequalities in (7.1), proving (0.5).
At \(s=1,2\), integrality forces a nonempty cell and the full swap has
largest cell one.

The obstruction is stronger than exact ownership.  On the unavoidable
root set

\[
 \mathcal E_s=\{P:\text{no ground horizontal step of either colour}\},
\]

every library row has first target \(2s\).  In the variables (3.3), its
contribution is identically

\[
 \sum_{P\in\mathcal E_s}\sum_{h\in H}z_{P,h}
       =|\mathcal E_s|=R_{s-1}.                       \tag{7.2}
\]

Thus reciprocal rectangle cubes, arbitrary legal ownership-component
choices, and even fractional selectors cannot change this contribution.
They can only remove the nonnegative second term in (6.5).

The exact scope is the row library

\[
             \{hF_s(hP):h\in H\}\quad\text{at each root }P.       \tag{7.3}
\]

An overlapping collection of locally commuting rectangle switches does
not automatically lie in (7.3): one must prove that every resulting row
is a single coordinate-conjugate row and that (3.5) holds.  Conversely,
to beat the exact bound \(R_{s-1}\) one must change the first edge on at
least one root of \(\mathcal E_s\) to an edge outside (7.3).  To lower the
normalized load below \(1/9-\varepsilon\), for fixed
\(0<\varepsilon<1/9\),
one must do this on at least
\((\varepsilon+o(1))C_s\) roots of \(\mathcal E_s\); reducing this cell to
\(o(C_s)\) requires changing
\((1/9-o(1))C_s\) such roots.  General anchored exact factors,
exterior-moving packets, and non-coordinate first-edge trades are not
ruled out by this theorem.
