# Master redirect, lane S: exact no-go theorems for recursive SCD selection

Date: 2026-07-25

Inputs re-audited: `MATHEMATICAL_HANDOFF.md` through item 1423,
`MATH_ATTACK_J_ROTOR_SCD_RESOLUTION_20260724.md`,
`MATH_ATTACK_D_ROTOR_SCD_TOLL_SURGERY_20260725.md`,
`MATH_ATTACK_D_FIFTH_WAVE_MULTIFRAME_SCD_SURGERY_20260725.md`, and
`MATH_ATTACK_J_RSCD_RECURSIVE_EULER_REPORT_20260725.md`, together with the
independently derived forced-target theorem in
`MATH_ATTACK_G_ROTOR_SCD_LOW_SWITCH_REDIRECT_20260725.md`.

## 0. Outcome

The standard recursive-selection route does not produce a low-toll SCD.  In
fact, it has an unavoidable toll of order $W\sqrt m$, uniformly over the
parent SCD and over every local phase choice.

More precisely, let an arbitrary full SCD of $B_{2m}$ be lifted to
$B_{2m+2}$ by decomposing each parent-chain box

\[
 C\times B_{\{a,b\}}
\]

in either of its two standard phases, with the phase chosen independently in
every box.  At every native child radius $d\ge1$, each parent radius-
$d-1$ chain creates a child chain having indegree zero in the induced
directed rotor graph.  Hence

\[
 p_d^*\ge c_{d-1}^{(m)}.
\]

For $H=\lceil A\sqrt{m+1}\rceil$, $A>0$ fixed, the corrected exact-prefix
toll therefore satisfies

\[
 \widehat\Phi_H
 \ge
 \biggl(
  2\int_0^A e^{-x^2}\,dx-2Ae^{-A^2}+o(1)
 \biggr)W_m\sqrt m,
 \qquad W_m=\binom{2m}{m}.
\]

Since $W_{m+1}=(4+o(1))W_m$, this is

\[
 \frac{\widehat\Phi_H}{W_{m+1}}
 \ge
 \left(
   \frac12\left[\int_0^A e^{-x^2}\,dx-Ae^{-A^2}\right]+o(1)
 \right)\sqrt m.
\]

Thus every standard two-coordinate recursive SCD, every whole-chain
multicolor recombination of its two phases over the same parent boxes, and
every $o(W_m)$-state surgery around any such output fails
$\mathrm{RSCD}_A$.

There is a second, independent no-go.  The exact low-toll odd-cut
pseudo-orbit and the coordinate orbit of genuine BTK SCDs have exactly the
same state-occurrence fibers, so statewise bijections give an entirely
integral recoloring from one to the other.  Nevertheless the pseudo-orbit
has $o(Q_mW_m)$ exact-prefix toll, whereas every one of those genuine-SCD
recolorings has toll at least

\[
 \bigl(C(A)+o(1)\bigr)Q_mW_m\sqrt m,
 \qquad
 C(A)=4\int_0^A x^2e^{-x^2}\,dx>0.
\]

Consequently, exact state marginals, exact Birkhoff/statewise resolution,
and low uncolored or pseudo-colored toll do not guarantee low toll under a
prescribed target-orbit resolution.  An adaptively chosen successful target
orbit, if one exists, must be chosen jointly with the rotor arcs.

These theorems close the standard $B_2$-recursive phase library, sparse
surgery around it, whole-chain phase multicover recombination, and every
uncoupled marginal/conditional-expectation selection argument into a
prescribed orbit.  They do not refute $\mathrm{RSCD}_A$.  The surviving SCD
route must differ on $\Omega(W_m)$ chain states from every standard phase
product and must solve an arc-correlated integral Hall problem.  Those dense
changes could come from a nonstandard within-box decomposition or from
cross-parent splicing; neither is excluded.  Section 5 proves a new exact
necessary condition for the surviving Hall route.

For that surviving route, Section 5 also records the exact positive
one-layer composition lemma: at layer $h$, the minimum additional cut count is
$|E_h|-M_h^\star$, where $M_h^\star$ is the maximum simultaneous agreement
of two integral endpoint perfect matchings with the forced rotor labels.
Along one recursively consistent sequence, total disagreement
$o(W_m/H)$ is sufficient for one full low-toll SCD at that fixed window.
If such compatible sequences exist for every fixed $A$, the accepted tail
step and diagonalization give constant one.  The exact one-layer
characterization and conditional implication are proved; existence of the
required compatible small-disagreement sequences is unproved.

All objects below are integral.  No finite search, computation, or
fractional-to-integral inference is used.

## 1. Notation and the exact prefix statistic

Put

\[
 N_j^{(m)}=\binom{2m}{m-j},
 \qquad
 c_j^{(m)}=N_j^{(m)}-N_{j+1}^{(m)},
 \qquad
 W_m=N_0^{(m)}.
\]

Every full SCD of $B_{2m}$ has exactly $c_j^{(m)}$ chains of native
radius $j$.  A native radius-$d$ chain is represented by its state

\[
 \omega=(L;z_1,\ldots,z_{2d};R),
 \qquad |L|=|R|=m-d.
\]

For $d\ge1$, its directed rotor successors are

\[
 (L-x+y;x,z_1,\ldots,z_{2d-1};R-y+z_{2d}),
 \qquad x\in L,\quad y\in R.
 \tag{1.1}
\]

