# Independent audit of the lexical GMN upper-turn obstruction

Date: 2026-08-01  
Lane: K cross-audit of Lane R  
Audited source:
`MATH_THEOREM_R_PROSPECTIVE_GMN_COLORED_PULL_TREE_AND_LEXICAL_UPPER_OBSTRUCTION_20260801.md`  
Verdict: PASS, with the construction-specific prefix scope stated below.

## 0. Verdict

All four load-bearing numerical claims are correct.

For the canonical lexical factor with paper parameter `r`, the exact number
of initially missing projected upper-turn colours is

\[
 M_r={2r-1\choose r-3}-{2\over r-1}{2r-2\choose r-3}
    =W_r{(r-2)(r-3)\over2(r+2)(2r-1)},               \tag{0.1}
\]

where

\[
                         W_r={2r+1\choose r}.         \tag{0.2}
\]

Every factor-alternating pull hexagon changes at most three turn-map values.
A canonical pull tree uses at most `Cat_r-1` such hexagons.  Therefore every
canonical-tree endpoint retains at least

\[
                         M_r-3(\operatorname {Cat}_r-1)              \tag{0.3}
\]

missing projected upper colours.  This quantity is `1941` at `r=11` and is
positive for every `r>=11`.  Since the owner-layer parameter is exactly
`r=m-1`, the uniform no-go starts at

\[
                              m\ge12.                \tag{0.4}
\]

No disjointness assumption on the selected pulls is needed for the
three-per-pull bound; it is a telescoping bound on recovery of colours
missing in the initial map.

## 1. Re-derivation of the lexical defect count

Let `C(z)` be the Catalan generating series, so

\[
                              C-1=zC^2.              \tag{1.1}
\]

In the lexical turn fibre with `b` unmatched zeros, the two central valleys
must both be nonempty.  Before the exceptional rescue, the missing count is

\[
 \sum_{b=0}^{r-3}[z^{r-b-1}](C-1)^2C^{2b+2}
 =\sum_{b=0}^{r-3}[z^{r-b-3}]C^{2b+6}.               \tag{1.2}
\]

The Lagrange coefficient formula

\[
                         [z^j]C^k={k\over2j+k}{2j+k\choose j}        \tag{1.3}
\]

turns the `b`th summand into

\[
                  {b+3\over r}{2r\choose r-b-3}.    \tag{1.4}
\]

Summing (1.4) by the adjacent-binomial identity gives

\[
                  \sum_{b=0}^{r-3}{b+3\over r}
                         {2r\choose r-b-3}
                    ={2r-1\choose r-3}.              \tag{1.5}
\]

The `b=0`, height-one exceptional branch is actually present and must be
restored.  Its order is

\[
 [z^{r-1}](C-1)^2=[z^{r-3}]C^4
       ={2\over r-1}{2r-2\choose r-3}.               \tag{1.6}
\]

Subtracting (1.6) from (1.5) proves the first expression in (0.1).
Straight factorial cancellation against (0.2) gives the second expression.
The exceptional term is load-bearing; omitting it would overstate the
obstruction.

## 2. Maximum recovery by canonical pulls

A factor-alternating incidence hexagon has three lower-rail vertices.  At
every other lower vertex the two chosen neighbours are unchanged, so its
projected upper-turn map is unchanged there.  At each of the three touched
vertices there is only one turn-map value.  Hence one pull can create at
most three colours absent from the initial turn image.

For sequential or adaptive pulls, charge an initially missing colour to the
first pull after which it appears.  That pull can receive at most three
charges.  Thus `s` pulls recover at most `3s` initially missing colours,
regardless of overlaps or later loss and recovery.  This proves the
telescoping bound used in (0.3).

Let `p_r` be the number of plane-tree components of the lexical factor.
Forgetting the root maps the `Cat_r` rooted plane trees onto those
components, so

\[
                              p_r\le\operatorname {Cat}_r.           \tag{2.1}
\]

A pull spanning tree has exactly `p_r-1` labels, and hence at most
`Cat_r-1` pulls.  Combining this with the preceding paragraph proves
(0.3).

## 3. Positivity and parameter indexing

Since

\[
                         \operatorname {Cat}_r={W_r\over2r+1},       \tag{3.1}
\]

we have

\[
 M_r-3\operatorname {Cat}_r
 ={W_r(2r^3-21r^2-11r+18)
       \over2(r+2)(2r-1)(2r+1)}.                   \tag{3.2}
\]

The cubic numerator equals `18` at `r=11`.  Its derivative is

\[
                              6r^2-42r-11,           \tag{3.3}
\]

which is positive and increasing for `r>=11`.  Therefore (3.2) is positive
for every such `r`; adding the final `+3` in (0.3) preserves positivity.

At `r=11`, the exact values are

\[
 W_{11}=1,352,078,\qquad
 \operatorname {Cat}_{11}=58,786,qquad
 M_{11}=178,296,                                      \tag{3.4}
\]

and

\[
                         178,296-3(58,786-1)=1,941.   \tag{3.5}
\]

The lexical graph has ground `2r+1=2m-1`, its two middle-level shores have
ranks `r=m-1` and `r+1=m`, and the tested turn unions have rank
`r+2=m+1`.  Thus `r=m-1` is the exact translation and (0.4) follows.

## 4. Exact scope

The no-go applies to endpoints obtained from the canonical lexical factor
by a canonical pull spanning tree.  A protected prefix encoded by forced or
forbidden incidences **inside that same pull family** only restricts the
available trees and cannot improve the bound.

A genuinely noncanonical planted edit is not merely such a restriction.
If it changes `q` lower-turn states, the proof-safe bound is instead

\[
                         M_r-q-3(\operatorname {Cat}_r-1).           \tag{4.1}
\]

Opening or rerooting cannot create a missing projected turn colour, but a
literal word can have additional cross-boundary OR witnesses not represented
by this projected-turn statistic.  Those witnesses must be audited
separately.

Accordingly, the theorem says nothing negative about PBBS, a nonlexical or
rotational MMM source, long alternating switches, prospective selection of
`M_0`, residence, deeper shadows, common cap, or the lower compiler.  It is
a sharp closure of the canonical lexical pull-tree lane, not a general
Catalan obstruction.
