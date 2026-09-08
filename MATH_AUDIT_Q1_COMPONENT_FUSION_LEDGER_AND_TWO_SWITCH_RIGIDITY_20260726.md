# Audit of the depth-one component-fusion ledger and two-switch rigidity

Date: 2026-07-26

Audited source:
MATH_THEOREM_Q1_COMPONENT_FUSION_LEDGER_AND_TWO_SWITCH_RIGIDITY_20260726.md.

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

The note passes. In particular:

1. the weighted endpoint argument, including isolated owners, gives exactly

   \[
   c(F)\le \frac{W}{m+\varepsilon+1};
   \]

2. every missing-colour, collision-excess, and signed conservation identity
   in Theorem 2.2 is correct;
3. the lower--upper two-flag rectangle is necessarily the displayed
   four-coordinate star; and
4. no nontrivial two-edge trade preserves simultaneously both signed colour
   multisets and the complete middle-degree vector.

The scope is also correct. Unrestricted endpoint splicing proves an
\(o(W)\)-defect, \(O(W/m)\)-component forest, but does not preserve exact
rainbowness. The Hall theorem in Section 5 gives upper exactness and lower
coverage, not lower floor/ceiling load at most two. Neither result proves
the missing exact common refinement.

## 1. Weighted endpoint spectral bound

Let the maximal splice forest have \(p\) nontrivial path components, \(z\)
isolated owners, and \(c=p+z\) total components. Put weight one on each
genuine endpoint of a nontrivial path, weight two on each isolated owner,
and zero elsewhere. Then

\[
 \sum_Xw_X=2c,\qquad
 \|w\|_2^2=2p+4z=2c+2z.                              \tag{1.1}
\]

Maximality forbids a Johnson edge between positive-weight owners belonging
to different components. Within one nontrivial path there is only one
unordered pair of endpoints, and its weights are both one. Isolated
owners create no loop. Therefore

\[
                         w^TA_Jw\le2p=2(c-z).          \tag{1.2}
\]

This is the exact point at which treating an isolated owner as two distinct
vertices would be invalid; the weight-two convention handles it correctly.

The Johnson graph \(J(2m+\varepsilon,m)\) is
\(k=m(m+\varepsilon)\)-regular, with eigenvalues

\[
 \theta_j=(m-j)(m+\varepsilon-j)-j,\qquad 0\le j\le m.
\]

Their consecutive differences are

\[
 \theta_{j+1}-\theta_j=-(2m+\varepsilon-2j)<0,
\]

so \(\lambda_{\min}=\theta_m=-m\). For every real vector \(v\), constant
plus orthogonal decomposition gives

\[
 v^TA_Jv\ge
 \frac{k+m}{W}\left(\sum_Xv_X\right)^2-m\sum_Xv_X^2
 =
 \frac{m(m+\varepsilon+1)}W\left(\sum_Xv_X\right)^2
 -m\sum_Xv_X^2.                                      \tag{1.3}
\]

Applying (1.3) to \(w\) and combining with (1.1)--(1.2) yields

\[
 2(c-z)\ge
 \frac{4m(m+\varepsilon+1)}Wc^2-2mc-2mz,
\]

and hence

\[
 \frac{4m(m+\varepsilon+1)}Wc^2
 \le2(m+1)c+2(m-1)z
 \le4mc.
\]

For \(c>0\), division by \(4mc\) proves

\[
                         c\le\frac{W}{m+\varepsilon+1}. \tag{1.4}
\]

All constants and inequality directions pass. Consequently
\(Hc/W=o(1)\) exactly when \(H=o(m)\), as claimed.

## 2. Colour-defect ledger

A spanning forest with \(c_0\) components has \(W-c_0\) edges. If both
colour maps are initially injective, adding
\(s=c_0-c(F)\) splice edges can never shrink either support, and each added
edge raises collision excess on one fixed shore by at most one. Thus

\[
 M_\sigma(F)\le M_\sigma(F_0),\qquad
 R_\sigma(F)\le s<c_0.
\]