For an SCD $\mathcal D$, let $p_d^*(\mathcal D)$ be the minimum number
of components in a spanning vertex-disjoint directed path forest of the
induced radius-$d$ rotor graph.  If the SCD is clipped at radius $H$, its
exact hard-prefix toll is

\[
 \widehat\Phi_H(\mathcal D)
 =\sum_{d=0}^H 2d\,p_d^*(\mathcal D).
 \tag{1.2}
\]

The radius-zero weight is exactly zero.  The conservative reset weight
$2d+1$ has the same $o(W)$ threshold, but every lower bound below is
proved for the sharper weight $2d$.

For $d<H$, clipping does not change the native radius-$d$ class.  The
top class $d=H$ also contains clips of chains of larger native radius, so
all finite lower bounds below deliberately omit $d=H$.

## 2. The standard-product indegree obstruction

### 2.1 The four child signatures

Let

\[
 C=(L;z_1,\ldots,z_{2r};R)
\]

be a parent chain state, and add two new coordinates $a,b$.  Choose a
phase $p\in\{a,b\}$ and write $q$ for the other new coordinate.  The
standard phase-$p$ decomposition of
$C\times B_{\{a,b\}}$ has the following chain states:

\[
 \begin{aligned}
 \mathsf A_p(C)
   &=(L;z_1,\ldots,z_{2r},p,q;R),\\
 \mathsf H_p(C)
   &=(L+p;z_1,\ldots,z_{2r-1},q;R+z_{2r}),\\
 \mathsf S_q(C)
   &=(L+q;z_1,\ldots,z_{2r};R+p),\\
 \mathsf C(C)
   &=(L+p+q;z_1,\ldots,z_{2r-2};
             R+z_{2r-1}+z_{2r}).
 \end{aligned}
 \tag{2.1}
\]

Terms with a negative singleton length are omitted at the boundary.  In
particular, a radius-zero parent still produces the radius-one
$\mathsf A$-chain.

Consequently the new-coordinate signatures of a native radius-$d$ child
are exhaustive and are as follows.

\[
\begin{array}{c|c|c}
\text{child type}&\text{parent radius}&
  \text{positions of the two new coordinates}\\ \hline
\mathsf A&d-1&
  \text{singleton positions }2d-1,2d\\
\mathsf H&d&
  \text{one in }L,\ \text{the other at singleton position }2d\\
\mathsf S&d&
  \text{one in }L,\ \text{the other in }R\\
\mathsf C&d+1&
  \text{both in }L.
\end{array}
\tag{2.2}
\]

Changing phase exchanges the names $a,b$, but not their locations in
this table.

### Theorem 2.1 (every outer child is a rotor source)

Let $\mathcal D$ be any full SCD of $B_{2m}$.  Independently in each
parent-chain box, choose either standard phase, and let $\mathcal E$ be
the resulting full SCD of $B_{2m+2}$.  Then for every native radius
$d\ge1$, every $\mathsf A$-child has indegree zero in the induced
directed rotor graph on the radius-$d$ chains of $\mathcal E$.  Hence

\[
 \boxed{
 p_d^*(\mathcal E)\ge c_{d-1}^{(m)}.
 }
 \tag{2.3}
\]

#### Proof

Suppose first that $d\ge2$.  Under a rotor move, a source singleton word

\[
 (s_1,\ldots,s_{2d})
\]

becomes

\[
 (\xi,s_1,\ldots,s_{2d-1}),
 \tag{2.4}
\]

where $\xi$ is the coordinate removed from the source lower block.  In an
$\mathsf A$-target, the two new coordinates occupy target singleton
positions $2d-1,2d$.  Equation (2.4) therefore forces those same two
coordinates to occupy source singleton positions $2d-2,2d-1$.

No row of (2.2) has this signature.  A source of type $\mathsf A$ has
them at positions $2d-1,2d$; a source of type $\mathsf H$ has only one
new singleton, at position $2d$; and sources of types $\mathsf S$ and
$\mathsf C$ have no new singleton.  Thus an $\mathsf A$-target has no
predecessor when $d\ge2$.

For $d=1$, write the $\mathsf A$-target singleton word as $p,q$.
Equation (2.4) says that a predecessor would have to remove $p$ from its
lower block and have $q$ in source singleton position (1).  An
$\mathsf A$-source has no new lower coordinate.  An $\mathsf H$-source
can have $p$ in its lower block, but its first singleton is an old
coordinate and the other new coordinate is at singleton position (2).
An $\mathsf S$-source has no new singleton, and a $\mathsf C$-source
also has no new singleton.  Hence no predecessor exists at $d=1$ either.
This explicitly includes the radius-zero parent boundary.

There is exactly one $\mathsf A$-child for each parent radius-$d-1$
chain, independently of phase.  Thus there are exactly
$c_{d-1}^{(m)}$ distinct indegree-zero vertices.  Every indegree-zero
vertex must start its own component in any spanning directed path forest,
which proves (2.3).  $\square$

### Corollary 2.2 (exact clipped toll and sharp constant)

Let $2\le H\le m$.  Then every $\mathcal E$ in Theorem 2.1 satisfies

\[
 \begin{aligned}
 \widehat\Phi_H(\mathcal E)
 &\ge 2\sum_{d=1}^{H-1}d\,c_{d-1}^{(m)}\\
 &=2\left(
       \sum_{j=0}^{H-2}N_j^{(m)}
       -(H-1)N_{H-1}^{(m)}
     \right).
 \end{aligned}
 \tag{2.5}
\]

