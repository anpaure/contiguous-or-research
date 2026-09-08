# CMS is closed; failure of the remaining packing gate forces a critical double-deck saturation

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

There are two results in this note.

1.  The crossing-mask seam theorem `CMS(H)` is valid.  In fact it is an
    arbitrary-Johnson-walk theorem, not a PBBS-specific theorem.  At one
    cut the lower crossing masks are two-dimensional dominance filters of
    the residence endpoint pairs.  Floor correctness excludes a strict
    southwest endpoint pair, and a southeast path through the Pareto
    minima represents every required lower mask by one contiguous union.
    The exact constructed cost is

    \[
       (2H-1)+2H=4H-1                                      \tag{0.1}
    \]

    nonzero letters, provided \(2H\le m+1\).  Together with endpoint
    erosion this gives \(\ell+(5H-1)J\) on a cycle cut at \(J\) edges.

2.  Write \(N=2r+1\), \(B_r=\operatorname {Cat}_r\), and let
    \(\overline\nu_H\) be the long-cycle quotient packing of PBBS
    residence intervals.  If the presently weakest direct gate

    \[
       \overline\nu_{\lceil A\sqrt r\rceil}
       =o_A(B_r/\sqrt r)                                  \tag{0.2}
    \]

    fails, then, after an absolute factor-two loss, there is a
    projected-edge-disjoint family of *simple fixed-core sectors* which
    covers a positive fraction of an entire PBBS quotient deck, and whose
    one-edge translates are also pairwise disjoint.  Every retained sector
    has both height and duration of order \(\sqrt r\).  Thus a critical
    counterfamily is not a sparse exceptional collection: it is a
    positive-density double-deck partial tiling by open-wreath sectors.

The second statement is an equality/stability normal form for the
reciprocal-height argument.  It does not prove (0.2), but it isolates the
additional structure that any strictness theorem must rule out.

## 1. Endpoint-pair normal form at one cut

Let

\[
 X_{i+1}=X_i-\{\alpha_i\}+\{\beta_i\},
 \qquad |X_i|=m+1,
\]

and cut between \(X_{-1}\) and \(X_0\).  Put

\[
 C=X_{-1}\cap X_0,
 \qquad |C|=m.
\]

For \(1\le s,t\le H\), write

\[
 P_{s,t}=\bigcap_{i=-s}^{t-1}X_i.                  \tag{1.1}
\]

For each \(x\in C\), let \(u_x\) and \(v_x\) be its capped consecutive
positive-residence extents to the left and right of the cut:

\[
\begin{aligned}
u_x&=\max\{u\le H:x\in X_{-u}\cap\cdots\cap X_{-1}\},\\
v_x&=\max\{v\le H:x\in X_0\cap\cdots\cap X_{v-1}\}.
\end{aligned}                                      \tag{1.2}
\]

Then, exactly,

\[
 \boxed{P_{s,t}=\{x\in C:u_x\ge s,\ v_x\ge t\}.} \tag{1.3}
\]

Thus the \(O(H^2)\) lower crossing masks are dominance filters of the at
most \(m\) endpoint pairs \(p_x=(u_x,v_x)\).

## 2. The only local obstruction disappears at the correct rank

The intersection in (1.1) uses \(s+t\) owners and therefore satisfies

\[
 |P_{s,t}|\ge m+2-s-t.                              \tag{2.1}
\]

Call it floor-correct when equality holds.

### Lemma 2.1 (southwest exclusion)

If \(P_{s,t}\) is floor-correct, then no endpoint pair is strictly
southwest of \((s,t)\):

\[
 \boxed{\nexists x\in C:\ u_x<s\text{ and }v_x<t.} \tag{2.2}
\]

#### Proof

List the \(L=s+t\) owners of (1.1) in chronological order.  Send every
coordinate of the first owner which is absent from the full intersection
to its first departure transition.  This is an injection into the
\(L-1\) transitions.

