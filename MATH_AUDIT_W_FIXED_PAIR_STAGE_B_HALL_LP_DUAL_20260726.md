# Fixed-pair cube Stage B: exact orbit Hall dual, Gaussian no-go, and the mixed-pair escape

Date: 2026-07-26

Method: pure mathematics only. No finite search, numerical optimization,
solver, or web input is used.

## 0. Verdict

Fix one perfect matching \(\mathcal P\) of the \(2m\) physical
coordinates. At depth \(q\), the hyperoctahedral group preserving
\(\mathcal P\) partitions the rank-\((m-q)\) targets into full-pair
orbits. If \(f\) is the number of full pairs, the target demand and
middle-start supply are

\[
 T_{f,q}
 =\frac{m!\,2^{m-2f-q}}
        {f!(f+q)!(m-2f-q)!},
 \qquad
 V_f
 =\frac{m!\,2^{m-2f}}
        {f!^2(m-2f)!}.
\tag{0.1}
\]

Every internal fixed-\(\mathcal P\) cube window preserves \(f\).
The exact optimal Hall deficiency of the fully flexible one-depth
fixed-pair face relaxation is

\[
 \boxed{
 D_{m,q}
 =\sum_f(T_{f,q}-V_f)_+.}
\tag{0.2}
\]

On every tileable source type this is also the exact deficit of the
fractional catalogue of all fixed-\(\mathcal P\) partial cycles. For
\(\ell=o(m)\), the nontileable types contribute only \(o(W)\), so the
full-catalogue deficit is \(D_{m,q}+o(W)\). The maximizing Hall set in the
maximal face relaxation is the union of all deficient target orbits.
Changing direction orders, cube tilings, translations, or resolution
classes while retaining the same unordered pairing cannot lower the
deficit below (0.2).

For

\[
 q=\lfloor c\sqrt m\rfloor,\qquad c>0\text{ fixed},
\]

one has

\[
 \boxed{
 \frac{D_{m,q}}{\binom{2m}{m}}
 \longrightarrow
 \delta(c):=
 e^{-c^2}\Phi_{\rm G}(c/2)-\Phi_{\rm G}(-3c/2)>0.}
\tag{0.3}
\]

Thus one fixed-pair cube Stage B misses \(\Omega_c(W)\) targets whenever
this Gaussian depth lies in its certified geodesic range. This is a
rigorous coefficient-one no-go for the fixed-pair Stage-B architecture,
provided only \(o(W)\) depth-\(q\) windows leave the fixed frame. It is not
a no-go for arbitrary coefficient-one words:
\(\Theta(W/\sqrt m)\) isolated frame changes can affect
\(\Theta(W)\) Gaussian windows, and one long block in another frame can
make all of its internal windows exceptional with only two boundary seams.

Genuine variation of the unordered coordinate pairing evades (0.2).
Indeed:

1. with pairing allowed to depend on one source window, the admissible
   target-owner graph is the ordinary Boolean inclusion graph and has an
   integral matching saturating every depth-\(q\) target;
2. one symmetric-chain decomposition gives an exact two-sided
   lower/middle/upper owner-incidence resolution at every fixed depth;
3. averaging complete ordered conjugates gives a simultaneous all-depth
   fractional cover, so no signed Hall/LP separator survives in the full
   mixed-pair reservoir.

The remaining obstruction is integral and bundled. One must choose
middle-disjoint physical cycles, one pairing per cycle, whose common
windows work simultaneously at all depths and on both sides. The exact
remaining inequality is the mixed-block integral coverage condition in
Section 9. No linear orbit-capacity no-go for that mixed reservoir is
currently proved.

## 1. Fixed-pair target and source orbits

Let

\[
 \mathcal P=\{P_1,\ldots,P_m\},\qquad |P_i|=2,
\]

and define

\[
 \phi_{\mathcal P}(S)
 =|\{P_i:P_i\subseteq S\}|.
\tag{1.1}
\]

The group

\[
 H_{\mathcal P}\cong S_2\wr S_m
\]

acts transitively on sets of a fixed rank and fixed full-pair type.

For a middle set \(X\), having \(\phi_{\mathcal P}(X)=f\) means that
\(X\) has

\[
 f\text{ full pairs},\qquad
 f\text{ empty pairs},\qquad
 s=m-2f\text{ split pairs}.
\]

Let \(\mathcal M_f\) be this middle orbit. Direct choice of full, empty,
and oriented split pairs gives

\[
 |\mathcal M_f|=V_f
 =\frac{m!}{f!^2(m-2f)!}2^{m-2f}.
\tag{1.2}
\]

A lower target \(L\) of rank \(m-q\) and full-pair type \(f\) has

\[
 f\text{ full pairs},\qquad
 f+q\text{ empty pairs},\qquad
 s-q=m-2f-q\text{ split pairs}.
\]

Let \(\mathcal T^-_{f,q}\) be this orbit. Then