For every fixed $A>0$, with

\[
 H=\lceil A\sqrt{m+1}\rceil,
\]

one has

\[
 \boxed{
 \widehat\Phi_H(\mathcal E)
 \ge (2f(A)+o(1))W_m\sqrt m,
 \qquad
 f(A)=\int_0^A e^{-x^2}\,dx-Ae^{-A^2}>0.
 }
 \tag{2.6}
\]

Equivalently,

\[
 \frac{\widehat\Phi_H(\mathcal E)}{W_{m+1}\sqrt m}
 \ge \frac{f(A)}2+o(1).
 \tag{2.7}
\]

#### Proof

Put $j=d-1$.  The finite identity in (2.5) is the telescoping calculation

\[
 \begin{aligned}
 \sum_{j=0}^{H-2}(j+1)
       (N_j^{(m)}-N_{j+1}^{(m)})
 &=\sum_{j=0}^{H-2}N_j^{(m)}
   -(H-1)N_{H-1}^{(m)}.
 \end{aligned}
 \tag{2.8}
\]

Uniformly for $0\le j\le A\sqrt m+O(1)$,

\[
 \frac{N_j^{(m)}}{W_m}
 =e^{-j^2/m}(1+o(1)).
 \tag{2.9}
\]

This follows directly by taking logarithms in

\[
 \frac{N_j^{(m)}}{W_m}
 =\prod_{i=1}^j\frac{m-i+1}{m+i};
\]

the logarithm is $-j^2/m+O_A(m^{-1/2})$ on the stated range.  Thus (2.8),
divided by $W_m\sqrt m$, is a Riemann sum and tends to

\[
 \int_0^A e^{-x^2}\,dx-Ae^{-A^2}.
\]

The positivity is strict for $A>0$, since

\[
 f(0)=0,
 \qquad
 f'(A)=2A^2e^{-A^2}>0.
\]

Finally,

\[
 \frac{W_{m+1}}{W_m}
 =\frac{(2m+2)(2m+1)}{(m+1)^2}
 =4-\frac2{m+1},
\]

which gives (2.7).  $\square$

The lower bound is of the correct order within this library: the trivial
singleton forest gives $\widehat\Phi_H=O_A(W_{m+1}\sqrt m)$.  Hence the
standard recursive library has toll $\Theta_A(W_{m+1}\sqrt m)$, not
$o(W_{m+1})$.

## 3. Multicolor and dense-surgery consequences

### 3.1 Whole-chain phase recombination creates no third local type

For a parent chain of radius $r\ge1$, overlay labelled copies of the two
standard phases.  In one target color, let

\[
 A_a,A_b,B_a,B_b,D_a,D_b
\]

denote the selected multiplicities of the six structural chain types.
Here the full-chain types $\mathsf B,\mathsf D$ have the radius-preserving
states denoted $\mathsf H,\mathsf S$ in (2.1)--(2.2).
Exact cell ownership forces

\[
 \begin{gathered}
 A_a+A_b=1,
 \quad B_a+D_a=1,
 \quad A_a+D_a=1,\\
 D_b+B_b=1,
 \quad D_b+A_b=1,
 \quad B_a+B_b=1.
 \end{gathered}
 \tag{3.1}
\]

Solving gives

\[
 B_a=D_b=A_a,
 \qquad
 B_b=D_a=A_b,
 \qquad
 A_a+A_b=1.
\]

Because the variables count integral whole chains, the target color chooses
one complete phase package.  The common $\mathsf C$-chain is selected
once independently.  The same equations apply with arbitrarily many
labelled copies: labels can be exchanged, but no third structural local SCD
is created.

At the radius-zero parent boundary, the only structural chains are
$A_a,A_b,D_a,D_b$.  Exact ownership of the four box cells gives

\[
 A_a+A_b=1,
 \qquad A_a+D_a=1,
 \qquad D_b+A_b=1.
 \tag{3.1a}
\]

Thus either $(A_a,D_b)=(1,1)$ and $(A_b,D_a)=(0,0)$, which is phase
$a$, or the reverse choice, which is phase $b$.  Hence the boundary box
also creates no third whole-chain local SCD type.

### Corollary 3.1 (no whole-chain selector in the standard phase library)

Consider any exact multicover consisting of labelled standard phase copies
over one fixed parent-chain box system.  Recolor it into target colors using
only whole child chains and require every target color to be an exact SCD.
Then every target color receives a complete phase package in every parent
box, including the radius-zero boundary.  Therefore every target color is a
boxwise phase field of the form covered by Theorem 2.1 and satisfies
(2.5)--(2.7).

In particular, no whole-chain multicover selection or recombination in this
library yields a low-toll SCD.  This is an integral statement; it is not an
averaging bound.

### 3.2 A successful surgery must change a positive fraction of the chains

The component statistic is two-Lipschitz under state replacement.  If
$\mathcal E,\mathcal F$ are two SCDs clipped to the same band and

\[
 M_d=|\mathcal E_d\setminus\mathcal F_d|
    =|\mathcal F_d\setminus\mathcal E_d|,
\]

then

\[
 |p_d^*(\mathcal E)-p_d^*(\mathcal F)|\le2M_d.
 \tag{3.2}
\]

Indeed, delete the $M_d$ removed vertices from an optimal path forest of
$\mathcal E_d$.  Since a path forest has vertex degree at most two, at
most $2M_d$ forest edges disappear.  Insert the new vertices as
singletons.  This gives one inequality in (3.2), and interchanging the SCDs
gives the other.

