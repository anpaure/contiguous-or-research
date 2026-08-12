# The direct-edgewise recursion has an exact trace-block law, but residence must be joint

Date: 2026-07-31  
Status: all-parameter block/charge identities; independent finite replay of
the strict recursive chain at child parameters (n=3,4,5); exact joint
DERF--RSB target.  No all-parameter guarded realization theorem is claimed.

## 0. Verdict

The strict direct-edgewise side lift is a serious recursive construction,
not merely a finite search pattern.  Before its two seam families are added,
its output has exactly

\[
                         3\operatorname {Cat}_{n+1}
\]

maximal sector components.  The two seam families contain exactly
(2\operatorname {Cat}_{n+1}) bridge edges and leave the required
(\operatorname {Cat}_{n+1}) ambient paths.  This bookkeeping is exact in
every dimension.

The frozen chain also has a favorable physical defect profile.  Its upper
side has no anchor-free component at any of the three steps, while the lower
side has respectively (0,1,2).  Anchor-free side components are exactly
the pure-side pieces untouched by either seam family, so this is the right
bounded-defect topology statistic.

However, it is not yet a guarded RSB induction.  The untouched child sector
copies every old internal residence defect verbatim.  In the literal chain,
the numbers of internal positive runs of length below three are

\[
                              17,quad44,quad144.
\]

Of these, (5,17,57) already lie strictly inside one maximal trace block.
They cannot be repaired by merely permuting or reversing intact blocks.
Thus the correct target is a **joint DERF--RSB realization theorem** which
selects the common basis, both side representative systems, and the guarded
fragment/socket state simultaneously.  Post-hoc Hamiltonization of the
frozen forest is the wrong target.

## 1. Exact trace-block conservation

Use the child-parameter notation

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=\operatorname {Cat}_n,
 \quad C=\operatorname {Cat}_{n+1}=M-P.
\]

The side forests have

\[
                       H=N-P=C-K                         \tag{1.1}
\]

components apiece.  Label the four ambient vertex sectors by the two new
coordinates (c,z):

* (0): the direct upper side;
* (c): the untouched child trace;
* (z): the punctured central trace;
* (cz): the direct lower side.

### Theorem 1.1 (three-block law)

Before adding the (0\leftrightarrow z) and
(z\leftrightarrow cz) seam families, the numbers of components in these
four sectors are

\[
       (b_0,b_c,b_z,b_{cz})=(C-K, K, C+K, C-K).       \tag{1.2}
\]

Consequently the number of trace blocks is exactly (3C).  The seams give
exactly (C) edges of type (0-z) and (C) edges of type (z-cz).
Whenever the complete physical support is a forest, all these edges are
bridges and the output has exactly

\[
                            3C-2C=C                     \tag{1.3}
\]

path components.

#### Proof

The two side counts are (1.1).  The child sector is the supplied
(K)-path forest.  Removing the common-basis edge set (Q), of size (C),
from the child forest leaves

\[
                   M-(N-C)=M-N+C=K+C
\]

central components.  Summing gives (1.2).  Every (q\in Q) supplies one
seam on each side, giving (2C) seam edges.  In a forest every edge joining
two pre-seam components lowers the component count by one, proving (1.3).
\(\square\)

The average number of sector blocks per output path is therefore exactly
three.  This does **not** bound the largest number on one path: the frozen
chain has maxima (7,12,20).

## 2. Anchor-free charge is the exact side-terminal statistic

On one side let (c_j) count components containing (j) seam anchors.
The seam-anchor degree cap implies (j\le2).  Since there are (H=C-K)
components and (C) anchors,

\[
 c_0+c_1+c_2=C-K,qquad c_1+2c_2=C.
\]

Hence

\[
             c_2=K+c_0,qquad c_1=C-2K-2c_0.           \tag{2.1}
\]

An anchor-free side component receives no collar seam.  It is therefore a
literal pure-sector output path, not merely an abstract charge defect.
Thus a uniform bound on (c_0^-+c_0^+) would give a uniform bound on the
number of exceptional **pure-side** terminals.

It would not by itself yield an (O(1))-piece owner chronology.  The DERF
output still has (C) ambient paths, including (K) untouched child paths.
A separate guarded endpoint-routing theorem must transparently join almost
all of those paths.

For the retained chain the exact anchor histograms are

