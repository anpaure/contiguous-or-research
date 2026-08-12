# Four-box intact-block barrier and square reparametrization

## 1. Complete central blocks cannot transport bulk tails

For the balanced four-chain product, write

\[
 \gamma_H(p)=(H+\min(p,0),m-H+\max(p,0))
\]

and

\[
 T_{H,K}(s)=(\gamma_H(s),\gamma_K(-s)),\qquad
 |s|\le \min(H,K).
\]

Direct coordinatewise maximization and minimization give

\[
 \bigvee_s T_{H,K}(s)=
 \begin{cases}
 (H,m-H+K,K,m),&H\ge K,\\
 (H,m,K,m-K+H),&K\ge H,
 \end{cases}
\]

and

\[
 \bigwedge_s T_{H,K}(s)=
 \begin{cases}
 (H-K,m-H,0,m-K),&H\ge K,\\
 (0,m-H,K-H,m-K),&K\ge H.
 \end{cases}
\]

Thus the join of every complete block has coordinate 2 or coordinate 4
equal to `m`, while its meet has coordinate 1 or coordinate 3 equal to zero.

An interior upper tail has the form

\[
 Z(c,u,r,x)=(c+r,m-c,x,m-u),\qquad c,u>0.
\]

Both its second and fourth coordinates are strictly below `m`.  Hence no
join interval for it can contain a complete central block.  By reflection,
no meet interval for an interior lower tail can contain a complete block.
Consequently, in a concatenation of intact oriented blocks, every bulk tail
witness crosses at most one block seam.  The proposed long monotone-trail
transport through intermediate complete blocks is therefore impossible.

This is a bulk obstruction.  In one orientation the number of tails with
`c,u>0` is

\[
 \sum_{r=2}^{m-1}(m-r)r(r-1)
 =\frac{m(m+1)(m-1)(m-2)}{12},
\]

whereas the total number of tails in that orientation is

\[
 \frac{m(m+1)^2(m+2)}{12}.
\]

Their ratio tends to one.

At a seam `B|C`, put

\[
 L_i=\bigvee B[i..\mathrm{end}],\qquad
 R_j=\bigvee C[1..j].
\]

Every cross-seam join is `L_i join R_j`, with both families nested chains.
The dual statement holds for meets.  Therefore the correct local carrier is
a two-chain seam grid, not a multi-block unit-demand trail.  Since one seam
grid has at most `(2m+1)^2` values, the displayed bulk count forces at least
`(1/48+o(1))m^2` active seams in any intact-block construction.

## 2. Exact square coordinates for one sector

Fix `c` and put `R=m-c`.  Every middle point in the corresponding sector,
including both triangular halves and the omitted centers, has the unique
form

\[
 X_c(a,b)=(c+a,m-c-b,b,m-a),\qquad (a,b)\in[0,R]^2.
\]

For any nonempty consecutive family `W` of such points,

\[
 \bigvee W=(c+\max a,m-c-\min b,\max b,m-\min a),
\]

and

\[
 \bigwedge W=(c+\min a,m-c-\max b,\min b,m-\max a).
\]

Thus the join and meet are determined by the same axis-aligned bounding
rectangle of the `(a,b)` points.  The triangular residual-tail problem asks
only for bottom-anchored rectangles; the central-square defects are the
missing rectangle classes.  A word on `[0,R]^2` whose consecutive bounding
boxes realize all required rectangles would simultaneously restore the
upper joins and lower meets and incorporate the centers.

This is still a shadow construction, not yet a max-word.  One must also
construct a linked variable-width factor band with `o(m^3)` slack whose
legal coordinate pins translate every selected lower meet into a max/OR
window.  That common pinning bridge remains open.

## 3. Correct positive target

Let `q(R)` be the repetition excess of a spanning triangular word.  The
exact sector accounting is

\[
 M_m+4m+2+2\sum_{R=0}^{m}q(R)+2\sum_{R=0}^{m-1}q(R).
\]

Hence even the relaxed estimate

\[
 q(R)=O(R^{2-\varepsilon})
\]

would give subcubic four-box shadow overhead and would be sufficient for the
known aggregation theorem once the common factor/pinning bridge is supplied.
The former exact edge-balanced recurrence is much stronger than necessary.

