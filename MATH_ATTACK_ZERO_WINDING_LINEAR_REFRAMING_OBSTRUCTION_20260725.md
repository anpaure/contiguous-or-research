# Genuine Gaussian zero-winding returns with linear canonical reframing

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put \(N=2m+1\), and let \(\tau=\phi^2\) be the normalized step-two PBBS
map on semilength-\(m\) Dyck roots.  This note closes one possible route
out of the residual in
`MATH_ATTACK_HEIGHT_SATURATION_DIFFUSE_REFRAMING_20260725.md`.

For every pair of integers

\[
 s\ge3,
 \qquad m\ge2s-1,                                 \tag{0.1}
\]

there are exactly

\[
 \boxed{\binom{m-s-1}{s-2}}                       \tag{0.2}
\]

explicit semilength-\(m\), height-\(s\) Dyck roots which start a genuine
first zero-winding PBBS return of gap \(2s+1\) and whose first \(s-1\)
step-two core transitions all change the canonical first deepest frame.
Thus

\[
 \boxed{R(I)=s-1.}                                \tag{0.3}
\]

In particular, for every fixed \(\alpha>0\), taking

\[
 s_m=\lfloor\alpha\sqrt m\rfloor                 \tag{0.4}
\]

gives genuine Gaussian-height zero-winding returns with

\[
 {R(I)\over s_m}\longrightarrow1.                \tag{0.5}
\]

Consequently zero winding does **not** imply \(R(I)=o(s(I))\), even on a
fixed Gaussian height window.  The linearly reframing residual of the
diffuse-reframing theorem is an actual PBBS class, not a formal artifact.

The family (0.2) is nevertheless Catalan-negligible.  For fixed \(s\) it
is polynomial in \(m\), whereas for \(s=\Theta(\sqrt m)\),

\[
 \binom{m-s-1}{s-2}
 =\exp(O(\sqrt m\log m))
 =\exp(o(m)).                                     \tag{0.6}
\]

This report therefore does not construct a critical
\(\Theta(\operatorname {Cat}_m/\sqrt m)\) packing and does not refute the
corrected coefficient-one gate.  It rigorously refutes only the structural
shortcut that every zero-winding trace must reframe sublinearly.  The next
exact question is the aggregate mass or trace compatibility of linearly
reframing returns.

No assertion of the form \(d(D)=1\Rightarrow\) return is used.  Every
return below is verified from its literal orbit and the exact ordinary
zero-winding equation.

## 1. A general identity: the dual block is exactly the reframing gap

Let

\[
 D_j=P_j1R_j0S_j,qquad 0\le j\le s,              \tag{1.1}
\]

be the canonical first-maximum factorizations along a genuine
zero-winding return of height \(s\).  The audited dual-seam theorem gives
a Dyck word \(T_j\) for every \(0\le j<s\) such that

\[
 \boxed{S_j1P_j=P_{j+1}1\overline{T_j}.}          \tag{1.2}
\]

Here the bar exchanges zero and one without reversing order.

### Theorem 1.1 (frame change iff the dual gap is nonempty)

For \(0\le j<s\), the transition \(D_j\mapsto D_{j+1}\) preserves the
transported canonical first deepest frame if and only if

\[
 \boxed{T_j=\varnothing.}                         \tag{1.3}
\]

#### Proof

The literal block rotation is

\[
 \tau D_j=S_j1P_j0R_j.                            \tag{1.4}
\]

The endpoint of the transported old deepest spine is the height-\(s\)
visit at the end of the prefix \(S_j1P_j\).  This is exactly what the
literal sector update transports: the old marked deepest leaf becomes
that displayed later height-\(s\) visit.

By definition, the new canonical first deepest leaf of \(D_{j+1}\) is
the height-\(s\) visit at the end of \(P_{j+1}1\).  Equation (1.2) says
that the contour segment between these two visits is
\(\overline{T_j}\).  Since \(T_j\) is Dyck, its complement is a
nonpositive excursion from height \(s\) back to height \(s\).

If \(T_j\ne\varnothing\), the first step of \(\overline{T_j}\) is a
down-step and its last step is an up-step.  Hence the two height-\(s\)
visits are distinct, and the new canonical leaf occurs strictly earlier
than the transported leaf.  The frame changes.

If \(T_j=\varnothing\), the two prefixes in (1.2) are identical.  The new
and transported deepest visits are the same leaf.  A rooted tree has a
unique root-to-leaf spine, so the full frames coincide.  This proves
(1.3).  \(\square\)

For a zero-winding interval whose core roots are
\(D_0,\ldots,D_{s-1}\), Theorem 1.1 gives the exact count

