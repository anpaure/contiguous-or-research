# The Catalan connector repeats form a regular upper design

Date: 2026-08-01  
Status: unconditional coordinate-cocycle theorem and unconditional abstract
repeat-multiset existence.  Physical realization on prescribed component
endpoints is not proved here.

## 0. Outcome

Put

\[
 \Omega=[2m-1],\qquad
 W={2m-1\choose m},\qquad
 C=\operatorname {Cat}_m,
 \qquad c=\operatorname {Cat}_{m-1}.
\]

Suppose a Johnson Hamilton path on all rank-`m` owners uses every
rank-`(m-1)` lower colour except `K_0`, and every rank-`(m+1)` upper colour
at least once.  Let `\mathcal R` be the multiset of its repeated upper
occurrences, beyond the first occurrence of every upper colour.  Then
`|\mathcal R|=C-1` and, for every coordinate `q`,

\[
 \boxed{
 d_{\mathcal R}(q)
 =2c+{\mathbf 1}_{q\in K_0}
   -{\mathbf 1}_{q\in T^-}-{\mathbf 1}_{q\in T^+}, }
 \tag{0.1}
\]

where `T^-` and `T^+` are the endpoint owners.

If the endpoints are Johnson-adjacent and

\[
 K_0=T^-\cap T^+,
 \qquad R_0=T^-\cup T^+,
\]

then

\[
\boxed{
 d_{\mathcal R}(q)=2c-{\mathbf 1}_{q\in R_0}. }
\tag{0.2}
\]

Thus `\mathcal Q=\mathcal R\mathbin{\dot\cup}\{R_0\}` is a
Catalan-sized rank-`(m+1)` block multiset with exact constant coordinate
degree `2c`.

Conversely, for every prescribed rank-`(m+1)` block `R_0` and every
`m>=3`, such an abstract multiset `\mathcal Q` containing `R_0` exists.
Hence the connector's singleton coordinate ledger has no further abstract
design obstruction.  The surviving problem is to realize the blocks of
`\mathcal Q-\{R_0\}` as literal endpoint-to-endpoint connector unions in
one component order.

## 1. The path cocycle

For a coordinate `q`, let

\[
 M_q={2m-2\choose m-1},\quad
 L_q={2m-2\choose m-2},\quad
 U_q={2m-2\choose m}.
\]

Summing coordinate incidence over the `W-1` path edges in two ways gives

\[
 2M_q-e_q
 =\bigl(L_q-{\mathbf 1}_{q\in K_0}\bigr)
  +\bigl(U_q+d_{\mathcal R}(q)\bigr),                 \tag{1.1}
\]

where

\[
 e_q={\mathbf 1}_{q\in T^-}+{\mathbf 1}_{q\in T^+}.  \tag{1.2}
\]

Indeed, every internal owner is incident with two path edges and each
endpoint owner with one.  On each Johnson edge, the sum of the two owner
incidence indicators equals the sum of its intersection and union
indicators.

The central binomial identity is

\[
 2M_q-L_q-U_q=2\operatorname {Cat}_{m-1}=2c.          \tag{1.3}
\]

Substitution in (1.1) proves (0.1).

If the endpoints are adjacent, their two incidence indicators satisfy

\[
 {\mathbf 1}_{q\in T^-}+{\mathbf 1}_{q\in T^+}
 ={\mathbf 1}_{q\in T^-\cap T^+}+{\mathbf 1}_{q\in T^-\cup T^+}
 ={\mathbf 1}_{q\in K_0}+{\mathbf 1}_{q\in R_0}    \tag{1.4}
\]

coordinatewise.  Equations (0.1) and (1.4) give (0.2).

The size of the repeat multiset is forced independently:

\[
 (W-1)-{2m-1\choose m+1}=C-1.                        \tag{1.5}
\]

Adding `R_0` to (0.2) therefore gives a multiset `\mathcal Q` of `C`
rank-`(m+1)` blocks, every coordinate having degree `2c`.

## 2. Abstract existence with a prescribed block

The required degree sum identity is

\[
 C(m+1)=2(2m-1)c.                                    \tag{2.1}
\]

Fix `R_0\in\binom{\Omega}{m+1}`.  After reserving this block, ask for a
simple bipartite graph between the `2m-1` coordinate vertices and `C-1`
labelled block vertices such that

* every block vertex has degree `m+1`;
* a coordinate in `R_0` has degree `2c-1`;
* a coordinate outside `R_0` has degree `2c`.

Its degree sums agree by (2.1).  Sort the coordinate degrees in
nonincreasing order.  The Gale--Ryser inequality for the first `t`
coordinate vertices has right side

\[
       \sum_{j=1}^{C-1}\min\{t,m+1\}
       =(C-1)\min\{t,m+1\}.                         \tag{2.2}
\]

For `t<=m+1`, the requested left degree sum is at most `2ct`, and

\[
 2c\le C-1\qquad(m\ge3).                             \tag{2.3}
\]

For `t>=m+1`, the right side of (2.2) is the total degree
`(C-1)(m+1)`, so the inequality follows from the equality of total sums.
Therefore the bipartite degree sequence is graphical.

For completeness, (2.3) is sharp at `m=3`; in general

\[
 C-2c={2(m-2)\over m+1}c\ge1.                       \tag{2.4}
\]

Read each labelled block vertex's neighbourhood as a rank-`(m+1)` block.
Different labelled block vertices may have the same neighbourhood.  This
is precisely why the conclusion is a **multiset** theorem, not a simple
block-design theorem.  The reserved labelled copy of `R_0` is present even
if one or more residual block vertices also have neighbourhood `R_0`.
Together they form the required regular multiset.

## 3. Exact remaining gate

The theorem solves only the coordinate/design row.  Given an upper-exact
`C`-component owner forest, let its `C` unused lower roots be the available
connector tails and its `C` unused incoming owner slots the connector
heads.  To obtain one Hamilton path one still must select `C-1` literal
Johnson connectors which simultaneously

1. use all but `K_0` of the unused lower roots;
2. use all but the two final endpoint slots;
3. join the component paths into one directed path; and
4. have upper-union multiset exactly `\mathcal Q-\{R_0\}` for some regular
   `\mathcal Q` above.

This is a regular coloured component-Hamilton-path problem.  Ordinary
endpoint Hall, the coordinate cocycle, and abstract block-design existence
are necessary but do not imply its physical solution.
