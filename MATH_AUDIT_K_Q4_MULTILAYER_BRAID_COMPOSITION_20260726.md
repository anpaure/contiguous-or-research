# Audit and composition theorem for the syndrome \(Q_4\) braid bank

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

Sources audited:

* MATH_THEOREM_SYNDROME_SUSPENDED_Q4_BRAID_COMPONENT_BANK_20260726.md;
* MATH_THEOREM_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md;
* MATH_AUDIT_Q4_COMMON_PHASE_BLOCK_TRANSPOSITION_20260726.md; and
* MATH_OBSTRUCTION_REPLICATED_Q4_BRAID_OCCURRENCE_LP_20260726.md.

## 0. Verdict

The repaired one-layer theorem is correct, with the scope stated in the
syndrome-bank source. One layer is a perfect matching of the syndrome
cycle labels by

\[
                         k\longleftrightarrow k+\delta,
\]

and a shore bit may be chosen independently on every such pair. The bit
must be constant at the two endpoints of the pair. This condition is both
necessary and sufficient. The two-cycle component has \(4h\) actual
owners, not merely two formal direction words.

There is an exact positive multilayer theorem. In the standard
parity-alternating syndrome factor, take

\[
 (a_j,b_j)=(4j,4j+2),\qquad 0\le j<r:=h/4.             \tag{0.1}
\]

All these coordinates lie in the same repeated-syndrome class. Put
\(\delta_j=e_{a_j}+e_{b_j}\). For every \(j\), independently choose an
arbitrary bit field

\[
 \epsilon_j:K_0\longrightarrow\mathbb F_2,
 \qquad
 \epsilon_j(k)=\epsilon_j(k+\delta_j).                \tag{0.2}
\]

No invariance under any \(\delta_\ell\), \(\ell\ne j\), is required.
Then

\[
 \sigma_k=\prod_{j=0}^{r-1}(a_j\ b_j)^{\epsilon_j(k)} \tag{0.3}
\]

defines an exact factor

\[
             \{\,\sigma_kP+k:k\in K_0\,\}             \tag{0.4}
\]

of \(Q_h\) into isometric \(C_{2h}\)'s, and every such factor has the same
global cyclic owner phase colouring.

This is a literal owner-overlapping composition, not a word-only
construction. The \(j\)-th layer partitions the current cycles into
two-cycle owner components and exchanges actual path segments inside each
selected component. Every layer uses the full cube owner set, so layers
overlap maximally in owners, although their two changed phase intervals are
disjoint.

If

\[
                         N=|K_0|={2^h\over2h},          \tag{0.5}
\]

then each layer has \(N/2\) independent bits and the \(r=h/4\) layers have
exactly

\[
                  {rN\over2}={2^h\over16}              \tag{0.6}
\]

independent bits. Hence the atlas contains exactly

\[
                         2^{\,2^h/16}                  \tag{0.7}
\]

distinct phase-coloured exact factors. This is \(h/8\) bits per syndrome
cycle, or exactly \(1/16\) bit per cube owner. It gives the requested
linear cycle-specific direction information rate.

The full overlay on cycle labels has components of size \(2^r\); it does
not force a uniform shore choice on such a component. The reason is that
the different matching dimensions occupy disjoint prefix-displacement
intervals. At every phase only one matching acts, so the phasewise Latin
condition factorizes exactly.

This theorem invalidates any extension of the one-bank occurrence cut that
keeps the \(O(1/h)\) action-density conclusion after \(\Theta(h)\) layers.
With all layer bits switched, exactly half of all directed owner tails
differ from the reference factor. It does not prove balanced lower/upper
shadow quotas, a protected collar, or the constant-one theorem.

## 1. What the one-layer sources actually prove

Let \(h=2^a\ge4\), \(V=\mathbb F_2^h\), and let
\(\Psi:V\to\mathbb F_2^a\) be the parity-alternating syndrome map in the
source. Its prefix syndromes are a transversal, and

