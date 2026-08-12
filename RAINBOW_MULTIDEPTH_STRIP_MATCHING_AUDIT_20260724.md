# Audit of the quantitative multidepth strip-matching theorem

Audited source: `RAINBOW_MULTIDEPTH_STRIP_MATCHING_20260724.md`.

## Verdict

**VALID.**  I found no mathematical gap in the strip reconstruction,
degree/codegree ledger, growing-uniformity matching application, cycle-cut
accounting, or the proof that the short-run charge is zero.  The theorem
unconditionally supplies the reduced Johnson-path gate through

\[
H=\Theta\!\left(
\left(\frac{\log m}{\omega\log\log m}\right)^{1/3}
\right).
\]

It remains only a partial central-band result and does not reach the
sprinkled-tail scale.

## 1. Strip geometry and injectivity

Put `a=ell-H`.  The assumptions give `2<=a<ell=|R|/2`.

* The middle masks
  \[
  T_t=C\cup I(t,\ell)
  \]
  form a Johnson cycle because the shift removes `z_t` and adds
  `z_(t+ell)`.
* Intersecting or unioning `q+1` consecutive middle windows gives exactly
  \[
  C\cup I(t+q,\ell-q),\qquad C\cup I(t,\ell+q).
  \]
  All coordinates in these windows are distinct and `q<=H<ell`, so the
  ranks really are `m-q` and `m+q`.
* The lowest row recovers `C` as its total intersection and `C union R` as
  its total union.  Hence it also recovers `D`.
* In a cycle of length `2ell`, an adjacent coordinate pair lies in exactly
  `a-1` cyclic `a`-intervals.  A nonadjacent pair at shorter cyclic distance
  `delta>=2` lies in at most `max(0,a-delta)<=a-2` such intervals.  Thus the
  lowest row recovers the undirected cycle.  Reversal changes no interval
  family.

Therefore distinct triples `(C,D,gamma)` give distinct hyperedges; the
hypergraph is ordinary and simple.

## 2. Exact edge and degree counts

The number of choices is

\[
 \binom{2m}{m-\ell}
 \binom{m+\ell}{m-\ell}
 \frac{(2\ell-1)!}{2}
 =\frac{(2m)!}{4\ell(m-\ell)!^2}.
\]

Each strip has `2ell` vertices in every one of the `2H+1` ranks, hence

\[
 K=2\ell(2H+1).
\]

Double-counting incidences in rank `m+d` gives

\[
 D_d=\frac{(m+d)!(m-d)!}{2(m-\ell)!^2}.
\]

The ratios show that `D_0` is the minimum and `D_H=D_(-H)` the maximum.
Moreover

\[
 D/D_0=\exp(O(H^2/m)),\qquad
 \log D=(2+o(1))\ell\log m,
\]

since `H,ell` are polylogarithmic and `ell=o(m)`.

## 3. Pair-codegree bound

For fixed distinct band masks `X,Y`, the stabilizer orbit of `Y` relative
to `X` has size

\[
 \binom{|X|}{|X\cap Y|}
 \binom{2m-|X|}{|Y\setminus X|}.
\]

If this product is not one it is at least `m-H`.  Product one would force
`Y` to be one of `emptyset,X,X^c,[2m]`; only `X^c` is not immediately
excluded by rank or distinctness, and it cannot share a strip with `X`
because every member of that strip contains the nonempty core `C`.

Every strip through `X` has only `2ell` vertices in the rank of `Y`.
Orbit double counting therefore gives

\[
 \Gamma/D\le 2\ell/(m-H).
\]

This argument remains valid when `X,Y` have the same rank.

## 4. ABKV hypotheses and residual

Use

\[
 C_* = \left\lceil\frac{2\ell D}{m-H}\right\rceil.
\]

The chosen parameters satisfy

\[
 \ell=(1+o(1))\omega H^2,qquad
 K=(4+o(1))\omega H^3
   \le(1+o(1))\frac{\log m}{16\log\log m}.
\]

The near-regular defect is admissible because

\[
 \frac{H^2}{m}
 =o\!\left[
 \left(\frac{C_*\log D}{D}\right)^{1/3}
 \right],
\]