\[
 |\mathcal T^-_{f,q}|=T_{f,q}
 =\frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q}.
\tag{1.3}
\]

Summing the orbit sizes gives

\[
 \sum_fV_f=W:=\binom{2m}{m},
 \qquad
 \sum_fT_{f,q}=N_q:=\binom{2m}{m-q}.
\tag{1.4}
\]

Complementation gives the identical ledger for rank \(m+q\); full and
empty types are exchanged.

## 2. The exact one-depth Hall graph

Define a bipartite graph \(\Gamma_{f,q}\) between
\(\mathcal M_f\) and \(\mathcal T^-_{f,q}\). Join \(X\) to \(L\) when
\(L\) is the lower endpoint of some fixed-\(\mathcal P\)
axis-parallel \(q\)-face containing \(X\).

Equivalently, \(L\) is obtained from \(X\) by choosing \(q\) of the
\(s=m-2f\) split pairs and deleting from \(X\) its selected endpoint in
each chosen pair.

### Lemma 2.1 (exact degrees)

The graph \(\Gamma_{f,q}\) is biregular, with

\[
 d_{\mathcal M}=\binom{m-2f}{q},
 \qquad
 d_{\mathcal T}=2^q\binom{f+q}{q}.
\tag{2.1}
\]

#### Proof

For \(X\in\mathcal M_f\), choose the \(q\) split pairs which become empty
in \(L\). This gives the first degree.

For \(L\in\mathcal T^-_{f,q}\), choose which \(q\) of its \(f+q\) empty
pairs become split, and choose one of the two endpoints inserted into
\(X\) in each selected pair. This gives the second degree. \(\square\)

Double counting the edges gives

\[
 V_f\binom{m-2f}{q}
 =T_{f,q}\,2^q\binom{f+q}{q}.
\tag{2.2}
\]

Put

\[
 \lambda_{f,q}
 :=\frac{V_f}{T_{f,q}}
 =\frac{2^q\binom{f+q}{q}}
        {\binom{m-2f}{q}}
 =\frac{2^q(f+1)^{\overline q}}
        {(m-2f)_{\underline q}}.
\tag{2.3}
\]

Here rising and falling factorial notation is used in the last expression.

### Theorem 2.2 (exact fixed-pair Hall deficiency)

The maximum matching in \(\Gamma_{f,q}\) has size

\[
 \nu(\Gamma_{f,q})=\min(V_f,T_{f,q}).
\tag{2.4}
\]

Consequently, in the direct sum over all \(f\),

\[
 \boxed{
 \nu_{\mathcal P,q}
 =\sum_f\min(V_f,T_{f,q}),\qquad
 N_q-\nu_{\mathcal P,q}=D_{m,q}.}
\tag{2.5}
\]

Moreover,

\[
 \boxed{
 \max_{\mathcal A\subseteq\binom{[2m]}{m-q}}
 \bigl(|\mathcal A|-|N_{\Gamma}(\mathcal A)|\bigr)
 =D_{m,q},}
\tag{2.6}
\]

and a maximizing Hall set is

\[
 \mathcal A^*_{\mathcal P,q}
 =\bigcup_{f:T_{f,q}>V_f}\mathcal T^-_{f,q}.
\tag{2.7}
\]

#### Proof

Suppose first that \(V_f\le T_{f,q}\). For
\(\mathcal A\subseteq\mathcal M_f\), edge counting gives

\[
 d_{\mathcal M}|\mathcal A|
 \le d_{\mathcal T}|N(\mathcal A)|
\]

and, by (2.2),

\[
 \frac{d_{\mathcal M}}{d_{\mathcal T}}
 =\frac{T_{f,q}}{V_f}\ge1.
\]

Thus \(|N(\mathcal A)|\ge|\mathcal A|\), so Hall matches all
\(V_f\) source vertices. The same argument with the shores reversed
matches every target when \(T_{f,q}\le V_f\). This proves (2.4).

The type graphs are disjoint, so their matching numbers and deficiencies
add, proving (2.5). The target-side deficiency form of Hall gives (2.6).
The set (2.7) has neighborhood exactly the union of the corresponding
\(\mathcal M_f\), and its deficiency is the right side of (0.2), so it
attains the maximum. \(\square\)

The likelihood ratio \(\lambda_{f,q}\) is strictly increasing in \(f\)
through its valid range. Indeed,

\[
 \frac{\lambda_{f+1,q}}{\lambda_{f,q}}
 =
 \frac{f+q+1}{f+1}
 \frac{(m-2f)_{\underline q}}
      {(m-2f-2)_{\underline q}}>1.
\tag{2.8}
\]

Hence the deficient types \(\lambda_{f,q}<1\) form one initial
\(f\)-segment. The maximizing orbit cut is therefore a single type
threshold, up to a possible equality type.

### LP dual form

The fractional matching primal is

