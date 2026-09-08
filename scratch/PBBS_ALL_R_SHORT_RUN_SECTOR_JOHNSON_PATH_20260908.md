# An explicit Johnson path through the entire PBBS three-run sector

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: proved for every `r>=3`. The proof is algebraic; bounded checks at
`r=3,...,10` used only the explicit short-run sector and ran only on h100.
No all-r upper-support preservation or universal-word claim is made.

## 1. The general construction

Put `n=2r+1` and `M=r-2`. Represent a rooted rank-r state by

\[
 D(x,y,z)=(10)^x1(10)^{y+1}0(10)^z,
 \qquad x+y+z=M,
\]

with unmatched physical zero at `u`. The established explicit PBBS map is

\[
 f(x,y,z,u)=(y,z,x,u+2(x+1))\pmod n,
 \qquad g=f^2.                                             \tag{1.1}
\]

Its third power rotates the physical state by one position. Let `rho`
denote that rotation. Thus `f^3=rho`, and each boundary-triple component
has period `3n` under both f and g.

For `0<=b<=r-3`, define the physical lower state

\[
 A_b=(b,r-2-b,0,n-1).                                      \tag{1.2}
\]

These represent the `r-2` distinct components containing all positive
three-runs of the complementary upper-middle factor. This exact component
classification is proved in
`scratch/PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md`.

For `1<=b<=r-3`, put `c_b=2n-b`; put `c_0=0`. Open the b-th component
at `g^(c_b)A_b` and traverse it forward for its full `3n` states. Order
the resulting blocks by

\[
                         1,2,\ldots,r-3,0.                \tag{1.3}
\]

For r=3 the list consists just of block zero. Complement every lower state
to obtain upper-middle owners.

**Theorem.** The resulting sequence contains exactly

\[
                            3(2r+1)(r-2)
\]

distinct rank-(r+1) owners. It is a Johnson path, and every internal
positive coordinate run has length at least three. Its maximal
depth-two source is nonempty, has two more letters than the number of
owners, and reproduces every owner exactly.

At r=8 this is exactly the already materialized all-ports Johnson
306-owner path. The formula does not require another optimization or
search in each dimension.

## 2. Explicit parity forms

Write `evens[a,b]` or `odds[a,b]` for the integers of that parity in the
displayed inclusive range, interpreted as empty if the range is empty.
All physical labels lie in `0,...,2r`; rotation is modulo n.

In physical coordinates (1.2) is

\[
 A_b=\operatorname{evens}[0,2b]
       \cup\operatorname{odds}[2b+1,2r-3].                  \tag{2.1}
\]

Put `B_b=fA_b` and `C_b=f^2A_b`. Direct complementation at the unmatched
root, or substitution in (1.1), gives

\[
 B_b=\operatorname{odds}[1,2b-1]
       \cup\operatorname{evens}[2b+2,2r-2]
       \cup\{2r-1\},                                      \tag{2.2}
\]

\[
 C_b=(A_b\setminus\{2b+1\})\cup\{2r\}.                    \tag{2.3}
\]

For consecutive parameters b,b+1, put

\[
                      x=2b+1,\quad y=2b+2,\quad z=2b+3.
\]

Their differences in the three f-phases are

\[
\begin{array}{c|cc}
\text{phase}&\text{left-only coordinate}&\text{right-only coordinate}\\\hline
0&A_b\setminus A_{b+1}=\{x\}&A_{b+1}\setminus A_b=\{y\}\\
1&B_b\setminus B_{b+1}=\{y\}&B_{b+1}\setminus B_b=\{x\}\\
2&C_b\setminus C_{b+1}=\{z\}&C_{b+1}\setminus C_b=\{y\}.
\end{array}                                                \tag{2.4}
\]

Thus equal-time pairs `f^tA_b,f^tA_(b+1)` are Johnson-adjacent for every
integer t, because f³ is a common rotation.

