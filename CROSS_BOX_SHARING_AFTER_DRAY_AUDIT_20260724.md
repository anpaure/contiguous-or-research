# Independent mathematical audit: cross-box sharing after DRAY

Date: 2026-07-25

Audited source: `CROSS_BOX_SHARING_AFTER_DRAY_20260724.md`

Method: proof audit only.  No web search and no finite computation were used.

## 1. Verdict

The mathematical core passes.

In particular, the following statements are valid as written in the body of
the note:

\[
 \sum_{\mathcal B} g_3(\mathcal B)\leq \sum_j d_j,
\]

the translated plateau endpoint inequality

\[
 (C_L-w)+(C_R-w)\geq \frac{w(r-p-q)}r,
\]

the positive-density dominant-box estimate

\[
 \Delta_s=\sum_{\mathcal B}(g_3(\mathcal B)-w(\mathcal B))
 \geq \delta_0 W_{3s},
\]

and the two resulting sharing-capacity inequalities

\[
 \mathcal C_{\rm let}\geq
 \Delta_s-(n-W_{3s})+Z
\]

and

\[
 \mathcal C_\partial\geq
 2\delta_0W_{3s}-2(n-W_{3s}).
\]

No overcounting, translation error, zero-projection error, or hidden
box-contained-witness assumption was found.

There is one required scope qualification in the introductory prose.  The
unqualified sentence

\[
 \text{``cross-box sharing capacity }=\Omega(W(3s))\text{''}
\]

is true for a near-width word, in particular for
\(n=W_{3s}+o(W_{3s})\), but not for an arbitrary very long universal word.
The displayed theorems themselves contain the correct dependence on
\(n-W_{3s}\), and all later architectural conclusions impose the near-width
hypothesis.  Thus this is a wording/scope correction rather than a defect in
the proof.

## 2. Product boxes, translations, and width accounting

For a block SCD chain of height \(p\), its bottom has rank
\((s-p)/2\).  Therefore a point of local rank \(x+y+z\) in a product box
has global rank

\[
 \frac{3s-(p+q+r)}2+x+y+z.
\]

At local middle rank \((p+q+r)/2\), this is exactly \(3s/2\).  Since the
product of three chains is rank-symmetric and rank-unimodal, its width is its
middle coefficient.  Every product box therefore contributes exactly
\(w(p,q,r)\) points to the global middle layer.  The product boxes partition
that layer, proving

\[
 \sum_{\mathcal B}w(\mathcal B)=W_{3s}.
\]

This also confirms that translated chain bottoms introduce no extra rank
term overlooked in (1.3).

The number of chains in an SCD of \(B_s\) is exactly \(W_s\), since every
chain meets the central layer once.  Hence the number of product boxes is
exactly \(W_s^3\), as used later.

## 3. Join-homomorphic projection and deletion of zero images

Fix one factor chain

\[
 C_t=C_0\cup\{e_1,\ldots,e_t\}.
\]

The projected coordinate

\[
 h(A)=\max(\{t:e_t\in A\}\cup\{0\})
\]

satisfies

\[
 h(A\cup A')=\max(h(A),h(A')).
\]

Taking the three coordinates gives the exact join homomorphism (2.2).  It is
irrelevant that an arbitrary letter need not itself contain a prefix of the
increment list: range-maximum words allow every grid point, and the maximum
index is the correct closure coordinate.

For the embedded target

\[
 T=C^{(1)}_x\cup C^{(2)}_y\cup C^{(3)}_z,
\]

the projection is exactly \((x,y,z)\).  Chain-bottom coordinates and
coordinates above the chain top are correctly ignored.  If a global interval
has union \(T\), every letter in it is a subset of \(T\), because Boolean OR
has no cancellation; nevertheless the proof only needs join preservation.

After projecting the whole global word, delete all zero images.  The images
originating in a fixed physical interval form a consecutive block in the
compressed word: deletion can remove positions inside the block but cannot
insert a position from outside it.  If the target point is nonzero, at least
one retained image remains, and its range maximum is unchanged.  Thus Lemma
2.1 is valid under the nonempty-letter convention.

The local abstract origin is deliberately not required by \(g_3\).  This is
compatible with a translated box whose embedded origin is a nonempty Boolean
mask: the projection ledger only needs nonzero abstract points.  The later
endpoint ledger separately selects the embedded local-middle targets, which
are nonempty.

