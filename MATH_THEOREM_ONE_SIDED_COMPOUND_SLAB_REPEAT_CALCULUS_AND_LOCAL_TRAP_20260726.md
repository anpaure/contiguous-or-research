# One-sided compound-slab calculus for repeats and holes

Date: 2026-07-26

This note replaces the quadratic CPCR derivative by the exact one-sided
objective

\[
\mathcal R(L)=\sum_T(L(T)-1)_+.
\]

It is conditional on the asserted literal slab catalogue.  The negative
example below is an exact scalable packet-image incidence model satisfying
all presently used slab mass and injectivity axioms; it is not claimed to be
a Johnson/compiler realization.

## 1. The master threshold identity

Let (L\in\mathbb Z_{\ge0}^{\mathcal T}), let
(\delta\in\mathbb Z^{\mathcal T}), assume (L+\delta\ge0), and assume the
move preserves occurrence mass:

\[
\sum_T\delta(T)=0.
\]

Since

\[
(z-1)_+=z-\mathbf1_{\{z>0\}},
\]

one has the exact identity

\[
\boxed{
\mathcal R(L+\delta)-\mathcal R(L)
=\#\{T:L(T)>0,\ L(T)+\delta(T)=0\}
-\#\{T:L(T)=0,\ \delta(T)>0\}.
}
\tag{1.1}
\]

Thus a compound move improves the repeat objective if and only if it fills
more old holes than the number of covered targets it empties.  Multiplicity
changes which stay on the positive side of the threshold cancel globally.

