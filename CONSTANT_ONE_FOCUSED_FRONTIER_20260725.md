# Constant-one focused frontier

Date: 2026-07-25

This note records only statements which directly feed

\[
 \nu(k)\le(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

It is not a proof of that inequality.

## 1. The surviving physical core

For \(n=2m+1\), put

\[
 W=\binom nm,\qquad T=\binom n{m-1},\qquad
 H=\lceil A\sqrt m\rceil
\]

with fixed \(A\).

The first-avoided-pair token construction gives a lower-saturating,
middle-injective path core of mass \(T=W-O(W/m)\).  Its tight-row version
has

\[
 J=O(W\log^2m/m)=o(W/H).
\tag{1.1}
\]

The PBBS transition-factor version additionally has first-upper duplicate
and hole defect

\[
O(W\log m/m)=o(W).
\tag{1.2}
\]

The canonical PBBS turn factor now also has a complete second lower
shadow.  Every rank-\((m-2)\) target \(S\) occurs with multiplicity

\[
 1\le \mu_{P,2}(S)\le 10.
\tag{1.3}
\]

For all sufficiently large \(m\), its depth-two balanced floor is one.
Writing \(B=\operatorname{Cat}_m=W/(2m+1)\), the exact excess mass is

\[
 R_2=W-\binom{2m+1}{m-2}<12B,
\]

and consequently

\[
 O_2(P_m)<12B,
 \qquad
 \sum_S\binom{\mu_{P,2}(S)-1}{2}<48B.
\tag{1.4}
\]

More strongly, the PBBS correct-shadow support problem is now solved at
every depth.  If (g=f^2) is the canonical step-two PBBS permutation,
then for every (1\le q\le m) and every

\[
 S\in\binom{[2m+1]}{m-q}
\]

there is a canonically oriented path

\[
 A_0\longrightarrow A_1\longrightarrow\cdots\longrightarrow A_q
\]

such that

\[
 \bigcap_{t=0}^q A_t=S.
\tag{1.5}
\]

The proof cuts the expanded forward/reverse unmatched-mark circle after a
global maximum of its zero-sum gap potential.  The resulting simultaneous
forward and backward corridor inequalities make exact clean-label induction
work at every one of the (q) rank-\((m-1)\) overlap cores.  Shared marks do
not collapse a state.  Moreover

\[
 1\le \mu_{P,q}^{\rm corr}(S)\le\binom{2q+1}{q}.
\tag{1.6}
\]

Complementation gives complete upper support.  This is a support theorem:
for (q\ge3), other PBBS windows can still have the wrong rank because of
short coordinate returns.

Conditional on the isolated PBBS residence transversal

\[
 \rho_H=o\!\left(\frac{\binom{2m-1}{m-1}}
                         {H\log m}\right),
\tag{1.7}
\]

the PBBS seed is a genuine radius-\(H\) literal core with \(J=o(W/H)\).
Recursively conjugate PBBS phases remain compatible with the interval
descent below, and every interval corner preserves or improves (1.2).

## 2. Long interval descent

For every disjoint layer of adjacent priority pairs, maximal physical
carrier intervals may be switched independently.  Every corner remains
lower-saturating and middle-injective, the total new boundary count is

\[
 O(W\log^2m/m)=o(W/H),
\tag{2.1}
\]

and the exact doubled factorial-floor drift equals minus the activated
cross-packet duplicate charge.  In tight cyclic rows the entire first-upper
layer is pointwise flat; in the PBBS transition version its first-upper
orbit loads remain between the two permuted coherent endpoints and hence
cannot worsen.

The interval layer is therefore a cheap bulk mechanism, but it sees only
its adjacent-visible collision sector.

## 3. Owner-fixed spike charts

The local owner obstruction is now removed for both signs.

### Upper spike

Suppose \(t\) occurrences in one source phase share an upper depth-\(q\)
target \(U\), where \(q\ge1\).  For occurrence \(i\), let \(b_i\) be the
coordinate entering its upper flag at depth \(q\), and choose a helper
\(z_i\notin U_H(e_i)\cup A\).  Exchanging the omitted pair \(A\) with
\(\{b_i,z_i\}\) fixes the lower--owner incidence \((S_i,Y_i)\)
pointwise, fixes all lower flags and
all upper flags before \(q\), and gives

\[
 \left\|\sum_i d_i\right\|_w^2-sum_i\|d_i\|_w^2
 \ge w_q^+t(t-1).
\tag{3.1}
\]

### Lower spike

Suppose \(t\) occurrences share a lower depth-\(q\) target \(L\), where
\(q\ge2\).  Let \(b_i\) be the coordinate deleted on entry to \(L\),
choose \(a_i\in L\), and transpose \(a_i,b_i\).  This fixes the central
incidence and every upper flag and gives

\[
 \left\|\sum_i d_i^-\right\|_w^2-sum_i\|d_i^-\|_w^2
 \ge w_q^-t(t-1).
\tag{3.2}
\]

Both charts are exact integral Haar cubes.  Their conservative run toll is
at most \(2t\), so the certified curvature per new run is at least

\[
\frac12w_q^\pm(t-1).
\tag{3.3}
\]

More globally, inside one source phase and one signed depth, let
\(C_{\ge K}\) be the number of colliding occurrence pairs lying in fibres
of load at least \(K\).  The spike cubes tensorize and satisfy

\[
 \boxed{
 \mathfrak A-\mathfrak V\ge2w_q^\pm C_{\ge K},
 \qquad
 \Delta J\le\frac{4C_{\ge K}}{K-1}.}
\tag{3.4}
\]

At the first upper shadow, choose a fixed coordinate of the omitted pair as
the image marker.  Distinct owners in one common target then give distinct
image targets.  If \(B_{\ge K}^{(1)}\) is the sum of their current image
loads, the exact doubled-floor law is

\[
 \mathbb E Q_1'=Q_1+B_{\ge K}^{(1)}-\frac32C_{\ge K}.
\tag{3.5}
\]

Thus the first-shadow spike has a current-relative, not merely
higher-endpoint, descent criterion.

Thus high-multiplicity spikes are cheap.  The owner packing and the need
for a separate lower-centred word are no longer local obstructions.

## 4. The exact remaining sector

The unresolved mass is the **diffuse bounded-multiplicity sector**:
linearly many collision fibres of load \(O(H)\), especially pairs of
occurrences whose missing collars are disjoint and hence invisible to one
common-partner interval chart.

Singleton spike contexts cannot solve that sector: touching \(R\) such
occurrences costs \(\Theta(R)\) new source-row pieces.  A fixed partner can
persist through only \(O(q)\) consecutive depth-\(q\) starts, so a direct
owner-fixed packet catalog touching \(R\) roots needs \(\Omega(R/q)\)
packets.  At \(q\le H\), the required \(o(W/H)\) boundary budget therefore
cannot touch a linear number of diffuse roots.

There is no abstract packet-count obstruction.  In each source-phase/depth
stratum, collision fibres of loads \(2\le\mu\le K\), containing \(T\)
occurrences and \(C\) collision pairs, admit a balanced rainbow partition
into packets of size at most \(H\), one occurrence per fibre per packet.
The number of packets is at most

\[
 \frac{2C}{H}+(K+1)s,
\tag{4.1}
\]

where \(s\le mH\) is the number of nonempty strata.  Tying one spike bit
inside each upper packet loses none of the certified collision Gram.

The obstruction is exactly physical.  A fixed owner-preserving conjugacy
on one labelled row changes at most two depth-\(q\) entry markers.  Hence
constant-frame pieces satisfy

\[
 P\ge \frac{C}{K-1},
 \qquad
 T\le 2(P+R),
\tag{4.2}
\]

where \(P\) is the number of outer packets and \(R\) the number of
internal frame seams.  In particular diffuse load-two collisions force
\(R=\Omega(C)\); ordinary paid seams cannot implement (4.1).

The formerly proposed same-phase rotating-frame two-port seam is now
**ruled out**.  For requests in one source phase, consecutive switched
starts are separated by \(H+q\).  Thus a compiler serving \(p\) such
requests has literal length at least

\[
 1+(p-1)(H+q),
\]

so the claimed \(p+O(1)\) implementation is impossible.  This is an
ordering/age obstruction, not a defect that can be repaired by choosing
better common entrance and exit states.

Any surviving fusion theorem must therefore do something materially more
global: interleave requests from different source phases according to their
ages, construct age-compatible packets whose crossing windows do useful
work, or abandon the canonical packet compiler in favour of a direct OR
construction.  The exact capture and end-surcharge ledgers remain relevant,
but they are not by themselves a physical compiler.

This is now a fallback lane rather than the shortest route.  The complete
all-depth PBBS support theorem bypasses collision balancing if the PBBS
cycles can be literalized at Gaussian depth while preserving their correct
witnesses.

The theorem must use crossing windows at a positive density of seams.  A
separate exact capacity calculation rules out sparse fusion of large fixed
pair-status orientation cubes: at \(q=A\sqrt m\), packet-internal windows
miss a limiting positive fraction

\[
 \Delta(A)=\Phi(A/2)-e^{A^2}\Phi(-3A/2)>0.
\tag{4.3}
\]

Hence blocks of length \(\omega(H)\) with only sparse seams cannot prove
constant one.  Critical blocks must have length \(\Theta(H)\), almost all
seams must be fused, and the seam-crossing windows themselves must provide
macroscopic vertical coverage.

## 5. The two primary remaining PBBS gates

A proposed stronger pointwise inequality relating return gap to peak defect
is false.  There are roots of arbitrarily large peak defect with an exact
gap-seven omitted-label return.  The gap-seven roots are nevertheless
completely classified: their total number is only exponential base two,
and their maximum edge-disjoint residence packing is
\(\Theta((2m+1)2^m)=o(\operatorname{Cat}_m)\).  Fixed short gaps are
therefore harmless, but no pointwise vacancy/height estimate can prove the
Gaussian residence bound.  The surviving PBBS gate is aggregate quotient
clustering of growing return gaps.

Let \(B=\operatorname{Cat}_m\). For every fixed \(A>0\), put
\(H_A=\lceil A\sqrt m\rceil\). A linear dominance-staircase chart now
repairs every floor-correct lower intersection and every upper union crossing
one cut in exactly \(4H_A-1\) nonzero letters. Together with endpoint-capped
erosion this gives the sharpened central-band ledger

\[
 \boxed{
 W+2H_AB+2(5H_A-1)\nu_{H_A}(P_m).}
 \tag{5.1}
\]

Consequently the weakest direct packing theorem required by this ledger is

\[
 \boxed{\nu_{H_A}(P_m)=o_A(B\sqrt m).}
\tag{ST_A}
\]

No uniformity in \(A\) is required. Since \(H_A=O_A(\sqrt m)\) and
\(W=(2m+1)B\), the last term in (5.1) is then \(o_A(W)\), while
\(2H_AB=o_A(W)\). Diagonalizing through integer \(A\to\infty\) slowly and
adjoining the proved product-SCD tail gives the full constant-one bound.

Equivalently, after removing negligible short quotient cycles, the deck
reduction turns \((\mathrm{ST}_A)\) into

\[
 \overline\nu_{H_A}
 =o_A\!\left(\frac{B}{\sqrt m}\right).
 \tag{5.2}
\]

The height-gap theorem and the exact Dyck height spectrum already give

\[
 \overline\nu_{H_A}=O_A(B/\sqrt m).
 \tag{5.2a}
\]

Thus the coefficient-one gap is only a vanishing improvement over the
critical reciprocal-height capacity. The stronger Catalan-order condition

\[
 \nu_{H_A}(P_m)=O_A(B)
 \tag{CP_A}
\]

remains a useful sufficient theorem, but it is not the shortest gate.

There are now two further exact reductions of this packing problem.

First, every projected-edge-disjoint family of return intervals contains,
after splitting by one parity, a projected-edge-disjoint family of simple
returns of at least half its cardinality.  A simple return has pairwise
distinct omitted labels and is exactly a pair of fixed-core open-wreath
sectors joined by one core-swap square.  Thus internal repeated returns and
the former zero-winding/positive-winding distinction are not part of the
local packing obstruction: up to a factor two, all return packing may be
studied inside fixed-core open-wreath sectors.

Second, one dominance staircase can serve a whole cluster of cuts.  If the
cluster span is \(S\) and \(3H_A+S\le m+1\), the exact auxiliary cost is at
most

\[
 7H_A+3S-3.
 \tag{5.3}
\]

The negative endpoint-erosion prefixes can simultaneously be deleted, so
there is no residual \(H_AJ\) initialization term.  For cut clusters of
spans \(S_j\), put

\[
 \mathfrak S_{H_A}=\sum_j(7H_A+3S_j-3).
\]

The complete central-band ledger is then

\[
 \boxed{W+2H_AB+\mathfrak S_{H_A}.}
 \tag{5.4}
\]

Consequently the currently weakest sufficient PBBS statement is

\[
 \boxed{\mathfrak S_{H_A}=o_A(W).}
 \tag{CS_A}
\]

For deck-invariant choices its quotient form asks for clustered-span cost
\(o_A(B)\).  The direct packing-and-clustering argument currently gives
only \(O_A(B)\).

The apparent alternative between \((\mathrm{CS}_A)\) and
\((\mathrm{ST}_A)\) has now been removed.  Modulo the already proved
sub-Gaussian-height packing tail, they are equivalent at the
coefficient-one scale:

\[
 \boxed{
 \mathfrak S_{H_A}=o_A(B)
 \quad\Longleftrightarrow\quad
 H_A\overline\nu_{H_A}=o_A(B).}
 \tag{5.4a}
\]

The upper comparison uses a circular-interval transversal of size at most
\(2\overline\nu_H\).  For the converse, fix \(a>0\).  Every return whose
start height is at least \(a\sqrt m\) has trace length at least
\(\gamma_{a,A}H\).  If one cut cluster of span \(S\) receives cuts from
\(t\) pairwise edge-disjoint such traces, then the middle \(t-2\) traces
lie between the extreme cuts, so

\[
 S\ge\gamma_{a,A}H(t-2).
\]

Thus every cluster costs at least \(c_{a,A}Ht\), and summing over a
maximum packing gives

\[
 \mathfrak S_H\ge c_{a,A}H\overline\nu_H^{\ge a}.
\]

Letting \(a\downarrow0\) proves (5.4a).  The complete proof is in
`PBBS_ST_CS_EQUIVALENCE_20260726.md`.  Hence cross-cut sharing changes
constants but cannot rescue a genuinely critical
\(\Theta_A(B/\sqrt m)\) residence packing.  If \((\mathrm{ST}_A)\) is
false, this additive PBBS compiler requires an in-place baseline
replacement or a different architecture.  The stronger completion and
Catalan-order packing formulations remain available when useful.

The packing question itself now has an exact two-time form.  Let \(E_H\)
be the retained quotient roots which start an eligible residence, put

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=
 \sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|.
 \tag{5.4b}
\]

The conflict graph of the actual residence intervals has at most
\(\mathcal C_H\) edges.  Turan--Cauchy therefore gives the rigorous lower
bound

\[
 \boxed{
 \overline\nu_H\ge
 {R_H^2\over R_H+2\mathcal C_H}.}
 \tag{5.4c}
\]

Thus, at the numerically suggested critical one-point scale
\(R_H\asymp B/H\), bounded average short-lag clustering would refute
\((\mathrm{ST}_A)\); a positive proof requires
\(\mathcal C_H/R_H\to\infty\).  No current theorem decides this direction.

For zero-winding returns the two-time event has also been reduced to one
literal boundary-block equality.  With

\[
 c_i=d(\tau^iD),
 \qquad \widehat c_i=d(\phi\tau^iD),
\]

two height-\(h\) zero-return starts at positions \(i\) and \(i+t\) are
equivalent to one zero return together with

\[
 \boxed{
 \sum_{j=0}^{t-1}c_{i+j}
 =
 \sum_{j=0}^{t-1}\widehat c_{i+h+j}.}
 \tag{5.4d}
\]

The proof is the telescope

\[
 F_{i+t}^{(h)}-F_i^{(h)}
 =\sum_{j<t}\widehat c_{i+h+j}-\sum_{j<t}c_{i+j},
 \qquad
 F_i^{(h)}=\sum_{j<h}c_{i+j}-\delta(\tau^{i+h}D).
\]

Cyclewise bounded multiplicity is false: the exact one-defect mountain
rotor has clustering ratio of order \(h\).  It is not at Gaussian ambient
scale, so the aggregate correlation (5.4b) remains open.

Finally, all presently local in-place reuse has been audited.  Deleting
every erosion letter whose old witnesses are assumed by a cluster chart
gives credit at most \(\sum_JS_J\), and the remaining chart charge still
dominates the trace mass of every packed return family.  Even replacing a
whole cluster collar by its \(2M+1\)-letter dominance word leaves
\(\Omega_A(B)\) excess under critical saturation.  Hence a successful
replacement must be nonlocal: a rank-monotone braid which rethreads
positions across many clusters while preserving middle singletons and
both endpoint witness systems.  The exact no-go is in
`MATH_THEOREM_PBBS_BASELINE_REPLACEMENT_CREDIT_NO_GO_20260726.md`.

An attempted proof that \((\mathrm{RP}_A)\) is false has been retracted.
The proposed implication

\[
 d(D)=1\Longrightarrow
 \text{next return gap }2\operatorname{ht}(D)+1
\]

fails because a transported \(A_i\)-forest can become the new first deepest
branch under \(\tau\).  Explicit counterexamples are recorded in
PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md.  Hence the spectral
Catalan mass of primitive roots does not currently yield a residence lower
bound. The stronger \((\mathrm{RP}_A)\) remains open rather than refuted,
and the weaker sufficient gate \((\mathrm{ST}_A)\) is also open.

### 5.1 Strict progress inside the quotient gate

The critical (O_A(B/\sqrt m)) bound has now been improved to little-oh
on several complete sectors.  These are reductions of the actual gate
((5.2)), not stronger optional hypotheses.

For a genuine zero-winding return of duration (s\), let

\[
 \Lambda=\delta(D_0)+\delta(D_s)-2m=2\ell
\]

be its endpoint overlap.  Its forward and dual staircase arrays contain
the *same* balanced boundary word (E) of length (2\ell).  Record-minimum
parsing gives the pointwise critical boundary estimate (O(4^{-\ell}))
on each side.  Summing only over balanced common words, and retaining the
conditional coefficient anti-concentration of the untouched central
array, gives the audited bound

\[
 \boxed{
 z_{m,s,2\ell}
 \le C4^m\frac{(\ell+2)^2}
 {s^6\sqrt{\ell+1}}.}
 \tag{5.5}
\]

Consequently, if (L\log m=o(m^{1/5})), then all zero-winding starts
with

\[
 s\le A\sqrt m,\qquad 0<\Lambda\le2L
\]

have total cardinality

\[
 o_A(B/\sqrt m).
 \tag{5.6}
\]

For the edge-disjoint packing actually required by \((5.2)\), the
logarithm can be removed.  Split at height (a\sqrt m): the proved
sub-Gaussian height packing theorem makes the lower piece vanish after
(a\downarrow0), while (5.5) sums above that fixed cutoff.  Hence

\[
 \boxed{L=o(m^{1/5})\quad\Longrightarrow\quad
 \overline\nu_{H_A}^{0,\,0<\Lambda\le2L}
 =o_A(B/\sqrt m).}
 \tag{5.7}
\]

The case \(\Lambda=0\) already has the stronger (O_A(B/m)) quotient
bound.  Thus the entire zero-winding packing sector with

\[
 \Lambda=o(m^{1/5})
\]

is removed from the coefficient-one gate.  The common-boundary capped
relaxation has an intrinsic \(\ell^{3/2}\) residual, so extending (5.6)
requires additional PBBS chronology or packing, not merely remembering
that the two boundary words agree.

Peak deletion supplies one further unconditional large-overlap cut.  Let
\(p\) be the first-mountain pruning depth, put \(q=s-p\), and write
\(\lambda=\Lambda/2\).  In the unsaturated sector \(p<2q\), the common
boundary is confined to the strip \([-p,p]\).  Uniformly for every overlap
size,

\[
 z_{m,s,2\lambda,p}
 \le C4^m\frac{(\lambda+2)^2}{s^6}
 \min\!\left\{
 (\lambda+1)^{-1/2},
 e^{-c\lambda/(p+1)^2}
 \right\}.
 \tag{5.7a}
\]

Consequently, for a sufficiently large absolute \(K\), all starts with

\[
 p<2q,
 \qquad \lambda\ge K(p+1)^2\log m
\]

already contribute \(o_A(B/\sqrt m)\).  The complementary saturated-top
sector \(p\ge2q-O(1)\), \(q\ge\varepsilon\sqrt m\), is also proved
negligible.  Thus in the Gaussian-\(q\) lane a possible saturator is forced
into the intermediate strip

\[
 p<2q-O(1),
 \qquad \eta(m)m^{1/5}<\lambda
 <K(p+1)^2\log m,
 \tag{5.7b}
\]

for an arbitrarily slow \(\eta(m)\downarrow0\).  An explicit genuine family
shows that large overlap alone forces neither pruning saturation nor a
vanishing pointwise Pascal-fan factor, so the residual is genuinely
aggregate.

The complete unsaturated pruning-profile sum is now also exact.  With
\(b=2q-p+1\), \(Q_{j+1}=Q_j-zQ_{j-1}\), and
\(C_j=Q_j/Q_{j+1}\), the full Pascal-fan capacity envelope over every
convex inverse-fibre profile having first mountain depth \(p\) is

\[
 [z^{m-s}]\,\frac{C_p(z)^b}{Q_p(z)^3}
 \left[1-\left(1-\frac{z^p}{Q_p(z)^2}\right)^b\right].
 \tag{5.7c}
\]

The bracket is the exact \(y_p\ge1\) first-mountain correction.  A
two-pole tilted coefficient bound and exact summation give

\[
 \sum_{s\le A\sqrt m,\ p<2(s-p)}\mathcal E_{m;s,p}
 =O_A(4^m/m^2)=O_A(B/\sqrt m).
 \tag{5.7d}
\]

Moreover,

\[
 \lim_{\varepsilon\downarrow0}\limsup_{m\to\infty}
 \frac{m^2}{4^m}
 \sum_{s\le A\sqrt m,\ p\le\varepsilon\sqrt m}
 \mathcal E_{m;s,p}=0.
 \tag{5.7e}
\]

Thus every common lane \(p=o(\sqrt m)\) is negligible already at
start-count level, uniformly over all overlaps.  The only unsaturated
profile lane still capable of critical mass has
\(p\asymp q\asymp\sqrt m\).  The envelope itself has a matching
\(\Omega(4^m/m^2)\) lower bound along arbitrarily large \(m\), so profile
capacity alone cannot supply the strict little-oh; one must use genuine
PBBS realizability, a joint boundary--profile constraint, or descendant
edge packing.

One proposed genuine critical obstruction in that lane has now been
eliminated at the required **packing** scale.  In the explicit transported
corner family with parameters \((s,K,Y,t,u)\), every return interval
contains the quotient edge at the uniquely parseable root

\[
 C(s,K,Y)=1^s0^K Y0^s,
 \tag{5.7f}
\]

independent of \((t,u)\).  Hence an edge-disjoint family uses at most one
interval for each \((s,K,Y)\).  At fixed rank \(m=s+K+n\), the number of
possible strip words is at most \(2^{2m-2s-K}\), and therefore, for every
fixed \(0<\alpha<A\),

\[
 \Pi_m^{\rm corner}(\alpha,A)
 \le {2\over3}4^m4^{-\lceil\alpha\sqrt m\rceil}
 =o_{\alpha,A}(B/\sqrt m).
 \tag{5.7g}
\]

Thus the free strip corridor can be coefficientwise critical only after its
deterministic collars are discarded; the actual embedded corner family is
exponentially negligible in quotient packing.  This does not yet bound all
genuine zero-winding returns, but it removes the strongest explicit
candidate saturator constructed so far.

There is now also an exact local dictionary for the remaining residence
mass.  For a rank-\(k\) Johnson path

\[
 X_{i+1}=X_i-\{\alpha_i\}+\{\beta_i\},
 \qquad L_{i,q}=\bigcap_{h=0}^{q}X_{i+h},
\]

if both adjacent depth-\(q\) shadows are floor-correct, then

\[
 \boxed{L_{i,q}=L_{i+1,q}
 \quad\Longleftrightarrow\quad
 \beta_i=\alpha_{i+q}.}
 \tag{5.8}
\]

Thus adjacent equality is exactly a positive coordinate residence of
length \(q\).  In the step-two PBBS projection this is the consecutive
omitted-label gap \(2q-1\), and hence

\[
 C_q^{\rm fc}\le M_{q-1}
 =E_q-2E_{q-1}+E_{q-2}.
 \tag{5.9}
\]

The first four depths are already harmless:

\[
 C_1^{\rm fc}=C_2^{\rm fc}=0,
 \qquad C_3^{\rm fc}=(2m+1)(m-1),
 \qquad C_4^{\rm fc}\le(2m+1)(2^{m-1}-m).
 \tag{5.10}
\]

Consequently any critical adjacent-shadow/residence mass must occur at
depth tending to infinity.  Equivalently, after fixing a target \(S\), a
floor-correct occurrence is a good directed \(q\)-edge window in the PBBS
permutation restricted to owners containing \(S\), while (5.8) is exactly
the existence of a good one-edge extension.  The remaining packing problem
can therefore be stated as suppression of long extendible paths in these
fixed-target fibres.

For positive winding, the exact first-deficit moment, height trace, and
chronological-cell ledgers remove, at little-oh scale:

* winding tending to infinity;
* support/height ratio tending to infinity;
* sub-Gaussian height;
* cells carried substantially by deficits (o(m)); and
* near-total carrier deficits.

The remaining positive sector has bounded winding and one actual
even--odd chronological cell of length \(\Omega_A(\sqrt m)\), with both
carrier deficits interior-macroscopic.  Proving that these two rare
carrier events cannot form a critical matching is the positive-winding
residual.

There is also an exact transfer-matrix formulation of the zero-winding
residual.  A separated one-crossing seam has a four-strip kernel of
coefficient order (4^m s^{-6}).  Unrestricted recrossings restore a
diagonal Green factor of critical mass \(\Theta(s)\), exactly losing that
gain.  Every critical near-saturator must therefore have a linear number
of seam recrossings.  The tempting localization of the shared carrier to
two first hits inside one dual block is false: an explicit genuine return
has its copied word crossing a dual-block separator.  The exact
synchronized state must therefore retain both unmatched height and current
block index.  The remaining coefficientwise statement is a
two-dimensional outer-carrier reconstruction inequality of critical mass
\(o(s)\).  Such an inequality would settle all zero winding at once.

The exact marked automaton has now been evaluated, and it corrects the
initial diffusion guess.  If \(p\) is the current record depth and one
lower seam loop reaches depth \(h\), then

\[
 p'=\max\{p,h\},
 \qquad\Delta a=(h-p)_+.
 \tag{5.11}
\]

The transfer is upper triangular.  With \(A=s-u\), \(b=u-1\), and
\(\lambda_q=zC_A C_q\), its Green entries are

\[
 [(I-\mathsf R)^{-1}]_{p,p}=(1-\lambda_p)^{-1},
\]

\[
 [(I-\mathsf R)^{-1}]_{p,q}
 =(1-\lambda_q)^{-1}-(1-\lambda_{q-1})^{-1}
 \quad(q>p).
 \tag{5.12}
\]

At \(z=1/4\), the first is at most \(p+2\), while every prescribed
positive displacement entry is at most one.  Thus the scalar
\(\Theta(s)\) mode is confined to zero block displacement from a
macroscopic incoming record.  The Fourier-curvature conjecture for this
natural state is false: its eigenvalues are independent of the block
marker.  Worse, exact source/sink identification is now complete and
closes this shortcut.  In reverse carrier order the final lower
first-passage resets the incoming record state to zero; after the renewal
pairs, the initial upper first-passage resets every possible outgoing
state to zero.  Therefore the physical sink sums all intermediate block
displacements, and the triangular entries telescope exactly back to

\[
 \sum_q[(I-\mathsf R)^{-1}]_{0,q}
 ={1\over1-zC_bC_A},
 \tag{5.13}
\]

with critical mass \(\Theta(s)\).  A general matrix Fourier lemma remains
true, but neither it nor the block-index mark improves the one-seam free
corridor.  Any further zero-winding gain must use cross-phase chronology
or quotient-edge-disjoint packing information absent from this local
language.

The same no-go holds for any fixed collection of transported phases whose
renewal scans admit one common atomization.  Their joint state is a product
of record chains, updated by coordinatewise maximum; Möbius inversion on
that product shows that summing the full reset sink rectangle again gives
exactly \((1-\rho)^{-1}\).  The only surviving finite-phase local question
is therefore a genuinely interlaced atomization, which must remember which
phase's renewal atom is currently open.  Soft multi-seam caps or correlated
record maxima alone cannot help.

Likewise, imposing the exact carrier factorization at a second transported
phase gives no second projection: the phase events are equivalent under the
bijective word update, and the transported tail equation is just the
iterate of the one-step tail identities.  A useful multi-phase theorem must
therefore add genuinely new simultaneous canonical geometry, not multiply
transported copies of the same equality.

There is, however, a new exact positive theorem in the independent
rotor--SCD lane.  For every power of two \(\ell\), define recursively on
\(Q_{2a}=Q_a\times Q_a\)

\[
 F_{2a}(u,v)=
 \begin{cases}
  (F_a(u),v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_a(v)),&|u|+|v|\equiv1\pmod2.
 \end{cases}
 \tag{5.14}
\]

This is an exact two-factor of \(Q_\ell\) into \(2\ell\)-cycles.  Every
cycle has transition word \(\pi\pi\), so every coordinate residence is
exactly \(\ell\).  More importantly, for every \(q\le\ell/2\), both the
forward and reverse maps

\[
 x\longmapsto
 \bigl(D_q^\pm(x),x|_{[\ell]\setminus D_q^\pm(x)}\bigr)
 \tag{5.15}
\]

are injective on the entire cube.  Thus one orientation cube has an exact
integral long-cycle factor whose lower and upper shadows are simultaneously
rainbow through half its dimension.  The proof is recursive: for even
\(q=2t\) the shadow splits into the two depth-\(t\) half-shadows; for odd
\(q=2t+1\), the cardinalities of the two deleted half-sets reveal which
half moved first and leave depths \(t+1,t\).  This also forces, and the
construction realizes, exponentially many cyclic coordinate orders.

This removes the former conflict between long residence, two-sided
rainbowness, and order-template diversity **inside one orientation
stratum**.  It is not yet coefficient one.  A fixed coordinate pairing has
a positive Gaussian pair-type capacity deficit at depth \(A\sqrt m\), so
the cycles must be coupled across both split/full/empty strata and genuinely
different pair frames.  They must moreover be thinned with the exact SCD
radius census while keeping one owner per Boolean mask.  That integral
multi-frame ownership coupling is now the precise rotor-side gate.

Finally, packet-internal literalization is no longer an obstruction.  A
simple fixed-core return has an exact circular two-core word of length
(2s+3), only one more than its (2s+2) owners.  Grouping normalized
port types across all spatial phases gives every packet-internal target
with total excess (o_A(W)).  The unresolved fusion clause is exactly
the preservation or replacement of targets whose original owner window
crosses a packet boundary.  A baseline-relative block compiler of length

\[
 N\ell+o(N\ell)+O_A(NH)
\]

for quotient blocks \(\ell\gg H\) would also prove coefficient one.
Pure diagonal-intersection replacement cannot supply it: an explicit
Johnson family forces \((5/4-o(1))\ell\) monotone interception vertices
already at depth one.  In fact a chain-of-stars Johnson family gives a
stronger arbitrary-word lower bound (L\ge(1+1/24)S-O(1)), even with
arbitrary nonzero helper letters and arbitrary witnesses.  Suspending the
example to depth two preserves distinct adjacent lower colours, so
first-shadow rainbowness and odd-graph legality are still insufficient.
This obstruction cannot occur in the actual PBBS depth-one projection,
whose adjacent lower colours are the intervening distinct middle owners;
it shows that any successful block compiler must use genuinely
PBBS-specific higher-depth chronology, not a universal Johnson theorem.

### Exact multi-frame two-resolution and the bridge-one gate

The recursive orientation-cube factor has now been assembled into an exact
integer multi-frame multicover.  Fix a power of two \(\ell\) with
\(2H\le \ell\le m\), put \(R=2\ell\), and take all coordinate relabellings
of every radius class with the clipped SCD census

\[
 \gamma_d=N_d-N_{d+1}\quad(d<H),\qquad \gamma_H=N_H.
\]

After the common scale \(Q=R(2m)!\), the resulting labelled-chain multiset
has two exact resolutions:

* a dynamic resolution into genuine \(R\)-cycles of the recursive rotor,
  with total one-cut toll
  \[
    {Q\over\ell}\sum_{q=1}^H N_q=O(QW/\sqrt m)=o(QW);
  \]
* a coverage resolution into \(Q\) genuine clipped SCD colours, each of
  which covers every band mask exactly once.

The equality is statewise, not merely fractional: both sides are invariant
under \(S_{2m}\), and every labelled radius-\(d\) chain state has the same
multiplicity \(Q\gamma_d/|\Omega_d|\).  Giving every occurrence a full
radius-\(H\) collar preserves this equality.  Consequently every individual
SCD colour already gives an integral partition of the \(W\) middle owners
with **zero** designated lower or upper holes.  The only missing cost is the
ordering of its chosen useful states.

For full states

\[
 \omega=(L;z_1,\ldots,z_{2H};R),\qquad |L|=|R|=m-H,
\]

the bridge-one successors are classified exactly.  Besides identity, they
are

\[
 L'=L-x+y,\quad z'=(x,z_1,\ldots,z_{2H-1})
 \quad(x\in L,\ y\in R),
\]

and

\[
 L'=L-x+z_j,\quad
 z'=(x,z_1,\ldots,\widehat z_j,\ldots,z_{2H})
 \quad(x\in L,\ 1\le j\le2H).
\]

Thus the bridge-one digraph is regular, strongly connected, and has degree

\[
 1+(m-H)^2+2H(m-H)=1+m^2-H^2.
\]

A radius-\(d\) chain has exactly

\[
 E_{d,H}=((m-d)_{H-d})^2
\]

full-collar extensions.  This yields the weakest current rotor gate:

> For every fixed \(A\), find one SCD and one radius-\(H\) collar extension
> of each of its chains such that the \(W\) useful states have a directed
> bridge-one path cover with \(p=o(W/H)\) paths.

Indeed the paths cost one letter per owner, and joining the \(p\) paths
costs at most \(2Hp=o(W)\).  This `EP_A` statement is strictly weaker than
requiring the SCD itself to follow rotor edges: singleton-promotion arcs and
arbitrary collar extensions are allowed.  It is still unproved.  In
particular the \(N_H\) chains reaching the outer boundary have no extension
freedom, so high degree of the ambient bridge graph alone is not a rounding
argument.

The same conclusion can be phrased as a low-switch identification of two
already integral resolutions.  For each labelled chain type, its dynamic
occurrences and its SCD-colour slots form a balanced complete bipartite
graph, so typewise perfect matchings exist.  The objective, however, counts
colour changes between consecutive *different* types around a rotor cycle;
therefore independent typewise Birkhoff decompositions do not control it.

The SCD hypothesis can in fact be removed.  Two independent
lower-bounded inclusion flows give, integrally, one ordered deletion flag
and one ordered addition flag of length \(H\) at every middle owner.  At
each depth every lower and upper target then has multiplicity

\[
 \left\lfloor W/N_q\right\rfloor
 \quad\hbox{or}\quad
 \left\lceil W/N_q\right\rceil .
\]

Combining the two flags gives one genuine full useful state at each owner.
Thus common ownership, nesting, both signs, integrality, and zero holes are
simultaneously feasible without any SCD.  The strictly weakest current
literal gate is therefore:

> **\(\mathrm{CP}_A\).**  Choose one full useful state at every middle
> owner so that all lower and upper targets through
> \(H=\lceil A\sqrt m\rceil\) are covered, and so that the chosen states
> have a bridge-one path cover with \(p=o_A(W/H)\) paths.

Such paths compile directly to length \(W+2Hp=W+o_A(W)\).  The two-flow
theorem proves existence of the covering transversal; it does not prove
the path cover.  In deletion/addition coordinates a bridge-one step shifts
the entire deletion queue, prepends the departing coordinate to the
addition queue, and performs one Johnson exchange.  Consequently
\(\mathrm{CP}_A\) is precisely the still-missing correlated coupling of the
two balanced flag flows with long MTF chronology, not another marginal
rounding problem.

There is a second, quotient-row formulation with unusually sharp local
statistics.  For prime \(p=2m+1\), retain only translation packets whose
cyclic rows are rainbow simultaneously through
\(K=\lceil A\sqrt m\rceil\).  The discarded fractional middle mass is
\(o(B/\sqrt m)\), where \(B=W/p\), and the same common packet weights have
aggregate signed-band deficit \(o(W)\).  At positive depth every
nonexceptional packet pair has relative codegree \(O_A(m^{-2})\).  At the
middle rank the only \(m^{-1}\)-scale codegrees lie on a quotient odd graph
of maximum degree at most \(m+1\); off that sparse backbone the codegree is
again \(O(m^{-2})\).  All exceptional quotient vertices over the Gaussian
window form only a polynomial family.

This reduces the row-orbit route to the integral packet lemma
\(\mathrm{ISBP}_A\): find a quotient packet matching leaving
\(o(B/\sqrt m)\) middle vertices while respecting every balanced
lower-rank quota.  That lemma would lift to an \(o(W)\)-defect literal
band cover.  It is not implied by ordinary degree--codegree nibbling (the
sparse high-codegree cycle backbone and the bundled cross-rank flags must be
used), and it remains unproved.

### PBBS critical-sector audit correction

The proposed profile--boundary ``exact joint saturation'' construction is
not a theorem about actual PBBS objects.  Three gaps are decisive:

1. its weak-composition coefficient \(\mathcal E_{m;s,p}\) is an upper
   capacity envelope; the source note explicitly does not assert that every
   counted tuple is a dynamically realizable inverse tower;
2. the fixed-word estimate is only an upper bound
   \(\mathcal B(e)\le U(e)\), but the loading argument uses it as a lower
   available capacity and assigns arbitrary words to fibres; and
3. giving every formal tower its own \(3(2s+1)\)-cycle proves only a global
   Catalan edge count, not the required fibrewise injection into distinct
   compatible parent and descendant clones.

Accordingly that note proves, at most, saturation of a formal numerical
allowance/free-cycle relaxation.  It does not close, or refute, the actual
critical \(p\asymp q\asymp\sqrt m\) PBBS packing problem.

There is nevertheless a genuine local chronology family.  For
\(p\ge3\), \(s\ge2p-1\), \(h\le p-2\), and any height-\(h\) Dyck filler
\(F\),

\[
 D=1^{s-p+1}0^p1^{2p-1}0^{s-h}F0^h
\]

has an explicit first zero-winding PBBS return of duration \(s\), overlap
\(p\), first-mountain depth \(p\), and residual depth \(s-p\).  Height-
bounded fillers can carry a positive fraction of their *local* Catalan
class, so local-word rigidity cannot supply the missing gain.  Relative to
the full ambient semilength, however, this family is still smaller by
\(\exp(-\Theta(\sqrt m))\); it is not a critical packing or a coefficient-
one obstruction.

The genuine PBBS critical residual has also narrowed.  The full-depth
profile contribution with terminal curvature \(y_p\ge2\) is
\(O_A(4^m/m^{5/2})\); after the already proved two-limit deletions, only

\[
 p,q,b\asymp\sqrt m,\qquad y_p=1
\]

remains.  Its terminal inverse fibre is an actual \((2q+1)\)-state PBBS
rotor.  Exactly one state is bad, so precisely
\(b=2q+1-p\) consecutive phases support the terminal fan, and its return
packing is one.  Hence any positive endpoint boundary is created strictly
above this terminal rotor.  Transporting all allowed top starts back to one
rotor fibre gives sets \(\mathcal A_x\); every edge-disjoint family has
size at most

\[
 2\left|\bigcup_x\mathcal A_x\right|.
\]

Thus the remaining terminal theorem is the weighted transported-union
estimate \(\sum|\bigcup_x\mathcal A_x|=o_A(4^m/m^2)\), not another
terminal profile bound.

Independently, the complete two-phase nonoverlap atlas is an upper ideal in
a triangular phase lattice.  Minimal nonoverlap corners inject into two
coloured quotient edges, and a strict first-maximum suffix tail shows that
every critical-order packing has only \(o(s)\) such corners per return on
average.  All additional phases within the same return merely refactor one
of these corner corridors.  Therefore the surviving zero-winding family is
either persistent-overlap or a support-disjoint sparse-corner shield; the
missing step is a cross-return incidence theorem for those sparse roots.

## 6. Exact current conclusion

The constant-one route now has:

1. complete correct PBBS lower and upper support at every depth;
2. a low-boundary physical spine, conditional only on PBBS residence;
3. legal tensorized long-interval descent;
4. owner-fixed positive spike charts for both signs, including upper
   depth one; and
5. exact abstract rainbow binning of every bounded-load upper collision
   sector;
6. an exact \(4H-1\) dominance-staircase chart compressing all
   floor-correct lower and upper targets destroyed at one cut;
7. a factor-two reduction of all return packing to simple fixed-core
   open-wreath sectors;
8. an exact multi-cut chart of cost \(7H+3S-3\), eliminating the former
   \(HJ\) endpoint toll; and
9. an exact obstruction proving that fixed-frame or paid-seam realizations
   of the remaining cross-cut packets are insufficient.
10. an exact shared-boundary collision theorem removing zero-winding
    endpoint overlap through every (L=o(m^{1/5})) at the required
    packing scale;
11. an exact four-strip/renewal decomposition locating the remaining
    zero-winding loss in one diagonal Green mode;
12. a positive-winding reduction to a matching of two
    interior-macroscopic carrier spikes; and
13. an all-phase circular packet compiler with (o(W)) excess for every
    packet-internal target.

The shortest direct route still lacks \((\mathrm{ST}_A)\) for every
fixed \(A\), but the possible saturator is now much narrower: it must use
large-overlap zero winding with a surviving diagonal renewal mode, or
bounded positive winding with a genuine macroscopic two-carrier cell.
Equivalently, one may prove the outer-carrier reconstruction inequality.
The clustered fallback
\((\mathrm{CS}_A)\) asks instead for vanishing active-span density. The
stronger \((\mathrm{CP}_A)\) and bounded ambient-completion congestion
statements are optional routes, not the coefficient-one threshold. The
same-phase entry-neutral two-port formulation remains closed by the spacing
bound above. Until either reciprocal-height saturation is excluded or
active-span density vanishes, coefficient one is not established.

## 7. Growing-depth top-fibre promotion gate

There is now a sharper direct literal gate which removes the fixed-Gaussian
reset obstruction.  Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q=W/N_q,
\]

