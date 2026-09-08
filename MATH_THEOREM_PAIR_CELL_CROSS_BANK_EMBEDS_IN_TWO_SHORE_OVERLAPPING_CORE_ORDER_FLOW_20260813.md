# The pair-cell cross bank embeds in a two-shore overlapping-core order flow

**Date:** 2026-08-13  
**Status:** unconditional exact bridge plus an exact method obstruction.  A
pure-rail ordering automatically supplies a macroscopic cross-cell bank and
the required parity charge.  Adding the immediate-lower shore to the
overlapping-core ledger forces an exact uniform core/toggle role vector; a
cyclic-orbit construction realizes that vector with genuine shells and can
simultaneously make both named shores fractionally uniform.  Integral
two-shore ordering remains open.  Its natural hypergraph has an unavoidable
owner--facet codegree which defeats the favorable owner-only growing-rank
collision estimate.

## 0. Parameters

Put

\[
 k=2p+1,\qquad R=p+1,\qquad
 \mathcal O={{[k]}\choose R},\qquad
 \mathcal L={{[k]}\choose {R-1}},\qquad
 W=|\mathcal O|=|\mathcal L|.                         \tag{0.1}
\]

Fix a sentinel `z` and matched pairs

\[
 [k]=\{z\}\mathbin{\dot\cup}\bigdotcup_{i=1}^p
 P_i,\qquad P_i=\{a_i,b_i\}.                          \tag{0.2}
\]

Let `q>=2`, put `c=R-q`, and take a legal pure-rail shell

\[
 |C|=c,\qquad |T|=N,\qquad C\cap T=\varnothing,
 \qquad N\ge2q+2.                                      \tag{0.3}
\]

For a cyclic order \(\sigma=(x_i)_{i\in\mathbb Z_N}\) of \(T\), define

\[
 A_i=C\cup\{x_i,x_{i+1},\ldots,x_{i+q-1}\},           \tag{0.4}
\]

\[
 L_i=A_i\cap A_{i+1}
    =C\cup\{x_{i+1},\ldots,x_{i+q-1}\}.               \tag{0.5}
\]

The `A_i` form a simple Johnson cycle and the `L_i` are its distinct
rank-`R-1` edge colours.

## 1. Exact cross-edge incidence of a pure rail

The edge `A_iA_(i+1)` exchanges the two coordinates

\[
                         \{x_i,x_{i+q}\}.              \tag{1.1}
\]

Put

\[
 h_P(\sigma)=
 \left|\left\{i\in\mathbb Z_N:
       \{x_i,x_{i+q}\}=P_j\text{ for some }j\right\}\right|.  \tag{1.2}
\]

### Theorem 1.1 (exact rail cross count and charge)

Relative to the fixed pair structure `(0.2)`, the rail has exactly

\[
                         N-h_P(\sigma)                 \tag{1.3}
\]

cross-cell edges, and

\[
                         h_P(\sigma)\le\lfloor N/2\rfloor.       \tag{1.4}
\]

Consequently every legal pure rail has at least

\[
                         \lceil N/2\rceil              \tag{1.5}
\]

cross-cell edges.

For an edge `e` exchanging `u,v`, define

\[
 \alpha(e)_j=\mathbf1_{\{a_j\in\{u,v\}\}}
       \quad\text{in }\mathbb F_2,
 \qquad
 \eta(e)=1+\sum_j\alpha(e)_j.                         \tag{1.6}
\]

Then every pure rail obeys

\[
 \sum_{e\text{ in the rail}}\alpha(e)=0,
 \qquad
 \sum_{e\text{ in the rail}}\eta(e)=N\pmod2.         \tag{1.7}
\]

#### Proof

Equation `(1.1)` is immediate from consecutive windows.  Such an edge is
internal exactly when its exchanged pair is one of the `P_j`, proving
`(1.3)`.  Since `N>2q`, a matched pair can occur in `(1.2)` at most once:
its two positions cannot be separated by `q` in both cyclic directions.
Different internal transitions use disjoint matched pairs, proving `(1.4)`.

As `i` runs cyclically, every toggle coordinate `x_r` occurs in exactly two
exchange supports, at transitions `r` and `r-q`.  Every distinguished
`a_j` therefore occurs an even number of times, proving the vector identity
in `(1.7)`.  Summing `(1.6)` over the `N` edges gives the scalar identity.
\(\square\)

### Corollary 1.2 (global cross bank)

