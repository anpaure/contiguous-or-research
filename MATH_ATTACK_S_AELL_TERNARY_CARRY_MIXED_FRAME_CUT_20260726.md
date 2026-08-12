# Exact order-orbit insertion into ternary carry: recursive fusion and the dominant-frame Hall cut

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Audited outcome

Write

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q}.
\tag{0.1}
\]

Let \(t\) be the least power of two at least \(H\), put \(h=2t\), and
suppose

\[
 H\le t<2H,\qquad h=o(m),\qquad H\longrightarrow\infty.
\tag{0.2}
\]

The good middle owners in the phase-dense construction are partitioned
into canonical first-\(t\)-eligible-block macrocells

\[
 \mathcal M\cong\mathcal V^t,\qquad
 |\mathcal V|=24,\qquad |\mathcal M|=24^t.
\tag{0.3}
\]

For either sign, \(M_q^\pm\) denotes the number of literal rank-\((m\pm
q)\) targets absent from the corresponding depth-\(q\) consecutive
intersection/union image, after granting the final compiler its crossing
windows.

The proposed insertion has two meanings. They have different local
answers but the same global negative answer.

1. **The original Hamming carry remains false at logarithmic depth.**
   Even if its \(Q_h\)-cells use different exact order conjugates, its
   signed depth-\(q\) image in one macrocell is at most

   \[
    24^t\left(
       {h\over2^q}+{3q(1-3^{-t})\over4h}
    \right).
   \tag{0.4}
   \]

   At \(q_*=\lceil2\log _2h\rceil\), this is \(o(24^t)\).
   Both physical target layers consequently have \(W-o(W)\) holes.
   The certified literal equal-syndrome two-for-two order trade only
   doubles the first term and does not change this conclusion.

2. **The ternary carry is not intrinsically Hamming-specific.** A common
   rooted recursive \(C_{2h}\)-factor can be copied over the ternary row
   cells and fused by the same two-\(C_3\) odometer. The resulting exact
   factor has

   \[
      \text{cycle length}=2h\,3^t,\qquad
      \text{component count}={24^t\over2h\,3^t},
   \tag{0.5}
   \]

   and differs from its static reference on exactly

   \[
      E_{\mathcal M}
      ={3(1-3^{-t})\over4h}\,24^t
   \tag{0.6}
   \]

   outgoing tails. Aligning each physical eight-block with one bottom
   sibling pair of the recursion makes the carried cycles literally
   \(H\)-geodesic for \(H\le t\). Thus a common aligned recursive
   substitution is valid.

3. **The full \(A_h\)-orbit is not certified by the current collar.**
   At \(H=t\), the proved block-safe coordinate group is contained in

   \[
                         S_2\wr S_t,
   \tag{0.7}
   \]

   not \(A_h\). This subgroup has separate within-block and cross-block
   orbits already on two-sets. A full \(A_h\)-orbit requires a new
   same-eight-block two-edge collar. The final no-go below grants that
   collar, so this local gap is not used as the decisive obstruction.

4. **Even the maximally favourable recursive/\(A_h\) insertion fails
   physical signed coverage.** Every static all-new edge is a flip in
   one fixed global pair frame \(\mathcal P_1\). Order conjugation,
   recursive trace rainbowness, and the literal same-kernel packet trades
   only reorder \(\mathcal P_1\)-edges. The odometer creates exactly

   \[
      B_{\mathcal P_1}
       ={1-3^{-t}\over4t}\,G
       ={1-3^{-t}\over2h}\,G
   \tag{0.8}
   \]

   genuinely non-\(\mathcal P_1\) outgoing edges on the good owner mass
   \(G=W-o(W)\). If \(q=x\sqrt m+o(\sqrt m)\), then for each sign

   \[
    \boxed{
    M_q^\pm
       \ge D_{m,q}
          -{q(1-3^{-t})\over4t}G-o(W),}
   \tag{0.9}
   \]

   where

   \[
      D_{m,q}=\sum_f(T_{f,q}-V_f)_+
   \tag{0.10}
   \]

   is an explicit literal target-set Hall deficit, and

\[
    {D_{m,q}\over W}\longrightarrow
    \delta(x):=e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.
   \tag{0.11}
\]

