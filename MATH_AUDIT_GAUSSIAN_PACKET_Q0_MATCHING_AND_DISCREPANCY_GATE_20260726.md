# Gaussian packet design at the first annular rank: exact degrees and the two remaining gates

Date: 2026-07-26

> **Subsequent extension.**
> `MATH_THEOREM_CORRECTED_ANNULUS_INTERVAL_CODEGREES_MATCHING_AND_SHADOW_LEDGER_20260726.md`
> adds the exact distance-stratum link mass, internal packet-overlap
> parameter, consecutive higher-codegree hierarchy, a self-contained
> growing-rank isolated bite, and the owned-extension/floor-energy ledger
> for every deeper annular rank.  It confirms the near-factor is still an
> integral residual-regeneration gate and quantifies why Poisson-dispersed
> deeper loads leave \(\Theta(W\sqrt m)\) holes.

## 0. Verdict

Put

\[
 n=2m,\qquad q_0=\lceil a\sqrt m\rceil,\qquad r=m-q_0,
 \qquad N_r=\binom nr,
\]

where (a>0) is fixed.  The packets in
`MATH_THEOREM_GAUSSIAN_SHARED_PREFIX_PACKET_FRACTIONAL_BRAID_20260726.md`
are simply the (n) cyclic (m)-windows of an ordinary cyclic ordering
of ([n]).  At rank (r), the same packet consists of the (n) cyclic
(r)-intervals of that ordering.

The rank-(r) packet hypergraph is exactly regular and has very small
relative pair codegree:

\[
 D_r=\frac{r!(n-r)!}{2},\qquad
 \frac{\Delta _2}{D_r}
 =\frac{2}{r(n-r)}=(2+o(1))m^{-2}.
\]

Thus it satisfies the formal hypotheses of the fixed-uniformity
Frankl--Roedl--Pippenger theory more strongly than one could reasonably
ask.  This does **not**, by itself, prove an almost-perfect matching in
our diagonal regime: the hyperedges have size (n=2m=\Theta(\log N_r)),
whereas the standard theorem fixes the hyperedge size before taking the
degree limit.  No uniform quantitative version located in the audit
turns the displayed (O(m^{-2})) ratio into an (o(N_r)) leave.

Equivalently, the missing owner theorem is the following constant-density
partial Bailey--Stevens statement.

> For (r=m-\lceil a\sqrt m\rceil), pack all but (o(N_r)) edges of
> (K_{2m}^{(r)}) into edge-disjoint tight Hamilton cycles.

This is a sharply stated open gate, not an application of a currently
quoted black box.

Even that gate is not the full annulus theorem.  One must also make the
chosen packets nearly collision-free on the middle rank and nearly
covering at every deeper annular rank.  These are separate discrepancy
conditions; rank-(r) disjointness does not force them.

## 1. Packets are cyclic orders

With the notation of the shared-prefix note, the packet generated from

\[
 (u_1,v_1),\ldots,(u_m,v_m)
\]

is the cyclic-window family of

\[
 \pi=(u_1,u_2,\ldots,u_m,v_1,v_2,\ldots,v_m).
\]

Indeed, shifting the first (m)-window once deletes (u_1) and inserts
(v_1), and the subsequent shifts give exactly the states (Z_j).
Conversely every cyclic order has this form after cutting it immediately
before one of its (m)-windows.  Thus the unlabelled packet catalogue has

\[
 |\mathcal P|=\frac{(n-1)!}{2}
\]

members, cyclic orders being identified with their reversals.

For (1<r<n-1), a packet contains (n) distinct cyclic (r)-intervals.
Let \(\mathcal H_r\) be the (n)-uniform hypergraph with vertex set
\(\binom{[n]}r\) and packet set \(\mathcal P\).

## 2. Exact degree

### Proposition 2.1

Every rank-(r) target has degree

\[
 \boxed{D_r=\frac{r!(n-r)!}{2}.}
\]

### Proof

Double-count packet--target incidences.  There are ((n-1)!/2) packets,
each with (n) targets, and \(\binom nr\) targets.  Hence

\[
 D_r=\frac{n(n-1)!}{2\binom nr}
     =\frac{r!(n-r)!}{2}.\qedhere
\]

## 3. Exact pair codegree

Fix distinct (S,T\in\binom{[n]}r) and write