For a fixed box, the number of retained projected letters is exactly

\[
 \#\{j:\pi_{\mathcal B}(A_j)\neq0\}.
\]

It is at least \(g_3(\mathcal B)\).  Summing and reversing the finite double
sum proves (2.4) with no multiplicity ambiguity.  A physical letter is
supposed to be counted once for every box in which it is active; this is the
sharing resource measured by the theorem, not overcounting.

## 4. Endpoint partitions and seam crossing

Choose one physical interval for every selected target in one dominant box.
Targets with a common left endpoint are nested, because increasing the right
endpoint only enlarges an OR.  Targets with a common right endpoint are
nested for the analogous reason.  Since the product-box embedding reflects
inclusion, these are chains in the local grid.

The two partitions are orthogonal.  If a left-endpoint class and a
right-endpoint class shared two distinct targets, those targets would have
the same physical left and right endpoints.  They would therefore be unions
of the same interval and hence equal, a contradiction.

Now put \(H=r-p-q\).  In each plateau layer there are \(w=(p+1)(q+1)\)
targets.  If one endpoint partition has \(C=w+\delta\) chains, the sets of
chains occupied in two consecutive layers each have size \(w\), so at least
\(w-\delta\) chains occur in both.  Such a common chain supplies a genuine
grid cover, because its two comparable points differ in rank by one.  Across
the \(H\) consecutive layer pairs, there are at least

\[
 H(w-\delta)
\]

used covers.

For \(\phi(x,y,z)=x+y\), the bottom and top plateau layers have the same
\(\phi\)-multiset: both contain one point for every pair \((x,y)\).  Exactly
\(w\) partition chains begin at the bottom and exactly \(w\) end at the top;
the remaining \(\delta\) starts and \(\delta\) ends are internal.  On
telescoping \(\phi\) along all partition chains, the boundary sums cancel and
the internal contribution is at most \((p+q)\delta\).  Every counted
horizontal cover increases \(\phi\) by one, while skipped ranks only add
nonnegative \(\phi\)-increase.  Hence at least

\[
 H(w-\delta)-(p+q)\delta=Hw-r\delta
\]

of the used covers are vertical.

There are exactly \(wH\) vertical covers in the slab.  A vertical cover
cannot be used by both endpoint partitions, by their orthogonality.  Applying
the preceding lower bound to both partitions gives (3.3).

Nothing in this argument refers to letters outside the chosen interval or
requires the interval to lie in a boxwise subword.  Foreign letters and
arbitrary seam crossings are already included.  Translation by chain bottoms
also causes no change: all targets stay inside one order-embedded product
box.

## 5. Height distribution and positive aggregate mass

The number of SCD chains of height \(h\), where \(h\equiv s\pmod2\), is

\[
 a_s(h)=\binom{s}{(s-h)/2}-\binom{s}{(s-h)/2-1}.
\]

This count is forced in every SCD by the rank sizes.  Uniformly for
\(h=u\sqrt s\) in a fixed positive compact interval,

\[
 \frac{a_s(h)}{W_s}
 =\frac{2u}{\sqrt s}e^{-u^2/2}+o(s^{-1/2}).
\]

Because admissible heights are spaced by two, the sum over
\([a\sqrt s,b\sqrt s]\) tends to

\[
 \int_a^b u e^{-u^2/2}\,du
 =e^{-a^2/2}-e^{-b^2/2}>0.
\]

Thus the two low windows and one high window used in the source contain
fixed positive fractions \(\kappa_L,\kappa_L,\kappa_H\) of the factor chains.
There are therefore

\[
 (\kappa_L^2\kappa_H+o(1))W_s^3
\]

dominant boxes, with no box counted twice.

For each such box, \(p,q\in[\sqrt s,1.1\sqrt s]\) and
\(r\in[3\sqrt s,3.1\sqrt s]\), up to parity rounding.  Hence, eventually,

\[
 H\ge0.7\sqrt s,\qquad H/r\ge1/5,
 \qquad w\ge s.
\]

Lemma 3.1, applied to a standalone local word, also gives

\[
 g_3-w\ge \frac{wH}{2r}\ge\frac w{10}.
\]

Finally,

\[
 \frac{sW_s^3}{W_{3s}}\longrightarrow\frac{2\sqrt3}{\pi}.
\]

