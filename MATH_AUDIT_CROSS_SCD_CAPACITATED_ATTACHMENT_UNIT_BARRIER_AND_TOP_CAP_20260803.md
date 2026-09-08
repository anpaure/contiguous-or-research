# Independent audit: cross-SCD attachment, the unit barrier, and the top cap

**Date:** 2026-08-03  
**Audited theorem:**  
MATH_THEOREM_CROSS_SCD_CAPACITATED_ATTACHMENT_UNIT_BARRIER_AND_TOP_CAP_20260803.md  
**Audited theorem SHA256:**  
e3abe5f684f64f6c3eb89d17cdc4fe6e5d42a9e2103a56d44dfb97a64a26a2cd

**Verdict:** PASS. The exact attachment graph, the linear exact-depth
barrier, and the two-stage \(d+1\) matching to rank \(r-1\) are valid. The
positive bridge covers only the top collar rank \(r-1\); it does not place
the lower collar ranks \(r-a,\ldots,r-2\).

No computation or finite search is used.

## 1. Exact attachment graph

For a residual flag \(F\), write

\[
 h(F)=|F|,\qquad S(F)=\max F.
\]

At an owner slot \(T\), let the fixed collar flag have length
\(\ell_T\) and bottom \(B_T\). For an empty collar flag the convention
\(B_T=T\), \(\ell_T=0\), is correct.

Keeping the residual flag whole and placing it below this collar is
possible exactly when

\[
 S(F)\subsetneq B_T
 \quad\text{and}\quad
 h(F)+\ell_T\le D.
\tag{1.1}
\]

Necessity is immediate from inclusion and marked-length capacity.
Sufficiency follows because the concatenation

\[
 F_1\subset\cdots\subset S(F)
 \subsetneq B_T\subset\cdots\subset C_{T,\ell_T}\subset T
\tag{1.2}
\]

is one literal inclusion flag. Since distinct slots have distinct owners,
an injective attachment is precisely a matching saturating the residual
shore. Hall's condition in Theorem 1.1 is therefore necessary and
sufficient.

The assumption that residual and collar target banks are disjoint is
enough to prevent a target collision after concatenation.

## 2. Capacity-only majorization

If containment is suppressed, a residual item of height \(h\) can use a
slot of residual capacity \(c_T=D-\ell_T\) exactly when \(h\le c_T\).
This is a nested threshold graph.

Sorting residual heights and slot capacities decreasingly shows that it
has a saturating matching exactly when

\[
 A_t:=|\{F:h(F)\ge t\}|
 \le
 K_t:=|\{T:c_T\ge t\}|
 \qquad(1\le t\le D).
\tag{2.1}
\]

Equivalently, any Hall-minimal obstruction in this threshold graph is an
upper level set of the height order. Thus (1.4) is an exact criterion for
the capacity projection and a necessary condition for the literal graph.

## 3. Exact count of full residual chunks

The first even-parity block is

\[
 B_{0,0}=\{u,u-2,\ldots,u-2(d-1)\},
\]

whose minimum rank is

\[
 m=u-2(d-1)=r-a-2d+1.
\tag{3.1}
\]

A saturated symmetric chain contributes a length-\(d\) chunk for this
block exactly when its starting rank is at most \(m\). If

\[
 c_j=\binom{2r}j-\binom{2r}{j-1}
\]

is the number of chains starting at rank \(j\), the number of such chains
is

\[
 \sum_{j=0}^{m}c_j=\binom{2r}{m}.
\tag{3.2}
\]

This also follows by counting the unique rank-\(m\) member on each such
chain. Therefore

\[
 A_d^{\mathrm{raw}}\ge
 \binom{2r}{r-a-2d+1}.
\tag{3.3}
\]

The inequality rather than equality is correct because the other parity
block and later blocks may add further full chunks.

Each deleted residual target belongs to one chunk and can destroy the
full-length status of at most one chunk. Hence after
\(\beta_{\mathrm{res}}\) arbitrary residual deletions,

\[
 A_d^{\mathrm{remaining}}
 \ge A_d^{\mathrm{raw}}-\beta_{\mathrm{res}}.
\tag{3.4}
\]

## 4. The \(\gamma\) asymptotic

The deviation of the rank in (3.3) below the middle is

\[
 x_r=a+2d-1.
\tag{4.1}
\]

Using

\[
 {a\over\sqrt r}\longrightarrow {7\over8},
\qquad
 {d\over\sqrt r}\longrightarrow{\sqrt\pi\over2},
\]

gives

\[
 {x_r\over\sqrt r}
 \longrightarrow {7\over8}+\sqrt\pi.
\tag{4.2}
\]

The central-binomial local ratio yields

\[
 {\binom{2r}{r-x_r}\over W}
 \longrightarrow
 \exp\left[-\left({7\over8}+\sqrt\pi\right)^2\right]
 =:\gamma>0.
\tag{4.3}
\]

Thus the lower bound in Lemma 2.1 is
\((\gamma-o(1))W\). The shifts \(+1\) in the minimum rank and \(-1\) in
\(x_r\) vanish after normalization by \(\sqrt r\).

## 5. Zero-collar-slot bound

Let

\[
 n_{r-1}=\binom{2r}{r-1}-b_{r-1}
\]

be the number of nonboundary top-collar targets. An inclusion flag contains
at most one target at a fixed rank. Therefore covering these distinct
rank-\((r-1)\) targets requires at least \(n_{r-1}\) distinct nonempty
owner slots, regardless of how all lower collar ranks are chainized.

Among \(W\) owner slots, the number with zero collar load is consequently
at most