\[
 d=|S\setminus T|=|T\setminus S|.
\]

### Proposition 3.1

If (1\le d\le r-1), then

\[
 \boxed{
 D_r(S,T)=d!^2(r-d)!(n-r-d)!.
 }
\tag{3.1}
\]

If (d=r), so that (S,T) are disjoint, then

\[
 \boxed{
 D_r(S,T)=\frac{r!^2(n-2r+1)!}{2}.
 }
\tag{3.2}
\]

### Proof

For (d<r), all four Venn cells

\[
 S\setminus T,\quad S\cap T,\quad T\setminus S,
 \quad [n]\setminus(S\cup T)
\]

are nonempty.  Two equal short circular intervals with nonempty
intersection force these four cells to occur as four consecutive blocks,
in that order or its reversal.  After quotienting cyclic orders by
reversal, the number of orders is the product of the four internal
factorials, which is (3.1).

If (S,T) are disjoint, contract each to one block.  Together with the
(n-2r) remaining singleton objects there are (n-2r+2) circular
objects.  Ordering those circularly, ordering the two blocks internally,
and quotienting by reversal gives (3.2).  \(\square\)

For (d<r), division by Proposition 2.1 gives

\[
 \frac{D_r(S,T)}{D_r}
 =\frac{2}{\binom rd\binom{n-r}d}.
\tag{3.3}
\]

At (r=m-q_0), the disjoint-pair ratio is

\[
 \frac{(2q_0+1)}{\binom{m+q_0}{2q_0}},
\tag{3.4}
\]

which is exponentially smaller than (m^{-2}).  Log-concavity of
\(\binom rd\binom{n-r}d\), together with its endpoint values, shows that
for (q_0=\Theta(\sqrt m)) and large (m) the maximum in (3.3) occurs at
(d=1).  Therefore

\[
 \boxed{
 \Delta _2(\mathcal H_r)
 =\frac{2D_r}{r(n-r)},\qquad
 \frac{\Delta _2}{D_r}=(2+o(1))m^{-2}.
 }
\tag{3.5}
\]

## 4. What the matching theorem would say

Since

\[
 \frac{N_r}{W}
 =\frac{m!^2}{(m-q_0)!(m+q_0)!}
 =e^{-a^2+o(1)},
\]

an almost-perfect matching in \(\mathcal H_r\) would consist of

\[
 K=(1-o(1))\frac{N_r}{n}
   =(e^{-a^2}+o(1))\frac W{2m}
\]

packets.  It would be a constant-density partial tight-Hamilton
decomposition of (K_{2m}^{(r)}).

The classical Pippenger theorem states the desired conclusion for each
**fixed** packet size (n), assuming regularity and relative codegree
(o(1)).  Here (n=2m\to\infty).  Treating (3.5) as a direct application
silently interchanges the fixed-uniformity and (m\to\infty) quantifiers.
The quantitative results checked in the audit also fix the uniformity,
or yield an error exponent of order (1/n), which is ineffective when
(D_r/\Delta_2=\Theta(m^2)).

There is a useful exact calibration against the variable-rank result of
Grable.  Its near-perfect conclusion assumes, in the present notation,

\[
 \Delta_2=o\!\left(\frac{D_r}{n\log N_r}\right).
\]

Our packet design lies at the *constant* boundary rather than below it:

\[
 \frac{n\Delta_2\log N_r}{D_r}
 =\frac{(2m)\,2\log N_r}{(m-q_0)(m+q_0)}
 =8\log 2+o(1).
\tag{4.1}
\]

Likewise, the older Frankl--Roedl hypothesis
\(\Delta_2<D_r/(\log N_r)^a\) with (a>3) misses (3.5), whose scale is
\(D_r/(\log N_r)^2\).  Thus the failure of the black boxes is not just
an unknown degree threshold: the known growing-rank criterion is
quantitatively critical here.