and let \(H\) be the largest integer for which

\[
 \lambda_H\le m+H.
\]

Then, exactly,

\[
 m-H<\lambda_H\le m+H,
\]

and asymptotically

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=\Theta(W/m),\qquad HN_H=o(W).
\]

The two Boolean tails beyond depth \(H\) contain only \(O(W/H)=o(W)\)
masks.

Fix a top \(U\in\binom{[2m]}{m+H}\).  Every cyclic order of \(U\) gives a
bridge-one promotion cycle whose middle owners are its cyclic \(m\)-windows.
A consecutive segment of \(s\) states is one legal promotion path; at every
depth \(q\le H\), its lower and upper useful flags are the corresponding
cyclic intervals of lengths \(m-q\) and \(m+q\).  Write

\[
 a=\lfloor\lambda_H\rfloor,\qquad r=W-aN_H.
\]

The exact scalar identity

\[
 (N_H-r)a+r(a+1)=W
\]

uses only legal segment lengths, since \(m-H\le a\le a+1\le m+H\) whenever
the longer length occurs.  Thus one path at every top, with \(r\) paths of
length \(a+1\) and all others of length \(a\), has exactly \(W\) owner slots
and reset toll \(2HN_H=o(W)\).

Taking the full coordinate orbit of these two segment lengths gives an exact
fractional solution in which every top and middle owner has weight one, every
lower and proper upper depth-\(q\) target has hit weight \(W/N_q\ge1\), and
the depth-\(H\) upper target has weight one.  Balanced integral owner-to-top
assignment is also available separately by a totally-unimodular inclusion
flow.  Hence reset cost, tails, scalar capacities, divisibility, local
chronology, and all fractional marginals are settled.