\[
                         \Psi(e_{2t})=z                \tag{1.1}
\]

for every even coordinate. Let

\[
 K=\ker\Psi,\qquad
 p_i=e_0+\cdots+e_{i-1}\quad(0\le i<h).               \tag{1.2}
\]

The all-one vector lies in \(K\). For one repeated-column transposition
\(\tau=(a\ b)\), put

\[
                         \delta=e_a+e_b\in K.          \tag{1.3}
\]

Choose a linear functional \(\eta:K\to\mathbb F_2\) with

\[
 \eta({\bf1})=1,\qquad \eta(\delta)=0,\qquad K_0=\ker\eta. \tag{1.4}
\]

Then the reference cycles

\[
 P+k=(p_0+k,\ldots,p_{h-1}+k,
      {\bf1}+p_0+k,\ldots,{\bf1}+p_{h-1}+k),
 \qquad k\in K_0,                                    \tag{1.5}
\]

form an exact isometric factor. There are

\[
                         |K_0|={2^h\over2h}            \tag{1.6}
\]

cycles.

For a row-specific field \(\tau^{\epsilon(k)}\), the complete owner
condition is

\[
 \epsilon(k)=\epsilon(k+\delta)\qquad(k\in K_0).      \tag{1.7}
\]

Indeed, at a phase at which the prefix separates \(a\) and \(b\), the
owner-label map is

\[
                         k\longmapsto
                 k+\epsilon(k)\delta.                 \tag{1.8}
\]

On a \(\delta\)-pair, (1.8) is a permutation only for bit patterns
\((0,0)\) and \((1,1)\). The mixed patterns identify two inputs. At all
other phases the map is the identity. This proves necessity and
sufficiency, not merely sufficiency.

When (1.7) holds, a selected pair of old cycles and the corresponding pair
of transposed cycles have the same union of \(4h\) owners. Thus one layer
has \(|K_0|/2\) pairwise owner-disjoint components. Different layers on
different \(\delta\)'s do not have disjoint owner supports: each layer
uses every cycle and every owner. None of the four audited sources proved
that arbitrary choices in such overlapping layers compose.

There is a source-history point worth recording. The independent audit
correctly rejected the earlier undoubled row with direction word
\(1432\,1234\). The current theorem file has incorporated the repair and
uses \(1432\,1432\). The repaired table is isometric; the rejected table
is not. The syndrome-bank report uses only the repaired table.

Finally, common phase is not a full protected collar. The finite shores
already disagree on half of their depth-one targets. Every multilayer
conclusion below retains this caveat.

## 2. A simultaneous phase complement for all layers

Assume now \(h=2^a\ge4\). Since \(h\) is divisible by four, put

\[
                         r=h/4.                       \tag{2.1}
\]

For \(0\le j<r\), define (0.1) and

\[
 \tau_j=(a_j\ b_j),\qquad
 \delta_j=e_{a_j}+e_{b_j}.                           \tag{2.2}
\]

The supports of the \(\delta_j\)'s are pairwise disjoint. Equation
(1.1) gives \(\delta_j\in K\). Let

\[
                         D=\langle\delta_0,\ldots,
                                  \delta_{r-1}\rangle. \tag{2.3}
\]

Every vector in \(D\) vanishes on all odd coordinates, whereas
\({\bf1}\) does not. Hence \({\bf1}\notin D\). We may therefore choose

\[
 \eta:K\to\mathbb F_2,\qquad
 \eta({\bf1})=1,\qquad \eta(D)=0,                    \tag{2.4}
\]

and again set \(K_0=\ker\eta\).

For every \(j\), a bit field satisfying (0.2) defines an involutive
permutation

\[
 S_j(k)=k+\epsilon_j(k)\delta_j                    \tag{2.5}
\]

of \(K_0\). The invariance in (0.2) is exactly what makes \(S_j^2=1\).
No commutation between the different \(S_j\)'s will be used.