Fix $0<a<b<A$, let $\mathcal E$ be any standard phase-field product
from Theorem 2.1, and let $\mathcal F$ be any child SCD with

\[
 \widehat\Phi_H(\mathcal F)=o(W_{m+1}),
 \qquad H=\lceil A\sqrt{m+1}\rceil.
\]

For all sufficiently large $m$, the annulus
$a\sqrt m\le d\le b\sqrt m$ is native, and (2.3), (3.2) give

\[
 p_d^*(\mathcal F)\ge c_{d-1}^{(m)}-2M_d.
\]

Now

\[
 \frac1{W_m\sqrt m}
 \sum_{a\sqrt m\le d\le b\sqrt m}
 2d\,c_{d-1}^{(m)}
 \longrightarrow
 4\int_a^b x^2e^{-x^2}\,dx.
 \tag{3.3}
\]

Indeed,

\[
 c_{d-1}^{(m)}
 =N_{d-1}^{(m)}\frac{2d-1}{m+d},
\]

and (2.9) gives, uniformly for $d=x\sqrt m$ with $x\in[a,b]$,

\[
 \frac{c_{d-1}^{(m)}}{W_m}
 =\frac{2x}{\sqrt m}e^{-x^2}+O_{a,b}(m^{-1}).
\]

Multiplication by $2d$ and summation is the Riemann limit (3.3).

Therefore

\[
 \boxed{
 \sum_{a\sqrt m\le d\le b\sqrt m}dM_d
 \ge
 \left(\int_a^b x^2e^{-x^2}\,dx-o(1)\right)W_m\sqrt m,
 }
 \tag{3.4}
\]

and, since $d\le b\sqrt m$,

\[
 \boxed{
 \sum_{a\sqrt m\le d\le b\sqrt m}M_d
 \ge
 \left(\frac1b\int_a^b x^2e^{-x^2}\,dx-o(1)\right)W_m.
 }
 \tag{3.5}
\]

Thus no $o(W_m)$-state surgery, and in particular no $o(W_m)$-whole-
chain surgery, around a standard phase-field product can prove
$\mathrm{RSCD}_A$.  A successful output must be densely different in
every fixed typical-radius annulus.

## 4. Exact desynchronization inside the rotor multicover

The preceding theorem closes the standard recursive phase library.  The
next theorem closes a different proposed shortcut: first create a low-toll
exact occurrence multicover, then select an SCD color using only exact state
marginals or statewise Birkhoff bijections.

Fix $A>0$ and

\[
 H=\lceil A\sqrt m\rceil\le m-2,
 \qquad
 Q_m=(2m-1)(2m)!.
\]

For a clipped SCD put

\[
 \gamma_d=c_d^{(m)}\quad(0\le d<H),
 \qquad
 \gamma_H=N_H^{(m)}.
\]

Then

\[
 \sum_{d=q}^H\gamma_d=N_q^{(m)}.
 \tag{4.1}
\]

The exact odd-cut construction supplies a pseudo-color with $\gamma_d$
legitimate radius-$d$ states and a directed path forest having

\[
 p_d^0\le\frac{\gamma_d}{m+1}+2.
 \tag{4.2}
\]

It need not be an SCD, because masks in its lower and upper shadows can
collide.

### Theorem 4.1 (integral desynchronization gap)

There is an exact integral chronology of the whole $Q_m$-fold band rotor
master on which the odd-cut pseudo-colors have exact-prefix toll

\[
 R_{\rm ps}
 \le Q_m\left(
     \frac{2\sum_{q=1}^H N_q^{(m)}}{m+1}
     +2H(H+1)
   \right)
 =o(Q_mW_m).
 \tag{4.3}
\]

The same state-occurrence fibers admit exact statewise recolorings into the
labelled coordinate orbit of the genuine BTK SCD.  Nevertheless every such
recoloring, for every choice of the statewise bijections and every rotor
chronology, has exact-prefix toll at least

\[
 R_{\rm BTK}
 \ge Q_m\sum_{d=1}^{H-1}2d\,c_d^{(m)}
 =\bigl(C(A)+o(1)\bigr)Q_mW_m\sqrt m,
 \tag{4.4}
\]

where

\[
 \boxed{
 C(A)=4\int_0^A x^2e^{-x^2}\,dx
 =\sqrt\pi\,\operatorname{erf}(A)-2Ae^{-A^2}>0.
 }
 \tag{4.5}
\]

#### Proof

First, (4.1) gives the exact weighted telescoping identity

\[
 \sum_{d=0}^H2d\,\gamma_d
 =2\sum_{q=1}^HN_q^{(m)}.
 \tag{4.6}
\]

Using (4.2),

\[
 \begin{aligned}
 \sum_{d=0}^H2d\,p_d^0
 &\le
 \frac{2\sum_{q=1}^HN_q^{(m)}}{m+1}
 +4\sum_{d=1}^Hd\\
 &=
 \frac{2\sum_{q=1}^HN_q^{(m)}}{m+1}
 +2H(H+1).
 \end{aligned}
 \tag{4.7}
\]

Taking $2m-1$ copies of the complete coordinate orbit and applying the
exact balanced-master Eulerization embeds every pseudo-forest path
consecutively in a chronology of all $Q_m$ occurrences.  This proves the
first inequality in (4.3).  Its right side is

