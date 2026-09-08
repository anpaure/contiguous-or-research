# Audit of the PBBS dynamic-frame literal-fusion fallback

Date: 2026-07-25

Pure mathematics only. No computation, finite search, solver, or external
input is used.

Audited file:
MATH_ATTACK_K_PBBS_DYNAMIC_FRAME_LITERAL_FUSION_GATE_20260725.md.

## Verdict

**Pass after material scope patches.**

The protected-class import, the chronological priority-cylinder toll, the
physical and quotient residence-band normalizations, and the quotient-block
count are correct. The cited zero-winding staircase identities are also
correct.

The initial report nevertheless needed five qualifications.

1. The sharp \(H-j\) toll applies only to a prescribed chronological
   refined lower prefix, not to an arbitrary saturated MTF state over the
   same middle owner.
2. The PBBS rank-excess \(E_H\) is a universal lower bound on the
   independent priority toll; elapsed residence does not generally
   determine the exact priority.
3. The \(o(H)\)-per-physical-interval target is a worst-case volume
   guarantee, not an unconditional necessity theorem about the still-open
   PBBS packing.
4. A per-block DFB theorem needs a global support-complete witness choice,
   a unique carrier assignment, read-only collars, and a promise that all
   such costs are included in the \(O(H)\) block charge. These conditions
   were added.
5. The staircase theorem applies only to zero-winding returns. A DFB which
   services every true short return must also handle positive-winding
   dynamic frames without assuming a staircase factorization.

The report has been patched accordingly and now calls DFB a sufficient
conditional fallback, not the exact or sole remaining theorem. \(RP_A\)
remains open.

## 1. Protected-sector import

The imported canonicality criterion is exact:

\[
 A_k=\varnothing\quad(0\le k<h),\qquad
 \operatorname{ht}(B_k)\le k\quad(0\le k<h).
\]

On this class,

\[
 d(D_j)=2|B_j|+1\quad(0\le j<h),
\]

whereas

\[
 \delta(D_j)=h+2\sum_{t<j}|B_t|
 \quad(0\le j\le h).
\]

The original display incorrectly put the \(d(D_j)\) formula through
\(j=h\), where \(B_h\) is undefined. This endpoint was patched. The
resulting identity

\[
 \delta(D_j)-\sum_{t<j}d(D_t)=h-j
\]

and the first return at gap \(2h+1\) are correct.

The size estimate

\[
 |\mathcal S_r|\le r4^r e^{-c r^{1/3}}
 =o(\operatorname{Cat}_r/r^K)
\]

absorbs every polynomial loss. Hence

\[
 {N(H^2+2H)|\mathcal S_r|\over W}
 =(H^2+2H){|\mathcal S_r|\over B}=o_A(1)
\]

for \(H=O_A(\sqrt r)\).

This is a negligible incremental literal charge in a complete all-return
cut-repair construction. It is not, by itself, a standalone erosion word:
unprotected short runs may remain. The main report was narrowed at this
point.

## 2. Exact scope of the \(H-j\) MTF toll

The source priority-prefix theorem starts from a refined state

\[
 (B,\{x_{H-1}\},\ldots,\{x_0\},\mathcal R)
\]

and prescribes the next chronological deletion queue

\[
 (x_1,\ldots,x_j,a,x_{j+1},\ldots,x_{H-1}).
\]

The word

\[
 \{a\},\{x_{j+1}\},\ldots,\{x_{H-1}\},B
\]

has length \(H-j+1\), hence excess \(H-j\). Minimality is exact for this
prescribed prefix: after the last touch of \(a\), the \(H-j\) displayed
blocks which must finish above it require distinct later last-occurrence
times.

It is false as a distance claim to an arbitrary saturated state over the
same target owner. A different core/tail decomposition can be reached in
one update. The report now states this explicitly.

For the odd PBBS application, the projected owner rank is \(m=r+1\);
the MTF ordered-partition proof does not require an even ground set. Both
the owner and complementary sides contain at least \(H\) coordinates for
all sufficiently large \(r\). This normalization was added to Section 4.