The remaining theorem is the integral top-fibre promotion design
\((\mathrm{TFP}_H)\): choose one cyclic segment of length \(a\) or \(a+1\)
at every top so that the middle owners partition the middle layer and all
lower and upper flags through depth \(H\) cover their ranks.  Its linear
relaxation is feasible exactly.  Independent topwise rounding is useless:
a fixed middle owner is then missed with probability \(e^{-1}+o(1)\).
Moreover the depth-one collision budget is only

\[
 W-N_1=W/(m+1),
\]

so the integral choice must be almost two-sided rainbow, not merely
concentrated around the fractional mean.  Proving \((\mathrm{TFP}_H)\), or
an approximate version with total owner-and-shadow defect \(o(W)\), gives a
literal word of length \(W+o(W)\).

The extreme \(H=m-1\) formulation is exact but not presently stronger.  It
becomes an all-ranks move-to-front universal-recency problem and demands
strictly \(o(W/m)\) path components.  Whole local odd-wreath cycles and every
fixed-core construction have only the critical \(\Theta(W/m)\) component
count.  The calibrated growing depth above is preferable because
\(\Theta(W/m)\) paths already have negligible reset cost.

### Weaker first-crossing packet form and the exact absorber

For covering rather than exact owner partition, the cleanest calibration is
the first \(H\) satisfying

\[
 \lambda_H\ge M:=m+H.
\]

Then

\[
 T:=MN_H=W-O(WH/m)=W-o(W),\qquad HN_H=o(W).
\]

Choose one full cyclic promotion packet at every rank-\(M\) top.  The
literal compiler uses \(T+O(HN_H)=W+o(W)\) entries.  Repeated middle owners
are harmless: if \(C_q^\pm=\sum(\mu_q^\pm-1)_+\) and

\[
 E_q^\pm=C_q^\pm-(T-N_q)_+,
\]

then the exact hole identity is

\[
 M_q^\pm=(N_q-T)_++E_q^\pm.
\]

The forced deficits satisfy

\[
 \sum_{q\le H}(N_q-T)_+
 =O(WH^{3/2}/m)=o(W).
\]

Hence the weakest static packet gate asks only for one cyclic order per top
with

\[
 \sum_{q\le H}(E_q^-+E_q^+)=o(W).
\]

No exact middle matching or SCD is required.  The top-owner packet
hypergraph has exact maximum relative owner codegree \(2/m^2\), while the
realized sum of owner-pair codegrees inside one packet is only
\((2+o(1))/m\).  A reservoir of \(o(W/M)\) additional full packets repairs
every depth beyond

\[
 Q=(1+o(1))\sqrt{m\log\log m}
\]

at \(o(W)\) word cost.  The hard integral discrepancy is therefore confined
to \(q\le Q\).  Same-row packet codegrees are subcritical in aggregate over
this window; the genuine remaining dependence is vertical, because adjacent
nested ranks have normalized pair mass \(4+o(1)\).

There is an exact rank-isolating signed trade.  Two disjoint adjacent swaps
in one cyclic order give four orders \(\pi_{ij}\).  If the swap boundaries
have separation \(r\), then

\[
 {\cal I}_s(\pi_{00})+{\cal I}_s(\pi_{11})
 -{\cal I}_s(\pi_{10})-{\cal I}_s(\pi_{01})
\]

vanishes for every interval length except \(r\) and \(M-r\).  At length
\(r\) it is one octahedral square, and these squares generate exactly the
integer kernel of the point-incidence map on rank \(r\).  Thus \(r=m-q\)
isolates lower depth \(q\), and \(r=m+q\) isolates upper depth \(q\), with no
extra lattice or parity obstruction.

Using two full diagonal packets is invalid: they share at least \(M-4\)
middle owners and would leave a linear middle defect.  The valid physical
version uses two complementary promotion segments whose phase sets overlap
only in \(O(Q)\) swap-boundary neighborhoods.  It realizes the same exact
rank selector on the hard band, retains \(M-O(Q)\) distinct owners, and
costs globally only \(O(QN_H)=o(W)\) duplicate occurrences and
\(O(HN_H)=o(W)\) resets.  It is therefore a sound final absorber after an
owner/shadow near-solution.  What remains unproved is support-feasible
positivity: enough such absorber tops, with balanced point marginals, must
span the actual residual while both packet sides remain nonnegative and
near-transversal.

There is now a sharp correction to the naive positive gate.  If
\(W_1^J\) denotes transportation distance in the rank-
\(r\) Johnson graph, then every sequence of \(L\) octahedral rectangle
moves satisfies

\[
L\ge \frac12 W_1^J(\mu,\nu).
\]

This can be \(\Omega(H)\) even when \(\|\mu-\nu\|_1=4\), the two load
vectors have identical point marginals, and both lie arbitrarily deep in
the positive orthant.  Thus a positive realization cannot in general cost
\(O(\ell_1\text{-defect})\).  The correct absorber target must control
Johnson transport for the *special packet residual* and bundle many
elementary rectangles into shared segment deployments.  See
`RECTANGLE_POSITIVITY_TRANSPORT_OBSTRUCTION_20260725.md`.

### Translation-equivariant algebraic ansatz is not universal

The three-report audit isolates one exact algebraic no-go.  If
\(p=2m+1\) is prime, a wreath fixed by a nonzero translation of
\(\mathbb Z_p\) must be an arithmetic-progression wreath; up to reversal
there are exactly \(m\) of them.  A translation-invariant exact factor would
therefore require

\[
\operatorname{Cat}_m=a+p b,\qquad 0\le a\le m.
\]

But

\[
\operatorname{Cat}_m\equiv2(-1)^m\pmod p.
\]

For \(p\equiv3\pmod4\), the residue is \(p-2>m\), so no such equivariant
factor exists.  Thus a full-translation-orbit construction cannot be the
general solution; the calibrated packet/absorber route must allow genuinely
non-equivariant choices.  The proof and attachment corrections are recorded
in `ATTACHMENT_THREE_REPORTS_MASTER_AUDIT_20260725.md`.

### Strict weakening: truncated carrier-rotor paths

The primary crossing-scale atom need not be a full radius-\(H\) cyclic
packet.  The reservoir already removes all depths \(q>Q\), where

\[
Q\sim\sqrt{m\log\log m}=o(H).
\]

Inside each carrier \(U\in\binom{[2m]}{m+H}\), one may instead use the
radius-\(Q\) rotor on states

\[
(L;z_1,\ldots,z_{2Q};R_U),
\quad |L|=m-Q,\quad |R_U|=H-Q.
\]

It is a strongly connected regular digraph of degree
\((m-Q)(H-Q)\).  A path of \(M=m+H\) states compiles literally with only
\(2Q+1\) excess entries.  Taking one such path per carrier therefore still
costs

\[
MN_H+O(QN_H)=W+o(W).
\]

At every controlled rank its uniform stationary fractional load is exactly
\(MN_H/N_q\), while a cyclic packet is only one special path.  Thus the
open path-selection statement `(TRP)` in
`TRUNCATED_CARRIER_ROTOR_PATH_REDUCTION_20260725.md` is strictly weaker than
the cyclic packet gate: select one length-\(M\) rotor path per carrier so
the total hard-band hole count is \(o(W)\).  Independent paths still have
Poisson holes, so this is a genuine correlated integral theorem rather than
a completed proof.

The owner geometry of this atom is now substantially sharper. For two
time-labelled owners at Johnson distance \(\delta\), the exact relative
codegree is

\[
 \frac{\pi_d(\delta)}{\binom m\delta^2},
\]

and the first \(Q\) steps are deterministically geodesic. Late returns to
distance one are \(e^{-\Omega(Q)}\), so the maximum distinct-owner relative
codegree is actually \(O(m^{-2})\), not \(O(m^{-1})\). Splitting every
carrier into independently initialized chunks of length

\[
 Q\ll\ell\ll m
\]

costs only \(O((Q/\ell)W)=o(W)\), omits only
\(O((\ell/m)W)=o(W)\) slots, and gives an owner hypergraph of rank
\(r=\ell+1\) with

\[
 r^2\Delta_2/D=O(\ell^2/m^2)=o(1).
\]

This is a strict owner-near-factor reduction, but it is not yet a theorem
for the nested flag rows. A custom growing-rank nibble and its flag audit
remain open.

The first-bite audit shows why the vanishing pair parameter is not yet
enough. Two shifted chunks of one longer rotor walk may share
\(\ell-1\) owners, and residual-degree iteration weights such overlaps
exponentially. Thus pair codegrees clear a single sparse bite but do not
close the nibble recurrence; an exponentially weighted common-subchunk
hierarchy, or a large symmetric pruning of the walk catalogue, is still
needed. After the flag rows are added, adjacent nested rows have exact
relative codegree \((2+o(1))/m\). Treating the whole flag ladder as a
generic augmented edge therefore fails for every reset-compatible
\(\ell\). Any successful matching theorem must contract and preserve the
nested column structure rather than expose its rows independently.

The dynamic transition has an exact triangular form. The arrival choice
determines the next owner and every next flag except the deepest lower flag;
the delayed departure controls that last flag and only later propagates up
the lower queue. In one *fresh* round of independent uniform states, an
average-conflict pruning followed by the Lovasz local lemma selects
simultaneously collision-free successor columns for
\((1-o(1))N_H\) carriers. The relevant average option-conflict degree is

\[
 A\frac{1+2\sum_{q\le Q}\lambda_q}{\lambda_H}=o(A),
 \qquad A=(m-Q)(H-Q),
\]

which is exactly strong enough for pruning at threshold \(\delta A\).
This one-round result does not iterate automatically. Exact continuation is
governed by candidate-facet congestion, and the delayed-departure light
cone creates a nonclosing hierarchy of future quota constraints. A
lookahead LLL works only for

\[
 \ell^2\sum_{q\le Q}\lambda_q/\lambda_H=o(1),
\]

far shorter than the radius-\(Q\) reset scale. Thus the present dynamic
gate is a genuine multi-round column-nibble invariant, not ordinary Hall.

There is nevertheless no abstract scheduling obstruction. Start from the
exact integral balanced top-rooted flag flow, with \(M\) nested columns at
every carrier and floor/ceiling total loads in every controlled row.
Independently permute each carrier's \(M\) columns into \(M\) round slots.
If a target has total load \(b\), two of its occurrences from distinct
carriers meet in one round with probability \(1/M\). Consequently the
expected total same-round collision-pair count through depth \(Q\) is

\[
 O\!\left(\frac WM\sum_{q\le Q}\lambda_q\right)
 =O(W\lambda_Q/Q)=o(W).
\]

Thus some deterministic schedule preserves every exact balanced total
quota and has rowwise-distinct current layers after marking only \(o(W)\)
carrier-rounds. The remaining temporal problem is purely physical:
factor each carrier's scheduled balanced columns into one legal rotor path.
Quota alignment and round scheduling themselves are already compatible.

There is also an exact fluctuation--dissipation obstruction to local heat
baths. If an \(\ell\)-owner chunk mean-reverts at rate \(\alpha\), then

\[
 \mathbb E\|v'-v\|_2^2
 =2\alpha\ell(1-\ell/\binom Mm).
\]

Likewise, a cube of \(K\) support-disjoint rectangle bits with cellwise
rate \(\alpha\) has variance \(2\alpha K\). Hence neither independent
chunk resampling nor an isolated topwise cube can give useful drift with
bounded variance. Any successful descent must couple many carriers so
that their fluctuations cancel through negative covariance.

### Literal rectangular rotor cube

A new positive construction crosses the earlier static fragmentation
barrier. An arbitrary ordered \(2Q\)-collar can be reprogrammed, while
performing one prescribed core--tail exchange, in exactly \(4Q+1\) legal
rotor updates. Rectangularizing the multi-swap cube with

\[
 t\sim M/(8Q),\qquad p\sim Q/2
\]

therefore compiles every cube vertex into one \(M\)-state carrier path and
realizes

\[
 pt=(1/16-o(1))M
\]

independent support-disjoint rank-isolating rectangles per carrier. Across
all carriers this is \(\Theta(W)\) genuine designated repair directions at
literal length \(W+o(W)\). The complete middle-owner vector is affine in
the bits with bounded influence:

\[
 O(E)=O(0)+\sum E_{ij}d_{ij},\qquad
 \|d_{ij}\|_1\le8,\quad\|d_{ij}\|_2^2\le64.
\]

Thus middle ownership no longer causes a superconstant variance penalty.
The unresolved part is the nonmiddle connector braid. For a source collar
swap at positions \(r,r+1\), the explicit flush/reload route has exact
connector squared norm \(4\) at every rank
\(h=r+1,\ldots,2Q-1\), hence total \(\Omega(Q)\) per active bit. The
connector image is not low-dimensional, and the obvious opposite-route
pairing cancels the desired marked rectangle together with the connector.
A genuine cross-port or cross-carrier coboundary is therefore required.
The construction and audits are in
TRUNCATED_ROTOR_STATIC_CUBE_COMPILATION_20260725.md and
TRUNCATED_STATIC_CUBE_CONNECTOR_AUDIT_20260725.md.

### Deterministic all-depth-rainbow carrier trajectories

There is now an explicit large path catalogue in which the internal
support problem is solved exactly. Label a carrier
\(U=\{u_c:c\in\mathbb Z_M\}\), let \(u_c\) depart at time \(c\), and let
it return at time \(\rho(c)\). If the positive gaps satisfy

\[
 \sum_c[\rho(c)-c]_M=HM,\qquad
 Q<[\rho(c)-c]_M<M/2-Q,
\]

then the resulting owner cycle has a unique radius-\(Q\) rotor lift and
every map

\[
 t\mapsto L_q(t),\qquad t\mapsto U_q(t)
\]

is injective for every \(q\le Q\). Zero-winding disjoint adjacent switches
already give \(2^{\lfloor M/2\rfloor}\) such noncyclic trajectories per
labelled carrier.

After full coordinate symmetrization and nested priority claims, this
catalogue has an exact carrier-saturating fractional point, target loads at
most one, scalar leave \(o(W)\), and every separate-rank Hall inequality
integrally. Thus internal chronology, self-collision, scalar capacity, and
ordinary rowwise Hall are all closed simultaneously. The remaining theorem
is one common trajectory choice per carrier.

A partial common matching on \(N_H-R\) carriers leaves at most
\(\delta_q+c_qR\) holes in each protected row. Hence the necessary
rowwise \(o(W)\) condition requires only \(R=o(N_H)\), not
\(R=o(N_H/\sqrt m)\). Converting that weaker rowwise leave into total
\(o(W)\) cost still needs a tagged vertical reserve theorem. The exact
catalogue and reserve ledgers are in
MATH_ATTACK_H_DETERMINISTIC_CARRIER_ROTOR_TRAJECTORIES_20260725.md and
MATH_ATTACK_H_RAINBOW_CATALOGUE_RESERVE_COMPLETION_20260725.md.

### New audits: exact owner hierarchy, priority ladders, and the residual gate

A coordinate-symmetric pruning to monotone Johnson geodesics of length

\[
 \ell=\lfloor\sqrt{QH}\rfloor
\]

has an exact all-orders owner-overlap bound.  If \(P\) is one chunk, then

\[
 \Psi_j(P)
 \le (2+o(1))\frac{\ell}{\binom m{j-1}^{,2}}
 \qquad(2\le j\le\ell),
\]

and consequently the exponentially weighted overlap series down to owner
density \(1/\log m\) is

\[
 \sup_{z\ge1/\log m}\mathcal K_z(P)
 \le(2+o(1))\frac{\ell}{m^2}.
\]

This closes the *static* higher-owner-overlap enumeration which defeated
the shifted-chunk catalogue.  It does not by itself prove hereditary
residual degree/link control through all nibble rounds; that propagation
claim is still under audit.  Even if the owner near-factor closes, its
flag rows must still be packed simultaneously.

For the monotone geodesic orbit, however, the controlled flags are not
genuinely hidden.  With

\[
 G_{i,j}=C+\{a_{i+1},\ldots,a_g\}+\{b_1,\ldots,b_j\},
\]

one has

\[
 X_t=G_{t,t},\qquad L_q(t)=G_{t+q,t},\qquad
 U_q(t)=G_{t-q,t}.
\]

Taking a geodesic certificate with \(Q\) buffer phases at both ends makes
these identities valid for all \(\ell\) physical central starts at only
the usual \(O(QW/\ell)=o(W)\) reset cost.  Thus the remaining flag problem
is exactly a packing problem for diagonal strips in two-chain grids, not a
choice of hidden rotor states.  See
`GEODESIC_GRID_STRIP_FLAG_REDUCTION_20260725.md`.
The exact enumeration is in
`MATH_ATTACK_GEODESIC_ORBIT_TRP_OVERLAP_PRUNING_20260725.md`.

The common priority order has a sharper exact residual description.  If
\(B_q(P)\) is the number of phases of a base trajectory whose first blocked
depth is at most \(q\), and \(d_q=M-c_q\), then a legal nested priority
exists exactly when

\[
 B_q(P)\le d_q\quad(q\le Q).
\]

The number of priorities is

\[
 (M-B_Q)!
 \prod_{q=1}^Q\frac{(d_q-B_{q-1})!}{(d_q-B_q)!}.
\]

After enlarging every deadline by only an \(o(W)\) scalar ledger, this
gives a rigorous first owner-scale bite of order \(N_H/M\), a factor
\(\Theta(\sqrt m)\) larger than treating all flag slots independently.
Iteration is equivalent to regeneration of the pathwise prefix slack
\(d_q-B_q(P)\); a row-quasirandom residual exhausts that slack almost
immediately.  Thus the new exact gate is an aligned deadline-slack
residual, not another pair-codegree estimate.  See
`MATH_ATTACK_LADDER_PRIORITY_OWNER_SCALE_NIBBLE_20260725.md`.

### Symmetrized stationary rotor resolution and hidden-color obstruction

Full coordinate symmetrization of any integral balanced top-rooted flag
resolution gives constant integral multiplicity on every exact quotient
rotor state.  Regularity of the rotor graph then gives a deterministic
legal cycle factorization of this whole multicover.  Hence fractional
stationarity, denominators, and integral dynamics are all solved after
symmetrization.

Desymmetrization is a low-color-run problem.  If \(R\) is the total number
of maximal balanced-color runs along the rotor cycles, then a color with
reset \(o(W)\) follows from

\[
 R=o\!\left(\frac{|S_{2m}|W}{Q}\right).
\]

This does not follow from rank balance.  At one top, a prescribed state
measure has a stationary legal rotor coupling if and only if the weighted
successor Hall inequalities hold.  Stationarity also forces equality of
all consecutive ordered queue-cylinder histograms.  An explicit anticycle
table is locally floor/ceiling-balanced and rainbow at every proper rank
but has no legal successor edge at all; after orbit symmetrization its
aggregate measure is exactly uniform.  Thus the remaining information is
conditional ordered transport inside one balanced color.  The exact
results are in
`MATH_ATTACK_TRP_WHOLE_TRANSVERSAL_STATIONARY_ROTOR_COUPLING_20260725.md`,
`MATH_ATTACK_TRP_SYMMETRIZED_BALANCED_ROTOR_DOUBLE_RESOLUTION_20260725.md`,
and `MATH_ATTACK_TRP_BALANCED_FLOW_HIDDEN_COLOR_OBSTRUCTION_20260725.md`.

### Four-template coboundary: local success, dense-packing obstruction

A genuinely new local switch bypasses the failed natural connector
telescope.  The difference of two arrival diamonds whose saturated base
chains differ by one adjacent increment is zero at every controlled rank
except one, where it is the elementary Boolean rectangle

\[
 e_{B+a+y}+e_{B+b+y'}-e_{B+a+y'}-e_{B+b+y}.
\]

Using two carrier tags makes this a positive four-path switch with no
reset or connector toll.  Thus exact rank-isolated \(O(1)\)-norm rotor
coboundaries really exist.

The proposed dense paired conveyor is nevertheless closed by a new owner
obstruction.  At every useful block its two carrier sources have the same
middle owner unless the adjacent collar swap straddles the middle cut;
the injection source is also coalesced.  Hence one length-\(M\) paired
conveyor contains \((1/2-o(1))M\) disjoint equal-owner occurrence pairs.
Installing it on almost all carrier pairs forces middle duplicate excess

\[
 \left(\frac14-o(1)\right)MN_H
 =\left(\frac14-o(1)\right)W.
\]

Only the isolated rank \(m+1\) forward gadget is compatible at its source
with an owner-simple family.  The local four-template identity survives,
but coefficient one now requires a separated higher-template coboundary
whose positive paths do not coalesce at almost every source.  See
`MATH_ATTACK_FOUR_TEMPLATE_ROTOR_COBBOUNDARY_20260725.md` and
`FOUR_TEMPLATE_PAIRED_CONVEYOR_OWNER_DUPLICATION_AUDIT_20260725.md`.

### Tagged reserve: exact chain Hall and a cross-rank antichain barrier

For one-state reserve columns there is an exact capacitated hosted-chain
Hall theorem.  Every positive reserve certificate with \(R\) reserve tags,
\(S\) local cells, and \(E\) literal exceptions obeys

\[
 \operatorname{width}(\mathcal H)
 \le MR+(4Q+4)S+E,
\]