\[
\begin{array}{c|c|c|c|c}
n&c_0^-& (c_1^-,c_2^-)&c_0^+&(c_1^+,c_2^+)\\ \hline
3&0&(4,5)&0&(4,5)\\
4&0&(14,14)&1&(12,15)\\
5&0&(48,42)&2&(44,44).
\end{array}                                             \tag{2.2}
\]

Here the minus sign denotes the upper direct-lift side and the plus sign
the lower projection side.  The sequence (0,1,2) is finite evidence only;
it does not prove a uniform bound.

## 3. Residence debt is inherited, not washed out

For the even ambient instances in the retained chain the deadline depth is
two, so the weak flat-carrier residence test forbids an internal positive
coordinate run of length one or two.

### Lemma 3.1 (child-sector inheritance)

Every child path (P=(v_0,\ldots,v_s)) appears in the output as the intact
path

\[
                    c+P=(c+v_0,\ldots,c+v_s).          \tag{3.1}
\]

No collar seam is incident with this sector.  For every old coordinate,
the positive-run word on (3.1) is identical to its word on (P).  Hence
every internal child residence defect, and every cut-hitting obstruction
for those defects, is inherited literally as a strict interior defect of
one (c)-trace block.

#### Proof

The (c)-sector atoms are exactly the child physical edges with (c)
adjoined.  The only cross-sector atoms are (0-z) and (z-cz).  Thus (3.1)
is a complete output component, and adjoining the constant coordinate
(c) changes no old-coordinate bit word. \(\square\)

The independent replay gives

\[
\begin{array}{c|r|r|r|r}
n&\text{internal short runs}&\text{paths hit}&
 \text{any-incident cut floor}&\text{flanking-cut cover}\\ \hline
3&17&7&11&12\\
4&44&21&34&35\\
5&144&65&116&124.
\end{array}                                             \tag{3.2}
\]

The third column after `paths hit' is an exact interval-stabbing lower
bound: a length-two run on positions (i,i+1) remains insulated unless at
least one of the three incident path edges is cut.  The last column is the
exact minimum when cuts are restricted to the two flanks so the run is
exposed intact.  Hitting is necessary, not sufficient, for a later braid to
repair residence.

The strict block-interior defects split as

\[
\begin{array}{c|rrrr|r}
n&0&c&z&cz&\text{total}\\ \hline
3&0&5&0&0&5\\
4&0&17&0&0&17\\
5&3&44&2&8&57.
\end{array}                                             \tag{3.3}
\]

In particular, at the last audited step the new side/central blocks create
thirteen fresh body defects in addition to the forty-four inherited through
the child sector.  This is why bounded (c_0) does not settle the RSB
interface.

## 4. The exact joint induction target

The results above suggest the following proof-safe target.

> **Joint direct-edgewise guarded routing theorem (DERF--RSB).**  There is
> an absolute (B) and a recursively right-total protected state such that,
> from every accepted child state, one can jointly choose:
>
> 1. a strict synchronized common basis (Q) and its two direct side SDRs;
> 2. anchor-capped side forests whose contracted shore matchings are
>    acyclic with the punctured center and satisfy
>    (c_0^-+c_0^+\le B);
> 3. orientations and protected states for every new (0,z,cz) trace
>    block with no unbudgeted internal residence event;
> 4. the (2C) collar seams, with their deep-shadow witnesses and compiler
>    ownership, as valid natural joins of those protected states; and
> 5. a node-private transparent connector forest on the resulting (C)
>    ambient paths, leaving at most (B) terminal macrofragments and an
>    accepting exported RSB relation for the next lift.

Theorem 1.1 and (2.1) close the scalar topology accounting in this target.
Lemma 3.1 makes the joint quantifier load-bearing: residence cannot be
postponed to a later recursion.  The general protected-braid theorem then
converts an accepting terminal relation into the desired optimal word.

This is neither a demand for a Hamilton middle-levels cycle nor a claim that
the frozen (n=3\to6) chain already passes RSB.  It is the precise correlated
selection statement still separating the verified strict recursion from a
general construction.

## 5. Audit

The standard-library consumer

```text
scratch/audit_catalan_derf_rsb_trace_blocks_20260731.py
```

authenticates and reconstructs

```text
scratch/catalan_direct_edgewise_side_lift_recursive_n3_n5_20260731.witness.json
```

then checks (1.2)--(1.3), the two anchor histograms, every positive-run
event, the child-sector inheritance equalities, and both cut floors.  It
writes

```text
scratch/catalan_derf_rsb_trace_blocks_20260731.audit.json
```

No remote solver status and no unproved all-parameter boundedness assertion
is used.
