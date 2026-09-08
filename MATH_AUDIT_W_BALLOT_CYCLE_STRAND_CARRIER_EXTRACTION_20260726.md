# Ballot-forced cycle certificates versus strand and carrier demand

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web
input is used.

## 0. Verdict

The new ballot theorem supplies the right **order of raw material**, with
square-root slack:

\[
 M_r\ge {r-1\over(r+1)(r+2)}C_r
       =\left({1\over r}+O(r^{-2})\right)C_r
\tag{0.1}
\]

pairwise selected-edge-disjoint cycle certificates, whereas the stated
carrier demand is

\[
                         D_r^{\rm car}=\Theta(C_r/r^{3/2}).
\tag{0.2}
\]

Thus only an `Omega(r^(-1/2))` fraction of the raw bank is needed if every
retained certificate has constant useful carrier gain and serial closure
does not lose that gain.

This numerical comparison is favourable. It is not yet a construction.
The ballot theorem gives no positive lower bound for any of the following:

1. certificates whose selected edges lie on distinct old paths;
2. certificates whose toggle is a genuine alternating circuit of the full
   degree factor;
3. a jointly switch-stable bank;
4. serial aligned copies with cancelled phase-length cocycle; or
5. coherent full-carrier sign.

There is an exact local obstruction hidden between Items 1 and 2. Every
selected outgoing edge has one distinguished core for which the proposed
new half-edge is already the old down-successor edge. A directed certificate
is a clean distinct-strand circuit exactly when its cycle avoids all such
successor arcs. The ballot count permits, at the level of its proved
inequalities, one successor arc in the unique directed cycle of every
eligible core. Therefore it does not imply even one clean certificate.

**Correction.** Serial finite-order repetition does not promote a
nonidentity twisted packet in an ordinary fixed-exterior \(r\)-step slab.
For endpoints

\[
 O\cup P,\qquad O\cup(J\setminus\tau(P)),
\]

one has

\[
 d_J(O\cup P,O\cup(J\setminus\tau(P)))=|P\cap\tau(P)|.
\tag{0.3}
\]

An \(r\)-step geodesic therefore forces

\[
                         \tau(P)=P.
\tag{0.4}
\]

A later inverse twist cannot repair the defect because every contiguous
subpath of a geodesic is geodesic. Thus the phase-coboundary calculation
below is only an abstract path-length/ownership ledger in fixed exterior;
the former literal-factor conclusion is retracted.

The only surviving promotion target is an **exterior-moving** packet. If

\[
 |O_L|=|O_R|=m-r,\qquad e(P)=|O_L\setminus O_R|,
\]

then an \(r\)-step twisted slab is geodesic exactly when

\[
 \boxed{e(P)=r-|P\cap\tau(P)|=|P\setminus\tau(P)|.}
\tag{0.5}
\]

This equality must hold row by row, and the changed exterior forces a new
audit of every ambient state, ownership ledger, seam, and crossing collar.
Accordingly the ballot bank is only an abstract certificate supply. It
does not become a physical local engine through strand admissibility and
finite-order repetition alone.

## 1. Exact supply and square-root slack

Write

\[
                         C_r=\operatorname {Cat}_r.
\]

For an oriented `D_r`-port path factor, take the outgoing incidence
matching from

\[
 \binom{[2r]}r\setminus\overline{D_r}
        \quad\hbox{to}\quad\binom{[2r]}{r+1}.
\tag{1.1}
\]

The ballot theorem proves that exactly

\[
 Z_r={r-1\over r+2}\binom{2r}{r-1}
     ={r(r-1)\over r+2}C_r
\tag{1.2}
\]

cores `K` have all `r+1` extensions in the domain. Each corresponding
functional digraph contains a directed cycle of length at least three.
Greedy selected-edge disjointness gives (0.1).

Let

\[
                         D_r^{\rm car}=\kappa_r{C_r\over r^{3/2}},
 \qquad 0<c\le\kappa_r\le C<\infty,
\tag{1.3}
\]

be the required useful carrier mass. Then

\[
 {D_r^{\rm car}\over M_r}
 \le \kappa_r{(r+1)(r+2)\over(r-1)r^{3/2}}
 = {\kappa_r\over\sqrt r}\left(1+O(r^{-1})\right).
\tag{1.4}
\]

Consequently, if a fraction `f_r` of the certified bank becomes legal and
each retained certificate contributes useful gain at least `g_r`, the raw
numerical requirement is only