\[
 O_A(W_m/\sqrt m)+O_A(m)=o(W_m)
\]

after division by $Q_m$.  The established refined-prefix realization also
makes its physical initialization $o(Q_mW_m)$.

Now prescribe target colors

\[
 (b,\sigma)\in[2m-1]\times S_{2m},
\]

with target color $(b,\sigma)$ carrying
$\operatorname{clip}_H(\sigma\mathcal B)$, where $\mathcal B$ is the
BTK SCD.  For each chain state $\omega$, let $P_\omega$ be its set of
pseudo-occurrence slots and let

\[
 A_\omega=
 \{(b,\sigma):
      \omega\in\operatorname{clip}_H(\sigma\mathcal B)\}.
\]

Orbit transitivity and the exact clipped radius histogram give

\[
 |P_\omega|=|A_\omega|.
 \tag{4.8}
\]

Choose an arbitrary bijection

\[
 \pi_\omega:P_\omega\longrightarrow A_\omega
 \tag{4.9}
\]

independently at every state and give each slot its image color.  Each
target color then receives exactly the chain states of its prescribed
clipped full SCD.  Conversely, every recoloring into the prescribed target
orbit restricts to bijections (4.9).  Thus this is an exact integral SCD
resolution of precisely the same occurrence fibers.

The positive-radius induced rotor graph of every coordinate permutation of
the BTK SCD is empty at every native radius.  This is the audited BTK stack
lemma and is invariant under coordinate relabeling.  Therefore no internal
native-$d$ rotor adjacency, $1\le d<H$, can be monochromatic under any
choice of (4.9).  All $Q_m c_d^{(m)}$ native-$d$ occurrences are separate
monochromatic runs.  Charging only those native radii proves the first
inequality in (4.4); no assertion about the clipped top is used.

Finally,

\[
 c_d^{(m)}
 =N_d^{(m)}\frac{2d+1}{m+d+1},
 \tag{4.10}
\]

and (2.9) holds uniformly for $d\le A\sqrt m+O(1)$.  Hence

\[
 \frac1{W_m\sqrt m}
 \sum_{d=1}^{H-1}2d\,c_d^{(m)}
 \longrightarrow4\int_0^Ax^2e^{-x^2}\,dx.
\]

Integration by parts gives (4.5), whose positivity is immediate from its
integral form.  $\square$

### 4.1 Exact first invalid implication

The failure occurs when a low-toll pseudo adjacency is assumed to survive
statewise recoloring.  Conditions (4.8)--(4.9) constrain each state fiber
separately; a rotor adjacency couples two different fibers.  In the BTK
target orbit, every possible conditional-expectation outcome is bad, not
merely the average outcome.

Thus none of the following data is sufficient, by itself, to guarantee a
low-toll full SCD under a prescribed statewise target-orbit resolution:

1. exact equality of all state marginals;
2. an exact integral occurrence multicover;
3. statewise Birkhoff resolvability into genuine SCD colors;
4. an $o(Q_mW_m)$-toll uncolored or pseudo-colored chronology.

The required datum is a common arc-correlated coloring.  Optimizing that
datum is not an averaging argument: by the exact arbitrary-weight master
identity, its optimum is precisely

\[
 Q_m\min_{\mathcal D}\widehat\Phi_H(\mathcal D),
\]

which is $\mathrm{RSCD}_A$ itself.

### 4.2 An exact whole-atom thinning obstruction

There is also a purely integral obstruction before any asymptotics enter.
It shows that an exact multicover by literal rotor-path atoms cannot in
general be thinned by selecting whole atoms.

### Proposition 4.2 (an integral two-cover with no one-cover selector)

For every $d\ge1$ and $m\ge d+1$, there is a mask-disjoint family of
$2d+2$ native radius-$d$ symmetric chains and an exact integral two-fold
cover of that family by literal directed rotor-path atoms such that no
subcollection of the atoms covers every chain exactly once.

#### Proof

Put $n=2d+2$.  Partition $[2m]$ into disjoint sets

\[
 K,\quad E,\quad \{a_0,\ldots,a_{n-1}\},
 \qquad
 |K|=|E|=m-d-1,
\]

and read active indices modulo $n$.  For $t\in\mathbb Z/n\mathbb Z$, set

\[
 \omega_t=
 \bigl(
 K+\{a_t\};
 a_{t-1},a_{t-2},\ldots,a_{t-2d};
 E+\{a_{t+1}\}
 \bigr).
 \tag{4.11}
\]

In the rotor rule (1.1), choose $x=a_t$ and $y=a_{t+1}$.  Since
$a_{t-2d}=a_{t+2}$ modulo $n$, direct substitution gives

\[
 \omega_t\longrightarrow\omega_{t+1}.
 \tag{4.12}
\]

Thus the states form a directed rotor cycle of length $n$.

The $j$-th mask of the chain represented by $\omega_t$ (at absolute rank
$m-d+j$), for $0\le j\le2d$, has active part

\[
 \{a_t,a_{t-1},\ldots,a_{t-j}\}.
 \tag{4.13}
\]

For fixed $j$, these are the $n$ distinct nonempty proper cyclic intervals
of length $j+1$.  Hence the $n$ symmetric chains are pairwise mask-disjoint.

