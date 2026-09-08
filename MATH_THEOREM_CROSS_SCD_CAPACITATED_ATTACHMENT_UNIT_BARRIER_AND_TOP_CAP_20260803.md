# Cross-SCD capacitated attachment, the exact-depth unit barrier, and a top-cap bridge

**Date:** 2026-08-03  
**Status:** unconditional attachment reduction, sharp linear obstruction to
whole-chunk attachment at depth \(d\), and an exact \(d+1\) attachment of
every sparse residual chunk to the top collar rank. No computation is used.
The lower \(a-1\) collar ranks remain unassigned.

## 0. Outcome

Use the parity-block residual chunks from
MATH_THEOREM_SPARSE_TOP_SCD_FLAG_ROUNDING_AND_SINGLE_SCD_BARRIER_20260803.md.
Thus
\[
 k=2r,\qquad
 a=\left\lceil\frac78\sqrt r\right\rceil,\qquad
 u=r-a-1,
\]
and every residual chunk is a literal inclusion flag of length at most
\(d=d(2r)\), with a top of one of the block ranks
\[
 u-2jd,\qquad u-1-2jd.
\]

This note proves three facts.

1. Once residual and collar flags are fixed, whole-chunk attachment is one
   ordinary bipartite matching with edge condition
   \[
   \max F\subseteq\min C,\qquad |F|+|C|\le D.
   \]
2. At the exact depth \(D=d\), the natural whole-chunk face has a linear
   capacity obstruction. The residual construction has at least
   \[
   \left(e^{-(7/8+\sqrt\pi)^2}-o(1)\right)W
   \]
   chunks of full length \(d\), while every exact collar chainization has
   only \(o(W)\) owners with zero collar load. Consequently
   \(\Omega(W)\) full chunks must be shortened or cross-spliced.
3. One extra flag position removes this particular obstruction completely
   at the top collar rank. Every residual chunk can be matched to a distinct
   containing rank-\((r-1)\) target and then to a distinct rank-\(r\)
   owner. Appending that target gives a literal flag of length at most
   \(d+1\).

Thus, on this residual-chunk face, the exact-\(B\) route needs linearly
many one-target residual splices; the \(B+1\) route has an exact
residual-plus-top-rank bridge. What remains for the additive theorem is to
insert ranks \(r-a,\ldots,r-2\) into the remaining capacities while
preserving bottom containment.

## 1. The exact attachment graph

Let \(\mathscr F\) be any family of pairwise target-disjoint residual flags,
and assume the collar targets lie in a disjoint higher rank band.
For \(F\in\mathscr F\), write
\[
 h(F)=|F|,\qquad S(F)=\max F.
\]

Let \(W\) collar slots be indexed by distinct rank-\(r\) owners. At slot
\(T\), let
\[
 C_T=(B_T=C_{T,1}\subset\cdots\subset C_{T,\ell_T}\subset T)
\]
be its collar flag. The flag may be empty; in that case put
\(\ell_T=0\) and use the unmarked anchor \(B_T=T\).

For a proposed total depth \(D\), form the bipartite graph
\(\Gamma_D\) between \(\mathscr F\) and the owner slots, with
\[
 F\sim T
 \quad\Longleftrightarrow\quad
 S(F)\subsetneq B_T
 \ \text{ and }\
 h(F)+\ell_T\le D.
\tag{1.1}
\]

### Theorem 1.1 (whole-chunk attachment equivalence)

All residual chunks can be attached, one per owner, below the fixed collar
flags if and only if
\[
 |N_{\Gamma_D}(X)|\ge|X|
 \qquad(X\subseteq\mathscr F).
\tag{1.2}
\]

Whenever (1.2) holds, every resulting owner row is one literal inclusion
flag of length at most \(D\).

### Proof

Hall's theorem makes (1.2) equivalent to a matching saturating
\(\mathscr F\). For a matched pair \(F,T\), condition (1.1) gives
\[
 F_1\subset\cdots\subset S(F)\subsetneq
 B_T\subset\cdots\subset C_{T,\ell_T}\subset T.
\]
This is one literal flag and has at most \(D\) marked targets. Different
matched slots have different
owners, and the target banks were already disjoint.

Conversely, any attachment which keeps each residual chunk whole assigns
it to one distinct owner slot satisfying exactly (1.1), hence gives the
Hall matching. \(\square\)

