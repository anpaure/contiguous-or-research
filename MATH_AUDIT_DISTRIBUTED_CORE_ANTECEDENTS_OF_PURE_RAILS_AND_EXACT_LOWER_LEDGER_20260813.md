# Audit: distributed-core antecedents of pure rails

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_DISTRIBUTED_CORE_ANTECEDENTS_OF_PURE_RAILS_AND_EXACT_LOWER_LEDGER_20260813.md`  
**Source SHA-256:**
`d4ae47405fdc529487d213e251cf2f2e50e7020d898573347f3f949f67fdaebe`  
**Verdict:** **PASS**, at the local closed-rail and fractional scopes
stated in the source.

## 1. Hitting schedules are exactly the owner equations

For one core coordinate `f`, preservation of every width-`q` owner is
equivalent to

\[
                         E_f\cap[i,i+q-1]\ne\varnothing
                         \quad(i\in\mathbb Z_N).                    \tag{1.1}
\]

Thus the state space factors coordinatewise as
`H_(N,q)^F`; no equation in the pure owner rail couples two distinct core
coordinates.  A cyclic hitting set has all gaps at most `q`, and conversely
that gap condition hits every `q`-interval.  The lower bound
`ceil(N/q)` and the gap-composition construction are correct.

The rotation-orbit lower bound in Corollary 4.2 is also safe.  If a
minimum `t`-set has rotational stabilizer of order `s`, then `s` divides
`t`; hence its orbit has size `N/s>=N/t`.

## 2. Interval ledger and private toggles

The union over a source interval is literally

\[
 \left(\bigcup G_t\right)\cup I_i^\ell(\sigma).
\]

For `ell>=q`, the interval contains a `q`-subinterval, so every core
coordinate appears and the value is `F union I_i^ell(sigma)`.  Therefore
the owner and every longer row agree with the repeated-core rail exactly,
not merely by rank.

For `ell<q`, the toggle labels are distinct and disjoint from `F`, giving
the exact rank formula

\[
                         \ell+|G_i\cup\cdots\cup G_{i+\ell-1}|.
\]

Each `x_i` occurs in only one source letter.  This proves adjacent
incomparability and supplies the literal outgoing/incoming labels
`x_i,x_(i+q)` of the owner transition.  Source nonemptiness never needs a
core emission because every letter contains its toggle; the extra
`G_i!=empty` sentence is correctly limited to robustness after deleting
the toggle.

## 3. Phase balance

When `q|N`, a residue class modulo `q` meets every cyclic `q`-interval
exactly once.  Partitioning `F` into phase blocks therefore gives the
displayed consecutive-block rank sum.  With `|F|=aq+b`, a cyclic balanced
placement of the `b` large blocks has every `ell`-arc count equal to
`floor(b ell/q)` or `ceil(b ell/q)`.  Substitution gives the two ranks in
(4.6) and typical value `R ell/q+O(1)`.  No owner or upper incidence is
changed by this rank balancing.

## 4. Period `2q+1` single-cell programming

For

\[
                         E_a=\{a-1,a,a+q\}\subset\mathbb Z_{2q+1},
\]

the gaps are `1,q,q`, so it is a minimum legal hitting schedule.  After
rotating a strict interval to `J=[0,ell-1]`, `ell<q`,

\[
 E_0=\{-1,0,q\}\text{ meets }J,qquad
 E_{-1}=\{-2,-1,q-1\}\text{ misses }J.
\]

Choosing these schedules independently on `H` and `F-H` therefore emits
exactly the desired core mask `H` on that one cell.  The rank ranges
`[ell,ell+R-q]`, `1<=ell<q`, cover `1,...,R-1`.

The source explicitly preserves the essential quantifier: this programs
one marked interval.  Two requested intervals can impose incompatible
hit/avoid conditions on one core coordinate, so no simultaneous lower
cover follows from Theorem 5.1.

## 5. Immediate-lower-preserving schedules

For `q>=4`,

\[
                         S_a=\{a,a+q-1,a+2q-2\}
                         \subset\mathbb Z_{2q+1}
\]

has gaps `q-1,q-1,3`.  It meets every `(q-1)`-interval.  The open gap of
`S_(i-1)` contains precisely `i,...,i+q-3`, while `S_i` contains `i`.
Thus every cell of width at most `q-2` is individually programmable and
every row of width at least `q-1` is literally unchanged.  The claimed
immediate-lower, owner, upper, and owner-residence invariance follows.

This does not assert that the source-emission trace itself is biresident;
residence is inherited at the unchanged owner trace, exactly as stated.

## 6. Period `q+2` two-hole ring

For

\[
                         P_a=\{a,a+q-1\}\subset\mathbb Z_{q+2},
\]

the two cyclic gaps are `q-1` and `3`.  Hence, for `q>=4`, every
`(q-1)`-interval is hit.  The schedule `P_(i-1)` has points `i-1` and
`i+q-2`, so it avoids every

\[
                         J=[i,i+\ell-1],\qquad\ell\le q-2,
\]

whereas `P_i` hits `J` at `i`.  Theorem 6.1 follows coordinatewise and
preserves the entire width-`q-1`, width-`q`, and width-`q+1` three-shore
ledger.

The parameter identification in Corollary 6.2 is exact: the external
all-parity two-hole packet has `D=q`, period `D+2=q+2`, and core rank
`R-q`.  Its proved uniform weights are an exact fractional factor on owner
and immediate-lower rows, with the stated uniform marking on the upper
row.  Schedule decoration changes none of these incidences.

The period-`q+2` ring has only a two-position zero run and is not claimed
to be a biresident final carrier.  The corollary is correctly fractional
and does not infer an integral packet matching.

## 7. Audit conclusion

No flaw was found in the distributed-core ledger, the coordinatewise
state-space factorization, either programming construction, or the
two-hole fractional linkage.  The safe conclusion is

\[
 \boxed{
 \text{large exact antecedent state space + single-cell programmability},
 }
\]

not simultaneous protected lower coverage, cross-rail target simplicity,
component fusion, or bounded seam completion.