Partition the directed cycle into three nonempty consecutive vertex paths
$P_0,P_1,P_2$.  For $i$ modulo three, let $T_i$ be the directed path formed
by $P_i$, the connecting rotor edge, and $P_{i+1}$.  The omitted third
chunk is nonempty, so each $T_i$ is a path rather than the whole directed
cycle.  Each $\omega_t\in P_i$ occurs in exactly the two atoms
$T_{i-1},T_i$.  Therefore $\{T_0,T_1,T_2\}$ is an exact integral two-fold
cover by literal rotor-path atoms.

If a one-fold whole-atom selector existed, with
$x_i\in\{0,1\}$ recording selection of $T_i$, every state in $P_i$ would
give

\[
 x_{i-1}+x_i=1.
 \tag{4.14}
\]

The three equations force alternation around an odd cycle and imply
$x_i=1/2$, a contradiction.  Hence no one-fold whole-atom selector exists.
$\square$

Proposition 4.2 is deliberately local: the displayed partial chain family
is not asserted to extend to a full SCD.  Its exact implication is that no
general desuspension lemma of the form

\[
 \text{``exact integral rotor-atom multicover''}
 \Longrightarrow
 \text{``exact one-fold whole-atom subcover''}
\]

can be valid.  A full-SCD construction must exploit additional global
structure or cut and splice atom interiors; exact multiplicities alone do
not suffice.

## 5. Exact one-layer characterization and conditional recursive composition

The standard $B_2$ recursion is now closed, but the nonstandard recursive
constrained-Hall lift remains logically possible.  At one layer this lift
has an exact integral characterization, not merely a Hall relaxation.

Suppose an exact depth-$h$ band SCD has top states

\[
 v=(L_v;z_1(v),\ldots,z_{2h}(v);R_v),
 \qquad
 U_v=[2m]\setminus R_v.
\]

Choose an active set $A_h$ of exactly $N_{h+1}^{(m)}$ top states and let
$F_A$ be its inherited induced directed path forest.  For an edge
$e:v\to w$ using $x_e\in L_v$ and $y_e\in R_v$, define the two forced
rank-$(m-h-1)$ targets

\[
 \lambda(e)=L_v-\{x_e\},
 \qquad
 \rho(e)=R_v-\{y_e\}.
 \tag{5.A1}
\]

Let $\mathfrak M_-(A_h)$ be the set of perfect matchings

\[
 P^-:A_h\longrightarrow\binom{[2m]}{m-h-1},
 \qquad P^-(v)\subset L_v,
 \tag{5.A2}
\]

and define $\mathfrak M_+(A_h)$ analogously with
$P^+(v)\subset R_v$.  If either matching family is empty, the active set
cannot be extended even after deleting every inherited rotor edge.

### Theorem 5.1 (exact forced-target agreement)

Assume both matching families are nonempty.  For
$P^-\in\mathfrak M_-(A_h)$ and $P^+\in\mathfrak M_+(A_h)$, an inherited
edge $e:v\to w$ lifts to a radius-$(h+1)$ rotor edge if and only if

\[
 \boxed{
 P^-(v)=\lambda(e),
 \qquad
 P^+(w)=\rho(e).
 }
 \tag{5.A3}
\]

Consequently, if

\[
 M_h^\star=
 \max_{P^-,P^+}
 \left|
 \{e=v\to w\in E(F_A):
       P^-(v)=\lambda(e),\ P^+(w)=\rho(e)\}
 \right|,
 \tag{5.A4}
\]

then the exact minimum number of inherited active edges that must be cut is

\[
 \boxed{k_h^{\min}=|E(F_A)|-M_h^\star.}
 \tag{5.A5}
\]

#### Proof

An extension of a top state chooses $\ell_v\in L_v$ and $u_v\in R_v$.
Its new lower endpoint and upper-complement endpoint are

\[
 P^-(v)=L_v-\{\ell_v\},
 \qquad
 P^+(v)=R_v-\{u_v\}.
 \tag{5.A6}
\]

The exact one-edge rotor-lift criterion is

\[
 \ell_v=x_e,
 \qquad
 u_w=z_{2h}(v),
 \qquad
 \ell_w\ne y_e,
 \qquad
 u_v\ne y_e
 \tag{5.A7}
\]

for $h\ge1$; at $h=0$, the second equality is $u_w=x_e$.
The first equality in (5.A7) is equivalent to
$P^-(v)=L_v-\{x_e\}=\lambda(e)$.  For $h\ge1$ the rotor rule gives

\[
 R_w=R_v-\{y_e\}+\{z_{2h}(v)\},
\]

so the second equality is equivalent to
$P^+(w)=R_v-\{y_e\}=\rho(e)$.  The same conclusion at $h=0$ follows from
$R_w=R_v-\{y_e\}+\{x_e\}$.

It remains to check that the two inequalities in (5.A7) impose no further
condition.  If $\ell_w=y_e$, then

\[
 P^-(w)=L_w-\{y_e\}=L_v-\{x_e\}=P^-(v),
\]

contrary to injectivity of the perfect matching $P^-$.  If $u_v=y_e$,
then

\[
 P^+(v)=R_v-\{y_e\}=P^+(w),
\]

contrary to injectivity of $P^+$.  Thus (5.A3) is equivalent to the full
edge-lift criterion.

For a fixed pair of matchings, all edges in its agreement set lift
simultaneously, because they are a subforest and use the already fixed
endpoint choices.  Conversely every exact extension supplies the two
perfect matchings (5.A6), and its retained edges lie in their agreement
set.  Maximizing the agreement proves (5.A5).  $\square$