where \(\mathcal H\) is the residual hole poset.  There are explicit
weighted-level antichains of size \(\Theta(W)\) having only
\(O(W/\sqrt m)\) holes in each rank; they fit all presently proved row
budgets for some \(R=o(N_H)\), yet force \(E=\Omega(W)\) under the
coefficient-safe cell budget.  Therefore rowwise \(o(W)\) leave and every
separate-rank Hall inequality do not imply reserve completion.  A partial
common matcher must additionally force residual cross-rank width \(o(W)\)
and a legal \(O(Q)\)-phase block cover.  See
`TAGGED_FLAGGED_RESERVE_CHAIN_HALL_AUDIT_20260725.md`.

### Protected-strip pruning closes the raw overlap and fractional-cut gates

Split the deterministic banded trajectories into return-free geodesic
chunks of length (g=(1-o(1))H).  Their physical owners and every
controlled flag form one protected diagonal strip in a two-chain grid.
Declare two candidate chunks incompatible when their protected strips
share a three-element antichain.  The exact four-gap census gives

\[
 {\Delta_3+1\over A}
 \le m^{o(1)}{gQ\over m^4}=m^{-3+o(1)},
\]

where (A) is a tag degree.  Weighted isolated pruning with
(L=Q\log m), tag-fibre weight (g), and target-fibre weight one loses
only (o(W)) physical mass and retains degree

\[
 \mu=m^{5/2-o(1)}
\]

in the relevant fibres.  Every surviving protected intersection has
width at most two.  If its meet--join span is (t), it has at most
(2(t+1)) cells, there are at most (8g^2(t+1)16^t) such shapes in a
fixed strip, and each has relative degree at most

\[
 m^{o(1)}{t+1\over\binom{m-g}{t}}.
\]

Consequently the complete exponential intersection excess is
\(m^{o(1)}\) uniformly for weight \(w\le C\log m\).  The corresponding
raw moment hierarchy is summable at the formal density \(1/\log m\), and
the previous large-square obstruction is removed.  This does not make an
ordinary induced residual viable: the retained support degree is only
polynomial while the protected edge rank is \(K=gQ=m^{1+o(1)}\), so
\(\mu(1/\log m)^K\to0\).  A simultaneous multicover/color resolution is
needed instead of sequential product-survival.

There is also a new aggregate fractional conclusion.  Use the same random
pruning outcome, discard tags whose retained degree is below (mu/2),
and put uniform weights on the surviving paths above each tag.  The exact
calibration (d_v/A\le1), binomial target deviations, and tag-denominator
deviations give

\[
 \sum_v(\ell(v)-1)_+
 =O\!\left(QW(\mu^{-1/2}+L^{-1})\right)=o(W).
\]

Thus the full weighted hitting-set dual has a coefficient-safe feasible
point; individual fibre lower bounds are not being used as a substitute
for the dual.  The remaining theorem is now an integral rounding theorem:
round this one tag-saturating fractional point to one legal chunk per
retained tag with (o(W)) duplicate excess.  The width-two census supplies
the required raw moments, but hereditary/grid-aware rounding has not yet
been proved.  See
`RECTANGLE_BAD_GRAPH_BALANCED_PRUNING_LEMMA_20260725.md`,
`PROTECTED_STRIP_WIDTH_TWO_PRUNING_AND_DUAL_GATE_20260725.md`, and
`ISOLATED_PRUNING_FRACTIONAL_OVERLOAD_THEOREM_20260725.md`.

### Two-update Latin transport closes the finite PSTUBE8 connector

The separated eight-template Latin block has a literal two-update
triple-to-singleton transport.  If its four endpoint lower traces are
\(S-\{q_i\}\), choose a fresh common-residual set
\(P=\{p_1,p_2,p_3,p_4\}\) and common departures \(d_1,d_2\), then use

\[
 (d_1,p_i),\qquad(d_2,q_i).
\]

The one new connector occurrence per carrier is owner-simple; the final
states have a common lower core and the allowed adjacent-swap collar braid,
with singleton traces \(p_i\).  The common residual reservoir loses only
\(O(M/Q)\) labels per tube, so one four-carrier tube gives
\(M/4-o(M)\) isolated bits and the aggregate capacity is
\((1/16-o(1))W\).  The carrier hypergraph of four \(M\)-sets sharing an
\((M-1)\)-core has a near-perfect quartet matching.  The remaining
\((\mathrm{PSTUBE}_8)\) statement is the committed whole-tube owner
near-factor.

The transport does not close protected-strip rounding.  The corrected
pointwise pruning degree is \(\mu=m^{11/6-o(1)}\), so
\(K^2/\mu=m^{1/6+o(1)}\), and the parameter-matched projective cut remains
compatible with the abstract data.  Moreover \(W/16\) Latin rectangles can
repair only \(W/8\) positive target units; since a missed chunk carries
\(K=\Theta(gQ)\) claims, the absorber still requires a
\(1-O(1/Q)\) transversal and coordinate-marginal balance.  See
`MATH_ATTACK_PSTUBE8_LATIN_TRANSPORT_AND_PROTECTED_STRIP_ABSORBER_20260725.md`
and `MATH_ATTACK_PROTECTED_STRIP_EDGE_COLORING_WIDTH_TWO_FAILURE_20260725.md`.

### Whole-tube absorption exposes the exact owner leave

For \(t\) carrier-disjoint four-carrier Latin tubes, any squarefree final
configuration covers exactly \(4Mt\) owners.  Hence its leave is

\[
 |\mathcal L|=W-4Mt.
\]

If all but \(r\) calibrated carrier tags are used, then

\[
 |\mathcal L|=(W-MN_H)+Mr=o(W)
\]

whenever \(r=o(N_H)\).  The stronger exact condition is

\[
 d_a(\mathcal L)=W/2-\Gamma_a,
\]

because every Latin rectangle preserves coordinate marginals.  A rooted
matching of the owner-defect rectangles into distinct port-stable cells
then commits all tube signs and gives a genuine owner near-factor with
literal cost \(W+O(QN_H)=W+o(W)\).  The remaining theorem is the hereditary
host Hall condition for those rooted rectangles; the scalar cyclic-interval
near-design ledger alone does not imply it.

There is a coefficient-scale restriction which the raw
\((1/16-o(1))W\) flag-cell count hides.  In the present transported
one-braid tube, the adjacent collar swap reaches a middle-owner-sensitive
cut only \(O(1)\) times per \(\Theta(Q)\)-cell sweep.  Hence only

\[
 O(W/Q+WQ/M)=o(W)
\]

cells change the middle-owner multiset, and their total positive correction
capacity is of the same order.  The rooted absorber therefore cannot create
a near-factor from a positive-density defect.  The missing global theorem
must first produce a whole-tube owner prepacking already within this
absorption scale, and must then prove the hereditary host Hall cuts for its
residual rectangles.  The detailed count is in
`MATH_ATTACK_WHOLE_LATIN_TUBE_MATCHING_AND_OMITTED_OWNER_LEDGER_20260725.md`.

## Orbit-capacity and hard-resource stalling update

For one indexed edge-transitive template orbit with vertex-orbit
intersection numbers (a_O), the exact fractional capacity is

\[
 \nu^*=\frac{|E|}{\Delta}=min_{O:a_O>0}\frac{|O|}{a_O}.
\]

One full-orbit integral matching also implies every nonnegative weighted
residual cut by averaging its coordinate translates.  The middle-only
wreath case is exact by the MSW odd-graph factor.  Protected multirank
targets change the unweighted matching number and are not covered by that
theorem.

For a floor-calibrated band in (n=2m+1), the signed quota floors have
total arithmetic defect (o(W)), and their Gaussian sum shows that a
common augmented matching leave (L) would only need

\[
 L=o(T/\sqrt m),qquad T=W/n,
\]

rather than (o(T/Q)).  The canonical MSW factor itself cannot be the
fixed augmented seed: it has an audited
((1/16-o(1))W) first-shadow hole obstruction, and its wreath supports
have no non-dihedral order freedom.  Any MSW-started repair must therefore
replace a positive proportion of its rows.

There is also a decisive scope restriction on treating every protected
target as a hard matching resource.  A single coordinate orbit contains
at most (n!) templates and one full calibrated edge has
(K=(1+o(1))n\sqrt{\pi m}) resources.  Under product resource survival
at density (z), the expected live catalogue is (Mz^K), so it is empty
with high probability after only (O(\log m/\sqrt m)) resource depletion.
This rules out the standard product-pseudorandom nibble for one giant hard
orbit, though not an arbitrary correlated construction or a catalogue
with many genuinely distinct template types.

The corrected stochastic formulation separates resource density (z_t)
from decorated-edge degree density (\rho_t).  The desired two-anchor Palm
reference is (\rho_t/z_t); fixed composition forces its scalar row mean
exactly.  Only centered link dispersion, conditioned second moments, and
the signed residual sampler cuts remain.  The hard-orbit stalling theorem
suggests using this machinery only for bounded-rank chunks, while treating
the full lower/upper band as a soft additive trace defect.

See `AUGMENTED_ORBIT_STALLING_AND_SOFT_TRACE_REDIRECT_20260725.md`,
`MATH_ATTACK_MSW_SEEDED_FLOOR_AUGMENTATION_LEDGER_20260725.md`, and
`MATH_THEOREM_RHO_Z_PAIR_RECURRENCE_AND_COMPENSATOR_DUAL_20260725.md`.

## July 26 Gaussian-annulus update

The independent-depth entropy ledger is not a valid obstruction.  One
canonical PBBS centered Johnson (2)-factor has complete correct-rank lower
support simultaneously for every (1\le q\le m).  Thus catalogue size
cannot be multiplied by an iid occupancy rate to infer a logarithmic depth
ceiling.  This does not solve cyclic residence or literal factorization.

The critical-order residence estimate nevertheless gives a new
unconditional literal theorem.  For every (h=o(\sqrt m)), the PBBS
dominance compiler with parameter (H=h+1) has

\[
 \mathcal L_{h+1}
 \le W+O(\operatorname {Cat}_m h\sqrt m)
 =W+o(W)
\]

and covers the paired central ranks through depth (h).  Hence the central
band is proved not merely for (c\log m), but for
(\sqrt m/\omega(m)) with arbitrary \(\omega(m)\to\infty\).

The exterior quantifier is sharp in the opposite direction.  For the exact
product-SCD word,

\[
 {L_m(m-H-1)\over\binom{2m}m}\to F(A)>0
 \quad\text{if }H/\sqrt m\to A<\infty,
\]

whereas the ratio is (o(1)) exactly when
(H/\sqrt m\to\infty).  Any separately appended exterior word at fixed
Gaussian cutoff also has the antichain lower bound

\[
 |R|\ge\binom{2m}{m-H-1}
      =(e^{-A^2+o(1)})\binom{2m}m.
\]

Thus the two proved mechanisms leave a genuine Gaussian annulus.  Additive
shells, dyadic product-SCD partitions, and independent local product-box
replacement cannot bridge it: a near-(W) compiler must rethread a positive
density of baseline endpoints across cells.  Appending (s) letters repairs
at most (s) previously missing targets in any one rank.

The current constructive annulus gate is the integrally port-sparsified
fine-strip hypergraph.  Exact bipartite (b)-matching selects ports so that
all nonmiddle target degrees equal (D_1), all middle degrees are
((1-o(1))D_1), and a strip edge has only (O(h\sqrt m+H)) hard ports.
Coefficient one follows if some such port system has an integral strip
matching with nonmiddle leave (o(W)).  This laminar growing-rank matching
statement is open; ordinary maximum-codegree nibble estimates do not reach
it.

For fixed integers (1\le H<h), the ordinary full-band strip hypergraph
does satisfy the fixed-uniformity Pippenger--Frankl--Rödl hypotheses.  Hence

\[
 \tau_{m,H,h}=\tau^*_{m,H,h}+o_{H,h}(W),
\]

and a slow diagonal gives an unconditional (H_m\to\infty) integral
fine-strip cover.  This is another genuine growing-depth theorem, but its
qualitative diagonal does not reach the Gaussian tail.

Finally, a portal-tree Euler walk of length (W+O(H\operatorname {Cat}_m))
does preserve every PBBS state window, but it is **not** a literal OR word:
the forward/backward portal excursions violate delay-(H) safety.  No word
length conclusion may be drawn from that chronology without a new
factorization theorem.

The live alternatives are now:

1. prove \((ST_A)\) at every fixed Gaussian window;
2. prove the port-sparsified annulus matching theorem;
3. construct a positive-density nonlocal baseline braid; or
4. cover the annulus by a different architecture such as the ordered-Hall
   SCD rotor programme.

### July 26 late parallel audits

The ordinary Kupavskii--Zakharov relative-spread route does not apply to
the physical fine-strip port system.  For every exact target-regular port
selection and every (s=o(m^{1/4})), a deterministic (s\times s)
crossing-flag grid survives with enough common degree to force the usual
spread parameter to (1+o(1)) at (s=m^{1/5}).  This misses the
Ω(log m) spread required by the theorem.  The replacement physical
high-cover EKR theorem is now proved and independently audited.  Its
Boolean-envelope kernel contracts every non-star pairwise-intersecting
selected-port support to

\[
 \sum_{C\in\mathcal F}y_C
   =o(D_1/\sqrt m)\max_C y_C .
\]

The proof is uniform over the adaptive bounded-span witnesses and does not
require selected closure or global chart holonomy.  Thus the high-cover
clique gate is closed.  The remaining port obstruction is genuinely more
general: arbitrary non-clique fractional matching-dual supports / a
coefficient-one fractional edge-colouring.  See
`MATH_AUDIT_KZ_SPREAD_APPROXIMATION_PHYSICAL_PORT_HIGH_COVER_20260726.md`,
`MATH_THEOREM_LOCALIZED_FLAG_BOUNDARY_ADAPTIVE_KERNEL_HIGH_COVER_EKR_20260726.md`,
and `MATH_AUDIT_LOCALIZED_FLAG_BOUNDARY_EKR_QUANTIFIERS_20260726.md`.

That non-clique gate has now been sharpened.  Every support whose
conflicts are faithfully routed through two physical target anchors per
strip is the line graph of a multigraph of maximum degree at most \(D_1\)
and multiplicity at most \((4+o(1))D_1/m\).  Edmonds' odd-set formula then
gives

\[
 \chi_f'\le D_1+O(D_1/m)=D_1+o(D_1/\sqrt m).
\]

Moreover every fixed incidence gadget with at least two prescribed
targets per column has only \(O(D_1/m)\) physical realizations, while the
localized EKR theorem removes standard projective-plane multistars at
every order.  Thus the residual is not an ordinary odd cycle, multigraph
odd set, bounded gadget, or projective plane.  It must be a growing,
distributed, non-clique, rank-at-least-three strong-cycle tangle.  Exact
sufficient forms are a dual-weight \(o(D_1/\sqrt m)\) transversal of all
odd strong cycles, or deletion of that much dual mass followed by a
faithful two-anchor compression.  See
`MATH_THEOREM_PHYSICAL_FRACTIONAL_DUAL_RANK_TWO_AND_BALANCED_CORE_REDUCTION_20260726.md`.

The binary-rotor lane has a new explicit positive component.  With strict
alternation of the two rotors, (G=BA) has position-cycle lengths (m)
and (m+1), so the resulting component has length (2m(m+1)) and half
of its arcs are switches.  For odd (m\ge3) all its middle owners are
distinct; for even (m) the two owner orbits coincide, giving an exact
parity obstruction.  Thus in odd parameter the owner/component part of
the rotor gate reduces to a coordinate-orbit near-factor problem.  The
required leave (o(W/m)), lower-prefix coverage, and all-depth signed
divergence cancellation remain open.  See Theorem 4.6 of
`MATH_THEOREM_BINARY_ROTOR_DEBRUIJN_DIVERGENCE_AND_MINIMAL_SKELETON_20260726.md`.

That alternating component has now been fully audited and is **not** a
bulk solution.  For odd (m), its owner block is the disjoint union of
the two cyclic-interval products of types ((r+1,r)) and ((r,r+1)),
(m=2r+1).  Every block double-covers only half as many depth-one
targets as it has owners.  If (A_{\rm alt}) owner occurrences lie in
alternating components, then

\[
 M_1^-
 \ge\left({A_{\rm alt}\over2}-{2W\over m+2}\right)_+.
\]

Thus (M_1^-=o(W)) forces (A_{\rm alt}=o(W)); alternating components
can only be a vanishing reserve.  See
`MATH_THEOREM_ALTERNATING_ROTOR_ORBIT_HYPERGRAPH_AND_PREFIX_PROFILE_20260726.md`.

The nested-star cancellation atoms give a different and genuinely
positive rotor result.  Their six-owner hypergraph is exactly regular
with

\[
 D=m^2(m+1)(m-1)^3,
 \qquad \Delta_2/D=O(m^{-2}).
\]

A fixed-uniformity nibble therefore covers (W-o(W)) owners and supplies
((1/2-o(1))W) exactly all-depth-cancelling switches, matching the
global switch toll.  Exact de Bruijn balance is equivalent to requiring
the selected atom-source set (S) to satisfy (S=BA(S)), hence to be a
union of (m(m+1))-state orbits.  A fixed three-orbit packet is already
impossible for protected height (H\ge4), by ordered-suffix
reconstruction.  The live rotor theorem is therefore a phase-varying
matching--circulation intersection.  See
`MATH_THEOREM_NESTED_STAR_ATOM_OWNER_NIBBLE_AND_FLOW_GATE_20260726.md`.

The phase-varying part is exactly soluble at full density.  For every
protected height, all permutation states admit an explicit factor into
protected star atoms, constructed flagwise from derangements of the
boundary labels.  Thus suffix flags and (BA)-flow have no intrinsic
incompatibility.  Sparse activation must still satisfy the middle-owner
rows.  Each interaction component has an active-orbit count divisible by
(n), and a component of the minimum possible size (n) is impossible for
every (H\ge3): its orbit cuts form a square (1)-design, forcing all
pair-capacity inequalities to be tight, while the common directed suffix
edge lowers the capacity below the forced average.  Hence every sparse
atom component has at least (2n) orbits.  See
`MATH_THEOREM_PHASE_VARYING_BA_ORBIT_FLAG_FACTOR_20260726.md`.

The component lower bound has since sharpened enough to remove every
bounded packet.  With (h=\lceil H/2\rceil), disjoint protected runs give

\[
 M=kn,\qquad
 k\ge h+1\quad(m\text{ odd}),
 \qquad k\ge h\quad(m\text{ even}).
\]

Thus a height-(H) sparse atom molecule contains
\(\Omega(nH)\) full BA orbits.  For even (m), the source- and
successor-owner decks of each orbit coincide, causing linear owner
overload and closing the unperturbed atom-only lane.  Odd (m) remains only
as a growing-block integral rounding problem; the doubled Paley/Hadamard
and coherent doubled-interval designs are both refuted.

Finally, sparse PBBS/product-SCD baseline fusion is closed.  In any
literal word, a rank-(r) target needs a distinct eligible right endpoint
whose terminal letter has size at most (r).  At the first rank below a
PBBS erosion floor, none of the (W) owner-aligned endpoints is eligible.
At (H=A\sqrt m), any coefficient-one fusion must therefore rewrite at
least ((e^{-A^2}-o(1))W) baseline letters; at (H=o(\sqrt m)), it must
rewrite (W-o(W)).  This forces wholesale rethreading.  Once the desired
witness intervals are scheduled, their literal realization is exactly
the coordinatewise forbidden-interval criterion of Theorem 5.1 in
`MATH_THEOREM_PBBS_SCD_BASELINE_FUSION_ENDPOINT_NO_GO_20260726.md`.

The same file also contains a positive wholesale theorem.  Any
residence-safe Johnson middle chronology has a sparse morphological
preimage (Q) of the same length with

\[
 M_t=\bigcup_{j=t-H+1}^t Q_j,
 \qquad |Q_j|\le m-H.
\]

Thus wholesale rewriting preserves every middle target, makes every
endpoint eligible for the first exterior rank, and automatically
preserves the entire upper dilation tower.  The canonical lower tower is
rigid and cannot survive this rewrite; only the lower annulus must be
reassigned.  The live fusion theorem is now an SCD-quality lower endpoint
schedule satisfying the coordinatewise forbidden-interval criterion.
# July 26 late update: entropy retraction and exact annulus gates

The independent-depth entropy ledger is not a valid obstruction.  PBBS
supplies complete correct-rank lower support at every depth in the Johnson
sibling model, while the literal PBBS compiler proves coefficient one for
every central half-width (h=o(\sqrt m)).

The audited product-SCD exterior has (o(W)) length if and only if
(H/\sqrt m\to\infty).  It therefore does not overlap the proved PBBS
range.  The exact remaining region is the Gaussian annulus between these
two scales.

The corrected sprinkling reduction is aggregate, not pointwise.  With

\[
 q_0=\left\lceil\sqrt{2m\log\log m}\right\rceil,
\]

any family of \((1-o(1))\operatorname{Cat}_m\) cyclic orders satisfying
\(\sum_{q\le q_0}M_q=o(W)\) can be supplemented by
\(\operatorname{Cat}_m/\log m\) independent orders to leave only
\(o(W)\) holes in every deeper rank.  The aggregate quantifier is
essential.  This theorem does not bridge the annulus by itself, but it is
the valid residue of the earlier occupancy calculation.