## 3. The disjoint-prefix-interval identity

For a coordinate transposition \(\tau_j=(a_j\ b_j)\), define

\[
 d_i(\tau_j)=\tau_jp_i+p_i.                         \tag{3.1}
\]

Because \(a_j<b_j\), direct inspection of the prefix gives

\[
 d_i(\tau_j)=
 \begin{cases}
  \delta_j,&a_j<i\le b_j,\\
  0,&\text{otherwise}.
 \end{cases}                                         \tag{3.2}
\]

In the present choice \(b_j=a_j+2\), so the nonzero interval is

\[
                         I_j=\{4j+1,4j+2\}.           \tag{3.3}
\]

The intervals \(I_0,\ldots,I_{r-1}\) are pairwise disjoint. The
transpositions \(\tau_j\) also have disjoint coordinate supports and hence
commute. Therefore, for \(\sigma_k\) from (0.3),

\[
 \sigma_kp_i+p_i=
 \begin{cases}
  \epsilon_j(k)\delta_j,&i\in I_j,\\
  0,&i\notin\bigcup_jI_j.
 \end{cases}                                         \tag{3.4}
\]

The important statement in (3.4) is not merely that the summands commute.
It is that at any fixed phase there is at most one nonzero summand. This
is why arbitrary cross-layer bit dependence is harmless.

## 4. Exact factor and common-phase theorem

### Theorem 4.1 (multilayer braid tiling)

For every family of bit fields satisfying (0.2), the cycles (0.4) are an
exact factor of \(Q_h\) into isometric \(C_{2h}\)'s. They all admit the
same owner phase map

\[
 c(x)=i+h\eta(x+p_i)\pmod {2h},
 \qquad \Psi(x)=\Psi(p_i).                           \tag{4.1}
\]

This phase map is independent of every \(\epsilon_j\).

#### Proof

At first-half phase \(i\), row \(k\) has owner

\[
 \sigma_kp_i+k=p_i+T_i(k),\qquad
 T_i(k)=k+\sigma_kp_i+p_i.                           \tag{4.2}
\]

By (3.4), either \(T_i\) is the identity or

\[
                         T_i=S_j                    \tag{4.3}
\]

for the unique \(j\) with \(i\in I_j\). Equations (0.2) and (2.5)
show that every \(T_i\) is a permutation of \(K_0\). Hence the rows
cover every owner in the phase class \(p_i+K_0\) exactly once. Their
antipodal halves cover \({\bf1}+p_i+K_0\) exactly once. The prefix
syndromes are distinct, so these \(2h\) phase classes partition \(Q_h\).
This proves exact ownership.

For a fixed row \(k\), the first-half direction at position \(a_j\) is
\(b_j\), and that at position \(b_j\) is \(a_j\), precisely when
\(\epsilon_j(k)=1\). All other directions retain their positions.
Thus the first-half direction word is the permutation \(\sigma_k\) of all
\(h\) coordinates, and the second half repeats the same word. The row is
therefore an isometric \(C_{2h}\).

Finally, (3.4) lies in \(D\), on which \(\eta\) vanishes. Thus a
first-half owner in (4.2) has colour \(i\) under (4.1), while its
antipode has colour \(i+h\). Every successor increases the colour by one,
including both half-seams. This proves the common-phase assertion.
\(\square\)

This proof is the complete phasewise Latin audit. It neither averages
owners nor identifies formal direction words without their translations.

## 5. Literal sequential owner trades

The preceding proof gives a final factor directly. The stronger fact is
that it can be reached by \(r\) successive literal braid layers, with every
intermediate state exact.

Let

\[
 \sigma_k^{(j)}=\prod_{0\le\ell<j}
              \tau_\ell^{\epsilon_\ell(k)},
 \qquad 0\le j\le r.                                \tag{5.1}
\]

Let \(\mathcal F^{(j)}\) consist of the rows
\(\sigma_k^{(j)}P+k\). Theorem 4.1, applied to the first \(j\) fields,
shows that every \(\mathcal F^{(j)}\) is exact, isometric, and has the
same phase map.