Here \(\Phi\) is the standard normal distribution function.

   In the intended phase-dense regime \(t/\sqrt m\to\infty\),

   \[
     \boxed{M_q^-\ge(\delta(x)-o(1))W,\qquad
            M_q^+\ge(\delta(x)-o(1))W.}
   \tag{0.12}
   \]

Thus exact fibrewise direction balance, fibre-tagged affine injectivity,
ternary fusion, and even a hypothetical legal full \(A_h\)-orbit do not
yield physical signed-target coverage. A successful repair must create
\(\Omega_x(W/q)\) genuinely frame-escaping outgoing edges relative to
every fixed pair frame at a Gaussian depth. The present carry has only
\(O(W/h)=o(W/q)\).

## 1. Exact \(A_h\)-orbit counts are real but fibre-tagged

Let \(C\) be any exact factor on a labelled \(Q_h\)-fibre. For an oriented
sign \(\epsilon\), put

\[
 v_q^\epsilon(D;C)
 =\#\{x:D_{q,C}^\epsilon(x)=D\}.
\tag{1.1}
\]

For an \(H\)-geodesic factor and \(q\le H\),

\[
 \sum_{D\in\binom{[h]}q}v_q^\epsilon(D;C)=2^h.
\tag{1.2}
\]

### Theorem 1.1 (deterministic \(A_h\)-orbit resolution)

For \(h\ge4\), \(1\le q<h\), and \(D\in\binom{[h]}q\),

\[
 \boxed{
 \sum_{g\in A_h}v_q^\epsilon(D;gCg^{-1})
 ={ |A_h|\,2^h\over\binom hq}.}
\tag{1.3}
\]

#### Proof

Conjugacy gives

\[
 v_q^\epsilon(D;gCg^{-1})
 =v_q^\epsilon(g^{-1}D;C).
\tag{1.4}
\]

The alternating group is transitive on \(q\)-sets. An odd map between two
such sets can be parity-corrected by a transposition inside the target or
its complement; at least one has size at least two. Hence exactly
\(|A_h|/\binom hq\) elements send a fixed \(q\)-set to \(D\). Summing
(1.4) and using (1.2) proves the formula. \(\square\)

This is a deterministic orbit identity, not random averaging. Complete
orbits can also be packed integrally. Grouping the canonical macrocells
into blocks of \(|A_h|\) leaves fewer than \(|A_h|24^t\) owners. Since

\[
 \log(|A_h|24^t)=O(h\log h),
\tag{1.5}
\]

the leave is \(o(W)\) whenever \(h\log h=o(m)\).

It cannot be a local orbit of the \(6^t\) row cells:

\[
 {6^t\over|A_h|}
 ={2\,6^{h/2}\over h!}\longrightarrow0.
\tag{1.5a}
\]

Thus complete \(A_h\)-symmetry necessarily spans many physical
macrocells (or binary row packets), whose exterior tags are different.

The count is nevertheless an abstract-slot count. Each macrocell has a
physical embedding

\[
 \iota_{\mathcal M}:Q_h\hookrightarrow\binom{[2m]}m
\tag{1.6}
\]

recording its selected blocks, local row types, and frozen exterior.
Different embeddings attach different Boolean targets to the same
abstract direction.

There is an exact residual invariant even on a bare cube. Write an affine
trace as \((D,\eta)\), where

\[
 |D|=q,\qquad \eta\subseteq[h]\setminus D,\qquad|\eta|=r,
\tag{1.7}
\]

and let \(N_{q,r}^\epsilon(C)\) count base starts of outside weight \(r\).
The \(A_h\)-orbit load of each such trace is

\[
 \boxed{
 { |A_h|N_{q,r}^\epsilon(C)
  \over\binom hq\binom{h-q}r}.}
\tag{1.8}
\]

Indeed, \(A_h\) is transitive on disjoint pairs of prescribed sizes, and
the formula follows by double counting. Uniformity over every affine face
would require

\[
       N_{q,r}^\epsilon(C)=2^q\binom{h-q}r
       \qquad(0\le r\le h-q).
\tag{1.9}
\]

Physical row, exterior, eligibility, and pair-frame labels split these
orbits further. Fibre-tagged \(0/1\) incidence does not identify those
tags.

## 2. The original common-order carry fails at logarithmic depth