If containment is temporarily ignored and only the lengths are retained,
put
\[
 A_t=\#\{F:h(F)\ge t\},
 \qquad
 K_t=\#\{T:D-\ell_T\ge t\}.
\tag{1.3}
\]
The nested capacity graph has a saturating matching exactly when
\[
                         A_t\le K_t\qquad(1\le t\le D).
\tag{1.4}
\]
Thus (1.4) is a necessary majorization row for the literal graph
\(\Gamma_D\).

## 2. There are linearly many full residual chunks

Let \(B_{0,0}\) be the first parity block. Its top is \(u\), and its
smallest rank is
\[
 u-2(d-1)=r-a-2d+1.
\tag{2.1}
\]

### Lemma 2.1 (full-chunk supply)

Before boundary deletion, the residual construction has at least
\[
 A_d^{\rm raw}\ge
 \binom{2r}{\,r-a-2d+1\,}
\tag{2.2}
\]
chunks of length exactly \(d\). Consequently
\[
 \liminf_{r\to\infty}\frac{A_d^{\rm raw}}W
 \ge
 \gamma:=e^{-(7/8+\sqrt\pi)^2}>0.
\tag{2.3}
\]

If \(\beta_{\rm res}\) residual targets are subsequently deleted, at least
\[
                         A_d^{\rm raw}-\beta_{\rm res}
\tag{2.4}
\]
full chunks remain.

### Proof

A chain of the fixed SCD contains all \(d\) selected ranks of \(B_{0,0}\)
whenever its starting rank is at most the smallest rank (2.1). The number
of such chains is exactly the number of sets at that rank, namely the
binomial coefficient in (2.2).

Since
\[
 \frac a{\sqrt r}\longrightarrow\frac78,
 \qquad
 \frac{2d}{\sqrt r}\longrightarrow\sqrt\pi,
\]
the central-binomial local limit gives (2.3). Every deleted named target
belongs to only one residual chunk, so it can shorten at most one full
chunk. This proves (2.4). \(\square\)

The other parity block and later blocks only increase the full-chunk count;
one block already gives a positive-density obstruction.

## 3. Exact-depth whole-chunk attachment has linear deficiency

Let \(\mathcal B_{r-1}\) be the nonboundary rank-\((r-1)\) collar targets,
and put
\[
 n_{r-1}=|\mathcal B_{r-1}|
 =\binom{2r}{r-1}-b_{r-1}.
\tag{3.1}
\]

### Theorem 3.1 (unit-capacity barrier)

For any collar chainization covering all nonboundary collar targets on at
most \(W\) owners, at most
\[
 W-n_{r-1}
 =\frac{W}{r+1}+b_{r-1}
\tag{3.2}
\]
owner slots have zero collar load.

Hence any depth-\(d\) attachment which keeps every residual chunk whole
leaves at least
\[
 \boxed{
 A_d^{\rm raw}-\beta_{\rm res}
 -\left(\frac{W}{r+1}+b_{r-1}\right)}
\tag{3.3}
\]
full residual chunks unattached.

For the optimal triangular boundary,
\[
 b_{r-1}+\beta_{\rm res}=O(r)=o(W),
\]
so (3.3) is \((\gamma-o(1))W\).

### Proof

One inclusion flag contains at most one rank-\((r-1)\) target. Therefore
the \(n_{r-1}\) distinct top-collar targets occupy at least \(n_{r-1}\)
different owner slots. At most \(W-n_{r-1}\) slots have empty collar flag,
which gives (3.2), using
\[
 \binom{2r}{r-1}=\frac r{r+1}W.
\]

A remaining length-\(d\) residual chunk can satisfy
\[
 d+\ell_T\le d
\]
only at a zero-collar slot. Apply the \(t=d\) row of (1.4), together with
Lemma 2.1, to obtain (3.3). The optimal boundary has at most
\(\binom{d+1}{2}=O(r)\) targets in total, proving the asymptotic statement.
\(\square\)

### Corollary 3.2 (minimal extra splice)

At exact depth \(d\), any construction starting from these residual chunks
must alter at least the quantity in (3.3) of the full chunks. If all
residual targets are retained, each altered full chunk must export at least
one target to another flag. Thus \(\Omega(W)\) one-target cross-chunk
splices are necessary on this face.

Equivalently, one additional unit of permitted flag depth is the smallest
uniform scalar relaxation which can attach a full residual chunk to a
singleton collar flag. It does not provide room for a longer collar flag.