\[
\begin{aligned}
\max\quad&\sum_{X,L}x_{X,L}\\
\text{subject to}\quad&
\sum_Lx_{X,L}\le1\quad(X\in\mathcal M),\\
&\sum_Xx_{X,L}\le1\quad(L\in\mathcal T_q^-),\\
&x_{X,L}\ge0.
\end{aligned}
\tag{2.9}
\]

Its dual is

\[
\begin{aligned}
\min\quad&\sum_Xa_X+\sum_Lb_L\\
\text{subject to}\quad&
a_X+b_L\ge1\quad(XL\in E(\Gamma)),\\
&a_X,b_L\ge0.
\end{aligned}
\tag{2.10}
\]

An optimal integral dual chooses all middle vertices in a deficient type
\(T_{f,q}>V_f\), and all target vertices in a surplus type
\(T_{f,q}\le V_f\). Its cost is
\(\sum_f\min(V_f,T_{f,q})\). Thus (2.7) is simultaneously the exact
Hall cut and the exact LP-dual obstruction.

## 3. Exact physical cycle-window supply

The preceding graph permits every fixed-pair \(q\)-face independently.
The same capacity ratio occurs in the actual catalogue of physical partial
cycles.

Fix a source type \(f\), put \(s=m-2f\), and let
\(1\le q<\ell\le s\).
A geometric partial pair-flip cycle has \(2\ell\) middle vertices and uses
\(\ell\) distinct pair directions before returning through their
complements.

### Lemma 3.1 (cycle degrees)

The number of geometric partial \(2\ell\)-cycles through a prescribed
middle vertex in the \(s\)-dimensional orientation stratum is

\[
 g_s=\frac{(s)_{\underline\ell}}2.
\tag{3.1}
\]

The number of compatible cycles in which a prescribed
\(L\in\mathcal T^-_{f,q}\) occurs as a depth-\(q\) lower window is

\[
 h_{f,q}
 =2^{q-1}(f+q)_{\underline q}
       (s-q)_{\underline{\ell-q}}.
\tag{3.2}
\]

Consequently

\[
 \boxed{\frac{h_{f,q}}{g_s}=\lambda_{f,q}.}
\tag{3.3}
\]

#### Proof

For (3.1), choose the \(\ell\) active directions and order them, modulo
reversal:

\[
 \binom{s}{\ell}\frac{\ell!}{2}
 =\frac{(s)_{\underline\ell}}2.
\]

For (3.2), choose the \(q\) empty pairs of \(L\) which become the free
directions of its face, choose the remaining \(\ell-q\) active directions
from its \(s-q\) split pairs, and count the cycles containing the fixed
face. The three factors are

\[
 \binom{f+q}{q},\qquad
 \binom{s-q}{\ell-q},\qquad
 2^{q-1}q!(\ell-q)!.
\]

Their product is (3.2). Dividing by (3.1) gives (3.3). \(\square\)

### Theorem 3.2 (exact fractional cycle-block deficit)

Consider all geometric fixed-\(\mathcal P\) partial cycles, with middle
packing constraints

\[
 \sum_{B:X\in M(B)}x_B\le1.
\tag{3.4}
\]

Let

\[
 d_x(L)=\sum_{B:L\in C_q^-(B)}x_B
\]

be the fractional target degree, and maximize capped target coverage

\[
 \sum_L\min(1,d_x(L)).
\tag{3.5}
\]

Equivalently, introduce variables \(0\le c_L\le1\) with
\(c_L\le d_x(L)\) and maximize \(\sum_Lc_L\). Thus this is a genuine
finite linear program; (3.5) is its value after eliminating the \(c_L\).

On the tileable target types \(s\ge\ell\), the optimum is exactly

\[
 \boxed{
 \sum_{f:m-2f\ge\ell}\min(T_{f,q},V_f).}
\tag{3.6}
\]

If all target types are demanded and only partial \(2\ell\)-cycles are
admitted, the exact minimum fractional uncovered mass is

\[
\boxed{
D^{(\ell)}_{m,q}
=\sum_{f:m-2f\ge\ell}(T_{f,q}-V_f)_+
 +\sum_{f:m-2f<\ell}T_{f,q}
=D_{m,q}
 +\sum_{f:m-2f<\ell}\min(T_{f,q},V_f).}
\tag{3.7}
\]

#### Proof

Every cycle lies in one source type \(f\), has \(2\ell\) middle vertices,
and has \(2\ell\) distinct depth-\(q\) lower targets of that same type.
Therefore

\[
\begin{aligned}
\sum_{L\in\mathcal T^-_{f,q}}d_x(L)
&=\sum_{B\text{ of type }f}2\ell x_B\\
&=\sum_{X\in\mathcal M_f}
       \sum_{B:X\in M(B)}x_B
\le V_f.
\end{aligned}
\tag{3.8}
\]

Thus capped coverage in type \(f\) is at most
\(\min(T_{f,q},V_f)\).