Put \(P=24^t=6^t2^h\). The static Hamming reference in one macrocell is
the disjoint union of \(6^t\) \(Q_h\)-cells. In each cell all cycles have
one doubled cyclic direction order. The support estimate below even grants
different conjugates in different cells; any legal carry using that
enlarged reference must still obey it if it retains the audited
changed-tail ledger.

### Lemma 2.1 (common-order physical support)

For either sign and \(1\le q<h\), the static signed image has size at most

\[
                         6^th2^{h-q}=Ph2^{-q}.
\tag{2.1}
\]

#### Proof

In one cell, a \(q\)-window uses one of \(h\) cyclic direction intervals.
For a fixed interval, at most \(2^{h-q}\) outside bit strings occur. The
physical intersection and union are functions of this affine face. Sum
over the cells. Different orders do not affect the bound. \(\square\)

### Lemma 2.2 (changed-edge support)

If successor permutations \(F,F_0\) differ on \(e\) outgoing tails, then

\[
 |\operatorname{im}T_{q,F}^\epsilon|
 \le|\operatorname{im}T_{q,F_0}^\epsilon|+qe.
\tag{2.2}
\]

#### Proof

A changed tail occurs in exactly one start at each of the \(q\) possible
lags. At most \(qe\) starts see a changed edge; every other window agrees
with its reference window. \(\square\)

The ternary carry has exact changed-tail count

\[
                      e={3(1-3^{-t})\over4h}P.
\tag{2.3}
\]

Lemmas 2.1 and 2.2 prove (0.4). At

\[
                      q_*=\lceil2\log_2h\rceil,
\tag{2.4}
\]

one has \(q_*\le H\) for all sufficiently large \(H\), because
\(h<4H\). The image fraction is at most

\[
 h2^{-q_*}+{3q_*(1-3^{-t})\over4h}
 \le h^{-1}+O(\log h/h)=o(1).
\tag{2.5}
\]

Also \(q_*=o(\sqrt m)\), and

\[
 {N_q\over W}=\prod_{j=0}^{q-1}{m-j\over m+j+1}
\tag{2.6}
\]

implies \(N_{q_*}=W-o(W)\). Summing over all macrocells and granting bad
or compiler-boundary starts distinct new targets gives

\[
                         M_{q_*}^-=W-o(W),\qquad
                         M_{q_*}^+=W-o(W).
\tag{2.7}
\]

A complete deterministic \(A_h\)-assignment does not change this support
cardinality.

### Literal two-for-two trade audit

Let \(K=\ker\phi\), let \(\tau=(a\ b)\) swap equal-syndrome coordinates,
and put \(\delta=e_a+e_b\in K\). The actual owner identity is

\[
 \mathbf1_{P+k}+\mathbf1_{P+k+\delta}
 =\mathbf1_{\tau P+k}+\mathbf1_{\tau P+k+\delta}.
\tag{2.8}
\]

Selecting one shore of each overlay component is a literal owner
partition. Copy the same packet-bit pattern over all ternary \(z\)-cells
in one binary class, root the resulting cycles, and apply the carry. Each
static cycle has one of the two orders \(\sigma,\tau\sigma\), so

\[
 |\operatorname{im}T_q^\epsilon|
 \le P\left(2h2^{-q}+{3q(1-3^{-t})\over4h}\right).
\tag{2.9}
\]

This remains \(o(P)\) at \(q_*\). Moreover

\[
                         \phi\tau=\phi
\tag{2.10}
\]

shows that all such trades preserve the syndrome-colour word and every
quotient-face total. They do not generate the full \(A_h\)-library.
Coherence in \(z\) is necessary: otherwise a carry edge lands in a cell
with a different successor, and the port layer is not a proved bijection.

## 3. A general ternary-carry lift over a recursive factor

At an adjacent local port, the six row labels split into two orbits of
the relative old/new matching. Label them

\[
                         (b_i,z_i)\in\mathbb Z_2\times\mathbb Z_3,
\tag{3.1}
\]

so the nontrivial matching sends \(z_i\mapsto z_i+1\).

### Theorem 3.1 (rooted-factor ternary odometer)