## 3. Exact seam test for short complementary runs

Write the lower-owner stencil at a proposed seam as

\[
                         L_2,L_1,L_0\mid R_0,R_1,R_2.
\]

Suppose `L_0,R_0` are Johnson-adjacent, with
`L_0 minus R_0={alpha}` and `R_0 minus L_0={beta}`. In the complemented owner
row, every positive run meeting this seam has length at least three if
and only if

\[
 \alpha\notin R_1\cup R_2,\qquad
 \beta\notin L_1\cup L_2,\qquad
 L_1\cap R_1\subseteq L_0\cup R_0.                         \tag{3.1}
\]

Indeed alpha is the coordinate whose complementary positive run begins at
R_0, so its first three positions are positive precisely under the first
test. The coordinate beta ends its complementary positive run at L_0, giving
the second test. For a coordinate positive at both L_0 and R_0, the only
remaining bad possibility is a two-position run, with that coordinate
present in both lower owners L_1,R_1. The third test excludes it. All
other coordinates are absent from both complementary seam endpoints and
have no positive run meeting the seam.

Equivalently, without using Johnson adjacency, the five forbidden run
patterns of length one or two are excluded by

\[
\begin{split}
 L_1\cap R_0&\subseteq L_0,\qquad
 L_0\cap R_1\subseteq R_0,\\
 L_2\cap R_0&\subseteq L_1\cup L_0,\\
 L_1\cap R_1&\subseteq L_0\cup R_0,\\
 L_0\cap R_2&\subseteq R_0\cup R_1.
\end{split}                                                \tag{3.2}
\]

## 4. Every interior block seam passes

For `1<=b<=r-4`, the left block's last state and the next block's first
state are

\[
                  g^{2n-b-1}A_b,\qquad g^{2n-b-1}A_{b+1}.
\]

They are equal-time pairs, so (2.4) proves Johnson adjacency. It remains
to check (3.1). Remove their common spatial rotation, reducing the f-time
to phase 0, 1, or 2. Their exact stencils are:

\[
\begin{array}{c|ccc|ccc}
 &L_2&L_1&L_0&R_0&R_1&R_2\\\hline
0&\rho^{-2}C_b&\rho^{-1}B_b&A_b&A_{b+1}&C_{b+1}&\rho B_{b+1}\\
1&\rho^{-1}A_b&\rho^{-1}C_b&B_b&B_{b+1}&\rho A_{b+1}&\rho C_{b+1}\\
2&\rho^{-1}B_b&A_b&C_b&C_{b+1}&\rho B_{b+1}&\rho^2 A_{b+1}.
\end{array}                                                \tag{4.1}
\]

Here are the three checks in explicit label form. In phase zero,
`alpha=x,beta=y`; formulas (2.1)–(2.3) give

\[
 x\notin C_{b+1}\cup\rho B_{b+1},\qquad
 y\notin\rho^{-1}B_b\cup\rho^{-2}C_b.
\]

The only possible coordinate of `R_1` outside `L_0 union R_0` is `2r`,
and it is absent from `rho^(-1)B_b` because 0 is absent from B_b.

In phase one, `alpha=y,beta=x`, and

\[
 y\notin\rho A_{b+1}\cup\rho C_{b+1},\qquad
 x\notin\rho^{-1}C_b\cup\rho^{-1}A_b.
\]

The only possible coordinate of `R_1` outside `L_0 union R_0` is z.
It is absent from `rho^(-1)C_b`, since `z+1=2b+4` is absent from C_b.

In phase two, `alpha=z,beta=y`, and

\[
 z\notin\rho B_{b+1}\cup\rho^2A_{b+1},\qquad
 y\notin A_b\cup\rho^{-1}B_b.
\]