Form the bipartite multigraph $\mathscr B_h$ whose two vertex classes are
rank-$(m-h-1)$ masks and whose edge occurrence $e$ joins
$\lambda(e)$ to $\rho(e)$.  Let $\nu_h$ be its matching number.  Every
agreement set in (5.A4) is a matching in $\mathscr B_h$, so
$M_h^\star\le\nu_h$ and

\[
 \boxed{
 k_h^{\min}
 =\underbrace{|E(F_A)|-\nu_h}_{\text{paired-rainbow defect}}
 +\underbrace{\nu_h-M_h^\star}_{\text{Boolean extendability loss}}.
 }
 \tag{5.A8}
\]

This theorem is the exact one-layer composing lemma for the surviving
recursive architecture; it is not an exact global dynamic characterization.
Fix $A>0$ and put $H=\lceil A\sqrt m\rceil$.  With the globally contiguous
active blocks and inherited forest ledger, suppose that for all sufficiently
large $m$ there is one recursively consistent sequence of active sets and
locally maximizing matching pairs, both matching families exist at every
layer of that same sequence, write $F_{A,h}$ for its active forest at layer
$h$, and assume

\[
 \sum_{h=0}^{H-1}
 \left[(|E(F_{A,h})|-\nu_h)+(\nu_h-M_h^\star)\right]
 =o(W_m/H),
 \tag{5.A9}
\]

then those compatible maximizing matchings give $K_H=o(W_m/H)$.  The exact
recursive toll identity then gives $\widehat\Phi_H=o(W_m)$, and the
central-band extension gives one full integral SCD.  Thus (5.A9) proves
$\mathrm{RSCD}_A$ for this fixed $A$.  If the hypothesis holds for every
fixed $A>0$, the established literal rotor/tail construction followed by
the usual diagonalization $A\to\infty$ yields constant one.  Condition
(5.A9) remains unproved; Theorem 5.1 and this conditional implication are
proved.  Local maximizing pairs need not be recursively compatible, which
is why compatibility is an explicit hypothesis.

The following simpler duplicate-excess bound is an immediate necessary
consequence and is useful at the first odd-cut layer.

For an edge $e:v\to w$, define

\[
 M^-(e)=L_v\cap L_w=L_v-\{x_e\},
 \tag{5.1}
\]

\[
 M^+(e)=U_v\cup U_w=U_v+\{y_e\}.
 \tag{5.2}
\]

For either sign, put

\[
 \mu^\pm(S)=|\{e\in E(F_A):M^\pm(e)=S\}|,
 \qquad
 E_h^\pm=\sum_S(\mu^\pm(S)-1)_+.
 \tag{5.3}
\]

### Corollary 5.2 (duplicate-excess lower bound on recursive cuts)

If deleting $k_h$ further edges from $F_A$ leaves a forest admitting an
exact one-layer SCD extension that preserves every retained rotor edge, then

\[
 \boxed{k_h\ge\max(E_h^-,E_h^+).}
 \tag{5.4}
\]

#### Proof

An extension of $v$ chooses

\[
 \ell_v\in L_v,
 \qquad
 u_v\in R_v,
\]

and has new lower and upper endpoints

\[
 \widetilde L_v=L_v-\{\ell_v\},
 \qquad
 \widetilde U_v=U_v+\{u_v\}.
 \tag{5.5}
\]

For a retained rotor edge $e:v\to w$, exact rotor compatibility forces

\[
 \ell_v=x_e
 \tag{5.6}
\]

and, for $h\ge1$,

\[
 u_w=z_{2h}(v).
 \tag{5.7}
\]

At $h=0$, (5.7) is replaced by $u_w=x_e$.  From (5.1), (5.5),
(5.6),

\[
 \widetilde L_v=M^-(e).
 \tag{5.8}
\]

For $h\ge1$, the rotor rule gives

\[
 U_w=U_v+\{y_e\}-\{z_{2h}(v)\},
\]

so (5.7) gives

\[
 \widetilde U_w=U_v+\{y_e\}=M^+(e).
 \tag{5.9}
\]

The same conclusion follows at $h=0$ with $x_e$ in place of
$z_{2h}(v)$.

In an exact one-layer SCD extension, the maps
$v\mapsto\widetilde L_v$ and $v\mapsto\widetilde U_v$ are bijections
onto their respective new boundary ranks.  Distinct retained forest edges
have distinct sources and distinct targets.  Equations (5.8)--(5.9)
therefore force the retained $M^-$-colors to be injective and the retained
$M^+$-colors to be injective.

Deleting one edge reduces either duplicate excess in (5.3) by at most one.
To make the lower colors injective requires at least $E_h^-$ deletions,
and to make the upper colors injective requires at least $E_h^+$
deletions.  The same deletion can repair one duplicate of each sign, so the
rigorous combined lower bound is their maximum, not their sum.  This proves
(5.4).  $\square$

### Corollary 5.3 (the odd cut must have vanishing meet defect)

Let the initial odd-cut middle forest have

\[
 B=\operatorname{Cat}_m=\frac{W_m}{m+1}
\]

paths.  Each has $m+1$ vertices and $m$ edges, so the forest has

\[
 mB=W_m-B=N_1^{(m)}
\]

edges.  Its join colors are pairwise distinct.  Define its full meet defect

\[
 E_{\rm cut}^-
 =\sum_{S\in\binom{[2m]}{m-1}}
   (\mu_{\rm cut}^-(S)-1)_+.
 \tag{5.10}
\]