For every \(b\in\mathbb Z_2^t\), let \(F_b\) be an exact factor of
\(Q_h\) into rooted isometric \(C_{2h}\)'s. Copy \(F_b\) into every row
cell indexed by \(z\in\mathbb Z_3^t\). On each base cycle \(C\), choose
one directed edge supported in each physical block and list those ports
cyclically as

\[
                         i_1(C),\ldots,i_t(C).
\tag{3.2}
\]

At port \(i_s(C)\), use the nontrivial row matching precisely when the
already updated digits satisfy

\[
                         z_{i_1}=\cdots=z_{i_{s-1}}=0.
\tag{3.3}
\]

The resulting physical successor is a permutation of \(\mathcal V^t\).
Its component length and count are (0.5), and its changed-tail count is
(0.6).

#### Proof

Condition (3.3) excludes the active digit. Thus each six-row fibre uses
either the whole identity matching or the whole \(C_3\sqcup C_3\)
matching. Every phase layer is a bijection.

During one base-cycle lap, the successive rules perform ordinary
base-three ripple carry:

\[
                       z\longmapsto z+1
                       \quad\text{in }\mathbb Z/3^t\mathbb Z.
\tag{3.4}
\]

The binary vector \(b\) and base cycle \(C\) remain fixed. A component
therefore has length \(2h3^t\). There are \(2^h/(2h)\) base cycles for
each of \(2^t\) binary vectors, hence

\[
              2^t{2^h\over2h}={24^t\over2h3^t}
\tag{3.5}
\]

components. At port \(s\), (3.3) holds on \(3^{t-s+1}\) ternary states
per \((b,C)\). Thus

\[
 \begin{aligned}
  2^t{2^h\over2h}\sum_{s=1}^t3^{t-s+1}
  &={3(1-3^{-t})\over4h}24^t,
 \end{aligned}
\tag{3.6}
\]

which proves the changed-tail count. \(\square\)

No Hamming syndrome is used. It supplied a canonical root in the original
proof; copying a rooted factor supplies the same datum.

### Lemma 3.2 (recursive sibling separation)

In the recursive factor \(F_h\), group the \(h=2t\) coordinate leaves
into bottom sibling pairs. In every base-cycle direction permutation, the
two members of each pair occur at cyclic distance exactly \(t\).
Consequently every interval of at most \(t\) transitions uses each pair
at most once.

#### Proof

The assertion is immediate for \(h=2\). Passing from \(F_a\) to
\(F_{2a}\) interleaves the two parent direction words. A sibling
separation of \(a/2\) parent positions becomes a separation of \(a\)
child positions, equal to \((2a)/2\). Induction proves the claim.
\(\square\)

### Corollary 3.3 (literal \(H\)-geodesicity)

Identify bottom sibling pairs with the two active directions in the
\(t\) disjoint physical eight-blocks. The factor of Theorem 3.1 is
cyclically \(H\)-geodesic for \(H\le t\).

#### Proof

The carry changes row matchings but not projected \(Q_h\) directions. A
\(q\le H\) window uses \(q\) distinct blocks by Lemma 3.2. Its deletions
and insertions have disjoint physical supports, so its endpoints have
Johnson distance \(q\), and its intersection and union have ranks
\(m-q\) and \(m+q\). \(\square\)

For the static all-new shore, recursive trace maps are injective within
each cell, and local activity signatures separate distinct cells. Its
macrocell signed trace map is therefore injective through depth \(t\).
The reverse form of Lemma 2.2 gives

\[
 \boxed{
 |\operatorname{im}T_{q,\mathrm{car}}^\epsilon|
 \ge24^t-qE_{\mathcal M}.}
\tag{3.7}
\]

Thus the common-order logarithmic cut disappears. Equation (3.7) does
not prove exact carried injectivity; windows crossing ternary ports need
a separate decoder.

## 4. The current collar does not support the full \(A_h\)-orbit

### Proposition 4.1 (antipodal block rigidity)

At \(H=t\), the coordinate conjugacies certified by the disjoint-block
geodesicity proof lie in

\[
                         \Gamma_t=S_2\wr S_t.
\tag{4.1}
\]

The two \(\Gamma_t\)-orbits on two-sets are the sibling pairs and the
cross-block pairs. Every certified block-safe direction word has zero
consecutive load on the first orbit.

#### Proof

