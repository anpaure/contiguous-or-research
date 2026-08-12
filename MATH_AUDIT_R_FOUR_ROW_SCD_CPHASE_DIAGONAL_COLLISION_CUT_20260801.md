# The canonical four-row SCD C-phase has two exact diagonal overload cuts

Date: 2026-08-01  
Lane: explicit four-row SCD C-phase / owner graph  
Status: **solver-free all-dimensional counterexample to the canonical
max-degree-two claim; exact smallest failure at `m=4`.  Palette counts and
acyclicity are not disputed.**

## 0. Verdict

Let

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad
 G=[2m-3],\qquad m\ge 3,
\]

and use the standard Greene--Kleitman SCD with `0` an opening step and `1`
a closing step.  For a long central chain write

\[
 R\subset S=R+\rho\subset L=S+x\subset U=L+y.
\]

The two new C-phase owner heads of the long `aU` ear are

\[
 \beta_a(R,S,L,U)=a(S+y),\qquad
 \delta_a(R,S,L,U)=az(R+x).                       \tag{0.1}
\]

Both maps have an explicit fibre of size `m-2`.  Their image owners already
carry one unchanged seed edge.  Consequently the canonical candidate has
physical degree at least

\[
                         1+(m-2)=m-1.              \tag{0.2}
\]

Thus it is a cap-two owner forest only at `m=3`; it fails for every
`m>=4`.  At `m=4` the two bad owners and their complete incident stars are

\[
\begin{aligned}
 a135 &: \quad a125-a135,\ a134-a135,\ a135-az35,\\
 az24 &: \quad az14-az24,\ az23-az24,\ a245-az24.
\end{aligned}                                      \tag{0.3}
\]

These are trees.  Therefore a monotone potential proving acyclicity would
not repair the candidate: max degree two already fails locally.

## 1. The exact `delta_a` collision cut

Put

\[
 E=\{2,4,\ldots,2m-4\}\subseteq G,qquad |E|=m-2.
\]

For `j=1,...,m-2`, define

\[
                         R_j=E\setminus\{2j\}.      \tag{1.1}
\]

The binary word of `R_j` is a concatenation of `01` pairs except that the
`j`th pair is `00`, followed by the final `0` at coordinate `2m-3`.
Hence it is a Greene--Kleitman chain bottom of rank `m-3`, with exactly the
three free coordinates

\[
                 2j-1<2j<2m-3.                    \tag{1.2}
\]

Its central chain is therefore

\[
\begin{aligned}
 S_j&=R_j+(2j-1),\\
 L_j&=S_j+2j,\\
 U_j&=L_j+(2m-3).
\end{aligned}                                      \tag{1.3}
\]

In the notation of (0.1), `x=2j`, so

\[
                     \delta_a(R_j,S_j,L_j,U_j)
                       =az(R_j+2j)=azE             \tag{1.4}
\]

for all `m-2` values of `j`.

The set `E` itself is a short-chain bottom: its word is
`(01)^(m-2)0`, with sole free coordinate `2m-3`.  Its unchanged seed edge is

\[
                    a(E+2m-3)-azE.                 \tag{1.5}
\]

For each `j`, the C-phase ear contributes the additional physical edge

\[
                         azS_j-azE.                \tag{1.6}
\]

The `S_j` are distinct.  Equations (1.5)--(1.6) prove (0.2) without any
enumeration.

Equivalently, after charging the already selected seed edge, the singleton
head set `X={azE}` has residual capacity one but receives `m-2` fixed
C-phase tasks:

\[
 \boxed{\ |\delta_a^{-1}(X)|=m-2>1=\operatorname{cap}(X)
          \quad(m\ge4).\ }                         \tag{1.7}
\]

Its exact Hall deficiency is `m-3`.

## 2. The independent `beta_a` collision cut

Put

\[
 O=\{1,3,\ldots,2m-3\}\subseteq G,qquad |O|=m-1.
\]

For `j=1,...,m-2`, define

\[
                  R'_j=O\setminus\{1,2j+1\}.       \tag{2.1}
\]

Its word consists of an initial zero and `01` pairs, with the `j`th pair
replaced by `00`.  Hence it is a chain bottom of rank `m-3` whose free
coordinates are

\[
                       1<2j<2j+1.                  \tag{2.2}
\]

Thus

\[
 S'_j=R'_j+1,qquad L'_j=S'_j+2j,qquad
 U'_j=L'_j+(2j+1),                                 \tag{2.3}
\]

and