\[
 \boxed{
        f_rg_r\ge {\kappa_r+o(1)\over\sqrt r}.}
\tag{1.5}
\]

The square-root slack in (1.5) is the precise positive content of the new
count.

## 2. When a certificate is a genuine clean strand circuit

Fix one eligible `(r-1)`-core `K`. For every `a` outside `K`, write its
selected outgoing edge as

\[
                         K+a\longrightarrow K+a+b(a)
\tag{2.1}
\]

and draw the functional arc `a->b(a)`. A directed cycle

\[
                         a_0\to a_1\to\cdots
                         \to a_{\ell-1}\to a_0
\tag{2.2}
\]

lifts to the alternating **matching** certificate

\[
 K+a_i\;--\;K+a_i+a_{i+1}\;--\;K+a_{i+1}.
\tag{2.3}
\]

The first half of every two-edge segment belongs to the outgoing
matching. The second half need not be absent from the full path factor.

### Definition 2.1 (successor arc)

Let the old path containing `X=K+a` have next lower state

\[
                         X^+=X-x+b(a),
\tag{2.4}
\]

where its selected outgoing edge is `X -> X+b(a)`. Call the arc
`a->b(a)` a **successor arc at K** when

\[
                         K+b(a)=X^+.
\tag{2.5}
\]

Equivalently, `x=a`.

### Lemma 2.2 (one bad core per outgoing edge)

For every selected outgoing edge `X -> X+b`, exactly one of the `r` cores

\[
                         K_x=X\setminus\{x\},\qquad x\in X,
\]

makes its functional arc a successor arc: the core obtained by deleting
the coordinate removed at the old down-step.

#### Proof

The old successor is `X-a+b` for one unique `a in X`. For the core
`K_x=X-x`, the other lower endpoint proposed by the functional arc is
`K_x+b=X-x+b`. This equals the old successor exactly when `x=a`.
\(\square\)

### Lemma 2.3 (clean-strand criterion)

A directed cycle (2.2) uses distinct old path strands if and only if it
contains no successor arc. In that case (2.3) is a genuine alternating
circuit of the full path factor, all selected edges have coherent forward
orientation, and toggling it gives a root-to-sink path cover with cyclic
endpoint twist.

#### Proof

Suppose two lower states `K+a_i,K+a_j` lie on one old complement
geodesic. Two lower states at phases `s<t` on such a geodesic have Johnson
distance `t-s`. The displayed states have distance one, so they must be
consecutive phases. The outgoing edge from the earlier state then has the
later state as its old down-successor. Since a functional cycle uses the
unique outgoing arc, this is a successor arc.

Conversely, a successor arc joins two consecutive lower states of one old
path, so the strands are not distinct. Thus avoidance is equivalent to
the clean distinct-strand condition. When it holds, every proposed second
half-edge is absent from the old factor, and the cycle alternates between
old and new edges. All old selected edges are outgoing `X->Y` edges and
therefore coherently oriented. The clean strand theorem then gives a path
cover and the cyclic tail permutation. \(\square\)

The lemma isolates exactly what the ballot count does not control.

There are `rC_r` outgoing edges in (1.1), hence `rC_r` successor
edge--core incidences before restriction to eligible cores. Since

\[
                         Z_r=(1+o(1))rC_r,
\tag{2.6}
\]

the available count is consistent with one successor obstruction in the
unique directed cycle of every eligible core. This does not construct such
a factor, but it proves that the ballot and incidence counts alone cannot
yield a positive clean fraction. A separate avoidance theorem is required.

## 3. Phase defects and the fixed-exterior geodesic obstruction

Let a clean cycle use old paths `P_0,...,P_(ell-1)`, each of common old
incidence length `L`. Let `p_i` be the number of old incidence edges before
the selected edge on `P_i`. With a consistent cyclic indexing, the switched
path rooted at `P_(i+1)` receives the old suffix of `P_i`, and therefore has
length

\[
                         L+p_{i+1}-p_i.
\tag{3.1}
\]

The length-defect vector is consequently a cyclic coboundary and satisfies

\[
                         \sum_{i=0}^{\ell-1}(p_{i+1}-p_i)=0.
\tag{3.2}
\]

In particular, equal phase `p_i` makes one copy an equal-length **abstract
twisted path cover**. It does not make it a fixed-exterior geodesic factor
unless the twist fixes the relevant port.