while

\[
 f(D)/D
 =O\!\left((\ell^2\log m/m)^{1/3}\right)=o(1).
\]

Also

\[
 \log\!\left(e^{2K}\frac{C_*\log D}{D}\right)
 =-\log m+o(\log m),
\]

so the growing-`K` codegree condition holds.  Finally

\[
 \eta:=\frac{C_*\log(1+C_*)}{D}
 =O(\ell^2\log m/m),
\]

and `log eta=-log m+O(log log m)`.  Since
`K<=(1+o)log m/(16 log log m)`, this yields

\[
 \eta^{1/(K-1)}\le(\log m)^{-16+o(1)}.
\]

The exact matching conclusion used is the `B=emptyset` case of
[ABKV Theorem 3.9](https://web.math.princeton.edu/~nalon/PDFS/abkv4.pdf):

\[
 O\!\left(
 K\eta^{1/(K-1)}|V|
 \right)
\]

uncovered vertices.  As
`|V|<=(2H+1)W` and `K,H` are polylogarithmic, the claimed bound

\[
 U_m\le W(\log m)^{-10}
\]

follows with room to spare.

## 5. Cycle cuts and the exact shadow ledger

A matched strip contributes all `2ell` cyclic shadows in each signed depth.
After cutting one cycle edge, the path has `2ell` middle vertices and exactly
`2ell-q` windows of `q+1` consecutive middle vertices.  Matching disjointness
makes all retained shadows globally distinct.  Hence

\[
 M_q^-=M_q^+=N_q-p_m(2\ell-q).
\]

Before the cuts, the total unmatched band vertices are exactly

\[
 U_m=(W-2\ell p_m)
 +2\sum_{q=1}^H(N_q-2\ell p_m).
\]

Subtracting the nonnegative missed-middle term and adding the `q` lost
windows on each side gives

\[
 \sum_{q=1}^H(M_q^-+M_q^+)
 \le U_m+p_mH(H+1).
\]

Adding the endpoint-cap charge `Hp_m` and using
`p_m<=W/(2ell)` gives

\[
 Hp_m+\sum_q(M_q^-+M_q^+)
 \le U_m+\frac{H^2+2H}{2\ell}W
 =U_m+\left(\frac1{2\omega}+o(1)\right)W=o(W).
\]

## 6. Short coordinate runs

Coordinates in `C` occur throughout a path and coordinates in `D` never
occur.  Every coordinate of `R` has one cyclic one-run of length exactly
`ell`.  Cutting the cycle either leaves that as one internal run of length
`ell`, or splits it into two boundary runs.  Because `ell>H`, no internal
one-run has length at most `H`, and therefore

\[
 \rho_H=0.
\]

## 7. Independently-cut architecture ceiling

The added Section 6 is also valid.  If the matching misses `o(W)` middle
vertices, then

\[
p_m=(1-o(1))\frac{W}{2\ell}.
\]

Independent cycle cuts destroy exactly `q` lower and `q` upper cyclic
windows per selected cycle at depth `q`.  Since all pre-cut values are
globally distinct, these are exactly new missing colours, and an `o(W)`
charge requires

\[
H^2/\ell=o(1).
\]

For a fixed middle mask, every incident strip contains exactly two
rank-`m+1` immediate supersets.  Stabilizer transitivity over its `m`
immediate supersets therefore gives

\[
\Gamma\ge 2D_0/m=(2-o(1))D/m.
\]

The displayed ABKV codegree hypothesis then forces

\[
8\ell H\le(1+o(1))\log m.
\]

Multiplication yields

\[
H^3=(H^2/\ell)(\ell H)=o(\log m),
\qquad H=o((\log m)^{1/3}).
\]

This is correctly scoped only to the full-strip ABKV matching followed by
independent cuts; safe splicing may recover those windows.

## Minor edits only

I corrected three harmless TeX issues in the source (`\qquad`, `\le`, and two
missing display terminators).  It would also be slightly clearer to say
explicitly that `f(D)` is evaluated with the upper codegree parameter `C_*`,
as the subsequent estimates already do.  None changes the proof.