If (2.2) failed, the coordinate \(x\) would arrive internally before the
cut and depart internally after the cut.  The latter departure cannot be
the first departure of an initial coordinate: if \(x\) was not initial it
is outside the domain of the injection, while if it was initial it already
departed before its displayed re-arrival.  That transition also cannot be
charged to another coordinate.  Hence the injection uses at most \(L-2\)
transitions, giving

\[
 |P_{s,t}|\ge(m+1)-(L-2)=m+3-s-t,
\]

contrary to floor correctness. \(\square\)

This is the precise reason arbitrary FIFO/LIFO endpoint order is not
needed.  PBBS can exhibit the endpoint permutation \(213\); (2.2), not
endpoint monotonicity, is the operative condition.

## 3. A linear dominance staircase

Take the distinct Pareto-minimal points among \(\{p_x:x\in C\}\), order
them by increasing first coordinate, and join them by a southeast unit
lattice path \(\Gamma\) from \((1,H)\) to \((H,1)\), moving east before
south between successive required points.  Then

\[
 |\Gamma|=2H-1.                                    \tag{3.1}
\]

If a query \(q=(s,t)\) has no endpoint pair strictly southwest of it,
then every rectangle \([q,p_x]\), with \(p_x\ge q\), meets \(\Gamma\).
Indeed descend from \(p_x\) to a Pareto minimum.  If that minimum is west
of \(q\), move forward until first coordinate \(s\); if it is south of
\(q\), move backward until height \(t\).  Southwest exclusion and the
east-before-south convention keep the other coordinate inside the
rectangle.

Emit the actual set \(P_z\) for each \(z\in\Gamma\).  Along \(\Gamma\),
the condition \(z_1\ge s\) is a suffix and \(z_2\ge t\) is a prefix, so
their conjunction is a contiguous subpath.  Coordinatewise rectangle
interception and (1.3) give

\[
 \boxed{
 P_{s,t}=\bigcup_{\substack{z\in\Gamma\\z\ge(s,t)}}P_z
 }
                                                               \tag{3.2}
\]

for every floor-correct query.  Every helper is nonempty when
\(2H\le m+1\), since it intersects at most \(2H\) consecutive owners and
therefore has size at least \(m+2-2H\ge1\).

The upper crossing masks require no endpoint analysis: emit

\[
 X_{-H},X_{-H+1},\ldots,X_{H-1}.                  \tag{3.3}
\]

Every crossing union of at most \(H+1\) owners is the union of its
literal contiguous subsegment.  Equations (3.1)--(3.3) prove the
\(4H-1\) one-cut theorem.  Appending one such chart at every cut to the
endpoint-capped erosion words proves `CMS(H)` with total active-cycle
length

\[
 \boxed{\ell+(5H-1)J.}                            \tag{3.4}
\]

This independently confirms
`MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md` and
`MATH_ATTACK_Y15_PBBS_LINEAR_DOMINANCE_SEAM_AUDIT_20260725.md`.

## 4. Reciprocal-height capacity and its equality case

The local seam is therefore closed.  Consider the quotient packing gate.
The PBBS quotient permutation preserves Dyck height.  Let

\[
 b_{r,h}=\#\{D\in\mathcal D_r:\operatorname{ht}(D)=h\}.
\]

A residence interval beginning at height \(h\) uses at least \(h+2\)
quotient transition edges.  Hence every projected-edge-disjoint family
\(\mathcal P\) satisfies

\[
 (h+2)|\mathcal P_h|\le b_{r,h}.                  \tag{4.1}
\]

Summing and using the Dyck height spectrum gives

\[
 \overline\nu_H\le
 \sum_h\frac{b_{r,h}}{h+2}=O(B_r/\sqrt r).        \tag{4.2}
\]

There is an exact defect decomposition behind (4.1).  If a selected
height-\(h\) trace \(I\) has \(k(I)\) quotient edges and
\(U_h\) height-\(h\) edges are uncovered by the selected traces, then