Let a collection of ordered pure rails have total period

\[
                         \sum_jN_j=W.                 \tag{1.8}
\]

Then it contains at least

\[
 \boxed{
 \sum_j\left\lceil{N_j\over2}\right\rceil\ge {W\over2}}
                                                               \tag{1.9}
\]

cross-cell edges.  Its total cross-edge parity charge is

\[
                         \sum_jN_j=W\pmod2.            \tag{1.10}
\]

In particular, on `p=2^s-1`, the charge is odd automatically.  Thus a
global pure-rail owner factor is a constructive large-bank alternative to
a bounded parity absorber.  This statement is independent of how the
cyclic orders are selected.

At occurrence level the earlier low-cell bound is also automatic.  An
owner with `m` singleton matched pairs has only `m` internal Johnson
neighbours.  Hence a selected rail through a `Q_0` owner supplies two cross
incidences and a selected rail through a `Q_1` owner supplies at least one.

## 2. Adding the lower shore rigidifies the role flow

For a shell collection, before choosing its cyclic orders, put

\[
 K_x=\sum_{j:x\in C_j}N_j,
 \qquad
 U_x=|\{j:x\in T_j\}|.                                 \tag{2.1}
\]

A core point occurs in all `N_j` owner and lower windows of shell `j`.
A toggle point occurs in `q` owner windows and `q-1` lower windows.  Thus
the point loads are

\[
                         K_x+qU_x                     \tag{2.2}
\]

on the owner shore and

\[
                         K_x+(q-1)U_x                 \tag{2.3}
\]

on the lower shore.

### Theorem 2.1 (exact two-shore role vector)

If ordered versions of the shells partition both \(\mathcal O\) and
\(\mathcal L\), then necessarily

\[
 \boxed{
 U_x={W\over k},\qquad K_x=c{W\over k}
 \qquad(x\in[k]).}                                    \tag{2.4}
\]

Conversely `(2.4)` is exactly the simultaneous ground-point ledger for
the two shores.  Here

\[
                         {W\over k}=\operatorname {Cat}_p         \tag{2.5}
\]

is an integer.

#### Proof

Exact owner and lower coverage require respectively

\[
 K_x+qU_x={R\over k}W,
 \qquad
 K_x+(q-1)U_x={R-1\over k}W.                          \tag{2.6}
\]

Subtracting gives `U_x=W/k`; substituting and using `c=R-q` gives
`K_x=cW/k`.  Equation `(2.5)` is the standard Catalan identity

\[
 {1\over2p+1}{2p+1\choose p+1}
 ={1\over p+1}{2p\choose p}.                          \tag{2.7}
\]

\(\square\)

This is stronger than the owner-only equation `K_x+qU_x=RW/k`: exact
lower colours remove all pointwise freedom in the split between core and
toggle roles.

## 3. A deterministic exact overlapping-core shell allocation

Take the consecutive legal periods

\[
                         n=2q+2,\qquad n+1=2q+3,       \tag{3.1}
\]

and assume `n+1<=k-c`.  Put `K=W/k`.  Assume

\[
                         K\ge n^2-1.                  \tag{3.2}
\]

Choose the unique \(0\le B<n\) satisfying \(B\equiv K\pmod n\) and put

\[
                         A={K-(n+1)B\over n}.          \tag{3.3}
\]

Then `A,B` are nonnegative integers and

\[
                         nA+(n+1)B=K.                 \tag{3.4}
\]

Fix one regular cyclic permutation `tau` of `[k]`.  One **orbit block**
of period `N` is obtained by choosing any disjoint base pair

\[
                         |C|=c,\qquad |T|=N            \tag{3.5}
\]

and taking the `k` labelled shells

\[
                         (\tau^rC,\tau^rT,N),
                         \qquad r\in\mathbb Z_k.       \tag{3.6}
\]

### Theorem 3.1 (exact two-shore orbit role flow)

Take `A` orbit blocks of period `n` and `B` orbit blocks of period `n+1`,
with arbitrary base pairs in each block.  The resulting genuine shell
multiset satisfies

\[
 \sum_jN_j=W,
 \qquad
 U_x=K,
 \qquad
 K_x=cK\quad(x\in[k]).                                \tag{3.7}
\]

Therefore it satisfies the exact owner and lower ground-point ledgers
simultaneously.

#### Proof