In a cyclic permutation of \(2t\) positions, every direction has a unique
antipode. If two directions from one physical block are not antipodal,
one cyclic interval between them has length at most \(t-1\), so an
\(H=t\) window uses that block twice. Hence each physical block must be
one antipodal pair. Lemma 3.2 identifies these with the bottom siblings,
so a safe conjugacy stabilizes the partition. The two-set orbit statement
is immediate. \(\square\)

This does not prove every \(g\notin\Gamma_t\) impossible. It proves that
the present one-edge port theorem does not certify it. A window using two
directions from one block requires a new proof that the two deletions and
two insertions remain distinct across changing shores.

The literal trade (2.8) has the same limitation. At \(H=t\), a single
transposition preserves the block partition only when it swaps the two
directions of one block. The equal-syndrome theorem does not guarantee
such a pair. Even when it exists, it stays in \(\Gamma_t\).

The next theorem grants all missing collars and all \(A_h\) conjugates.
Thus Proposition 4.1 is not the final no-go.

## 5. The exact dominant-frame target cut

In one associator block, write

\[
 \mathcal P_0=ab\mid cd\mid uv\mid wx,\qquad
 \mathcal P_1=ac\mid bd\mid uv\mid wx.
\tag{5.1}
\]

Apply \(\mathcal P_1\) in every global eight-block and pair the bounded
leftovers arbitrarily. This is one fixed global matching. Every static
all-new transition is a \(\mathcal P_1\)-pair flip, independently of its
order conjugate.

### Lemma 5.1 (exact nonframe edge count)

Every carried component contains exactly \(3^t-1\) outgoing edges which
are not \(\mathcal P_1\)-pair flips. Their total number on the good owner
set is (0.8).

#### Proof

At digit \(s\), the carry triggers on \(3^{t-s+1}\) odometer states. In
each relative \(C_3\)-orbit, two active-digit values are old main rows,
using \(ab\) or \(cd\), and one is an old reservoir row, using \(uv\) or
\(wx\). Exactly the first two leave \(\mathcal P_1\). Digit \(s\)
therefore contributes \(2\,3^{t-s}\) nonframe edges per component, and

\[
                  \sum_{s=1}^t2\,3^{t-s}=3^t-1.
\tag{5.2}
\]

Divide by the component length \(4t3^t\) and multiply by \(G\).
\(\square\)

Fix any perfect matching \(\mathcal P\) of the \(2m\) coordinates. A
middle owner of type \(f\) has \(f\) full pairs, \(f\) empty pairs, and
\(m-2f\) split pairs. Its exact orbit size is

\[
 V_f={m!\over f!^2(m-2f)!}\,2^{m-2f}.
\tag{5.3}
\]

A lower rank-\((m-q)\) target of type \(f\) has \(f\) full,
\(f+q\) empty, and \(m-2f-q\) split pairs, so

\[
 T_{f,q}
 ={m!\over f!(f+q)!(m-2f-q)!}\,2^{m-2f-q}.
\tag{5.4}
\]

The upper orbit has the same size by complement symmetry. Call a
depth-\(q\) window \(\mathcal P\)-internal if its moves flip distinct
pairs of \(\mathcal P\), and let \(A_{\mathcal P,q}^\epsilon\) count
noninternal signed windows.

### Theorem 5.2 (literal window-level Hall cut)

For every exact owner factor and both signs,

\[
 \boxed{
 M_q^\epsilon\ge
 \left[D_{m,q}-A_{\mathcal P,q}^\epsilon\right]_+,\qquad
 D_{m,q}=\sum_f(T_{f,q}-V_f)_+.}
\tag{5.5}
\]

If a literal compilation contributes \(s_q\) extra depth-\(q\) starts and
\(u\) omitted owners are granted arbitrary new targets, the right side
decreases by at most \(s_q+u\).

#### Proof

An internal lower window from a type-\(f\) owner preserves its full pairs
and empties \(q\) split pairs. It reaches a type-\(f\) target. Since
owners are not repeated, internal starts cover at most
\(\min(V_f,T_{f,q})\) distinct targets in that orbit. Noninternal starts
cover at most \(A_{\mathcal P,q}^-\) more targets. Hence the total
covered lower targets are at most