Conversely, assign every geometric cycle in an \(s\)-stratum weight
\(1/g_s\). Lemma 3.1 gives middle degree one and target degree
\(\lambda_{f,q}\). Its capped coverage is

\[
 T_{f,q}\min(1,\lambda_{f,q})
 =\min(T_{f,q},V_f).
\]

Sum over the tileable \(f\). Nontileable targets have zero supply, which
gives (3.7). \(\square\)

Whenever \(Q_s\) admits a genuine exact tiling by these cycles—for example,
in the explicit power-of-two construction used in the fixed-pair
program—the attaining weights can also be obtained by averaging one such
tiling under the full cube isometry group. Thus the equality is compatible
with convex averaging of actual resolution classes in the intended
tileable regime. The capacity upper bound itself does not require tiling
existence.

An equivalent Farkas witness puts target weight one on every deficient
orbit and middle weight one on the corresponding source orbit. For every
fixed-\(\mathcal P\) cycle \(B\),

\[
 \sum_{L\in C_q^-(B)}y_L
 \le
 \sum_{X\in M(B)}z_X,
\tag{3.9}
\]

while globally

\[
 \sum_Ly_L-\sum_Xz_X=D_{m,q}.
\tag{3.10}
\]

This proves that resolution-class variation inside one pairing cannot
evade the obstruction even fractionally.

In the intended regime \(\ell=o(m)\), the types \(s<\ell\) lie a linear
distance from the \(s\sim m/2\) central range and have \(o(W)\) total
mass. Hence \(D^{(\ell)}_{m,q}=D_{m,q}+o(W)\) at Gaussian depth, and the
nontileable correction does not affect the lower bound below.

## 4. Gaussian evaluation of the worst cut

Let

\[
 q=c\sqrt m+o(\sqrt m),\qquad c>0,
\qquad
 X_m=\frac{f-m/4}{\sqrt m}.
\tag{4.1}
\]

Stirling's formula applied uniformly to (1.2)--(1.3) on bounded
\(X_m\)-intervals gives the more explicit local estimates

\[
 \frac{V_{\lfloor m/4+x\sqrt m\rfloor}}W
 =
 \frac4{\sqrt{2\pi m}}e^{-8x^2}(1+o(1)),
\tag{4.2}
\]

\[
 \frac{T_{\lfloor m/4+x\sqrt m\rfloor,q}}W
 =
 \frac4{\sqrt{2\pi m}}
 e^{-c^2-8(x+c/2)^2}(1+o(1)).
\tag{4.3}
\]

Equivalently, these estimates give the local central limits

\[
 X_m\Rightarrow N(0,1/16)
 \quad\text{under }V_f/W,
\tag{4.4}
\]

and

\[
 X_m\Rightarrow N(-c/2,1/16)
 \quad\text{under }T_{f,q}/N_q.
\tag{4.5}
\]

Also,

\[
 \frac{N_q}{W}\longrightarrow e^{-c^2}.
\tag{4.6}
\]

The exact likelihood ratio is

\[
 \frac{T_{f,q}}{V_f}
 =\prod_{i=0}^{q-1}
       \frac{m-2f-i}{2(f+1+i)}.
\tag{4.7}
\]

Uniformly for bounded \(X_m\),

\[
 \log\frac{T_{f,q}}{V_f}
 =-8cX_m-3c^2+o(1).
\tag{4.8}
\]

Hence \(T_{f,q}>V_f\) precisely below the asymptotic threshold

\[
 X_m<-\frac{3c}{8}+o(1).
\tag{4.9}
\]

For completeness, the tails do not hide additional mass. Under either
law, \(f\) is the sum of the \(m\) indicators that a fixed matching pair
is fully selected in a uniformly sampled fixed-size set. Direct
two-indicator sampling gives variance \(O(m)\). Chebyshev's inequality
therefore makes the mass outside
\(|X_m|\le K\) uniformly \(O(K^{-2})\). Letting first \(m\to\infty\) and
then \(K\to\infty\), the local estimates above may be summed over the
complete type range. Hence
summing the positive difference over the complete initial type segment
gives

\[
\begin{aligned}
\frac{D_{m,q}}W
&\longrightarrow
e^{-c^2}
 \Pr\!\left(N(-c/2,1/16)\le-3c/8\right)\\
&\hspace{28mm}
 -\Pr\!\left(N(0,1/16)\le-3c/8\right)\\
&=
e^{-c^2}\Phi_{\rm G}(c/2)
-\Phi_{\rm G}(-3c/2).
\end{aligned}
\tag{4.10}
\]

This proves the limit in (0.3).

The strict positivity needs no numerical evaluation. Let
\(\varphi\) be the standard normal density. Substituting
\(t=u+2c\) in the second Gaussian tail gives