In one orbit block every point lies in exactly `c` translated cores and in
exactly `N` translated supports.  The core contribution at that point is
therefore `Nc`, while its support incidence is `N`.  Sum over the blocks
and use `(3.4)`.  The total period is

\[
 k(nA+(n+1)B)=kK=W.                                   \tag{3.8}
\]

Theorem 2.1 completes the proof. \(\square\)

The construction is positive and deterministic.  Different orbit blocks
may overlap, as required in the overlapping-core programme; every
individual core is disjoint from its own support.

## 4. Exact point roles coexist with two-shore fractional uniformity

For a fixed shell `(C,T,N)`, give every cyclic order of `T` equal weight.
Its contribution to a named owner `A` is

\[
 X^+_{N,A}={N\over{N\choose q}}
 \mathbf1_{\{C\subset A,\ A-C\subseteq T\}},          \tag{4.1}
\]

and its contribution to a named lower colour `L` is

\[
 X^-_{N,L}={N\over{N\choose {q-1}}}
 \mathbf1_{\{C\subset L,\ L-C\subseteq T\}}.         \tag{4.2}
\]

Put

\[
 b=\max_{N\in\{n,n+1\}}
 \max\left\{{N\over{N\choose q}},
             {N\over{N\choose {q-1}}}\right\}.        \tag{4.3}
\]

### Theorem 4.1 (orbit-conditioned two-shore checkpoint)

In each orbit block of Theorem 3.1, choose its base pair independently and
uniformly from all disjoint `(c,N)` pairs.  If

\[
                         \eta=4\sqrt{kb\log(8W)}\le1,   \tag{4.4}
\]

then with positive probability the shell multiset still satisfies the
exact role equations `(3.7)` and, simultaneously,

\[
 \boxed{
 |L_A^+-1|\le\eta\quad(A\in\mathcal O),
 \qquad
 |L_L^--1|\le\eta\quad(L\in\mathcal L),}              \tag{4.5}
\]

where the loads use the uniform order distribution on each frozen shell.
Consequently a deterministic shell multiset with `(3.7)` and `(4.5)`
exists.

For `q=Theta(sqrt(k))`,

\[
                         \eta=e^{-\Omega(q)}.           \tag{4.6}
\]

#### Proof

Every orbit block satisfies `(3.7)` for every choice of its base pair.
Fix a named owner.  One translated shell has expected contribution `N/W`
by transitivity: a shell has exactly `{N choose q}` eligible owners and
uniform ordering gives each eligible owner window probability
`N/{N choose q}`.  A full orbit block therefore has mean `kN/W`.
The same argument on the equally large lower shore, using `(4.2)`, gives
the same mean for a named lower colour.

For either named row, one orbit-block contribution lies in `[0,kb]`.
The blocks are independent, their total mean is one by `(3.4)`, and hence
their total variance is at most `kb`.  Bernstein's inequality gives, for
`0<eta<=1`,

\[
 \Pr(|L-1|>\eta)
 \le2\exp\left(-{3\eta^2\over8kb}\right).             \tag{4.7}
\]

With `(4.4)` this is at most `2(8W)^(-6)`.  A union bound over the `2W`
named rows is strictly below one.

For the periods `(3.1)`, `b=O(q^2 4^{-q})`; since `log W=O(k)`, equation
`(4.4)` is exponentially small in `q` in the central regime. \(\square\)

This closes the former separation between exact ground-point roles and
named-owner fractional concentration, and does so on both equal shores.
It is still a fractional-order checkpoint, not an integral factor.

## 5. The exact two-shore named-order system

Freeze any shells satisfying `(3.7)`.  For token `j`, let `Omega_j` be
the cyclic orders of `T_j`, modulo rotation, and introduce

\[
                         z_{j,\sigma}\in\{0,1\}.       \tag{5.1}
\]

There is a pure-rail exact owner/lower factor on these shells if and only if

\[
 \sum_{\sigma\in\Omega_j}z_{j,\sigma}=1
                         \qquad(j),                    \tag{5.2}
\]

\[
 \sum_{j:C_j\subset A}
 \sum_{\substack{\sigma:\ A-C_j\text{ is a cyclic }q\text{-window}}}
 z_{j,\sigma}=1
                         \qquad(A\in\mathcal O),       \tag{5.3}
\]

and

\[
 \boxed{
 \sum_{j:C_j\subset L}
 \sum_{\substack{\sigma:\ L-C_j\text{ is a cyclic }(q-1)\text{-window}}}
 z_{j,\sigma}=1
                         \qquad(L\in\mathcal L).}      \tag{5.4}
\]