### Proposition 3.1 (fixed-exterior twist obstruction; corrected)

Let one proposed \(r\)-step slab have fixed exterior \(O\), local
coordinate set \(J\), and endpoints

\[
 A=O\cup P,\qquad B=O\cup(J\setminus\tau(P)).
\tag{3.3}
\]

Then it is a Johnson geodesic only if 

\[
                         \tau(P)=P.
\tag{3.4}
\]

Consequently no serial product, including a finite-order product whose
total twist is the identity, can contain a nonidentity fixed-exterior
twisted slab as a contiguous part of one complement geodesic.

#### Proof

The endpoints have intersection

\[
 |A\cap B|=|O|+|P\cap(J\setminus\tau(P))|
          =m-|P\cap\tau(P)|,
\]

so \(d_J(A,B)=|P\cap\tau(P)|\). An \(r\)-step path is geodesic only when
this distance is \(r\), which is equivalent to (3.4). Every contiguous
segment of a global Johnson geodesic is geodesic: replacing a longer-than-
distance segment by a shortest segment would shorten the global path.
Therefore later slabs cannot cancel the positive metric defect of the
present slab. \(\square\)

The algebraic facts that the endpoint permutation has finite order and
that (3.2) telescopes remain true for an abstract serial ledger. They do
not imply physical geodesicity.

For comparison, let the exterior move. If

\[
 |O_L|=|O_R|=m-r,\qquad e=|O_L\setminus O_R|,
\]

then direct intersection counting gives

\[
 d_J(O_L\cup P,O_R\cup(J\setminus\tau(P)))
   =e+|P\cap\tau(P)|.
\tag{3.5}
\]

Thus an \(r\)-step packet is geodesic exactly under (0.5). Under equality,
the deletion and insertion menus are respectively

\[
 (O_L\setminus O_R)\mathbin{\dot\cup}(P\cap\tau(P)),
 \qquad
 (O_R\setminus O_L)\mathbin{\dot\cup}
       (J\setminus(P\cup\tau(P))).
\tag{3.6}
\]

These row-dependent menus are additional physical data, not a consequence
of the clean-cycle certificate.

## 4. Abstract carrier summation and its physical scope

Let `Delta_C` be the complete signed physical carrier vector of one clean
certificate in an abstract serial ledger. Let `T_j` be the formal transport
from the first carrier space to copy `j`.

If

\[
                         T_{j*}\Delta_C=\Delta_C
                 \qquad(0\le j<\ell),
\tag{4.1}
\]

then the closed serial atom has carrier vector

\[
                         \ell\Delta_C.
\tag{4.2}
\]

Thus the **abstract additive ledger** has no per-copy loss under (4.1).
More generally its authoritative vector is

\[
                         \sum_{j=0}^{\ell-1}T_{j*}\Delta_C.
\tag{4.3}
\]

Equation (4.3), not the order of the endpoint permutation, determines the
abstract carrier sum. It has physical meaning only after every copy is
realized by an exterior-moving geodesic satisfying (0.5), and after the
transported phase-defect vectors, ambient carriers, and collars are shown
to be the claimed \(T_j\)-images. Ordinary path reversal can send an
antisymmetric carrier to its negative; complement reversal is
sign-preserving only under the separately unproved lower-rainbow condition.

There is no valid scalar replacement obtained by dividing a single-copy
gain by a nominal serial loss. The quantity that must be charged is the
actual signed group gain

\[
 \left\langle z,\sum_jT_{j*}\Delta_C\right\rangle
\tag{4.4}
\]

per consumed physical group resource. Serial order supplies no free
capacity amplification: \(\ell\) useful copies also consume \(\ell\) stage
incidences.

## 5. Edge disjointness is not joint switchability

The cycles in (0.1) are disjoint only in their selected outgoing matching
edges. They may:

* use different selected edges of the same old path;
* meet the same path in different certificates;
* revisit the same old strand at different phases;
* induce noncommuting tail permutations; or
* create a joint strand component larger than either certificate.

The selected outgoing edges form a matching, so selected-edge-disjoint
certificates do not share those selected vertices. They can nevertheless
revisit an old strand at different phases. Without a cycle-length bound,
a naive row-disjoint extraction can lose up to \(O(r^2)\), already larger
than the square-root slack in (1.4). The explicit suffix-\(C_8\) bank in
the corrected later theorem avoids this particular supply problem for the
canonical factor, but not the exterior-moving or carrier problems.