The dominant boxes alone consequently contribute a fixed positive multiple
of \(W_{3s}\).  Every nonzero-height SCD box has \(g_3\ge w\), because its
local middle antichain is nonzero and one endpoint supports at most one
member of that antichain.  The only negative terms are the all-zero abstract
boxes.  Their number is

\[
 \left(\frac{W_s}{s/2+1}\right)^3=o(W_{3s}),
\]

so they do not affect positivity.  The conservative choice (4.12) is indeed
small enough for both (4.10) and (4.11), after increasing the threshold in
\(s\).

## 6. Global endpoint ledger

The product boxes partition the Boolean masks, but the same physical endpoint
may support witnesses for targets in several boxes.  This is exactly what
\(\ell_j\) and \(r_j\) measure.

For every box, the selected local-middle targets form an antichain of size
\(w_{\mathcal B}\); hence each of its endpoint partitions has at least that
many classes.  Dominant boxes gain the additional combined excess from Lemma
3.1.  Summing gives

\[
 \sum_{\mathcal B}(C_L(\mathcal B)+C_R(\mathcal B))
 \ge 2W_{3s}+2\delta_0W_{3s}.
\]

Each pair (physical endpoint, box) is counted exactly once on each relevant
side, regardless of how many targets of that box use the endpoint.  Therefore

\[
 \sum_{\mathcal B}C_L(\mathcal B)=\sum_j\ell_j,
 \qquad
 \sum_{\mathcal B}C_R(\mathcal B)=\sum_jr_j.
\]

For nonnegative integer incidences \(x_j\),

\[
 \sum_jx_j\le n+\sum_j(x_j-1)_+.
\]

This proves (5.3).  In particular, if \(n=W_{3s}+o(W_{3s})\), then

\[
 \mathcal C_\partial\ge(2\delta_0-o(1))W_{3s}=\Omega(W_{3s}).
\]

Similarly, (2.8) and (4.10) give

\[
 \mathcal C_{\rm let}\ge(\delta_0-o(1))W_{3s}+Z
 =\Omega(W_{3s})
\]

for a near-width word.  These are the precise versions of the introductory
sharing-capacity claim.

For a word much longer than width, (5.3) may have a negative right-hand side,
and no \(\Omega(W)\) endpoint-sharing conclusion follows.  For example, a
literal listing architecture can pay for targets with many separate
endpoints.  The source's displayed formulas correctly record this; only the
opening shorthand needs the near-width qualifier.

## 7. Sparse portal corollaries

If only \(P_s\) physical positions have endpoint degree at least two and both
endpoint degrees are at most \(D\), then

\[
 \mathcal C_\partial\le2(D-1)P_s.
\]

Substitution into (5.3) gives

\[
 n\ge(1+\delta_0)W_{3s}-(D-1)P_s.
\]

The letter version follows in the same way from
\(\mathcal C_{\rm let}\le(D-1)P_s\).  A corridor assignment of length
\(u_s\) to each box has at most \(u_sW_s^3\) distinct portal positions, even
before overlaps are removed.  Since

\[
 W_s^3=\Theta(W_{3s}/s),
\]

the hypothesis \(u_s=o(s)\) implies \(P_s=o(W_{3s})\).  Thus bounded-degree
\(O(\sqrt s)\)-length corridors cannot support a near-width construction.

This conclusion is architecture-specific and does not exclude high-degree
global positions.  The source correctly preserves that escape route.

## 8. Required correction and final status

Recommended wording correction in Section 0:

> For three equal blocks of even size \(s\), every universal word of length
> \(W_{3s}+o(W_{3s})\) has letter-sharing and endpoint-sharing capacity
> \(\Omega(W_{3s})\).

With that qualification, the note passes.  Its claimed no-go for sparse,
bounded-degree portal architectures and its surviving high-degree global
sharing target are rigorously supported.

## 9. Post-audit source recheck

The source was subsequently patched to say explicitly:

> For three equal blocks of even size \(s\), any global construction of
> near-width length \(n=W(3s)+o(W(3s))\) is forced by these ledgers to have
> cross-box sharing capacity \(\Omega(W(3s))\).

This is exactly the qualification required above.  It agrees with both
(2.8) and (5.3), and the following sparse-portal consequence retains the
same near-width hypothesis.  No neighboring statement reintroduces the
unqualified claim.

\[
 \boxed{\text{FINAL VERDICT: PASS.}}
\]