The initial hole formulas follow by subtracting \(W-c_0\) from the shore
sizes. On even ground the two shores have size
\(W-W/(m+1)\), giving

\[
 M_-(F_0)=M_+(F_0)=c_0-\frac{W}{m+1}.
\]

On odd ground their sizes are \(W-2W/(m+2)\) and \(W\), giving

\[
 M_-(F_0)=c_0-\frac{2W}{m+2},\qquad M_+(F_0)=c_0.
\]

Finally, for every graph and every shore,

\[
 R_\sigma-M_\sigma
 =(|E|-|\operatorname{supp}_\sigma|)
  -(N_\sigma-|\operatorname{supp}_\sigma|)
 =|E|-N_\sigma.
\]

Substituting \(|E(F)|=W-c(F)\) gives exactly (2.9d)--(2.9e).
Thus the proof tracks every repeat introduced by fusion; it does not hide
one as a missing colour.

## 3. Two-flag rectangle classification

Suppose distinct lower sets \(S,T\) and distinct upper sets \(U,V\) satisfy
all four containments. Then

\[
 S\cup T\subseteq U\cap V.
\]

The left side has size at least \(m\), while the right side has size at most
\(m\). Equality follows, giving the unique middle set

\[
 X=S\cup T=U\cap V.
\]

Writing

\[
 S=X-p,\quad T=X-q,\quad U=X+a,\quad V=X+b
\]

with \(p\ne q\) and \(a\ne b\) gives exactly the old and crossed star flags
listed in the source. There is no second rectangle type.

If a two-edge trade preserves the two lower and two upper colour multisets,
then either the lower-to-upper pairing is unchanged, in which case each
flag determines the same Johnson edge, or the pairing is crossed and the
star classification applies. In the crossed case the central owner \(X\)
has multiplicity two on both sides. The other four owners are

\[
 X-p+a,\quad X-q+b,\quad X-p+b,\quad X-q+a.
\]

They are pairwise distinct: equality with a common deleted coordinate
forces \(a=b\), equality with a common inserted coordinate forces \(p=q\),
and a diagonal equality forces both. Hence the two middle-incidence
multisets cannot agree. Theorem 4.1 passes.

Corollary 4.2 also passes: for any two spanning rainbow forests,
\[
 |E(F')|-|E(F)|
 \le N_\sigma-|E(F)|=M_\sigma(F)
\]
on each shore, independently of whether \(F\subseteq F'\).

## 4. Odd-ground Hall and component scope

An exact lower core on odd ground has

\[
 N_1=W-\frac{2W}{m+2}
\]

edges. If it is a spanning forest, it has exactly
\[
 d=W-N_1=\frac{2W}{m+2}
\]
path or isolated components. A residual incidence flow satisfying (5.5)
adds exactly \(d\) edges. After contracting the old paths, these edges
form a \(2\)-regular multigraph on \(d\) vertices, allowing loops and
parallel edges in the quotient but giving a simple physical factor before
contraction. Hence the completed factor has at most \(d=o(W/H)\)
components for \(H=o(m)\).

The Hall network chooses two distinct facets of every unused upper set. It
therefore proves upper load one and lower coverage. It does not prevent
two different completion edges from having the same lower intersection.
If exact lower floor/ceiling balance is required, one must add lower-colour
capacity one, obtaining the separate determinant-two flag-matching system.
This is a scope qualification, not an error in the source, which explicitly
states the lower conclusion as “at least once.”

## 5. Final boundary

The unconditional result is exactly:

> A spanning two-sided-rainbow linear forest with \(o(W)\) components can
> be spliced by literal Johnson edges to one with \(O(W/m)\) components,
> without increasing holes and with only \(o(W)\) collision excess.

It does not yield an exact two-sided-rainbow factor. The no-two-edge-switch
theorem shows that a colour- and owner-exact repair cannot be assembled from
ordinary two-edge switches. A larger compound trade, or a Hall-aware
initial construction, remains necessary.