The only possible coordinate of `L_1` outside `L_0 union R_0` is x.
It is absent from `rho B_(b+1)`, because `x-1=2b` is absent from B_(b+1).
These observations verify all of (3.1) in every phase. The range
`b<=r-4` ensures the displayed labels and parity intervals have the
stated positions, without a hidden cyclic endpoint identification.

## 5. The final seam also passes

For r>=4, the last nonzero block has parameter `b=r-3`. Its final
state is

\[
 g^{3r+4}A_{r-3}=f^5A_{r-3},
\]

because `2(3r+4)=3n+5` and this component has f-period 3n. The following
block begins at A_0. Their exact six-owner stencil is

\[
\begin{aligned}
 L_0&=\{0\}\cup\operatorname{odds}[1,2r-5]\cup\{2r-2\},\\
 R_0&=\{0\}\cup\operatorname{odds}[1,2r-3],\\
 L_1&=\operatorname{odds}[1,2r-5]\cup\{2r-4,2r-2\},\\
 L_2&=\operatorname{odds}[1,2r-7]\cup\{2r-4,2r-2,2r-1\},\\
 R_1&=\{0\}\cup\operatorname{odds}[3,2r-3]\cup\{2r\},\\
 R_2&=\operatorname{odds}[3,2r-1]\cup\{2r\}.
\end{aligned}                                              \tag{5.1}
\]

The seam replaces `alpha=2r-2` by `beta=2r-3`, so it is Johnson.
The coordinate alpha is absent from R_1,R_2, and beta is absent from L_1,L_2.
The only possible coordinate of R_1 outside `L_0 union R_0` is 2r,
which is absent from L_1. Thus (3.1) holds. At r=3 there is only one
block and no seam to check.

## 6. Completion of the shallow-path proof

The component classification supplies pairwise disjoint blocks, each of
length 3n, so the stated owner count and uniqueness follow. Each old
component is a Johnson cycle and has no positive run shorter than three.
Sections 4–5 prove the same properties at every new seam. A run of length
at most two cannot cross two seams because every block has length at least
21. Hence the whole linear owner path has no internal positive run of
length one or two.

For a path of length L, define its source by

\[
 E_p=\bigcap_{\max(0,p-2)\le i\le\min(p,L-1)}T_i,
 \qquad0\le p<L+2.
\]

At most three consecutive rank-(r+1) Johnson owners are intersected, so
every letter has size at least r−1 and is nonempty. The positive-run
condition is exactly the depth-two residence criterion, so
`E_i union E_(i+1) union E_(i+2)=T_i` for every owner i.

This is a constructive shallow source on the entire short-run sector in
every dimension under consideration. It is not the full-cube word: it
contains only O(r²) of the exponentially many middle owners.

## 7. Bounded checks and exact limit of the result

For r=3,...,10, a bounded remote check generated only the stated
`3n(r-2)` states using (1.1). The owner lengths were respectively

```text
21, 54, 99, 156, 225, 306, 399, 504.
```

Every seam had Hamming distance two and every complete path had minimum
internal positive run three. No full middle factor was rebuilt for these
checks, and no alternative cuts or orderings were tried.

The r=8 path coincides with the full exact decision recorded in
`scratch/K17_PBBS_ALLPORTS_JOHNSON_306_OWNER_PREFIX_20260908.md`, where
its depth-two source, internal facet injectivity, and full global proper
upper coverage against the other 140 intact cycles were separately
verified. Those additional upper and facet properties are **not** claimed
for all r by the present theorem.

The remaining all-dimensional tasks are therefore to control the upper
targets lost when these cycles are opened, integrate the clean sector with
valid seams, and produce the shared lower compiler. The formula removes
the need to search for the shallow bad-sector path itself.

## 8. Internal review

Root independently read this full proof and the original component
classification, checked the three phase stencils and the final seam
containments algebraically, and found the general claims valid. The
exchanged-coordinate names were then clarified to alpha and beta to keep
them distinct from the block parameter b. This is an internal review;
no external or formal verification is asserted.