Moreover the critical distance-one scale cannot be removed by taking a
regular subcatalogue.  In any subcatalogue in which a target (S) has
degree (D'(S)), every packet through (S) gives exactly two cyclic
neighbours of (S) at Johnson distance one.  Consequently

\[
 \sum_{T:\,|S\setminus T|=1}D'(S,T)=2D'(S).
\tag{4.2}
\]

There are (r(n-r)) such neighbours.  Thus every (D')-regular
subcatalogue has some distance-one pair of codegree at least

\[
 \frac{2D'}{r(n-r)}.
\tag{4.3}
\]

The factor causing (4.1) is therefore the intrinsic cyclic adjacency
skeleton, not an avoidable concentration in the complete catalogue.
Any improvement over the general growing-rank nibble must use that
skeleton rather than merely sparsify it.

### 4.1 The 2025 Gould--Kelly theorem does not diagonalize here

Theorem 1.4 of Gould--Kelly, arXiv:2511.11375, gives (in their notation)
a leftover

\[
 N_r B^{-1+\gamma}(\log D_r)^A
\]

under the hierarchy

\[
 1/D_r\ll1/A\ll\gamma\ll1/k,
\]

where the packet uniformity is (k+1=n=2m).  This is a
fixed-uniformity hierarchy; it cannot be read with (k=m) merely because
(D_r) is factorially large.  Indeed a diagonal reading would require

\[
 \gamma=o(1/m),\qquad A\gg1/\gamma\gg m.
\]

Even granting the optimal-looking full codegree parameter (B=cm), the
factor ((\log D_r)^A/B) is then enormous, not (o(1)).  More directly,
their proof explicitly uses an inequality of the form

\[
 B^{\gamma/3}\ge (\log D_r)^{\gamma A/6}
                 \ge16(\log D_r)^{6k}.
\]

For (B=\Theta(m)) and (gamma=o(1/m)), the left side tends to one,
whereas the final member is
\(\exp(\Theta(m\log\log m))\).  Thus this new theorem is also vacuous in
the present diagonal regime, independently of the unresolved exact
higher-codegree calculation.

### 4.2 One exact higher-codegree family

There is nevertheless a useful exact checkpoint on the full codegree
sequence.  Put

\[
 g=\gcd(n,r),\qquad L=n/g,
\]

and take the (L) rank-(r) intervals whose starts form one complete
orbit of the shift (x\mapsto x+r) on \(\mathbb Z_n\).  Their boundary
gaps are that same orbit and divide the coordinate circle into (L)
Venn atoms, each of size (g).  The complete interval family determines
the cyclic order of those atoms up to reversal, while the (g) labels
inside each atom may be permuted arbitrarily.  Hence its codegree is

\[
 \boxed{C_L=(g!)^L.}
\tag{4.4}
\]

Stirling's formula gives

\[
 \left(\frac{D_r}{C_L}\right)^{1/(L-1)}
 =\exp\!\left(g\log\frac{m}{g}+O(g)\right).
\tag{4.5}
\]

For (g=1) this is asymptotic, up to a constant factor, to (m/e);
for (g\ge2) it is much larger.  Thus complete boundary components do
not obstruct the conjectural all-codegree choice (B=cm).  Proving that
choice for every intermediate (j) still requires a uniform
circular-breakpoint/PC-tree enumeration; it is not supplied by the pair
calculation alone.

Accordingly, the rigorous status is:

\[
 \boxed{
 \text{fractional perfect matching: proved;\qquad
 integral }(1-o(1))\text{-matching: open in the growing-rank regime.}
 }
\]

## 5. Middle-rank collision is a second packing constraint

Let \(\mu_m^{\mathcal F}(X)\) count selected packets having (X) as a
cyclic (m)-interval, and define

\[
 C_m(\mathcal F)=\sum_{X\in\binom{[n]}m}
                 (\mu_m^{\mathcal F}(X)-1)_+.
\tag{5.1}
\]

The selected packets contribute (nK=(1-o(1))N_r) middle occurrences.
After appending every missing middle owner singly, their middle-layer cost
is exactly

\[
 W+C_m(\mathcal F)+o(W).
\tag{5.2}
\]

Thus coefficient one needs (C_m(\mathcal F)=o(W)); a rank-(r)
matching alone does not imply this.  The clean hard version is to match
packets simultaneously on

\[
 \binom{[n]}r\ \sqcup\
 \bigl(\binom{[n]}m/\{X,X^c\}\bigr),
\]

where a packet uses (n) vertices on the first shore and (m) antipodal
owner pairs on the second.

The uniform fractional point remains feasible.  With lower targets
saturated, its load on an individual middle owner is

\[
 \alpha_m=\frac{D_m}{D_r}
 =\frac{m!^2}{(m-q_0)!(m+q_0)!}
 =e^{-a^2+o(1)}<1.
\tag{5.3}
\]

The worst cross-rank codegree is also tiny.  If (S\subset X),
\(|S|=r,|X|=m\), then

\[
 D(S,X)=\frac{r!(q_0+1)!m!}{2},
\tag{5.4}
\]

so

\[
 \frac{D(S,X)}{D_r}
 =\frac{q_0+1}{\binom{m+q_0}{q_0}},\qquad
 \frac{D(S,X)}{D_m}
 =\frac{q_0+1}{\binom m{q_0}}.
\tag{5.5}
\]

These are superpolynomially small.  Hence no local degree or codegree
obstruction is visible; the issue is again integral rounding with growing
packet size.

## 6. The simultaneous deeper-shadow gate

For (q\ge q_0), put

\[
 \mu_q^{\mathcal F}(T)
 =\#\{P\in\mathcal F:T\text{ is a cyclic }(m-q)\text{-interval of }P\}
\]

and

\[
 H_q(\mathcal F)=\sum_{T\in\binom{[n]}{m-q}}
                  (1-\mu_q^{\mathcal F}(T))_+.
\tag{6.1}
\]

For a first-rank near-factor, the total occurrence mass at every deeper
rank is still

\[
 n|\mathcal F|=(1-o(1))N_r,
\]

and hence its mean deeper load is

\[
 \lambda_{q\mid q_0}
 =\frac{N_r}{N_q}.
\tag{6.2}
\]

The exact remaining annulus condition is

\[
 \boxed{
 C_m(\mathcal F)=o(W),\qquad
 \sum_{q=q_0}^{\lfloor b\sqrt m\rfloor}H_q(\mathcal F)=o(W).
 }
\tag{6.3}
\]

Complementation supplies the upper side automatically.

There is no automatic one-step propagation from the rank-(r) matching.
For (R\in\binom{[n]}{r-1}),

\[
 2\mu_{q_0+1}^{\mathcal F}(R)
 =\#\{x\notin R:
 R\cup\{x\}\text{ is owned and }x\text{ is an endpoint in its packet}\}.
\tag{6.4}
\]

Rank-(r) disjointness says that each extension (R\cup\{x\}) has at
most one owner; it gives no lower bound on the endpoint count in (6.4).
Thus the endpoint/discrepancy problem is genuinely additional.

More generally, let (s=q-q_0\ge1), and let
\(\operatorname{Ext}_s(R)\) count selected owned rank-(r) intervals
(S) for which (R\subset S) and (R) is one of the (s+1) aligned
length-((r-s)) subintervals of (S) in the same packet.  Every
occurrence of (R) lies in exactly (s+1) rank-(r) windows of its
packet, so

\[
 \boxed{
 \operatorname{Ext}_s(R)=(s+1)\mu_{q_0+s}^{\mathcal F}(R).
 }
\tag{6.5}
\]

The total extension supply is exactly

\[
 \sum_R\operatorname{Ext}_s(R)
 =(s+1)n|\mathcal F|=(1-o(1))(s+1)N_r.
\tag{6.6}
\]

Thus the deeper gate is a simultaneous grouped extension design: at
depth (s), almost every target must receive at least one entire packet
of (s+1) aligned extensions.  The rank-(r) matching controls uniqueness
of the extension (S), but not their distribution among the (R)'s.

## 7. Precise theorem that would close the fixed annulus

For each fixed (0<a<b), it is enough to prove:

> **Gaussian packet partial-design theorem.**  With
> (q_0=\lceil a\sqrt m\rceil), there is a family \(\mathcal F_m\) of
> cyclic orders of ([2m]) such that
> 
> 1. their rank-((m-q_0)) interval sets are pairwise disjoint;
> 2. \(|\mathcal F_m|=(1-o(1))N_{q_0}/(2m)\);
> 3. (C_m(\mathcal F_m)=o(W)); and
> 4. \(\sum_{q=q_0}^{\lfloor b\sqrt m\rfloor}H_q(\mathcal F_m)=o(W)\).

Items 1--2 are the growing-uniformity approximate tight-Hamilton design
gate.  Item 3 is the middle-resource gate.  Item 4 is the simultaneous
endpoint-discrepancy gate.  The exact orbit-average construction proves
the corresponding fractional load identities, but none of these three
integral conclusions follows merely from (3.5).