Fine-strip ports now have exact target degrees, width (O(h\sqrt m)), and
summed off-edge-star interaction (o(D_1)), but this local information is
not sufficient abstractly: a projective-plane construction satisfies the
same degree, width, codegree, and off-edge-star scales while having
(\chi_f'/D_1\) polynomially large.  The physical route must use the full
cyclic flag kernel.

For two strip-factor alternatives, the integral choice problem reduces to
a signed graph.  Near coverage requires signed frustration index (o(W))
and pair-load imbalance (o(W)).  Same-coordinate-pair reflections have
zero frustration but linear pair imbalance, closing that natural family;
mixed-pair/product-SCD conjugates remain open.

The current exact sufficient gates are therefore:

1. (\nu_{\lceil A\sqrt m\rceil}(P_m)=o_A(\operatorname{Cat}_m\sqrt m))
   for every fixed (A);
2. aggregate layered Hall deficiency (o(W)) for one fine-strip critical
   matching; or
3. an explicitly structured physical signed-coboundary/circulation
   construction crossing the Gaussian annulus.

There is now a cleaner fixed-annulus normal form.  The proposed
"shared-prefix packet" is exactly the ordinary directed cyclic-order
packet on (2m) coordinates; its orbit-average fractional design is not a
new incidence theorem.  What is new and useful is that full middle-owner
mass is unnecessary.  For fixed (0<a<b), put

\[
 q_0=\lceil a\sqrt m\rceil,
 \qquad H=\lfloor b\sqrt m\rfloor.
\]

It suffices to choose about

\[
 {N_{q_0}\over2m}
   =(e^{-a^2}+o(1)){W\over2m}
\]

cyclic packets with middle collision mass (o(W)) and aggregate annular
holes

\[
 \sum_{q=q_0}^{H}h_q=o(W).
\]

Every missing middle owner is then appended as a singleton at exact
baseline cost, while one shared delay collar for each packet costs only
(O(W/\sqrt m)).  Thus the annulus gate is a constant-density partial
cyclic-interval design, strictly weaker than a near wreath factor.

At the first annular rank (r=m-q_0), its packet hypergraph is exactly
regular with

\[
 D_r={r!(2m-r)!\over2},
 \qquad {\Delta_2\over D_r}={2\over r(2m-r)}
      =(2+o(1))m^{-2}.
\]

The corresponding integral near-factor is still not supplied by a quoted
black box: its edge size is (2m=\Theta(\log N_r)), and the known
variable-rank nibble criterion is met only at constant-critical scale
\((2m)\Delta_2\log N_r/D_r\to8\log2\).  Rank-(r) matching also does not
force deeper coverage; the exact extension identity is

\[
 \operatorname{Ext}_s(R)=(s+1)\mu_{q_0+s}(R).
\]

See `MATH_AUDIT_GAUSSIAN_SHARED_PREFIX_PACKET_FRACTIONAL_BRAID_20260726.md`
and `MATH_AUDIT_GAUSSIAN_PACKET_Q0_MATCHING_AND_DISCREPANCY_GATE_20260726.md`.

The nonsymmetric binary-rotor gate has since been weakened further.  If
(a) is the number of nonlinear rotor switches, complementary upper load
differs from lower load by an exact sum of (a) Johnson divergences at
every depth.  Hence exact upper coverage is unnecessary: it suffices to
find an owner-transversal clustered de Bruijn cycle cover with

\[
 C=o(W/m),\qquad a=o(W/H),\qquad
 \sum_{q\le H}M_q^-=o(W).
\]

The preceding scalar switch conclusion is superseded by the global
adjacent-swap toll.  Consecutive (B)-run wreath supports add at most two
new owners, so (W\le nC+2a-2c_1).  Hence (C=o(W/m)) forces
(a\ge(1/2-o(1))W), and (Ha=o(W)) is impossible for growing (H).
The exact upper--lower divergence identity still survives.  The corrected
rotor gate requires cancellation

\[
 \frac12\sum_{q\le H}\|R_q-L_q\|_1=o(W)
\]

rather than a small number of switches.

The all-form one-chip voltage packet catalogue is also completely
resolved as a bulk mechanism.  In the weak-composition quotient, upward
packet stars intersect exactly when their downward shadows intersect.
Almost every parent has downward-shadow size
\((1/2-o(1))m\), while the entire quotient lower shadow has only
\((1/4+o(1))T\) vertices.  Consequently every packet matching covers at
most

\[
 \left(\frac12+o(1)\right)T
\]

odd form classes, and the explicit phase matching attains this bound.
Hence neither an exact nor a near-perfect one-chip packet decomposition
exists.  Modified VT deletion-code colourings do not descend through this
cyclic zero-insertion quotient.  One-chip packets remain a sharp
half-cover/reserve, not a coefficient-one bulk architecture.  See
`MATH_AUDIT_ONE_CHIP_PACKETS_VS_DELETION_CODES_20260726.md`.

# July 26 final update: one baseline and the flag-coherent SCD gate

The fixed-annulus packet theorem cannot simply be appended to PBBS, nor
can its fixed Gaussian entrance be moved inward by an uncontrolled
diagonal argument.  If the packet mass is

\[
 T=N_{q_0}-\rho,
\]

then at every omitted shallow depth

\[
 M_q^\sigma=N_q-N_{q_0}+\rho+E_q^\sigma.
\]

For fixed \(q_0=a\sqrt m\), the unavoidable two-sign shallow deficit is
\(\Theta_a(W\sqrt m)\).  For \(q_0=o(\sqrt m)\), it is

\[
 \left({4\over3}+o(1)\right){Wq_0^3\over m}.
\]

Thus a one-baseline packet proof needs \(q_0=o(m^{1/3})\) and aggregate
shallow repeat excess \(o(W)\), or else a wholesale PBBS/packet endpoint
rethreading.  This correction is independently audited in
`MATH_AUDIT_PARTIAL_ANNULUS_BASELINE_FUSION_AND_DIAGONAL_GAP_20260726.md`.

# July 26 promotion-ring closure of the chronology side

The tuned promotion-ring lane is now substantially sharper than the last
paragraph above.  Let \(H_*\) be the greatest integer satisfying

\[
 \lambda_{H_*}={W\over N_{H_*}}\le m+H_*.
\]

Then

\[
 H_*=(1+o(1))\sqrt{m\log m},\qquad
 (m+H_*)N_{H_*}=W+E,qquad E=o(W),
\]

and

\[
 N_{H_*}=\Theta(W/m)=o(W/H_*).
\]

Use one full-top promotion ring over every rank-\((m+H_*)\) top.  Across
their \((m+H_*)N_{H_*}\) phase slots, the exact truncated-SCD census

\[
 g_d=N_d-N_{d+1}\quad(d<H_*),
 \qquad g_{H_*}=N_{H_*}
\]

can be placed with exactly \(E\) blanks and exactly one tag-\(H_*\)
anchor in each ring.  The nonblank slots of every ring can be ordered as
one promotion path.  Sorting the tags in each path gives, at every
threshold \(q\), exactly \(N_q-N_{H_*}\) high--high promotion edges and
meets all coherent forced-tail lower bounds simultaneously.  Therefore
the tag census, physical path chronology, long-tail bank, component count,
and collar cost are all solved before masks from different tops are
compared.

The remaining theorem is now the **tuned vertical frame theorem**:
choose one oriented cyclic frame on every top so that middle collision
mass and the aggregate uncovered signed annular targets are both \(o(W)\).
The uniform one-frame-per-top distribution is an exact fractional design.
Horizontal same-rank relative codegrees are \(O(m^{-2})\), while adjacent
nested ranks have the exact relative value \(\Theta(m^{-1})\).  This
vertical thread is structural and makes the flattened edge-size-times-
codegree parameter diverge.

Independent top frames are decisively insufficient.  Their exact
floor-correct collision energy is

\[
 \left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.
\]

For an arbitrary joint law the energy decomposes as mean defect plus this
diagonal ring variance plus cross-top covariance.  Hence a successful
resolution must create

\[
 \mathcal C=-\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m+o(W)
\]

negative literal covariance.  Reversible one-top heat converges to the
wrong baseline, and bounded-congestion local ring switches have only
\(o(W)\) throughput.  The live object is a deterministic or highly
correlated multi-top alternating resolution, not a product nibble or a
spectral mixing estimate.

This locality obstruction is now quantitative at the literal hole level.
For a fixed middle target there are

\[
 R=\binom mH
\]

eligible roots, and a uniform frame at one root hits it with probability

\[
 p={m+H\over\binom{m+H}{H}},\qquad Rp=1+o(1).
\]

If the roots are partitioned into independent correlation blocks of size
at most \(b\), with arbitrary dependence inside each block and uniform
one-root marginals, then \(bp=o(1)\) still leaves at least
\((e^{-1}-o(1))W\) expected middle holes.  Any block-product law supported
on \(o(W)\)-hole selections must therefore have

\[
 b\ge(1-o(1))p^{-1}=(1-o(1))\binom mH,
\]

and

\[
 \log b\ge\left({1\over2}+o(1)\right)
 \sqrt m(\log m)^{3/2}.
\]

Thus bounded, polynomial, and ordinary multiscale product circuits are
all ruled out; the required dependence is essentially an entire root
star.  See
MATH_THEOREM_PROMOTION_RING_BLOCK_FACTOR_HOLE_FLOOR_20260726.md.

The same-block triple count strengthens this substantially.  At the
covering-side critical normalization, any independent-block law with
balanced one-root marginals and \(o(W)\) expected holes must have

\[
 b\ge R^{2-o(1)},\qquad R=\binom mH,
\]

or equivalently

\[
 \log b\ge(1+o(1))\sqrt m(\log m)^{3/2}.
\]

This is not an entropy obstruction to one global latent construction:
before cyclic orderability is imposed, a bipartite network flow gives an
exact integral root--target resolution, and orbit averaging uses support
at most \((2m)!\).  The remaining deterministic condition is precisely
that every root's assigned \(H\)-sets form consecutive windows of one
cyclic order, with the common shadow ledger.  The theorem and independent
audit are
`MATH_THEOREM_PROMOTION_RING_R2_BLOCK_FLOOR_AND_GLOBAL_LATENT_OVERLAP_20260726.md`.

At the owner-only level there is one useful simplification.  The full
rooted middle catalogue is edge-transitive, so exactly

\[
 \chi_f'={N_H(M-1)!\over\nu}.
\]

Consequently its all-weights/fractional-edge-colouring estimate
\(\chi_f'\le(M-1)!+o((M-1)!/\sqrt m)\) is equivalent, with no loss, to
the single unweighted estimate
\(\nu=N_H-o(N_H/\sqrt m)\).  Fibre-dense weighted duals are not a second
owner-level gate; the unweighted growing-uniformity matching remains the
gate.  See
MATH_THEOREM_ROOTED_PROMOTION_EDGE_TRANSITIVITY_COLLAPSE_20260726.md.

See
`MATH_THEOREM_TUNED_PROMOTION_RING_CAPACITY_FRACTIONAL_DESIGN_20260726.md`,
`MATH_AUDIT_CRITICAL_FULL_TOP_PROMOTION_RING_HEAT_AND_TAIL_20260726.md`,
and
`MATH_THEOREM_S_PROMOTION_RING_GLOBAL_DEGREES_CODEGREES_AND_CAPACITY_CUT_20260726.md`.

There is now an audited way to remove that interface entirely.  Retain
the chains of radius at least \(q_0\) from one full SCD, keep their
original middle corners and all original inner flags, and extend only the
outer collars to radius \(H\).  The shallow target maps are injective, so
their repeat excess is exactly zero.  At every depth \(q_0\le q\le H\),
the tag-at-least-\(q\) chains supply every signed target exactly once.

Consequently, if these inner-flag-coherent states have a bridge-one path
cover with

\[
 p=o(W/H),
\]

then one literal word has length at most

\[
 W+2Hp+2\sum_{q<q_0}(N_q-N_{q_0})=W+o(W)
\]

whenever \(q_0=o(m^{1/3})\).  Taking also
\(H/\sqrt m\to\infty\) lets the audited product-SCD exterior finish at
\(o(W)\) cost.  A concrete scale is

\[
 q_0=\lceil m^{1/4}\rceil,
 \qquad H=\lceil\sqrt m\log\log(m+3)\rceil.
\]

This theorem and its independent audit are
`MATH_THEOREM_FLAG_COHERENT_SCD_ONE_BASELINE_REDUCTION_20260726.md` and
`MATH_AUDIT_FLAG_COHERENT_SCD_ONE_BASELINE_REDUCTION_20260726.md`.
The single remaining statement in this lane is

\[
 \boxed{
 \min_{\mathcal D\ {\rm an\ SCD}}
 \operatorname{fcpath}_{q_0,H}(\mathcal D)=o(W/H).}
\]

This gate has a strong necessary geometry.  For any fixed
\(0<b<\sqrt{\log2}\), put

\[
 \kappa_b=\int_0^b(2e^{-x^2}-1)\,dx.
\]

Every successful moving-entrance path forest contains a positive-density
family of edges whose forced lower/upper SCD tails agree after a shift for
\(\Theta(\sqrt m)\) consecutive positions; quantitatively at least

\[
 \left({\kappa_b\over2b-\kappa_b}-o(1)\right)W
\]

edges have overlap at least \((\kappa_b/2)\sqrt m\).  Sparse surgery from
any stationary coordinate-pair scaffold is therefore impossible; a
successful SCD must be globally noncanonical on positive owner mass.

The custom cyclic-interval nibble has also been sharpened.  Its exact
local pair mass is only \((4+o(1))/m\), and an independent product
residual of density \(z\ge1/\log m\) has relative degree variance
\(O((\log m)^5/m^2)+o(1)\).  However there are positive-density exact
coordinate \(1\)-design residuals, at every Gaussian rank, containing no
cyclic packet: parity supplies the even-rank examples and a mod-three
character supplies the odd-rank examples.  Thus the remaining nibble
claim is a trajectory-level finite-character/holonomy theorem, not an
ordinary degree-regeneration estimate.  See
`MATH_THEOREM_CYCLIC_INTERVAL_LOCAL_MASS_AND_PARITY_HOLONOMY_20260726.md`.

Finally, tune the SCD scale to

\[
 H\asymp\sqrt{m\log m}.
\]

Then \(N_H\asymp W/m\), while one exact full-top promotion ring carries
\(m+H\) chain slots.  Hence the total local ring capacity
\(N_H(m+H)\) is of order \(W\), exactly matching the retained-chain
census, and the number of rings is already \(o(W/H)\).  The current best
constructive subproblem is therefore a promotion-ring SCD factorization:
choose one cyclic frame per top mask and a global tag assignment with the
exact SCD radius census, while making the resulting chain masks pairwise
disjoint up to \(o(W)\).  Local rings and long exterior-moving splices are
proved; their global one-fold selection remains open.

# July 26 interface correction: partial annuli do not supply the central baseline

The corrected constant-density packet theorem covers the middle layer
and the signed annulus (q_0\le q\le H) in (W+o(W)) letters, but its
(W-N_{q_0}) omitted middle owners are middle-only singletons.  A
separate PBBS central word would therefore cost a second baseline.

For (T=N_{q_0}-\rho) selected packet occurrences and shallow repeat
excess (E_q^\sigma), the exact missing interface is

\[
 M_q^\sigma=N_q-N_{q_0}+\rho+E_q^\sigma
 \qquad(q<q_0).
\]

Hence, when (q_0=o(\sqrt m)), the unavoidable aggregate shallow holes
over both signs are

\[
 \left({4\over3}+o(1)\right){Wq_0^3\over m}.
\]

A packet-only one-baseline proof therefore needs
(q_0=o(m^{1/3})) **and** aggregate shallow repeat excess (o(W)).
Neither condition follows from the fixed-(a) annulus theorem or from
ordinary diagonalization (a\to0).

At fixed Gaussian (q_0=a\sqrt m), baseline sharing is unavoidable.
Endpoint capacity forces any coefficient-one PBBS/packet fusion to
rewrite (N_{q_0}-o(W)=(e^{-a^2}-o(1))W) PBBS positions; when
(q_0=o(\sqrt m)), it must rewrite (W-o(W)).  The exact alternative is
a common order-and-cap overlay, or equivalently a wholesale endpoint
schedule satisfying the coordinatewise forbidden-interval criterion.
See
`MATH_AUDIT_PARTIAL_ANNULUS_BASELINE_FUSION_AND_DIAGONAL_GAP_20260726.md`.

# July 26 global-resolution update: the surviving integral gates

The promotion-ring problem now has a capacity-correct packing-side form.
Delete one consecutive phase from every critical top frame.  If a matching
misses \(s\) top roots, its middle-owner leave is exactly

\[
 W-(M-1)N_H+(M-1)s.
\]

Since the first two terms are \(o(W)\), an owner matching with
\(s=o(N_H)\) is sufficient for the middle ledger.  The complete repaired
catalogue has exact relative pair codegree

\[
 {\Delta_2\over D}={2+o(1)\over m^2},
\]

all static higher-codegree scales tend to infinity, and the path-local
external influence is at most \((20+o(1))D/m^2\).  A fresh isolated bite
therefore has a Bernstein exponent of order \(m^2\).  The missing statement
is hereditary regeneration of this path-distributed link bound through
\(\Theta(m)\) dependent bites; it is recorded as
\(\mathrm{RPRN}(z)\) in
`MATH_AUDIT_REPAIRED_PROMOTION_RING_OWNER_HYPERGRAPH_CODEGREES_AND_NIBBLE_GATE_20260726.md`.

There is also no local matching-polytope explanation for the remaining
factor gap.  The repaired-ring EKR theorem gives

\[
 \omega(L(\mathcal G))=D_T=M!,
\]

with the full root stars as the unique maximum cliques, while every
nonstar intersecting family has size at most
\((8/m+o(m^{-1}))D_T\).  More generally, every subcatalogue of matching
number at most \((1/8+o(1))m\) satisfies the ideal density inequality

\[
 |\mathcal B|\le D_T\nu(\mathcal B).
\]

Thus no fixed gadget, clique, triangle, or \(o(m)\)-matching-number odd
mesh obstructs a near-perfect owner packing.  Any obstruction must be
mesoscopic/global or genuinely weighted.  See
`MATH_THEOREM_REPAIRED_RING_EKR_AND_NONSTAR_CLIQUES_20260726.md` and
`MATH_THEOREM_REPAIRED_RING_SMALL_MESH_DENSITY_20260726.md`.

Independently, the explicit mechanical support atlas removes every raw
profile and one-row Hall obstruction.  A single cyclic mechanical binary
pattern balances every interval length.  Inside that support there are
integral clone matchings covering \(W-o(W)\) middle targets and, separately,
\(N_q-o(W)\) entrance targets for each \(q=o(\sqrt m)\).  The exact remaining
condition is to group all phase clones at every root into one common labelled
cyclic order.  This grouping cannot be rounded rootwise: the block-hole
theorem forces root-star-scale dependence.  The authoritative reduction is
`MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md`.

A stronger support atlas now imposes one literal common \(2H\)-core in
every top.  One may choose all cores simultaneously so that Hall assigns

\[
 L=m-3H+1
\]

distinct core-compatible middle owners to every top, leaving only
\(O(HN_H)=o(W)\) middle holes.  The same cores separately clear every
signed rank with aggregate \(O(H^{3/2}N_H)=o(W)\) holes, and each top
admits a literal \(L\)-phase core-safe promotion path.  The complete
core-safe path catalogue also has an exact symmetric fractional point,
so every nonnegative configuration-Hall cut passes.  What remains is to
make the separately integral rank assignments be traces of the same
tail order and nested phase history.  See
`MATH_THEOREM_S_GLOBAL_COMMON_CORE_PROMOTION_ATLAS_20260726.md`.

The common-core remainder now has a single audited form, CCTPF. At the
calibrated crossing height, choose one core-safe ordered tail and one
nested tag word at every top, with \(b_q\) active phases at depth \(q\).
CCTPF asks that the middle masks and both signed active trace lists be
globally injective at every depth. If it holds, an explicit delayed-atom
compiler emits only \(L+2H\) entries per top, the central repair is

\[
(W-LN_H)+2N_H+
2\sum_{q=1}^{H-1}(N_q-b_qN_H)
=O(H^{3/2}N_H)=o(W),
\]

and the established product-SCD exterior contributes \(o(W)\). Thus
CCTPF gives a literal \(W+o(W)\) word with no additional gate. The
calibration \(L+c_0H\le W/N_H\le m+C_0H\) is essential; relative
\(H=(1+o(1))\sqrt{m\log m}\) alone is too weak. The theorem and its
independent audit are recorded in the dated common-core tight-path fusion
files.

Low-order linear duals have now been eliminated as well.  For one actual
integral frame per top, all Johnson-character energies through every
sublinear degree \(d=o(m)\) can simultaneously be made subexponential.
Consequently
no subexponential-coefficient linear character inequality in those degrees
can separate every integral selection from the fractional point by
\(\Omega(W)\).  A surviving obstruction must be support-sensitive,
nonlinear, exponentially weighted, or live in genuinely linear degree
\(\Omega(m)\).  See
`MATH_THEOREM_PROMOTION_RING_ALL_LOW_DEGREE_CHARACTER_NO_GO_20260726.md`.

The complete middle positivity problem has an exact nonlinear normal form.
For one frame per root, let \(L_D\) be the middle load and put

\[
 \Phi=\sum_D{(L_D-1)(L_D-2)\over2}
      =\sum_D\binom{L_D}{2}-(MN_H-W).
\]

Then \(\Phi\) is a nonnegative integer, dominates the number of holes,
and vanishes exactly on the load floor \(\{1,2\}\).  Symmetry makes
the multi-marginal transport and Gibbs/IPF problems collapse exactly to
the deterministic minimum \(\Phi_*\); every nonnegative weighted Hall
dual passes.  Equivalently, \(\Phi_*\) is the minimum floor defect among
monomials in the product of the root cyclic-frame polynomials.  Hence the
remaining obstruction is literally a nonlinear coefficient-support hole
created by the common lag-\(H\) permutation identities.  See
`MATH_THEOREM_GLOBAL_PROMOTION_FLOOR_TRANSPORT_DUAL_AND_GIBBS_COLLAPSE_20260726.md`.

There is one genuinely global alternative to the repaired-top packing.
Deleting a coordinate from an exact odd wreath factor partitions the even
middle layer into

\[
 B={W\over m+1}=o(W/H)
\]

complementary rotor paths, whose full critical-height bridge lift has
length \(W+o(W)\).  This evades every local block obstruction.  Keeping the
paths intact leaves only endpoint queues adjustable: at depth \(q\), at
most \(qB\) flags per sign can move.  Hence a covering lift requires the
forced interior hole count to lie below this sharp capacity.  Canonical MSW
fails that cut for a positive-density set of deletion coordinates, but not
yet for all coordinates.  The audited reduction is
`MATH_THEOREM_MSW_INFINITY_CUT_CRITICAL_GLOBAL_REDUCTION_AND_TOP_NO_GO_20260726.md`.

The deletion-coordinate effect is now exact at every depth.  If \(Z_q\)
is the odd-factor depth-\(q\) lower-shadow hole count, then for a deleted
coordinate \(x\)

\[
 h_q^-(x)=Z_q-d_{q,x}+c_{q,x},
 \qquad h_q^+(x)=d_{q-1,x},
\]

where \(d_{q,x}\) counts odd holes containing \(x\), while \(c_{q,x}\)
is the intersection of the \(2q\)-boundary bands of all occurrences.
Consequently

\[
 \sum_x\sum_{q\le H}(h_q^-(x)+h_q^+(x))
 =(2m+1)\sum_{r<H}Z_r+(m+H+1)Z_H+\sum_{q\le H}K_q.
\]

Thus deleting a coordinate merely transfers an odd lower hole to the
next upper depth; coordinate averaging cannot reduce aggregate hole
mass.  A successful cut must start from a much stronger odd factor or
exploit a genuinely nonaverage almost-star concentration of its holes.
The identities and a direct \(Q_7\) check are in
`MATH_THEOREM_INFINITY_CUT_DEPTH_ONE_COORDINATE_AVERAGE_20260726.md`.

A second global formulation uses two SCDs.  Exact selectors are component
bits of their common owner overlay, and bounded owner/provider holonomy plus
legal diagonal radius-nondecreasing skips gives

\[
 L=W+O(HN_H)=W+o(W),
 \qquad p=O(N_H)=o(W/H).
\]

The algebraic ledger is complete; the missing object is a tailored pair of
SCDs realizing the physical bounded-holonomy ladder.  See
`MATH_THEOREM_N_GLOBAL_TWO_SCD_PROMOTION_SELECTOR_AND_HOLONOMY_GATE_20260726.md`.

Accordingly the frontier is no longer a scalar-capacity, profile, low-degree,
or finite-gadget problem.  The two live constructions are:

1. a globally correlated common-permutation coupling of the mechanical
   clone matchings (or a hereditary repaired-ring nibble proving
   \(\mathrm{RPRN}(z)\)); and
2. a globally noncanonical odd factor/two-SCD system whose forced interior
   flags satisfy the endpoint-capacity cuts and whose endpoint queues form
   legal nested promotion paths.

# July 26 audit: what the newest global results do and do not settle

The repaired-ring matching is **not** an immediate application of the
classical Pippenger--Spencer theorem.  That theorem is stated for fixed
uniformity, and its quantitative descendants retain constants and exponents
depending on the uniformity.  In particular, the Alon--Kim--Spencer simple
hypergraph bound has exponent \(1/(k-1)\), while the natural-barrier bounds
for non-simple hypergraphs also deteriorate with \(k\).  Here \(k=(1+o(1))m\)
and the catalogue is not simple.  The exact maximum relative pair codegree
of the repaired catalogue really is \((2+o(1))/m^2\); the antipodal
\(1/m\) codegree from the unrestricted wreath hypergraph is absent.
Consequently a growing-uniformity custom nibble remains a live possibility,
but neither an \(o(N_H)\) leave nor an \(N_H/\sqrt m\) leave follows verbatim
from the classical theorem.

The uniformity dependence is structural, not merely a missing constant:
the line hypergraph of a projective plane has
\(k=D=q+1\), \(\Delta_2=1\), and \(\Delta_2/D\to0\), while every two
edges meet.  Hence no estimate with an absolute positive power of
\(\Delta_2/D\) can imply a near-perfect matching for growing \(k\).
For the Gaussian first-annulus packet catalogue the favorable
\((2+o(1))/m^2\) maximum is nevertheless real; the disjoint-pair
codegree is exponentially smaller.  But the known variable-rank scale is
exactly critical:

\[
 (2m){\Delta_2\over D}\log N_{q_0}\longrightarrow8\log2.
\]

Thus this catalogue may beat the general theorem only by using its exact
cyclic distance-stratum geometry.

The subsequent quantifier audit makes the point exact.  Pippenger--Spencer
has \(\delta=\delta(k,\varepsilon)\) with fixed \(k\); Alon--Kim--Spencer's
one-bite theorem also fixes \(k\), takes an edge with probability \(1/D\),
and covers an \(e^{-k}+o(1)\) fraction per bite.  Grable and Vu retain
uniformity-dependent exponents, while Gould--Kelly assumes
\(1/D\ll1/A\ll\gamma\ll1/k\).  Hence replacing the bite by \(c/(kD)\)
and iterating \(O(k\log m)\) times is a plausible **new proof strategy**, not
a published black box.  See
`MATH_AUDIT_GROWING_UNIFORMITY_PS_AND_CORRELATED_LEAVE_20260726.md`.

There are also two different leave thresholds.  A finite-density theorem
for the repaired owner catalogue would suffice, because its exact owner
defect is \(W-rN_H+rs\) and only \(s=o(N_H)\) is needed.  The synchronized
all-rank common-core configuration instead has

\[
 \mathfrak H=\Delta+k(N-\nu),\qquad
 k=(\sqrt\pi+o(1))m^{3/2},\qquad N=(1+o(1))W/m,
\]

and therefore needs \(N-\nu=o(N/\sqrt m)\).  Using the same missed roots at
all ranks is already built into this identity and gives no extra
\(\sqrt m\)-saving.  A leave of order \(N/\sqrt m\) produces
\(\Theta(W)\) aggregate holes.

There is a literal support-reachable warning against an excessively strong
form of hereditary regeneration. A matching of \(o(N_H)\) genuine
repaired-ring edges can create \(o(W)\) exceptional owners with a fixed
degree loss while the ambient residual remains regular on all but
\(o(N_H)+o(W)\) vertices. Those exceptional owners retain actual residual
pair-links to at least \((4/5-o(1))N_H\) roots. Thus statewise,
every-reachable-residual RPRN is false. It does **not** refute a
high-probability theorem for the unbiased trajectory.

The stochastic audit separates noise from drift. A fresh slow bite creates
such a root-covering defect by fluctuation with probability
\(Qe^{-\Omega(m^2)}=o(1)\). Through \(O_z(m)\) bites, stopped while the
path-influence bound holds, the containment-energy martingale gives error
\(TQe^{-\Omega_z(m)}=o(1)\). The remaining dynamic event is now exact:
either path influence itself stops regenerating, or a positive-containment
family acquires adverse **predictable accepted-loss drift**. Static
codegrees and martingale noise have both been removed from this gate. See
`MATH_THEOREM_RPRN_REACHABLE_EXCEPTIONAL_LINK_COUNTEREXAMPLE_20260726.md`.

The finite-density owner process now has a weaker exact formulation.  In a
**wasteful compensated bite**, all vertices touched by any marked edge are
deleted and isolated marked edges enter the matching.  For every vertex set
\(S\), the survivor law is exactly

\[
 \Pr(S\subseteq V^*)=q^{|S|}(1-p)^{-J(S)},\qquad
 J(S)=\sum_{v\in S}d(v)-\left|\bigcup_{v\in S}{\cal E}(v)\right|.
\]

Time-zero repaired paths have internal pair mass at most
\((3+o(1))R/m\), giving relative expectation error \(O(\gamma/m^2)\).
The owner width-two estimate yields an \(m^2\)-scale one-bite tail, but
the independently audited statement does **not** extend that tail to roots
without a hereditary root--path estimate.  Weighted quarantine is enough:
an exceptional owner family \(B\) costs total root degree at most
\(\sum_{X\in B}d(X)\), so the earlier sparse reachable counterexample is
harmless.  Conditional `WBR+(z)` now consists precisely of cumulative
degree regularity plus the two-path bridge counts

\[
 b_X(e,g)=|\{f:X\in f, f\cap e\ne\varnothing,
                         f\cap g\ne\varnothing\}|
\]

and their higher-path hierarchy along the actual trajectory.  It implies
an \(o(N_H)\)-root leave and closes the repaired owner packing, but remains
unproved.  See
`MATH_THEOREM_FINITE_DENSITY_WASTEFUL_REPAIRED_RING_NIBBLE_20260726.md`.

The common-permutation interface has one sharp negative and one exact
positive theorem.  Two separately near-perfect clone Hall matchings can be
linearly incompatible: after a shore conjugation, \(W-o(W)\) paired
incidences violate the necessary physical containment

\[
                         J_a\subseteq C_a.
\]

The obstruction has a nonzero top Johnson harmonic and therefore cannot be
removed by low-degree/profile balancing.  It applies only to arbitrary
post-hoc coupling of separate matchings, not to jointly selected nested
atoms.  Conversely, checkerboard quartets of four actual tops give exact
phasewise exchanges at **every** interval length.  These moves eliminate
local top-harmonic and all non-affine parity obstructions inside a joint
fibre.  They preserve every scheduled load, however, so they provide a
candidate connectivity/Markov basis rather than energy descent.  The exact
remaining algebraic question is whether these quartets connect the integral
joint common-permutation fibre, or whether a higher nonabelian invariant
survives.  See
`MATH_AUDIT_COMMON_PERMUTATION_CONTAINMENT_AND_QUARTET_HOLONOMY_20260726.md`.

The quartet top-index lattice is now completely understood integrally.
For \(2\le M\le2m-2\), let \(A\) be the element--top incidence matrix on
\(\binom{[2m]}M\). The lattice generated by the checkerboard rectangle
vectors

\[
e_{C+a_0+b_0}-e_{C+a_0+b_1}
-e_{C+a_1+b_0}+e_{C+a_1+b_1}
\]

is exactly \(\ker_{\mathbb Z}A\). The proof computes the rectangle
annihilator over every field: it consists precisely of affine element
functions \(c+\sum_{x\in U}\alpha_x\). Field-independent rank then
implies saturation, so there is no hidden rational, modular, or torsion
obstruction beyond the element margins. This is a genuine strengthening
of the parity audit. It still does not prove physical connectivity:
actual quartet moves require four current frames with one common ordered
\((M-2)\)-template, and a lattice decomposition need not remain in the
nonnegative frame fibre. The surviving obstruction is therefore
positional/nonabelian or box-feasibility, not top-index homology. See the
dated quartet rectangle-lattice theorem in the workspace.

The phasewise identity is not restricted to quartets. For every
\(2\le d\le m-H\), choose \(d\) disjoint label pairs and an
\((M-d)\)-set common core. The \(2^d\) resulting tops support a
checkerboard exchange between any two permutations of the \(d\)
placeholder positions, and the alternating sum cancels at every phase and
every proper interval length. This reaches the full Johnson-distance range
between critical tops and preserves all signed loads and tags exactly.
The price is exponential component size and complete-cube availability;
the move remains load-neutral. Thus larger cubes remove the strictly local
template barrier but still require a global nonnegative connectivity
theorem. See the dated higher-cube exchange theorem in the workspace.

Finally, local all-depth chronology integrality is now genuinely solved.
For paired lower/upper trace maps which form a quotient chain and have
injective coordinate projections, one nested system of representatives
simultaneously covers both signs at every depth.  The natural promotion
macro is a literal instance after deleting one distinguished suffix phase;
the deleted lower image always has a unique retained copy.  Small independent
macro blocks nevertheless have a positive middle-hole floor, and a hierarchy
of branching at most \(2m\) requires depth \((1/2-o(1))H\).  Paying a fresh
cut at every level costs order \(W\log m\).  The remaining theorem is thus
precisely a globally correlated one-frame-per-root construction with
suffix-closed paired fibres and recycled/cross-spliced physical cuts.  See
`MATH_AUDIT_PROMOTION_GLOBAL_COMMON_HISTORY_20260726.md`.

# July 27 audit: deterministic collision gate, local repair radius, and slow-bite retraction

The common-core path compiler now has an exact weakest integral objective.
For one chosen literal configuration at every top, let \(\lambda_v\) be
the load of a protected physical target and put

\[
 K(e)=\sum_{v:\lambda_v>0}(\lambda_v-1).
\]

The number of missing protected targets is exactly \(\Delta+K(e)\), where
\(\Delta=O(H^{3/2}N_H)=o(W)\).  Thus the literal compiler closes if and
only if one can choose one configuration per top with

\[
                         \min K(e)=o(W).
\]

The stronger matching-and-discard route still needs leave
\(o(N_H/\sqrt m)\), because a configuration contains
\(\Theta(m^{3/2})\) protected targets.  Separate rankwise Hall matchings
do not imply this joint selection: a literal determinant-two triangle and
the depth-one common-support cuts survive.  See
`MATH_AUDIT_AND_THEOREM_COMMON_CORE_TIGHT_PATH_FUSION_20260726.md`.

Several generic rounding mechanisms for this objective are now closed.
For the full all-core path polynomial, the uniform fractional exponent is
the exact positive capacity minimizer, but the independent product law has

\[
 \mathbb E\sum_X\binom{K_X}{2}=(1/2+o(1))W,
 \qquad
 \Pr(K_X=0)=e^{-1}+o(1).
\]

The collision energy concentrates at this wrong linear plateau.  Moreover,
low-collision terms occupy at most
\(\exp(-(1-o(1))W/\binom MH)\) of product mass, and bounded target-cluster
entropy cannot improve that scale.  Neither the individual root supports
nor their global Minkowski sum are M-convex; the corresponding polynomials
are not stable or Lorentzian.  These results do not prove a positive lower
bound on \(\min K\); they show that any favorable selection must use
catalogue-scale deterministic correlation.  See
`MATH_THEOREM_COMMON_CORE_PATH_CAPACITY_AND_NONLORENTZIAN_GATE_20260726.md`
and `MATH_THEOREM_COMMON_CORE_PHI_ENTROPY_COMPRESSION_20260726.md`.

There is also a sharp abstract integrality barrier at exactly the physical
parameter scale.  A regular partitioned catalogue exists with
\(N\asymp W/m\), configuration size \(k\asymp m^{3/2}\), arbitrarily
large degree, saturated uniform fractional point, integral local root
fibres, and \(\Delta_2/D=O(m^{-2})\), yet every one-per-root selection has

\[
                              K\ge Nk/8.
\]

The construction uses affine-line directions in \(\mathbb F_R^3\) with
incidence-label twists.  It is not a literal interval-catalogue
counterexample, but it proves that fractional flow, exact regularity, local
network integrality, and pair spread cannot imply the desired collision
rounding.  A proof must use a higher interval/diagonal-shell/cocycle
identity.  See
`MATH_AUDIT_COLLISION_OBJECTIVE_CONVEX_ROUNDING_BARRIER_20260727.md`.

There is nevertheless a new exact load-changing primitive.  Three tops

\[
 C\cup\{x,y\},\qquad C\cup\{x,a\},\qquad C\cup\{a,y\}
\]

support two squarefree three-frame shores with identical complete middle
support.  Their derivative vanishes on one signed side through every
protected depth and, on the opposite side, has \(8q\) coefficients of each
sign and squared norm \(16q\) at depth \(q\).  The move has no quadratic
self-toll in the floor energy, and a fresh fourth frame witnesses strict
descent at any prescribed depth.  One- and two-top complete-frame
exchanges are load-neutral, so three tops are support-minimal.  What is not
proved is owner-level availability or simultaneous favorable signing
inside an arbitrary global selection.  At the abstract top level the
support triples form a regular 3-graph with relative pair codegree
\(2/((m-H)(m+H))=o(1)\), so fixed-rank Pippenger--Spencer gives an
almost-spanning family of pairwise top-disjoint catalysts.  These packets
also cross Boolean-cell faces and genuinely change a chosen ordered-core
histogram.  The unresolved packing concerns their \(3M\) middle owners and
their \(16q\) derivative coordinates, not their top supports.  See
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md` and
`MATH_AUDIT_THREE_TOP_TWO_BASE_CONVEYOR_AND_CORE_INVARIANT_20260727.md`.

The load-neutral exchange bank cannot supply that missing availability.
Quartets have normalized parity quotient \((\mathbb Z/2)^{2m}\), but even
after clearing these characters a degree-eight cube relation can have both
endpoints globally quartet-isolated.  Permanently hitting a dense family
of these cubes costs \((1/8-o(1))W\) incidences.  Higher cubes preserve all
loads and do not group the \(W-o(W)\) incidencewise MSW witnesses into the
\(N_H\) physical frames required by promotion.  Recyclable temporary
catalysts and the squarefree moving-hole exchanges remain open.  See
`MATH_THEOREM_L_QUARTET_INTEGER_QUOTIENT_DENSE_MARKOV_NOGO_20260726.md`
and `MATH_THEOREM_K_MSW_OWNER_STAR_GLOBAL_EXCHANGE_BRAID_OBSTRUCTION_20260726.md`.

The three-top conveyor itself is middle-neutral: its two shores have the
same middle incidence vector, so it cannot lower the middle part of
\(K^*\).  The audited moving-hole exchanges share this property.  The
six-frame mixed-placeholder rectangle is middle-nonneutral and can lower
the middle collision energy, but every such derivative preserves all
coordinate marginals.  An explicit integral load vector of collision
\((1/4+o(1))W\) is the global minimum in its fixed-marginal fibre.  That
vector has not been shown to be a legal common-core coefficient, so this
is a move-set obstruction rather than a counterexample.  The next literal
question is whether legal coefficients avoid shielded marginal fibres, or
whether a support-preserving primitive can change coordinate marginals.
See `MATH_THEOREM_PSI_MOVING_HOLE_MARGINAL_SHIELD_20260727.md`.

The displayed shield is now excluded from the literal coefficient support.
Every retained length-\(d\) cyclic path uses a coordinate in between
\(m-(4H-1)\) and \(m\) of its middle windows on every top containing that
coordinate, and every coordinate lies in exactly
\(\binom{2m-1}{M-1}\) tops.  Hence every legal coefficient satisfies

\[
 b_i=(1/2+o(1))W\qquad\text{uniformly in }i,
\]

whereas the shield has two marginals \((3/4-o(1))W\).  Collision rounding
inside the legal near-flat marginal box is still open.  See
`MATH_THEOREM_COMMON_CORE_COORDINATE_MARGINAL_FLATNESS_20260727.md`.

The corresponding **abstract marginal-fibre problem is now closed**.
If an integer singleton-marginal vector has total (mT), (T/W\to1),
and normalized deviations

\[
 \varepsilon_i=b_i/T-1/2,
 \qquad \|\varepsilon\|_\infty=o(1),
 \qquad \sum_i\varepsilon_i^2=o(1),
\]

then it has a nonnegative integer (m)-set realization (L) with those
exact marginals and

\[
                         \sum_D\binom{L_D}{2}=o(W).
\]

The asymmetric legal common-core interval implies the aggregate condition
by the zero-sum identity, with
\(\sum_i\varepsilon_i^2=O(H^3/m^2)=o(1)\).  The proof uses a local
maximum-entropy point of the hypersimplex, adjacent-integer rounding, and
only (o(W)) fresh Johnson-edge corrections.  Coordinatewise
\(b_i=W/2+o(W)\) alone is insufficient: a two-block deviation of size
\(W/\sqrt m\) forces linear collision energy.  This theorem is only in
load space; it selects no physical paths or nested shadows and supplies no
correlated annulus leave.  See
`MATH_THEOREM_NEAR_FLAT_MARGINAL_FIBRE_ROUNDING_20260727.md` and
`MATH_AUDIT_NEAR_FLAT_MARGINAL_ROUNDING_SCOPE_AND_ANNULUS_INTERFACE_20260727.md`.

The marginal neutrality is in fact only a defect of the earlier exchange
library, not an invariant of legal coefficients.  Swapping the first two
letters of one retained tight-path word changes only its second deleted
\(H\)-window, and therefore has exact middle derivative

\[
                              e_Y-e_X
\]

for Johnson-adjacent owners \(X,Y\).  It is a legal one-root replacement,
is support-minimal, changes at most two targets at each protected depth,
and strictly lowers the middle collision energy when \(L_X\ge L_Y+2\).
Every oriented Johnson edge is realizable at some top, so these legal
differences generate the full zero-total load lattice.  The exact remaining
issue is state-dependent chronology routing: bring a current duplicate
occurrence to boundary phase two, orient the unit transfer toward a hole,
and combine many such swaps without paying their \(O(H)\) trace collateral
independently.  See
`MATH_THEOREM_COMMON_CORE_BOUNDARY_SWAP_MARGINAL_ESCAPE_20260727.md`.

The strongest hoped-for **closed** router is now ruled out.  If all
companion configurations are restored and the net middle derivative is one
unit \(e_Y-e_X\), the initial and final focal tight-path decks differ in one
window.  Two-sided window chronology then forces the removed phase into

\[
          \{1,\ldots,H+1\}\cup\{d-H,\ldots,d\};
\]

an interior phase \(H+2\le i\le d-H-1\) is uniquely reconstructed from the
unchanged leaving and entering histories.  Thus neutral routing followed by
one boundary swap and exact companion restoration can expose only an
\(O(H/m)\) fraction of occurrences, regardless of the number of intermediate
moves.  Open catalyst banks, several nonneutral endpoint changes, or a
larger catalogue remain possible.  See
`MATH_THEOREM_BOUNDARY_SWAP_CLOSED_CATALYST_CHRONOLOGY_OBSTRUCTION_20260727.md`.

Allowing two nonneutral endpoint changes gives an exact positive result.
For every ((m-2))-set (R) and distinct (a,b,z,z'\notin R), two
oppositely oriented boundary swaps on two explicit tops have zero
derivative at every protected deletion length (h\ne H), while at the
middle they give the hypersimplex rectangle

\[
 e_{R\cup\{a,z\}}+e_{R\cup\{b,z'\}}
 -e_{R\cup\{a,z'\}}-e_{R\cup\{b,z\}}.
\]

The cancellation survives the nested tagged catalogue by assigning the
two changed phases a common tag.  These literal two-top rectangles generate
the complete integral kernel of the singleton-incidence matrix.  Hence
every same-singleton-marginal middle displacement has a **formal signed
physical lift with exactly zero collateral at every nonmiddle depth**; an
arbitrary zero-total displacement (z) has formal toll at most
(2H\|Az\|_1).  This closes the vertical-collateral problem at the signed
relation level and matches the near-flat marginal-fibre theorem exactly.

The remaining lift gate is dense chronological composability.  The
master-order legal state is total-variation distance ((1-o(1))W) from
every (o(W))-collision load, so a boundary-swap route needs
(\Omega(W)) nonneutral steps.  A one-toggle-per-top bank has only
(N\sim W/m) steps and is short by a factor (m).  A proof must recycle
an average of \(\Theta(m)\) rectangle states per top, or use a different
starting coefficient.  See
`MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md`.

The literal-splice audit makes that throughput deficit structural for the
present primitive.  One rectangle shore has two forced repeated owner
occurrences, and each rooted top has only one available boundary involution:
its option graph is a copy of \(K_2\).  Repeating the same swap therefore
alternates and cancels, so a rectangle-only bank has total useful
displacement \(O(N)=O(W/m)\), not \(\Theta(W)\).  Any successful dense
compiler now needs a **collar-neutral re-rooting or tail-changing move**
between rectangle toggles (or an entirely different initial table).  This
is recorded in
`MATH_THEOREM_COLLAR_NEUTRAL_RECTANGLE_BANK_LITERAL_SPLICE_AND_INSTALLABILITY_20260727.md`.

The required local re-rooting primitive has now been constructed.  Widen
the two conveyor context palettes to radius \(2H-1\), cut matched blocks of
\(4H-1\) phase starts, and telescope one direct placeholder edge against a
two-edge path on three tops.  The resulting three-top exchange has

\[
                         \Delta_h=0\qquad(0\le h\le2H),
\]

and its two shores are squarefree with the identical set of \(3d\) middle
owners.  On a designated focal top it swaps the label in rooted position
three with any label at cyclic distance at least \(4H+1\), while fixing the
ordered two-letter boundary port.  It therefore joins distinct rectangle
\(K_2\)-components.  With fresh catalysts, one focal top admits
\(m-O(H)\) successive exact recharges, so the old **local** factor-\(m\)
throughput shortage is gone.  Support three is minimal in the safely
restorable fixed-port category.

The remaining issue is global rather than local: every recharge needs two
companion source paths on the corresponding Johnson triangle of top sets.
Fresh companions prove local reuse but cannot be spent independently for
all tops; one must construct a coefficient-one global source table or a
recycling circuit in which companion states themselves feed later
recharges.  See
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`.

At the nonmiddle layers the conveyor reservoir is considerably stronger.
A transitive-orbit greedy packing gives \(W/P_H\) actual packets with
pairwise disjoint tops, common middle supports, and derivative supports at
all protected depths, where

\[
 P_H=9M^2+(9+256\sum_{q\le H}q^2){W\over N_H}
     =m^{5/2+o(1)}
\]

at the critical scale.  A single signing makes the aggregate positive
floor leakage \(o(W)\).  Thus polynomially many literal port-changing
catalysts and their simultaneous signing are proved.  Their completion to
a global owner resolution, or their occurrence in a prescribed exact
table, remains open.  See
`MATH_THEOREM_THREE_TOP_CONVEYOR_DENSE_ORBIT_PACKING_AND_SIGNING_20260727.md`.

The bank itself no longer creates an additional integral installation
gate.  If an ordinary frame matching already covers \(W-h\) middle
owners, delete every frame meeting a packet top or packet owner and insert
the whole bank.  Owner disjointness bounds the extra uncovered mass by

\[
                         3M^2K=o(W).
\]

The two packet shores are parallel in the top--owner projection, so their
all-depth signing can then be chosen after installation.  Literal splicing
costs \(o(W)\).  Therefore dense-bank installation is reduced exactly to
the **unseeded ordinary frame near-resolution** problem, rather than a new
absorber.  The latter is a growing-\((M+1)\)-uniform matching problem with
relative owner codegree \(2/m^2\), exact fractional balance, and an actual
determinant-two triangle; no integral near-resolution theorem is known.
See
`MATH_THEOREM_THREE_TOP_BANK_OWNER_RESOLUTION_PROJECTION_AND_COLLAR_WALL_20260727.md`
and
`MATH_AUDIT_PROMOTION_FRAME_GROWING_UNIFORMITY_AND_ODD_TRIANGLE_20260727.md`.

Adding middle owners to the packet hypergraph restores the critical
growing-rank obstruction.  Its exact top and owner degrees are

\[
 D_T=3(m-H)M!,\qquad
 D_O={3M(m!)^2\over(m-H-1)!},
\]

and \(\Delta_2=\Theta(D_T/m^2)\).  With packet uniformity \(3M+3\),
the standard variable-rank nibble parameter is bounded below by
\(12\log2-o(1)\), not \(o(1)\).  One slow bite gives an
\(\varepsilon\)-fraction top packing with \(O(\varepsilon^2W)\) owner
collisions, but taking \(\varepsilon=o(1)\) covers only \(o(N_H)\) tops.
The exact residual shore choice is a weighted Ising form whose quadratic
matrix is the overlap Gram of the trace derivatives.  See
`MATH_THEOREM_PHYSICAL_CATALYST_PACKET_CODEGREES_AND_SIGNING_GATE_20260727.md`.

A separate audit of the Gaussian-annulus packet catalogue confirms the
favourable time-zero maximum

\[
 K=2m,\qquad \Delta_2/D=(2+o(1))/m^2.
\]

The \(\Theta(1/m)\) antipodal codegree belongs to a different middle-rank
catalogue; at (r=m-q_0<m), adjacent targets are extremal and disjoint
targets are much smaller.  This does **not**, however, justify a verbatim
Pippenger--Spencer application.  The classical theorem fixes (K) before
choosing its regularity and leave thresholds, and its proof suppresses
\(3^K\), \(K^2\), concentration, and dependency constants.  The formal
\(N/\sqrt m\) leave comes from inserting \(K=2m\) into a fixed-rank
linear-hypergraph estimate; the catalogue is non-linear.  Vu's non-linear
bound instead contains
\((D/\Delta_2)^{-1/(K-1)}=1-o(1)\).  The known variable-rank condition is
constant-critical here:

\[
              K(\Delta_2/D)\log N=8\log2+o(1),
\]

not \(o(1)\).  A single slow bite is uniform and covers \(\Theta(N/K)\),
but iterating it needs a new trajectory-specific regeneration/absorption
theorem.  Separate \(N_q/\sqrt m\) leaves at
\(\Theta(\sqrt m)\) annular ranks would total \(\Theta(W)\), but one
synchronized packet family has a real scalar advantage.  If it selects
\(s\) packets and \(ns=N_{q_0}-L\), then exactly

\[
 H_q=(N_q-ns)_+ + \widetilde E_q,
\]

where \(\widetilde E_q\) is repeat excess above the forced floor.  For
\(q_0=a\sqrt m\) and \(L=O(N_{q_0}/\sqrt m)\), the decreasing layer sizes
give \(\sum_q(N_q-ns)_+=O_a(N_{q_0}/\sqrt m)=o(W)\).  Thus a correlated
leave does remove the scalar \(\sqrt m\) loss.  The additional theorem
still needed is the genuinely combinatorial one
\(\sum_q\widetilde E_q=o(W)\); matching at \(q_0\) alone gives no control
of these deeper-rank repeats.  There is also a catalogue-specific positive
estimate invisible to the maximum codegree: for every cyclic packet \(e\),

\[
 {1\over D}\sum_{\{S,T\}\subset e}d(S,T)
       ={4\over m}+O_a(m^{-2}).
\]

Under formal thinning to density \(z\), both this within-packet collision
parameter and the maximum one-edge link influence are \(O_a((mz)^{-1})\),
so they are \(O(m^{-1/2})\) at \(z=m^{-1/2}\); even their integrated
same-packet correction is \(o(1)\).  A wasteful slow bite with
\(\gamma=1/m\) also has total collision waste \(o(N/\sqrt m)\).  Thus
collision waste and first moments are not the obstruction.  On the other
hand, for every fixed \(m\)-set \(A\), the targets with

\[
 |S\cap A|\in\{\lfloor r/2\rfloor,\lceil r/2\rceil\}
\]

form a \(\Theta(m^{-1/2})\)-density transversal of every cyclic packet;
its complement is an edge-free residual of density
\(1-\Theta(m^{-1/2})\).  Hence regeneration cannot hold for every dense
residual: it must be trajectory-specific and avoid these slice barriers.
More sharply, entrance matching barely suppresses deeper collisions:
two packets through one deeper target have disjoint entrance traces with
probability \(1-O(1/m)\), and \(j=o(\sqrt m)\) mutually entrance-disjoint
packets can all repeat that same target.  If a near-perfect entrance
matching has the usual factorial-moment pseudorandomness at a macroscopic
deeper depth, its loads are asymptotically Poisson and it leaves
\(\Theta(W)\) holes at that single depth.  Therefore an unbiased
regenerated nibble is the wrong colored process even if its entrance leave
is optimal.  A positive annular theorem needs explicit all-depth color
compensation driving the common-interval pair energy toward its balanced
integer floor.

There is also an exact paired obstruction architecture.  Swapping every
adjacent position pair of a cyclic order (P) produces a domino twin
(P^\tau) satisfying

\[
 |E_\ell(P)\cap E_\ell(P^\tau)|=
 \begin{cases}m,&\ell\text{ even},\\0,&\ell\text{ odd},\end{cases}
\]

for (2\le\ell\le2m-2).  Hence when the entrance length (R) is odd,
the twin pair is exactly entrance-disjoint but shares (m) targets at
length (R-1).  A near-factor of these (4m)-uniform twin superpackets
would force ((1/4-o(1))N_{q_0}=\Theta(W)) repeat excess at the first
deeper rank and would refute any universal claim that entrance matching
alone controls the annulus.  The twin catalogue is regular and
fractionally saturating.  Its full local profile is now explicit: its
degree is \(D^\square=2nR!(n-R)!\), its maximum relative pair codegree is

\[
 {\Delta_2^\square\over D^\square}
 ={5\over R(n-R)}=(5+o(1))m^{-2},
\]

and its edge-local collision energy is \((50+o(1))/m\).  Moreover any
radius-\(h\) Johnson ball inside one twin superpacket contains at most
\(4h+2\) vertices, which gives factorial higher-codegree decay.  Thus the
twin catalogue passes every presently proved static/local slow-bite gate;
no degree or cut obstruction to a near-factor has appeared.  Its integral
near-factor is still not proved because the same variable-rank dynamic
ACLE iteration remains open.  See
`MATH_THEOREM_DOMINO_TWIN_SUPERPACKET_DEGREES_AND_CRITICAL_FACTOR_GATE_20260727.md`.

The specialized ACLE audit now passes every static common-column core
through logarithmic order.  The first starred \(C_4\), \(K_{2,3}\), and
\(K_{2,4}\) close by direct small-cluster counts.  The apparent
\(K_{2,5}\) loss from the crude radius-ball maximum is removed by the
factorial overlap theorem

\[
\sup_{X,F}{1\over D}\sum_{F'\ni X}
       (|F\cap F'|-1)_p
 \le (Cp)^{Cp}m^{-2},\qquad p\le C_0\log m.
\]

The proof partitions a \(p\)-subset of a fixed twin packet by its maximum
Johnson distance from the protected entrance target.  A radius-\(h\) ball
has at most \(4h+2\) packet vertices, while the farthest pair supplies the
factor \(5/[\binom Rh\binom{n-R}h]\).  Summing the diameter ranges gives
the displayed bound uniformly for \(p=O(\log m)\).  Thus the twin
near-factor question has no remaining time-zero mixed-diagram gate; only
the stopped/hereditary regeneration of these bounds is open.  See
`MATH_THEOREM_DOMINO_TWIN_FACTORIAL_OVERLAP_BOUND_20260727.md` and
`MATH_AUDIT_DOMINO_TWIN_FIRST_ACLE_AND_K25_OVERLAP_GATE_20260727.md`.
Dynamic regeneration and compensated repeat control remain open.  See
`MATH_AUDIT_PIPPENGER_SPENCER_GROWING_UNIFORMITY_CLAIM_20260726.md` and
`MATH_AUDIT_ANNULAR_PACKET_SLOW_BITE_AND_SHARED_LEAVE_20260727.md` and
`MATH_AUDIT_ANNULAR_REPEAT_EXCESS_LOCAL_COMPATIBILITY_AND_POISSON_GATE_20260727.md`.

The full-history configuration system has a substantial local positive
theorem.  Any closed odd-port subsystem on

\[
 \exp\{o(\sqrt{m\log m})\}
\]

roots admits pairwise target-disjoint literal histories.  More precisely,
the repair radius is at least
\(\exp((\log2/4-o(1))\sqrt{m\log m})\).  Total unimodularity is false: an
actual six-history, three-root triangular prism has a half-integral point
and no integral collision-free choice within those six columns.  The prism
is not closed, so it is repairable from the full fibres.  A counterexample,
if one exists, must therefore be a genuinely global fibre-dense port mesh.
See `MATH_ATTACK_O_CCTPF_FULL_HISTORY_ODD_PORT_AND_REPAIR_20260726.md`.

Two proposed deterministic globalizations are now ruled out in their
natural forms.  In the two-SCD lane, predecessor-root rigidity makes every
one-letter duplicate-head diagonal seam impossible; a half-splice with
bounded provider holonomy exists algebraically, but does not supply the
physical seam.  In the anchored two-orbit lane, suppressing cross-sector
histories forces at least \((0.0962+o(1))W\) paired deficiency, while
independent class motion creates a linear collision floor.  Multi-letter
seams and exceptional targetwise correlated alignment remain open.  See
`MATH_OBSTRUCTION_N_TWO_SCD_DIAGONAL_FORK_AND_HALF_SPLICE_20260726.md`
and `MATH_THEOREM_W_ANCHORED_TWO_ORBIT_PAIRED_QUOTIENT_STATEWISE_GATE_20260726.md`.

Finally, the formerly claimed unconditional repaired-ring slow-bite
trajectory is retracted.  The multiplicity hierarchy correctly handles a
repeated next edge, but its finite moving buffer does not control the top
strip during a checkpoint of length \(\Theta(m)\).  The compensation-coin
square generator can request an energy two orders beyond the recorded top;
the resulting normalized top growth can be \(\exp(\Theta(m))\), larger than
the \(\exp(-\Theta((\log m)^2))\) buffer attenuation.  The surviving
conditional theorem is exact: weighted bad-owner quarantine plus the mixed
diagonal link-energy/boundary-flux hierarchy (MDLE) yields an \(o(N_H)\)
root leave and hence \(o(W)\) owner loss.  MDLE itself is unproved.  See the
retraction at the head of
`MATH_THEOREM_REPAIRED_RING_GROWING_UNIFORMITY_SLOW_BITE_TRAJECTORY_20260726.md`
and the pending July 27 buffer audit.

The completed July 27 audits reveal a second, independent buffer defect.
For an aggregate energy \(Y=\sum_Cw_CA_C^h\), its quadratic variation
depends on the column sums

\[
 Z_Y(g)=\sum_Cw_CA_C^{h-1}B_C(g),
 \qquad \sum_g Z_Y(g)^2,
\]

where the same next edge \(g\) may hit many different depleted clusters.
The available one-row power bounds control \(\sum_{C,g}B_C(g)^\ell\),
which does not bound these column moments; an explicit biregular breadth
model separates them.  The exact sufficient replacement is ACLE, an
incidence-weighted aggregate column-link energy hierarchy, or equivalently
a full mixed row-column diagram buffer.  Moreover inverse/direct
factorially weighted infinite-order norms do not close: damping the upward
generator is incompatible with the exact order-\(\Theta(m)\) private-star
spine already present initially.  See
`MATH_AUDIT_BUFFERED_SLOW_BITE_COLUMN_ENERGY_OBSTRUCTION_20260727.md`,
`MATH_AUDIT_REPAIRED_RING_BUFFERED_STOPPED_GENERATOR_ESCAPE_20260727.md`,
and `MATH_AUDIT_WEIGHTED_RPRN_BUFFERED_DIAGONAL_GENERATOR_20260727.md`.

The first literal breadth term is nevertheless positive.  For fixed owner
\(X\), the conflict-incidence graph between link options through \(X\) and
next edges has left degree at most \(L=K\Delta_t\) and stopped right degree
at most \(A\).  A tree-homomorphism count gives, for all \(h,\ell\ge1\),

\[
 \sum_g\left(\sum_ea_X(e)^{h-1}b_X(e,g)\right)^\ell
 \le d_XL^{\ell+1}A^{h\ell-1}.
\]

Thus the missing column moments have exactly the desired normalized factor
\((A/d_X)^{\ell-1}\); protected-index removals obey the same estimate.
The ACLE gate has narrowed to regeneration of the high influence moment
\(A/d_X=O(\operatorname{polylog}m/m^2)\), including the compensation
columns.  See
`MATH_THEOREM_FIRST_COLUMN_BREADTH_ENERGY_REPAIRED_RING_20260727.md`.

The first drift-coherence cycle also has the favorable scale.  The
leaf--leaf witness diagram is \(K_{2,2}\); closing its fourth incidence
forces one additional endpoint gap and gives

\[
 \sum_{e,g}^{*}b_X(e,g)^2
 \le C L^2d_X^2\alpha^2,
 \qquad \alpha=A/d_X.
\]

Its normalized \(J\)-moment drift cost is \(O(J^2\alpha)=o(1)\).  The
larger forced centre--leaf common-neighbourhood term costs only
\(O(J/K)=o(1)\), and compensation-resource columns have the same first
cycle scale.  Thus neither the first breadth tree nor the first coherence
cycle is a literal obstruction.  See
`MATH_THEOREM_FIRST_C4_DRIFT_COHERENCE_SCALE_20260727.md`.

The complete **static** mixed-diagram hierarchy is now proved.  If a
row--column diagram has formal-row count (a), nonempty-column count
(c), and excess

\[
 \omega=(\text{witness incidences})-c,
\]

then row exploration gives

\[
 Z_\Gamma(X)
 \le d(X)^a(KD)^c
 \left({C(\omega+1)^4\over m^2}\right)^\omega.
\]

Each newly exposed row is charged simultaneously against all its old
resource-disjoint columns by the path-mesh maximum; each column introduced
there is charged by the internal census.  Every column has exactly one
free incidence, so the exponent is identically \(\omega\).  This covers
theta and arbitrary overlapping-cycle cores without an unproved holonomy
independence; equality partitions are paid by unused factorial row degree.

The dynamic hierarchy also has a graded moment simplex.  A (q)-th jump
moment of an excess-(r) core can be truncated to excess below
(q(2r+1)).  Choosing

\[
 q(r)=\min\{J,\lfloor L/(2r+1)\rfloor\}
\]

keeps every requested moment inside the moving buffer regardless of one
new column's raw incidence.  Full (J)-th moments hold low in the buffer
and quadratic variation through its lower three quarters.  The sole
remaining stochastic boundary is an incidence-weighted **first-moment
quarantine for the graded top strip**; the broad ACLE outer-flux and
recursive row-count gates have been removed.  See
`MATH_THEOREM_STATIC_MIXED_DIAGRAM_EXCESS_AND_DYNAMIC_OMEGA_BUFFER_20260727.md`
and `MATH_AUDIT_THETA_CORE_AND_GRADED_MOMENT_BUFFER_20260727.md`.

The first proposed quarantine proof does not yet close this boundary.
After exposing all but the last physical row, a mixed count has the form
\(Z=\sum_C w_CA_C\).  Exact compensation combines terminal death of the
prefix \(P_C\) with loss of a last-row option \(S_f\) into the joint hazard
of \(P_C\cup S_f\).  Existing estimates control \(J(P_C)\) and \(J(S_f)\)
separately, but not the cross-prefix term

\[
 \sum_{C,f}w_C\bigl[J(P_C\cup S_f)-J(P_C)-J(S_f)\bigr].
\]

This is precisely a new degree-two column joining the exposed prefix to
the last row, hence an excess-\((r+1)\) aggregate first-moment link term.
Merely using the sign of terminal deletion is insufficient against a
negative reference drift.  Thus the attractive
\(\exp[-\Theta((\log m)^3)]\) quarantine arithmetic is conditional on one
exact **cross-prefix q=1 ACLE** estimate; equality resolution alone does
not supply it.  The status correction is in
`MATH_THEOREM_AGGREGATE_FIRST_MOMENT_TOP_STRIP_QUARANTINE_20260727.md`.

A finite-order tail calculation clarifies exactly what heredity must buy.
For a fixed set of \(a\) resource-disjoint physical arms and current pair
spread \(\delta_t=\Delta_{2,t}/\Delta_t\), the common-edge fraction is

\[
                         \beta_E\le aK\delta_t.
\]

If \(a=O((\log m)^2)\) and \(\delta_t=O(m^{-2})\), then
\(T\beta_E=O((\log m)^3)\), and a sufficiently large polylogarithmic
initializer makes the chronological tail summable.  But this is not
hereditary: an explicit deletion-reachable pair-star residual has
\(\beta_E=\Theta(1)\) after equality resolution, and near-coincident rows
can have coin fraction \(1-o(1)\).  If protected extension columns are
allowed to become new arms, the arm count grows with the tower level and
the Duhamel majorant eventually expands by \(\Theta(\log m)\) per level.
Thus the ordered-column repair is valid only under a new hereditary
pair-spread plus full coin-fibre theorem; it does not close the present
process.  See
`MATH_THEOREM_FINITE_ORDER_EDGE_BETA_TAIL_AND_ARM_GROWTH_NOGO_20260727.md`
and
`MATH_AUDIT_PAIR_COLUMN_TAIL_BETA_AND_PAIR_STAR_OBSTRUCTION_20260727.md`.

Accordingly the two sharpest live gates are now:

1. **Dense physical collision lift:** turn the proved near-flat integer
   load and zero-collateral rectangle lattice into one legal table by
   chronologically composing \(\Theta(W)\) swaps with average
   \(\Theta(m)\) top reuse, or construct a different starting coefficient
   already close to the low-collision fibre.
2. **Top-strip stochastic cleaning:** prove the cross-prefix q=1 ACLE
   above (or a nonrecursive substitute), and then use the static
   \(\alpha^r\) slack to quarantine only \(o(N_H)\) roots.

Either gate would close a full coefficient-one compiler already audited
outside that gate.  Neither is currently proved.

# July 27 latest update: local rerooting and static annular overlap are closed

The dense physical lift has advanced past its local-capacity and abstract
support questions.  The explicit three-top reroot packet has now been
independently audited: its matched cuts cancel every protected length
coefficientwise, complementation commutes with the three-top telescope, both
middle shores are squarefree with the same owner support, and one focal top
has (m-O(H)) genuinely different rooted rectangle directions.  Moreover the
abstract packet hypergraph on rank-(M) tops is 3-uniform with

\[
 D=\binom M2(2m-M),\qquad \Delta _2=M-1.
\]

Here fixed-uniformity Pippenger--Spencer is legitimate.  Combining one
near-perfect packet matching with (cm) coordinate relabelings gives
\((1-o(1))cmN\) distinct exchanged-pair incidences, so almost every top has
\(\Theta(m)\) abstract reroot directions.  Thus neither local chronology nor
top support is the remaining obstruction.

There is, however, a new exact global invariant.  If (C_{j,v}) denotes the
number of current top words carrying label (v) in rooted position (j),
then every three-top reroot packet and every collar-neutral boundary rectangle
preserves the whole matrix \((C_{j,v})\).  A reroot packet is three coupled
two-by-two switches, equivalently an alternating six-cycle in the top--label
incidence graph.  The exact deterministic gate is therefore one
coefficient-one chronology inside a fixed column-histogram fibre, with the
owner capacities respected at every prefix.  See
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`
and
`MATH_AUDIT_REROOT_CONVEYOR_FUSION_COLUMN_INVARIANT_AND_DENSE_SUPPORT_20260727.md`.

The claimed black-box growing-uniformity annular nibble is not available.
Classical Pippenger--Spencer and Alon--Kim--Spencer fix the edge uniformity;
their constants are not uniform for (K=\Theta(m)).  The actual
growing-uniformity hypotheses are constant-critical here.  For ordinary
packets

\[
 {K\Delta _2\log N\over D}=8\log2+o(1),
\]

and for domino twins

\[
 K_\square=4m,\qquad
 {\Delta _2^\square\over D^\square}={5+o(1)\over m^2},\qquad
 {K_\square\Delta _2^\square\log N\over D^\square}
   =40\log2+o(1).
\]

Thus Grable's required little-oh condition fails, while Vu's fixed-(K)
power \((D/\Delta _2)^{-1/(K-1)}\) is (1-o(1)).  The favorable annular
geometry is still real: the complete static factorial-overlap hierarchy

\[
 \sup_{X,F}{1\over D}\sum_{F'\ni X}(|F\cap F'|-1)_p
 \le (Cp)^{Cp}m^{-2},\qquad p\le C_0\log m,
\]

is proved.  The annular near-factor now has exactly one stochastic gate:
regenerate this hierarchy hereditarily along a stopped slow-bite trajectory.
See `MATH_AUDIT_DOMINO_TWIN_PS_GROWING_UNIFORMITY_20260727.md` and
`MATH_THEOREM_DOMINO_TWIN_FACTORIAL_OVERLAP_BOUND_20260727.md`.

The two current endgame gates are consequently sharper than the preceding
list:

1. **Latin/six-cycle chronology:** connect the required low-collision load
   inside the conserved \((C_{j,v})\)-fibre while keeping middle ownership
   coefficient one at every prefix.
2. **Stopped factorial-overlap regeneration:** prove the hereditary dynamic
   analogue of the already-complete static domino-twin overlap bounds.

Both are full theorems, not routine lemmas.  The first is deterministic and
the second stochastic; all presently known local, marginal, collar, and
time-zero obstructions outside them have been discharged or isolated.

# July 27 second update: bounded recharge and all-scale annular quarantine

The local position-component obstruction in the deterministic lane is now
closed.  A twelve-top bidirectional recharge pairs a forward six-cycle with a
backward six-cycle on two edge-disjoint Hamilton cycles of six outside
labels.  After a necessary audit correction--both the (F)- and (G)-context
palettes must use the same proper edge-colouring--the packet has squarefree
shores, identical middle-owner support, zero derivative at every protected
length, and unchanged rooted position--label histograms.  It transports
labels across adjacent rooted positions and therefore connects the admitted
position graph locally.  The first vertex-indexed palette version was false:
it created six duplicate middle owners per shore; the repaired theorem has
been checked independently.

The simple top-packet hypergraph for this recharge is 12-uniform and regular,
with

\[
 {\Delta _2\over D}={6\over M(2m-M)}=O(m^{-2}).
\]

Fixed-uniformity Pippenger--Spencer edge-colouring therefore supplies
\(\Theta(m)\) near-perfect top layers and \(\Theta(W)\) abstract packet
incidences.  A parallel root-port-flag formulation is fixed 6-uniform and
gives almost every top \(M-o(M)\) directed port incidences.  Thus local
position connectivity, raw top supply, and the factor-(m) abstract reuse
shortage are all solved.  The deterministic gate is now strictly physical:
coalesce the port incidences into compatible trails and install successive
source words with globally disjoint middle-owner resources.  See
`MATH_THEOREM_TWELVE_TOP_HISTOGRAM_NEUTRAL_BIDIRECTIONAL_RECHARGE_20260727.md`,
`MATH_AUDIT_TWELVE_TOP_RECHARGE_SQUAREFREE_REPAIR_AND_TOP_PACKING_20260727.md`,
and
`MATH_AUDIT_TRIPLE_PRODUCT_CELL_ABSTRACT_RECYCLING_AND_ROOT_PORT_OBSTRUCTION_20260727.md`.

The annular lane now has an explicit all-scale quarantine rather than only a
negative generator audit.  Join two simple domino-twin packets when their
supports overlap in more than (K-s) resources.  The first trace count gives

\[
 \Delta(\Gamma_s)\le e^{Cn}n^{3s}.
\]

Random local-minimum thinning has a realization which is simultaneously
near-regular at every entrance target, keeps relative pair codegree
\((5+o(1))/m^2\), preserves asymptotically full fractional factor capacity,
and removes every overlap above (K-s).  For (s=o(m)) its degree still has
logarithm \((2-o(1))m\log m\).  The current exponent (3) is not sufficient
for the survivor tilt, but the remaining inverse problem has a much sharper
paired-cycle normal form.  A twin packet is a cyclic order of (m) unordered
dominoes and a disjoint union of (m) four-target cells.  Overlap at least
(K-s) forces at least (m-s) identical cells, one global dihedral
alignment, and all but (O(s)) literal domino positions fixed.

There is also a matching lower calibration.  Arbitrarily repartitioning one
contiguous segment of (ell) domino positions gives at least

\[
 {(2\ell)!\over2^\ell(2m)}
\]

different packets while changing at most (8\ell+8) targets.  Consequently
the sharp close-neighbour exponent (c) in

\[
 \#\{G:|F\cap G|\ge K-s\}\le e^{O(m)}n^{cs}
\]

must satisfy (c\ge1/4), while stopped survival needs (c<1/2).  The exact
annular inverse-stability window is therefore

\[
                         \boxed{1/4\le c<1/2.}
\]

The only configurations blocking the immediate (c=1/3) charge are now
identified as star-to-top shared-edge coincidences.  Proving the corresponding
local list-decoding theorem, followed by the incidence-weighted stopped
covariance estimate, is the current annular route.  See
`MATH_AUDIT_DOMINO_TWIN_STOPPED_FACTORIAL_GENERATOR_AND_MACRO_OVERLAP_GATE_20260727.md`
and
`MATH_THEOREM_MACRO_OVERLAP_QUARANTINE_BY_CONFLICT_THINNING_20260727.md`.

# July 27 third update: independent audit of the claimed one-third zipper

The proposed inverse-stability estimate

\[
 \#\{G:|F\cap G|\ge K-s\}\le e^{Cm}n^{s/3}
\]

is **not yet a verified theorem**.  The cell normal form, the star/top census,
the weak-cell defect of at least three, and the global dihedral alignment on
complete cells survive audit.  What does not yet survive is the global inverse
step: the paired sliding recurrences identify whole dominoes but do not by
themselves prove (i) alignment of noncomplete edge anchors across gaps or
(ii) that at most one genuinely free label can be charged injectively to each
weak cell.  These two statements are exactly the missing content of the
claimed zipper lemma; they cannot be replaced by restating the recurrence.

There is a second independent correction.  Even if the list bound with
exponent (c<1/2) is granted, the first allowed survivor shell is not killed by
the raw catalogue count alone.  With an unthinned shell degree of order
(D_s\asymp D/(e^{Cm}n^{cs})), normalizing at residual density
(z=m^{-1/2}) reverses the advertised sign.  The desired negative exponent is
available only after a shell-equitable thinning which reduces the incident
shell and the ambient degree in the correct proportional way.  Therefore the
two annular subgates are now:

1. prove the actual inverse decoder with some exponent (c<1/2); and
2. prove a retained-shell/equitable quarantine theorem which converts that
   decoder into a hereditary stopped bound.

The self-audited one-third note remains a candidate proof, not a result.  The
independent verdict is recorded in
`MATH_AUDIT_DOMINO_TWIN_INVERSE_STABILITY_C_ONE_THIRD_20260727.md`.

## Correction: the one-third target is actually false

A subsequent adversarial construction turns the preceding proof gap into a
sharp obstruction.  In the annular parametrization

\[
 2r=m-h,\qquad h=\Theta(\sqrt m),
\]

take two length-(\ell) domino segments whose initial indices differ by (r),
and repartition the labels inside the two segments independently.  The two
remote bands of changed core fronts are displaced by

\[
 2r\equiv-h\pmod m,
\]

so for (\ell\gg h) they overlap almost completely.  The family has size at
least

\[
 {1\over2m}\left({(2\ell)!\over2^\ell}\right)^2,
\]

while at most

\[
 s_\ell=8\ell+4\min\{\ell,h\}+O(1)
\]

targets are lost.  Taking (\ell=m/\sqrt{\log m}) gives close-neighbour
exponent (1/2-o(1)).  Consequently **no** uniform raw-defect estimate

\[
 \#\{G:|F\cap G|\ge K-s\}\le e^{O(m)}n^{cs}
\]

can hold with fixed (c<1/2), even in the intended Gaussian annulus.  The
local deferred-mate charge at ratio (1/3) is genuine but nonadditive across
the two aligned corridors.  The annular inverse-stability target is therefore
retired, not merely left open.  See
`MATH_OBSTRUCTION_GLOBALLY_ALIGNED_DOUBLE_SEGMENT_DOMINO_ENTROPY_20260727.md`
and
`MATH_COUNTEREXAMPLE_DOMINO_TWIN_ZIPPER_UNIFORM_RADIUS_20260727.md`.

There is nevertheless a useful exact repair to the thinning calculation.
For a regular conflict graph of degree (\Delta), random-priority local-minimum
thinning with (p=1/(\Delta+1)) satisfies, for every nonconflicting pair,

\[
 \Pr(F,G\hbox{ both retained})
 = {2\over(\Delta+1)(\Delta+a+2)}\le2p^2,
\]

where (a) is the number of neighbours unique to either endpoint.  A
polynomial-threshold alteration therefore makes every retained defect shell
proportional to (p) while losing only (o(1)) of the retained packets and only
(o(N)) entrance targets.  This restores the correct one-list-factor survivor
normalization, but the double-segment family sits exactly at its exponent
(1/2), so no asymptotic decay follows.  The new annular gate is structural:
quotient the critical corridor clusters, or prove that the actual stopped
trajectory encounters only (o(W)) incidence from them.  The corrected
normalization is in
`MATH_AUDIT_DOMINO_TWIN_MACRO_SHELL_NORMALIZATION_AND_EQUITABLE_THINNING_20260727.md`.

## Stronger annular verdict: literal twins cannot feed the compiler

The critical-cluster issue is superseded for the direct twin architecture by
an exact first-shadow obstruction.  Split each selected domino twin into its
two ordinary cyclic packets (P) and (P^\tau).  At an odd entrance length (r)
their entrance decks are disjoint.  At the first deeper, even length (r-1),
the (m) intervals with endpoints on domino boundaries occur in both decks,
independently of the internal orientation.  Thus a twin matching covering
(G=N_0-L) entrance targets has first-shadow repeat excess

\[
 E_1\ge {G\over4},
\]

and, after subtracting the scalar floor,

\[
 \widetilde E_1\ge {N_0-L\over4}-O_a(W/\sqrt m).
\]

For (L=o(W)) this is (\Omega(W)).  Neither an (o(W))-incidence quarantine nor
an (o(W))-length PBBS appendage can repair it.  Therefore a domino-twin
near-factor, even if constructed perfectly, does **not** establish the
annular input needed for constant one.  Its only possible surviving use is a
global rebundling theorem which repartitions almost all retained entrance
roots into new, non-twin ordinary histories.  Internal orientation choices
do not count as such a rebundling.  See
`MATH_THEOREM_DOMINO_TWIN_ANNULUS_PBBS_COMMON_LEAVE_INTERFACE_20260727.md`.

Accordingly, the direct twin matching/quarantine lane is retired from the
endgame.  The live stochastic target returns to the ordinary-frame catalogue.
There the integral incidence lattice is saturated and the pair-profile and
whole-arm stopped estimates are proved.  The remaining stochastic boundary is
an all-order profile problem: the pair stop is controlled before a natural
triple-fibre stop, but controlling that stop introduces fourth fibres, and so
on.  A finite hierarchy merely moves the boundary.  The appropriate next
object is one joint factorial/exponential profile energy whose child-fibre
cost contracts across all orders and terminates at complete edges.

### Audit of the all-order profile proposal

The naive scalar all-order completion is now ruled out.  A factorial EGF does
indeed close formally under the conditional child estimate

\[
 \sum_w q_{k+1}(S\cup\{w\})\le {C\over m}q_k(S)
\]

at every order.  The actual ordinary-frame catalogue does not satisfy that
hypothesis.  Along a literal consecutive profile spine the aggregate child
kernel equals (\Theta(1/m)) only for (k<H); for

\[
 H\le k<m
\]

it is (\Theta(1)).  The transition occurs exactly at the collar width
(H=\Theta(\sqrt{m\log m})).

More strongly, suppose a positive scalar energy
(\Phi=\sum_k a_kE_k) pays every order-(k) positive boundary with its one-level
child.  Over the square-root-density time interval, the post-(H) spine forces

\[
 a_{k+1}\ge c\,m\log m\,a_k.
\]

The exact terminal spine mass is
(\exp[-m\log m+O(m)]), so the initialized terminal contribution then grows
like (\exp[(1+o(1))m\log\log m]).  No positive scalar weight sequence can
both absorb the full (+1) hierarchy and have a finite initialized norm.

Thus the pair-to-triple stopped estimate remains useful, but its boundary
cannot be removed by another scalar factorial EGF.  A successful stochastic
proof must instead use compensation to cancel the (+1) shift, retain the
two-shore/gap geometry in a multidimensional energy, or prove a direct
trajectory theorem for the triple-profile stop.  See
`MATH_THEOREM_ALL_FIBRE_EGF_PROFILE_STOP_QUARANTINE_20260727.md` for the
conditional calculation and
`MATH_NOGO_ALL_ORDER_PROFILE_ENERGY_CONSECUTIVE_SPINE_20260727.md` for the
physical counter-audit.

Two narrower escapes from that no-go are now isolated.

First, one may stop at

\[
 J=\lceil(\log m)^2\rceil=o(H).
\]

The proved static higher-codegree bound through (J) makes the total
time-zero mass of all relevant terminal (J)-profiles reachable from one
marked incidence at most

\[
 \left({CJ^2\over m}\right)^{J-1}
 =\exp[-(1-o(1))(\log m)^3].
\]

A trajectory-specific Doob quarantine can therefore pay the terminal layer
directly.  This reduces the stochastic target to a uniform one-step stopped
estimate only for orders (2,\ldots,J-1); it does not require a pointwise
terminal theorem for arbitrary residuals and never enters the post-(H)
spine.  See
`MATH_REDUCTION_LOGSQUARED_TRAJECTORY_PROFILE_CUTOFF_20260727.md`.

Second, the apparent order-one child mode has an exact algebraic
decomposition.  For every active (k)-profile (S),

\[
 \sum_a d_t(S\cup\{a\})=(r-k)d_t(S).
\]

With time-zero child weights (p_{S,a}) and natural normalized link ratios,

\[
 \sum_ap_{S,a}X_{S,a}=uX_S.
\]

Hence the constant child mode is parent-determined.  After centering it, the
categorical covariance operator is
(\operatorname{diag}(p)-pp^{\mathsf T}); on the exact post-collar
consecutive spine its norm is (O(1/(m-k))), even though the positive
(\ell^1) kernel is one.  This opens a genuinely different Hilbert/two-shore
route.  Its remaining gate is to prove that the compensated physical jump
covariance respects this centered operator.  See
`MATH_LEMMA_CENTERED_CHILD_PROFILE_COVARIANCE_20260727.md`.

The first compensated finite-cutoff formulation also required a correction.
Subtracting the linear mean removes the raw (+1) transport, but a quadratic
Taylor term can repeat the same child resource.  A compensation coin at (a)
contributes

\[
 \chi_t(a)\,d_t(S\cup\{a\})^2,
\]

which has only one new physical resource and is therefore a repeated-child
(+1) diagonal.  The correct truncated generator contains

\[
 \delta_{s+1}\mathscr E_{s+1}
 +\sum_{\ell\ge2}A^\ell\kappa_{s+\ell}^{\ell-1}
  \mathscr E_{s+\ell}.
\]

The geometric cutoff still works if

\[
 {\mathcal T\over\theta}\max_{t\le J}\delta_t=o(1),
\]

and in particular if (\delta_t\le m^{-1+o(1)}) for
(J=(\log m)^2).  This is now the exact finite stochastic census gate.
On the dangerous consecutive spine the centered covariance calculation gives
(\delta=O(1/(r-k))), so the raw unit mode is genuinely gone; what remains is
to prove the same squared-codegree bound for every equality-resolved
column--row and compensation orbit through polylogarithmic order.  See
`MATH_AUDIT_COMPENSATED_PLUS_TWO_CUTOFF_REPEATED_CHILD_DIAGONAL_20260727.md`
and
`MATH_AUDIT_COMPENSATED_CONSECUTIVE_SPINE_CENTERING_AND_VARIANCE_20260727.md`.

The repeated-child coefficient itself is now discharged by a pathwise reverse
sum.  If (A_a=d_t(S\cup\{a\})) and selected edges ring at rate
(1/(r\Delta_t)), then in every induced residual

\[
 {1\over r\Delta_t}\sum_g\sum_{a\in g}A_a^2
 = {1\over r\Delta_t}\sum_a d_t(a)A_a^2
 \le {1\over r}\sum_aA_a^2.
\]

The compensation clocks contribute at most the same amount.  Hence the
physical (+1) repeated-child diagonal has coefficient

\[
 \delta_{k+1}\le {2\over r}=O(1/m)
\]

uniformly in the profile order and current state.  Its integrated weighted
cost in the logarithmic-square cutoff is

\[
 {\mathcal T\over\theta}\delta
 =O(\sqrt{\log m/m})=o(1).
\]

Thus the compensation-coin correction no longer blocks the finite profile
route.  The sole remaining stochastic generator input is the
equality-resolved **distinct-child** census through total order
((\log m)^2), plus an aggregate terminal type count.  See
`MATH_THEOREM_REPEATED_CHILD_DIAGONAL_ONE_OVER_R_20260727.md`.

An immediate normalization audit prevents overclaiming this last step.  The
raw reverse sum is exact, but converting it to the natural level-(k+1)
profile energy inserts

\[
 \left({\mu_{S\cup a}\over\mu_S}\right)^2,
\]

which may be as large as (u^{-2}) for a rare child fibre.  Hence
(\delta\le2/r) is not yet established in the literal stopped-incidence norm.
The true remaining statement is an incidence-averaged version of the reverse
sum, or an exact generator inequality for the centered variance

\[
 \sum_ap_{S,a}(X_{S,a}-uX_S)^2.
\]

The raw identity and the spine spectrum show where the needed gain can come
from; they do not yet complete its normalization.

On the deterministic side, the owner-aware census of the repaired twelve-top
packet is complete.  All higher codegrees admit the exact orbit formula

\[
 d(\Omega)={E\,a_\Omega(P)\over|\Omega|},
\]

the maximum relative pair codegree is (O(m^{-2})), and logarithmic factorial
overlaps satisfy the same static bound as the twin catalogue.  Nevertheless
the augmented edge size is (\Theta(m)), and

\[
 K{\Delta_2\over d_{\min}}\log V_{\rm aug}\ge48\log2-o(1),
\]

so this catalogue too is constant-critical for the usual growing-rank bite.
The new positive fact is deterministic: a source bank using only (15n) tops
and (15nd) owners realizes every requested position-three label, and can be
installed after quarantining only (O(m^2)) rows and (O(m^3)=o(W)) owner
incidences.  This proves that broad local source support is asymptotically
cheap.  The remaining deterministic gate is the coefficient-one owner
near-factor/chronology into which that bank must be installed.

The atomic-to-path lift is now known to fail by a linear margin.  One may
choose (d) contained owners which are independent in the Johnson graph of
deleted (H)-sets; every literal length-(d) cyclic deck then replaces at least
(\lfloor d/2\rfloor=\Theta(m)) of them.  There is also an explicit
three-top/two-deck odd-cycle gadget whose path LP has the half-half solution
and whose atomic owner allocation is integral, but which has no integral
grouped deck choice.  Thus neither robust Hall flow nor generic alternating
paths can supply the physical lift.

For a current coefficient-one word table, the exact carrier graph (G_C) of a
fixed common context (C) records which exterior pairs occur as legal rows.
Its total edge count is (MN), with mean

\[
 {s(s-1)\over M-1}=(s-1)-\Theta(H),
\]

which lies below the forest threshold.  A reroot-only twelve-top bank obeys

\[
 2|\mathcal B|\le\sum_C\beta(G_C),
\]

where (\beta) is cycle rank.  Consequently the shortest positive
deterministic theorem is extensive **decorated** carrier-cycle rank, including
the word/palette compatibility of each cycle.  Conditional on such a bank,
the owner mass changed is only ((4H-1)N=o(W)).  See
`MATH_THEOREM_GROUPED_OWNER_PATH_LINEAR_GAP_ODD_CYCLE_AND_REROOT_CYCLE_RANK_20260727.md`.