At the first recursive lift, assign the $N_1^{(m)}$ active centers as one
global suffix of a concatenation of the $B$ odd-cut paths.  If $b_A$ is
the number of nonempty active runs, then

\[
 b_A\le B
 \tag{5.11}
\]

because each original path contributes at most one suffix run.  The active
induced forest has $N_1^{(m)}-b_A$ edges, whereas the full odd-cut forest
has $N_1^{(m)}$ edges.  Passing to the active forest therefore deletes
exactly $b_A$ edges and reduces meet duplicate excess by at most $b_A$.
Corollary 5.2 gives the exact necessity

\[
 \boxed{
 k_0\ge(E_{\rm cut}^--b_A)_+
     \ge(E_{\rm cut}^--\operatorname{Cat}_m)_+.
 }
 \tag{5.12}
\]

The constrained recursive Hall lift at window
$H=\lceil A\sqrt m\rceil$ requires

\[
 K_H=\sum_{h=0}^{H-1}k_h=o(W_m/H).
\]

Since $k_0\le K_H$ and

\[
 \frac{\operatorname{Cat}_m}{W_m/H}
 =\frac{H}{m+1}=o(1),
\]

it necessarily follows that

\[
 \boxed{E_{\rm cut}^-=o(W_m/\sqrt m).}
 \tag{5.13}
\]

This condition is necessary, not sufficient.  The remaining endpoint
inequalities and the two full Hall systems can create additional defects.
The join family being rainbow only says $E_{0,A}^+=0$; it does not solve
the upper cap Hall system.

## 6. Audit, integrality, and implication scope

### 6.1 Independent audits

The decisive new-coordinate signature argument was checked independently.
The audit specifically verified:

1. the four signatures in (2.2) are exhaustive;
2. the $d=1$ case cannot be inferred from the shifted-position argument
   and requires the separate lower-block/singleton-position check given
   above;
3. the clipped top $d=H$ must be omitted;
4. the exact-prefix weight is $2d$, not $2d+1$;
5. the telescoping constant in (2.5) is exact.

The multicover theorem was audited independently by recomputing both
telescoping identities, the BTK native-radius restriction, and the Riemann
constant (4.5).  The forced-target theorem was checked in both directions;
in particular, the two apparent endpoint inequalities in (5.A7) really do
follow from injectivity of the two perfect matchings.  The duplicate-excess
corollary was separately checked against the exact one-layer rotor
equalities at $h=0$ and $h\ge1$.

A final adversarial audit also verified the mask-disjoint rotor cycle and
odd-cycle selector contradiction in Proposition 4.2, the dense-surgery
constants (3.3)--(3.5), the fixed-$A$ quantifier in (5.A9), and the need for
one recursively compatible sequence rather than unrelated layerwise
maximizers.  It found no remaining mathematical error after the stated
scope qualifications were inserted.

### 6.2 What is now rigorously closed

The following routes cannot yield $\widehat\Phi_H=o(W)$:

1. standard two-coordinate product recursion from any parent SCD, with an
   arbitrary phase field;
2. whole-chain multicolor trades among labelled copies of the two standard
   phases over the same parent-chain boxes;
3. any $o(W)$-state or $o(W)$-whole-chain repair of an output from (1)
   or (2);
4. selection into a prescribed target orbit based only on exact state
   marginals, statewise Birkhoff factors, separate convexity, or uncoupled
   conditional expectation in the exact rotor occurrence multicover;
5. a black-box assertion that every exact integral rotor-atom multicover
   contains an exact one-fold whole-atom subcover.

The multiframe $\mathsf A\to\mathsf D\to\mathsf B$ braid is not a
counterexample to Theorem 2.1: it changes radius and pays a recency inversion
at a cross-type seam.  The theorem says precisely that this braid cannot be
recolored or reinterpreted as one low-toll fixed-radius rotor forest inside
its standard product SCD.

### 6.3 What remains unproved

No theorem here excludes:

1. a nonstandard product decomposition;
2. dense cross-parent splicing that replaces $\Omega(W)$ chains;
3. an arc-correlated construction of a genuinely different SCD;
4. a recursively consistent forced-target agreement sequence satisfying
   (5.A9), after the meet-defect and all later Hall gates are solved;
5. a direct literal OR word that does not remain in the fixed-radius
   SCD/rotor architecture.

Thus this report does not prove a lower bound for arbitrary contiguous-OR
words and does not refute the constant-one conjecture.  It definitively
closes the assigned standard recursive selection mechanism and identifies
the first exact condition on the presently formulated no-merger CRHL
mechanism.

### 6.4 Literal realizability

Every SCD in Theorems 2.1 and 3.1 is a full integral SCD.  Every rotor path
used in the toll definition has the established refined-prefix literal OR
realization with exact hard-start cost $2d$.  The pseudo-orbit in Theorem
4.1 also consists of legitimate integral rotor states and paths, but one
pseudo-color is explicitly not asserted to be an SCD; it is used only as a
counterexample to a selection implication.  No fractional object is
promoted to a full SCD or to a literal constant-one word.

The quantitative conclusion for lane S is therefore a no-go, not a claimed
construction: any successful recursive proof of

\[
 \nu(k)\le(1+o(1))W(k)
\]

must leave the entire standard phase multicover, make a dense nonstandard
within-box and/or cross-parent arc-correlated choice, and in the known
recursive Hall architecture begin with an odd cut satisfying (5.13).