If a coordinate has positive residence \(s+1\), then after its insertion
there are \(s\) intervening projected transition slots before its removal.
At most one coordinate contemporaneous with it can have its first departure
in each slot. Therefore its chronological priority satisfies

\[
 j\le s,
\]

and its independent portal excess is at least

\[
 (H-j)_+\ge(H-s)_+.
\]

Summing over gap multiplicities gives the valid lower bound

\[
 J_H\ge\sum_s(H-s)_+M_s=E_H.
\]

Equality need not hold because priority is the first-exit rank among
contemporaries, not elapsed residence length. Later arrivals do not
contribute to \(j\).

## 3. Staircase citation

For a zero-winding return with

\[
 L_j=\sum_{t<j}d_t,\qquad L_s=\delta_s,
\]

the cited theorem proves

\[
 \delta_j-L_j\ge s-j>0\quad(j<s)
\]

and

\[
 P_s1=(S_{s-1}1)(S_{s-2}1)\cdots(S_01),
\qquad \operatorname{ht}(S_j)\le j.
\]

The dual local factorization

\[
 S_j1P_j=P_{j+1}1\overline{T_j}
\]

with \(T_j\) Dyck is also quoted accurately. These are binary contour-word
identities, not a contiguous-OR realization.

Their quantifier is zero winding. A positive-winding return still has the
universal frame recursion

\[
 D_{j+1}=S_j1P_j0R_j,
\]

but the report may not apply the staircase product to it. The DFB fallback
was patched to take all exact dynamic frames as input and to use staircase
data only on the zero-winding subfamily.

## 4. Residence-band normalizations

For an edge-disjoint physical family with residence
\(\ell\in[H/2,H]\), every interval uses at least \(H/2\) projected edges.
The projected physical factor has \(W\) edges, so

\[
 |\mathcal P|\le {2W\over H}.
\]

An additive per-interval chart of cost \(\beta_H\) is therefore bounded by

\[
 O(\beta_HW/H).
\]

Thus \(\beta_H=o(H)\) guarantees \(o(W)\) uniformly from edge volume.
The weaker hypothesis \(\beta_H=o(H^2)\) alone does not. This becomes a
necessary per-interval scale only when the mechanism actually faces
\(\Theta(W/H)\) intervals; no such PBBS lower bound is claimed.

The quotient has \(B=W/N\) directed edges. An edge-disjoint quotient family
in the same band has at most \(2B/H\) traces. If all \(N\) spatial lifts of
one trace share a single \(O_A(H)\) chart, the bill is

\[
 O_A(H)\,{2B\over H}=O_A(B)=o(W).
\]

This calculation permits no later per-lift connector charge: all lifted
baseline owners must be reordered inside the existing \(W\) positions.

## 5. DFB block count, carriers, and implication

For a quotient cycle of length \(L\), the stated partition uses at most

\[
 {L\over H}+1
\]

blocks. Summing gives at most

\[
 {B\over H}+c_\tau,\qquad c_\tau\le B.
\]

If the complete chart cost is \(O_A(H)\) per block, then

\[
 O_A\!\left(H(B/H+c_\tau)\right)
=O_A(B+HB),
\]

and

\[
 {B+HB\over W}={1+H\over N}=O_A(r^{-1/2})=o(1).
\]

The arithmetic is exact. The initial DFB statement, however, did not say
who carries a crossing witness or whether collar and support-selection
costs were included. The patched conditional theorem now requires:

- one global support-complete family \(\mathscr W_H\) of correct lower and
  upper PBBS windows;
- assignment of each chosen witness and each short return to the unique
  block containing its first quotient edge;
- a read-only right collar of \(H\) quotient edges;
- unique home ownership of every baseline position; and
- inclusion of every carrier, collar, and boundary-composition toll in the
  stated \(O_A(H)\) block overhead.

Under these hypotheses, DFB is sufficient by definition: item 2 realizes
one witness for every central target, item 1 retains middle ownership, and
the block charts compose integrally. Without them, the displayed block
count alone would not prove a literal global word.

No existing theorem proves DFB, its \(O(H)\) chart, or the required global
owner assignment. It is a conditional global-fusion fallback while the
direct packing gate \(RP_A\) remains open; it is not the exact remaining
theorem and does not prove constant one.