Fix the transition from \(\mathcal F^{(j)}\) to
\(\mathcal F^{(j+1)}\). Partition \(K_0\) into the pairs

\[
                         \{k,k+\delta_j\}.            \tag{5.2}
\]

The two endpoints have the same \(\epsilon_j\)-bit. If it is zero, leave
their two cycles unchanged. If it is one, transpose \(a_j,b_j\) in both
cycles.

We now check actual owners. At a phase outside \(I_j\), \(\tau_jp_i=p_i\),
and \(\tau_j\) commutes with every earlier \(\tau_\ell\), so the old and
new owner in a fixed row are identical. At a phase \(i\in I_j\), all
earlier displacement intervals are disjoint from \(I_j\). Consequently

\[
 \sigma_k^{(j)}p_i=p_i,\qquad
 \sigma_{k+\delta_j}^{(j)}p_i=p_i.                  \tag{5.3}
\]

The old owners in the paired rows are

\[
                         p_i+k,\qquad p_i+k+\delta_j, \tag{5.4}
\]

and the new owners are the same two owners in the opposite rows. The same
calculation holds in the antipodal half. Therefore

\[
 C_k^{(j)}\mathbin{\dot\cup}C_{k+\delta_j}^{(j)}
 =C_k^{(j+1)}\mathbin{\dot\cup}
       C_{k+\delta_j}^{(j+1)}                       \tag{5.5}
\]

as literal owner sets for every selected pair.

Equation (5.5) is the required componentwise completion statement. One
does not discard the portions of the two cycles outside the local
four-direction view. Inside a selected component the operation exchanges
the two phase arcs in \(I_j\); the two boundary edges change from directions
\(a_j,b_j\) to \(b_j,a_j\), and the antipodal exchange repeats it. Hence
the new cycles are precisely the repaired physical \(Q_4\) braid embedded
in the two current \(C_{2h}\)'s.

For a fixed \(j\), the pairs (5.2) partition all current cycles, so the
layer components are owner-disjoint. For different \(j\)'s the pairings
are transverse and the layers share owners. Thus the construction is a
composition on actual supports, not a tensor product of disjoint owner
blocks.

## 6. Exact information and overlay counts

The vectors \(\delta_0,\ldots,\delta_{r-1}\) are independent. Hence the
graph on \(K_0\) containing every layer matching is a disjoint union of
\(r\)-cubes, one on each coset of \(D\). It has

\[
                         {|K_0|\over2^r}              \tag{6.1}
\]

components. In one such cube, every edge in dimension \(j\) carries an
arbitrary switch bit; there are \(r2^{r-1}\) such edges. Globally the
number of free bits is therefore

\[
 {N\over2^r}\,r2^{r-1}={rN\over2}={2^h\over16}.      \tag{6.2}
\]

Different edge labellings give different phase-coloured factors. Indeed,
phase zero is outside every \(I_j\), so row \(k\) is anchored at owner
\(k\). Its outgoing direction at phase \(a_j\) is \(b_j\) rather than
\(a_j\) exactly when \(\epsilon_j(k)=1\). The final factor therefore
recovers every edge bit. This proves the exact state count (0.7), rather
than only a lower bound.

The full-overlay connectedness is not an indivisibility invariant. One
coset of \(D\) contains \(2^r\) cycles, yet it supports
\(r2^{r-1}\) independently chosen switches. The phasewise maps remain
permutations because dimension \(j\) acts only on \(I_j\).

There is also an exact action count. In one selected two-cycle component,
one layer changes eight directed successor tails: two boundary phases,
two antipodal halves, and two cycles. Boundary phase sets are disjoint
between layers, so these changed tails never cancel across \(j\). If
\(B\) is the total number of selected component bits, the final successor
map differs from the reference at exactly

\[
                              8B                       \tag{6.3}
\]