\[
 \sum_f\min(V_f,T_{f,q})+A_{\mathcal P,q}^-
 =N_q-D_{m,q}+A_{\mathcal P,q}^-.
\tag{5.6}
\]

Subtract from \(N_q\). The upper proof exchanges full and empty pairs.
Each extra start adds at most one target. \(\square\)

This is a literal Hall cut: take the union of the actual target orbits
with \(T_{f,q}>V_f\). Its internal candidate capacity is the corresponding
sum of the \(V_f\)'s.

### Lemma 5.3 (Gaussian constant)

If \(q=x\sqrt m+o(\sqrt m)\), \(x>0\), then

\[
 {D_{m,q}\over W}\longrightarrow
 \delta(x)=e^{-x^2}\Phi(x/2)-\Phi(-3x/2)>0.
\tag{5.7}
\]

#### Proof

Choose a uniform rank-\((m-q)\) target and let \(F\) be its number of
full pairs. Its exact factorial moments are

\[
 \mathbb E(F)_j
 =(m)_j{(m-q)_{2j}\over(2m)_{2j}}
 \qquad(j\ge1\text{ fixed}).
\tag{5.8}
\]

Expanding (5.8) for \(q=x\sqrt m+o(\sqrt m)\) gives

\[
 \mathbb EF={m\over4}-{q\over2}+O(1),\qquad
 \operatorname {Var}F={m\over16}+O(\sqrt m).
\tag{5.9}
\]

The same factorial-moment expansion shows that the joint cumulant of
\(j\) distinct pair indicators is \(O(m^{-(j-1)})\); after summing over
coincidence patterns, every fixed cumulant of \(F\) of order \(j\ge3\)
is \(O(m)\). After normalization by \((\sqrt m/4)^j\), it vanishes. The
cumulant criterion therefore gives

\[
 {4\over\sqrt m}\left(F-{m\over4}+{q\over2}\right)
 \Longrightarrow Z\sim N(0,1).
\tag{5.10}
\]

The exact source/target likelihood ratio is

\[
 \lambda_{f,q}={V_f\over T_{f,q}}
 ={2^q\binom{f+q}q\over\binom{m-2f}q}.
\tag{5.11}
\]

Taylor expansion on the central range gives

\[
                     \log\lambda_{f,q}
                     =-x^2+2xZ+o(1).
\tag{5.12}
\]

Since \(0\le(1-\lambda_{f,q})_+\le1\), convergence in distribution and
the usual truncation argument yield

\[
 {D_{m,q}\over N_q}
 \longrightarrow
 \mathbb E(1-e^{-x^2+2xZ})_+.
\tag{5.13}
\]

The limiting variable is below one exactly when \(Z<x/2\), and

\[
 \mathbb E[e^{2xZ}\mathbf1_{Z<x/2}]
 =e^{2x^2}\Phi(-3x/2).
\tag{5.13a}
\]

Therefore (5.13) equals
\(\Phi(x/2)-e^{x^2}\Phi(-3x/2)\). Finally
\(N_q/W\to e^{-x^2}\), proving (5.7). Positivity follows because the
lognormal variable is nonconstant and has positive mass below one.
\(\square\)

### Theorem 5.4 (maximally granted \(A_h\)-carry no-go)

Grant simultaneously:

* recursive trace-rainbow factors in every static fibre;
* a complete deterministic \(A_h\)-orbit with \(o(W)\) leave;
* a legal same-block collar for every conjugate;
* the exact ternary fusion of Theorem 3.1; and
* every coherent literal two-for-two order trade.

Then, for \(q=x\sqrt m+o(\sqrt m)\),

\[
 \boxed{
 M_q^\pm
 \ge D_{m,q}
   -{q(1-3^{-t})\over4t}G-u-s_q.}
\tag{5.14}
\]

If \(t/\sqrt m\to\infty\), \(u=o(W)\), and \(s_q=o(W)\), then (0.12)
holds.

#### Proof

All static order conjugates and packet trades use only
\(\mathcal P_1\)-pair flips. Lemma 5.1 gives
\(B_{\mathcal P_1}\) nonframe outgoing edges. One outgoing edge lies in
at most \(q\) forward windows and \(q\) reverse windows. Thus

\[
 A_{\mathcal P_1,q}^\pm
 \le qB_{\mathcal P_1}
 ={q(1-3^{-t})\over4t}G.
\tag{5.15}
\]