\[
\begin{aligned}
\delta(c)
&=\int_{-\infty}^{c/2}
 \left(e^{-c^2}-e^{2ct-2c^2}\right)\varphi(t)\,dt\\
&=e^{-c^2}\int_{-\infty}^{c/2}
 \left(1-e^{2ct-c^2}\right)\varphi(t)\,dt>0
\end{aligned}
\tag{4.11}
\]

for every \(c>0\), since \(2ct-c^2\le0\) on the integration interval
and is strictly negative away from its endpoint.

## 5. Physical fixed-frame no-go and its exact scope

Assume \(q\) lies in the certified geodesic range of the cyclic
fixed-\(\mathcal P\) cube factor—for partial \(2\ell\)-cycles,
\(1\le q<\ell\). Every middle vertex then supplies one depth-\(q\) start,
and every internal window preserves its source type. Therefore Theorem 2.2
immediately gives

\[
 M_q^-\ge D_{m,q}
\tag{5.1}
\]

for the number of missing lower targets. The upper analogue follows by
complementation; the lower side alone suffices for the no-go.

More generally, suppose a linear row uses every middle set once and has
\(R_m\) additional row positions of any kind. Let \(E_{m,q}\) be the
number of depth-\(q\) starts which are not wholly contained in a
fixed-\(\mathcal P\) cell block. Every remaining start is charged to its
fixed-pair source type, while each additional row position supplies at
most one additional depth-\(q\) start. Hence the invariant bound is

\[
 \boxed{
 M_q^-\ge D_{m,q}-R_m-E_{m,q}.}
\tag{5.2}
\]

If the entire row is partitioned into \(b_m\) fixed-\(\mathcal P\) cell
blocks, then at most \(q\) starts cross each boundary, so

\[
 E_{m,q}\le qb_m
\quad\Longrightarrow\quad
 M_q^-\ge D_{m,q}-R_m-qb_m.
\tag{5.3}
\]

Combining (4.10) and (5.2), if

\[
 R_m=o(W),\qquad E_{m,q}=o(W),
\tag{5.4}
\]

then at \(q=\lfloor c\sqrt m\rfloor\),

\[
 M_q^-\ge(\delta(c)-o(1))W.
\tag{5.5}
\]

For partial blocks of length \(2\ell\) with
\(\sqrt m\ll\ell=o(m)\), one has

\[
 b_m=O(W/\ell),\qquad qb_m=o(W),
\]

so the usual linearization or seam padding does not repair the defect.

Changing the cube tiling, direction order, pair order, within-pair
orientation, or algebraic resolution class leaves \(\phi_{\mathcal P}\)
unchanged and is already allowed by the maximal catalogue in Sections
2--3. None can evade (5.5).

The scope is sharp. If departures from \(\mathcal P\) are isolated to seam
neighborhoods, one seam can contaminate at most \(q\) depth-\(q\) starts,
so escaping (5.3) requires \(\Omega_c(W/\sqrt m)\) such seams. In a
genuinely mixed row, however, one transition into one long block using a
different pairing has only two boundary seams while every internal window
of that block is exceptional relative to \(\mathcal P\). Thus the invariant
quantity is \(E_{m,q}\), not the number of visible frame changes.

The theorem rules out a row with only \(o(W)\) non-fixed-frame
depth-\(q\) windows. It does not rule out a coefficient-one braid which
uses another frame on a positive fraction of its windows, even if that
mixing is organized by only a sublinear number of block boundaries.

## 6. Exact fractional dual for whole resolution choices

The Hall graph above permits independent face choices. The following LP
records arbitrary whole-cycle resolution classes inside a predetermined
family of source cubes.

Let \(\mathcal C\) be the source cubes and
\(\mathcal R(C)\) the allowed resolutions of cube \(C\). Put

\[
 a_{C,r}(S)=
 \mathbf1_{\{\text{resolution }r\text{ exposes target }S\}}.
\]

The fractional minimum-hole LP is

\[
\begin{aligned}
\min\quad&\sum_Su_S\\
\text{subject to}\quad&
\sum_{r\in\mathcal R(C)}x_{C,r}=1
 \quad(C\in\mathcal C),\\
&u_S+\sum_{C,r}a_{C,r}(S)x_{C,r}\ge1
 \quad(S\in\mathcal T_q^-),\\
&x_{C,r},u_S\ge0.
\end{aligned}
\tag{6.1}
\]

Its exact dual is

\[
\boxed{
 \operatorname{Def}^{\rm res}_{\rm LP}
 =
 \max_{0\le y_S\le1}
 \left[
 \sum_Sy_S
 -\sum_{C\in\mathcal C}
   \max_{r\in\mathcal R(C)}
      \sum_Sa_{C,r}(S)y_S
 \right].}
\tag{6.2}
\]

#### Proof

Use multiplier \(y_S\ge0\) for the coverage constraint and a free
multiplier for each simplex equality. Minimization over \(u_S\ge0\)
forces \(y_S\le1\). Minimization over the simplex variables replaces the
free multiplier by the maximum resolution score in each cube, giving
(6.2). Strong finite-dimensional LP duality applies. \(\square\)