\[
 W-n_{r-1}
 =W-\left({r\over r+1}W-b_{r-1}\right)
 ={W\over r+1}+b_{r-1}.
\tag{5.1}
\]

Allowing a collar chainization to use fewer than \(W\) named owners does
not improve this bound: the unused owners can simply be regarded as empty
slots.

## 6. Exact-depth linear barrier

At total depth \(D=d\), a residual chunk of length \(d\) satisfies

\[
 d+\ell_T\le d
\]

only when \(\ell_T=0\). Hence the \(t=d\) threshold row can attach at most
the number of zero-collar slots in (5.1). Combining Sections 3 and 5 gives
at least

\[
 A_d^{\mathrm{raw}}-\beta_{\mathrm{res}}
 -\left({W\over r+1}+b_{r-1}\right)
\tag{6.1}
\]

unattached full residual chunks.

For the optimal triangular boundary,

\[
 b_{r-1}+\beta_{\mathrm{res}}=O(d^2)=O(r)=o(W),
\]

and \(W/(r+1)=o(W)\). Equation (4.3) therefore turns (6.1) into

\[
 (\gamma-o(1))W.
\tag{6.2}
\]

This is a barrier on the specified whole-chunk face. It is not a global
lower bound against every possible cross-SCD construction.

If every residual target is retained, altering one of these full chunks so
that it fits below a nonempty collar requires at least one of its old
targets to move to another flag. Thus linearly many modified chunks imply
linearly many one-target exports. A relaxation from \(d\) to \(d+1\)
allows a full chunk below a singleton collar target, but not below a longer
collar flag.

## 7. First stage of the top-cap bridge

Let \(\mathcal S\) be the collection of parity-block top ranks and

\[
 \sigma_r=\sum_{s\in\mathcal S}p_s.
\]

The sparse-top theorem proves that \(\sigma_r\) converges to a constant
strictly below one. Since

\[
 p_{r-1}={\binom{2r}{r-1}\over W}={r\over r+1}
 \longrightarrow1,
\]

we have \(\sigma_r<p_{r-1}\) for all sufficiently large \(r\).

For a chunk with rank-\(s\) top \(S\), join it to all rank-\((r-1)\)
sets \(B\supset S\). Its degree is

\[
 D'_s=\binom{2r-s}{r-1-s}.
\tag{7.1}
\]

Weight every such edge by \(1/D'_s\). Every chunk sends unit mass. A fixed
rank-\((r-1)\) cap \(B\) contains \(\binom{r-1}s\) rank-\(s\) tops from
that block, so the load contributed by the block is

\[
 {\binom{r-1}s\over\binom{2r-s}{r-1-s}}
 ={\binom{2r}s\over\binom{2r}{r-1}}
 ={p_s\over p_{r-1}}.
\tag{7.2}
\]

Summing over blocks gives cap load
\(\sigma_r/p_{r-1}<1\). The fractional matching saturates every chunk and
respects every cap capacity. It proves Hall directly, hence bipartite
integrality supplies an injective chunk-to-cap matching.

The proof is valid for the full residual family. Arbitrary residual
boundary deletions may be postponed until after this matching; deleting
members only shortens or removes the already assigned chunks.

## 8. Second stage: caps to owners

A rank-\((r-1)\) cap has exactly \(r+1\) rank-\(r\) supersets. Give every
cap--owner incidence weight \(1/(r+1)\). Each cap sends unit mass.

A rank-\(r\) owner contains exactly \(r\) rank-\((r-1)\) facets, so its
incoming load is

\[
 {r\over r+1}<1.
\tag{8.1}
\]

Again Hall and bipartite integrality give a matching saturating every
rank-\((r-1)\) cap. Composing it with the first matching gives

\[
 F_1\subset\cdots\subset S(F)\subset B\subset T.
\tag{8.2}
\]

Caps used in the first matching extend their residual chunks. Every other
cap is a singleton flag. Since all caps receive distinct owners, all final
flags receive distinct owners. Their lengths are at most \(d+1\).

Arbitrary top-cap boundary deletions can also be postponed. If a used cap
is deleted, it may be remembered only as a containment certificate between
the residual top and owner. It is not a marked target and consumes no
capacity. If an unused singleton cap is deleted, its empty flag and owner
can be released.

## 9. Exact scope of the positive result

The two-stage construction covers:

\[
 \text{all residual ranks }1,\ldots,r-a-1
 \quad+\quad
 \text{the single collar rank }r-1.
\tag{9.1}
\]

It does **not** cover, allocate, or reserve compatible owner capacity for

\[
 r-a,\ldots,r-2.
\tag{9.2}
\]

In particular, a full length-\(d\) residual chunk plus its cap already has
length \(d+1\); no lower-collar target can be inserted into that same flag
at depth \(d+1\). The positive bridge therefore is not a full-collar
attachment theorem and by itself proves neither \(B+1\) universality nor
the additive-\(O(1)\) conjecture.

The lower collar still requires a correlated chainization using shorter
residual chunks, unused owner slots, cap-only owners, and/or cross-SCD
splices.

## 10. Presentation and claim-scope repairs

The audited theorem was clarified in five places.

1. The outcome now says that the exact-\(B\) splice conclusion holds on
   this residual-chunk face.
2. The export conclusion explicitly assumes all residual targets are
   retained.
3. The one-unit scalar relaxation is stated for a singleton collar flag,
   not an arbitrary nonempty collar flag.
4. A deleted cap is proof-only and capacity-free, and Theorem 4.1 is
   explicitly labelled a top-rank-only result.
5. The zero-slot bound explicitly assumes an exact collar chainization
   covering every nonboundary collar target.

Within those scopes, every count and matching argument is exact.