owners. With every bit selected,

\[
 B={rN\over2},\qquad
 8B=4rN={1\over2}(2hN)={2^{h-1}}.                   \tag{6.4}
\]

Thus the atlas reaches changed-edge density \(1/2\). The one-bank density
was \(2/h\).

## 7. Why arbitrary crossing layers do not follow for free

The positive theorem uses disjoint prefix-displacement intervals. It
does not prove an arbitrary Beneš network. There is a precise reason.

An elementary matching permutation has the form

\[
 S(x)=x+\epsilon(x)\delta,\qquad
 \epsilon(x)=\epsilon(x+\delta).                    \tag{7.1}
\]

If a second matching is

\[
 R(x)=x+\zeta(x)\gamma,\qquad
 \zeta(x)=\zeta(x+\gamma),                           \tag{7.2}
\]

and their prefix intervals cross, then removing the first layer while the
second remains active replaces \(S\) by the conjugate \(RSR^{-1}\). The
boundary is a physical \(\delta\)-boundary only if this conjugate is again
a \(\delta\)-matching. If one insists on closing the layer with the same
fixed matching \(S\), the exact condition is

\[
                              RS=SR.                 \tag{7.3}
\]

For independent \(\delta,\gamma\), direct comparison gives

\[
\begin{aligned}
 \epsilon(x+\zeta(x)\gamma)&=\epsilon(x),\\
 \zeta(x+\epsilon(x)\delta)&=\zeta(x)
\end{aligned}                                        \tag{7.4}
\]

as the exact commutation equations. Arbitrary pair bits do not satisfy
(7.4). Allowing a newly chosen matching at the exit weakens commutation to
the condition that \(RSR^{-1}(x)+x\in\{0,\delta\}\) for every \(x\), but
ordinary one-layer pair constancy does not imply even this weaker
condition. Therefore a claim that all crossing layers compose merely
because each layer separately satisfies its pair constancy is false.

The atlas above avoids this obstruction exactly: distinct nonzero phase
intervals never coexist, so no conjugation boundary occurs. Laminar
stack constructions provide another possible escape, and a genuine Beneš
network would have to route the conjugated matchings at every crossing.
Neither is needed for the linear-rate theorem proved here.

## 8. Consequences for the occurrence LP and precise scope

The replicated one-bank obstruction counts \(8q\) potentially affected
depth-\(q\) starts per selected component and

\[
                         {G\over4h}                  \tag{8.1}
\]

components in one layer. It is correct for that layer. Repeating it over
the present \(r=h/4\) exact layers gives only

\[
 8q\,{rG\over4h}={qG\over2},                        \tag{8.2}
\]

which is no longer an \(o(G)\) edit budget at any nontrivial depth. More
fundamentally, (6.4) exhibits a state with constant successor-action
density. Hence the logarithmic-depth cut in the one-bank report cannot be
cited against this multilayer atlas.

What is proved:

1. exact intermediate and final owner factors;
2. literal two-current-cycle support equality at every selected switch;
3. a common-support exact isometric \(C_{2h}\) factor and one common phase
   map for all states;
4. \(h/4\) mutually owner-overlapping repaired \(Q_4\) layers;
5. \(2^h/16\) independent switch bits and exact state count; and
6. constant, in fact \(1/2\), attainable changed-tail density.

What is not proved:

1. arbitrary \(S_h\)-valued row fields or a universal Beneš network;
2. equality of phase-resolved lower/upper collars;
3. satisfaction of the exact multi-depth occurrence-cover LP;
4. preservation of any additional external PBBS, \(X/Y\), port, or anchor
   ledger not encoded by owner and phase; or
5. coefficient one.

The exact new boundary is therefore positive: the syndrome \(Q_4\) bank
does compose on common owners at linear information and constant action
rate. The remaining gate is statewise shadow/collar selection inside this
explicit \(2^{2^h/16}\)-state atlas, not an exact-factor or ownership
composition gate.
