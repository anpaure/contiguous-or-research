# Exact boundary defect of the one-prefix MNW prism

**Date:** 2026-08-07  
**Method:** literal mirror-gamma edge tracing in the modified published MNW
tree; no computation or search  
**Status:** unconditional obstruction to the *unmodified* relay tree being
the prepared prism.  The natural `01` boundary survives, and one destination
owner is prepared automatically, but a named leaf owner lacks exactly the
required destination incidence.

## 1. The source boundary is untouched by the first relay

The gamma-alpha relay uses

\[
(1\operatorname{revcomp}(\gamma)0)v,
\qquad
\alpha(1100)v.                                       \tag{1.1}
\]

Every vertex of both witnessing cycles has first coordinate one.  Therefore
the relay changes no incidence whose owner or colour has first coordinate
zero.

The natural `B8` boundary after the Dyck prefix `10` has fixed context `01`.
All its owners and colours have first coordinate zero.  Hence the complete
source boundary

\[
                         (Z_B)_{01,U(v)}              \tag{1.2}

survives the first relay literally in its canonical phase.

The same argument protects every `00` owner-side auxiliary rail before any
annulus sweep.

## 2. Two destination owners meet mirror gamma

In the first base hexagon `H0` of the `B8` relay, the three base owners are

\[
10001101,\qquad10001011,\qquad11001001.              \tag{2.1}

In positive context `10`, the first and third become

\[
 O_1=1010001101,
 \qquad
 O_3=1011001001.                                     \tag{2.2}

These are exactly two lower centres of the mirror-gamma cycle:

\[
\begin{aligned}
O_1&=F(10011101),\\
O_3&=F(11011001),
\end{aligned}
\qquad F(A)=1\operatorname{revcomp}(A)1.             \tag{2.3}

Thus the first relay is not disjoint from the desired `10` boundary.  Its
effect can be read exactly.

## 3. The third owner is prepared perfectly

At base owner `11001001`, `H0` needs the selected pair

\[
 Q^- =11001101,
 \qquad E=11011001,                                  \tag{3.1}

and needs `Q^+=11001011` unselected.

At `O_3`, mirror gamma retains the facet

\[
                         10E=1011011001

and replaces its old marked facet by

\[
                         10Q^-=1011001101.            \tag{3.2}

Therefore its final selected pair is exactly the positive-context copy of
`{E,Q^-}`.  This owner satisfies the required destination phase with no
additional action.

## 4. The first owner has one exact incidence defect

At base owner `10001101`, `H0` needs

\[
\begin{aligned}
Q^-&=10001111,\\
Q^+&=11001101,\\
E&=10101101.
\end{aligned}                                        \tag{4.1}

After adding context `10`, these are

\[
\begin{aligned}
10Q^-&=1010001111,\\
10Q^+&=1011001101,\\
10E&=1010101101.
\end{aligned}                                        \tag{4.2}

Mirror gamma removes `10Q^+`, as desired, and retains `10E`.  But its new
facet is

\[
                         R=1110001101,                \tag{4.3}

not `10Q^-`.  Thus the final selected pair at `O_1` is

\[
                         \{1010101101,1110001101\},   \tag{4.4}

whereas the prepared prism requires

\[
                         \{1010101101,1010001111\}.   \tag{4.5}

Equivalently, the missing local operation is the endpoint transfer

\[
 (O_1,R)\longmapsto(O_1,10Q^-),                      \tag{4.6}

with the mate `(O_1,10E)` fixed.

## 5. No later tuple in the modified published tree fixes (4.6)

The centre `O_1` lies on the canonical path rooted at

\[
 r_*=1\operatorname{revcomp}(11101000)0=1111010000. \tag{5.1}

In the standard `F_4` tree, the root `11101000` belongs only to gamma: the
central `alpha(10)` tuple meets gamma at the different root `11011000`.
After mirror wrapping, `r_*` is therefore a leaf of the wrapped `F_4`
subtree.

The replacement connector `alpha(1100)` meets that subtree at
`1110011000`, not at `r_*`.  The later `F_(m,j)` connectors have their old
block root of the form

\[
                         1(10)^{j-3}10010\,w,
\]

and the top connector has the beta alternating-tail roots.  None equals
`r_*v`.  Hence the selected tuple degree of `r_*v` stays one in the full
modified recursive tree.

Conflict-free rethreading consequently makes no second change at either
incidence adjacent to `O_1`.  Pair (4.4), and therefore defect (4.6),
survives in the final published relay factor.

### Theorem 5.1 (published-tree prism no-go)

The gamma-alpha modified MNW spanning tree does not by itself satisfy the
one-prefix prepared-prism lemma.  In every suffix fibre, the positive
`H0` boundary lacks the selected incidence

\[
                         (1010001101v,1010001111v).   \tag{5.2}

The obstruction is replicated on pairwise disjoint supports over all
`v in D_(m-5)`.

## 6. The named spare providers are not hit by the first relay pair

The two negative base targets of the closed four-hex macro have complements
`45` and `28`.  Their second canonical inverse witnesses are, respectively,
the pairs `(6,7)` and `(1,6)`.  The corresponding base owner centres are

\[
                         11100001,qquad00111010.       \tag{6.1}

In positive context `10`, the two spare-provider owners are

\[
                         1011100001,qquad1000111010.   \tag{6.2}

Neither is one of the three mirror-gamma lower centres or the three
`alpha(1100)` lower centres.  Thus the *relay pair itself* leaves both spare
providers unchanged.  Additional recursive tuples must still be audited or
chosen to avoid their two selected incidences.

## 7. Sharpened remaining host condition

The one-prefix prepared-prism lemma is not a cyclic-rotation issue and is
not blocked by the source boundary.  Its first unavoidable new action is
the replicated endpoint transfer (4.6), together with the q1-degree
compensation at the other endpoint of `10Q^-` and at the displaced colour
`R`.

A sufficient next lemma is therefore:

> **Leaf endpoint-transfer prism lemma.**  In every suffix fibre, perform
> (4.6) by a common alternating incidence circuit, preserve the two spare
> providers (6.2), and install the complementary rail phases of the
> `01->10` annulus without changing the protected pivot bank.

This is strictly smaller than planting an arbitrary prepared prism: one
destination owner is already exact, the source boundary is canonical, and
the first explicit phase defect is one named leaf incidence per suffix.