For a fixed pairing, taking

\[
 y_S=\mathbf1_{\{S\in\mathcal A^*_{\mathcal P,q}\}}
\tag{6.3}
\]

gives at least the orbit deficit \(D_{m,q}\), because every resolution
exposes at most one target per physical start and every such target stays
in the source type. Whole-cycle chronology or a restricted direction
catalogue may create additional dual cuts; it cannot reduce this one.

For the independent-window or fractional individual-cycle relaxation,
Sections 2--3 prove that (6.3) is the exact worst cut. For the genuine
whole-resolution LP, \(D_{m,q}\) is the exact orbit-capacity cut but need
not be the only obstruction.

## 7. Genuine pairing variation removes the orbit cut

Let pairings now vary with the source choice. Consider the union of all
fixed-pair face graphs.

### Theorem 7.1 (the mixed owner graph is the Boolean inclusion graph)

A rank-\((m-q)\) target \(L\) is adjacent to a middle set \(X\) under
some coordinate pairing if and only if

\[
                         L\subset X.
\tag{7.1}
\]

Every such incidence extends to a physical partial \(2\ell\)-cycle for
\(q<\ell\le m\).

#### Proof

Necessity is the definition of a lower intersection target.

Conversely, fix \(L\subset X\). Choose a perfect matching crossing the
balanced cut \(X\mid X^c\). Order first the \(q\) matching pairs whose
\(X\)-endpoints are the elements of \(X\setminus L\). Flipping these
\(q\) pair directions gives a geodesic path whose intersection is \(L\).
Add any \(\ell-q\) of the remaining matching directions and extend the
path to the standard partial \(2\ell\)-cycle. \(\square\)

The inclusion graph between ranks \(m-q\) and \(m\) is biregular:

\[
 d_{m-q}=\binom{m+q}{q},
 \qquad
 d_m=\binom mq.
\tag{7.2}
\]

Since \(d_{m-q}\ge d_m\), edge counting proves Hall on the target side.
Thus:

### Corollary 7.2

At one fixed depth, allowing the pairing to vary per owner gives an
integral matching saturating every lower target.

There is an exact two-sided strengthening.

### Theorem 7.3 (one-depth two-sided owner-incidence resolution)

For every fixed \(q\), there are distinct triples

\[
 L\subset X\subset U,\qquad
 |L|=m-q,\quad |X|=m,\quad |U|=m+q,
\tag{7.3}
\]

which use every lower target \(L\) and every upper target \(U\) exactly
once and use distinct middle owners \(X\). Each triple is the
intersection/middle/union triple of a geodesic fixed-pair \(q\)-window for
some pairing, and extends to a partial \(2\ell\)-cycle when \(q<\ell\le m\).

#### Proof

Take any symmetric-chain decomposition of the Boolean lattice. Every chain
meeting rank \(m-q\) has unique vertices \(L,X,U\) at the three displayed
ranks. These triples cover the two outer layers once and have distinct
middle vertices.

Pair \(X\setminus L\) bijectively with \(U\setminus X\), and pair \(L\)
bijectively with \([2m]\setminus U\). This is a perfect matching crossing
\(X\mid X^c\). Flip first the \(q\) pairs between
\(X\setminus L\) and \(U\setminus X\). The resulting geodesic has
intersection \(L\) and union \(U\). Extend it as in Theorem 7.1.
\(\square\)

Theorem 7.3 proves that no one-depth target-orbit Hall obstruction survives
free pairing variation, integrally in the target-to-owner incidence graph.
It is not a physical window packing: although the distinguished middle
owners \(X\) are distinct, the intermediate middle states of two geodesic
paths, and a fortiori their extended cycles, may overlap. It also does
**not** group the chosen windows into common cycles; different triples
generally use different pairings.

## 8. Simultaneous fractional mixed-pair feasibility

There are two exact ways to see that the fixed-pair dual disappears
fractionally.

First, let \(\mathfrak P\) be the set of all perfect matchings and
\(M=|\mathfrak P|\). Put

\[
 \rho_q=N_q/W,\qquad
 \lambda_{f,q}=V_f/T_{f,q}.
\]

For a fixed target \(S\), its type under a uniform random pairing has law

\[
 \pi_q(f)=T_{f,q}/N_q.
\]

The exact size-bias identity is

\[
 \pi_q(f)\lambda_{f,q}
 =\rho_q^{-1}\pi_0(f),
 \qquad
 \pi_0(f)=V_f/W.
\tag{8.1}
\]

Give target \(S\) the amount

\[
 z_{\mathcal P,S}
 =\frac{\rho_q}{M}
   \lambda_{\phi_{\mathcal P}(S),q}
\tag{8.2}
\]

from pairing \(\mathcal P\). Then

