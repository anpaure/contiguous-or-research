# Scope audit of the odd-diamond residence tax

Date: 2026-07-31  
Verdict: the regenerative and `K15 -> K17` conclusions pass; the unrestricted run identity needs two boundary cases

Let \(T_0,\ldots,T_{s-1}\) be a cyclic set sequence, fix a coordinate
\(x\), and write

\[
 b_i=1_{x\in T_i},\qquad
 c_i=1_{x\in T_i\cap T_{i+1}}=b_i b_{i+1}.           \tag{1}
\]

Thus the trace word is the cyclic adjacent-AND transform of the parent
word.

## Correct exact identity

If \(x\) is nonconstant on the component, every maximal parent one-run of
length \(\ell\) is bounded by zeros on both sides.  Formula (1) maps it to

\[
                    \max(\ell-1,0)                   \tag{2}
\]

consecutive ones.  Hence:

* a run of length \(\ell\ge2\) becomes a run of length exactly
  \(\ell-1\);
* a singleton run disappears; it does not become a positive run of length
  zero.

If \(x\) is present on the entire cyclic component, then both words are
all-one and the cyclic run does not shorten.  The all-zero case remains
all-zero.

Therefore the literal assertion that every cyclic Johnson-component run
has length at least two, and that every run shortens by one without a
nonconstant-coordinate hypothesis, is too broad.

## The used theorem survives

In the regenerative application, every relevant parent coordinate is
nonconstant and the parent minimum run is at least \(d+1\ge2\).  Equation
(2) then gives the advertised one-unit tax exactly: a flat child requiring
minimum \(d+1\) needs parent margin \(d+2\), unless an exported actuator
hits every parent run of length \(d+1\).

For the authenticated `K15` parent, every old coordinate is nonconstant and
all runs have length at least four.  Its `1425` length-four runs therefore
become length-three trace runs exactly; the `165` unique-colour forced
packets and the fixed-parent no-go are unchanged.

This audit changes no finite count and no `K17` conclusion.  It only scopes
the dimension-uniform identity correctly.