\[
 \boxed{
 R(I)=\#\{0\le j\le s-2:T_j\ne\varnothing\}.}    \tag{1.5}
\]

Thus the linearly reframing residual can equivalently be phrased as a
linear density of nonempty dual staircase blocks.  This is an exact
chronology statement, not a static-spine converse.

## 2. Literal star--comb roots

Fix \(s,m\) as in (0.1).  Choose positive integers

\[
 L_0,L_1,\ldots,L_{s-2}\ge1,qquad
 \sum_{i=0}^{s-2}L_i=m-s.                         \tag{2.1}
\]

Put

\[
 E_i=(10)^{L_i}.                                  \tag{2.2}
\]

Define the initial Dyck word literally by

\[
 \boxed{
 D_0=E_0,1E_1,1\cdots1E_{s-2},11,0^s.}       \tag{2.3}
\]

Equivalently, its first deepest sector arrays are

\[
 A_i^{(0)}=E_i\quad(0\le i\le s-2),qquad
 A_{s-1}^{(0)}=\varnothing,                       \tag{2.4}
\]

\[
 B_i^{(0)}=\varnothing\quad(0\le i<s).           \tag{2.5}
\]

Each \(E_i\) has height one.  Read at spine depth \(i\le s-2\), it
reaches height at most \(i+1\le s-1\).  Thus none of these teeth reaches
the global height.  The terminal spine first reaches height \(s\), and
the final \(s\) zeros return directly to zero.  Hence (2.3) is a Dyck
word of height exactly \(s\), and (2.4)--(2.5) are its canonical first
deepest frame.

Its semilength is

\[
 s+\sum_{i=0}^{s-2}L_i=m.                         \tag{2.6}
\]

## 3. Exact sector induction

For later use put

\[
 F_i=(10)^{L_i}.                                  \tag{3.1}
\]

### Theorem 3.1 (successive tooth reframing)

For every \(0\le j\le s-1\), the canonical frame of
\(D_j:=\tau^jD_0\) has

\[
 A_i^{(j)}=
 \begin{cases}
  \varnothing,&0\le i<j,\\
  E_{i-j},&j\le i\le s-2,\\
  \varnothing,&i=s-1,
 \end{cases}                                      \tag{3.2}
\]

and its post-spine forests are empty below level \(s-j\).  The already
consumed combs occur above that level in reverse consumption order.  When
the first tooth of \(E_k\) becomes the new deepest spine child, the
remaining \(L_k-1\) old teeth together with the old transported spine
child form the post-spine comb \(F_k=(10)^{L_k}\).

For every \(0\le j\le s-2\), the transition
\(D_j\mapsto D_{j+1}\) is a genuine frame change.

At \(D_s\), all pre-spine forests are empty.

#### Proof

The assertion at \(j=0\) is (2.4)--(2.5).  Assume (3.2) at a time
\(j\le s-2\).  The literal sector update for the transported frame is

\[
 \widetilde A_0=B_0^{(j)},qquad
 \widetilde A_i=A_{i-1}^{(j)}\quad(1\le i<s),     \tag{3.3}
\]

\[
 \widetilde B_i=B_{i+1}^{(j)}\quad(0\le i<s-1),
 \qquad \widetilde B_{s-1}=\varnothing.           \tag{3.4}
\]

By induction, \(B_0^{(j)}=\varnothing\) for \(j<s\).  The top
pre-spine forest in the transported frame is

\[
 \widetilde A_{s-1}=A_{s-2}^{(j)}=E_{s-j-2}.
\]

It is nonempty.  At depth \(s-1\), its first tooth reaches height \(s\)
strictly before the transported deepest leaf.  Therefore that tooth is
the new canonical deepest child, so the transition changes frame.

Reframing around this first tooth replaces the top pre-spine forest by
the empty forest.  After the selected tooth returns, the contour reads
the remaining \(L_{s-j-2}-1\) old teeth and then the old transported
spine child, which is itself a leaf.  The top post-spine forest is
therefore

\[
 F_{s-j-2}=(10)^{L_{s-j-2}}.                      \tag{3.5}
\]

All lower pre-spine forests are exactly the shifts in (3.3), and every
older post-spine residue shifts down one level by (3.4).  This proves
(3.2) at time \(j+1\) and also shows that no residue reaches \(B_0\)
before time \(s\).  The induction gives a frame change at each
\(j=0,\ldots,s-2\).

After the last such transition, every original \(E_i\) has been consumed
and all pre-spine forests are empty.  One final literal update gives
\(D_s\), still with all pre-spine forests empty.  \(\square\)

The extra final tooth in (3.5) is essential: it is the old transported
spine child.  Omitting it would give \((10)^{L_i-1}\) and would violate
literal word length.  For example, at \(s=2,L_0=1\),
\(101100\) maps to \(110100\), whose new top post-spine forest is
\(10\), not the empty forest.

## 4. Exact zero-winding and first-return verification

For a canonical sector word, the suffix \(S(D)) in

\[
 D=P1R0S
\]

is the root-level post-spine forest \(B_0\).  Theorem 3.1 therefore gives

\[
 S(D_j)=\varnothing,qquad
 d(D_j)=|S(D_j)|+1=1
 \quad(0\le j<s).                                 \tag{4.1}
\]

At time \(j<s\), the unconsumed pre-spine teeth are
\(E_0,\ldots,E_{s-j-2}\).  Hence the position of the first
maximum-reaching step is

\[
 \boxed{
 \delta(D_j)=s+2\sum_{i=0}^{s-j-2}L_i\ge s>j,}   \tag{4.2}
\]

where the sum is empty at \(j=s-1\).  The weak first inequality is exact
at that endpoint.

At time \(s\), all pre-spine forests are empty, and therefore

\[
 \boxed{\delta(D_s)=s.}                           \tag{4.3}
\]

Equations (4.1) and (4.3) give the ordinary zero-winding identity

\[
 \sum_{j=0}^{s-1}d(D_j)=s=\delta(D_s)<N.          \tag{4.4}
\]

For every \(0\le j<s\), its proper partial sum is \(j\), whereas (4.2)
gives \(j<\delta(D_j)<N\).  Thus no earlier ordinary equality is
possible.  Since both quantities lie in \([0,N)\), no earlier modular
equality with nonzero winding is possible either at an earlier odd
endpoint.  Moreover every normalized state on the segment has invariant
height \(s\).  The exact height--gap theorem forbids a return of either
parity at every gap smaller than \(2s+1\).  Therefore (4.4) is the first
omitted-coordinate return.  It occurs after \(s\) step-two moves and the
final odd move, so its literal PBBS gap is

\[
 \boxed{2s+1.}                                    \tag{4.5}
\]

The endpoint-overlap statistic is also exact.  Since

\[
 \delta(D_0)=s+2\sum_{i=0}^{s-2}L_i=2m-s,
 \qquad \delta(D_s)=s,
\]

one has

\[
 \boxed{\Lambda=\delta(D_0)+\delta(D_s)-2m=0.}   \tag{4.6}
\]

Thus maximal reframing cannot be charged to positive winding or to
positive endpoint overlap.  In this construction every preempting forest
has height one as well, so it cannot be charged to a disjoint collection
of tall preempting witnesses.

The first \(s-1\) core transitions are precisely
\(D_j\mapsto D_{j+1}\), \(0\le j\le s-2\).  Theorem 3.1 consequently
proves (0.3).

## 5. Exact enumeration and Gaussian floors

Condition (2.1) is a positive composition of \(m-s\) into \(s-1\)
parts.  It has exactly

\[
 \binom{(m-s)-1}{(s-1)-1}
 =\binom{m-s-1}{s-2}                              \tag{5.1}
\]

solutions.  Distinct compositions give distinct roots: the canonical
first deepest frame of (2.3) uniquely recovers every run \(E_i\), and
hence every \(L_i\).  This proves the exact count (0.2).

Fix \(\alpha>0\) and set

\[
 s_m=\lfloor\alpha\sqrt m\rfloor.                \tag{5.2}
\]

For all sufficiently large \(m\),

\[
 s_m\ge3,qquad m\ge2s_m-1,                       \tag{5.3}
\]

so the construction applies.  Its height is exactly \(s_m\), and

\[
 {s_m\over\sqrt m}\to\alpha,qquad
 {R(I)\over s_m}=1-{1\over s_m}\to1.             \tag{5.4}
\]

If a fixed window \([a\sqrt m,A\sqrt m]\) is prescribed, choose any
\(a<\alpha<A\).  Then (5.2) lies inside that window for all sufficiently
large \(m\).  If an upper duration is written
\(H_A=\lceil A\sqrt m\rceil\), one also has
\(s_m\le H_A\) eventually.  Under the alternative convention that the
final odd edge is included in the residence parameter, choose
\(\alpha<A\); then \(s_m+1\le H_A\) eventually as well.  This records all
endpoint floors explicitly.

For the size assertion, the standard elementary estimate gives

\[
 \binom{m-s-1}{s-2}
 \le\left({e(m-s-1)\over s-2}\right)^{s-2}.       \tag{5.5}
\]

When \(s=\Theta(\sqrt m)\), its logarithm is
\(O(\sqrt m\log m)=o(m)\).  On the other hand,

\[
 \operatorname {Cat}_m
 =\exp(m\log4-O(\log m)).                          \tag{5.6}
\]

Thus the family is exponentially negligible relative to Catalan mass.
It may lie entirely on the already negligible collection of short
quotient cycles; the standard short-cycle bound has the same
subexponential scale and cannot be subtracted from (5.1).  Accordingly no
packing lower bound is claimed.

## 6. Exact boundary

The following are proved.

1. The dual block \(T_j\) measures the literal gap between the new and
   transported deepest leaves, so a zero-winding transition reframes iff
   \(T_j\ne\varnothing\).
2. The star--comb word (2.3) is an exact semilength-\(m\), height-\(s\)
   Dyck root for every positive composition (2.1).
3. Its first \(s-1\) core transitions all reframe.
4. Its deficit ledger is exactly \(1,\ldots,1\), and the first return is
   the zero-winding equality at gap \(2s+1\).
5. The exact family size is (5.1), and Gaussian choices of \(s\) have
   reframing density tending one.

What is not proved is Catalan-scale mass, long-cycle survival, or a
critical quotient packing.  Hence the corrected coefficient-one gate
remains open.  The exact surviving statement is now narrower:

\[
 \boxed{
 \text{prove that linearly many mutually compatible reframings have
 aggregate packing }o(\operatorname {Cat}_m/\sqrt m),
 }
\]

or construct a Catalan-critical long-cycle family contradicting it.