Apply Theorem 5.2 and Lemma 5.3. \(\square\)

The carried component count on the good mass is

\[
                         p={G\over2h3^t}.
\tag{5.16}
\]

Even granting \(2q\) new crossing starts per component boundary,

\[
                         s_q\le2qp
                         ={qG\over h3^t}=o(W).
\tag{5.17}
\]

Any \(W+o(W)\)-length literal completion has only \(o(W)\) further starts
at one fixed depth and cannot repair a \(\Theta(W)\) deficit.

## 6. The exact remaining mixed-frame cut

For a cyclically \(q\)-geodesic physical factor, if
\(B_{\mathcal P}\) outgoing edges leave a fixed frame, then every window
using only \(\mathcal P\)-edges uses distinct pairs. Hence

\[
 A_{\mathcal P,q}^\pm\le qB_{\mathcal P},
\qquad
 M_q^\pm\ge D_{m,q}-qB_{\mathcal P}.
\tag{6.1}
\]

At \(q=x\sqrt m+o(\sqrt m)\), \(o(W)\)-hole coverage therefore forces

\[
 \boxed{
 B_{\mathcal P}\ge(\delta(x)-o(1)){W\over q}.}
\tag{6.2}
\]

The present carry instead has

\[
 B_{\mathcal P_1}={1-3^{-t}\over4t}G,\qquad
 {B_{\mathcal P_1}\over W/q}\le{q\over4t}=o(1).
\tag{6.3}
\]

The component-choice Hall interface can be written with physical labels.
For a macrocell \(M\), let \(\mathcal C_M\) be its menu of legal complete
carried factors and put

\[
 S_{M,c,q}^\epsilon
 =\{T_{q,c}^\epsilon(x):x\in M\}.
\tag{6.4}
\]

A necessary fractional cut for unit coverage is, for every physical
target set \(Y\),

\[
 \boxed{
 |Y|\le
 \sum_M\max_{c\in\mathcal C_M}|Y\cap S_{M,c,q}^\epsilon|
 +u+s_q.}
\tag{6.5}
\]

Taking \(Y\) to be the deficient \(\mathcal P_1\)-type orbits violates
(6.5) by (5.14). Thus the remaining obstruction is an explicit pair-type
quotient cut, not an unknown generic Hall set.

To escape, the physical edge library must create
\(\Omega_x(W/q)\) edges outside every dominant frame. A ported
block-transposition trade spanning different frames could in principle do
this. An \(A_h\) direction permutation, affine phase change, same-kernel
equal-column trade, or denser ternary predicate on the same ports cannot:
all retain the static frame and only sparse carry edges leave it.

## 7. Odd-ground and floor-corrected form

In the literal odd setting, with \(\varepsilon\in\{0,1\}\),

\[
 \Omega=\{\infty\}\dot\cup P_1\dot\cup\cdots\dot\cup P_m,
 \qquad W=\binom{2m+1}{m},\qquad
 N_q=\binom{2m+1}{m-q},
\tag{7.1}
\]

the upper target layer is its complementary rank-\((m+1+q)\) layer.

the native source and target types \((\varepsilon,f)\) have exact counts

\[
 V_{\varepsilon,f}
 ={m!2^{m-\varepsilon-2f}
  \over f!(f+\varepsilon)!(m-\varepsilon-2f)!},
\tag{7.2}
\]

\[
 T_{\varepsilon,f,q}
 ={m!2^{m-q-\varepsilon-2f}
  \over f!(f+q+\varepsilon)!(m-q-\varepsilon-2f)!},
\tag{7.3}
\]

and

\[
 \lambda_{\varepsilon,f,q}
 ={V_{\varepsilon,f}\over T_{\varepsilon,f,q}}
 ={2^q\binom{f+q+\varepsilon}q
   \over\binom{m-\varepsilon-2f}q}.
\tag{7.4}
\]

Let \(c_q=\lfloor W/N_q\rfloor\), and define

\[
 E_{m,q}=\sum_{\varepsilon,f:\,m-\varepsilon-2f<q}
             V_{\varepsilon,f}.
\tag{7.5}
\]

The exact floor-corrected deficits are