\[
 \boxed{
 b_{r,h}-(h+2)|\mathcal P_h|
 =U_h+\sum_{I\in\mathcal P_h}\bigl(k(I)-h-2\bigr).}
                                                               \tag{4.2a}
\]

Both terms on the right are nonnegative.  Thus exact saturation at one
height is equivalent to a tiling of the whole height stratum by
minimum-gap returns; near saturation forces simultaneously near-covering
and small mean height-gap slack.  This is the precise equality case of the
reciprocal-height proof.

The following stability statement records exactly what failure of the
needed strict little-oh means.

### Theorem 4.1 (critical double-deck saturation normal form)

Fix \(A>0\).  Suppose that along an infinite sequence of ranks there is
an \(\varepsilon>0\) and a projected-edge-disjoint family of nonwrapping
PBBS residence intervals of residence at most
\(H=\lceil A\sqrt r\rceil\) with

\[
 |\mathcal P|\ge\varepsilon B_r/\sqrt r.          \tag{4.3}
\]

Then there are constants \(a=a(A,\varepsilon)>0\) and
\(c=c(A,\varepsilon)>0\), and a projected-edge-disjoint family
\(\mathcal Q\) of simple PBBS return sectors, such that

1. \(|\mathcal Q|\ge cB_r/\sqrt r\);
2. every member has initial height
   \(a\sqrt r\le h\le A\sqrt r\);
3. every trace has between \(a\sqrt r\) and \(A\sqrt r+1\) edges;
4. the union of the traces contains at least \(cB_r\) quotient edges;
5. the one-edge translates of all these traces are pairwise disjoint;
6. every member has the exact simple fixed-core open-wreath normal form.

#### Proof

The standard minimal-return reduction shrinks every return to a simple
one and, after splitting by the parity of the shrinkage, retains at least
half the family.  In the retained parity class both the simple traces and
their one-edge translates remain pairwise disjoint.  This proves items 5
and 6 and loses only an absolute factor two.

For any fixed \(a>0\), the path-graph spectral estimate gives

\[
 \sum_{h<a\sqrt r}\frac{b_{r,h}}{h+2}
 \le \eta(a)\frac{B_r}{\sqrt r},
 \qquad \eta(a)\longrightarrow0\quad(a\downarrow0).
                                                               \tag{4.4}
\]

Choose \(a\) so that the right side is at most
\(\varepsilon B_r/(4\sqrt r)\), with the harmless constants enlarged to
absorb the factor-two reduction.  Inequality (4.1) then shows that
discarding all lower-height sectors leaves a family \(\mathcal Q\) of
size at least \(cB_r/\sqrt r\).  The height-gap theorem and the residence
cutoff give items 2 and 3.  Finally the traces are disjoint and every one
has at least \(a\sqrt r\) edges, so their union has size at least

\[
 a\sqrt r\,|\mathcal Q|\ge cB_r,
\]

which is item 4. \(\square\)

## 5. Consequence for the remaining proof strategy

The strictness missing from (4.2) cannot be obtained from another scalar
height moment.  A counterfamily at the critical scale necessarily gives a
positive-density packing in *both* parity decks by Gaussian-sized,
rainbow, fixed-core open-wreath sectors.  Therefore it is enough to prove
either of the following structural statements:

1. no family of simple PBBS sectors satisfying items 2, 3, 5, and 6 of
   Theorem 4.1 can cover a fixed positive fraction of a height deck; or
2. every such positive-density double-deck packing is confined to a Dyck
   chronology class of \(o(B_r)\) roots.

This is strictly sharper than asking for an unspecified improvement in
the reciprocal-height sum.  It identifies the equality object: a
Gaussian-scale partial tiling by two synchronized, shifted systems of
fixed-core open-wreath sectors.

The theorem does not assert that this object is impossible.  Establishing
that impossibility, or constructing a shared cross-cut compiler which
handles it at sublinear cost, is the surviving PBBS task.