If (M(L)=\#\{T:L(T)=0\}), then the same formula gives

\[
\boxed{
M(L+\delta)-M(L)
=\mathcal R(L+\delta)-\mathcal R(L).
}
\tag{1.2}
\]

This is also immediate from (M=N-G+\mathcal R), because (N,G) are fixed.

## 2. Exact single-slab score

Fix one slab (t), remove its current shore, and let (B_t) be the load of
all other choice groups.  Every slab resolution has an internally rainbow
image

\[
\Gamma_{t,a}\in\{0,1\}^{\mathcal T},\qquad
\sum_T\Gamma_{t,a}(T)=m_t.
\]

For every alternative (a),

\[
\boxed{
\mathcal R(B_t+\Gamma_{t,a})
=\mathcal R(B_t)
\sum_{T:B_t(T)\ge1}\Gamma_{t,a}(T).
}
\tag{2.1}
\]

Equivalently,

\[
M(B_t+\Gamma_{t,a})
=M(B_t)-\sum_{T:B_t(T)=0}\Gamma_{t,a}(T).
\tag{2.2}
\]

Therefore the exact one-slab score is

\[
s_t(a)=|\operatorname{supp}\Gamma_{t,a}
          \cap\operatorname{supp}B_t|,
\tag{2.3}
\]

and the current shore is slab-locally minimal if and only if it minimizes
(s_t(a)), or equivalently maximizes the number of background holes hit by
its image.  This score sees only the zero/nonzero threshold of the
background, not its load magnitudes.

For a current state (a_0) and
(\delta_{t,a}=\Gamma_{t,a}-\Gamma_{t,a_0}), (2.1) becomes

\[
\mathcal R(L+\delta_{t,a})-\mathcal R(L)
=\sum_{T:B_t(T)\ge1}\delta_{t,a}(T)
=-\sum_{T:B_t(T)=0}\delta_{t,a}(T).
\tag{2.4}
\]

## 3. Exact compound score

Let (S) be a simultaneously legal family of slabs.  Remove all their
current shores and call the outside load (B_S).  For one joint resolution
(x=(a_t)_{t\in S}), put

\[
k_x(T)=\sum_{t\in S}\Gamma_{t,a_t}(T).
\]

Then

\[
\boxed{
\begin{aligned}
\mathcal R(B_S+k_x)
&=\mathcal R(B_S)
 +\sum_{T:B_S(T)>0}k_x(T)
 +\sum_{T:B_S(T)=0}(k_x(T)-1)_+,\\
M(B_S+k_x)
&=\#\{T:B_S(T)=0,\ k_x(T)=0\}.
\end{aligned}}
\tag{3.1}
\]

Thus the compound problem is linear on targets already occupied by the
outside background.  All nonlinear interaction is the collision functional
among the selected slab images on the outside holes.

There is also an exact holonomy expansion relative to the original load
(L).  Let (\delta_t\in\{-1,0,1\}^{\mathcal T}) be the individual
derivatives, and for each target write

\[
p_T=\#\{t\in S:\delta_t(T)=+1\},\qquad
n_T=\#\{t\in S:\delta_t(T)=-1\}.
\]

Assume every individual move and the compound move are legal.  If
(g_t=\mathcal R(L+\delta_t)-\mathcal R(L)), then

\[
\boxed{
\begin{aligned}
\mathcal R\!\left(L+\sum_{t\in S}\delta_t\right)-\mathcal R(L)
=\sum_{t\in S}g_t
&+\sum_{T:L(T)=0}(p_T-1)_+\\
&-\#\{T:L(T)=1,\ n_T=1,\ p_T\ge1\}\\
&+\#\{T:L(T)\ge2,\ n_T-p_T=L(T)\}.
\end{aligned}}
\tag{3.2}
\]

The three interaction terms have distinct meanings:

1. several slabs try to fill the same hole, producing diminishing return;
2. a positive incidence rescues a target which one slab would have emptied;
3. several removals jointly empty a multiply covered target.

Formula (3.2), unlike quadratic overlap holonomy, depends only on threshold
crossings.

## 4. Discrete convexity: the precise verdict

On the full fixed-mass load lattice

\[
\{L\in\mathbb Z_{\ge0}^{N}:\sum_TL(T)=G\},
\]

the function (\mathcal R(L)) is separable convex and hence (M)-convex.
Indeed the discrete increments of ((z-1)_+) are (0,1,1,\ldots).  If a
hole and a target of load at least two coexist, transferring one occurrence
from the latter to the former lowers (\mathcal R) by exactly one.  Hence

\[
\boxed{
\mathcal R(L)- (G-N)_+
=M(L)-(N-G)_+
}
\tag{4.1}
\]

is both the exact number of excess holes and the exact number of unrestricted
unit transfers needed to reach an optimal support.

This (M)-convexity does **not** survive restriction to whole legal slab
images.  On the unrestricted ground set of resolution options, the natural
extension

\[
A\longmapsto
\sum_{e\in A}|I_e|-\left|\bigcup_{e\in A}I_e\right|
\tag{4.2}
\]

is supermodular, because union coverage is submodular.  The legal domain is a
partition-base domain: exactly one option must be chosen from every slab.
Replacing one option simultaneously removes one set and adds another, and
the pullback to the binary replacement coordinates can be neither
submodular nor supermodular.

Two three-target examples show both signs of the mixed second difference.

* From (L=(0,1,1)), let
  (\delta_1=(1,-1,0)), (\delta_2=(1,0,-1)).  The four repeat values are
  (0,0,0,1), giving positive mixed difference and violating
  submodularity.
* From (L=(1,0,1)), let
  (\delta_1=(-1,1,0)), (\delta_2=(1,0,-1)).  The four values are
  (0,0,1,0), giving negative mixed difference and violating
  supermodularity.

Common private incidences pad these unit moves to any required equal slab
mass.  Thus no submodular exchange theorem follows from equal shore mass.

## 5. A scalable strict local minimum for the repeat objective

Put (s=2^R) and (L_0=s/2).  Index eight independent slab variables by
(v\in Q_3).  Every variable has its full resolution menu; choose one current
label (a_v^0) and define

\[
\chi_v(a_v^0)=x_0(v),\qquad
\chi_v(a)=1-x_0(v)\quad(a\ne a_v^0),
\qquad x_0(v)=v_1\oplus v_2.
\tag{5.1}
\]

For every (v), create a private block (P_v) of size (L_0), common to
all resolutions of that slab.  For every cube edge (e\in E(Q_3)) and
(b\in\{0,1\}), create a block (T_{e,b}) of size (L_0).  All blocks are
disjoint.  Set

\[
I_{v,a}
=P_v\ \dot\cup\!
 \mathop{\dot\bigcup}_{e\ni v}T_{e,\chi_v(a)}.
\tag{5.2}
\]

Every option is a (0)-(1) image of size

\[
|I_{v,a}|=4L_0=2s,
\]

exactly the mass of a two-packet slab resolution.  The target universe has

\[
N=(8+2|E(Q_3)|)L_0=32L_0,
\]

and the eight chosen images also have total occurrence mass (G_0=32L_0=N).
If desired, add a fixed state-independent background of total mass (D),
supported on the always-covered private blocks.  Then (G=N+D), while every
state comparison below is unchanged.

For a color choice (x:Q_3\to\{0,1\}), a private block has load one.  On an
edge (uv), the two color blocks have loads (1,1) when (x(u)\ne x(v)),
and loads (2,0) when (x(u)=x(v)).  Therefore

\[
\boxed{
\mathcal R(x)=D+L_0\,m(x),\qquad
M(x)=L_0\,m(x),
}
\tag{5.3}

where (m(x)) is the number of monochromatic cube edges.

At (x_0(v)=v_1\oplus v_2), exactly the four direction-three edges are
monochromatic.  Every vertex is incident with one monochromatic and two
bichromatic edges.  Changing one slab to any alternative flips its color,
destroys one monochromatic edge, and creates two.  Hence every one-slab move
strictly increases (\mathcal R) and (M) by (L_0).

But

\[
x_*(v)=v_1\oplus v_2\oplus v_3
\]

is bichromatic on every cube edge, so

\[
\mathcal R(x_0)=D+4L_0,qquad
\mathcal R(x_*)=D,qquad
M(x_0)=4L_0,qquad M(x_*)=0.
\tag{5.4}
\]

Thus (x_0) is a strict one-slab local minimum with linear excess repeats
and holes, while a four-slab compound exchange reaches the global support
optimum.  Direct sums give this trap at arbitrary scale.  Direction-support
marginals may be added occurrencewise exactly as in the existing quadratic
(Q_3) audit, without changing any target load.

Under the natural one-hot encoding of slab resolutions, an (M)-convex
function has the unit-exchange local-to-global property.  The state (x_0)
violates that property.  Consequently the repeat objective is not
(M)-convex on the legal slab state space at the level of the currently
proved image axioms.

## 6. Exact remaining literal theorem

The countermodel does not prove that the literal diverse-order compiler
realizes the frustrated (Q_3) incidence pattern.  It proves that exact
ownership, equal shore mass, within-shore injectivity, direction marginals,
and the full slab resolution menu do not imply one-sided descent.

A positive literal result must use additional compiler geometry to prove a
coverage-coercivity statement such as

\[
M(L)\ge\varepsilon W
\quad\Longrightarrow\quad
\exists\text{ legal compound slab move }\delta:
\#\{L=0,\delta>0\}
>\#\{L>0,L+\delta=0\}.
\tag{6.1}
\]

No currently cited slab theorem proves (6.1).  The quadratic CPCR local trap
was therefore not an artefact of the quadratic objective: the same scalable
frustration persists for the exact missing-target/repeat objective.

