# Ordered Boolean diamonds: the JMS perfect-completion proof fails, but a high-girth `N-o(N)` four-transversal follows

Date: 2026-08-01  
Status: definitive theorem-hypothesis audit and strongest presently justified
black-box fallback for this exact four-uniform host.  The exact ordered
four-transversal remains open.

Primary sources:

* F. Joos, D. Mubayi, Z. Smith, *Conflict-free Hypergraph Matchings and
  Coverings*, [arXiv:2407.18144v2](https://arxiv.org/abs/2407.18144),
  especially (S2), (H1), (H2), and Theorem 3.1.
* M. Delcourt, L. Postle, *Finding an almost perfect matching in a
  hypergraph avoiding forbidden submatchings*,
  [arXiv:2204.08981v3](https://arxiv.org/abs/2204.08981v3), Corollary 1.17.

## 0. Definitive verdict

The private-completion proof does **not** prove an exact ordered
four-resource selection.  Its first-stage hypergraph simultaneously forces

\[
                    \varepsilon>2^{-1/3}-o(1)             \tag{0.1}
\]

from the JMS ambient-size condition and

\[
                    \varepsilon\le {1\over2}+o(1)          \tag{0.2}
\]

from a literal pair codegree.  No fixed theorem parameter satisfies both.
Adding three private vertices to each completion edge changes neither
inequality.

The strongest unconditional conclusion available from the same ordered
diamond host is:

> There is an ordered four-resource partial transversal of size
> `N-o(N)`.  It may be chosen so that its directed physical graph has no
> cycle of any prescribed fixed bounded length.  By a diagonal choice and
> deletion of one edge from every remaining cycle, it yields a directed
> linear forest of `N-o(N)` ordered diamonds.

Here

\[
 N=\binom{2m}{m-1}=\binom{2m}{m+1}.
\]

The `o(N)` outer-colour leave is the precise gap between the valid result
and the claimed exact factor.

## 1. Exact host parameters

Let

\[
 \mathcal L={ [2m]\choose m-1},\qquad
 \mathcal U={ [2m]\choose m+1},\qquad
 \mathcal M={ [2m]\choose m}.
\]

Use disjoint tail and head copies of `M`.  For `L in L` and ordered distinct
`a,b notin L`, put

\[
 e(L;a,b)=\{L,\ L+a+b,\ (L+a)_{\rm tail},\ (L+b)_{\rm head}\}. \tag{1.1}
\]

Let `H_1` be the four-graph of all such atoms.  Set

\[
 D=m(m+1),\qquad W=\binom{2m}{m}.
\]

The exact degrees are

\[
 d(L)=d(U)=D,\qquad d(T_{\rm tail})=d(H_{\rm head})=m^2. \tag{1.2}
\]

Hence

\[
 \Delta(H_1)=D,\qquad {\delta(H_1)\over\Delta(H_1)}={m\over m+1}=1-o(1),
 \qquad |E(H_1)|=ND.                                  \tag{1.3}
\]

The maximum pair codegree is exactly

\[
                         \Delta_2(H_1)=m.              \tag{1.4}
\]

For example, after fixing `L` and `T=L+a`, the atoms
`e(L;a,b)` are indexed by the `m` choices `b notin T`.  All other pair types
have codegree at most `m`: an incident `L,U` pair has two ordered atoms and
an incident tail/head pair has one.

## 2. Why no JMS parameter exists

In the proposed tripartite encoding, `P=L`, while `Q` contains `U` and the
two middle copies.  The `H_2` edge associated with `e(L;a,b)` consists of
`L` and three private vertices and merely remembers the physical atom.

Write `d_J` for the JMS degree parameter.  Condition (H1) includes

\[
 (1-d_J^{-\varepsilon})d_J\le\delta_P(H_1)=D,
 \qquad \Delta(H_1)=D\le d_J.                         \tag{2.1}
\]

Therefore

\[
 0\le d_J-D\le d_J^{1-\varepsilon},\qquad
                         d_J=(1+o(1))D=(1+o(1))m^2.    \tag{2.2}
\]

Choosing a larger nominal degree cannot relax the other hypotheses.

### 2.1 Ambient size

JMS condition (S2) requires

\[
                  |P\cup Q|\le \exp(d_J^{\varepsilon^3}). \tag{2.3}
\]

But

\[
 \log|P\cup Q|=(2\log2+o(1))m,\qquad
 d_J^{\varepsilon^3}=m^{2\varepsilon^3+o(1)}.        \tag{2.4}
\]

Thus (2.3) requires `2 epsilon^3>=1-o(1)`.  For a fixed parameter it in
fact requires strict inequality at the boundary, since at
`epsilon=2^(-1/3)` the right exponent is `(1+o(1))m`, below
`(2 log 2+o(1))m`.  In particular,

\[
                         \varepsilon>2^{-1/3}-o(1).    \tag{2.5}
\]

### 2.2 Pair codegree

Condition (H2) requires

\[
                         \Delta_2(H_1)\le d_J^{1-\varepsilon}. \tag{2.6}
\]

Using (1.4) and (2.2),

\[
 m\le m^{2(1-\varepsilon)+o(1)},                    \tag{2.7}
\]

so

\[
                         \varepsilon\le {1\over2}+o(1). \tag{2.8}
\]

Since `2^(-1/3)=0.793700...>1/2`, (2.5) and (2.8) are incompatible.

The private `H_2` vertices do not occur in `H_1`, do not reduce
`|P union Q|`, and do not reduce the `m` atoms through `(L,T)`.  They cannot
alter this contradiction.  The proposed cycle-conflict estimates and mixed
unavoidability estimates are downstream hypotheses and therefore cannot
rescue the application.

There is also a matching-scale version of the same obstruction.  Fix an
`H_1` atom with tail `T` and another lower colour `L' subset T`.  Among the
`D` private alternatives through `L'`, exactly `m` remember a diamond with
tail `T`.  Their normalized collision weight is

\[
                              {m\over D}={1\over m+1}
                                =D^{-1/2+o(1)},          \tag{2.9}
\]

again incompatible with a required `D^(-epsilon)` bound at the ambient-size
exponent.  This is corroboration, not needed for the decisive contradiction.

## 3. The valid fallback needs no private completion copy

An ordinary matching in `H_1` is already a partial ordered four-transversal:
all selected lower colours, upper colours, tails and heads are distinct.
The host is four-uniform, asymptotically regular by (1.3), and

\[
                         \Delta_2(H_1)=m=o(D).          \tag{3.1}
\]

Therefore the classical Pippenger--Frankl--Rodl theorem gives a matching of
size `N-o(N)`.

A slightly stronger form, including fixed physical girth, follows from the
Delcourt--Postle colouring corollary.  Fix `g>=3`.  Let `C_g` consist of host
matchings whose directed physical edges `T->H` form a simple cycle of length
between three and `g`.

Fixing one atom of an `i`-cycle leaves a physical path with one prescribed
closing endpoint.  The middle Johnson graph has degree `m^2=Theta(D)`, so

\[
 \Delta_i(C_g)=O_g(D^{i-2}),\qquad
 \Delta_{i,j}(C_g)=O_g(D^{i-j-1})\quad(2\le j<i\le g). \tag{3.2}
\]

There are no two-edge configurations.  Taking, for example, `beta=1/3`,

\[
 \Delta(H_1)\le D,\qquad
 \Delta_2(H_1)=m\le D^{2/3}=D^{1-\beta}              \tag{3.3}
\]

for large `m`, while (3.2) is stronger by a full power of `D` than the
remaining configuration bounds.  Corollary 1.17 therefore colours
`L(H_1) union C_g` with at most

\[
                         D(1+D^{-\alpha_g})             \tag{3.4}
\]

colours for some fixed `alpha_g>0`.  Its largest colour class is a
`C_g`-free matching of size

\[
 {ND\over D(1+D^{-\alpha_g})}
       \ge N(1-D^{-\alpha_g}).                         \tag{3.5}
\]

Thus it omits only `o(N)` lower colours and `o(N)` upper colours, while all
used tail and head roles remain injective.

## 4. Valid asymptotic forest conclusion

The directed physical graph of a host matching has indegree and outdegree at
most one.  It is simple: choosing both orientations of one Johnson edge
would repeat its lower and upper vertices.  Hence its components are paths
and directed cycles.

For fixed `g`, the matching from (3.5) has no cycle of length at most `g`.
Delete one atom from every remaining cycle.  The loss is at most `N/(g+1)`.
First take `m` large for fixed `g`, then let `g` tend to infinity along a
slow diagonal.  This gives a directed linear forest `F_m` with

\[
                              |F_m|=N-o(N).             \tag{4.1}
\]

Every selected lower colour, upper colour, tail and head remains distinct.
Equivalently, this is an asymptotically complete ordered four-transversal
with `o(N)` outer-palette omissions and `o(N)` path components after isolated
middle vertices are included.

One may repair the missing immediate lower and upper colours by appending
`o(N)` explicit two-middle-set fragments, obtaining a middle word of length
`W+o(W)` with both immediate shadows complete.  Such repair repeats middle
roles and is **not** an exact ordered four-transversal.  It also supplies no
residence, deeper-shadow, or common-cap theorem.

## 5. Sharp scope

The following implications from the proposed proof are invalid:

```text
P-perfect ordered four-transversal,
exact outer palettes,
exact factor with o(N) physical cycles.
```

The following are valid from current black boxes:

```text
N-o(N) ordered four-transversal,
fixed-girth N-o(N) ordered four-transversal,
N-o(N) directed linear forest after a diagonal deletion,
W+o(W) middle word with both immediate shadows after explicit repairs.
```

Closing `o(N)` to zero is an absorption or specialized alternating-exchange
problem.  It is not supplied by the JMS private-copy construction.