\[
 \sum_{\mathcal P}z_{\mathcal P,S}
 =\rho_q\mathbb E_{\mathcal P}
       \lambda_{\phi_{\mathcal P}(S),q}
 =1.
\tag{8.3}
\]

For a fixed bucket \((\mathcal P,f)\), summing (8.2) over all its
\(T_{f,q}\) targets uses exactly

\[
 \frac{\rho_qV_f}{M}
\tag{8.4}
\]

units of its \(V_f/M\) normalized middle supply. Thus every mixed type-Hall
cut holds; the full target-layer cut is tight. The unused amount
\((1-\rho_q)V_f/M\) is intentional. This argument is an exact aggregate
type-bucket flow. By itself it does not disaggregate the flow into common
physical cycle blocks.

Second, in the ideal full-support system, start from one complete physical
block partition whose components support every asserted depth, and average
all ordered coordinate conjugates with equal weight. Middle transitivity
makes every middle degree one. At one depth, each conjugate factor has
\(W\) window occurrences, so target transitivity gives every
rank-\((m-q)\) target degree

\[
 \frac W{N_q}=\rho_q^{-1}\ge1.
\tag{8.5}
\]

The same averaging is simultaneous in \(q\) and on both sides. Hence the
complete ideal mixed reservoir has a zero-hole fractional Stage-B coverage
solution. In the actual fixed-pair construction, the balanced tileable
strata cover all but the already audited exceptional mass; adjoining
singleton repair columns gives fractional repair \(o(W)\).

If one instead uses the explicitly radius-resolved decorated reservoir
whose base radius counts telescope to \(N_q\), every typed target degree is
exactly one. That stronger equality is bundled edgewise; it is not obtained
by independently thinning occurrences at different depths.

Section 9 gives the full coverage Farkas dual and verifies directly from
the conjugate average that no \(\Omega(W)\) linear separator exists.

This is fractional evasion, not an integral middle factor.

## 9. The exact remaining mixed-frame inequality

Let \(\mathscr B\) be the physical catalogue of candidate cycles from all
allowed pairing and resolution classes. For \(B\in\mathscr B\), write
\(M(B)\) for its middle vertices and \(C_{B,q}^{\epsilon}\) for its
distinct physical depth-\(q\) targets of sign
\(\epsilon\in\{-,+\}\).

An integral mixed factor is a family \(\mathcal F\subseteq\mathscr B\)
such that

\[
 \{M(B):B\in\mathcal F\}
\]

partitions the middle layer, apart from an allowed \(o(W)\) exceptional
set.

For a selected exact middle factor, physical Stage B has no artificial
matching conflict: windows do not consume one another. Its exact missing
count is

\[
 M_q^\epsilon(\mathcal F)
 =N_q-
 \left|\bigcup_{B\in\mathcal F}C_{B,q}^{\epsilon}\right|.
\tag{9.1}
\]

Conditional on the separately supplied SCD/tail outside \(q\le H\), and
on \(o(W)\) repair of any exceptional middle vertices, the exact
central-band Stage-B coverage target is

\[
 \boxed{
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}
 M_q^\epsilon(\mathcal F)=o(W).}
\tag{9.2}
\]

If auxiliary per-block quotas \(b_{B,q}^\epsilon\) are imposed, define

\[
 0\le b_{B,q}^\epsilon\le|C_{B,q}^\epsilon|,
 \qquad
 \sum_{B\in\mathcal F}b_{B,q}^\epsilon\le N_q,
\tag{9.3}
\]

and

\[
 r_q^\epsilon
 =N_q-\sum_{B\in\mathcal F}b_{B,q}^\epsilon
\ge0
\tag{9.4}
\]

and the exact Hall deficiency

\[
 \delta_q^\epsilon
 =\max_{\mathcal A\subseteq\mathcal F}
 \left(
 \sum_{B\in\mathcal A}b_{B,q}^\epsilon
 -
 \left|\bigcup_{B\in\mathcal A}
            C_{B,q}^{\epsilon}\right|
 \right)_+.
\tag{9.5}
\]

Then the quota version is feasible with total \(o(W)\) repair if and only
if

\[
 \boxed{
 \sum_{q\le H}\sum_{\epsilon\in\{-,+\}}
 (r_q^\epsilon+\delta_q^\epsilon)=o(W).}
\tag{9.6}
\]

For simultaneous selection of the middle factor and its shadows, the
fractional minimum-hole LP is

\[
\begin{aligned}
\min\quad&\sum_Su_S\\
\text{subject to}\quad&
\sum_{B:X\in M(B)}x_B=1\quad(X\text{ middle}),\\
&u_S+\sum_{B:S\in C(B)}x_B\ge1
   \quad(S\text{ a typed target}),\\
&x_B,u_S\ge0.
\end{aligned}
\tag{9.7}
\]

Its exact dual is

