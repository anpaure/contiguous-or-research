# Audit and corrected sufficient theorem for the positive four-box route

## 1. Exact value of the triangular reduction

In the equal four-box let

\[
 \gamma_H(p)=(H+\min(p,0),m-H+\max(p,0)),
\]

and

\[
 X(H,p;K,q)=(\gamma_H(p),\gamma_K(q)).
\]

The natural middle block is

\[
 T_{H,K}(s)=X(H,s;K,-s),\qquad |s|\le\min(H,K).
\]

For `H>K`, its residual upper and lower cells are exactly the regions
`p>K` and `p<-K`; the natural diagonal intervals cover the complementary
central square.

Fix `c=H-r` and `R=m-c`.  Put

\[
 E_{c,r,x}=T_{c+r,r}(r-x),\qquad P_{c,u}=E_{c,u,0}.
\]

Every residual upper target is

\[
 Z_{u,r,x}=E_{c,r,x}\vee P_{c,u},qquad
 0\le u<r\le R,quad0\le x<r.
\]

Thus a spanning triangular word over

\[
 \mathcal T_R=\{P_0\}\cup\{E_{r,x}:1\le r\le R,0\le x<r\}
\]

of length `|T_R|+rho(R)` supplies every residual upper join.  Its reflected
reverse supplies the corresponding lower targets as **meets**.

The middle-occurrence accounting is

\[
 M_m+2\rho(m)+4\sum_{R=0}^{m-1}\rho(R)+O(m).         \tag{1.1}
\]

The `O(m)` term permits one unmerged boundary occurrence per sector.  It
vanishes when each triangular word has the completion-core endpoint used in
the canonical merge.  Hence `rho(R)=O(R)` really does give only `O(m^2)`
overload for residual tail shadows.  The certified `R=6` word with excess
five is evidence for, but not a proof of, this scale.

## 2. Why a trail or triangular word is not yet a max-word

Four independent implications remain.

1. **Central squares.**  An arbitrary triangular word need not preserve the
   natural monotone diagonal intervals which cover `|p|<=K` at every depth.
2. **Lower signs.**  A lower target cannot be the maximum of middle-rank
   points below it: its rank is smaller.  Reflection gives a meet, not a
   max/OR witness.
3. **Factor and pins.**  Translating those meets into maxima requires one
   common factor interval system and coordinatewise pin survival.
4. **Physical overload and contamination.**  A bound on the number of
   abstract trails controls neither repeated middle occurrences nor the
   condition that every intervening point lie below its target.

Therefore an `O(m^2)` trail count, by itself, does not imply a four-box
construction.

This failure is finite and explicit.  Embed the verified `R=6`, excess-five
triangular certificate in the balanced sector, concatenate its reflected
reverse, and insert the six omitted block centers.  All residual upper-tail
joins and lower-tail meets remain present, but exhaustive interval extrema
miss 143 upper and 143 lower central-square targets among the 455 block
points.  The first missed upper example is the block datum `(r,p,q)=(1,0,1)`,
corresponding to `(1,5,1,6)`.  Thus triangular tail universality does not
merely fail to *prove* diagonal compatibility; it can actively destroy it.

## 3. Correct sufficient theorem

It is sufficient to construct a row

\[
 T_1,\ldots,T_L,qquad L\le M_m+Cm^2,
\]

and a physical length `N=L+d`, `d=O(m^2)`, with monotone central intervals

\[
 I_i=[i+\alpha_i,i+\beta_i]
\]

such that:

* every middle point occurs among the `T_i`;
* every upper point is the join of a consecutive `T`-interval;
* every lower point is the meet of a consecutive `T`-interval `[u,v]`;
* the central intervals are linked:
  `alpha_(i+1)<=beta_i`;
* for each coordinate atom `b`, with
  
  \[
  Z_b=[N]\setminus\bigcup_{i:b\notin T_i}I_i,
  \]
  
  every positive central interval meets `Z_b`;
* every chosen lower meet has a nonempty core
  
  \[
  J_{u,v}=[v+\alpha_v,u+\beta_u],
  \]
  
  and `J_(u,v)` meets `Z_b` for every atom in the meet.

Then the maximal factor

\[
                         A_p=\{b:p\in Z_b\}
\]

is one max/OR word of length `N`.  Linkedness translates the upper joins;
the core-pinning theorem translates every lower meet.  Consequently

\[
                         g_4(m,m,m,m)\le M_m+O(m^2).
\]

Non-core lower windows are allowed only under the stronger global legal-set
criterion including all of their negative barriers.

## 4. Exact primary target

The positive route therefore requires a **factorable triangular braid**:

1. `rho(R)=O(R)` (or any bound summing to `o(m^3)`);
2. simultaneous preservation/replacement of all central-square intervals;
3. one monotone linked interval band of `O(m^2)` slack; and
4. all central and lower-core pin inequalities.

Canonical full fan blocks, uniformly short tail witnesses, and literal
fixed-delay padding have proved cubic obstructions.  The required braid must
use linearly long shared intervals and noncanonical triangular providers.