The corollary counts modified chunks, not omitted targets. It does not rule
out a global exchange system which moves those exported targets into
spare positions elsewhere.

## 4. One extra position attaches every residual chunk to the top collar

Let \(\mathscr F_{\rm res}\) be the complete residual chunk family before
or after arbitrary target deletion. First work before deletion. If
\(\mathcal S\) is the multiset of block-top ranks, put
\[
 \sigma_r=\sum_{s\in\mathcal S}p_s.
\tag{4.1}
\]
The sparse-top theorem proves \(\sigma_r<1\) for all sufficiently large
\(r\), and in fact \(\sigma_r\) converges to a constant strictly below
one. Since
\[
 p_{r-1}=\frac r{r+1}\longrightarrow1,
\]
we have
\[
                         \sigma_r<p_{r-1}
\tag{4.2}
\]
for all sufficiently large \(r\).

### Theorem 4.1 (exact top-cap matching)

For all sufficiently large \(r\), every residual chunk can be assigned to
a distinct rank-\((r-1)\) target \(B\) containing its top. All
rank-\((r-1)\) targets can then be assigned to distinct rank-\(r\) owners.
Consequently:

* every residual chunk extends by one top-collar target to a literal flag;
* every remaining rank-\((r-1)\) target is a singleton collar flag;
* every owner is used at most once; and
* every resulting flag has length at most \(d+1\).

Arbitrary named boundary targets may be deleted afterward. A deleted cap
may be remembered as a proof-only containment anchor; it is not a marked
target and consumes no flag capacity.

### Proof

For a block with top rank \(s\), its nonempty SCD chunks are canonically
indexed by the complete rank-\(s\) layer: every rank-\(s\) set is the top
of exactly one chunk. Join a chunk with top \(S\) to every
\(B\in\binom{[2r]}{r-1}\) containing \(S\).

Give every edge out of a rank-\(s\) top weight
\[
 \frac1{\binom{2r-s}{r-1-s}}.
\]
Every chunk sends one unit. A fixed rank-\((r-1)\) target receives from
that block total load
\[
 \frac{\binom{r-1}{s}}
      {\binom{2r-s}{r-1-s}}
 =\frac{\binom{2r}{s}}{\binom{2r}{r-1}}
 =\frac{p_s}{p_{r-1}}.
\]
Summing over all blocks gives load
\(\sigma_r/p_{r-1}<1\) by (4.2). Thus this is a fractional matching
saturating every residual chunk. Bipartite integrality gives an integral
matching.

Independently, the complete containment graph from rank \(r-1\) to rank
\(r\) has a matching saturating the rank-\((r-1)\) shore. For example,
send each rank-\((r-1)\) set uniformly to its \(r+1\) owners; every owner
receives load \(r/(r+1)<1\), and use bipartite integrality.

Compose the two matchings. A chunk ending at \(S\) is followed by its
distinct cap \(B\), and then by the distinct owner \(T\):
\[
                         F_1\subset\cdots\subset S\subset B\subset T.
\]
Its marked length is at most \(d+1\). Caps not used by residual chunks are
singleton flags at their matched owners. Deleting boundary targets
afterward preserves containment and only decreases marked loads.
\(\square\)

This theorem integrates the entire exact residual ideal with the top
collar rank **only**. It does not place, match, or reserve capacity for the
remaining collar ranks
\[
                         r-a,\ldots,r-2.
\]

## 5. Remaining collar attachment

After Theorem 4.1, the exact unresolved object is a chainization of ranks
\(r-a,\ldots,r-2\) into the remaining owner capacities such that each new
chain lies above the residual top already present at that owner and below
its rank-\((r-1)\) cap.

At depth \(d\), Theorem 3.1 proves that this cannot be achieved by keeping
the parity residual chunks whole. At depth \(d+1\), the immediate top-cap
obstruction disappears, but full chunks have no capacity below their cap.
All lower-collar targets must therefore be routed to shorter residual
chunks, singleton-cap owners, or owner slots without a cap.

The exact next theorem is the Hall condition (1.2) after the collar flags
are chosen jointly. Equivalently, one needs an integral cross-SCD splice
system which exports at least one target from each of the
\(\Omega(W)\) full residual chunks in the exact-depth route, or a
rank-interleaved lower-collar chainization on the \(d+1\) route.