Equations `(5.2)--(5.4)` are an exact multiple-choice two-shore matching
system.  Any integral solution is already a global cross-cell analogue:
it has the bank `(1.9)`, exact charge `(1.10)`, every owner once, and every
lower colour once.  No separate pair-cell absorber row is required.

The transversal lift can be protected in the same formulation.  If `Y`
and `Z` are its owner and lower shores, restrict every selected rail deck
to avoid `Y cup Z` and replace the right sides in `(5.3)--(5.4)` by the
indicators of \(\mathcal O-Y\) and \(\mathcal L-Z\).  If

\[
 y_x=|\{A\in Y:x\in A\}|,
 \qquad z_x=|\{L\in Z:x\in L\}|,                      \tag{5.5}
\]

then the exact residual role targets are

\[
 \boxed{
 U_x={W\over k}-y_x+z_x,
 \qquad
 K_x=c{W\over k}+(q-1)y_x-qz_x.}                      \tag{5.6}
\]

These identities are necessary for a protected two-shore shell bank and
follow by subtracting the protected point loads from `(2.6)`.  Their total
sums are correct and they are positive for all sufficiently large `p`, but
this note does not construct the nonuniform protected shell allocation.

## 6. Exact codegree barrier for direct growing-rank rounding

Take the complete parameterized orbit of all period-`N` pure rails and
form a hypergraph on

\[
                         \mathcal O\mathbin{\dot\cup}\mathcal L,        \tag{6.1}
\]

where one hyperedge consists of the `N` owners and `N` lower colours of one
ordered rail.  Symmetry and `|mathcal O|=|mathcal L|` make it regular, and
uniform edge weights form an exact fractional perfect matching on both
shores.

### Theorem 6.1 (forced owner--facet codegree)

Let `D_N` be the common vertex degree of the complete two-shore orbit
hypergraph.  For every incident pair \(L\subset A\),

\[
 \boxed{
 \deg(A,L)={2\over R}D_N.}                             \tag{6.2}
\]

Consequently

\[
                         {\Delta_2\over D_N}\ge{2\over R}.       \tag{6.3}
\]

Since the joint edge size is `2N`,

\[
 (2N)^2{\Delta_2\over D_N}
 \ge {8N^2\over R}.                                   \tag{6.4}
\]

For `N=2q+O(1)` and `q=Theta(sqrt R)`, the right side is bounded away
from zero.  Thus the favorable owner-only collision parameter
\(N^2\Delta_2/D=\Theta(k^{-1})\) does not survive the literal addition of the
lower shore.

#### Proof

Fix an owner occurrence `A_i` in one rail.  Exactly two lower windows of
that rail are subsets of it, namely its two incident edge colours
`L_(i-1),L_i`.  Because `N>2q`, no other cyclic `(q-1)`-window is contained
in its cyclic `q`-window.  Summing the codegrees `deg(A,L)` over the `R`
facets \(L\subset A\) therefore gives \(2D_N\).  The stabilizer of `A` in the
full symmetric orbit acts transitively on those facets, so all `R`
codegrees are equal.  This proves `(6.2)--(6.4)`. \(\square\)

Equation `(6.4)` is a method obstruction, not a nonexistence theorem.  It
rules out importing any owner-only growing-uniformity argument whose error
requires the squared edge size times normalized codegree to vanish.  A
successful integral proof must exploit the deterministic pairing between
each owner occurrence and its two rail facets, use a partite/conflict
matching theorem adapted to that incidence, or absorb a structured leave.

## 7. Scope

The exact bridge is now:

\[
 \boxed{
 \begin{gathered}
 \text{cyclic orbit blocks}\Rightarrow
 \text{exact owner/lower point roles},\\
 \text{random orbit bases}\Rightarrow
 \text{simultaneous two-shore fractional named loads},\\
 \text{integral equations }(5.2)--(5.4)\Rightarrow
 \text{a global parity-correct cross-cell factor}.
 \end{gathered}}                                      \tag{7.1}
\]

The remaining obstruction is no longer cross-edge supply.  It is integral
two-shore cyclic ordering with its forced owner--facet correlations.  The
theorem does not solve `(5.2)--(5.4)`, preserve upper support or source
flags, make one component, or construct the nonuniform shell allocation
around a protected transversal lift.
