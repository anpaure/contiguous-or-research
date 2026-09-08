# Independent audit of the Catalan connector repeat-design cocycle

Date: 2026-08-01  
Audited file: `MATH_THEOREM_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md`  
Verdict: **valid after direct typographical/proof-scope corrections.**

## 1. Path identity

Let a Johnson Hamilton path on all rank-`m` owners omit exactly the lower
colour `K_0`, cover every upper colour, and have endpoint owners
`T^- ,T^+`.  If `mathcal R` is the multiset of upper occurrences beyond
one copy of each upper colour, then

\[
 |\mathcal R|=\operatorname {Cat}_m-1
\]

and coordinate incidence on path edges gives

\[
 d_{\mathcal R}(q)=2\operatorname {Cat}_{m-1}
 +\mathbf1_{q\in K_0}-\mathbf1_{q\in T^-}-\mathbf1_{q\in T^+}.
\]

This is exact.  If the endpoints are adjacent and

\[
 K_0=T^-\cap T^+,qquad R_0=T^-\cup T^+,
\]

then `mathcal Q=mathcal R dotcup {R_0}` has `Cat_m` rank-`(m+1)`
members and constant coordinate degree `2 Cat_(m-1)`.

The assumptions that the endpoints are adjacent and that their
intersection is the omitted lower colour are explicit extra hypotheses;
they are not consequences of Hamiltonicity.

## 2. Prescribed-`R_0` Gale--Ryser row

Write `C=Cat_m`, `c=Cat_(m-1)` and reserve one labelled copy of a prescribed
`R_0 in binom(Omega,m+1)`.  The residual bipartite degree sequence is:

* `C-1` labelled block vertices, each of degree `m+1`;
* the `m+1` coordinates in `R_0`, each of degree `2c-1`;
* the `m-2` coordinates outside `R_0`, each of degree `2c`.

The total degrees agree because

\[
 C(m+1)=2(2m-1)c.
\]

After sorting the coordinate degrees, Gale--Ryser asks for every `t`

\[
 \sum_{i=1}^t d_i\le (C-1)\min\{t,m+1\}.
\]

For `t<=m+1`, the left side is at most `2ct`, and

\[
 2c\le C-1,qquad
 C-2c={2(m-2)\over m+1}c\ge1
\]

for every `m>=3` (equality in the first inequality at `m=3`).  For
`t>=m+1`, the right side is the total degree, so the inequality is
automatic.  Hence the prescribed residual sequence is graphical.

The theorem originally compressed this argument too aggressively.  The
audited file now states the sorted Gale--Ryser right side and the proof of
`2c<=C-1` explicitly.

## 3. Exact multiset scope

The graph is simple only between a coordinate vertex and a **labelled**
block vertex.  It prevents a coordinate from appearing twice in one block.
It does not prevent two block vertices from having the same coordinate
neighbourhood.  Therefore the conclusion is exactly a block **multiset**,
not a simple design.  A residual labelled block may even equal `R_0`, in
which case the final multiset contains multiple copies of `R_0`.

This scope is sufficient for repeated upper occurrences.  It proves no
endpoint placement, Johnson connector, component order, owner capacity,
lower-colour injection, residence or compiler statement.

## 4. Direct corrections

The audited theorem was corrected in place to:

1. replace corrupted incidence-indicator bytes in equation (1.4);
2. restore the missing closing display delimiter after the degree bound;
3. write the complete Gale--Ryser inequalities; and
4. state explicitly that repeated block neighbourhoods, including another
   copy of `R_0`, are allowed.

No mathematical counterexample remains within the stated multiset scope.