A viable theorem must instead provide one of:

1. a switch-stable serial ordering whose strand effects compose exactly;
2. a bounded-congestion joint strand diagram with an integral routing
   theorem; or
3. a stronger extraction retaining at least the fraction in (1.5) after
   all path conflicts are removed.

This is why the new supply theorem is important but not yet the missing
construction theorem.

## 6. The corrected physical local lemma

### Exterior-moving carrier extension `EMCE_r(kappa)` -- **UNPROVED**

For a `D_r`-port factor at the relevant parent-visible scale, start with a
proved clean bank. For the canonical factor, the corrected suffix-\(C_8\)
theorem supplies \(C_{r-3}\) pairwise row/vertex-disjoint clean routers, so
successor avoidance is not the primary supply gate there. Extract and
extend packets satisfying all of the following.

1. **Strand legality.** Every retained toggle is a genuine full-factor
   alternating circuit, not merely an outgoing functional cycle.
2. **Exterior-moving geodesicity.** Every moved row comes with explicit
   exteriors \(O_L,O_R\) satisfying
   
   \[
       |O_L\setminus O_R|=|P\setminus\tau(P)|,
   \tag{6.1}
   \]
   
   and its complete state sequence realizes the menus (3.6). Every seam
   and every crossing window is literal.
3. **Serial closure after local geodesicity.** Only after Item 2 is
   verified may packets be grouped serially. In every group the transported
   twist product is the identity, the phase-defect vectors are transported
   equivariantly, and the complete `X/Y` ledgers remain exact.
4. **Joint compatibility.** Overlaps are handled by one joint strand atlas;
   selected-edge disjointness is not substituted for row or port
   compatibility.
5. **Carrier amount and sign.** With the complete physical row/start
   carrier vectors, collars, and actual unaffected background, one common
   choice across all protected depths has the required useful hinge gain,
   while all collateral and exceptional losses are lower order.
6. **Actual resource normalization.** The numerator is the signed group
   gain (4.4), and the denominator is the number of consumed physical
   parent incidences. Finite order itself receives no capacity credit.

The often quoted target

\[
                         C_r/r^{3/2}
\tag{6.2}
\]

is useful only when an independent parent ledger proves that this is the
demand in the same local units. The known one-context plateau demand can
be \(\Theta(C_r)\); in that normalization a unit-gain bank of order
\(C_r/r\) is a factor \(r\) short. Thus (1.4) is a conditional scalar
comparison, not a constant-one implication.

`EMCE_r` is not the final MWB lemma. Its physical groups must still pass
the global balanced-hinge dual and target-specific integral rounding gate.

## 7. Audit against the current obstructions

* **No `C_4` moves.** The clean banks use circuits of length at least six.
* **Wrong monodromy.** Serial identity is imposed only after every slab
  separately passes (6.1); it cannot repair a metric defect.
* **Mirror sign loss.** The carrier sum (4.3) is explicit and must be
  coherently positive.
* **First-edge Hall failure.** The starting object is an already exact port
  factor; no inference from a balanced prefix is used.
* **Bounded-seed inactivity.** A constant-width \(C_8\) router has only
  \(o(W)\) Gaussian action. A useful atlas must be extensive in the actual
  parent carrier normalization.
* **Component overlap.** Joint switch-stability is an explicit clause.
* **Unsigned orientation.** Useful hinge gain, not cycle count or component
  variance, is required.
* **Simultaneous depths.** One common choice and the full row/start tensor
  are required.
* **Literal realizability.** Exterior-distance equality, statewise menus,
  serial seams, endpoint complements, collars, and both ownership ledgers
  are explicit hypotheses.

None of these clauses follows from the ballot count. In particular, its
cycle bank remains an abstract \(b\)-factor/path ledger until Item 2 is
proved.

## 8. Final boundary

The corrected frontier is

\[
 \boxed{
 \text{abstract cycle abundance is proved; physical promotion requires}
 \\[-1mm]
 \text{rowwise exterior motion and a full carrier/collar extension.}}
\tag{8.1}
\]

Strand admissibility plus finite order do **not** meet the physical carrier
demand. What remains is the exterior-moving, extensive, quota-directed
carrier extension `EMCE_r`, followed by the global hinge and rounding
theorem.