\[
\boxed{
\begin{aligned}
\max\quad&
\sum_Sy_S-\sum_Xz_X\\
\text{subject to}\quad&
0\le y_S\le1,\qquad z_X\in\mathbb R,\\
&\sum_{S\in C(B)}y_S
\le\sum_{X\in M(B)}z_X
\quad(B\in\mathscr B).
\end{aligned}}
\tag{9.8}
\]

The mixed conjugate average in Section 8 makes the optimum of (9.7) zero
in the ideal full-support system. More explicitly, let \(x\) be that
average, so every middle degree is one and every target degree
\(d_x(S)\ge1\). For any feasible \((y,z)\) in (9.8),

\[
\begin{aligned}
\sum_Sy_S-\sum_Xz_X
&\le
\sum_Sy_Sd_x(S)-\sum_Xz_X\\
&=
\sum_Bx_B\left(
 \sum_{S\in C(B)}y_S-\sum_{X\in M(B)}z_X
\right)\le0.
\end{aligned}
\tag{9.9}
\]

Thus the ideal LP has no positive dual witness. The displayed LP itself
has no middle-repair variables. To include the known exceptional cells,
one must augment it by middle and target singleton columns with their
literal costs; the known fractional singleton mass in that augmented LP is
\(o(W)\).

The unresolved statement is the additive integrality inequality

\[
 \boxed{
 \operatorname{OPT}_{\rm integral}(9.7)
 \le
 \operatorname{OPT}_{\rm fractional}(9.7)+o(W)
 =o(W).}
\tag{9.10}
\]

Here the integral optimum means \(x_B\in\{0,1\}\). In the actual
exceptional-cell system, (9.10) refers to the augmented singleton-cost LP.

This is strictly stronger than the one-depth inclusion matching and
strictly different from a separate matching at every \(q\). It must bundle:

1. exact middle ownership;
2. one common pairing and cyclic order inside each selected block;
3. lower and upper windows simultaneously;
4. the same selected blocks at every depth; and
5. any transported radius or tail certificate required by the
   coefficient-one compiler.

Equation (9.10), or the physical union form (9.2), is the exact remaining
mixed-frame gate.

## 10. A restricted two-resolution no-go

One integral obstruction survives when only two whole middle partitions
are offered.

### Proposition 10.1 (two-partition rigidity)

Let \(\mathcal P_0,\mathcal P_1\) be two partitions of the middle layer
into whole blocks. Form their bipartite overlap multigraph: its left and
right vertices are the blocks of the two partitions, and each middle set
is an edge joining its two containing blocks.

An exact middle cover using whole blocks from
\(\mathcal P_0\cup\mathcal P_1\) chooses, independently in each connected
component of this overlap graph, every block from one shore and no block
from the other.

#### Proof

If \(x_B,y_C\in\{0,1\}\) are the shore choices, exact coverage of a middle
set represented by edge \(BC\) is

\[
 x_B+y_C=1.
\]

These equations force all left variables in one connected component to
one common value and all right variables to its complement. Either
componentwise shore choice also satisfies all equations. \(\square\)

If the overlap graph is connected and each endpoint partition uses one
fixed pairing, the only exact whole-block middle factors are the two
endpoints. For internal cyclic windows their respective deficits (0.2)
survive exactly; after a linear compilation the surviving lower bound is
the scoped form (5.2), specialized to (5.3) for a fixed-pair block
partition, and it yields (5.5) under the corresponding \(o(W)\)
hypotheses. Thus two whole partitions whose overlap graph is connected do
not evade Stage B when their extra positions and exceptional depth-\(q\)
windows total \(o(W)\).

This obstruction does not extend to disconnected overlays, componentwise
mixing, three or more pairing systems, genuine multiblock absorbers, or
near-covers with \(o(W)\) deletions or overlaps.

## 11. Final implication boundary

The following are proved.

1. For one fixed pairing, \(D_{m,q}\) is the exact worst Hall/LP cut in
   the maximal face relaxation. On tileable types the fractional
   cycle-catalogue deficit is the first sum in (3.7), and the full
   \(2\ell\)-cycle catalogue has deficit \(D_{m,q}+o(W)\) when
   \(\ell=o(m)\).
2. At every fixed positive Gaussian depth,
   \(D_{m,q}=(\delta(c)+o(1))W\) with \(\delta(c)>0\).
3. Resolution variation inside that pairing cannot help.
4. Free pairing variation removes the cut integrally in the one-depth
   owner-incidence graph and fractionally at all depths.
5. Two connected whole-resolution systems are component-rigid.

The following are not proved.

1. An integral mixed-pair cycle factor satisfying (9.2).
2. The additive integrality bound (9.10).
3. A new higher-order dual or lattice invariant obstructing (9.10).

Therefore there is a rigorous no-go for fixed-pair cube Stage B, but no
Hall/LP no-go for genuine mixed pairing. The shortest live theorem is the
common-cycle integrality inequality (9.10); another fixed-type capacity
estimate cannot settle it.