\[
 D_q^-=
 \sum_{m-\varepsilon-2f\ge q}
       (c_qT_{\varepsilon,f,q}-V_{\varepsilon,f})_+,
\tag{7.6}
\]

\[
 D_q^+=E_{m,q}+
 \sum_{m-\varepsilon-2f\ge q}
       (V_{\varepsilon,f}-(c_q+1)T_{\varepsilon,f,q})_+.
\tag{7.7}
\]

If \(L_q\) starts are nonnative, every quota vector \(\beta_q\) with
coordinates in \(\{c_q,c_q+1\}\) satisfies

\[
 \boxed{
 {1\over2}\|\mu_q-\beta_q\|_1
 \ge\max(D_q^-,D_q^+)-L_q.}
\tag{7.8}
\]

At \(q=x\sqrt m+O(1)\), along a subsequence with \(c_q=c\), put

\[
 z_a={x^2+\log a\over2x}.
\tag{7.9}
\]

The likelihood-ratio limit gives

\[
 {D_q^-\over N_q}\longrightarrow
 c\Phi(z_c)-e^{x^2}\Phi(z_c-2x),
\tag{7.10}
\]

\[
 {D_q^+\over N_q}\longrightarrow
 e^{x^2}\Phi(2x-z_{c+1})-(c+1)\Phi(-z_{c+1}).
\tag{7.11}
\]

Their maximum is strictly positive. If \(e^{x^2}\) is integral, take the
minimum over the two adjacent possible subsequential floors; it is still
a positive constant \(\kappa_x\). Since the carry has
\(L_q\le qB_{\mathcal P_1}+u+s_q=o(W)\) whenever
\(t/\sqrt m\to\infty\) and \(u+s_q=o(W)\), the floor-corrected
discrepancy is \((\kappa_x-o(1))W\) in that phase-dense regime. Neither
parity nor the exact floor opens an escape.

## 8. Independent audit and precise scope

The decisive steps were rederived independently.

1. Equation (1.3) is a deterministic group-orbit identity.
2. Theorem 3.1 chooses a whole \(C_3\sqcup C_3\) matching. Since its
   predicate omits the active digit, every layer is a bijection and owner
   integrality is exact.
3. The changed-edge count (3.6) and the genuinely frame-changing count
   (5.2) differ by \(3/2\). Reservoir-row switches remain in
   \(\mathcal P_1\).
4. Lemma 3.2 is the physical-geodesicity input. Arbitrary \(A_h\)
   conjugacy is not claimed legal; Theorem 5.4 grants legality, so the
   final no-go does not depend on the missing collar.
5. Theorem 5.2 counts distinct literal targets. It is not histogram
   cancellation.
6. Local recursive injectivity can coexist with a global type deficit:
   it prevents collisions inside a macrocell, not competition among
   physical macrocells for the same target types.
7. Compiler seams, bad owners, and every \(W+o(W)\) appendage contribute
   only \(o(W)\) starts at one fixed Gaussian depth.
8. The obstruction is architectural, not universal. It does not rule out
   a factor with positive-density frame-changing edges, genuinely
   cross-atlas physical trades, or a no-dominant-frame construction.

## 9. Final proved/conditional boundary

**Proved positive:** exact deterministic direction-orbit counts; exact
owner-one recursive ternary fusion; exact component and changed-edge
ledgers; literal \(H\)-geodesicity under sibling alignment; and the
recursive support lower bound (3.7).

**Proved negative:** the original common-order carry has \(W-o(W)\) holes
at logarithmic depth after exact order conjugates and the certified
two-for-two trades. The recursive upgrade still has a positive Gaussian
literal Hall deficit because its mixed-frame edge mass is \(o(W/q)\).
The odd floor-corrected quota discrepancy is also \(\Omega(W)\).

**Unproved but insufficient:** a same-block collar making every \(A_h\)
conjugate physical, and an exact decoder for carry-crossing recursive
shadows. Granting both leaves the dominant-frame cut.

**Smallest escape:** an integral owner-preserving physical trade library
producing at least \((\delta(x)-o(1))W/q\) edges outside every fixed pair
frame at each controlled Gaussian depth, together with a carried shadow
decoder and outer target Hall assignment. No theorem in the present
\(A_h\)/same-kernel/ternary-port package supplies this library.