\[
                  \beta_a(R'_j,S'_j,L'_j,U'_j)
                    =a(S'_j+2j+1)=aO.              \tag{2.4}
\]

The set `O\setminus{1}` is a short-chain bottom with sole free coordinate
`1`, so the unchanged seed already has the edge

\[
                         aO-az(O\setminus\{1\}).    \tag{2.5}
\]

The `m-2` ears contribute the distinct edges

\[
                         aL'_j-aO.                 \tag{2.6}
\]

Therefore `X={aO}` gives a second singleton Hall cut of deficiency `m-3`.
For `m>=4` the two displayed task families are disjoint, since one consists
of nonempty even chain bottoms and the other of nonempty odd chain bottoms.
(At `m=3` both consist of the unique rank-zero bottom.)  Any repair for
`m>=4` which retains the fixed diagonal maps must alter at least `m-3`
assignments in each family, hence at least `2m-6` distinct long-ear
assignments in total.

## 3. Smallest literal counterexample

For `m=4`, take `G=[5]`.

### 3.1 The `delta_a` star

Here `E={2,4}`.  The two long chains have

\[
\begin{array}{c|c|c|c}
R&S&L&U\\ \hline
\{4\}&\{1,4\}&\{1,2,4\}&\{1,2,4,5\}\\
\{2\}&\{2,3\}&\{2,3,4\}&\{2,3,4,5\}.
\end{array}
\]

Both `delta_a` heads are `az24`.  The short chain `24<245` supplies the
old edge `a245-az24`; the two ears supply `az14-az24` and
`az23-az24`.  Hence `deg(az24)=3`.

### 3.2 The `beta_a` star

Here `O={1,3,5}`.  The two long chains have

\[
\begin{array}{c|c|c|c}
R&S&L&U\\ \hline
\{5\}&\{1,5\}&\{1,2,5\}&\{1,2,3,5\}\\
\{3\}&\{1,3\}&\{1,3,4\}&\{1,3,4,5\}.
\end{array}
\]

Both `beta_a` heads are `a135`.  The short chain `35<135` supplies the
old edge `a135-az35`; the ears supply `a125-a135` and `a134-a135`.
Hence `deg(a135)=3`.

At `m=3`, each displayed fibre has size `m-2=1`, so it creates degree two
and not an overload.  Directly, the five physical edges are

\[
 a23-az2,quad az2-az1,quad
 a12-a13,quad a13-az3,quad
 123-z12.                                          \tag{3.1}
\]

They are three nontrivial paths, with `z13,z23` isolated, hence have
maximum degree two and no cycle.  Consequently `m=4` is the smallest
counterexample to the canonical candidate.

## 4. Exact general repair cut

Suppose a broadened C-phase catalogue gives every ear task `t` a set
`N(t)` of legal replacement heads of the same signature.  Every such head
already has one seed incidence, so it has residual capacity one.  A
cap-two realization exists on that signature shore only if

\[
              |T'|\le |N(T')|\qquad(T'\subseteq T). \tag{4.1}
\]

This is also sufficient for the degree row, by Hall.  It is not sufficient
for the whole owner graph: the selected head matching must additionally be
independent in the graphic matroid after contracting the seed.

For the frozen diagonal candidate `N(t)` is a singleton.  The sets in
Sections 1 and 2 are therefore literal violated Hall cuts.  A contextual
Tamari or cross-chain repair can succeed only if it exports at least
`m-3` tasks from each singleton fibre to genuinely different physical
heads.  Relabelling the same head, or proving a monotone potential on the
resulting stars, cannot help.

## 5. Independent audit of the positive rows

For a standard chain

\[
 R\xrightarrow{\rho}S\xrightarrow{x}L\xrightarrow{y}U
       \xrightarrow{v}W,
 \qquad \rho<x<y<v,
\]

literal replay of the two C-phase augmenters gives the physical owner
arrows

\[
\begin{array}{c|c|c}
\text{arrow}&\text{lower}&\text{upper}\\ \hline
aL\to azS&aS&azL\\
aL\to a(S+y)&aS&aU\\
azS\to az(R+x)&azR&azL\\
U\to zL&L&zU\\
U\to L+v&L&W\\
zL\to z(S+y)&zS&zU.
\end{array}                                                 \tag{5.1}
\]

The first row is used on a short chain; rows two--four are used on a long
chain ending at `U`; and rows two, three, five, six are used on a chain
reaching `W`.  Consequently

\[
 c+3I_m+4H=\binom{2m-1}{m+1},\qquad
                         2c+I_m=\operatorname{Cat}_m.        \tag{5.2}
\]

The four `{a,z}` upper signatures and the lower rows in (5.1) independently
verify both injectivity ledgers.

The coordinate-sum increments along (5.1) are

\[
 z-x,\quad y-x,\quad x-\rho,\quad z-y,
                    \quad v-y,\quad y-x,                    \tag{5.3}
\]

all positive.  Distinct lower tails give physical outdegree at most one.
An undirected cycle would have a coordinate-sum-minimum vertex with two
outgoing cycle edges, impossible.  Thus the canonical support is an
undirected forest in every dimension, even though Sections 1--3 prove that
it branches.

This verifies the exact strategic split:

* palette/count/lower rows: **valid**;
* acyclicity: **valid for every `m`**;
* maximum degree two: **false for every `m>=4`**.

## 6. Scope

This note refutes only the **canonical fixed diagonal** C-phase owner
assignment.  It does not refute:

* the exact count `c+3I_m+4H` or the unused-lower count `2c+I_m`;
* upper/lower palette exactness;
* acyclicity of the canonical branching support;
* a prospective cross-facet detachment which changes the diagonal heads;
  or
* a jointly selected noncanonical SCD/Tamari realization.

It does prove that max degree two cannot follow from a potential or from
the scalar count alone.  The first indispensable constructive row is the
Hall expansion (4.1), followed separately by graphic independence.
